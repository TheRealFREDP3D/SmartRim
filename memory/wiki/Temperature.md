Temperature - RimWorld Wiki
 
 
- 
- 
 
 

- 

- 
- 
- 
- 
- 
- 
- 
 

 
 

 
 

 

 Temperature

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 

Basics

Menus

Game&#160;Creation

Gameplay

Pawns

Plants

Resources

Gear

Mods

Menus

Architect

Work

Schedule

Assign

Animals

Wildlife

Research

Quests

World

History

Factions

Menu

Architect&#160;Menu

Orders

Zone

Structure

Production

Furniture

Power

Security

Misc

Floors

Recreation

Ship

Temperature

Special

Ideology (Buildings)

Biotech (Buildings)

Anomaly (Buildings)

Odyssey (Buildings)

Contents

- 1 Measuring temperature

- 2 Outdoors vs indoors

- 3 Thermodynamics

- 4 Summary

- 4.1 Crops

- 4.2 Food

- 4.3 Creatures

- 4.4 Fire

- 5 Managing temperature

- 5.1 Temperature thresholds

- 6 Cooling buildings

- 6.1 Passive cooler

- 6.2 Cooler

- 6.2.1 Analysis

- 6.2.2 Adding coolers

- 7 Heating buildings

- 7.1 Campfire

- 7.2 Heater

- 8 Incidental heat

- 8.1 Generators

- 8.2 Steam geysers

- 8.3 Fire weapons

- 8.4 Body heat

- 8.5 Solar pinhole

- 8.6 Production buildings

- 9 Heat transfer

- 9.1 Vent

- 9.2 Doors

- 10 Temperature mechanics

- 10.1 Passive equalization

- 10.2 Active equalization

- 11 Version history

This article is suggested to be rewritten. Reason: Tone, conciseness, verification and mechanics. You can help the RimWorld Wiki by improving it.

Temperature management is an important part of a productive colony. Temperature mainly affects pawn thoughts, food and corpse spoilage, work bench operation speed, and plant growth. Severe heat or cold leads to pawn injury and eventual death from heatstroke or hypothermia.

Measuring temperature[edit]

Players can switch the in-game temperature to display in Celsius (°C), Fahrenheit (°F), or Kelvins (K). This Wiki will list values in both Celsius and Fahrenheit.

Internally, the game uses Celsius degrees (°C) for all temperature functions, such as "too hot" or "too cold" thoughts. As the game always rounds temperature to an integer ("whole number"), values reported in Fahrenheit are inaccurate by around 0.3°F. For reliable temperature values, and especially when modding, use Celsius or Kelvin.

The maximum temperature is 1,000&#160;°C (1,832&#160;°F) and the minimum is -273&#160;°C (-459.4&#160;°F), very close to absolute zero. The minimum temperature is not encountered during normal gameplay, but fires in small enclosed spaces can reach the maximum temperature.

Outdoors vs indoors[edit]

An area completely enclosed by walls, doors, and other impassable objects is considered a room, where colonists will automatically build roofing in unroofed tiles (unless otherwise designated). Tiles not inside of a room are considered "outdoors". 

Outdoors areas and >75% unroofed rooms will always have the outside temperature, no matter what. Outdoor temperature varies by latitude, time of day, day of the year, and biome. Unpredictable events like a cold snap, volcanic winter or heat wave can also change outdoor temperature unexpectedly. No amount of cooling or heating from buildings, even in development mode, will affect or change the outdoor temperature. The outdoors is simply treated as a very large room with a uniform temperature. Instead, only buildings with dedicated mechanics such as the climate adjuster and atmospheric heater can affect the temperature.

By turning a place from Indoors to Outdoors, it will instantly become the outdoors temperature. This is caused when any wall or door that borders the outside is destroyed or deconstructed. Buildings like doors and vents, as well as removing roof tiles, makes heat transfer faster. Removing roof tiles will cause temperatures to "equalize" with the outside. A room that is 75% roofed or less will remain at outdoors temperature.

Thermodynamics[edit]

All tiles within a room share the same temperature. 

A room's temperature is influenced by its roofing and the temperature of tiles adjacent to its walls. The temperature of two adjacent rooms are influenced by each other. This creates a gradient of temperature between the outside, the rooms of your colony, and a heat source such as a geyser or heater. 
Heat transfer with walls only occurs in cardinal directions. Thus the corners of rooms can be eliminated with minimal effect.
Open doors and open roofs will quickly "equalize" temperature to whatever's on the other side. Adding another layer of walls increases insulation, but only up to 2 layers of wall. Gaps between each layer will decrease the insulation, but still have an effect.

Larger rooms have more heat capacity: their temperature is more resistant to change than that of smaller rooms. Temperature equalization with the outside is proportional with a room's perimeter. A square-shaped room (shape with the lowest area:perimeter ratio) will lose heat slower than a thin, rectangular hallway of equivalent perimeter.

See the temperature mechanics section further down for more details.

Summary[edit]

Temperature has the following effects on:

Crops[edit]

All biomes have a listed growing season. Some are very short (or, in extreme cold, non-existent) and others are "year round". Crops will die, and colonists will avoid planting outdoors, if it isn't growing season. Many players pick their starting location based on this, with year round being the easiest option.

However, a year round climate is no guarantee of trouble-free farming experience. Just getting close to freezing will slow plant growth, reducing the output of crops. Moreover, climates that do not freeze tend to get very hot in the summer season, hot enough to kill crops in some instances. Cold snaps can drop the temperatures below freezing for short periods - but long enough to, again, kill crops.

The short-term solution is to immediately harvest everything to save what you can. The long-term solution is some sort of greenhouse, making use of temperature controlled indoor structures, walled and roofed, with heaters or coolers, sun lamps, and possibly hydroponics.

Food[edit]

Warm temperatures rot food, corpses, and certain plant matter like psychoid leaves and herbal medicine. Even "durable" foods like corn and rice will eventually rot away. Colder temperatures preserve food and corpses by slowing spoilage. Freezing temperatures stop spoilage entirely and preserve these items indefinitely. Coolers will preserve food, so colonists starting with Electricity will quickly want to build a dedicated room. When freezing a room, watch out for heat waves.

Fertillized eggs will be "ruined by temperature" when left long enough outside of its comfortable range of 0&#160;°C&#160;– 50&#160;°C (32&#160;°F&#160;– 122&#160;°F). "Ruined" eggs may still be eaten as normal, but won't hatch into an animal. In a similar vein, a fermenting barrel must be kept in a comfortable range between -1&#160;°C&#160;– 32&#160;°C (30.2&#160;°F&#160;– 89.6&#160;°F) for beer to be produced.

Deterioration is an entirely different mechanic, and items left outside will lose health regardless of temperature. Rotting isn't influenced by and has no effect on an item's hit points.

Creatures[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Burn/Frostbite chances.

Main articles: Heatstroke&#32;and&#32;Hypothermia

Pawns have a Maximum Comfortable Temperature and Minimum Comfortable Temperature. Going over 10&#160;°C (18&#160;°F) beyond these limits will start giving them heatstroke or hypothermia. The further above or below this 10&#160;°C (18&#160;°F) limit the faster the Heatstroke or Hypothermia rises. At 150&#160;°C (270&#160;°F) above their comfortable temperature range, creatures will begin to take burn damage. If Hypothermia reaches a severity of 37% and the pawn is in a location at 0&#160;°C (32&#160;°F) or below, there is a chance the pawn takes Frostbite damage. The higher the Hypothermia severity the higher the chance of Frostbite damage. Insectoids will experience hypothermic slowdown instead of hypothermia. Pawns will also receive negative moodlets based on how extreme the temperature is. The Gear tab shows aggregate stats about comfy temperatures.

Hypothermia and Heatstroke are both fatal at 100% severity. Though, both Heatstroke and Hypothermia have significant health consequences and can lead to death before the 100% severity level is reached.

For humans, apparel will increase both comfortable thresholds, depending on the apparel type and material (e.g. wool parkas insulate well against cold). Colonists will try and wear items suitable for the temperature, unless they are forced otherwise. Colonists' moods ignore apparel when considering sleeping moodlets. So piling on the warmest apparel doesn't avoid a "Slept in the cold" bad thought if a bedroom is not adequately heated.

Animals tend to have much higher comfortable thresholds. However, in extreme biomes, it may be necessary to build a "barn" of some sort with temperature control and designate indoor animal sleeping spots to keep your herd warm/cool.

Many work benches, such as a electric stove or stonecutter's table, have a comfortable range between 10&#160;°C&#160;– 35&#160;°C (50&#160;°F&#160;– 95&#160;°F). Above or below this range, the bench's work speed is multiplied by 70%.

Fire[edit]

Main article: Fire

Fire is a destructive force capable of destroying plants, buildings, and pawns alike. Pawns and items can spontaneously ignite when temperature is at or above 235&#160;°C (455&#160;°F). Fires can spread via embers from up to 2 tiles. 

Fire itself provides a massive amount of heat.

Managing temperature[edit]

Temperature management is important for any colony, regardless of climate. It can be simply managed with a good power supply and the following structures. Temperature changing buildings will still work while "outdoors", but have no noticeable effect.

Temperature thresholds[edit]

Temperature
Effects

1,000&#160;°C (1,832&#160;°F)
Maximum value

~235&#160;°C (455&#160;°F)
Items spontaneously catch fire

60&#160;°C (140&#160;°F)
Maximum comfortable temperature of any animal (Dromedary / Insectoids / Iguana)

58&#160;°C (136.4&#160;°F)
Plant growth stopped.

42&#160;°C (107.6&#160;°F)
Above this value Plant growth slowed.

35&#160;°C (95&#160;°F)
At this temperature and above work benches show "Bad temperature" and Work Speed is reduced to 70%.

30&#160;°C (86&#160;°F)
Campfire max temperature

26&#160;°C (78.8&#160;°F)
Default human upper comfort limit without clothing modifiers.
Sleeping above this temperature creates "Slept in the heat" thought in baseline humans.

23&#160;°C (73.4&#160;°F)
Torch lamp/Fungus darktorch/Darktorch/Brazier/Darklight brazier max temperature

21&#160;°C (69.8&#160;°F)
Heater and Cooler default target

17&#160;°C (62.6&#160;°F)
Passive cooler min temperature

16&#160;°C (60.8&#160;°F)
Default human lower comfort limit without clothing modifiers.
Sleeping below this temperature creates "Slept in the cold" thought in baseline humans.

10&#160;°C (50&#160;°F)
Below this value food spoiling slowed.
Food spoiling between 10C and 0C is multiplied by a factor of (Temp)/10, in Celsius.
Below this value work benches show "Bad temperature" and Work Speed is reduced to 70%.

9&#160;°C (48.2&#160;°F)
Food spoiling rate multiplied by a factor of 0.9, or time to spoil multiplied by 1.11.

8&#160;°C (46.4&#160;°F)
Food spoiling rate multiplied by a factor of 0.8, or time to spoil multiplied by 1.25.

7&#160;°C (44.6&#160;°F)
Food spoiling rate multiplied by a factor of 0.7, or time to spoil multiplied by 1.43.

6&#160;°C (42.8&#160;°F)
Food spoiling rate multiplied by a factor of 0.6, or time to spoil multiplied by 1.66.
Below this value plant growth slowed.

5&#160;°C (41&#160;°F)
Food spoiling rate multiplied by a factor of 0.5, or time to spoil multiplied by 2.

4&#160;°C (39.2&#160;°F)
Food spoiling rate multiplied by a factor of 0.4, or time to spoil multiplied by 2.5.

3&#160;°C (37.4&#160;°F)
Food spoiling rate multiplied by a factor of 0.3, or time to spoil multiplied by 3.33.

2&#160;°C (35.6&#160;°F)
Food spoiling rate multiplied by a factor of 0.2, or time to spoil multiplied by 5.

1&#160;°C (33.8&#160;°F)
Food spoiling rate multiplied by a factor of 0.1, or time to spoil multiplied by 10.

0&#160;°C (32&#160;°F)
Plant growth and food spoiling stopped.
Toxic wastepacks do not dissolve. (They can still deteriorate)

-10&#160;°C (14&#160;°F)
Most plants die.

-65&#160;°C (-85&#160;°F)
Minimum comfortable temperature of any animal (Thrumbo)

-75&#160;°C (-103&#160;°F)
Outdoor temperature in Orbit above the planet

-273&#160;°C (-459.4&#160;°F)
Minimum value.

Cooling buildings[edit]

Passive cooler[edit]

The passive cooler is a very low-tech option automatically unlocked for all default starts. They operate at the same strength as a Cooler and will cool rooms to a very comfortable 17&#160;°C (62.6&#160;°F). Passive coolers last for 5 days; it needs to be fueled with wood when it runs out of fuel. Due to the temperature limit, passive coolers are unable to preserve food.

Passive coolers are a life saver in extremely hot climates as they can be quickly built, are immune to electrical events and are easily massed in a heat wave. Use passive coolers to keep your living spaces survivable and chill rooms surrounding a freezer to further protect the products inside.

Cooler[edit]

The cooler is primarily used to lower the temperature of a room. It has two states of power consumption: low and high. In its low state, the cooler produces no heat or cold but still requires 20 W. It can be used to lower the temperature of a room to a comfortable 20&#160;°C (68&#160;°F) (room temperature) in the summer or create a walk-in freezer for your food. In hot biomes such as desert or rainforest, having comfortable air conditioning is a necessity for any base.

Coolers are heat pumps that produce both a cold side and a hot side. The hot side is rarely useful and should be directed to an outdoor space (or a 1x1, unroofed room) to not inconvenience your colony. The heating side is useful when outdoors temperature is uncomfortable, but not freezing. This is between 1&#160;°C&#160;– 16&#160;°C (33.8&#160;°F&#160;– 60.8&#160;°F), but in practical terms, you should point the heat side at the colony when the outdoors temperature rarely goes above 20&#160;°C (68&#160;°F). Never block a cooler's intake or exhaust port, or else it won't function. 

A cooler is theoretically able to cool a single square by about 1800 kelvin [K]. But this is not a linear relation, as a room always exchanges heat with adjacent rooms and/or the outside.

Analysis[edit]

Electric coolers are the only way to create freezers. Building one is as simple as making a room and replacing some wall tiles with coolers. Direct the cold "blue" zone of the cooler inside the room and the hot "red" tile to an outdoor area. Reduce the cooler's target temperature to below 0&#160;°C (32&#160;°F). As the room cools down any food left inside will decay more slowly until it freezes. Frozen food will stay fresh indefinitely and incurs no other benefit or penalty when eaten.

If your freezer area is more than about 50 squares, and/or you are living in an area with a hot summer, you will want 2 coolers (and perhaps more, see "adding coolers", below). Put one at 0, and the other at -2. With double walls, this will let one cooler "idle" at 20 W of power in cooler weather while the other easily keeps things frozen, but be available to help when needed for warmer weather. Batteries are useful for power outages; you may want to keep charged batteries disconnected via power switch for these situations.

Freezers lose heat through walls and doors. The material of a wall doesn't matter, but for maximum insulation, you should put a double layer of them. Doors will cause heat loss when opened. This loss can be offset by having doors arranged in sequence, one after another, at points of egress, in an "airlock" like fashion. The loss can be examined by mousing over the sections of the airlock to see the temperature. Using doors rather than autodoors can help reduce the cooling lost, though this slows down colonists. 

Adding coolers[edit]

There may come a moment when you realize "I don't have enough coolers for this area...". If the weather is cool, that's not a big problem, but it's more likely that the weather will be brutally hot when you realize this. And it's also likely that it's your freezer that's not at "freezing" (since colonists can tough it out). If you open a wall to put in an additional cooler, your freezer immediately rockets to "outside" temperatures - which is probably a dealbreaker, rotting all your frozen items. So here's what you do...

Decide where in the current wall you will put your new cooler, and build a door outside where you will tear the existing wall down (you don't need "side walls" to support it). (A wall would "block" the cooler exhaust and prohibit construction, but a door will not!) Then, [f]orbid the door (so it doesn't get opened), and deconstruct your wall; the new door will maintain the area as "inside". Then build your cooler (remembering the orientation, warm side "out"). Once the new cooler has been installed, deconstruct the door, and you're done.

Heating buildings[edit]

Campfire[edit]

Campfires are a quick and dirty solution to produce heat in a hurry. They require no energy, but are temporary structures and must be refreshed with wood every few days. Otherwise, they produce the same amount of heat as an electrical heater. They cannot raise the temperature to over 30&#160;°C (86&#160;°F). They can't be controlled, so may make pawns uncomfortably hot - open doors or roofs to lower heat.

Heater[edit]

The heater is used to raise the temperature of a room. It has two states of power consumption: low and high. In its low state, the heater produces no heat but still requires 18 W. It can be used to raise the temperature of a room to a likable 20&#160;°C (68&#160;°F) (room temperature) in the winter or create a walk-in heat trap for your foes. In any cold biome, such as the Tundra, the heater is a necessity for any base.

A heater (in theory) is able to heat a single square by about 1800 kelvin [K]. But this is not a linear relation as a room always exchanges heat with adjacent rooms and/or the outside. This heat conduction effect can be pretty noticeable in extremely cold or hot environments.
Example: In a realistic setup, this means it can heat a room with 50 squares by an average of about 36 K per square.
So a room with 50 squares and an outside temperature of -10&#160;°C (14&#160;°F) can be heated up to comfortable 26&#160;°C (78.8&#160;°F) or something near that with a single heater.

Incidental heat[edit]

Generators[edit]

Generators produce a non-negligible amount of heat for the room they occupy, especially when placed in numbers.
If placed strategically, you can reduce the number of heaters and coolers necessary to manage the temperature in your base.

It's also worth noting that generators will continue to produce heat (and burn fuel) during solar flare events. If your colony is in a very cold climate, this can be used to ensure that critical sections such as hydroponics or barns for sensitive animals don't lose all their heat in a power outage.

Steam geysers[edit]

A steam geyser will heat up a roofed room even when covered with a geothermal generator. They are extremely useful for staying warm in frozen climates, but can overheat an indoors space in warmer biomes.

Fire weapons[edit]

Weapons that generate fire such as molotov cocktail and incendiary launcher can be used to quickly generate heat inside your colony. Under normal conditions this is a bad idea because fires will quickly bring your base to intolerable temperatures. However in a bitter arctic climate with no wood and inadequate heaters, these weapons are your last defense against freezing to death. Draft your colonist and force them to open fire on an empty space, or burn spare corpses and rags to increase heat output.

Body heat[edit]

Living, organic creatures (excludes mechanoids, drones, nociospheres, fleshmass nuclei, metal horrors, revenants) generate a small amount of heat directly proportional to their body size as long as the ambient temperature is not above 40°C. The heat pushed follows the formula:

- 0.3 * Body Size * 4.1666665 ≈ 1.25 * Body Size for human pawns

- 0.3 * Body Size * 4.1666665 * 0.6 ≈ 0.75 * Body Size for all others

Heating is inconsistent, as creatures are prone to wandering, population and sizes fluctuate with births, culling, and growth, and livestock are frequently left in outdoor pens where heat will dissipate.

Solar pinhole[edit]

This section relates to content added by Royalty (DLC). Please note that it will not be present without the DLC enabled.

Solar pinhole is a psycast that creates heat and light. It lasts five days. It is useful for emergency situations, such as power shortages during cold snaps.

Production buildings[edit]

Certain production buildings generate heat while executing bills: Electric smelters at a rate of 9 heat per second, Electric crematoria at a rate of 12 heat per second, Fueled stoves at a rate of 4 heat per second, Electric stoves at a rate of 3 heat per second.

Heat transfer[edit]

Vent[edit]

A vent allows transfer of temperature and gases from one room to another.

Vents can have any building in front of it, but no walls. Vents work best when connecting directly to a climate controlled room. Trying to chain vents across smaller rooms will lead to each successive room getting less effective climate control, and connecting to a hallway won't work well if the hallway is blocked with doors. A vent can be designated to be closed, an action carried out by colonists assigned to Basic.

Doors[edit]

Similar to double thick walls, double doors (not side-by-side, rather, both in the path of travel) improve insulation and reduce temperature equalization.
A door can be left permanently open (mark the door to 'hold open' and have a pawn pass through) to help control temperature. Open doors allow temperature to more quickly equalize between rooms or the outdoors. Equalization through open doors is less potent than vents.

Temperature mechanics[edit]

Equalization calculations happens once every 120 game ticks.

Temperature seems to be measured to an extreme precision.

Passive equalization[edit]

This is equalization via walls and roofs.

Walls will equalize towards the room on the other side. This can be another fully realized room or simply the outdoors. If the other side is not outdoors, that room will also equalize towards this room. 

- The material of the walls does not matter. Wood is as insulating as any stone or metal. And unmined rocks are equally effective.
- A 2nd layer halves the temperature equalization via walls. Extra wall layers have no effect.

- Nutrient dispensers are one of the few items working fully like walls for equalization purposes.

- The surface area does matter. Basically, the game is using a 2D variant of the square-cube law, with walls taking the place of "surface area" and room size taking the place of "volume". As such square rooms are the most efficient at keeping temperatures.
- Furniture lowers the room size and therefore might change the rate of equalization.

Example of equalization values at -9555.208°C[Check] difference for:

Room
Single wall
Double wall

1x1
-161.470°C
-81.234°C

2x2
-81.235°C
-40.617°C

3x3
-54.157°C
-27.078°C

4x4
-40.618°C
-20.309°C

5x5
-32.494°C
-16.247°C

6x6
-27.078°C
-13.539°C

7x7
-23.210°C
-11.605°C

Roof is a major part with equalization with the outdoor temperature. It will always equalize with the outdoor temperature, regardless what the room borders. However, the equalization rate is also constant for all room sizes at the same temperature difference. There are 4 basic types of roof:

- Unroofed tiles are looked at in relation to the total count of roofed tiles in a room. With at least 1/4 unroofed the room will simply equalize to outdoor temperature on the next tick.

- Thin roof (constructed roof and thin rock): at a temperature difference of -9,555.208&#160;°C (-17,199.4&#160;°F) it equalizes by -57.331&#160;°C (-103.2&#160;°F) every 120 ticks.

- Thick rock does not equalize temperature with the outdoors at all, and has a passive cooling effect if the indoor temperature is 15&#160;°C (59&#160;°F) or above; however this effect is extremely small compared to other sources.

Active equalization[edit]

While Vents, Coolers and open doors still keep rooms separated, they also equalize temperature at a very high rate. This rate is unfortunately not shown on any tooltip.

Torches, Campfires, Heaters and Passive coolers will directly modify the room temperature instead, adding/removing heat every equalization tick as appropriate for their settings/current state.

Version history[edit]

- 0.13.1135 - Deep rooms stay cooler in the heat.

- Beta 19/1.0.0 - Equalized mood penalties for being too hot and too cold.

- 1.3.3066 - Fix: Changing temperature display mode (C to F) doesn’t update temperature readout immediately.

Architect

Temperature
Campfire &#8226; Heater &#8226; Cooler &#8226; Passive cooler &#8226; Vent

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Temperature&oldid=184101"

 Categories: - Pages to be rewritten
- Stubs
- Game mechanics
- Buildings

Hidden category: - Pages that need fact checking

 

 Navigation menu

 
 

 
 Personal tools
 

 
 
 
 - Not logged in
- Talk
- Contributions
- Create account
- Log in

 
 

 
 

 
 Namespaces
 

 
 
 
 - Page
- Discussion

 
 

 

 
 
 Variants
 

 
 
 
 
 
 

 

 
 

 
 Views
 

 
 
 
 - Read
- Edit
- View history

 
 

 

 
 
 More
 

 
 
 
 
 
 

 
 
 Search
 

 
 
 
 
 
 
 

 

 

 

 

 
 
 

 

 
 RimWorld
 

 
 
 
 - Official Site
- Official Twitter
- Subreddit
- Community Discord

 
 

 

 
 Navigation
 

 
 
 
 - Main page
- Recent changes
- Random page

 
 

 

 
 Tools
 

 
 
 
 - What links here
- Related changes
- Special pages
- Printable version
- Permanent link
- Page information
- Browse properties

 
 

 

 
 - This page was last edited on 17 August 2026, at 00:36.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -