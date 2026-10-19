# Rooms

From RimWorld Wiki

(Redirected from [Hospital](/index.php?title=Hospital&redirect=no "Hospital"))

Jump to navigation Jump to search

[1]

| [Basics](/wiki/Basics "Basics") | [Menus](/wiki/Menus "Menus") | [Game Creation](/wiki/Game_Creation "Game Creation") | **Gameplay** | [Pawns](/wiki/Pawns "Pawns") | [Plants](/wiki/Plants "Plants") | [Resources](/wiki/Resources "Resources") | [Gear](/wiki/Gear "Gear") | [Mods](/wiki/Mods "Mods")  
---|---|---|---|---|---|---|---|---  
[Gameplay Menu](/wiki/Gameplay "Gameplay") | [Caravan](/wiki/Caravan "Caravan") | [Combat](/wiki/Combat "Combat") | [Cover](/wiki/Cover "Cover") | [Drafting](/wiki/Drafting "Drafting") | [Environment](/wiki/Environment "Environment") | [Events](/wiki/Events "Events") | [Factions](/wiki/Factions "Factions") | [Firefighting](/wiki/Firefighting "Firefighting") | [Quality](/wiki/Quality "Quality") | [Quests](/wiki/Quests "Quests") | [Research](/wiki/Research "Research") | Rooms | [Time](/wiki/Time "Time") | [Trade](/wiki/Trade "Trade")  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
  
* * *

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This article is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Rooms&action=edit). Reason:** _Needs to clearly and obviously lay out the workspeed penalties._  
---|---  
  
## Contents

  * 1 General
    * 1.1 Temperature
  * 2 Indoors and Outdoors
    * 2.1 List of conditions
  * 3 Roles
    * 3.1 Summary
    * 3.2 Score calculation
    * 3.3 List of roles
  * 4 Stats
    * 4.1 Impressiveness
      * 4.1.1 Guidelines
      * 4.1.2 Formula
        * 4.1.2.1 Base values
        * 4.1.2.2 Modified values
        * 4.1.2.3 Impressiveness score
        * 4.1.2.4 Takeaways
        * 4.1.2.5 Example
    * 4.2 Wealth
    * 4.3 Beauty
    * 4.4 Space
    * 4.5 Cleanliness
  * 5 Map regions
  * 6 Version history
  * 7 Notes



A **room** is a space fully enclosed by impassable objects such as [walls](/wiki/Wall "Wall"), [doors](/wiki/Door "Door") (open or closed), [vents](/wiki/Vent "Vent"), natural rock, or [coolers](/wiki/Cooler "Cooler"). Corners do not need to be filled in order to enclose a room. [Vac barriers](/wiki/Vac_barrier "Vac barrier") also enclose a room despite not being impassable. 

## General[[edit](/index.php?title=Rooms&action=edit&section=1 "Edit section: General")]

The maximum size of a room is 36 map regions. The equivalent size in tiles varies based on the position and shape of the room, but as reference: 

  * The maximum area possible per room is 5,184 tiles (72x72).
  * An empty 50x50 square room is the largest room that won't have issues with map regions.
  * The more complex the shape of a room, the more likely it is to run into problems with map regions.
  * Above this size, the area in question will be treated as a non-room indoors space.



### Temperature[[edit](/index.php?title=Rooms&action=edit&section=2 "Edit section: Temperature")]

Indoor rooms can have a different [temperature](/wiki/Temperature "Temperature") than the outside. Open [doors](/wiki/Door "Door"), open [vents](/wiki/Vent "Vent"), or missing roof tiles will increase the rate at which heat is exchanged with the outside. For further information, see the [Temperature](/wiki/Temperature "Temperature") page. 

Outdoor rooms do not have a separate temperature from the outside environment. They will always match the outside temperature exactly. 

## Indoors and Outdoors[[edit](/index.php?title=Rooms&action=edit&section=3 "Edit section: Indoors and Outdoors")]

Rooms are considered either "indoors" or "outdoors" based on three distinct conditions that do not always agree, which each affect different mechanics. 

### List of conditions[[edit](/index.php?title=Rooms&action=edit&section=4 "Edit section: List of conditions")]

Name  | Condition  | Affected mechanics   
---|---|---  
`UsesOutdoorTemperature` | Any of the following: 

  * 25% or more of the room is unroofed
  * The room is open to the map edge

