# Raid points

From RimWorld Wiki

Jump to navigation Jump to search

See also: [Raids](/wiki/Raids "Raids")

## Contents

  * 1 Summary
  * 2 Viewing raid points
  * 3 Wealth points
  * 4 Pawn points
  * 5 Difficulty
  * 6 Starting factor
  * 7 Adaption factor
  * 8 Other factors
  * 9 Wealth independent mode
  * 10 Version history



**Raid Points** are a mechanic used to determine the size of [raids](/wiki/Raids "Raids"), other [major threats](/wiki/Major_threat "Major threat"), [quests](/wiki/Quest "Quest"), and certain other events. 

## Summary[[edit](/index.php?title=Raid_points&action=edit&section=1 "Edit section: Summary")]

Raid Points are spent by the [storyteller](/wiki/Storyteller "Storyteller") to purchase raiders. Each raider has a "cost", or Combat Power, associated with them. Every 1 raid point roughly equates to 1 combat power. For example, if the storyteller has 180 raid points, then it can potentially send out 3 "Warrior" raiders worth 60 combat power each. The combat power of each enemy type can be seen in tables on the [Raider](/wiki/Raider "Raider") page. Raid points are also used to calculate the extra loot carried by raiders. For an explanation of that system, see [Raider loot](/wiki/Raider#Loot "Raider"). 

The minimum Raid Points value is 35. The maximum is 10,000. The size of 10,000 Raid Point raids is approximately 250 [Tribals](/wiki/Tribes#Pawns "Tribes"), 100 [Pirates](/wiki/Pirates#Pawns "Pirates"), 66 [Scythers](/wiki/Scyther "Scyther"), or 25 [Centipedes](/wiki/Centipede "Centipede"). [Quests](/wiki/Quest "Quest") and the storyteller [Randy Random](/wiki/Randy_Random "Randy Random") multiply raid size after the point cap is applied; both can allow raids to be larger in size. 

Raid Points = (Wealth Points \+ Pawn Points) * (Difficulty) * (Starting Factor) * (Adaption Factor)   
---  
  
Raid Points are calculated using a formula based on your colony's wealth, colonist count and combat animals, threat scale, starting factor, and adaption factor. While simple at first glance, each variable, in turn, has its own process of calculation which significantly complicates the outcome. Despite this complexity, the two most significant player-controlled factors can be identified as total colony wealth and total colonist count. This is the motivation behind [wealth management](/wiki/Wealth_management "Wealth management") strategies. 

Each map and [caravan](/wiki/Caravan "Caravan") is calculated mostly independently. Once a caravan leaves the map tile those colonists and items no longer count towards the Raid Points of the map tile. Separate colonies have separate and independently calculated Raid Point totals. The "Adaption Factor" is an exception and is shared across multiple settlements. 

## Viewing raid points[[edit](/index.php?title=Raid_points&action=edit&section=2 "Edit section: Viewing raid points")]

Players on PC version of the game can view their raid points by turning on [Development mode](/wiki/Development_mode "Development mode"). Hit the 4th button, "Open the View Settings", and check "Write Storyteller". Then, back on the game screen, hit the Magnifying Glass button. "Base Points" is the Raid Point total. 

[![Raid base points.png](/images/thumb/3/3c/Raid_base_points.png/300px-Raid_base_points.png)](/wiki/File:Raid_base_points.png)

## Wealth points[[edit](/index.php?title=Raid_points&action=edit&section=3 "Edit section: Wealth points")]

A player can view their Wealth by hitting the [History](/wiki/History "History") menu and going to the [Statistics](/wiki/History#Statistics "History") tab. The game considers "Colony Wealth (buildings)" at only 50% for the purpose of calculating Raid Points. Instead of using "Colony Wealth (this map)", the game uses "Storyteller Wealth". Note that pawns count for their wealth values in addition to their pawn points. Temporary colonists from [quests](/wiki/Quest "Quest") count towards neither. 

"Storyteller Wealth" = (Colony Wealth Items + Colony Wealth Creatures + (Colony Wealth Buildings * 0.5))   
---  
  
"Storyteller Wealth" is linearly interpolated on a graph to create "Wealth Points". 

Graph | Points | Storyteller Wealth   
---|---|---  
| 0 | 0   
0 | 14,000   
2,400 | 400,000   
3,600 | 700,000   
4,200 | 1,000,000   
  
At 14,000 "Storyteller Wealth" and below, there are "0 Wealth Points". At 400,000 "Storyteller Wealth" there are "2,400 Wealth Points". Between 14k and 400k wealth, every $1 of storyteller wealth increases "Wealth Points" by `(2,400 - 0) / (400,000 - 14,000)` points. 

At the 14k to 400k threshold, 1 raid point would be worth ~ 160.83 storyteller wealth from wealth points. Wealth also has an impact on pawn points; see below for details. 

At 1 million "Storyteller Wealth", and all values over 1 million, there are 4,200 Raid Points. Further wealth has no effect on Raid Points. 

## Pawn points[[edit](/index.php?title=Raid_points&action=edit&section=4 "Edit section: Pawn points")]

"Pawn Points" is a points total given based on your Colonist count, Slaves, Children, Trainable [Animals](/wiki/Animals "Animals"), and player controlled Mechs. Rimworld's code labels these creatures as "pawns." "Pawn Points" is an addition to any "Wealth Points" given by the [pawn's Market Value](/wiki/Market_Value#Pawn_value "Market Value"). 

Only living, free, pawns of the player's faction on the map tile count. [Prisoners](/wiki/Prisoner "Prisoner"), even those from the player faction that can be released back into the colony at anytime, do not count for Pawn Points. Temporary colonists, called "Quest Lodgers", from other factions also do not count. 

Human pawn points are determined using the following chart. The result may be modified based on a few additional factors. 

Graph | Points | Storyteller Wealth   
---|---|---  
| 15 | 0   
15 | 10,000   
140 | 400,000   
200 | 1,000,000   
  
From 0 to 10,000 "Storyteller Wealth", each full colonist counts for 15 pawn points. At 400,000 "Storyteller Wealth", each colonist counts for 140 points. Between 10k to 400k Storyteller Wealth, each colonist gives `15 + [ (140 - 15) * (wealth - 10,000) / (400,000 - 10,000) ]` points. This can be simplified into `15 + (wealth - 10,000) / (3,120)` points per colonist. 

Between 10k to 400k Storyteller Wealth, every $1 of wealth gives `1 / 3,120` pawn points _per effective colonist_. So at the 10k to 400k threshold, 1 pawn point is worth `3,120 / (effective colonist count)` storyteller wealth. 

Assuming the same 10k to 400k wealth threshold: 

  * At 10 healthy colonists, 3,120 storyteller wealth would give 10 raid points through pawn points.
  * At 10 healthy colonists, 1 pawn point would be worth 312 storyteller wealth.
  * Going from 10 to 11 colonists would add `15 + (wealth - 10,000) / 3,120` raid points.



Remember that storyteller wealth also increases wealth points. 

Certain factors can modify the effective colonist count. See below for details. 

**Modifiers:**

  * [Slaves](/wiki/Slaves "Slaves")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") have a 75% multiplier to pawn points.
  * Pawns in [cryptosleep](/wiki/Cryptosleep_casket "Cryptosleep casket") have a 30% multiplier.
  * [Babies](/wiki/Babies "Babies")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") have a 0% modifier and thus add no pawn points.
  * [Children](/wiki/Children "Children")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") have a multiplier based on age. The multiplier rises linearly from 0% at age 3 to 50% at age 13. Then, from 50% at 13 it rises linearly until 100% at age 18.
  * Health: The Pawn Point value of all applicable pawns, including animals and mechs, is scaled based on their Health Bar. The most prominent visualization of the Health Bar is found when selecting a pawn and looking below their name in the bottom left information card. When at full health, the bar will display "Healthy" and be fully colored. While at full health bar, Pawns contribute 100% of their Pawn Points. Dead pawns do not count for pawn points, even when unburied and still showing in the colonist bar.



    When below full health, Pawns have reduced Pawn Points. The shading of the displayed Health Bar will be changed. The Health Bar is only changed due to temporary wounds. For example, a colonist with a damaged and bruised leg will displayed a reduced Health bar and thus have reduced Pawn Points. A colonist with a missing leg and no other injuries is considered at "Full Health" and contributes full Pawn Points.

    The exact calculation of Pawn Points based on the Health Bar is not fully known. The applicable code with num3 being the variable for "Pawn Points": num3 = Mathf.Lerp(num3, num3 * pawn.health.summaryHealth.SummaryHealthPercent, 0.65f);

* * *

The following factors add to pawn points, but are separate to colonist count. 

**Animals:**

  * Tamed animals that can learn "Attack" count for 8% of their Combat Power; this value is not scaled by Storyteller Wealth. Attack doesn't have to be trained, only possible to be trained. "Combat Power" is not affected by the age of the animal: baby animals that can attack count as adults for "Pawn Points". Downed animals do not count.



**Player-controlled Mechs and Entities:**

  * [Friendly mechanoids](/wiki/Friendly_mechanoids "Friendly mechanoids")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") and [entities](/wiki/Entities "Entities")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") count for 20% to 40% of their Combat Power; this value is scaled by Storyteller Wealth. Dormant mechs count. Recharging mechs count. Downed, dead or destroyed mechs and entities do not count.

Graph | Points | Storyteller Wealth   
---|---|---  
| 20% | 0   
20% | 10,000   
30% | 400,000   
40% | 1,000,000   
  
Labor mechanoids other than the [tunneler](/wiki/Tunneler "Tunneler") have a combat power of 10. The other mech values can be seen [here](/wiki/Mechanoid_hive#Pawns "Mechanoid hive"). The only entity capable of being friendly is the [ghoul](/wiki/Ghoul "Ghoul"), which has 90 combat power. 

## Difficulty[[edit](/index.php?title=Raid_points&action=edit&section=5 "Edit section: Difficulty")]

See also: [AI Storytellers](/wiki/AI_Storytellers "AI Storytellers")

Difficulty is solely the "Threat Scale" number. Threat Scale is determined by the Storyteller settings. The Threat Scales for the pre-set difficulties are listed below, however choosing "Custom" difficulty allows Threat Scale to range from 0% to 500%. 

Difficulty | Threat Scale   
---|---  
Peaceful | 0.10   
Community builder | 0.30   
Adventure story | 0.60   
Strive to survive | 1.00   
Blood and dust | 1.55   
Losing is fun | 2.20   
  
## Starting factor[[edit](/index.php?title=Raid_points&action=edit&section=6 "Edit section: Starting factor")]

The "Starting Factor" factor means that the start of the game is made easier. After 40 days, there is essentially no "Days Passed" factor because the factor is 1. 

The "Days Passed" factor is a defined chart. 

Days Passed | Starting Factor   
---|---  
10 | 0.7   
40 | 1   
  
At 10 Days, and earlier, the factor is 0.7. At 40 Days, and all dates after, the factor is 1. 

## Adaption factor[[edit](/index.php?title=Raid_points&action=edit&section=7 "Edit section: Adaption factor")]

Roughly, the Adaption Factor means Rimworld tries to make the game harder if it thinks the player is doing well, and easier if it thinks the player is doing poorly. Time passed since the deaths of colonists, and time passed since the downing of colonists are the major aspects that Adaption Factor considers. 

Slaves and quest lodgers are considered colonists for the purposes of the Adaption Factor. [Player-controlled mechs](/wiki/Friendly_mechanoids "Friendly mechanoids") do not count for the Adaption Factor. [Children](/wiki/Children "Children") that can walk do fully count towards the Adaption factor. It does not matter how a pawn is downed / killed, so violently killing your own colonists will impact adaptation (as opposed to executing or banishing them). 

Think of the "Adaption Factor" like the classic workplace sign that says "Days Since Last Injury: 10". The differences from this analogy to the "Adaption Factor" is that the "Adaption Factor" does not reset entirely on injuries. Instead, a number of days are subtracted from the total and how many days are subtracted gets quite complicated. In Rimworld, in this analogy, the sign can read "Days Since Last Injury: Negative 30". Also, the "Days Since Last Injury" don't necessarily go up 1 per day in Rimworld. 

The "Adaption Impact" in the custom Storyteller Settings adjusts how much the game considers the "Adaption Factor". If "Adaption Impact" is set to 0% the "Adaption Factor" is effectively turned off. The Adaption Factor has a maximum range of 0.4 to 1.47. By default "Losing is Fun" has "Adaption Impact" set to 40%. At "40% Adaption Impact" has an effective minimum and maximum range of the Adaption Factor is 0.75 to 1.19. 

The "Adaption Growth Rate" in the custom difficulty options controls how fast the "Adaption Factor" grows over time. On "Losing is Fun", the "Adaption Growth Rate" is set to the maximum speed. 

The "Adaption Factor" starts at 0.8. The "AdaptDays" starts at 0. There is a grace period of 30 days before the "AdaptDays" can go above 0. Every 12 hours (or 30,000 game ticks), the game checks how many "AdaptDays" to add. The game takes the current "AdaptDays" and looks at the following chart. Each value shown is halved. The halving occurs because the check is done every 12 hours, which means it happens twice a day. 

Graph | Current AdaptDays | AdaptDays Added   
---|---|---  
| -30 | 3   
-0.01 | 3   
0 | 1   
59.99 | 1   
60 | 0.5   
119.99 | 0.5   
120 | 0.25   
  
When a colonist dies an amount of "AdaptDays" are removed based on your population. Here's the Chart: 

Population | AdaptDays Removed   
---|---  
0 | 30   
11 | 30   
20 | 20   
  
When a colonist is downed a different amount of "AdaptDays" are removed based on your population. Here's that chart: 

Population | AdaptDays Removed   
---|---  
1 | 8   
2 | 6   
3 | 6   
11 | 5   
20 | 3.5   
  
"Adapt Days" have a minimum value of -60 and a maximum value of 100. "AdaptDays" are taken to a chart to determine "Adaption Factor". Here's that chart: 

Current AdaptDays | Adaption Factor   
---|---  
-30 | 0.4   
0 | 0.8   
30 | 1   
60 | 1.2   
120 | 1.6   
180 | 2   
  
The chart goes beyond the maximum potential "AdaptDays" value. Even though the chart goes up to 180 "AdaptDays" and 2.0 "Adaption Factor", "Adaption Factor" cannot reach that point. At the maximum value of 100 "AdaptDays", the "Adaption Factor" is 1.47. 

The "Adaption Factor" is shared across multiple map tiles. 

## Other factors[[edit](/index.php?title=Raid_points&action=edit&section=8 "Edit section: Other factors")]

Firstly, the raid point cap of 10,000 is applied. The following factors are applied after the cap: 

  * Storytellers may have a "randomPointsFactorRange" to modify raid size. [Randy Random](/wiki/Randy_Random "Randy Random") will randomly increase or decrease the raid point value by 50% to 150% for each event. [Cassandra Classic](/wiki/Cassandra_Classic "Cassandra Classic") and [Phoebe Chillax](/wiki/Phoebe_Chillax "Phoebe Chillax") will not do any further modification.


  * Major threats caused by a non-endgame [quest](/wiki/Quest "Quest") are multiplied by the number of stars of the quest (1 star = 1x raid points, 2 stars = 2x raid points, 3 stars = 3x raid points). A quest's raid points is further modified by a 70% to 130% multiplier. Quests do not use Randy Random's randomPointsFactorRange.


  * The type of major threat can modify raid size. [Sappers](/wiki/Sapper "Sapper") and center [drop pod](/wiki/Drop_pod "Drop pod") raids will be smaller than expected.


  * Raids caused by the [ship reactor](/wiki/Ship_reactor "Ship reactor")'s activation or the [Royal Ascent](/wiki/Royal_Ascent "Royal Ascent") quest will always have a minimum of 500 raid points, regardless of threat scale (or any other factor to raid points).



## Wealth independent mode[[edit](/index.php?title=Raid_points&action=edit&section=9 "Edit section: Wealth independent mode")]

"Wealth Independent" mode is another option in the "custom" section of the "Storyteller Settings". Rather than tracking "StorytellerWealth", an amount of wealth is assigned based on time passed on that specific map tile: 

Days Passed | StorytellerWealth   
---|---  
0 | 10,000   
180 | 180,000   
720 | 1,000,000   
1,800 | 2,500,000   
  
This chart is for the default choice of "Years until Max Threat: 12". Changing the "Years Until Maximum Threat" slider sets the year that the 1,000,000 wealth value will be assigned. For example, if 1 Year is chosen, then on day 60 (end of year 1), 1 Million Wealth will be assigned. If the year 20 is chosen, on day 1,200 (end of year 20), 1 million wealth will be assigned. 

All other factors, such as pawn count and adaptation, are applied as normal. 

The Wealth Independent Mode timer is exclusive to each map tile. Each map tile starts the timer at 0. Changing map tiles will reset the Wealth Independent mode timer. 

## Version history[[edit](/index.php?title=Raid_points&action=edit&section=10 "Edit section: Version history")]

  * [1.2.2719](/wiki/Version/1.2.2719 "Version/1.2.2719") \- Storyteller now ignores Hit Points of buildings for purposes of wealth calculation.
  * [1.3.3287](/wiki/Version/1.3.3287 "Version/1.3.3287") \- Added a 0.75x factor to pawn points for colony slaves when calculating threat point (wealth points was already adjusted for slaves). This means having slaves won't attract larger threats as much as colonists.
  * [1.4.3555](/wiki/Version/1.4.3555 "Version/1.4.3555") \- [Friendly mechanoids](/wiki/Friendly_mechanoids "Friendly mechanoids") now count towards pawn points, in addition to wealth points. Slightly reduce the impact that player mechanoids have on raid points.



Retrieved from "[https://rimworldwiki.com/index.php?title=Raid_points&oldid=182207](https://rimworldwiki.com/index.php?title=Raid_points&oldid=182207)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [Game mechanics](/wiki/Category:Game_mechanics "Category:Game mechanics")



Hidden categories: 

  * [Articles verified for 1.3.3101](/wiki/Category:Articles_verified_for_1.3.3101 "Category:Articles verified for 1.3.3101")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Raid+points "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Raid+points "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Raid_points "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Raid_points&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Raid_points)
  * [Edit](/index.php?title=Raid_points&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Raid_points&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Raid_points "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Raid_points "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Raid_points&oldid=182207 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Raid_points&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Raid-5Fpoints)



  * This page was last edited on 19 July 2026, at 00:17.
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
  *[[Note]]: This number is taken from decompiled code. Being a floating-point decimal, the actual value may have been changed in translation.
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
