Rooms - RimWorld Wiki
 
 
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
- 
 

 
 

 
 

 

 Rooms

 
 From RimWorld Wiki

 (Redirected from Hospital)

 

 
 

 Jump to navigation
 Jump to search
 &#91;1&#93;

Basics

Menus

Game&#160;Creation

Gameplay

Pawns

Plants

Resources

Gear

Mods

Gameplay&#160;Menu

Caravan

Combat

Cover

Drafting

Environment

Events

Factions

Firefighting

Quality

Quests

Research

Rooms

Time

Trade

This article is a stub. You can help RimWorld Wiki by expanding it. Reason: Needs to clearly and obviously lay out the workspeed penalties.

Contents

- 1 General

- 1.1 Temperature

- 2 Indoors and Outdoors

- 2.1 List of conditions

- 3 Roles

- 3.1 Summary

- 3.2 Score calculation

- 3.3 List of roles

- 4 Stats

- 4.1 Impressiveness

- 4.1.1 Guidelines

- 4.1.2 Formula

- 4.1.2.1 Base values

- 4.1.2.2 Modified values

- 4.1.2.3 Impressiveness score

- 4.1.2.4 Takeaways

- 4.1.2.5 Example

- 4.2 Wealth

- 4.3 Beauty

- 4.4 Space

- 4.5 Cleanliness

- 5 Map regions

- 6 Version history

- 7 Notes

A room is a space fully enclosed by impassable objects such as walls, doors (open or closed), vents, natural rock, or coolers. Corners do not need to be filled in order to enclose a room. Vac barriers also enclose a room despite not being impassable.

General[edit]

The maximum size of a room is 36 map regions. The equivalent size in tiles varies based on the position and shape of the room, but as reference:

- The maximum area possible per room is 5,184 tiles (72x72).

- An empty 50x50 square room is the largest room that won't have issues with map regions.

- The more complex the shape of a room, the more likely it is to run into problems with map regions.

- Above this size, the area in question will be treated as a non-room indoors space.

Temperature[edit]

Indoor rooms can have a different temperature than the outside. Open doors, open vents, or missing roof tiles will increase the rate at which heat is exchanged with the outside. For further information, see the Temperature page.

Outdoor rooms do not have a separate temperature from the outside environment. They will always match the outside temperature exactly.

Indoors and Outdoors[edit]

Rooms are considered either "indoors" or "outdoors" based on three distinct conditions that do not always agree, which each affect different mechanics.

List of conditions[edit]

Name

Condition

Affected mechanics

UsesOutdoorTemperature

Any of the following:
- 25% or more of the room is unroofed

- The room is open to the map edge

- Temperature

- Deterioration

- Plants turning leafless in the cold

- Pawns' outdoors or indoors needs

- Undergrounders' moodlets for being indoors or outdoors

OutdoorsForWork

Any of the following:
- More than 25% of the room is unroofed

- The room has more than 100 unroofed tiles

- Stats for certain buildings:
- Surgery success chance for sleep furniture

- Research speed for research benches

- Gene assembly speed for gene assemblers

- Throne room validity

PsychologicallyOutdoors

Any of the following:
- The room has 300 or more unroofed tiles

- The room is open to the map edge and at least 50% of the room is unroofed

Most parts of the game, including:
- Beauty

- Various forms of Recreation, including swimming, skygazing, going for a walk, and building snowmen

- Spawning of special trees, ambrosia bushes, boomshrooms, and gauranlen pods

- Room requirements for some Ideology buildings

- Gatherings, weddings, and other rituals (including some auto-selected locations and the quality of some rituals)

- Whether you can manually order a pawn to clean a room

- Slept outside moodlet

- Whether Acidic smog can apply a negative moodlet

- Calculations for drop pod and mech cluster locations

- Whether the reading bonus stat applies to actions in the room

- Whether the 80% multiplier to work speed for being outdoors is applied

- Whether the penalty for mismatched room role is applied to workbenches

Note that the lists of affected mechanics are not exhaustive, and that for some of the listed mechanics, the game applies additional conditions to outdoor/indoor checks.

Roles[edit]

Room roles are assigned to a room based on the buildings they contain, such as a kitchen when containing an electric stove or a fueled stove. They determine whether a colonist is affected by all, some, or none of the room stats.

Summary[edit]

Certain room roles grant moodlets based on their Impressiveness, which is affected by all four substats. To gain the moodlet, the room must be used by a pawn for the role's associated purpose (i.e., eating at a table for the dining room role or playing billiards for the rec room role). Despite the game displaying only one role, rooms can grant moodlets from multiple roles when used for that role. The moodlets are typically [When not?] applied when a colonist begins said activity in the room, and they last for 24 hours. [Verify]

Buildings associated with hospitals, laboratories, and kitchens make direct use of the Cleanliness stat for their Work Speed Factor.

Some room roles cannot have certain buildings inside without inflicting a mood penalty (i.e., throne rooms and temples with workstations).

Pawns also have separate needs for Beauty and Space, which every room can fulfill. Unlike the room stats of the same name, these needs are checked within a certain radius from the pawn, as opposed to anywhere in the room. See those pages for further details.

Score calculation[edit]

For each room, every room role is given a score based on the buildings inside, and the role with the highest score is the one displayed. In the case of a tie, the earlier roles on the following table take priority.

For the purposes of room role scoring, the following are considered non-baby human beds: ancient bed, bed, bedroll, double bed, double bedroll, double sleeping spot, hospital bed, royal bed, rusted bed, rusted double bed, slab bed, slab double bed, sleeping spot.

List of roles[edit]

Label

Mood impact

Related stats

Score calculation logic

Room

None

None

- Returns a score of 0.99.

Bedroom &#91;2&#93;

Yes

Impressiveness

- Returns 0 score if any of the following is true:
- There are no human beds.

- There is at least 1 medical human bed or at least 1 prisoner human bed.

- There is more than 1 non-assigned human bed.

- There is at least 1 adult assigned and there are other pawns assigned that are not in its love cluster.&#91;3&#93;

- There is at least 1 child assigned and there aren't any adults assigned that are a parent of the child.

- Returns 100,000 score otherwise.

Prison cell &#91;2&#93;

Yes

Impressiveness

- Returns 0 score if any of the following is true:
- There is at least 1 non-prisoner humanlike bed.

- There is more than 1 humanlike bed.

- Returns 170,000 score for a non-medical prisoner humanlike bed.

- Returns 100,000 score for a medical prisoner humanlike bed.

Dining room

Yes

Impressiveness

- Returns 12 score per each one of the following: table (1x2), table (2x2), table (2x4), table (3x3).

Rec room

Yes

Impressiveness

- Returns 7 score per each one of the following: billiards table, chess table, flatscreen television, game-of-ur board, harp, harpsichord, hoopstone ring, horseshoes pin, piano, poker table, telescope, tube television.

Hospital

Yes

Impressiveness, Cleanliness

- Returns 0 score if any of the following is true:
- There is at least 1 prisoner humanlike bed.

- There are no medical humanlike beds.

- Returns 100,000 score otherwise.

Laboratory

No

Cleanliness

- Returns 60 score per each one of the following: drug lab&#91;1&#93;, gene assembler, gene bank, gene extractor, gene processor, growth vat, hi-tech research bench&#91;1&#93;, large mech gestator, mech gestator, serum lab&#91;1&#93;, simple research bench&#91;1&#93;, subcore encoder&#91;1&#93;, subcore ripscanner, subcore softscanner.

Workshop

No

None

- Returns 27 score per each one of the following: art bench&#91;1&#93;, bioferrite shaper&#91;1&#93;, biofuel refinery&#91;1&#93;, brewery&#91;1&#93;, electric smelter&#91;1&#93;, electric smithy&#91;1&#93;, electric tailor bench&#91;1&#93;, fabrication bench&#91;1&#93;, fueled smithy&#91;1&#93;, hand tailor bench&#91;1&#93;, machining table&#91;1&#93;, stonecutter's table&#91;1&#93;. The crafting spot does not count.

Storeroom

No

None

- Returns 1 score per each one of the following: shelf, small shelf.

Barracks &#91;2&#93;

Yes

Impressiveness

- Returns 0 score if any of the following is true:
- There is at least 1 prisoner humanlike bed.

- The room is a valid bedroom.

- Returns 100,100 score for every non-medical humanlike bed otherwise.

Prison barracks &#91;2&#93;

Yes

Impressiveness

- Returns 0 score if any of the following is true:
- There is at least 1 non-prisoner humanlike bed.

- There are less than 2 prisoner beds.

- Returns 100,100 score per non-medical prisoner bed and 50,001 per medical prisoner bed.

Kitchen

No

Cleanliness

- Returns 28 score per production building that has at least 1 recipe that produces an edible result. The following fulfill the requirement: electric stove&#91;1&#93;, fueled stove&#91;1&#93;. The brewery, butcher spot, and butcher table do not fulfill the requirement.

Tomb

No

None

- Returns 50 score per each one of the following: sarcophagus.

Barn

No

None

- Returns 7.6 score per non-humanlike bed, which are the following: animal bed, animal sleeping box, animal sleeping spot.

Throne room 

No

Impressiveness

- Returns 10,000 score if there is any one of the following: grand meditation throne, meditation throne.

- Returns 0 score otherwise.

Temple &#91;4&#93;

No

None

- Returns -1 score if the Ideology DLC is not active.

- Returns 0 score if there are no altars with the colony's ideology.

- Returns 75 score per altar with the colony's ideology, with a minimum of 2,000 score. The following are considered altars: grand altar, large altar, medium altar, small altar.

Nursery 

No

None

- Returns 0 score if any of the following is true:
- The Biotech DLC is not active.

- There is at least 1 non-medical prisoner bed or at least 1 non-baby bed.

- There are less than 2 baby beds.

- Returns 100,200 score per baby bed. The following are considered baby beds: baby sleeping spot, crib.

Playroom 

No

None

- Returns 0 score if any of the following is true:
- The Biotech DLC is not active.

- There is at least 1 humanlike bed in the room.

- Returns 8 score per each one of the following: baby decoration, toy box.

Classroom 

No

None

- Returns 0 score if any of the following is true:
- The Biotech DLC is not active.

- There is at least 1 human bed in the room.

- Returns 8 score per each one of the following: blackboard, school desk.

Deathrest chamber 

Yes

Impressiveness

- Returns 100 score per deathrest casket and 50 score per deathrest accelerator , glucosoid pump , hemogen amplifier , hemopump , or psychofluid pump .

Containment cell 

None

None

- Returns 100 score per holding platform or holding spot and 50 score per bioferrite harvester , electric inhibitor , or electroharvester .

Ceremonial chamber 

None

None

- Returns 200 score per each one of the following: psychic ritual spot.

Other pieces of furniture not mentioned, such as chairs, are not considered for score calculation.

Stats[edit]

Room stats are values of a room that passively affect both thoughts about the room itself and some events and activities that take place within. These include Impressiveness, which is calculated from four composite stats: Wealth, Beauty, Space, and Cleanliness. These base stats are automatically calculated from buildings, flooring, filth, and the room's perimeter.

Room stats can be inspected with the room stats display, which can be toggled with a button in the lower right corner of the screen or a hotkey (G by default). Additional information can also be viewed by holding down the Alt key.

Room stats affect the following:

- Medical treatment quality (Cleanliness)

- Research speed (Cleanliness)

- Food poisoning chance in prepared meals (Cleanliness)

- Mood of the people using them (Impressiveness)

The following traits are affected by room stats:

- Greedy - Decrease without sufficiently Impressive bedroom.

- Jealous - Decrease if anyone has a noticeably better bedroom. [How much?]

- Ascetic - Decrease if room is too Impressive. Increase if bedroom is dull or worse.

Impressiveness[edit]

The value for Impressiveness is based on the four other room stats (Wealth, Beauty, Space, and Cleanliness).

The mood effects from the room depend on the Impressiveness level, and not on the precise value. That value is rounded down to the nearest whole number, and a label (or "level") of Impressiveness will be given to the room, according to the table below. This level is used to apply the relevant thought, positive or negative. 

The exact mood effects depend on the room role, with different rooms having different values at each level. For more information, see this section of the Thoughts page. For bedrooms, dining rooms, and rec rooms, the effects are as follows:[Verify table]

Value

Description

Mood impact

< 20

awful

−2 (bedrooms only)

>= 20 and < 30

dull

none

>= 30 and < 40

mediocre

+1 (bedrooms only)

>= 40 and < 50

decent

+2

>= 50 and < 65

slightly impressive

+3

>= 65 and < 85

somewhat impressive

+4

>= 85 and < 120

very impressive

+5

>= 120 and < 170

extremely impressive

+6

>= 170 and < 240

unbelievably impressive

+7

>= 240

wondrously impressive

+8

Guidelines[edit]

Since the impressiveness calculation (explained below) is fairly involved, it is not practical to predict impressiveness levels in an actual game. However, the following rules of thumb can be applied:

- Keep all four room stats equally in mind. There is a heavy weighting towards whichever stat is weakest, which is counted as much as all three other stats combined. For example, having a masterpiece work of art in a large room (high wealth, space and beauty) is not very effective if the floor is covered in vomit and animal filth (low cleanliness). It is quite difficult to compensate for one low stat by raising the other three.

- Making a particularly small room impressive is difficult. Room size is a limiting factor for Impressiveness. If you want to make the room "very impressive", it should have a space of at least around 25 (which still counts as "rather tight" in the game). E.g. a furnished bedroom with a 5x5 or 4×6 footprint would be fine, and a little smaller could still work, but it would be a challenge to get there with a 4x4 room. Note that any naturally "large" rooms like hallways, lobbies, recreation halls etc. will never run into this limitation at all.

- Cleanliness matters. Since the level of impressiveness is what counts, and there are sharp thresholds separating the levels, even a minute change of any of the values can have a strong effect. This is usually due to cleanliness changing (because the other factors are pretty much fixed); even a single speck of dirt on the floor can result in major mood changes. Make sure that the room is not too close to a level threshold, and keep it clean.

- Do not go overboard. There are sharply diminishing returns from increasing any room stat. Increasing any of the stats has dramatically diminishing returns with regards to impressiveness. It is not worth putting a lot of resources into any of the stats beyond a point.*

(* Not unless you care about the stat for other reasons; "room impressiveness" is not the only stat that can affect mood. Beauty, among others, has its own value.)
Formula[edit]

The actual formula for calculating impressiveness involves multiple steps, starting with the four room statistics (wealth, beauty, space and cleanliness) and resulting in a single integer value impressiveness.

The calculation is done in several steps:

- Convert each stat into natural units, so that typical in-game stats end up in a range of comparable single digit values.

- Curve values beyond (-1, 1) using a natural logarithm.

- Average the four stats into an impressiveness score, weighted towards the lowest one

- Soft-cap the result according to the space of the room.

Here is a Desmos graph with the formula implemented.

Detailed formula:

 
Base values[edit]

Firstly, all four raw stats are scaled individually by applying a factor, deriving the base contribution for each stat:

Wb = wealth ÷ 1500
Bb = beauty ÷ 3
Sb = space ÷ 125
Cb = 1 + (cleanliness ÷ 2.5)
Modified values[edit]

These base values are now modified if they lie outside the range (−1, 1), by applying the natural logarithm as follows: [Add image]

m = 1 + ln(b) (if b >= 1)
m = [1 + ln(−b)] × −1 (if b <= −1)

(This is symmetrical for positive and negative values).

Impressiveness score[edit]

These modified values are then combined to give the impressiveness score as follows.

Take a weighted sum of the average of the values and the smallest of the values:

I = (65 × (Wm + Bm + Sm + Cm) ÷ 4) + (35 × min(Wm, Bm, Sm, Cm))

This means that the smallest of the values contributes 51.25%, just over half, while the other three values each contribute 16.25%, or 48.75% combined.

As a final step we compare this impressiveness value to the spaciousness of the room:

S' = 500 × Sm
If I > S', then
 I' = 0.25 × I + 0.75 × S'
else
 I' = I (no change)

This means a room's max impressiveness is soft-capped to 500% of their space score.[Verify] However, this specific step is only relevant for very small, disproportionately luxurious rooms. Even a 60-space room (S = 0.5) will incur no penalty up to 240 impressiveness, enough to clear the highest bracket ("wondrously impressive"), and a 30-space room (S = 0.24) already reaches "extremely impressive" with no penalty.

Takeaways[edit]

It can be useful to think of impressiveness as a percentage value composed of four categories; a score of 1 in each category corresponds to 100 impressiveness, while values above 1 stop giving "fair" (ie. linear) returns. One unit of each stat is equivalent to each the following:

- Wealth of 1,500

- Beauty of 3

- Cleanliness of 0 (i.e. when using any cleanliness enhancers)

- Space of 125

Above these values, it begins to become more economical to invest attention in other stats. A "standard bedroom" of size 4×6, carpeted and containing bed, dresser, end table, lamp and plant pot will still have plenty of leeway in all categories (except cleanliness, which is at a natural 0 for a cleaned room); in this case, you will usually proceed by putting a sculpture or high quality armchair in the room, increasing beauty and wealth.

Furthermore, observe that the factors (i.e., modified values) for wealth and beauty will often be well above 1, but cleanliness and space usually lower than 1. Unless the room is "very spacious", or close to it, the decisive factor will thus be space, then cleanliness. In fact, even a well-cleaned room can never have a value over C = 1 (0 cleanliness; perfectly clean) or C = 1.215 (0.6 cleanliness; sterile), meaning rooms above ~100-120 impressiveness will always be bottlenecked by their cleanliness score. This makes "very impressive" (85-120 impressiveness) a natural set point for many rooms. 

Example[edit]

Start with a room with a wealth of 3000, space of 25, cleanliness of 0, beauty of 3.

Wb = 3000 ÷ 1500 = 2, but this is curved to 1 + ln(2) = 1.69
Bb = 3 ÷ 3 = 1
Sb = 25 ÷ 125 = 0.2
Cb = 1 + (0 ÷ 2.5) = 1
This makes the average score (1.69 + 1 + 0.2 + 1) ÷ 4) = 0.97 and the lowest score 0.2 (space).

From the above numbers, we can calculate the base Impressiveness

I = (65 × 0.97) + (35 × 0.2)
I = 63 + 7
I = 70 (70.21 unrounded)
Now, I < 500 × Sm (70 < 100), so there is no space penalty. Therefore, the reported Impressiveness of the room is 70 or "somewhat impressive"

If we were to increase the wealth of the above room by 6000 (4 units), our Wm would become 6 -> 1 + ln(6) = 2.79 (+1.1 increase). Wealth wasn't the lowest stat, so this would only improve impressiveness by 1.1*16.25% = 17.9%, resulting in a score of 88 or "very impressive"

If we were to increase the original room's space by 10 units instead, Sm becomes 0.28 (0.08 increase). Increasing the bottleneck stat results in a change of 0.08*51.25% = 4.1%, or 74 total impressiveness or "somewhat impressive"

 

Wealth[edit]

This is the sum of the Market Value of all buildings/furniture/floors(not under doors) in the room and all walls and doors surrounding the room.

Walls, doors, columns and animal flaps in the outer corner count as well. The value of power conduits in walls is also included, however, for some reason building or deconstructing a conduit doesn't immediately update room wealth. Only if wealth is recalculated for some other reason, is the value of the conduits included. The same is true when building a column in the outer corner of the wall.

Value

Description

< 500

impoverished

>= 500 and < 700

somewhat poor

>= 700 and < 2000

mediocre

>= 2000 and < 4000

somewhat rich

>= 4000 and < 10000

rich

>= 10000 and < 40000

luxurious

>= 40000 and < 100000

very luxurious

>= 100000 and < 1000000

extremely luxurious

>= 1000000

unbelievably luxurious

Beauty[edit]

This is the average environmental beauty of the room including its walls and doors with a penalty for small rooms. Walls, doors and columns in the outer corner count as well. Building or deconstructing a column in the outer corner doesn't trigger a recalculation however. Floor tiles underneath walls and doors have no influence. 

Room beauty is calculated as:

TotalBeauty = sum(beauty for each internal cell) + sum(beauty for each adjacent cell)
WeightedSize = size if (size > 40) else (20 + size / 2)
RoomBeauty = TotalBeauty / WeightedSize
This means that all rooms with less than 40 internal space will have their beauty penalised.

Value

Description

< -3.5

hideous

>= -3.5 and < 0

ugly

>= 0 and < 2.4

neutral

>= 2.4 and < 5

pretty

>= 5 and < 15

beautiful

>= 15 and < 50

very beautiful

>= 50 and < 100

extremely beautiful

>= 100

unbelievably beautiful

Space[edit]

Indicates how much free space is available in the room. A room's Space score is 1.4 times the number of tiles in the room. Objects that prevent a pawn from standing in a space will decrease the available space in the room by 0.9 per tile the object covers. Thus, an occupied tile contributes a total of 0.5 to space. Objects that reduce space include beds, tables, workbenches, lamps, and heaters. Stools and chairs do not reduce space.

Value

Description

typical size*

< 12.5

cramped

3x4 or smaller*

>= 12.5 and < 29

rather tight

3x6, 4x5*

>= 29 and < 55

average-sized

4x7, 5x6*

>= 55 and < 70

somewhat spacious

>= 70 and < 130

quite spacious

>= 130 and < 349.5

very spacious

>= 349.5

extremely spacious

(* These are "safe" approximations; as described, the items placed in the room can greatly reduce the effective size. For example, an empty 5x5 room has space (25 x 1.4 =) 35, easily "average" - when empty. However, placing just one bed (2 tiles), one table (2 tiles), a light, a heater, a plant pot and one artwork (1 tile each, a chair is "free") in that room reduces the effective space by -7.2 (= 8 tiles x .9), and the effective space is now 27.8, "rather tight".)
(* Due to floating point inaccuracies, sometimes a room that is right on a threshold may randomly count for one category or the other. For example, a room with 5 standable tiles and 11 walkable but non-standable tiles should come out to exactly 12.5 score, but may result in either "cramped" or "rather tight". It's safest to not rely on exact values.)
Note, that space of the room affects only its impressiveness. Careful to not confuse with Pawn's space need.

Cleanliness[edit]

This section is about the cleanliness of rooms. For the cleanliness stat of individual objects, see Cleanliness (Stat).

A rooms cleanliness affects surgery success chance, research speed, the chance that cooked meals will cause food poisoning, and gene Assembly Speed Factor. A room's cleanliness is the average cleanliness score of all tiles in the room. It is determined by the type of flooring, the presence of any filth, and the cleanliness value of some furniture such as the butcher table and the stonecutter's table. Note that the type of floor under a door doesn't count for cleanliness, but filth under a door does count.

Room Cleanliness

Description

< -1.1

very dirty

>= -1.1 and < -0.4

dirty

>= -0.4 and < -0.05

slightly dirty

>= -0.05 and < 0.4

clean

>= 0.4

sterile

Surface

Cleanliness
Value

Void metal 
1

Sterile tile floor
0.6

Steel, Silver or Gold floor
0.2

Bioferrite plate
0.2

all other constructed flooring; Bridges
0

Natural stone (rough or smoothed)
0

Straw matting
-0.1

all other natural surfaces (soil, gravel, etc.)
-1

Marsh, Marshy soil, Mud, Broken asphalt
-2

Chunks
-2

Flesh
-3

Dirt, rubble, all other filth
-5

Blood
-10

Insect blood, vomit, fuel puddle
-15

Corpsebile
-20

Using "Toggle the beauty display" can help locate filth in a given room, which typically stands out due to its negative beauty.

Map regions[edit]

Upon map generation, the map is divided into chunks of 12x12 squares called map regions. Each region requires a contiguous area and will be subdivided otherwise. Under no circumstance will a region extend beyond the initial 12x12 grid. Impassable buildings (both natural and artificial) are not considered as part of any map region for this purpose and will subdivide existing map regions accordingly. Regions will fuse when possible. Map regions are used for several calculations and can be seen in game via the debug option "Draw Regions".

Some additional notes:

 
- Impassable buildings are never part of any map region.
- Impassable non-walls (ex: Ship engine) may create a "red" temporal map region on construction that will be removed once anything else is build/destroyed.

- Impassable terrain creates map regions confined to its extension.
- These regions don't interact with the regular ones, but otherwise follow the stated rules.

- Passable buildings, such as fences and barricades, create map regions along their extension.
- These "fence" regions won't interact with other kinds, but otherwise follow the stated rules.

- Doors have unique behavior
- Single tile doors create a 3 tile map region centered on the doors' tile, following the door's orientation, that overlaps with other map regions.
- Impassable objects will delete the overlapping section, no interaction otherwise.

- Double tile doors create 2 map regions, 1 for each of its tiles.

- The map regions created by doors don't interact with any other, not even each other.

- The grid defining regions is drawn from the bottom-left of the map row by row.

 

Version history[edit]

- 0.12.906 - Added.

- 1.1 - Added room stats gizmo, which displays the stats of the room containing a selected building, at a glance.

- Royalty DLC release - Throne room role added.

- Ideology DLC release - Temple room role added.

- 1.3.3072 - Fix: Checking all beds instead of just humanlike ones for room owner.

- 1.4.3523 - Added the storeroom role for rooms with lots of shelves.

- Biotech DLC release - Nursery, playroom, classroom, and deathrest chamber roles added.

- Anomaly DLC release - Containment cell and ceremonial chamber roles added.

- 1.6.4518 - Some production buildings now have a work speed penalty if they are not in the correct room.

Notes[edit]

- ↑ 1.00 1.01 1.02 1.03 1.04 1.05 1.06 1.07 1.08 1.09 1.10 1.11 1.12 1.13 1.14 1.15 1.16 1.17 1.18 1.19 Work speed penalty of 80% if not placed in the room with the correct role.

- ↑ 2.0 2.1 2.2 2.3 This role will have its owners' name added to its name.

- ↑ A pawn's love cluster is all the other pawns that can be linked to the pawn through a chain of romantic relationships.

- ↑ This role changes to the ideoligion's set temple name.

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Rooms&oldid=184121#Roles"

 Categories: - Stubs
- Game mechanics

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

 
 

 

 
 - This page was last edited on 25 September 2026, at 23:05.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -