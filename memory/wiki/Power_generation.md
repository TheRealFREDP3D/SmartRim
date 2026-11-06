# Power generation (verified against game source)

Source of truth: decompiled `Assembly-CSharp.dll` and Defs from RimWorld
**1.6.4850 rev645**, indexed with RimSage. This page records what the code
actually does, not what a guide claims. Page last verified 2026-11-05.

## Quick reference

| Building | Output / storage | Size | Cost | Research | Terrain |
|---|---:|---:|---|---|---|
| Wind turbine | 2300 W (max) | 7×2 | 100 steel, 2 components | Electricity | Heavy |
| Solar generator | 1700 W (max, daylight) | 4×4 | 100 steel, 3 components | SolarPanels | Medium |
| Wood-fired generator | 1000 W | 2×2 | 100 steel, 2 components | Electricity | Medium |
| Geothermal generator | 3600 W | 6×6 | 340 steel, 8 components | Geothermal | Heavy |
| Battery | 600 Wd storage | 1×2 | 70 steel, 2 components | Batteries | Medium |
| Cooler | −200 W | 1×1 | 90 steel, 3 components | — | Medium |

Def names: `WindTurbine`, `SolarGenerator`, `WoodFiredGenerator`,
`GeothermalGenerator`, `Battery`, `Cooler`, `PowerConduit`.

## Wind turbine

`RimWorld/CompPowerPlantWind.cs`, `RimWorld/WindTurbineUtility.cs`.

- Base output **2300 W**, def field `basePowerConsumption = -2300`.
- Effective output:

  ```
  output = 2300 × min(windSpeed, 1.5)
  ```

  `windSpeed` comes from `Verse/WindManager.cs` and ranges **0.04–2.0**
  (`WindSpeedRange = FloatRange(0.04f, 2f)`), modified by weather and game
  conditions. Output is capped as if wind were 1.5, so above 1.5 there is no
  gain.
- **Clearance is much larger than the sprite.** `CalculateWindCells` builds a
  7-wide corridor:
  - rotation North/East: **10 cells in front**, **6 cells behind**;
  - rotation South/West: **6 cells in front**, **10 cells behind** (shifted one
    cell toward the front).
  That is a **7 × 16 footprint including the 7 × 2 turbine**, i.e. 112 cells
  that must stay clear.
- A cell blocks if it is **roofed** or if any thing on it has
  `def.blockWind` (trees, chunks, walls, most buildings).
- Each blocked cell costs **20% of the base output** (five blocked cells zero
  it). `RecalculateBlockages` re-runs periodically, so a new wall can silently
  kill production.
- Rotating the turbine 180° flips which side needs the long clearance.
- In a vacuum biome the turbine produces nothing.

Practical rule: find a 7 × 16 rectangle of buildable ground with no roofs and
no wind-blocking objects before placing it. Near a mature base this usually
means clearing trees/chunks or siting it away from the colony and running
conduits.

## Solar generator

`RimWorld/CompPowerPlantSolar.cs`.

```
output = 1700 × skyGlow × unroofedFraction
```

- `skyGlow` is 1.0 in full daylight, 0 at night.
- Each roofed cell of the 4×4 cuts output proportionally (`unroofedFraction`),
  so never roof it and keep it out of overhead mountain.
- No clearance corridor is required, unlike the turbine.

## Battery

`RimWorld/CompPowerBattery.cs`, `CompProperties_Battery`.

- Stores **600 Wd** per battery.
- **Efficiency 0.5**: `AddEnergy` multiplies incoming energy by 0.5, so
  **2 Wd of generation is needed per 1 Wd stored**.
- Self-discharge **5 W** while idle.
- `shortCircuitInRain = true`: an **unroofed battery can explode in rain or
  from fire**. Batteries belong in a roofed room; the warning "Unroofed
  electrical" is not cosmetic.
- Charging stops at `storedEnergyMax`; discharging floors at 0.

## Other generation

- **Wood-fired generator**: 1000 W, burns fuel, also emits heat
  (`CompHeatPusherPowered`). Good night-time baseline when wood is plentiful.
- **Geothermal generator**: 3600 W, 6×6, must be built on a steam geyser,
  cannot rotate.
- **Cooler**: draws 200 W; it raises room temperature on the exhaust side, so
  the exhaust must vent outdoors.

## Design implications

1. Turbines are cheap power but demand a 7 × 16 clear corridor; solar is more
   compact for a walled base but produces nothing at night.
2. Batteries are lossy (50%) and rain-sensitive. Roof them and treat stored
   watt-days as half of what you generated.
3. A typical stable early grid: one solar generator + one wood-fired generator
   + two roofed batteries (1200 Wd) covers a cooler and workshop loads without
   any clearance puzzle.
4. Conduits have no transmission loss; only batteries lose energy.