| 

  * [Temperature](/wiki/Temperature "Temperature")
  * [Deterioration](/wiki/Deterioration "Deterioration")
  * Plants [turning leafless in the cold](/wiki/Plants#Temperature "Plants")
  * Pawns' [outdoors](/wiki/Outdoors "Outdoors") or [indoors](/wiki/Indoors_\(need\) "Indoors \(need\)") needs
  * [Undergrounders](/wiki/Traits#Undergrounder "Traits")' moodlets for being indoors or outdoors

  
`OutdoorsForWork` | Any of the following: 

  * More than 25% of the room is unroofed
  * The room has more than 100 unroofed tiles

| 

  * Stats for certain buildings: 
    * [Surgery success chance](/wiki/Surgery_Success_Chance_Factor#Outdoors_Multiplier "Surgery Success Chance Factor") for [sleep furniture](/wiki/Sleep_furniture "Sleep furniture")
    * [Research speed](/wiki/Research_Speed_Factor "Research Speed Factor") for research benches
    * [Gene assembly speed](/wiki/Assembly_Speed_Factor "Assembly Speed Factor") for [gene assemblers](/wiki/Gene_assembler "Gene assembler")
  * [Throne room](/wiki/Titles#Thrones_and_Bedrooms "Titles") validity

  
`PsychologicallyOutdoors` | Any of the following: 

  * The room has 300 or more unroofed tiles
  * The room is open to the map edge and at least 50% of the room is unroofed

| Most parts of the game, including: 

  * [Beauty](/wiki/Beauty "Beauty")
  * Various forms of [Recreation](/wiki/Recreation "Recreation"), including swimming, skygazing, going for a walk, and building snowmen
  * Spawning of special trees, [ambrosia bushes](/wiki/Ambrosia_bush "Ambrosia bush"), [boomshrooms](/wiki/Boomshroom "Boomshroom"), and [gauranlen pods](/wiki/Gauranlen_pod "Gauranlen pod")
  * Room requirements for [some Ideology buildings](/wiki/Ideoligion#Buildings "Ideoligion")
  * Gatherings, weddings, and other rituals (including some auto-selected locations and the quality of some rituals)
  * Whether you can manually order a pawn to clean a room
  * [Slept outside](/wiki/Thoughts#Misc "Thoughts") moodlet
  * Whether [Acidic smog](/wiki/Acidic_smog "Acidic smog") can apply a negative moodlet
  * Calculations for drop pod and [mech cluster](/wiki/Mech_cluster "Mech cluster") locations
  * Whether the [reading bonus](/wiki/Reading_bonus "Reading bonus") stat applies to actions in the room
  * Whether the 80% multiplier to [work speed](/wiki/Work_Speed_Factor "Work Speed Factor") for being outdoors is applied
  * Whether the penalty for mismatched room role is applied to workbenches

  
  
Note that the lists of affected mechanics are not exhaustive, and that for some of the listed mechanics, the game applies additional conditions to outdoor/indoor checks. 

## Roles[[edit](/index.php?title=Rooms&action=edit&section=5 "Edit section: Roles")]

**Room roles** are assigned to a room based on the buildings they contain, such as a _kitchen_ when containing an [electric stove](/wiki/Electric_stove "Electric stove") or a [fueled stove](/wiki/Fueled_stove "Fueled stove"). They determine whether a colonist is affected by all, some, or none of the room stats. 

### Summary[[edit](/index.php?title=Rooms&action=edit&section=6 "Edit section: Summary")]

Certain room roles grant [moodlets](/wiki/Mood "Mood") based on their [Impressiveness](/wiki/Impressiveness "Impressiveness"), which is affected by all four substats. To gain the moodlet, the room must be used by a pawn for the role's associated purpose (i.e., eating at a table for the dining room role or playing billiards for the rec room role). Despite the game displaying only one role, rooms can grant moodlets from multiple roles when used for that role. The moodlets are typically [When not?] applied when a colonist _begins_ said activity in the room, and they last for 24 hours. [Verify]

Buildings associated with hospitals, laboratories, and kitchens make direct use of the [Cleanliness](/wiki/Cleanliness "Cleanliness") stat for their [Work Speed Factor](/wiki/Work_Speed_Factor "Work Speed Factor"). 

Some room roles cannot have certain buildings inside without inflicting a mood penalty (i.e., [throne rooms](/wiki/Titles#Thrones_and_Bedrooms "Titles") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and temples [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") with [workstations](/wiki/Production "Production")). 

Pawns also have separate needs for [Beauty](/wiki/Beauty "Beauty") and [Space](/wiki/Space "Space"), which every room can fulfill. Unlike the room stats of the same name, these needs are checked within a certain radius from the pawn, as opposed to anywhere in the room. See those pages for further details. 

### Score calculation[[edit](/index.php?title=Rooms&action=edit&section=7 "Edit section: Score calculation")]

For each room, every room role is given a score based on the buildings inside, and the role with the highest score is the one displayed. In the case of a tie, the earlier roles on the following table take priority. 

For the purposes of room role scoring, the following are considered non-baby human beds: [ ancient bed](/wiki/Ancient_bed "Ancient bed"),[ bed](/wiki/Bed "Bed"),[ bedroll](/wiki/Bedroll "Bedroll"),[ double bed](/wiki/Double_bed "Double bed"),[ double bedroll](/wiki/Double_bedroll "Double bedroll"),[ double sleeping spot](/wiki/Double_sleeping_spot "Double sleeping spot"),[ hospital bed](/wiki/Hospital_bed "Hospital bed"),[ royal bed](/wiki/Royal_bed "Royal bed"),[ rusted bed](/wiki/Rusted_bed "Rusted bed")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"),[ rusted double bed](/wiki/Rusted_double_bed "Rusted double bed")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"),[ slab bed](/wiki/Slab_bed "Slab bed")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"),[ slab double bed](/wiki/Slab_double_bed "Slab double bed")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"),[ sleeping spot](/wiki/Sleeping_spot "Sleeping spot"). 

### List of roles[[edit](/index.php?title=Rooms&action=edit&section=8 "Edit section: List of roles")]

Label  | Mood impact  | Related stats  | Score calculation logic   
---|---|---|---  
Room  | None  | None | 

  * Returns a score of 0.99.

  
Bedroom [2] | [Yes](/wiki/Mood#Room_Stats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 0 score if any of the following is true: 
    * There are no human beds.
    * There is at least 1 medical human bed or at least 1 prisoner human bed.
    * There is more than 1 non-assigned human bed.
    * There is at least 1 adult assigned and there are other pawns assigned that are not in its love cluster.[3]
    * There is at least 1 child assigned and there aren't any adults assigned that are a parent of the child.
  * Returns 100,000 score otherwise.

  
Prison cell [2] | [Yes](/wiki/Mood#Situational_RoomStats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 0 score if any of the following is true: 
    * There is at least 1 non-prisoner humanlike bed.
    * There is more than 1 humanlike bed.
  * Returns 170,000 score for a non-medical prisoner humanlike bed.
  * Returns 100,000 score for a medical prisoner humanlike bed.

  
Dining room  | [Yes](/wiki/Mood#Room_Stats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 12 score per each one of the following: [ table (1x2)](/wiki/Table_\(1x2\) "Table \(1x2\)"),[ table (2x2)](/wiki/Table_\(2x2\) "Table \(2x2\)"),[ table (2x4)](/wiki/Table_\(2x4\) "Table \(2x4\)"),[ table (3x3)](/wiki/Table_\(3x3\) "Table \(3x3\)").

  
Rec room  | [Yes](/wiki/Mood#Room_Stats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 7 score per each one of the following: [ billiards table](/wiki/Billiards_table "Billiards table"),[ chess table](/wiki/Chess_table "Chess table"),[ flatscreen television](/wiki/Flatscreen_television "Flatscreen television"),[ game-of-ur board](/wiki/Game-of-Ur_board "Game-of-Ur board"),[ harp](/wiki/Harp "Harp")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"),[ harpsichord](/wiki/Harpsichord "Harpsichord")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"),[ hoopstone ring](/wiki/Hoopstone_ring "Hoopstone ring"),[ horseshoes pin](/wiki/Horseshoes_pin "Horseshoes pin"),[ piano](/wiki/Piano "Piano")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"),[ poker table](/wiki/Poker_table "Poker table"),[ telescope](/wiki/Telescope "Telescope"),[ tube television](/wiki/Tube_television "Tube television").

  
Hospital  | [Yes](/wiki/Mood#Situation_RoomStats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness"), [Cleanliness](/wiki/Room_stats "Room stats") | 

  * Returns 0 score if any of the following is true: 
    * There is at least 1 prisoner humanlike bed.
    * There are no medical humanlike beds.
  * Returns 100,000 score otherwise.

  
Laboratory  | No  | [Cleanliness](/wiki/Room_stats "Room stats") | 

  * Returns 60 score per each one of the following: [ drug lab](/wiki/Drug_lab "Drug lab")[1],[ gene assembler](/wiki/Gene_assembler "Gene assembler")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ gene bank](/wiki/Gene_bank "Gene bank")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ gene extractor](/wiki/Gene_extractor "Gene extractor")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ gene processor](/wiki/Gene_processor "Gene processor")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ growth vat](/wiki/Growth_vat "Growth vat")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ hi-tech research bench](/wiki/Hi-tech_research_bench "Hi-tech research bench")[1],[ large mech gestator](/wiki/Large_mech_gestator "Large mech gestator")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ mech gestator](/wiki/Mech_gestator "Mech gestator")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ serum lab](/wiki/Serum_lab "Serum lab")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")[1],[ simple research bench](/wiki/Simple_research_bench "Simple research bench")[1],[ subcore encoder](/wiki/Subcore_encoder "Subcore encoder")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")[1],[ subcore ripscanner](/wiki/Subcore_ripscanner "Subcore ripscanner")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ subcore softscanner](/wiki/Subcore_softscanner "Subcore softscanner")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC").

  
Workshop  | No  | None  | 

  * Returns 27 score per each one of the following: [ art bench](/wiki/Art_bench "Art bench")[1],[ bioferrite shaper](/wiki/Bioferrite_shaper "Bioferrite shaper")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")[1],[ biofuel refinery](/wiki/Biofuel_refinery "Biofuel refinery")[1],[ brewery](/wiki/Brewery "Brewery")[1],[ electric smelter](/wiki/Electric_smelter "Electric smelter")[1],[ electric smithy](/wiki/Electric_smithy "Electric smithy")[1],[ electric tailor bench](/wiki/Electric_tailor_bench "Electric tailor bench")[1],[ fabrication bench](/wiki/Fabrication_bench "Fabrication bench")[1],[ fueled smithy](/wiki/Fueled_smithy "Fueled smithy")[1],[ hand tailor bench](/wiki/Hand_tailor_bench "Hand tailor bench")[1],[ machining table](/wiki/Machining_table "Machining table")[1],[ stonecutter's table](/wiki/Stonecutter%27s_table "Stonecutter's table")[1]. The [crafting spot](/wiki/Crafting_spot "Crafting spot") does _not_ count.

  
Storeroom  | No  | None  | 

  * Returns 1 score per each one of the following: [ shelf](/wiki/Shelf "Shelf"),[ small shelf](/wiki/Small_shelf "Small shelf").

  
Barracks [2] | [Yes](/wiki/Mood#Room_Stats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 0 score if any of the following is true: 
    * There is at least 1 prisoner humanlike bed.
    * The room is a valid bedroom.
  * Returns 100,100 score for every non-medical humanlike bed otherwise.

  
Prison barracks [2] | [Yes](/wiki/Mood#Situation_RoomStats "Mood") | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 0 score if any of the following is true: 
    * There is at least 1 non-prisoner humanlike bed.
    * There are less than 2 prisoner beds.
  * Returns 100,100 score per non-medical prisoner bed and 50,001 per medical prisoner bed.

  
Kitchen  | No  | [Cleanliness](/wiki/Room_stats "Room stats") | 

  * Returns 28 score per production building that has at least 1 recipe that produces an edible result. The following fulfill the requirement: [ electric stove](/wiki/Electric_stove "Electric stove")[1],[ fueled stove](/wiki/Fueled_stove "Fueled stove")[1]. The [brewery](/wiki/Brewery "Brewery"), [butcher spot](/wiki/Butcher_spot "Butcher spot"), and [butcher table](/wiki/Butcher_table "Butcher table") do _not_ fulfill the requirement.

  
Tomb  | No  | None  | 

  * Returns 50 score per each one of the following: [ sarcophagus](/wiki/Sarcophagus "Sarcophagus").

  
Barn  | No  | None  | 

  * Returns 7.6 score per non-humanlike bed, which are the following: [ animal bed](/wiki/Animal_bed "Animal bed"),[ animal sleeping box](/wiki/Animal_sleeping_box "Animal sleeping box"),[ animal sleeping spot](/wiki/Animal_sleeping_spot "Animal sleeping spot").

  
[Throne room](/wiki/Throne_room "Throne room") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | No  | [Impressiveness](/wiki/Impressiveness "Impressiveness") | 

  * Returns 10,000 score if there is any one of the following: [ grand meditation throne](/wiki/Grand_meditation_throne "Grand meditation throne")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"),[ meditation throne](/wiki/Meditation_throne "Meditation throne")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC").
  * Returns 0 score otherwise.

  
Temple [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [4] | No  | None  | 

  * Returns -1 score if the [Ideology DLC](/wiki/Ideology_DLC "Ideology DLC") is not active.
  * Returns 0 score if there are no altars with the colony's ideology.
  * Returns 75 score per altar with the colony's ideology, with a minimum of 2,000 score. The following are considered altars: [ grand altar](/wiki/Grand_altar "Grand altar")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"),[ large altar](/wiki/Large_altar "Large altar")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"),[ medium altar](/wiki/Medium_altar "Medium altar")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"),[ small altar](/wiki/Small_altar "Small altar")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC").

  
Nursery [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | No  | None  | 

  * Returns 0 score if any of the following is true: 
    * The [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") is not active.
    * There is at least 1 non-medical prisoner bed or at least 1 non-baby bed.
    * There are less than 2 baby beds.
  * Returns 100,200 score per baby bed. The following are considered baby beds: [ baby sleeping spot](/wiki/Baby_sleeping_spot "Baby sleeping spot")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ crib](/wiki/Crib "Crib")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC").

  
Playroom [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | No  | None  | 

  * Returns 0 score if any of the following is true: 
    * The [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") is not active.
    * There is at least 1 humanlike bed in the room.
  * Returns 8 score per each one of the following: [ baby decoration](/wiki/Baby_decoration "Baby decoration")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ toy box](/wiki/Toy_box "Toy box")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC").

  
Classroom [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | No  | None  | 

  * Returns 0 score if any of the following is true: 
    * The [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") is not active.
    * There is at least 1 human bed in the room.
  * Returns 8 score per each one of the following: [ blackboard](/wiki/Blackboard "Blackboard")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"),[ school desk](/wiki/School_desk "School desk")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC").

  
Deathrest chamber [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | Yes  | [Impressiveness](/wiki/Room_stats "Room stats") | 

  * Returns 100 score per [deathrest casket](/wiki/Deathrest_casket "Deathrest casket") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") and 50 score per [deathrest accelerator](/wiki/Deathrest_accelerator "Deathrest accelerator") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"), [glucosoid pump](/wiki/Glucosoid_pump "Glucosoid pump") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"), [hemogen amplifier](/wiki/Hemogen_amplifier "Hemogen amplifier") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"), [hemopump](/wiki/Hemopump "Hemopump") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"), or [psychofluid pump](/wiki/Psychofluid_pump "Psychofluid pump") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC").

  
Containment cell [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | None  | None  | 

  * Returns 100 score per [holding platform](/wiki/Holding_platform "Holding platform") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") or [holding spot](/wiki/Holding_spot "Holding spot") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") and 50 score per [bioferrite harvester](/wiki/Bioferrite_harvester "Bioferrite harvester") ,[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") [electric inhibitor](/wiki/Electric_inhibitor "Electric inhibitor") ,[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") or [electroharvester](/wiki/Electroharvester "Electroharvester") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC").

  
Ceremonial chamber [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | None  | None  | 

  * Returns 200 score per each one of the following: [ psychic ritual spot](/wiki/Psychic_ritual_spot "Psychic ritual spot")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC").

  
  
Other pieces of [furniture](/wiki/Furniture "Furniture") not mentioned, such as [chairs](/wiki/Chair "Chair"), are not considered for score calculation. 

## Stats[[edit](/index.php?title=Rooms&action=edit&section=9 "Edit section: Stats")]

[![Quality preview.png](/images/thumb/7/73/Quality_preview.png/300px-Quality_preview.png)](/wiki/File:Quality_preview.png)

**Room stats** are values of a room that passively affect both [thoughts](/wiki/Thought "Thought") about the room itself and some events and activities that take place within. These include [Impressiveness](/wiki/Impressiveness "Impressiveness"), which is calculated from four composite stats: [Wealth](/wiki/Wealth "Wealth"), [Beauty](/wiki/Beauty "Beauty"), [Space](/wiki/Space "Space"), and [Cleanliness](/wiki/Cleanliness "Cleanliness"). These base stats are automatically calculated from [buildings](/wiki/Buildings "Buildings"), [flooring](/wiki/Floor "Floor"), [filth](/wiki/Filth "Filth"), and the room's perimeter. 

Room stats can be inspected with the room stats display, which can be toggled with a button in the lower right corner of the screen or a hotkey (_G_ by default). Additional information can also be viewed by holding down the _Alt_ key. 

Room stats affect the following: 

  * Medical treatment quality (Cleanliness)
  * Research speed (Cleanliness)
  * [Food poisoning](/wiki/Food_poisoning "Food poisoning") chance in prepared meals (Cleanliness)
  * [Mood](/wiki/Mood#Room_stats "Mood") of the people using them (Impressiveness)



The following traits are affected by room stats: 

  * [Greedy](/wiki/Greedy "Greedy") \- Decrease without sufficiently Impressive bedroom.
  * [Jealous](/wiki/Jealous "Jealous") \- Decrease if anyone has a noticeably better bedroom. [How much?]
  * [Ascetic](/wiki/Ascetic "Ascetic") \- Decrease if room is too Impressive. Increase if bedroom is dull or worse.



### Impressiveness[[edit](/index.php?title=Rooms&action=edit&section=10 "Edit section: Impressiveness")]

The value for **Impressiveness** is based on the four other room stats (**Wealth** , **Beauty** , **Space** , and **Cleanliness**). 

The mood effects from the room depend on the Impressiveness level, and not on the precise value. That value is rounded _down_ to the nearest whole number, and a label (or "level") of Impressiveness will be given to the room, according to the table below. This level is used to apply the relevant thought, positive or negative. 

The exact mood effects depend on the [room role](/wiki/Room#Roles "Room"), with different rooms having different values at each level. For more information, see [this section of the Thoughts page](/wiki/Thoughts#Room_stats "Thoughts"). For bedrooms, dining rooms, and rec rooms, the effects are as follows:[Verify table]

    

     Value  | Description  | Mood impact   
---|---|---  
< 20  | awful  | −2 (bedrooms only)   
>= 20 and < 30  | dull  | _none_  
>= 30 and < 40  | mediocre  | +1 (bedrooms only)   
>= 40 and < 50  | decent  | +2  
>= 50 and < 65  | slightly impressive  | +3  
>= 65 and < 85  | somewhat impressive  | +4  
>= 85 and < 120  | very impressive  | +5  
>= 120 and < 170  | extremely impressive  | +6  
>= 170 and < 240  | unbelievably impressive  | +7  
>= 240  | wondrously impressive  | +8  
  
#### Guidelines[[edit](/index.php?title=Rooms&action=edit&section=11 "Edit section: Guidelines")]

Since the impressiveness calculation (explained below) is fairly involved, it is not practical to predict impressiveness levels in an actual game. However, the following rules of thumb can be applied: 

  * **Keep all four room stats equally in mind.** There is a heavy weighting towards whichever stat is weakest, which is counted as much as all three other stats combined. For example, having a masterpiece work of art in a large room (high _wealth_ , _space_ and _beauty_) is not very effective if the floor is covered in vomit and animal filth (low _cleanliness_). It is quite difficult to compensate for one low stat by raising the other three.


  * **Making a particularly small room _impressive_ is difficult.** Room size is a limiting factor for Impressiveness. If you want to make the room "very impressive", it should have a space of at least around 25 (which still counts as "rather tight" in the game). E.g. a furnished bedroom with a 5x5 or 4×6 footprint would be fine, and a little smaller could still work, but it would be a challenge to get there with a 4x4 room. Note that any naturally "large" rooms like hallways, lobbies, recreation halls etc. will never run into this limitation at all.


  * **Cleanliness matters**. Since the level of impressiveness is what counts, and there are sharp thresholds separating the levels, even a minute change of any of the values can have a strong effect. This is usually due to _cleanliness_ changing (because the other factors are pretty much fixed); even a single speck of dirt on the floor can result in major [mood](/wiki/Mood "Mood") changes. Make sure that the room is not too close to a level threshold, and keep it clean.


  * **Do not go overboard**. There are sharply diminishing returns from increasing any room stat. Increasing any of the stats has dramatically diminishing returns with regards to impressiveness. It is not worth putting a lot of resources into any of the stats beyond a point.*



    

    (* Not unless you care about the stat for other reasons; "room impressiveness" is not the only stat that can affect [mood](/wiki/Mood "Mood"). Beauty, among others, has its own value.)

#### Formula[[edit](/index.php?title=Rooms&action=edit&section=12 "Edit section: Formula")]

The actual formula for calculating impressiveness involves multiple steps, starting with the four room statistics (wealth, beauty, space and cleanliness) and resulting in a single integer value _impressiveness_. 

The calculation is done in several steps: 

  1. Convert each stat into natural units, so that typical in-game stats end up in a range of comparable single digit values.
  2. Curve values beyond (-1, 1) using a natural logarithm.
  3. Average the four stats into an impressiveness score, weighted towards the lowest one
  4. Soft-cap the result according to the space of the room.



Here is a [Desmos graph](https://www.desmos.com/calculator/eepwmhgiwr) with the formula implemented. 

Detailed formula:

##### Base values[[edit](/index.php?title=Rooms&action=edit&section=13 "Edit section: Base values")]

Firstly, all four raw stats are scaled individually by applying a factor, deriving the _base contribution_ for each stat: 

    **W** b = _wealth_ ÷ 1500
    **B** b = _beauty_ ÷ 3
    **S** b = _space_ ÷ 125
    **C** b = 1 + (_cleanliness_ ÷ 2.5)

##### Modified values[[edit](/index.php?title=Rooms&action=edit&section=14 "Edit section: Modified values")]

These base values are now modified if they lie outside the range (−1, 1), by applying the _natural logarithm_ as follows: [Add image]
    
    
    m =  1 + ln(b)          (if b >= 1)
    m = [1 + ln(−b)] × −1   (if b <= −1)
    

(This is symmetrical for positive and negative values). 

##### Impressiveness score[[edit](/index.php?title=Rooms&action=edit&section=15 "Edit section: Impressiveness score")]

These modified values are then combined to give the _impressiveness_ score as follows. 

Take a weighted sum of the average of the values and the smallest of the values: 
    
    
    I = (65 × (**W** m + **B** m + **S** m + **C** m) ÷ 4) + (35 × min(**W** m, **B** m, **S** m, **C** m))
    

This means that the smallest of the values contributes 51.25%, just over half, while the other three values each contribute 16.25%, or 48.75% combined. 

As a final step we compare this impressiveness value to the _spaciousness_ of the room: 
    
    
    S' = 500 × Sm
    If I > S', then
      I' = 0.25 × I + 0.75 × S'
    else
      I' = I (no change)
    

This means a room's max impressiveness is soft-capped to 500% of their space score.[Verify] However, this specific step is only relevant for very small, disproportionately luxurious rooms. Even a 60-space room (S = 0.5) will incur no penalty up to 240 impressiveness, enough to clear the highest bracket ("wondrously impressive"), and a 30-space room (S = 0.24) already reaches "extremely impressive" with no penalty. 

##### Takeaways[[edit](/index.php?title=Rooms&action=edit&section=16 "Edit section: Takeaways")]

It can be useful to think of impressiveness as a percentage value composed of four categories; a score of 1 in each category corresponds to 100 impressiveness, while values above 1 stop giving "fair" (ie. linear) returns. One unit of each stat is equivalent to each the following: 

  * _Wealth_ of 1,500
  * _Beauty_ of 3
  * _Cleanliness_ of 0 (i.e. when using any cleanliness enhancers)
  * _Space_ of 125



Above these values, it begins to become more economical to invest attention in other stats. A "standard bedroom" of size 4×6, carpeted and containing bed, dresser, end table, lamp and plant pot will still have plenty of leeway in all categories (except cleanliness, which is at a natural 0 for a cleaned room); in this case, you will usually proceed by putting a sculpture or high quality armchair in the room, increasing beauty and wealth. 

Furthermore, observe that the factors (i.e., modified values) for _wealth_ and _beauty_ will often be well above 1, but _cleanliness_ and _space_ usually lower than 1. Unless the room is "very spacious", or close to it, the decisive factor will thus be _space_ , then _cleanliness_. In fact, even a well-cleaned room can never have a value over C = 1 (0 cleanliness; perfectly clean) or C = 1.215 (0.6 cleanliness; sterile), meaning rooms above ~100-120 impressiveness will _always_ be bottlenecked by their cleanliness score. This makes "very impressive" (85-120 impressiveness) a natural set point for many rooms. 

##### Example[[edit](/index.php?title=Rooms&action=edit&section=17 "Edit section: Example")]

Start with a room with a _wealth_ of 3000, _space_ of 25, _cleanliness_ of 0, beauty of 3. 

    **W** b = _3000_ ÷ 1500 = 2, but this is curved to 1 + ln(2) = **1.69**
    **B** b = _3_ ÷ 3 = 1
    **S** b = _25_ ÷ 125 = 0.2
    **C** b = 1 + (_0_ ÷ 2.5) = 1

This makes the average score (1.69 + 1 + 0.2 + 1) ÷ 4) = 0.97 and the lowest score 0.2 (space). 

From the above numbers, we can calculate the base Impressiveness 

    I = (65 × 0.97) + (35 × 0.2)
    I = 63 + 7
    I = 70 (70.21 unrounded)

Now, I < 500 × **S** m (70 < 100), so there is no space penalty. Therefore, the reported Impressiveness of the room is 70 or "somewhat impressive" 

If we were to increase the _wealth_ of the above room by 6000 (4 units), our Wm would become 6 -> 1 + ln(6) = 2.79 (+1.1 increase). Wealth wasn't the lowest stat, so this would only improve impressiveness by 1.1*16.25% = 17.9%, resulting in a score of 88 or "very impressive" 

If we were to increase the original room's space by 10 units instead, **S** m becomes 0.28 (0.08 increase). Increasing the bottleneck stat results in a change of 0.08*51.25% = 4.1%, or 74 total impressiveness or "somewhat impressive" 

### Wealth[[edit](/index.php?title=Rooms&action=edit&section=18 "Edit section: Wealth")]

This is the sum of the [Market Value](/wiki/Market_Value "Market Value") of all buildings/furniture/floors(not under doors) in the room and all walls and doors surrounding the room. 
    
    
    Walls, doors, columns and animal flaps in the outer corner count as well. The value of [power conduits](/wiki/Power_conduit "Power conduit") in walls _is_ also included, however, for some reason building or deconstructing a conduit doesn't immediately update room wealth. Only if wealth is recalculated for some other reason, is the value of the conduits included. The same is true when building a column in the outer corner of the wall.
    

Value  | Description   
---|---  
< 500  | impoverished   
>= 500 and < 700  | somewhat poor   
>= 700 and < 2000  | mediocre   
>= 2000 and < 4000  | somewhat rich   
>= 4000 and < 10000  | rich   
>= 10000 and < 40000  | luxurious   
>= 40000 and < 100000  | very luxurious   
>= 100000 and < 1000000  | extremely luxurious   
>= 1000000  | unbelievably luxurious   
  
### Beauty[[edit](/index.php?title=Rooms&action=edit&section=19 "Edit section: Beauty")]

This is the average environmental beauty of the room including its walls and doors with a penalty for small rooms. Walls, doors and columns in the outer corner count as well. Building or deconstructing a column in the outer corner doesn't trigger a recalculation however. Floor tiles underneath walls and doors have no influence. 

Room beauty is calculated as: 
    
    
    TotalBeauty = sum(beauty for each internal cell) + sum(beauty for each adjacent cell)
    WeightedSize = size if (size > 40) else (20 + size / 2)
    RoomBeauty = TotalBeauty / WeightedSize

This means that all rooms with less than 40 internal space will have their beauty penalised. 

Value  | Description   
---|---  
< -3.5  | hideous   
>= -3.5 and < 0  | ugly   
>= 0 and < 2.4  | neutral   
>= 2.4 and < 5  | pretty   
>= 5 and < 15  | beautiful   
>= 15 and < 50  | very beautiful   
>= 50 and < 100  | extremely beautiful   
>= 100  | unbelievably beautiful   
  
### Space[[edit](/index.php?title=Rooms&action=edit&section=20 "Edit section: Space")]

Indicates how much free space is available in the room. A room's Space score is 1.4 times the number of tiles in the room. Objects that prevent a pawn from standing in a space will decrease the available space in the room by 0.9 per tile the object covers. Thus, an occupied tile contributes a total of 0.5 to space. Objects that reduce space include beds, tables, workbenches, lamps, and heaters. Stools and chairs do not reduce space. 

Value  | Description  | typical size*   
---|---|---  
< 12.5  | cramped  | 3x4 or smaller*   
>= 12.5 and < 29  | rather tight  | 3x6, 4x5*   
>= 29 and < 55  | average-sized  | 4x7, 5x6*   
>= 55 and < 70  | somewhat spacious   
>= 70 and < 130  | quite spacious   
>= 130 and < 349.5  | very spacious   
>= 349.5  | extremely spacious   
  
    (* These are "safe" approximations; as described, the items placed _in_ the room can greatly reduce the effective size. For example, an empty 5x5 room has space (25 x 1.4 =) 35, easily "average" - when empty. However, placing just one bed (2 tiles), one table (2 tiles), a light, a heater, a plant pot and one artwork (1 tile each, a chair is "free") in that room reduces the effective space by -7.2 (= 8 tiles x .9), and the effective space is now 27.8, "rather tight".)
    (* Due to floating point inaccuracies, sometimes a room that is right on a threshold may randomly count for one category or the other. For example, a room with 5 standable tiles and 11 walkable but non-standable tiles should come out to exactly 12.5 score, but may result in either "cramped" or "rather tight". It's safest to not rely on exact values.)

Note, that space of the room affects only its impressiveness. Careful to not confuse with Pawn's [space](/wiki/Space "Space") need. 

### Cleanliness[[edit](/index.php?title=Rooms&action=edit&section=21 "Edit section: Cleanliness")]

This section is about the cleanliness of rooms. For the cleanliness stat of individual objects, see [Cleanliness (Stat)](/wiki/Cleanliness_\(Stat\) "Cleanliness \(Stat\)").

A rooms cleanliness affects [surgery success chance](/wiki/Surgery_Success_Chance_Factor#Room_Cleanliness_Multiplier "Surgery Success Chance Factor"), [research speed](/wiki/Research#Research_speed "Research"), the chance that cooked meals will cause [food poisoning](/wiki/Food_poisoning "Food poisoning"), and gene [Assembly Speed Factor](/wiki/Assembly_Speed_Factor "Assembly Speed Factor").[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") A room's cleanliness is the average cleanliness score of all tiles in the room. It is determined by the type of [flooring](/wiki/Floor "Floor"), the presence of any [filth](/wiki/Filth "Filth"), and the cleanliness value of some furniture such as the [butcher table](/wiki/Butcher_table "Butcher table") and the [stonecutter's table](/wiki/Stonecutter%27s_table "Stonecutter's table"). Note that the type of [floor](/wiki/Floor "Floor") under a door doesn't count for cleanliness, but filth under a door does count. 

    

    

     Room Cleanliness  | Description   
---|---  
< -1.1  | very dirty   
>= -1.1 and < -0.4  | dirty   
>= -0.4 and < -0.05  | slightly dirty   
>= -0.05 and < 0.4  | clean   
>= 0.4  | sterile   
  
     Surface  | Cleanliness  
Value   
---|---  
[Void metal ](/wiki/Void_metal "Void metal")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | 1   
[Sterile tile](/wiki/Sterile_tile "Sterile tile") floor | 0.6   
[Steel](/wiki/Steel_tile "Steel tile"), [Silver](/wiki/Silver_tile "Silver tile") or [Gold](/wiki/Gold_tile "Gold tile") floor | 0.2   
[Bioferrite plate](/wiki/Bioferrite_plate "Bioferrite plate")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | 0.2   
all other constructed [flooring](/wiki/Floor "Floor"); [Bridges](/wiki/Bridge "Bridge") | 0   
Natural stone ([rough](/wiki/Rough_stone "Rough stone") or [smoothed](/wiki/Smooth_stone "Smooth stone")) | 0   
[Straw matting](/wiki/Straw_matting "Straw matting") | -0.1   
all other [natural surfaces](/wiki/Environment#Terrain "Environment") (soil, gravel, etc.) | -1   
[Marsh](/wiki/Marsh "Marsh"), [Marshy soil](/wiki/Marshy_soil "Marshy soil"), [Mud](/wiki/Mud "Mud"), [Broken asphalt](/wiki/Broken_asphalt "Broken asphalt") | -2   
[Chunks](/wiki/Chunk "Chunk") | -2   
[Flesh](/wiki/Flesh "Flesh")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | -3   
[Dirt, rubble, all other filth](/wiki/Filth "Filth") | -5   
[Blood](/wiki/Filth "Filth") | -10   
[Insect blood, vomit, fuel puddle](/wiki/Filth "Filth") | -15   
[Corpsebile](/wiki/Filth "Filth") | -20   
  
Using "Toggle the beauty display" can help locate filth in a given room, which typically stands out due to its negative beauty. 

## Map regions[[edit](/index.php?title=Rooms&action=edit&section=22 "Edit section: Map regions")]

Upon map generation, the map is divided into chunks of 12x12 squares called map regions. Each region requires a contiguous area and will be subdivided otherwise. Under no circumstance will a region extend beyond the initial 12x12 grid. Impassable buildings (both natural and artificial) are not considered as part of any map region for this purpose and will subdivide existing map regions accordingly. Regions will fuse when possible. Map regions are used for several calculations and can be seen in game via the debug option "Draw Regions". 

Some additional notes:

  * Impassable buildings are never part of any map region. 
    * Impassable non-walls (ex: [Ship engine](/wiki/Ship_engine "Ship engine")) may create a "red" temporal map region on construction that will be removed once anything else is build/destroyed.
  * Impassable terrain creates map regions confined to its extension. 
    * These regions don't interact with the regular ones, but otherwise follow the stated rules.
  * Passable buildings, such as [fences](/wiki/Fence "Fence") and [barricades](/wiki/Barricade "Barricade"), create map regions along their extension. 
    * These "fence" regions won't interact with other kinds, but otherwise follow the stated rules.
  * Doors have unique behavior 
    * Single tile doors create a 3 tile map region centered on the doors' tile, following the door's orientation, that overlaps with other map regions. 
      * Impassable objects will delete the overlapping section, no interaction otherwise.
    * Double tile doors create 2 map regions, 1 for each of its tiles.
    * The map regions created by doors don't interact with any other, not even each other.
  * The grid defining regions is drawn from the bottom-left of the map row by row.



## Version history[[edit](/index.php?title=Rooms&action=edit&section=23 "Edit section: Version history")]

  * [0.12.906](/wiki/Version/0.12.906 "Version/0.12.906") \- Added.
  * 1.1 - Added room stats gizmo, which displays the stats of the room containing a selected building, at a glance.
  * [Royalty DLC](/wiki/Royalty_DLC "Royalty DLC") release - Throne room role added.
  * [Ideology DLC](/wiki/Ideology_DLC "Ideology DLC") release - Temple room role added.
  * [1.3.3072](/wiki/Version/1.3.3072 "Version/1.3.3072") \- Fix: Checking all beds instead of just humanlike ones for room owner.
  * [1.4.3523](/wiki/Version/1.4.3523 "Version/1.4.3523") \- Added the storeroom role for rooms with lots of shelves.
  * [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") release - Nursery, playroom, classroom, and deathrest chamber roles added.
  * [Anomaly DLC](/wiki/Anomaly_DLC "Anomaly DLC") release - Containment cell and ceremonial chamber roles added.
  * [1.6.4518](/wiki/Version/1.6.4518 "Version/1.6.4518") \- Some production buildings now have a work speed penalty if they are not in the correct room.



## Notes[[edit](/index.php?title=Rooms&action=edit&section=24 "Edit section: Notes")]

  1. ↑ 1.00 1.01 1.02 1.03 1.04 1.05 1.06 1.07 1.08 1.09 1.10 1.11 1.12 1.13 1.14 1.15 1.16 1.17 1.18 1.19 Work speed penalty of 80% if not placed in the room with the correct role.
  2. ↑ 2.0 2.1 2.2 2.3 This role will have its owners' name added to its name.
  3. ↑ A pawn's love cluster is all the other pawns that can be linked to the pawn through a chain of romantic relationships.
  4. ↑ This role changes to the ideoligion's set temple name.



Retrieved from "[https://rimworldwiki.com/index.php?title=Rooms&oldid=184121#Roles](https://rimworldwiki.com/index.php?title=Rooms&oldid=184121#Roles)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Game mechanics](/wiki/Category:Game_mechanics "Category:Game mechanics")



Hidden category: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Rooms "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Rooms "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Rooms "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Rooms&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Rooms)
  * [Edit](/index.php?title=Rooms&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Rooms&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Rooms "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Rooms "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Rooms&oldid=184121 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Rooms&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Rooms)



  * This page was last edited on 25 September 2026, at 23:05.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: RGB: (255, 150, 100)
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[28.33 secs]: real-time at 1x speed
  *[Nutrition]: Nutrition gained when this item or object is eaten
  *[Maximum To Ingest]: Maximum Number To Ingest At Once
  *[1.33 secs]: real-time at 1x speed
  *[+4]: Stacking 1 times for a maximum of 4
  *[_Nuzzled_]: It is so cute, and supportive, and loving... I feel fulfilled and refreshed.
  *[+5]: Stacking 1 times for a maximum of 5
  *[_[Bonded animal]'s master_]: Being together with my bonded animal makes me feel better.
  *[−3]: Stacking 5 times with a 0.75 multiplier for maximum of -9
  *[_Not [Bonded animal]'s master_]: I should be together with my bonded animal.
  *[4]: Stacking 3 times with a 0.5 multiplier for maximum of 7
  *[10 secs]: real-time at 1x speed
  *[HP]: Hit Points
  *[5 mins]: real-time at 1x speed
  *[8.33 mins]: real-time at 1x speed
  *[29.17 mins]: real-time at 1x speed
  *[12.5 mins]: real-time at 1x speed
  *[4.5 mins]: real-time at 1x speed
  *[6.5 mins]: real-time at 1x speed
  *[5.75 mins]: real-time at 1x speed
  *[7.5 mins]: real-time at 1x speed
  *[11 mins]: real-time at 1x speed
  *[5.5 mins]: real-time at 1x speed
  *[7 mins]: real-time at 1x speed
  *[9.5 mins]: real-time at 1x speed
  *[3.5 mins]: real-time at 1x speed
  *[20.83 mins]: real-time at 1x speed
  *[10.83 mins]: real-time at 1x speed
  *[9.58 mins]: real-time at 1x speed
  *[18.33 mins]: real-time at 1x speed
  *[9.17 mins]: real-time at 1x speed
  *[11.67 mins]: real-time at 1x speed
  *[15.83 mins]: real-time at 1x speed
  *[5.83 mins]: real-time at 1x speed
  *[72.92 mins]: real-time at 1x speed
  *[26.25 mins]: real-time at 1x speed
  *[37.92 mins]: real-time at 1x speed
  *[33.54 mins]: real-time at 1x speed
  *[43.75 mins]: real-time at 1x speed
  *[64.17 mins]: real-time at 1x speed
  *[32.08 mins]: real-time at 1x speed
  *[40.83 mins]: real-time at 1x speed
  *[55.42 mins]: real-time at 1x speed
  *[20.42 mins]: real-time at 1x speed
  *[[Note]]: This value is automatically calculated by the wiki and may not be correct
  *[13.33 secs]: real-time at 1x speed
  *[Deconstruct yield]: Resources recovered when deconstructing.
  *[Destroy yield]: Resources recovered when destroyed.
  *[Stuff Tags]: The types of resource that can be substituted for the generic resource type
  *[12 secs]: real-time at 1x speed
  *[1.37 mins]: real-time at 1x speed
  *[1.11 mins]: real-time at 1x speed
  *[1.26 mins]: real-time at 1x speed
  *[29.33 secs]: real-time at 1x speed
  *[1.15 mins]: real-time at 1x speed
  *[25.33 secs]: real-time at 1x speed
  *[9.33 secs]: real-time at 1x speed
  *[33.33 secs]: real-time at 1x speed
  *[1.22 mins]: real-time at 1x speed
  *[0 secs]: real-time at 1x speed
  *[AP]: Armor Penetration
  *[DPS]: damage per second
  *[+10]: Stacking 1 times for a maximum of 10
  *[_Alcohol warmth_]: I just feel a bit more relaxed after that drink. That's good.
  *[+14]: Stacking 1 times for a maximum of 14
  *[_Quite inebriated_]: I'm a bit wobbly! And this is quite enjoyable.
  *[+20]: Stacking 1 times for a maximum of 20
  *[_Drunk_]: I feel so uninhibited and unafraid! This is a great time!
  *[+26]: Stacking 1 times for a maximum of 26
  *[_Hammered_]: Wooo! What's going on?
  *[−12]: Stacking 1 times for a maximum of -12
  *[_Pounding hangover_]: It feels like a gaggle of geese are pecking at my skull.
  *[−6]: Stacking 1 times for a maximum of -6
  *[_Serious hangover_]: My head hurts from all that liquor.
  *[_Mild hangover_]: The headache is almost gone.
  *[7.22 mins]: real-time at 1x speed
  *[41.67 secs]: real-time at 1x speed
  *[66.67 mins]: real-time at 1x speed
  *[1.25 mins]: real-time at 1x speed
  *[1 sec]: real-time at 1x speed
  *[14 mins]: real-time at 1x speed
  *[22.22 mins]: real-time at 1x speed
  *[10.85 mins]: real-time at 1x speed
  *[17.23 mins]: real-time at 1x speed
  *[4.07 mins]: real-time at 1x speed
  *[6.46 mins]: real-time at 1x speed
  *[1.81 mins]: real-time at 1x speed
  *[2.87 mins]: real-time at 1x speed
  *[33.68 secs]: real-time at 1x speed
  *[53.47 secs]: real-time at 1x speed
  *[50 secs]: real-time at 1x speed
  *[8.33 secs]: real-time at 1x speed
  *[2.78 mins]: real-time at 1x speed
  *[58.33 secs]: real-time at 1x speed
  *[2.08 mins]: real-time at 1x speed
  *[2.22 mins]: real-time at 1x speed
  *[3.33 mins]: real-time at 1x speed
  *[MTB]: Mean or average time between occurrences
  *[5 secs]: real-time at 1x speed
  *[15 secs]: real-time at 1x speed
  *[4.17 mins]: real-time at 1x speed
  *[25 mins]: real-time at 1x speed
  *[41.67 mins]: real-time at 1x speed
  *[+6]: Stacking 1 times for a maximum of 6
  *[_Bonded animal'smaster_]: Being together with my bonded animal makes me feel better.
  *[_Not bonded animal's master_]: I should be together with my bonded animals.
  *[−10]: Stacking 1 times for a maximum of -10
  *[_Bonded animal given away_]: My special bonded animal was given away!
  *[−8]: Stacking 1 times for a maximum of -8
  *[_Bonded animal died_]: Such a tender, unique animal. This universe is evil!
  *[_Bonded animal lost_]: Such a tender, unique animal. This universe is evil!
  *[_Bonded animal banished_]: My bonded animal was banished!
  *[−5]: Stacking 1 times for a maximum of -5
  *[_Bonded animal released_]: Such a tender, unique animal. Why did it have to go?
  *[12 in-game days]: there are 60,000 ticks in a day
  *[6 in-game days]: there are 60,000 ticks in a day
  *[Move Speed]: c/s
  *[Haul Throughput]: c*i/s
  *[Hunger Rate]: Nutrition
  *[Juvenile Age]: days
  *[Maturity Age]: days
  *[Min Temperature]: °C
  *[Max Temperature]: °C
  *[Needed  
Males / Female]: Assuming they sleep on the ground and mate as soon as possible.
  *[Tameness Decay Interval (Days)]: The tameness of animals that are blocked by fences or that have low enough wildness does not decay
  *[Males / Female]: Assuming they sleep on the ground and mate as soon as possible.
  *[Meat Nutrition / Day]: Units of nutrition of meat produced per female per day when adults are slaughtered, assuming constant pregnancy.
  *[Consumption / Day]: Units of nutrition consumed per day by one adult plus the nutrition consumed by the required males per female, including the offspring's consumption up to adulthood.
  *[Meat Nutrition Efficiency]: Meat Nutrition/Consumption
  *[_Darkness_]: I've been in the dark for a while. I don't like it.
  *[+16]: Stacking 1 times for a maximum of 16
  *[_Night owl at night_]: I feel much better at night.
  *[_Night owl in daytime_]: I don't like working during the day.
  *[+3]: Stacking 1 times for a maximum of 3
  *[_Undergrounder indoors_]: I like working or simply being indoors.
  *[_Underground_]: I love working or simply being in the underground.
  *[_Undergrounder outdoors_]: I don't like being outside. I want to get back to the underground.
  *[_Happily nude_]: I'm nude and loving it! I feel so free and unconstrained and in touch with my surroundings!
  *[_Constraining clothes_]: I'm a nudist but I have to wear these clothes. It's not unbearable - but I still feel constrained and uncomfortable.
  *[_Masochist in pain_]: Ow... heh heh heh... I could get used to this!/Ughhh... it hurts, but I love it! Keep it coming!/Ouch... I think something's broken... but what an exquisite feeling!/Ahhh... am I in heaven?
  *[_Masochist body strapped_]: The straps press in and calm my soul.
  *[+2]: Stacking 4 times for a maximum of 8
  *[_Masochist collared_]: Such restrictive discomfort... delightful.
  *[_Fed on by OTHER_]: I was violated by a bloodfeeder like some kind of livestock.
  *[_Body modder pleased_]: This artificial enhancement is cool. I want more./Two artificial enhancements are better than one. I wish I had more./Three artificial enhancements, and my weak human flesh is receding. But I still want more machine power./Four artificial enhancements and I am becoming more than human. But there's still some flesh that needs replacing./Five artificial enhancements! How could an enhanced being like me ever feel sad?/I asked for this.
  *[−4]: Stacking 1 times for a maximum of -4
  *[_Body modder frustrated_]: Flesh is so limiting. I wish I had some kind of artificial body part.
  *[_Body purist squeamish_]: I hate having this unnatural enhancement. I feel filthy!/Two artificial enhancements are sullying my natural, pure body. It makes me sick to think of it./Three artificial enhancements violate my body's pure flesh. I shudder when I think of it... and these objects shudder with me./I have four artificial enhancements; it's like I'm becoming a robot. What a horrifying sensation./Five artificial enhancements... Is there anything left of me? Or am I just a robot that thinks it's human?/I asked for the exact opposite of this!
  *[−20]: Stacking 1 times for a maximum of -20
  *[_Forced to take luciferium_]: I'm a body purist; I would never take luciferium by choice. But I was forced! I feel unclean.
  *[_Ate without table_]: I had to eat a meal off the ground. Can't we get a table around here?
  *[_Ascetic has awful-mediocre bedroom_]: My bedroom is just how I want it to be. Very humble and simple./My bedroom is just how I want it to be. Very humble and simple./My bedroom is very humble and simple. I like it.
  *[_Ascetic has impressive bedroom_]: I don't like having an impressive bedroom.
  *[_Greedy for impressive bedroom_]: I'm greedy. My room is pathetic! I want a really impressive bedroom./I'm greedy. My room isn't nearly good enough. I want a really impressive bedroom./I'm greedy. My room isn't good enough. I want a really impressive bedroom./I'm greedy. My room isn't quite good enough. I want a really impressive bedroom.
  *[_Jealous of OTHER's bedroom_]: I need to have the best one!
  *[_Pyromaniac has incendiary weapon_]: It makes me think of flame and fire. I can't wait to use it.
  *[+8]: Stacking 5 times with a 0.75 multiplier for maximum of 24
  *[_Used flame weapon_]: The searing heat will make my foes beautiful!
  *[_Beautiful fire_]: The sinuous flame dances, warm like love, bright like freedom, all-consuming.
  *[_Human leather APPAREL_NAME_]: I enjoy wearing the suffering of others./This will scare them. All will know my power./The faces on my clothes aren't smiling, but they make *me* happy./The flesh! The flesh signals my triumph!
  *[_Bloodlust organ harvested_]: Extracting the flesh from their bodies is so bloody and satisfying.
  *[_Witnessed death with bloodlust_]: I saw someone die! That was intense!
  *[+12]: Stacking 1 times for a maximum of 12
  *[_Killed someone_]: I killed someone! What a rush!
  *[+15]: Stacking 1 times for a maximum of 15
  *[_Cooked cannibalism_]: I ate a meal made from the meat of another human. So pleasurable. If only I had some fava beans and a nice chianti.
  *[_Raw cannibalism_]: I ate the meat of another human, raw, like an animal. It was so... succulent.
  *[_Ate corpse_]: I had to eat the flesh of a dead creature without even butchering or cooking it.
  *[_Brawler has ranged weapon_]: I hate shooting from a distance. I want to get up close and personal!
  *[_Tortured artist_]: Natural penalty from 'tortured artist' trait.
  *[_Kind words_]: I've been bestowed with kind words! What a nice person!
  *[_Denied joining_]: We just denied someone's request to join us. I hope they make it.
  *[_Chemical hunger_]: I'm interested in drugs. I want to try more./I'm interested in drugs. I want to experience a lot more./I'm interested in drugs. I want to consume drugs really badly.
  *[_Chemical satisfaction_]: I'm interested in drugs. I enjoyed satisfying my desire./I'm interested in drugs. I am really satisfied with all the drugs I've gotten recently.
  *[_Forced to take drugs_]: I'm a teetotaler; I would never take drugs by choice. But I was forced! I feel unclean.
  *[c/s]: cells per second
  *[_Sanguine_]: Natural bonus from 'sanguine' trait.
  *[_Optimist_]: Natural bonus from 'optimist' trait.
  *[_Pessimist_]: Natural penalty from 'optimist' trait.
  *[_Depressive_]: Natural penalty from 'optimist' trait.
  *[−2]: Stacking 20 times with a 0.75 multiplier for maximum of -8
  *[_OTHER rambling_]: OTHER is talking nonsense. Is s/he insane?
  *[_Captured entity_]: Such a magnificent creature. So much mystery. So much power.
  *[Work to clean]: Ticks required to clean 1 layer of the filth
  *[Days to disappear]: Will automatically disappear after this many days
  *[26.67 secs]: real-time at 1x speed
  *[_Slept in the heat_]: I had to sleep in unbearable heat. Can't we have air conditioning?
  *[8 in-game days]: there are 60,000 ticks in a day
  *[15 in-game days]: there are 60,000 ticks in a day
  *[30 in-game days]: there are 60,000 ticks in a day
  *[2 quadrums]: there are 900,000 ticks in a quadrum
  *[40 in-game days]: there are 60,000 ticks in a day
  *[XP Factor]: Potency * 0.7, clamped at 0.5 and 1.0.
  *[Human]: 500 * XP Factor
  *[Animal]: 175 * XP Factor
  *[4.17 secs]: real-time at 1x speed
  *[5.83 secs]: real-time at 1x speed
  *[6.67 secs]: real-time at 1x speed
  *[7.5 secs]: real-time at 1x speed
  *[3.33 secs]: real-time at 1x speed
  *[1 in-game hour]: there are 2,500 ticks in an hour
  *[Bulk Product Amount]: The amount of this item produced by the bulk recipe
  *[_Ate fine meal_]: I ate a really tasty fine meal. Yum!
  *[_Ate lavish meal_]: That lavish meal was amazing. It nourished my body and my soul.
  *[10.83 secs]: real-time at 1x speed
  *[9.72 mins]: real-time at 1x speed
  *[_Ate kibble_]: I had to eat animal kibble. It's like I don't get to be human any more.
  *[Light Radius]: The furthest away a tile can be before it falls below 30% light
  *[16.67 secs]: real-time at 1x speed
