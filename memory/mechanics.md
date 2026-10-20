# Game Mechanics

## Wealth System
- Raid strength scales with colony wealth (total value of buildings, items, colonists, animals)
- Wealth counted toward raids caps at 1,000,000 storyteller wealth; raid points cap at 10,000 (wiki: Wealth, Raid_points, verified 2026-10-18)
- Classic new-player trap: hoard everything → wealth spikes → raids get harder → colony dies
- Rules: build only what you need, sell/process loot fast, upgrade defenses before warehouse

## Mood System
- Mental break thresholds (wiki: Mental_break, Mood; verified 2026-10-18), base values for a normal colonist:
  - Minor break threshold 35% (MTB ~4 days below it)
  - Major break threshold 20% (MTB ~0.8 days below it)
  - Extreme break threshold 5% (MTB ~0.5 days below it)
- Traits shift these: Iron-willed -18%, Steadfast -9%, Nervous +8%, Volatile +15%
- Base mood by difficulty: Peaceful/Community builder 42, Adventure story 37, Strive to survive 32, Blood and dust 27, Losing is Fun 22
- Mood bar moves toward its target at most +12/hour up and -8/hour down (wiki: Mood)
- Expectations: wealth sets a base mood bonus (+30 at 0-15k wealth down to 0 at 308k+) and the number of recreation types needed (2 to 6) (wiki: Wealth)
- Earlier notes (below 25% / below 10% / above 50% safe) were wrong and have been removed.
- Key mood boosters: fine meals, nice bedrooms, recreation variety
- Key mood drains: raw food, sleeping outside, dirt, darkness, corpses, pain

## Research
- Requires research bench + colonist assigned to research
- Speed depends on Intellectual skill and bench tier
- Key early techs: Electricity → Battery → Air Conditioning → Machining
- Mid-game: Microelectronics
- Late-game: Fabrication, Multi-analyzer

## Food
- Packaged survival meals: "~8 days for 3 pawns (50 meals)" is unverified against the wiki (Packaged_survival_meal page lists nutrition but not a duration); meals deteriorate slowly but do not expire (wiki)
- Rice: fastest crop, harvest in ~6 days
- Corn: slow but high yield
- Potatoes: average soil is fine
- Simple meals: cook raw food before eating (mood bonus)
- Freezer: below 0°C prevents all spoilage
- Nutrient paste dispenser: efficient early food, no cooking skill needed, requires Electricity research (wiki: Nutrient_paste)
- Main stockpile as freezer: prevents perishable spoilage (community tip)
- Cleanliness affects research speed, surgery success, food poisoning chance, gene assembler speed (wiki: Bedroom, Research)
- Turn off unused workstations to save power (community tip)

## Combat
- Cover: sandbags, rock chunks give hit penalties to enemies
- Focus-fire: select everyone, right-click one enemy at a time
- Draft: enables direct pawn control
- Aftermath: tend wounds, haul bodies, strip raider weapons

## Time Management
- RimWorld runs in real-time but pausing is free
- 3x speed is a self-inflicted difficulty spike
- Pause on every new event, read it, assign response, unpause

## Notes
<!-- Add new mechanic discoveries here with dates -->

### 2026-10-19 (run-002)
- **Smithing is its own work type**, separate from Crafting. Smithy bills (weapons, simple helmet) need Smithing enabled; a colonist on Crafting only will ignore them.
- **Work type order matters more than priority ties**: a priority-1 Cooking bill with repeat mode "forever" keeps a colonist at the stove all day. Use target counts (10-12 meals) so other work resumes.
- **Recipe costs**: longsword = 100 steel, simple helmet = 40 steel. Compacted steel tiles give ~40 steel each and sit next to the workshop on this map.
- **Modal dialogs force-pause the game** and make `wait_for_event` return `ticksWaited: 0` with the same hour. `list_windows` shows them (`forcePause: true`); close with `window_action` before waiting again. "Research finished: X" is the common one.
- **`get_resource_readout` counts stored items only.** Harvested rice/berries lying in the field are invisible until hauled, and a full stockpile silently blocks hauling.
- **`daysPassed` = floor(ticksGame / 60000)**, so the run-length check fires 24 in-game hours after the previous increment, not at calendar midnight.
- **Quest colonists wander** without an allowed area; the Hunted Knight walked ~100 cells to a river and was downed by a manhunter rat.

### 2026-10-19 (run-002, player corrections)

Confirmed by the player after the run — these are ground truth, not inferences from snapshots:

- **Research cannot be queued in vanilla.** There is one active project and it is set by hand; the "Need research project" alert means the bench is idle. A multi-project queue is a mod feature, so the fix is deciding the next project in advance, not queueing.
- **A fire during a raid is arson.** The 12th Aprimay fire was lit by the raider, not by a wooden wall or a torch lamp. Firefighting is part of the battle, not cleanup afterwards.
- **Protection quests end when the target boards the shuttle** — the player had to order Antigonos into the vehicle when it landed next to the base. Until then he was a guest to keep alive, not a colonist to settle in; he had 18% mood and no weapon, and the "No acceptable food" alert was about his own restrictions.
- **The downing on 1st of Jugust happened before he joined**: he was chased and downed while still a quest guest, hence the rescue away from base.


