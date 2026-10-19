# Temperature

From RimWorld Wiki

Jump to navigation Jump to search

|  |  | [Basics](/wiki/Basics "Basics") | **Menus** | [Game Creation](/wiki/Game_Creation "Game Creation") | [Gameplay](/wiki/Gameplay "Gameplay") | [Pawns](/wiki/Pawns "Pawns") | [Plants](/wiki/Plants "Plants") | [Resources](/wiki/Resources "Resources") | [Gear](/wiki/Gear "Gear") | [Mods](/wiki/Mods "Mods")  
---|---|---|---|---|---|---|---|---  
[Menus](/wiki/Menus "Menus") | **Architect** | [Work](/wiki/Work "Work") | [Schedule](/wiki/Menus#Schedule "Menus") | [Assign](/wiki/Assign "Assign") | [Animals](/wiki/Menus#Animals "Menus") | [Wildlife](/wiki/Menus#Wildlife "Menus") | [Research](/wiki/Research "Research") | [Quests](/wiki/Quests "Quests") | [World](/wiki/Menus#World "Menus") | [History](/wiki/Menus#History "Menus") | [Factions](/wiki/Factions "Factions") | [Menu](/wiki/Menus#Menu "Menus")  
---|---|---|---|---|---|---|---|---|---|---|---|---  
  
[Architect Menu](/wiki/Architect "Architect") | [Orders](/wiki/Orders "Orders") | [Zone](/wiki/Zone/Area "Zone/Area") | [Structure](/wiki/Structure "Structure") | [Production](/wiki/Production "Production") | [Furniture](/wiki/Furniture "Furniture") | [Power](/wiki/Power "Power") | [Security](/wiki/Security "Security") | [Misc](/wiki/Misc "Misc") | [Floors](/wiki/Floors "Floors")  
---|---|---|---|---|---|---|---|---|---  
[Recreation](/wiki/Recreation "Recreation") | [Ship](/wiki/Ship "Ship") | Temperature | [Special](/wiki/Special "Special") | [Ideology (Buildings)](/wiki/Ideology_\(Buildings\) "Ideology \(Buildings\)") | [Biotech (Buildings)](/wiki/Biotech_\(Buildings\) "Biotech \(Buildings\)") | [Anomaly (Buildings)](/wiki/Anomaly_\(Buildings\) "Anomaly \(Buildings\)") | [Odyssey (Buildings)](/wiki/Odyssey_\(Buildings\) "Odyssey \(Buildings\)")  
---|---|---|---|---|---|---|---  
  
* * *

## Contents

  * 1 Measuring temperature
  * 2 Outdoors vs indoors
  * 3 Thermodynamics
  * 4 Summary
    * 4.1 Crops
    * 4.2 Food
    * 4.3 Creatures
    * 4.4 Fire
  * 5 Managing temperature
    * 5.1 Temperature thresholds
  * 6 Cooling buildings
    * 6.1 Passive cooler
    * 6.2 Cooler
      * 6.2.1 Analysis
      * 6.2.2 Adding coolers
  * 7 Heating buildings
    * 7.1 Campfire
    * 7.2 Heater
  * 8 Incidental heat
    * 8.1 Generators
    * 8.2 Steam geysers
    * 8.3 Fire weapons
    * 8.4 Body heat
    * 8.5 Solar pinhole
    * 8.6 Production buildings
  * 9 Heat transfer
    * 9.1 Vent
    * 9.2 Doors
  * 10 Temperature mechanics
    * 10.1 Passive equalization
    * 10.2 Active equalization
  * 11 Version history



[![Rewrite.png](/images/thumb/a/a3/Rewrite.png/40px-Rewrite.png)](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten") | This article is suggested to be [rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten"). **Reason:** Tone, conciseness, verification and mechanics. You can help the RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Temperature&action=edit)** it.__  
---|---  
  
**Temperature** management is an important part of a productive colony. Temperature mainly affects pawn [thoughts](/wiki/Thoughts "Thoughts"), food and corpse spoilage, work bench operation speed, and plant growth. Severe heat or cold leads to pawn injury and eventual death from [heatstroke](/wiki/Heatstroke "Heatstroke") or [hypothermia](/wiki/Hypothermia "Hypothermia"). 

### Measuring temperature[[edit](/index.php?title=Temperature&action=edit&section=1 "Edit section: Measuring temperature")]

Players can switch the in-game temperature to display in Celsius (°C), Fahrenheit (°F), or Kelvins (K). This Wiki will list values in both Celsius and Fahrenheit. 

Internally, the game uses Celsius degrees (°C) for all temperature functions, such as "too hot" or "too cold" [thoughts](/wiki/Thoughts "Thoughts"). As the game always rounds temperature to an integer ("whole number"), values reported in Fahrenheit are inaccurate by around 0.3°F. For reliable temperature values, and _especially_ when [modding](/wiki/Modding "Modding"), use Celsius or Kelvin. 

The maximum temperature is 1,000 °C (1,832 °F) and the minimum is -273 °C (-459.4 °F), very close to [absolute zero](https://en.wikipedia.org/wiki/absolute_zero "wikipedia:absolute zero"). The minimum temperature is not encountered during normal gameplay, but [fires](/wiki/Fire "Fire") in small enclosed spaces can reach the maximum temperature. 

### Outdoors vs indoors[[edit](/index.php?title=Temperature&action=edit&section=2 "Edit section: Outdoors vs indoors")]

An area completely enclosed by [walls](/wiki/Wall "Wall"), [doors](/wiki/Door "Door"), and other impassable objects is considered a [room](/wiki/Room "Room"), where colonists will automatically build [roofing](/wiki/Roof "Roof") in unroofed tiles (unless otherwise designated). Tiles not inside of a room are considered "outdoors". 

Outdoors areas and >75% unroofed rooms will always have the outside temperature, no matter what. Outdoor temperature varies by [latitude](/index.php?title=Latitude&action=edit&redlink=1 "Latitude \(page does not exist\)"), time of day, day of the year, and [biome](/wiki/Biome "Biome"). Unpredictable [events](/wiki/Events "Events") like a [cold snap](/wiki/Cold_snap "Cold snap"), [volcanic winter](/wiki/Volcanic_winter "Volcanic winter") or [heat wave](/wiki/Heat_wave "Heat wave") can also change outdoor temperature unexpectedly. No amount of cooling or heating from buildings, even in [development mode](/wiki/Development_mode "Development mode"), will affect or change the outdoor temperature. The outdoors is simply treated as a very large room with a uniform temperature. Instead, only buildings with dedicated mechanics such as the [climate adjuster](/wiki/Climate_adjuster "Climate adjuster")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and [atmospheric heater](/wiki/Atmospheric_heater "Atmospheric heater")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") can affect the temperature. 

By turning a place from Indoors to Outdoors, it will instantly become the outdoors temperature. This is caused when any wall or door that borders the outside is destroyed or deconstructed. Buildings like doors and vents, as well as removing roof tiles, makes heat transfer faster. Removing roof tiles will cause temperatures to "equalize" with the outside. A room that is 75% roofed or less will remain at outdoors temperature. 

### Thermodynamics[[edit](/index.php?title=Temperature&action=edit&section=3 "Edit section: Thermodynamics")]

All tiles within a room share the same temperature. 

A room's temperature is influenced by its roofing and the temperature of tiles adjacent to its walls. The temperature of two adjacent rooms are influenced by each other. This creates a gradient of temperature between the outside, the rooms of your colony, and a heat source such as a geyser or heater. Heat transfer with walls only occurs in cardinal directions. Thus the corners of rooms can be eliminated with minimal effect. Open doors and open roofs will quickly "equalize" temperature to whatever's on the other side. Adding another layer of walls increases insulation, but only up to 2 layers of wall. Gaps between each layer will decrease the insulation, but still have an effect. 

Larger rooms have more heat capacity: their temperature is more resistant to change than that of smaller rooms. Temperature equalization with the outside is proportional with a room's perimeter. A square-shaped room (shape with the lowest area:perimeter ratio) will lose heat slower than a thin, rectangular hallway of equivalent perimeter. 

See the temperature mechanics section further down for more details. 

## Summary[[edit](/index.php?title=Temperature&action=edit&section=4 "Edit section: Summary")]

Temperature has the following effects on: 

### Crops[[edit](/index.php?title=Temperature&action=edit&section=5 "Edit section: Crops")]

All [biomes](/wiki/Biome "Biome") have a listed growing season. Some are very short (or, in extreme cold, non-existent) and others are "year round". Crops will die, and colonists will avoid planting outdoors, if it isn't growing season. Many players pick their starting location based on this, with year round being the easiest option. 

However, a year round climate is no guarantee of trouble-free farming experience. Just getting close to freezing will slow plant growth, reducing the output of crops. Moreover, climates that do not freeze tend to get _very_ hot in the summer season, hot enough to kill crops in some instances. [Cold snaps](/wiki/Cold_snap "Cold snap") can drop the temperatures below freezing for short periods - but long enough to, again, kill crops. 

The short-term solution is to immediately harvest everything to save what you can. The long-term solution is some sort of greenhouse, making use of temperature controlled indoor structures, walled and roofed, with [heaters](/wiki/Heater "Heater") or [coolers](/wiki/Cooler "Cooler"), [sun lamps](/wiki/Sun_lamp "Sun lamp"), and possibly [hydroponics](/wiki/Hydroponics "Hydroponics"). 

### Food[[edit](/index.php?title=Temperature&action=edit&section=6 "Edit section: Food")]

Warm temperatures rot food, corpses, and certain plant matter like [psychoid leaves](/wiki/Psychoid_leaves "Psychoid leaves") and [herbal medicine](/wiki/Herbal_medicine "Herbal medicine"). Even "durable" foods like corn and rice will eventually rot away. Colder temperatures preserve food and corpses by slowing spoilage. Freezing temperatures stop spoilage entirely and preserve these items indefinitely. [Coolers](/wiki/Cooler "Cooler") will preserve food, so colonists starting with Electricity will quickly want to build a dedicated room. When freezing a room, watch out for [heat waves](/wiki/Heat_wave "Heat wave"). 

Fertillized [eggs](/wiki/Egg "Egg") will be "ruined by temperature" when left long enough outside of its comfortable range of 0 °C – 50 °C (32 °F – 122 °F). "Ruined" eggs may still be eaten as normal, but won't hatch into an animal. In a similar vein, a [fermenting barrel](/wiki/Fermenting_barrel "Fermenting barrel") must be kept in a comfortable range between -1 °C – 32 °C (30.2 °F – 89.6 °F) for [beer](/wiki/Beer "Beer") to be produced. 

[Deterioration](/wiki/Deterioration "Deterioration") is an entirely different mechanic, and items left outside will lose health regardless of temperature. Rotting isn't influenced by and has no effect on an item's hit points. 

### Creatures[[edit](/index.php?title=Temperature&action=edit&section=7 "Edit section: Creatures")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Temperature&action=edit). Reason:** _Burn/Frostbite chances._  
---|---  
  
Main articles: [Heatstroke](/wiki/Heatstroke "Heatstroke") and [Hypothermia](/wiki/Hypothermia "Hypothermia")

Pawns have a [Maximum Comfortable Temperature](/wiki/Maximum_Comfortable_Temperature "Maximum Comfortable Temperature") and [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"). Going over 10 °C (18 °F) beyond these limits will start giving them [heatstroke](/wiki/Heatstroke "Heatstroke") or [hypothermia](/wiki/Hypothermia "Hypothermia"). The further above or below this 10 °C (18 °F) limit the faster the Heatstroke or Hypothermia rises. At 150 °C (270 °F) above their comfortable temperature range, creatures will begin to take burn damage. If Hypothermia reaches a severity of 37% and the pawn is in a location at 0 °C (32 °F) or below, there is a chance the pawn takes Frostbite damage. The higher the Hypothermia severity the higher the chance of Frostbite damage. [Insectoids](/wiki/Insectoid "Insectoid") will experience [hypothermic slowdown](/wiki/Hypothermic_slowdown "Hypothermic slowdown") instead of hypothermia. Pawns will also receive negative [moodlets](/wiki/Mood "Mood") based on how extreme the temperature is. The Gear tab shows aggregate stats about comfy temperatures. 

Hypothermia and Heatstroke are both fatal at 100% severity. Though, both Heatstroke and Hypothermia have significant health consequences and can lead to death before the 100% severity level is reached. 

For humans, [apparel](/wiki/Apparel "Apparel") will increase both comfortable thresholds, [depending on the apparel type and material](/wiki/Insulation "Insulation") (e.g. [wool](/wiki/Wool "Wool") [parkas](/wiki/Parka "Parka") insulate well against cold). Colonists will try and wear items suitable for the temperature, unless they are forced otherwise. Colonists' moods _ignore_ apparel when considering sleeping moodlets. So piling on the warmest apparel doesn't avoid a "Slept in the cold" bad thought if a bedroom is not adequately heated. 

Animals tend to have much higher comfortable thresholds. However, in extreme [biomes](/wiki/Biome "Biome"), it may be necessary to build a "barn" of some sort with temperature control and designate indoor [animal sleeping spots](/wiki/Animal_sleeping_spot "Animal sleeping spot") to keep your herd warm/cool. 

Many work benches, such as a [electric stove](/wiki/Electric_stove "Electric stove") or [stonecutter's table](/wiki/Stonecutter%27s_table "Stonecutter's table"), have a comfortable range between 10 °C – 35 °C (50 °F – 95 °F). Above or below this range, the _bench'_ s work speed is multiplied by 70%. 

### Fire[[edit](/index.php?title=Temperature&action=edit&section=8 "Edit section: Fire")]

Main article: [Fire](/wiki/Fire "Fire")

Fire is a destructive force capable of destroying plants, buildings, and pawns alike. Pawns and items can spontaneously ignite when temperature is at or above 235 °C (455 °F). Fires can spread via embers from up to 2 tiles. 

Fire itself provides a massive amount of heat. 

## Managing temperature[[edit](/index.php?title=Temperature&action=edit&section=9 "Edit section: Managing temperature")]

Temperature management is important for any colony, regardless of climate. It can be simply managed with a good power supply and the following structures. Temperature changing buildings will still work while "outdoors", but have no noticeable effect. 

### Temperature thresholds[[edit](/index.php?title=Temperature&action=edit&section=10 "Edit section: Temperature thresholds")]

Temperature | Effects   
---|---  
1,000 °C (1,832 °F) | Maximum value   
~235 °C (455 °F) | Items spontaneously catch fire   
60 °C (140 °F) | Maximum comfortable temperature of any animal ([Dromedary](/wiki/Dromedary "Dromedary") / [Insectoids](/wiki/Insectoids "Insectoids") / [Iguana](/wiki/Iguana "Iguana"))   
58 °C (136.4 °F) | [Plant growth](/wiki/Plants#Temperature "Plants") stopped.   
42 °C (107.6 °F) | Above this value [Plant growth](/wiki/Plants#Temperature "Plants") slowed.   
35 °C (95 °F) | At this temperature and above work benches show "Bad temperature" and Work Speed is reduced to 70%.   
30 °C (86 °F) | [Campfire](/wiki/Campfire "Campfire") max temperature   
26 °C (78.8 °F) | Default [human](/wiki/Human "Human") upper comfort limit without clothing modifiers.  
Sleeping above this temperature creates "Slept in the heat" thought in baseline humans.   
23 °C (73.4 °F) | [Torch lamp](/wiki/Torch_lamp "Torch lamp")/[Fungus darktorch](/wiki/Fungus_darktorch "Fungus darktorch")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")/[Darktorch](/wiki/Darktorch "Darktorch")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")/[Brazier](/wiki/Brazier "Brazier")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")/[Darklight brazier](/wiki/Darklight_brazier "Darklight brazier")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") max temperature   
21 °C (69.8 °F) | [Heater](/wiki/Heater "Heater") and [Cooler](/wiki/Cooler "Cooler") default target   
17 °C (62.6 °F) | [Passive cooler](/wiki/Passive_cooler "Passive cooler") min temperature   
16 °C (60.8 °F) | Default [human](/wiki/Human "Human") lower comfort limit without clothing modifiers.  
Sleeping below this temperature creates "Slept in the cold" thought in baseline humans.   
10 °C (50 °F) | Below this value food spoiling slowed.  
Food spoiling between 10C and 0C is multiplied by a factor of (Temp)/10, in Celsius.  
Below this value work benches show "Bad temperature" and Work Speed is reduced to 70%.   
9 °C (48.2 °F) | Food spoiling rate multiplied by a factor of 0.9, or time to spoil multiplied by 1.11.   
8 °C (46.4 °F) | Food spoiling rate multiplied by a factor of 0.8, or time to spoil multiplied by 1.25.   
7 °C (44.6 °F) | Food spoiling rate multiplied by a factor of 0.7, or time to spoil multiplied by 1.43.   
6 °C (42.8 °F) | Food spoiling rate multiplied by a factor of 0.6, or time to spoil multiplied by 1.66.  
Below this value [plant growth](/wiki/Plants#Temperature "Plants") slowed.   
5 °C (41 °F) | Food spoiling rate multiplied by a factor of 0.5, or time to spoil multiplied by 2.   
4 °C (39.2 °F) | Food spoiling rate multiplied by a factor of 0.4, or time to spoil multiplied by 2.5.   
3 °C (37.4 °F) | Food spoiling rate multiplied by a factor of 0.3, or time to spoil multiplied by 3.33.   
2 °C (35.6 °F) | Food spoiling rate multiplied by a factor of 0.2, or time to spoil multiplied by 5.   
1 °C (33.8 °F) | Food spoiling rate multiplied by a factor of 0.1, or time to spoil multiplied by 10.   
0 °C (32 °F) | Plant growth and food spoiling stopped.  
[Toxic wastepacks](/wiki/Toxic_wastepack "Toxic wastepack")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") do not dissolve. (They can still [deteriorate](/wiki/Deteriorate "Deteriorate"))   
-10 °C (14 °F) | Most plants die.   
-65 °C (-85 °F) | Minimum comfortable temperature of any animal ([Thrumbo](/wiki/Thrumbo "Thrumbo"))   
-75 °C (-103 °F) | Outdoor temperature in [Orbit](/wiki/Orbit "Orbit") above the planet[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")  
-273 °C (-459.4 °F) | Minimum value.   
  
## Cooling buildings[[edit](/index.php?title=Temperature&action=edit&section=11 "Edit section: Cooling buildings")]

### Passive cooler[[edit](/index.php?title=Temperature&action=edit&section=12 "Edit section: Passive cooler")]

[![Passive cooler.png](/images/thumb/2/2d/Passive_cooler.png/56px-Passive_cooler.png)](/wiki/Passive_cooler "Passive cooler")

The [passive cooler](/wiki/Passive_cooler "Passive cooler") is a very low-tech option automatically unlocked for all default starts. They operate at the same strength as a Cooler and will cool rooms to a very comfortable 17 °C (62.6 °F). Passive coolers last for 5 days; it needs to be fueled with [wood](/wiki/Wood "Wood") when it runs out of fuel. Due to the temperature limit, passive coolers are unable to preserve food. 

Passive coolers are a life saver in extremely hot climates as they can be quickly built, are immune to electrical events and are easily massed in a heat wave. Use passive coolers to keep your living spaces survivable and chill rooms surrounding a freezer to further protect the products inside. 

### Cooler[[edit](/index.php?title=Temperature&action=edit&section=13 "Edit section: Cooler")]

[![Cooler south.png](/images/thumb/8/81/Cooler_south.png/56px-Cooler_south.png)](/wiki/Cooler "Cooler")

The [cooler](/wiki/Cooler "Cooler") is primarily used to lower the temperature of a room. It has two states of power consumption: low and high. In its low state, the cooler produces no heat or cold but still requires 20 W. It can be used to lower the temperature of a room to a comfortable 20 °C (68 °F) (room temperature) in the summer or create a walk-in freezer for your food. In hot biomes such as desert or rainforest, having comfortable air conditioning is a necessity for any base. 

Coolers are heat pumps that produce both a cold side _and_ a hot side. The hot side is rarely useful and should be directed to an outdoor space (or a 1x1, unroofed room) to not inconvenience your colony. The heating side is useful when outdoors temperature is uncomfortable, but not freezing. This is between 1 °C – 16 °C (33.8 °F – 60.8 °F), but in practical terms, you should point the heat side at the colony when the outdoors temperature rarely goes above 20 °C (68 °F). Never block a cooler's intake or exhaust port, or else it won't function. 

A cooler is theoretically able to cool a single square by about 1800 kelvin [K]. But this is not a linear relation, as a room always exchanges heat with adjacent rooms and/or the outside. 

#### Analysis[[edit](/index.php?title=Temperature&action=edit&section=14 "Edit section: Analysis")]

Electric coolers are the only way to create freezers. Building one is as simple as making a room and replacing some wall tiles with coolers. Direct the cold "blue" zone of the cooler inside the room and the hot "red" tile to an outdoor area. Reduce the cooler's target temperature to below 0 °C (32 °F). As the room cools down any food left inside will decay more slowly until it freezes. Frozen food will stay fresh indefinitely and incurs no other benefit or penalty when eaten. 

If your freezer area is more than about 50 squares, and/or you are living in an area with a hot summer, you will want 2 coolers (and perhaps more, see "adding coolers", below). Put one at 0, and the other at -2. With double walls, this will let one cooler "idle" at 20 W of power in cooler weather while the other easily keeps things frozen, but be available to help when needed for warmer weather. [Batteries](/wiki/Battery "Battery") are useful for power outages; you may want to keep charged batteries disconnected via [power switch](/wiki/Power_switch "Power switch") for these situations. 

Freezers lose heat through walls and doors. The material of a wall doesn't matter, but for maximum insulation, you should put a double layer of them. Doors will cause heat loss when opened. This loss can be offset by having doors arranged in sequence, one after another, at points of egress, in an "airlock" like fashion. The loss can be examined by mousing over the sections of the airlock to see the temperature. Using [doors](/wiki/Door "Door") rather than [autodoors](/wiki/Autodoor "Autodoor") can help reduce the cooling lost, though this slows down colonists. 

#### Adding coolers[[edit](/index.php?title=Temperature&action=edit&section=15 "Edit section: Adding coolers")]

There may come a moment when you realize _"I don't have enough coolers for this area..."_. If the weather is cool, that's not a big problem, but it's more likely that the weather will be brutally hot when you realize this. And it's also likely that it's your freezer that's not at "freezing" (since colonists can tough it out). If you open a wall to put in an additional cooler, your freezer immediately rockets to "outside" temperatures - which is probably a dealbreaker, rotting all your frozen items. So here's what you do... 

Decide where in the current wall you will put your new cooler, and build a door _outside_ where you will tear the existing wall down (you don't need "side walls" to support it). (A wall would "block" the cooler exhaust and prohibit construction, but a door will not!) Then, [f]orbid the door (so it doesn't get opened), and deconstruct your wall; the new door will maintain the area as "inside". Then build your cooler (remembering the orientation, warm side "out"). Once the new cooler has been installed, deconstruct the door, and you're done. 

## Heating buildings[[edit](/index.php?title=Temperature&action=edit&section=16 "Edit section: Heating buildings")]

### Campfire[[edit](/index.php?title=Temperature&action=edit&section=17 "Edit section: Campfire")]

[![Campfire.png](/images/thumb/0/01/Campfire.png/56px-Campfire.png)](/wiki/Campfire "Campfire")

Campfires are a quick and dirty solution to produce heat in a hurry. They require no energy, but are temporary structures and must be refreshed with wood every few days. Otherwise, they produce the same amount of heat as an electrical heater. They cannot raise the temperature to over 30 °C (86 °F). They can't be controlled, so may make pawns uncomfortably hot - open doors or roofs to lower heat. 

### Heater[[edit](/index.php?title=Temperature&action=edit&section=18 "Edit section: Heater")]

[![Heater.png](/images/thumb/9/93/Heater.png/56px-Heater.png)](/wiki/Heater "Heater")

The [heater](/wiki/Heater "Heater") is used to raise the temperature of a room. It has two states of power consumption: low and high. In its low state, the heater produces no heat but still requires 18 W. It can be used to raise the temperature of a room to a likable 20 °C (68 °F) (room temperature) in the winter or create a walk-in heat trap for your foes. In any cold biome, such as the Tundra, the heater is a necessity for any base. 

A heater (in theory) is able to heat a single square by about 1800 kelvin [K]. But this is not a linear relation as a room always exchanges heat with adjacent rooms and/or the outside. This heat conduction effect can be pretty noticeable in extremely cold or hot environments. Example: In a realistic setup, this means it can heat a room with 50 squares by an average of about 36 K per square. So a room with 50 squares and an outside temperature of -10 °C (14 °F) can be heated up to comfortable 26 °C (78.8 °F) or something near that with a single heater. 

## Incidental heat[[edit](/index.php?title=Temperature&action=edit&section=19 "Edit section: Incidental heat")]

### Generators[[edit](/index.php?title=Temperature&action=edit&section=20 "Edit section: Generators")]

[![Chemfuel powered generator.png](/images/thumb/a/a8/Chemfuel_powered_generator.png/56px-Chemfuel_powered_generator.png)](/wiki/Chemfuel_powered_generator "Chemfuel powered generator")

Generators produce a non-negligible amount of heat for the room they occupy, especially when placed in numbers. If placed strategically, you can reduce the number of heaters and coolers necessary to manage the temperature in your base. 

It's also worth noting that generators will continue to produce heat (and burn fuel) during solar flare events. If your colony is in a very cold climate, this can be used to ensure that critical sections such as hydroponics or barns for sensitive animals don't lose all their heat in a power outage. 

### Steam geysers[[edit](/index.php?title=Temperature&action=edit&section=21 "Edit section: Steam geysers")]

[![Steam geyser.png](/images/thumb/a/ac/Steam_geyser.png/56px-Steam_geyser.png)](/wiki/Steam_geyser "Steam geyser")

A steam geyser will heat up a roofed room even when covered with a [geothermal generator](/wiki/Geothermal_generator "Geothermal generator"). They are extremely useful for staying warm in frozen climates, but can overheat an indoors space in warmer biomes. 

### Fire weapons[[edit](/index.php?title=Temperature&action=edit&section=22 "Edit section: Fire weapons")]

[![Molotov.png](/images/thumb/5/5b/Molotov.png/56px-Molotov.png)](/wiki/Molotov_cocktail "Molotov cocktail")

Weapons that generate fire such as [molotov cocktail](/wiki/Molotov_cocktail "Molotov cocktail") and [incendiary launcher](/wiki/Incendiary_launcher "Incendiary launcher") can be used to quickly generate heat inside your colony. Under normal conditions this is a **bad idea** because fires will quickly bring your base to intolerable temperatures. However in a bitter arctic climate with no wood and inadequate heaters, these weapons are your last defense against freezing to death. Draft your colonist and force them to open fire on an empty space, or burn spare corpses and rags to increase heat output. 

### Body heat[[edit](/index.php?title=Temperature&action=edit&section=23 "Edit section: Body heat")]

[![Colonist.png](/images/thumb/b/b0/Colonist.png/60px-Colonist.png)](/wiki/Pawns "Pawns")

Living, organic creatures (excludes [mechanoids](/wiki/Mechanoid "Mechanoid"), [drones](/wiki/Drone "Drone"),[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") [nociospheres](/wiki/Nociosphere "Nociosphere"), [fleshmass nuclei](/wiki/Fleshmass_nucleus "Fleshmass nucleus"), [metal horrors](/wiki/Metal_horror "Metal horror"), [revenants](/wiki/Revenant "Revenant")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")) generate a small amount of heat directly proportional to their body size as long as the ambient temperature is not above 40°C. The heat pushed follows the formula: 

  * `0.3 * Body Size * 4.1666665` ≈ `1.25 * Body Size` for human pawns
  * `0.3 * Body Size * 4.1666665 * 0.6` ≈ `0.75 * Body Size` for all others



Heating is inconsistent, as creatures are prone to wandering, population and sizes fluctuate with births, culling, and growth, and livestock are frequently left in outdoor [pens](/wiki/Pen "Pen") where heat will dissipate. 

### Solar pinhole[[edit](/index.php?title=Temperature&action=edit&section=24 "Edit section: Solar pinhole")]

[![RoyaltyIcon.png](/images/thumb/4/41/RoyaltyIcon.png/40px-RoyaltyIcon.png)](/wiki/Royalty_\(DLC\) "Royalty \(DLC\)") | **This section relates to content added by[Royalty (DLC)](/wiki/Royalty_\(DLC\) "Royalty \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
  
[![SolarPinhole.png](/images/9/9e/SolarPinhole.png)](/wiki/File:SolarPinhole.png) [Solar pinhole](/wiki/Solar_pinhole "Solar pinhole") is a psycast that creates heat and light. It lasts five days. It is useful for emergency situations, such as power shortages during [cold snaps](/wiki/Cold_snap "Cold snap"). 

### Production buildings[[edit](/index.php?title=Temperature&action=edit&section=25 "Edit section: Production buildings")]

[![Electric smelter.png](/images/thumb/2/2e/Electric_smelter.png/56px-Electric_smelter.png)](/wiki/Electric_smelter "Electric smelter")

Certain production buildings generate heat while executing bills: [Electric smelters](/wiki/Electric_smelter "Electric smelter") at a rate of 9 heat per second, [Electric crematoria](/wiki/Electric_crematorium "Electric crematorium") at a rate of 12 heat per second, [Fueled stoves](/wiki/Fueled_stove "Fueled stove") at a rate of 4 heat per second, [Electric stoves](/wiki/Electric_stove "Electric stove") at a rate of 3 heat per second. 

## Heat transfer[[edit](/index.php?title=Temperature&action=edit&section=26 "Edit section: Heat transfer")]

### Vent[[edit](/index.php?title=Temperature&action=edit&section=27 "Edit section: Vent")]

[![Vent.png](/images/thumb/d/db/Vent.png/56px-Vent.png)](/wiki/Vent "Vent")

A **vent** allows transfer of temperature and [gases](/wiki/Gas "Gas") from one room to another. 

Vents can have any building in front of it, but no walls. Vents work best when connecting directly to a climate controlled room. Trying to chain vents across smaller rooms will lead to each successive room getting less effective climate control, and connecting to a hallway won't work well if the hallway is blocked with doors. A vent can be designated to be closed, an action carried out by colonists assigned to [Basic](/wiki/Work#Basic "Work"). 

### Doors[[edit](/index.php?title=Temperature&action=edit&section=28 "Edit section: Doors")]

[![Door.png](/images/thumb/3/36/Door.png/56px-Door.png)](/wiki/Vent "Vent")

Similar to double thick walls, double doors (not side-by-side, rather, both in the path of travel) improve insulation and reduce temperature equalization. A door can be left permanently open (mark the door to 'hold open' and have a pawn pass through) to help control temperature. Open doors allow temperature to more quickly equalize between rooms or the outdoors. Equalization through open doors is less potent than vents. 

## Temperature mechanics[[edit](/index.php?title=Temperature&action=edit&section=29 "Edit section: Temperature mechanics")]

Equalization calculations happens once every 120 game ticks. 

Temperature seems to be measured to an extreme precision. 

### Passive equalization[[edit](/index.php?title=Temperature&action=edit&section=30 "Edit section: Passive equalization")]

This is equalization via walls and roofs. 

**Walls** will equalize towards the room on the other side. This can be another fully realized room or simply the outdoors. If the other side is not outdoors, that room will also equalize towards this room. 

  * The material of the walls does not matter. Wood is as insulating as any stone or metal. And unmined rocks are equally effective. 
    * A 2nd layer halves the temperature equalization via walls. Extra wall layers have no effect.
    * Nutrient dispensers are one of the few items working fully like walls for equalization purposes.
  * The surface area does matter. Basically, the game is using a 2D variant of the [square-cube law](https://en.wikipedia.org/wiki/square-cube_law "wikipedia:square-cube law"), with walls taking the place of "surface area" and room size taking the place of "volume". As such square rooms are the most efficient at keeping temperatures. 
    * Furniture lowers the room size and therefore might change the rate of equalization.



Example of equalization values at -9555.208°C[Check] difference for: 

     Room | Single wall | Double wall   
---|---|---  
1x1 | -161.470°C | -81.234°C   
2x2 | -81.235°C | -40.617°C   
3x3 | -54.157°C | -27.078°C   
4x4 | -40.618°C | -20.309°C   
5x5 | -32.494°C | -16.247°C   
6x6 | -27.078°C | -13.539°C   
7x7 | -23.210°C | -11.605°C   
  
**Roof** is a major part with equalization with the outdoor temperature. It will always equalize with the outdoor temperature, regardless what the room borders. However, the equalization rate is also constant for all room sizes at the same temperature difference. There are 4 basic types of roof: 

    

  * **Unroofed** tiles are looked at in relation to the total count of roofed tiles in a room. With at least 1/4 unroofed the room will simply equalize to outdoor temperature on the next tick.
  * **Thin roof** (**constructed roof** and **thin rock**): at a temperature difference of -9,555.208 °C (-17,199.4 °F) it equalizes by -57.331 °C (-103.2 °F) every 120 ticks.
  * **Thick rock** does not equalize temperature with the outdoors at all, and has a passive cooling effect if the indoor temperature is 15 °C (59 °F) or above; however this effect is extremely small compared to other sources.



### Active equalization[[edit](/index.php?title=Temperature&action=edit&section=31 "Edit section: Active equalization")]

While Vents, Coolers and open doors still keep rooms separated, they also equalize temperature at a very high rate. This rate is unfortunately not shown on any tooltip. 

Torches, Campfires, Heaters and Passive coolers will directly modify the room temperature instead, adding/removing heat every equalization tick as appropriate for their settings/current state. 

## Version history[[edit](/index.php?title=Temperature&action=edit&section=32 "Edit section: Version history")]

  * [0.13.1135](/wiki/Version/0.13.1135 "Version/0.13.1135") \- Deep rooms stay cooler in the heat.
  * [Beta 19](/wiki/Beta_19 "Beta 19")/[1.0.0](/wiki/Version/1.0.0 "Version/1.0.0") \- Equalized [mood](/wiki/Mood "Mood") penalties for being too hot and too cold.
  * [1.3.3066](/wiki/Version/1.3.3066 "Version/1.3.3066") \- Fix: Changing temperature display mode (C to F) doesn’t update temperature readout immediately.



* * *

[Architect](/wiki/Architect "Architect")

Temperature
    [Campfire](/wiki/Campfire "Campfire") • [Heater](/wiki/Heater "Heater") • [Cooler](/wiki/Cooler "Cooler") • [Passive cooler](/wiki/Passive_cooler "Passive cooler") • [Vent](/wiki/Vent "Vent")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Temperature&oldid=184101](https://rimworldwiki.com/index.php?title=Temperature&oldid=184101)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Pages to be rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten")
  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Game mechanics](/wiki/Category:Game_mechanics "Category:Game mechanics")
  * [Buildings](/wiki/Category:Buildings "Category:Buildings")



Hidden category: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Temperature "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Temperature "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Temperature "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Temperature "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Temperature)
  * [Edit](/index.php?title=Temperature&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Temperature&action=history "Past revisions of this page \[h\]")



###  More




###  Search

[](/wiki/Main_Page "Visit the main page")

###  RimWorld

  * [Official Site](http://ludeon.com/)
  * [Official Twitter](https://twitter.com/TynanSylvester)
  * [Subreddit](https://www.reddit.com/r/RimWorld)
  * [Community Discord](https://discordapp.com/invite/UTaMDWc)



###  Navigation

  * [Main page](/wiki/Main_Page "Visit the main page \[z\]")
  * [Recent changes](/wiki/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [Random page](/wiki/Special:Random "Load a random page \[x\]")



###  Tools

  * [What links here](/wiki/Special:WhatLinksHere/Temperature "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Temperature "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Temperature&oldid=184101 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Temperature&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Temperature)



  * This page was last edited on 17 August 2026, at 00:36.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[+4]: Stacking 3 times with a 0.5 multiplier for maximum of 7
  *[_Nuzzled_]: A cute animal nuzzled me.
  *[+5]: Stacking 1 times for a maximum of 5
  *[_[Bonded animal]'s master_]: Being together with my bonded animal makes me feel better.
  *[−3]: Stacking 1 times for a maximum of -3
  *[_Not [Bonded animal]'s master_]: I should be together with my bonded animal.
  *[4]: Stacking 3 times with a 0.5 multiplier for maximum of 7
  *[10 secs]: real-time at 1x speed
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[[Note]]: This value is automatically calculated by the wiki and may not be correct
  *[13.33 secs]: real-time at 1x speed
  *[Deconstruct yield]: Resources recovered when deconstructing.
  *[Destroy yield]: Resources recovered when destroyed.
  *[1 in-game hour]: there are 2,500 ticks in an hour
  *[XP Factor]: Potency * 0.7, clamped at 0.5 and 1.0.
  *[Human]: 500 * XP Factor
  *[Animal]: 175 * XP Factor
  *[11.67 secs]: real-time at 1x speed
  *[Bulk Product Amount]: The amount of this item produced by the bulk recipe
  *[MTB]: Mean or average time between occurrences
  *[−6]: Stacking 1 times for a maximum of -6
  *[_Was imprisoned_]: The colony had me in jail for a while, like a caged animal.
  *[40]: Stacking 5 times with a 0.75 multiplier for maximum of 122
  *[_Catharsis_]: It felt good to finally unbottle my feelings.
  *[−8]: Stacking 1 times for a maximum of -8
  *[_Tortured artist_]: Natural penalty from 'tortured artist' trait.
  *[30]: Stacking 5 times for a maximum of 150
  *[_Void catharsis_]: There was a madness building in my mind. It's gone, for now.
  *[4 in-game hours]: there are 2,500 ticks in an hour
  *[10 in-game hours]: there are 2,500 ticks in an hour
  *[18 in-game hours]: there are 2,500 ticks in an hour
  *[16 in-game hours]: there are 2,500 ticks in an hour
  *[24 in-game hours]: there are 2,500 ticks in an hour
  *[12 in-game hours]: there are 2,500 ticks in an hour
  *[3.2 in-game hours]: there are 2,500 ticks in an hour
  *[28 in-game hours]: there are 2,500 ticks in an hour
  *[36 in-game hours]: there are 2,500 ticks in an hour
  *[4.8 in-game hours]: there are 2,500 ticks in an hour
  *[20 in-game hours]: there are 2,500 ticks in an hour
  *[−2]: Stacking 4 times for a maximum of -8
  *[_< name> rambling_]: <name> is talking nonsense. Is he/she insane?
  *[10.42 secs]: real-time at 1x speed
  *[0.8 in-game hours]: there are 2,500 ticks in an hour
  *[6 in-game hours]: there are 2,500 ticks in an hour
  *[2.4 in-game hours]: there are 2,500 ticks in an hour
  *[40 in-game hours]: there are 2,500 ticks in an hour
  *[5 in-game days]: there are 60,000 ticks in a day
  *[1.4 in-game hours]: there are 2,500 ticks in an hour
  *[0.48 in-game hours]: there are 2,500 ticks in an hour
  *[0.17 in-game hours]: there are 2,500 ticks in an hour
  *[7.2 in-game hours]: there are 2,500 ticks in an hour
  *[27.78 years]: there are 3,600,000 ticks in a year
  *[8 in-game hours]: there are 2,500 ticks in an hour
  *[14 in-game hours]: there are 2,500 ticks in an hour
  *[HP]: Hit Points
  *[40 secs]: real-time at 1x speed
  *[1.33 mins]: real-time at 1x speed
  *[]: RGB: (85, 85, 85)
  *[1 in-game day]: there are 60,000 ticks in a day
  *[3 secs]: real-time at 1x speed
  *[Stuff Tags]: The types of resource that can be substituted for the generic resource type
  *[4.8 secs]: real-time at 1x speed
  *[34.33 secs]: real-time at 1x speed
  *[31.67 secs]: real-time at 1x speed
  *[29.33 secs]: real-time at 1x speed
  *[11.73 secs]: real-time at 1x speed
  *[29 secs]: real-time at 1x speed
  *[5.33 secs]: real-time at 1x speed
  *[26.67 secs]: real-time at 1x speed
  *[10.13 secs]: real-time at 1x speed
  *[3.73 secs]: real-time at 1x speed
  *[41.67 secs]: real-time at 1x speed
