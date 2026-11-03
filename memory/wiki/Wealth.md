Wealth - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Wealth

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 For strategies on limiting wealth, see wealth management.

Wealth is a sum of the Market Value from your items, buildings, and pawns. A colony's total wealth can be viewed in the History tab and going to the Statistics tab. It has a few impacts on the game.

Contents

- 1 Raids

- 1.1 Wealth points

- 1.2 Pawn points

- 1.3 In total

- 2 Expectations

- 3 Room stat

- 4 Archonexus quest

- 5 Analysis

- 5.1 Practical examples

Raids[edit]

Main article: Raid points

Wealth is a key factor in determining the size of raids. Specifically, a colony's entire wealth is converted into "Storyteller Wealth", as follows:

"Storyteller Wealth" = (Colony Wealth Items + Colony Wealth Creatures + (Colony Wealth Buildings * 0.5))

In practice, this just means that buildings placed on the ground count as half wealth for the purposes of raids. 

Once you get "Storyteller Wealth", it is converted into "Wealth Points" and "Pawn Points", which are added together.

Wealth points[edit]

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

At 14,000 "Storyteller Wealth" there are "0 Wealth Points". At 400,000 "Storyteller Wealth" there are "2,400 Wealth Points". Between 14k and 400k wealth, points will increase by (2,400 - 0) / (400,000 - 14,000), or about 1/160.83, per wealth. This means that 1 raid point is worth ~ 160.83 wealth solely from wealth points. 

Wealth also has an impact on "pawn points" factor. 

Pawn points[edit]

"Pawn points" has a similar curve to wealth points.

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

To cut to the chase: below 400k wealth, 1 pawn point/colonist = 3120 wealth. So at 10 healthy adult colonists, 312 wealth = 1 raid point from "Pawn Points". This is added to wealth points. Therefore, the true amount of wealth per raid point depends on your colonist count.

In total[edit]

Assuming wealth < 400k, 1 storyteller wealth gives a total of (1/160.83) + (colonist count/3120) base raid points.

Therefore, 1 raid point would roughly equal to (19.4 + colonist count) / 3120 wealth. 

- At 0 colonists, each raid point is worth ~ 160.83 storyteller wealth.

- At 3 colonists, each raid point is worth ~ 139.29 storyteller wealth.

- At 10 colonists, each raid point is worth ~ 106.12 storyteller wealth.

Base raid points are then modified by a number of other factors, and then converted into raiders.

The most important modifier to raid points is difficulty. Specifically, the "threat scale" setting is a multiplier to raid points. A colony at 200% threat scale will double the raid points, meaning wealth matters twice as much. Once processed, these points are converted directly into raiders. Each raider has a "Combat Points" value, where 1 raid point = 1 combat point. For example, a scyther is worth 150 combat points. The weakest possible raider is worth 30 combat points. For a list of what raiders the storyteller can "buy", see Raiders.

The storyteller setting, Wealth-independent progress mode will make colony wealth have no impact on the game. Instead, "Storyteller Wealth" will be separate from colony wealth. Storyteller Wealth instead will increase linearly over time, until reaching $1,000,000 wealth at the desired Years until maximum threat.

Expectations[edit]

Colony wealth directly impacts the mood and recreation tolerance loss of your colonists. The higher your wealth, the less innately happy a colonist will be and the more bored they will become with their recreation sources.

Name
Mood
Wealth Limits
Recreation Tolerance
Loss/Day
Num. of Recommended
Recreation Types

Extremely low expectations
+30
0 - 15,000
18%
2

Very low expectations
+24
15,000 - 31,000
13%
3

Low expectations
+18
31,000 - 81,000
11%
3

Moderate expectations
+12
81,000 - 182,000
10%
4

High expectations
+ 6
182,000 - 308,000
8%
5

Sky-high expectations
0
308,000 - 1,000,000,000
7%
6

Elite expectations
− 6
High expectations as leader or moral guide
7%
6

Supreme expectations
−12
Sky-high expectations as leader or moral guide
7%
6

The Ideoligious Roles of leader and moral guide instead act as an offset to mood, acting as if they had expectations 2 levels higher.

Conceited nobles have a minimum expectation level, replacing their expectations (after considering role) if they'd be lower than the title's expectations. Conceited Acolytes start at Moderate expectations, increasing by 1 level per title until reaching −6 Noble Expectations at Baron and −12 Royal Expectations at Archon or higher.

In addition, a pawn's ideoligion may desire certain things at certain expectation levels. For example, a Transhumanist ideoligion will desire artificial body parts once expectations reach Moderate.

Room stat[edit]

Main article: Impressiveness

Wealth is a room stat. The sum of all items, buildings, and walls in a room contributes towards wealth. Wealth has no impact on its own, but it increases Impressiveness. Certain types of rooms give positive moodlets if they are impressive, such as a +5 Very impressive dining room or +6 Extremely impressive bedroom. 

Like the other room stats, wealth on its own has a diminishing impact in making a room impressive. Typically, ways of increasing wealth also increase its beauty.

Archonexus quest[edit]

This section relates to content added by Ideology (DLC). Please note that it will not be present without the DLC enabled.

Main article: Endings#The Archonexus

A total colony wealth of $350,000 is required to accept each part of The Archonexus quest. In exchange for your entire colony, you will get an archonexus map piece. Three map pieces are required in total, meaning you'll need 3 separate colonies at this wealth threshold. You don't need to restart again for the third colony.

Analysis[edit]

For strategies on limiting wealth, see wealth management. For strategies on increasing wealth, see money making guide.
To put it simply, you shouldn't feel the need to micromanage wealth, even in Losing is Fun. Extreme forms of wealth management are only really required when playing in an extreme custom difficulty. Wealth scaling means that, as your colony becomes stronger, raids become stronger - a simple relationship. So long as you invest reasonably into good weapons and armor, you should catch up. The expectations moodlets can be countered by placing sculptures and making rooms more beautiful.

Practical examples[edit]

In some scenarios, wealth can be helpful. For small rooms, like bedrooms, increasing wealth has a key impact on overall Impressiveness without impacting space.

- Example 1:

In a 6x7 room, going from wood floor to carpet can turn a room from +0 Dull to +3 Slightly impressive, from both the beauty and the wealth itself. 42 tiles of carpet would be worth &#160;520, which is then halved for raid points because it is a placed building. 

In Strive to Survive, the upgrade to carpet is less than 1/18th of the cheapest possible raider (per bedroom). This is almost negligible. On the flip side, wealth can matter massively at high difficulties. At 500% difficulty, upgrading just 3 bedrooms to carpet would lead to an extra raider. With 9 colonists, that's 3 tribal raiders by using carpet bedrooms. With pirates, this could potentially lead to an extra doomsday rocket launcher or so.

- Example 2:

The effects of wealth alone, and the effect of wealth and beauty combined, is demonstrated in the pictures below:

 - 
 

 
The direct impact of wealth in a small 5x5 room, ignoring beauty completely. 
Ignore it being a "barracks"; bedrolls were used for demonstration purposes.
(Bedrolls do not impact space or beauty)

 

 

 - 
 

 
A wooden large sculpture (normal quality) adds 196, and turns the same room from Mediocre to Slightly impressive, mostly due to beauty.
In Strive to Survive and below, this wealth won't seriously improve raids, even when using multiple sculptures in multiple rooms. At this difficulty, it takes 49 of the same sculpture to add a single extra raider.

 

 

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Wealth&oldid=176573"

 Category: - Game mechanics

Hidden category: - Pages with graphs

 

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

 
 

 

 
 - This page was last edited on 4 March 2026, at 18:01.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -