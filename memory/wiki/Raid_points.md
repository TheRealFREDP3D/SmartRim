Raid points - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Raid points

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 See also: Raids

Contents

- 1 Summary

- 2 Viewing raid points

- 3 Wealth points

- 4 Pawn points

- 5 Difficulty

- 6 Starting factor

- 7 Adaption factor

- 8 Other factors

- 9 Wealth independent mode

- 10 Version history

Raid Points are a mechanic used to determine the size of raids, other major threats, quests, and certain other events.

Summary[edit]

Raid Points are spent by the storyteller to purchase raiders. Each raider has a "cost", or Combat Power, associated with them. Every 1 raid point roughly equates to 1 combat power. For example, if the storyteller has 180 raid points, then it can potentially send out 3 "Warrior" raiders worth 60 combat power each. The combat power of each enemy type can be seen in tables on the Raider page. Raid points are also used to calculate the extra loot carried by raiders. For an explanation of that system, see Raider loot.

The minimum Raid Points value is 35. The maximum is 10,000. The size of 10,000 Raid Point raids is approximately 250 Tribals, 100 Pirates, 66 Scythers, or 25 Centipedes. Quests and the storyteller Randy Random multiply raid size after the point cap is applied; both can allow raids to be larger in size.

Raid Points = (Wealth Points + Pawn Points) * (Difficulty) * (Starting Factor) * (Adaption Factor)

Raid Points are calculated using a formula based on your colony's wealth, colonist count and combat animals, threat scale, starting factor, and adaption factor. While simple at first glance, each variable, in turn, has its own process of calculation which significantly complicates the outcome. Despite this complexity, the two most significant player-controlled factors can be identified as total colony wealth and total colonist count. This is the motivation behind wealth management strategies.

Each map and caravan is calculated mostly independently. Once a caravan leaves the map tile those colonists and items no longer count towards the Raid Points of the map tile. Separate colonies have separate and independently calculated Raid Point totals. The "Adaption Factor" is an exception and is shared across multiple settlements.

Viewing raid points[edit]

Players on PC version of the game can view their raid points by turning on Development mode. Hit the 4th button, "Open the View Settings", and check "Write Storyteller". Then, back on the game screen, hit the Magnifying Glass button. "Base Points" is the Raid Point total. 

Wealth points[edit]

A player can view their Wealth by hitting the History menu and going to the Statistics tab. The game considers "Colony Wealth (buildings)" at only 50% for the purpose of calculating Raid Points. Instead of using "Colony Wealth (this map)", the game uses "Storyteller Wealth". Note that pawns count for their wealth values in addition to their pawn points. Temporary colonists from quests count towards neither.

"Storyteller Wealth" = (Colony Wealth Items + Colony Wealth Creatures + (Colony Wealth Buildings * 0.5))

"Storyteller Wealth" is linearly interpolated on a graph to create "Wealth Points". 

Graph
Points
Storyteller Wealth

 

0
0

0
14,000

2,400
400,000

3,600
700,000

4,200
1,000,000

At 14,000 "Storyteller Wealth" and below, there are "0 Wealth Points". At 400,000 "Storyteller Wealth" there are "2,400 Wealth Points". Between 14k and 400k wealth, every $1 of storyteller wealth increases "Wealth Points" by (2,400 - 0) / (400,000 - 14,000) points. 

At the 14k to 400k threshold, 1 raid point would be worth ~ 160.83 storyteller wealth from wealth points. Wealth also has an impact on pawn points; see below for details.

At 1 million "Storyteller Wealth", and all values over 1 million, there are 4,200 Raid Points. Further wealth has no effect on Raid Points.

Pawn points[edit]

"Pawn Points" is a points total given based on your Colonist count, Slaves, Children, Trainable Animals, and player controlled Mechs. Rimworld's code labels these creatures as "pawns." "Pawn Points" is an addition to any "Wealth Points" given by the pawn's Market Value.

Only living, free, pawns of the player's faction on the map tile count. Prisoners, even those from the player faction that can be released back into the colony at anytime, do not count for Pawn Points. Temporary colonists, called "Quest Lodgers", from other factions also do not count. 

Human pawn points are determined using the following chart. The result may be modified based on a few additional factors.

Graph
Points
Storyteller Wealth

- 

15
0

15
10,000

140
400,000

200
1,000,000

From 0 to 10,000 "Storyteller Wealth", each full colonist counts for 15 pawn points. At 400,000 "Storyteller Wealth", each colonist counts for 140 points. Between 10k to 400k Storyteller Wealth, each colonist gives 15 + [ (140 - 15) * (wealth - 10,000) / (400,000 - 10,000) ] points. This can be simplified into 15 + (wealth - 10,000) / (3,120) points per colonist.

Between 10k to 400k Storyteller Wealth, every $1 of wealth gives 1 / 3,120 pawn points per effective colonist. So at the 10k to 400k threshold, 1 pawn point is worth 3,120 / (effective colonist count) storyteller wealth. 

Assuming the same 10k to 400k wealth threshold:

- At 10 healthy colonists, 3,120 storyteller wealth would give 10 raid points through pawn points.

- At 10 healthy colonists, 1 pawn point would be worth 312 storyteller wealth.

- Going from 10 to 11 colonists would add 15 + (wealth - 10,000) / 3,120 raid points.

Remember that storyteller wealth also increases wealth points. 

Certain factors can modify the effective colonist count. See below for details.

Modifiers:

- Slaves have a 75% multiplier to pawn points.

- Pawns in cryptosleep have a 30% multiplier.

- Babies have a 0% modifier and thus add no pawn points.

- Children have a multiplier based on age. The multiplier rises linearly from 0% at age 3 to 50% at age 13. Then, from 50% at 13 it rises linearly until 100% at age 18.

- Health: The Pawn Point value of all applicable pawns, including animals and mechs, is scaled based on their Health Bar. The most prominent visualization of the Health Bar is found when selecting a pawn and looking below their name in the bottom left information card. When at full health, the bar will display "Healthy" and be fully colored. While at full health bar, Pawns contribute 100% of their Pawn Points. Dead pawns do not count for pawn points, even when unburied and still showing in the colonist bar.

When below full health, Pawns have reduced Pawn Points. The shading of the displayed Health Bar will be changed. The Health Bar is only changed due to temporary wounds. For example, a colonist with a damaged and bruised leg will displayed a reduced Health bar and thus have reduced Pawn Points. A colonist with a missing leg and no other injuries is considered at "Full Health" and contributes full Pawn Points.
The exact calculation of Pawn Points based on the Health Bar is not fully known. The applicable code with num3 being the variable for "Pawn Points": num3 = Mathf.Lerp(num3, num3 * pawn.health.summaryHealth.SummaryHealthPercent, 0.65f);

The following factors add to pawn points, but are separate to colonist count.

Animals:

- Tamed animals that can learn "Attack" count for 8% of their Combat Power; this value is not scaled by Storyteller Wealth. Attack doesn't have to be trained, only possible to be trained. "Combat Power" is not affected by the age of the animal: baby animals that can attack count as adults for "Pawn Points". Downed animals do not count.

Player-controlled Mechs and Entities:

- Friendly mechanoids and entities count for 20% to 40% of their Combat Power; this value is scaled by Storyteller Wealth. Dormant mechs count. Recharging mechs count. Downed, dead or destroyed mechs and entities do not count.

Graph
Points
Storyteller Wealth

- 

20%
0

20%
10,000

30%
400,000

40%
1,000,000

Labor mechanoids other than the tunneler have a combat power of 10. The other mech values can be seen here. The only entity capable of being friendly is the ghoul, which has 90 combat power.

Difficulty[edit]

See also: AI Storytellers

Difficulty is solely the "Threat Scale" number. Threat Scale is determined by the Storyteller settings. The Threat Scales for the pre-set difficulties are listed below, however choosing "Custom" difficulty allows Threat Scale to range from 0% to 500%.

Difficulty
Threat Scale

Peaceful
0.10

Community builder
0.30

Adventure story
0.60

Strive to survive
1.00

Blood and dust
1.55

Losing is fun
2.20

Starting factor[edit]

The "Starting Factor" factor means that the start of the game is made easier. After 40 days, there is essentially no "Days Passed" factor because the factor is 1. 

The "Days Passed" factor is a defined chart.

Days Passed
Starting Factor

10
0.7

40
1

At 10 Days, and earlier, the factor is 0.7. At 40 Days, and all dates after, the factor is 1.

Adaption factor[edit]

Roughly, the Adaption Factor means Rimworld tries to make the game harder if it thinks the player is doing well, and easier if it thinks the player is doing poorly. Time passed since the deaths of colonists, and time passed since the downing of colonists are the major aspects that Adaption Factor considers. 

Slaves and quest lodgers are considered colonists for the purposes of the Adaption Factor. Player-controlled mechs do not count for the Adaption Factor. Children that can walk do fully count towards the Adaption factor. It does not matter how a pawn is downed / killed, so violently killing your own colonists will impact adaptation (as opposed to executing or banishing them).

Think of the "Adaption Factor" like the classic workplace sign that says "Days Since Last Injury: 10". The differences from this analogy to the "Adaption Factor" is that the "Adaption Factor" does not reset entirely on injuries. Instead, a number of days are subtracted from the total and how many days are subtracted gets quite complicated. In Rimworld, in this analogy, the sign can read "Days Since Last Injury: Negative 30". Also, the "Days Since Last Injury" don't necessarily go up 1 per day in Rimworld.

The "Adaption Impact" in the custom Storyteller Settings adjusts how much the game considers the "Adaption Factor". If "Adaption Impact" is set to 0% the "Adaption Factor" is effectively turned off. The Adaption Factor has a maximum range of 0.4 to 1.47. By default "Losing is Fun" has "Adaption Impact" set to 40%. At "40% Adaption Impact" has an effective minimum and maximum range of the Adaption Factor is 0.75 to 1.19.

The "Adaption Growth Rate" in the custom difficulty options controls how fast the "Adaption Factor" grows over time. On "Losing is Fun", the "Adaption Growth Rate" is set to the maximum speed. 

The "Adaption Factor" starts at 0.8. The "AdaptDays" starts at 0. There is a grace period of 30 days before the "AdaptDays" can go above 0. Every 12 hours (or 30,000 game ticks), the game checks how many "AdaptDays" to add. The game takes the current "AdaptDays" and looks at the following chart. Each value shown is halved. The halving occurs because the check is done every 12 hours, which means it happens twice a day. 

Graph
Current AdaptDays
AdaptDays Added

- 

-30
3

-0.01
3

0
1

59.99
1

60
0.5

119.99
0.5

120
0.25

When a colonist dies an amount of "AdaptDays" are removed based on your population. Here's the Chart:

Population
AdaptDays Removed

0
30

11
30

20
20

When a colonist is downed a different amount of "AdaptDays" are removed based on your population. Here's that chart:

Population
AdaptDays Removed

1
8

2
6

3
6

11
5

20
3.5

"Adapt Days" have a minimum value of -60 and a maximum value of 100. "AdaptDays" are taken to a chart to determine "Adaption Factor". Here's that chart:

Current AdaptDays
Adaption Factor

-30
0.4

0
0.8

30
1

60
1.2

120
1.6

180
2

The chart goes beyond the maximum potential "AdaptDays" value. Even though the chart goes up to 180 "AdaptDays" and 2.0 "Adaption Factor", "Adaption Factor" cannot reach that point. At the maximum value of 100 "AdaptDays", the "Adaption Factor" is 1.47.

The "Adaption Factor" is shared across multiple map tiles.

Other factors[edit]

Firstly, the raid point cap of 10,000 is applied. The following factors are applied after the cap:

- Storytellers may have a "randomPointsFactorRange" to modify raid size. Randy Random will randomly increase or decrease the raid point value by 50% to 150% for each event. Cassandra Classic and Phoebe Chillax will not do any further modification.

- Major threats caused by a non-endgame quest are multiplied by the number of stars of the quest (1 star = 1x raid points, 2 stars = 2x raid points, 3 stars = 3x raid points). A quest's raid points is further modified by a 70% to 130% multiplier. Quests do not use Randy Random's randomPointsFactorRange.

- The type of major threat can modify raid size. Sappers and center drop pod raids will be smaller than expected.

- Raids caused by the ship reactor's activation or the Royal Ascent quest will always have a minimum of 500 raid points, regardless of threat scale (or any other factor to raid points).

Wealth independent mode[edit]

"Wealth Independent" mode is another option in the "custom" section of the "Storyteller Settings". Rather than tracking "StorytellerWealth", an amount of wealth is assigned based on time passed on that specific map tile:

Days Passed
StorytellerWealth

0
10,000

180
180,000

720
1,000,000

1,800
2,500,000

This chart is for the default choice of "Years until Max Threat: 12". Changing the "Years Until Maximum Threat" slider sets the year that the 1,000,000 wealth value will be assigned. For example, if 1 Year is chosen, then on day 60 (end of year 1), 1 Million Wealth will be assigned. If the year 20 is chosen, on day 1,200 (end of year 20), 1 million wealth will be assigned.

All other factors, such as pawn count and adaptation, are applied as normal.

The Wealth Independent Mode timer is exclusive to each map tile. Each map tile starts the timer at 0. Changing map tiles will reset the Wealth Independent mode timer.

Version history[edit]

- 1.2.2719 - Storyteller now ignores Hit Points of buildings for purposes of wealth calculation.

- 1.3.3287 - Added a 0.75x factor to pawn points for colony slaves when calculating threat point (wealth points was already adjusted for slaves). This means having slaves won't attract larger threats as much as colonists.

- 1.4.3555 - Friendly mechanoids now count towards pawn points, in addition to wealth points. Slightly reduce the impact that player mechanoids have on raid points.

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Raid_points&oldid=182207"

 Category: - Game mechanics

Hidden categories: - Articles verified for 1.3.3101
- Pages with graphs

 

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

 
 

 

 
 - This page was last edited on 19 July 2026, at 00:17.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -