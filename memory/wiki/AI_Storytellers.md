# AI Storytellers

From RimWorld Wiki

Jump to navigation Jump to search

|  |  | [Basics](/wiki/Basics "Basics") | [Menus](/wiki/Menus "Menus") | **Game Creation** | [Gameplay](/wiki/Gameplay "Gameplay") | [Pawns](/wiki/Pawns "Pawns") | [Plants](/wiki/Plants "Plants") | [Resources](/wiki/Resources "Resources") | [Gear](/wiki/Gear "Gear") | [Mods](/wiki/Mods "Mods")  
---|---|---|---|---|---|---|---|---  
[Game Creation](/wiki/Game_Creation "Game Creation") | [Scenario system](/wiki/Scenario_system "Scenario system") | **AI Storytellers** | [World Generation](/wiki/World_generation "World generation") | [Biomes](/wiki/Biomes "Biomes")  
---|---|---|---|---  
AI Storytellers | [Cassandra Classic](/wiki/Cassandra_Classic "Cassandra Classic") | [Phoebe Chillax](/wiki/Phoebe_Chillax "Phoebe Chillax") | [Randy Random](/wiki/Randy_Random "Randy Random")  
---|---|---|---  
  
* * *

## Contents

  * 1 Current AI storytellers
  * 2 Difficulties
    * 2.1 Commitment mode
  * 3 Options
    * 3.1 Threats
    * 3.2 Economy
    * 3.3 General
    * 3.4 Player tools
    * 3.5 Adaptation
    * 3.6 Ideology
    * 3.7 Biotech
    * 3.8 Anomaly
      * 3.8.1 Standard with monolith options
      * 3.8.2 Ambient horror options
  * 4 Technical info
    * 4.1 New colonist events
  * 5 Trivia
  * 6 Version history



The **AI storyteller** is the main mechanism used to determine game difficulty and play style. There are currently three presets for narrative settings. Each preset features different raid frequencies and an eponymous cartoon mascot. The player must choose either **Cassandra Classic, Phoebe Chillax, or Randy Random** to act as their "unseeable God." They will periodically create [events](/wiki/Events "Events") for your colony, including [raids](/wiki/Raid "Raid"), [cargo pods](/wiki/Cargo_pods "Cargo pods"), and [manhunter packs](/wiki/Manhunter_pack "Manhunter pack"). The AI Storyteller does not have an in-game body, location, or manifestation; it is just a name given to describe game settings. 

Your choice of storyteller sets the tone for your colony—a more benevolent storyteller like Phoebe will send trade caravans or helpful travelers after hitting your colony hard with a tough raid. 

The frequency and type of storyteller events are based on a number of factors. Colony wealth, building wealth, colonists count, animal count, if a colonist has died or been severely wounded recently, and how long it has been since the last major event are all considered before a storyteller event occurs. 

The difficulty is adjusted separately from the storyteller, however, some storytellers are less merciful than others. Both difficulty and storyteller are changeable mid-game from the Settings Menu, with no downside or penalty. 

## Current AI storytellers[[edit](/index.php?title=AI_Storytellers&action=edit&section=1 "Edit section: Current AI storytellers")]

[![Cassandra.png](/images/thumb/9/9d/Cassandra.png/175px-Cassandra.png)](/wiki/Cassandra_Classic "Cassandra Classic")

**[Cassandra Classic](/wiki/Cassandra_Classic "Cassandra Classic")**  
  
 _Cassandra creates story events on a classic increasing curve of challenge and tension.  
She'll push you with dangerous events, then give breathing room, then come back to push once more._

[![Phoebe.png](/images/thumb/3/35/Phoebe.png/175px-Phoebe.png)](/wiki/Phoebe_Chillax "Phoebe Chillax")

**[Phoebe Chillax](/wiki/Phoebe_Chillax "Phoebe Chillax")**  
  
 _Phoebe gives lots of time between disasters to build your colony.  
But beware - at high difficulties, she'll hit as hard as anyone._

[![Randy.png](/images/thumb/3/33/Randy.png/175px-Randy.png)](/wiki/Randy_Random "Randy Random")

**[Randy Random](/wiki/Randy_Random "Randy Random")**  
  
 _Randy doesn't follow rules.  
He'll generate random events, and he doesn't care if they make a story of triumph or utter hopelessness. It's all drama to him.  
  
Warning: Since Randy is truly random, he will sometimes send extremely difficult or unfair groups of events at you.  
It makes for high drama - and unavoidable sacrifices._

## Difficulties[[edit](/index.php?title=AI_Storytellers&action=edit&section=2 "Edit section: Difficulties")]

There are 6 default difficulties: 

Difficulty | In-game description   
---|---  
Peaceful  | Build a community in a sandbox environment. Major direct threats are disabled, but challenges like disease, mental breaks, and mad animals can still occur. Recommended for: 

  * Players who want to learn the game mechanics with minimal pressure.
  * Players who just want to build.
  * Players who just want to relax.

  
Community builder  | Build a community with a taste of danger. Threats appear, but they're weakened. Recommended for: 

  * Players who are new to this kind of game.
  * Players who want to build a perfect colony.
  * Players who want to relax.

  
Adventure story  | There's room to grow and thrive, but it's still a dangerous planet. Recommended for: 

  * Experienced strategy gamers on their first game of RimWorld.
  * Experienced RimWorld players who want some breathing room to pursue funny or weird goals.

  
Strive to survive  | Strive to survive on a rough, tough planet. There will be triumph and tragedy. Recommended for: 

  * Experienced players who want a rough story requiring skill to survive.

  
Blood and dust  | Face brutal survival challenges. Even if you play well, people will die. You will need to anticipate threats before they arrive, and seek out every advantage. Recommended for: 

  * Experienced players who want to struggle to survive.

  
Losing is fun  | This setting is designed to be unfair. Huge threats will crash upon you without mercy until your colony dies. Only choose this setting if you are happy with the drama of struggling and dying. Recommended for: 

  * Experienced players who want to face a brutal, unfair challenge where even great skill may not prevent death.
  * Lovers of tragedy.
  * Digital masochists.

  
  
Each difficulty works by changing the values of each setting, displayed down below. Using the Custom difficulty will allow you to change each setting yourself. The default values are based on the "Strive to survive" difficulty level, where most values are at 1.0, or 100%. When creating a custom difficulty, you can use the "Set to Standard Playstyle" button to change the values to one of the 6 default difficulties. 

### Commitment mode[[edit](/index.php?title=AI_Storytellers&action=edit&section=3 "Edit section: Commitment mode")]

When creating a game, the player must choose between "Commitment" and "Reload anytime" mode. Unlike storyteller and difficulty, **this cannot be changed after game creation**. If desired, you can disable (or enable) commitment mode by [editing the save file](/wiki/Permadeath_save_conversion_guide "Permadeath save conversion guide"). 

With reload anytime, you can save and reload the game as you wish. Good if you're still learning the game, if you intend to self-enforce commitment mode, or if you want to have a more relaxed experience. RimWorld is a single player game - nobody will judge you for playing with saves. 

In commitment mode, you only get one save file and can only save when quitting the game. You cannot reload the game to fix mistakes. When the entire colony dies, but _only_ when the entire colony dies, [that's it](/wiki/Endings#Colony_End "Endings"). This is the way RimWorld was meant to be played with every dramatic turn - whether tragic or hopeful - played out to full impact. (Note: this can be dangerous if you use lots of mods - if something soft-locks, you cannot go back to an earlier save to avoid the situation!) 

## Options[[edit](/index.php?title=AI_Storytellers&action=edit&section=4 "Edit section: Options")]

### Threats[[edit](/index.php?title=AI_Storytellers&action=edit&section=5 "Edit section: Threats")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Threat scale  | Adjust the size of threats like raids (using [raid points](/wiki/Raid_points "Raid points")) and infestations, and the difficulty of quests. | 0% - 500% | 10% | 30% | 60% | 100% | 155% | 220%   
Major threats  | Allow major threats such as [raids](/wiki/Raids "Raids"), [infestations](/wiki/Infestation "Infestation"), manhunter packs, crashed mechanoid ships and more. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Quests threats  | Allow quests to present with violent threats and challenges. If this is disabled, quests will be modified to be non-violent. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Intro threats  | Enable the fixed intro threats that appear near game start. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Predators hunt humans  | Allow wild predators to hunt humans. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Extreme weather  | Allow extreme weather incidents such as [toxic fallout](/wiki/Events#Toxic_Fallout "Events"), [volcanic winters](/wiki/Events#Volcanic_Winter "Events") and [flashstorms](/wiki/Events#Flashstorm "Events"). | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
  
### Economy[[edit](/index.php?title=AI_Storytellers&action=edit&section=6 "Edit section: Economy")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Harvest yield  | Adjust the amount of materials produced when harvesting [plants](/wiki/Plants "Plants") and crops. This includes harvesting plants and cutting [trees](/wiki/Trees "Trees"). | 0% - 500% | 120% | 120% | 100% | 100% | 95% | 80%   
Mining yield  | Adjust the amount of materials produced when mining. | 0% - 500% | 120% | 120% | 100% | 100% | 95% | 80%   
Butchering yield  | Adjust the amount of materials produced when butchering. This includes [meat](/wiki/Meat "Meat"), [leather](/wiki/Leather "Leather"), and yield from shredding [mechanoids](/wiki/Mechanoids "Mechanoids"). | 0% - 500% | 100% | 100% | 100% | 100% | 90% | 80%   
Research speed  | Adjust the speed of research. | 0% - 500% | 120% | 120% | 100% | 100% | 95% | 90%   
Quest rewards  | Adjust the value of rewards given for quests. Note: Quest reward value is also automatically scaled to compensate for threat scale. If you adjust this setting, you'll be adding an additional multiplier. | 0% - 500% | 100%   
Raid loot  | Adjust the value of loot carried by raiders. Note: Raid loot value is also automatically scaled to compensate for threat scale. If you adjust this setting, you'll be adding an additional multiplier. | 0% - 500% | 100%   
Trade price disadvantage  | When trading, buy prices are increased by this amount while sell prices are reduced by this amount. | 0% - 50% | 0% | 0% | 0% | 0% | 10% | 20%   
Turret rearm cost  | Adjust the cost of rearming turrets. | 1% - 100% | 100%   
Scaria rot chance  | The probability that a corpse will immediately rot upon death, if the creature has the [scaria](/wiki/Scaria "Scaria") disease. Note: The default settings are designed to exactly balance out the increase in animal count at higher difficulties, so all players get the same meat rewards. | 0% - 100% | 0% | 0% | 33% | 60% | 74% | 82%   
Enemy death on downed  | Adjust the [extra chance](/wiki/Downed#Death_on_down "Downed") that an enemy will immediately die when downed. This affects the chances to take prisoners, and thus colony population growth rates. | 0% - 100% | 50% | 90% | 100% | 100% | 100% | 100%   
  
### General[[edit](/index.php?title=AI_Storytellers&action=edit&section=7 "Edit section: General")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Colonist mood  | A permanent mood offset applied to every colonist and prisoner. Colonists have a base mood of 50%. | -20 - +20 | +10 | +10 | +5 | +0 | -5 | -10   
Food poison chance  | Adjust the chance that a person will get [food poisoning](/wiki/Food_poisoning "Food poisoning") from eating a potentially-poisoned meal. | 0% - 500% | 30% | 50% | 75% | 100% | 110% | 120%   
Animal revenge chance  | Adjust the chance that injuring a wild animal will cause it to attack. | 0% - 500% | 25% | 100% | 100% | 100% | 100% | 100%   
Infection chance  | Adjust the chance that a wound will become [infected](/wiki/Infection "Infection"). | 0% - 500% | 30% | 50% | 75% | 100% | 100% | 110%   
Disease frequency  | Adjust the frequency of random [disease](/wiki/Disease "Disease") events. | 0% - 500% | 33% | 40% | 67% | 100% | 105% | 111%   
Insect spawning rate  | Adjust the rate at which existing insect [hives](/wiki/Hive "Hive") spawn new [insects](/wiki/Insects "Insects"). Lower values means more time between spawn events. This does not affect whether infestations can occur - only the speed at which active hives produce insects. | 0% - 500% | 10% | 15% | 50% | 100% | 100% | 100%   
Deep drilling infestations  | Adjust the chance that [deep drilling](/wiki/Deep_drill "Deep drill") will trigger an [infestation](/wiki/Infestation "Infestation"). | 0% - 500% | 0% | 25% | 75% | 100% | 110% | 130%   
Friendly fire  | Adjust the chance of [friendly fire](/wiki/Friendly_fire "Friendly fire"). Note: This setting only affects direct shots which were going to hit their target. It does not prevent damage from explosions, or from shots which were going to miss their target. | 0% - 100% | 40%   
Colonist instant kills  | Adjust the chance that a colonist can die instantly due to an attack. The incoming damage is adjusted so it will down the colonist instead. This only prevents some kinds of instant kills - colonists can still be downed and bleed to death, die from fire, explosions, disease, and so on. | 0% - 100% | 100%   
Map generation ancient threats  | [Ancient structures](/wiki/Ancient_shrine "Ancient shrine") may contain [dangerous](/wiki/Mechanoids "Mechanoids") [threats](/wiki/Insectoids "Insectoids"). | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Map generation natural hives  | Dormant insect [hives](/wiki/Hive "Hive") may spawn in natural caves. This setting only applies to map generation and does not affect active insects that may tunnel in during play. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
  
### Player tools[[edit](/index.php?title=AI_Storytellers&action=edit&section=8 "Edit section: Player tools")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Player can build spike traps  | Player can build traps like [spike traps](/wiki/Spike_trap "Spike trap") and [IED traps](/wiki/IED_trap "IED trap"). | Toggle | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Player can build turrets  | Player can build static turrets like [mini-turrets](/wiki/Mini-turret "Mini-turret"), [autocannon turrets](/wiki/Autocannon_turret "Autocannon turret"), and [uranium slug turrets](/wiki/Uranium_slug_turret "Uranium slug turret"). You can still use captured turrets even if this is disabled. | Toggle | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Player can build mortars  | Player can build mortars. You can still use captured mortars even if this is disabled. | Toggle | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png)  
Classic mortars  | Mortars will not require [reinforced barrels](/wiki/Reinforced_barrel "Reinforced barrel") to construct or reload, and are balanced for this ease of access. With "Classic Mortars", mortars are as they were before 1.3. Namely: 

  * The barrel need not be changed every 20 shots.
  * Reinforced barrels are removed from the recipe and game.
  * Forced miss radius increased from 9 to 13.
  * [Steel](/wiki/Steel "Steel") cost of all mortar shells increased by 10.

Note that the [Mortar Miss Radius Multiplier](/wiki/Mortar_Miss_Radius_Multiplier "Mortar Miss Radius Multiplier") still applies with this setting applied.  | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
  
### Adaptation[[edit](/index.php?title=AI_Storytellers&action=edit&section=9 "Edit section: Adaptation")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Adaptation growth rate  | Adaptation means the storyteller makes the game more challenging when you're doing well. An adaptation score grows over time, and is knocked down when you take damage. This setting adjusts how fast the adaptation score grows over time. | 0% - 100% | 0% | 25% | 75% | 100% | 100% | 100%   
Adaptation impact  | Adaptation means the storyteller makes the game more challenging when you're doing well. An adaptation score grows over time, and is knocked down when you take damage. This setting adjusts how much the adaptation score affects the difficulty. | 0% - 100% | 100% | 100% | 100% | 90% | 70% | 40%   
Wealth-independent progress mode  | Play in a wealth-independent progress mode. In normal mode, the storyteller scales threats according to colonist count, player wealth, and a variety of other factors. Wealth-independent mode removes the wealth factor and replaces it with a fixed progress curve based on time. The time is counted from the founding of each colony. This is only recommended for those looking for a strict skill challenge. In wealth-independent mode, it may be nearly impossible to recover from serious losses unless you found a new settlement. It's also possible to get too far ahead of the curve and find the game too easy. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Years until maximum threat  | The number of game years until the wealth-independent mode reaches its maximum threat level. Note that the storyteller will still scale threats according to colonist count and a variety of other factors. | 1 - 20 | 12   
  
### Ideology[[edit](/index.php?title=AI_Storytellers&action=edit&section=10 "Edit section: Ideology")]

[![IdeologyIcon.png](/images/thumb/9/94/IdeologyIcon.png/40px-IdeologyIcon.png)](/wiki/Ideology_\(DLC\) "Ideology \(DLC\)") | **This section relates to content added by[Ideology (DLC)](/wiki/Ideology_\(DLC\) "Ideology \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Low pop conversion boost  | With a single colonist of the player's starting [ideoligion](/wiki/Ideoligion "Ideoligion"), conversion chance to their ideoligion is multiplied by this amount. Conversion attempts against them have their impact divided by that amount. With two colonists of the player's starting ideoligion, the effect is halved. With three or more colonists of the player's starting ideoligion, this has no effect. | x100% - x500% | 300%   
  
### Biotech[[edit](/index.php?title=AI_Storytellers&action=edit&section=11 "Edit section: Biotech")]

[![BiotechIcon.png](/images/thumb/7/73/BiotechIcon.png/40px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)") | **This section relates to content added by[Biotech (DLC)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Wastepack cocoon infestation  | Adjust the chance that a dissolved wastepack will trigger the arrival of insect cocoons. | 0% - 500% | 0% | 25% | 50% | 100% | 150% | 200%   
Babies always healthy  | Human babies are always born healthy.  
Mothers can't die in childbirth or have miscarriages. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Disable children  | Humans can't become pregnant. Human babies and children will never appear unless you choose them as starting colonist. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Child enemies  | Hostile raids will sometimes include children. Disabling child enemies will not stop pregnant raiders from spawning. | Toggle | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Child aging rate  | Adjust the rate at which babies and children will age. | 100% - 600% | 400%   
Adult aging rate  | Adjust the rate at which adults will age. | 100% - 600% | 100%   
  
### Anomaly[[edit](/index.php?title=AI_Storytellers&action=edit&section=12 "Edit section: Anomaly")]

[![AnomalyIcon.png](/images/thumb/3/32/AnomalyIcon.png/40px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)") | **This section relates to content added by[Anomaly (DLC)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
  
These settings determine if the [Void monolith](/wiki/Void_monolith "Void monolith") spawns and how [Anomaly](/wiki/Anomaly "Anomaly") threats are treated by the Storyteller. 

Monolith setting | In-game description   
---|---  
Standard with monolith  | The standard Anomaly experience. Anomaly threats are linked to the activation of the void monolith.   
Ambient horror  | The monolith does not appear. Any Anomaly threat can occur, but Anomaly threats will be rare by default. Good if you want to interact with Anomaly expansion content without it being the focus. Note: The monolith endgame cannot occur in this mode.   
Anomaly incidents disabled  | Anomaly threats do not occur. Good if you don't want to interact with most Anomaly expansion content.   
  
#### Standard with monolith options[[edit](/index.php?title=AI_Storytellers&action=edit&section=13 "Edit section: Standard with monolith options")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Anomaly threats inactive  | Adjust the percentage of major threats that will be Anomaly-related when the monolith is not active. Only certain minor Anomaly incidents can occur when the monolith is inactive. | 0% - 100% | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Anomaly threats active  | Adjust the percentage of major threats that will be Anomaly-related when the monolith is active. The percentage of major threats that are Anomaly related when the monolith is at levels 2, 3, and 4 is this setting multiplied by 1.5x | 0%-100% | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Study efficiency  | Adds a multiplier to how much research is gained when studying unnatural entities. | 0% - 500% | 200% | 120% | 100% | 100% | 90% | 80%   
  
#### Ambient horror options[[edit](/index.php?title=AI_Storytellers&action=edit&section=14 "Edit section: Ambient horror options")]

Options | Description | Value options | Peaceful | Community builder | Adventure story | Strive to survive | Blood and dust | Losing is fun   
---|---|---|---|---|---|---|---|---  
Anomaly threats  | Adjust the percentage of major threats that will be Anomaly-related. | 0% - 100% | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png)  
Study efficiency  | Adds a multiplier to how much research is gained when studying unnatural entities. | 0% - 500% | 200% | 120% | 100% | 100% | 90% | 80%   
  
## Technical info[[edit](/index.php?title=AI_Storytellers&action=edit&section=15 "Edit section: Technical info")]

### New colonist events[[edit](/index.php?title=AI_Storytellers&action=edit&section=16 "Edit section: New colonist events")]

The formula that calculates the odds of random events that add new colonists has changed in 1.0. It factors in how long a player has been at the location for which the event is generated, and the current population of that colony, including pawns who are traveling on the world map. These events include "[refugee chased](/wiki/Events#Refugee_Chased_at_.28Settlement.29 "Events")", "[transport pod crash](/wiki/Events#Transport_pod_crash "Events")", "[wanderer joins](/wiki/Events#Wanderer_joins "Events")" and "[wild (human) wanders in](/wiki/Events#Wild_.28wo.29man_wanders_in "Events")". 

The following code examples and analysis were provided by user Bar0th on Steam, who gave permission for their inclusion here. To summarize these findings: There is a new variable, "PopulationIntent," which replaces the old variables "desiredPopulationMin," "desiredPopulationMax" and "desiredPopulationCritical." It controls the odds of colonist-adding incidents happening on a particular map. The odds based on the time at location decrease until the 10th day, and the odds based on population decrease until the 20th colonist. (For purposes of this formula, prisoners count as half a colonist.) Once both variables have decreased to their long-term minimum, the odds remain stable. Randy's minimum chance is .08%, while for Cassandra and Phoebe the minimum chance is .02%, so Randy is still the best option for players who wish to reach a large colony size. 

> * * *
> 
> **PopulationIntent (from StorytellerDef):  
> ** populationIntentFactorFromPopCurve x populationIntentFactorFromPopAdaptDaysCurve**  
> **
> 
> _minIncChancePopulationIntentFactor  
> _ Default = 0.05 (from C#)  
>  Randy = 0.20 (from StorytellerDef)_  
> _
> 
> _IncidentChanceFactor_PopulationIntent (from C#):  
> _ None = 1  
>  IncreaseHard = Max(0.4 + PopulationIntent, minIncChancePopulationIntentFactor)  
>  IncreaseMedium = Max(PopulationIntent, minIncChancePopulationIntentFactor)  
>  IncreaseEasy = Max(-0.4 + PopulationIntent, minIncChancePopulationIntentFactor)_  
> _
> 
> _IncidentChanceFinal (from C#):  
> _ baseChance (from IncidentDef) x IncidentChanceFactor_PopulationIntent _  
> _
> 
> * * *
> 
> **Example Event: Wanderer Join (baseChance = 0.4, populationEffect = IncreaseEasy)**
> 
> _Day >= 10, 5 Population (PopulationIntent = 1.0)_  
> 
> 
>   
>  _Randy: 0.24% (0.4 x Max(-0.4 + 1.0, 0.2) = 0.4 x 0.6)_  
>  _Other: 0.24% (0.4 x Max(-0.4 + 1.0, 0.05) = 0.4 x 0.6)_  
>  \- They are the same, because of the high PopulationIntent. 
> 
> _Day >= 10, 20+ Population (PopulationIntent = -1.0):_  
> 
> 
> _Randy: 0.08% (0.4 x Max(-0.4 + -1.0, 0.2) = 0.4 x 0.2)_  
>  _Other: 0.02% (0.4 x Max(-0.4 + -1.0, 0.05) = 0.4 x 0.05)_  
>  \- Here, the low PopulationIntent allows Randy's higher minIncChancePopulationIntentFactor to take effect. 
> 
> So, there doesn't appear to be a hard cap on any of the storytellers anymore. However, some events can become much rarer at high populations (0.02% chance of a wanderer join, 0.08% if using Randy @ 20+ population). Also, for purposes of population calculation, it searches the entire map for pawns of that colony (ie: includes caravans, etc), and it also includes prisoners of that colony (each prisoner counts as half a colonist). 
> 
> The multiple colony trick works, because it doesn't check all pawns in the map for all colonies, only the one it is currently determining the event for. 
> 
> Also, you can check the table for the PopulationIntent from the "debug logging menu" while in dev mode. Search for the population, and you can bring up the table. You'll notice that after 10 days (at the top), and populations > 20 (at the left) the numbers remain the same. That's because of the curves in Storytellers.xml: 
> 
> _< populationIntentFactorFromPopCurve>_  
>  _< points>_  
> 
> 
> * 0, 8.0
> 
>   
> 
> 
> * 1, 2.0
> 
>   
> 
> 
> * 5, 1.0
> 
>   
> 
> 
> * 9, 0.4
> 
>   
> 
> 
> * 12, 0.0
> 
>   
> 
> 
> * 20,-1.0
> 
>   
>  _< /points>_  
>  _< /populationIntentFactorFromPopCurve>_   
>    
>  _< populationIntentFactorFromPopAdaptDaysCurve>_  
>  _< points>_  
> 
> 
> * ( 0, 0)
> 
>   
> 
> 
> * (10, 1.00)
> 
>   
>  _< /points>_  
>  _< /populationIntentFactorFromPopAdaptDaysCurve>_   
> 
> 
> * * *

Further investigation and updates are needed. 

## Trivia[[edit](/index.php?title=AI_Storytellers&action=edit&section=17 "Edit section: Trivia")]

  * The "Losing is fun" difficulty is a reference to the game _Dwarf Fortress_ , which also happens to be that game's tagline. More specifically, it refers to _Dwarf Fortress_ lacking a definite ending, as the game will end with the player losing no matter how skilled they are.



## Version history[[edit](/index.php?title=AI_Storytellers&action=edit&section=18 "Edit section: Version history")]

  * [0.0.254B](/wiki/Version/0.0.254B "Version/0.0.254B") \- Added Chill Callie Classic [storyteller](/wiki/Storyteller "Storyteller"). Rebalanced Cassandra’s raiders to not send advanced enemies too early, and to pace them a bit slower.
  * [00.1.334](/wiki/Version/0.1.334 "Version/0.1.334") \- Kassandra renamed to Cleopatra.
  * [0.4.460](/wiki/Version/0.4.460 "Version/0.4.460") \- Storytellers now focus on wealth and let you recover from serious damage.
  * [0.11.877](/wiki/Version/0.11.877 "Version/0.11.877") \- Storytellers no longer entirely disallow events because of population. Randy’s event chances are affected by population (somewhat). Re-tuned storyteller population intent based on new output tables for smoother population gain with higher maximum and better recovery at small populations
  * [0.13.1135](/wiki/Version/0.13.1135 "Version/0.13.1135") \- Permadeath mode added - One save file, save on quit or autosave only.
  * The names of the difficulty levels were changed from 1.0 to: 
    * Peaceful
    * Builder
    * Medium
    * Rough
    * Savage
    * Merciless
  * [0.14.1236](/wiki/Version/0.14.1236 "Version/0.14.1236") \- Fix: Storyteller incorrectly adjusts trader frequency in relation to ally count.
  * [0.14.1238](/wiki/Version/0.14.1238 "Version/0.14.1238") \- Phoebe’s random incidents density reduced. Previously the same as Cassandra’s, which conflicted with Phoebe supposedly giving more breathing space between events.
  * [0.14.1241](/wiki/Version/0.14.1241 "Version/0.14.1241") \- Reduced event density on Randy Random from 1.5x that of Cassandra to about the same as Cassandra. The combination and distribution of events is still very different from Cassandra. [Toxic fallout](/wiki/Toxic_fallout "Toxic fallout"), [flashstorm](/wiki/Flashstorm "Flashstorm") and [volcanic winter](/wiki/Volcanic_winter "Volcanic winter") are now disabled in Free Play difficulty.
  * [1.1.2647](/wiki/Version/1.1.2647 "Version/1.1.2647") \- they have changed again to the following: 
    * Peaceful
    * Community builder
    * Adventure story
    * Strive to survive
    * The price of survival is blood
    * Losing is fun
  * [1.1.2654](/wiki/Version/1.1.2654 "Version/1.1.2654") \- "The price of survival is blood" was changed to Blood and Dust.
  * [1.2.2719](/wiki/Version/1.2.2719 "Version/1.2.2719") \- Custom playstyle system added. You can now select a new custom playstyle setting. This opens up a new menu that allows you to customize a large number of different settings exactly as you prefer.
  * [1.2.2753](/wiki/Version/1.2.2753 "Version/1.2.2753") \- Rename "fixed wealth" mode to "wealth-independent" mode, and give the player a slider to control how many years until this mode delivers its maximum threat level.
  * [1.3.3200](/wiki/Version/1.3.3200 "Version/1.3.3200") \- Turret ammo cost is no longer factored by difficulty.
  * [1.4.3555](/wiki/Version/1.4.3555 "Version/1.4.3555") \- Renamed "child raiders" storyteller setting to "child enemies" to be more accurate. Allow modifying the “child aging rate” and “babies are healthy” storyteller settings even if children are disabled, in case there are already children in the game. Fix: Wastepack cocoon infestation storyteller setting appearing in the wrong spot.
  * [1.6.4850](/wiki/Version/1.6.4850 "Version/1.6.4850") \- Fix: Butcher yield storyteller setting affecting "make any stone blocks" bill yield.



* * *

AI Storytellers

Classic
    [Cassandra Classic](/wiki/Cassandra_Classic "Cassandra Classic")

Friendly
    [Phoebe Chillax](/wiki/Phoebe_Chillax "Phoebe Chillax")

Random
    [Randy Random](/wiki/Randy_Random "Randy Random")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=AI_Storytellers&oldid=181181](https://rimworldwiki.com/index.php?title=AI_Storytellers&oldid=181181)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [AI](/wiki/Category:AI "Category:AI")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=AI+Storytellers "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=AI+Storytellers "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/AI_Storytellers "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:AI_Storytellers&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/AI_Storytellers)
  * [Edit](/index.php?title=AI_Storytellers&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=AI_Storytellers&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/AI_Storytellers "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/AI_Storytellers "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=AI_Storytellers&oldid=181181 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=AI_Storytellers&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:AI-5FStorytellers)



  * This page was last edited on 27 June 2026, at 03:51.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


