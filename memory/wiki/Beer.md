Beer - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Beer

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 
 Beer

The first beverage besides water ever consumed by mankind. Beer can taste good, but its main effect is intoxication. Excessive consumption can lead to alcohol blackouts and, over time, addiction.

Base Stats

Type
Drug&#32;–&#32; Social drug

Tech Level
Neolithic

Market Value
12&#160;

Stack Limit
25

Mass
0.3 kg

HP
50

Deterioration Rate
0.5

Flammability
50%

Rotatable
False

Path Cost
14 (48%)

Ingestion

Nutrition
0.08

Food Type
processed, fluid, liquor

Taste
Simple

Recreation Offset
17%

Recreation Kind
Chemical

Addictiveness
1%

Maximum To Ingest
1

Ingestion Time
0&#160;ticks (0&#160;secs)

Melee Combat

Mode
Melee

Melee Attack&#160;1
Bottle
9 dmg (Blunt)
13% AP
2 seconds cooldown

Melee Attack 2&#160;
Neck
9 dmg (Poke)
13% AP
2 seconds cooldown

Creation

Crafted At

Work To Make
0&#160;ticks (0&#160;secs)

Resources to make
 1

 Technical
 
defName
Beer
Has Quality
False
tradeTags
Drugs
Preferability
NeverForNutrition
Drug Category
Social
Is Pleasure Drug
true 
 

Beer is a beverage that functions as a drug. It provides some recreation, and inebriates the user. The more intoxicated a pawn is, the greater their mood, but the worse it is for health and performance. In addition to its intoxicating effects, beer is considered food, as it gives a small amount of nutrition.

It can also be used as a somewhat ineffectual melee weapon, doing less DPS than a club or even a lump of wood, but still more than a normal human fist. Conveniently, the beer is not lost after using it as a weapon.

Contents

- 1 Acquisition

- 1.1 Critical temperature

- 2 Summary

- 2.1 Upon drinking

- 2.2 Alcohol high

- 2.2.1 Hangover

- 2.3 Tolerance

- 2.4 Addiction

- 2.5 Withdrawal

- 3 Attack table

- 4 Analysis

- 4.1 Brewing temperature

- 4.2 Trade

- 5 Production math

- 6 Trivia

- 7 Gallery

- 8 Version history

Acquisition[edit]

Beer is produced in three steps. It requires the Beer brewing research to create.

- Plant and harvest hops, which is an easy task and can be done without Research (min Plants Skill 3).

- Turn 25 hops into 5 wort at a brewery. This is a Cooking task, and its speed dependent on cooking skill. There is no chance of food poisoning, so unskilled cooks can create wort, just slower.

- Place up to 25 units of wort (125 hops) into a fermenting barrel for 6 days. Filling the barrel is considered a Hauling task. Partial loads of wort are possible, but less efficient. The size of the load relatively to total capacity is represented by the length of the bar displayed on the barrel once any wort has been added.
If more wort is added to a barrel already fermenting, progress will be delayed proportional to both the wort added and already in the barrel. For example, adding 5 wort to a barrel with 5 wort would halve existing progress. Each wort is converted to 1 beer. If temperatures get too hot or cold, the brewing will fail and no beer will be produced.

- When the fermentation is complete, represented by the fill bar changing color from brown to yellow, the completed beer can be removed. This is considered a Hauling task.

 
Fermenting barrels.
Top: Fermenting, 0% progress
Bottom: Fermenting, 100% progress
Bar length shows # of wort inside.

Critical temperature[edit]

The process of brewing involves a living organism, so difficulty can increase greatly depending on your biome's weather conditions. Avoiding delays or failure requires following temperature requirements:

Temperature

Effect

7&#160;°C&#160;– 32&#160;°C (44.6&#160;°F&#160;– 89.6&#160;°F)

Ideal fermenting temperature range

-1&#160;°C&#160;– 7&#160;°C (30.2&#160;°F&#160;– 44.6&#160;°F)

Temporarily halts fermentation process, process continues when ideal temperature restored

> 32&#160;°C (89.6&#160;°F)
 < -1&#160;°C (30.2&#160;°F)

Freezing or "too hot" is fatal to the brewing process, all product is lost, all the previous work wasted

The inspect pane will indicate 'Overheating' or 'Freezing', increasing by 0.001% per 1&#160;°C (1.8&#160;°F) outside the safe temperature range each tick. This is halted when safe temperature is restored, but not reset. If it reaches 100%, the contents are 'ruined by temperature' and no beer can be obtained.

Summary[edit]

Beer is a mood enhancing drug that has a variety of effects. These can be broken into effects that occur:

- Instantaneously and one time upon using the drug.

- While high on the drug.

- After being high on the drug.

- While having a built-up tolerance to the drug.

- While addicted to the drug.

- While withdrawing from the drug.

Upon drinking[edit]

A pawn consuming beer will look for a place to sit in a twenty tile radius first, but will also drink it while standing if it doesn't find one. Drinking a beer takes 0&#160;ticks (0&#160;secs). It has the following one time effects:

- +17% Chemical recreation

- +0.08 Nutrition

- If the pawn has the chemical interest or chemical fascination trait:
- +20% Chemical need

- +3.75% to +15% Alcohol high severity, depending on tolerance (see "Alcohol high" below)

- +1.6% Tolerance severity, divided by body size (see "Tolerance" below)

- If the pawn has 25% tolerance already:
- 3% to 15% Addiction chance (see "Addiction" below)

- If the pawn has an addiction already:
- +90% Alcohol need (see "Addiction" below)

- −20% Addiction progress (see "Addiction" below)

Alcohol high[edit]

"Alcohol in the bloodstream. It makes people happy, but reduces capacities."
&#8212;&#160;Alcohol high description

Each beer increases the alcohol high severity by the following formula:

Increase in severity = 0.15 * (100 - (tolerance * 75 round 0))

Therefore with 0% tolerance the severity increases by 15%, with 100% tolerance by 3.75%. It decreases by 75% per day again, meaning that the high of a single dose lasts between 1.2 and 4.8&#160;hours. The maximum severity of an alcohol high is 100% which is reached with 6.7 to 26.7&#160;beer.

The alcohol high severity not only sets the length of the high but also affects the symptoms.

Level

Alcohol high severity

Mood

Pain

Consciousness

Moving

Social fight chance

Other effects

Warm

>0%

+10 Alcohol warmth thought

×90%

–
–
×1.5

−2% Manipulation

Tipsy

>25%

+14 Quite inebriated thought

×80%

×90%

−5%

×2.5

–

Drunk

>40%

+20 Drunk thought

×50%

×65%

−10%

×4

Vomiting: on average every 0.75 days.
Hangover once the alcohol high severity drops below 40% (see "Hangover" below).

Hammered

>70%

+26 Hammered thought

×30%

×50%

−10%

×5

Vomiting: on average every 0.2 days.

Blackout

>90%

–

×10%

max. 10%

–
–

Chemical damage (moderate):
The chemical damage occurs on average every 10 days and affects the brain.

Assuming the beers are consumed right after each other with initially 0% tolerance, the different stages last the following times:

Beers Consumed
Hours Warm
Hours Tipsy
Hours Drunk
Hours Hammered
Hours Blackout

1

4.8

0

0

0

0

2

8

1.6

0

0

0

3

8

4.8

1.5

0

0

4

8

4.8

6.1

0

0

5

8

4.8

9.6

1

0

6

8

4.8

9.6

5.5

0

7

8

4.8

9.6

6.4

3.2

Hangover[edit]

"An unpleasant delayed after-effect of alcohol intoxication."
&#8212;&#160;Hangover description

Once a colonist reaches at least the drunk state, they will go through the hangover stages after their alcohol high severity drops below 40% again. It isn't visible until after the alcohol effect is fully gone however. If a colonist drinks beer while hungover they will be both hungover and inebriated. Severity starts at 100% and decreases consistently to 0% over the course of a full day, 

Level
Severity&#160;%
Mood
Consciousness
Other effects

Pounding

>40%

−12 Pounding hangover thought

−18%
Vomiting: on average every 0.4 days.

Strong/serious

>15%

−6 Serious hangover thought

−8%

Slight/mild

>0%

−3 Mild hangover thought

−3%

Tolerance[edit]

Main article: Tolerance

"A built-up tolerance to alcohol. The more severe this tolerance is, the more alcohol it takes to get the same effect."
&#8212;&#160;Tolerance description

Each beer consumed increases the tolerance of the pawn by the following formula:

Increase in tolerance = 1.6% / body size

Thus smaller or not fully grown pawns gain more tolerance per drug use then bigger or fully grown ones. An adult human has a body size of 1. Tolerance decreases at a rate of 1.6% per day.

See sections "Alcohol high" and "Addiction" for how tolerance affects alcohol high severity and addiction chance respectively.

If the tolerance is above a certain thresholds it imposes a chance over time to gain the following ailments:

- Cirrhosis

Tolerance above 45% imposes a chance to get cirrhosis in the liver proportional to the tolerance held.

Tolerance
Average cirrhosis interval
Graph

45%
99999 Days

 

50%
60 Days

100%
45 Days

- Carcinoma

Tolerance above 45% imposes a chance to get carcinoma in the liver proportional to the tolerance held.

Tolerance
Average carcinoma interval
Graph

45%
99999 Days

- 

50%
180 Days

100%
150 Days

Addiction[edit]

"A chemical addiction to alcohol. Long-term presence of alcohol has caused neurological adaptations at the cellular level, so the brain can no longer function properly without the drug. Without regular doses of alcohol, withdrawal symptoms will begin. However, extended abstinence will force the brain to adapt back to its normal state, resolving the addiction."
&#8212;&#160;Addiction description

Once a pawn has a alcohol tolerance of 25% or above, each dose carries a chance of alcohol addiction that scales with tolerance. Due to the minimum tolerance to addict, beer can be safely consumed once every 1&#160;day without risking addiction, so long as the pawn has a body size of 1 or higher and their tolerance is not already elevated before starting the schedule.

The chance of addiction is as follows:

Tolerance
Addiction chance
Graph

0%
0%

- 

25%
3%

50%
5%

80%
15%

The addiction progresses by 3.33% per day from the initial 50%. Once it reaches 100% the addiction is healed, meaning it takes about 15&#160;days to overcome the addiction. Drinking beer during an alcohol addiction will reduce the addiction progress by 20% again (see "Upon drinking" above).

Developing an addiction also means a pawn has an alcohol need. The need for alcohol falls by 50% per day, drinking beer satisfies the need by 90% (see "Upon drinking" above), meaning the pawn will need to drink beer at least every 1.8&#160;days to prevent withdrawal symptoms.

Withdrawal[edit]

"Because of an alcohol addiction, this person needs to regularly consume alcohol to avoid withdrawal symptoms."
&#8212;&#160;Need description

As soon as the alcohol need reaches 0%, the pawn suffers from the following withdrawal symptoms:

- −35 Mood ("Feeling shaky. Everything pisses me off. I keep thinking of drinking.")

- −20% Consciousness

- −30% Moving

- −50% Manipulation

- Mental break chance:
- Social drug binge: on average every 40 days. This averages to 0.8&#160;social drug binges during each withdrawal.

 Attack table 

Feature
Toggle

Attacks

- 

 Beer
Bottle (Blunt) Neck (Poke) 

Human: Left & right fist (Blunt)

HP

Value

 DPS&#91;1&#93; 
 AP&#91;1&#93; 
 Dam. 
 Cool. 
 AP 
 DPS 
 Wt.&#91;2&#93;
 Chc.&#91;3&#93; Dam. 
 Cool. 
 AP 
 DPS 
 Wt.&#91;2&#93;
 Chc.&#91;3&#93; Dam. 
 Cool. 
 AP 
 DPS 
 Wt.&#91;2&#93;
 Chc.&#91;3&#93; 

4.4

12.75%

9

2s

13%

4.5

5.1

37.5%

9

2s

13%

4.5

5.1

37.5%

8.2

2s

12%

4.1

4.6

2× 12.5%

50

12 

- ↑ 1.0 1.1 Note: This is the actual base average derived from the melee verb system updated in 1.1.2610, it may sometimes disagree with the listed value in the in-game infobox.
It may also change depending on the stats and the melee verbs available to the wielder if the weapon is wielded by some other than a baseline human.

- ↑ Base selection weight for the attack, used for melee verb selection. While this weight is consistent for these stats, the resultant category depends on the melee verbs available to the wielder

- ↑ Chance for attack to be selected, assuming the weapon is wielded by a baseline human. It may change depending on the melee verbs available to the wielder

Analysis[edit]

Beer is one of the most difficult drugs to get addicted to - a pawn at 0% tolerance would need to drink 15 beers to get addicted. Therefore, beer is great for chemical interest pawns and High Life ideoligions. Note that alcohol binges can still lead to blackouts, which can lead to permanent brain damage.

Even for ordinary pawns, beer can be a good source of mood increase. One beer per day gives +10 mood for 4.8 hours with no chance for addiction and a tiny −2% Manipulation. It is recommended to set the drug policy to remove "Take for Recreation". Instead, set a schedule for pawns to take beer once per day. You can also set pawns to drink beer only when mood is low (while still only once per day) to conserve on beer.

In some cases, you can use beer to down animals - they will drink it if they have no other food source. This technique can even down thrumbos, allowing for an easy kill. Note that this will take multiple bottles depending on the creature and they will only attempt to drink the beer when there is no other food source that they can reach. This also applies to colony animals, so watch out.

Brewing temperature[edit]

Because the "fatal" range is unforgiving even for a moment, it's recommended to keep your temperatures well within the "ideal" range and have a separate, emergency power/temperature system so that an open door or short-term power loss will not cause the loss of the batch. Double-walling your brewery to insulate from extreme temperatures, and/or installing a long* entry hall/room as an "air lock" with doors at each end is not a bad idea. Also, when planning the location of your brewing, be aware that a kitchen will often be quite warm, as active stoves produce excess heat.

(* 6 tiles long gives time for the first door to shut before your colonist opens the next, so that your brewery is not exposed to "outside" temperatures. Autodoors would shorten this required length.)
Trade[edit]

Beer is more or less equal to smokeleaf joints. Beer takes +40.6% more planter work per item for −44.4% less cook work per item. Beer is worth +9.1% more silver, but it takes longer to load. Therefore, smokeleaf can be better with a better cook, and beer better with a better planter. Beer brewing requires research, though drug labs are needed to make smokeleaf at 100% speed, and they are unlocked with Drug production research.

Beer is almost completely inferior to flake as a trade drug, as beer takes +25% more planter work per item, is worth −16.7% less per item, for −20% less work per item created (not including extra loading). Flake creation is based off Intellectual skill, so beer may have a niche if you have a pawn great at Cooking, but no intellectual pawn.

Regardless - if your colony already uses beer, then you can sell any excess beer to traders.

Production math[edit]

Don't worry, we'll walk you through it...

- 25 hops makes 5 wort

- A single fermenting barrel can hold up to 25 wort

- 1 wort = 1 beer

That means that 125 hops items = 25 wort = 1 full barrel = 25 beer. 

- Fermentation takes 6 days for 25 beer.

- 1 pawn can drink 1 beer/day without risk of addiction.

Due to inefficiency, let's assume that the entire loading process takes 7 days. 1 barrel can therefore support 3.5 pawns (25 beer/7 days). It would not be too hard to have everything in place and approach something just over 6 days/run, which, if maintained, would give you a production rate closer to 1 barrel = beer for 4 pawns.

Before difficulty multipliers and the Plant Harvest Yield stat, and assuming hops are grown in regular soil: 

- 1 barrel can hold up to 16 hop plants' worth of yield at a time.

- 24 hop plants are enough to sustain 1 barrel indefinitely. (This is more than enough to fill a barrel, but hops grow slower than the fermentation process)
- In Losing is Fun, a grower with 8 Plants skill would require 30 hop plants to fill 1 barrel indefinitely.

Trivia[edit]

In real life, beer is brewed from malted barley/wheat, not hops. Hops are used in the brewing of beer to provide flavor and as a preservative. 

Also unlike its RimWorld counterpart, real beer is typically not flammable as it does not have sufficient alcohol content. In fact, a bottle of beer being placed in a fire would be more likely to extinguish it when the bottle broke.

This, along with wood, is one of only two items that serves dual purposes as both a usable item and an improvised weapons.

Gallery[edit]

 - 
 

 
One beer

 

 

 - 
 

 
Stack of beer

 

 

Version history[edit]

- 0.9.722 - Possibly Added. Beer brewing, beer drinking, inebriated thoughts, ability impacts and hangovers added.

- ? - No longer produced directly from hops at the brewery, now must be placed in barrels to ferment.

- Beta 19/1.0 - Beer fermenting time 10 days -> 6 days. Buffed beer bottles slightly (~10%) above fists in terms of DPS. Alcohol loses hidden ‘buzzed’ stage;‘warm’ begins from 0 severity. Alcohol severity per day -1.0 -> 0.75, so it lasts longer. Alcohol mood gains all increase +2.

- 1.1.0 - Fix: Pawn with alcohol-induced brain damage are doomed to die.[Actual change?]

- 1.5.4062 - Drug tolerance gain is now divided by body size and not body size squared - this also had the effect of making the suggested safe dose intervals for children correct.

Drugs

Social drugs
Ambrosia &#8226; Beer &#8226; Psychite tea &#8226; Smokeleaf joint &#8226; Psilocap
Hard drugs
Flake &#8226; Go-juice &#8226; Wake-up &#8226; Yayo
Medical drugs
Luciferium &#8226; Penoxycyline
Serums
Ghoul resurrection serum &#8226; Juggernaut serum &#8226; Metalblood serum &#8226; Mind-numb serum &#8226; Voidsight serum

Weapons

Melee | Neolithic
Breach axe &#8226; Club &#8226; Ikwa &#8226; Knife (Jade) &#8226; Spear
Medieval
Gladius &#8226; Longsword &#8226; Mace &#8226; Axe &#8226; Warhammer 
Ultra
Eltex staff &#8226; Monosword (Persona) &#8226; Plasmasword (Persona) &#8226; Zeushammer (Persona) 
Improvised
Beer &#8226; Elephant tusk &#8226; Thrumbo horn &#8226; Wood &#8226; Alpha thrumbo horn &#8226; Mastodon tusk
Ranged | Neolithic
Greatbow (Unique) &#8226; Pila &#8226; Recurve bow &#8226; Short bow &#8226; Flamebow 
Medieval
Nerve spiker
Industrial
Assault rifle (Unique) &#8226; Autopistol &#8226; Bolt-action rifle (Unique) &#8226; Chain shotgun (Unique) &#8226; Heavy SMG (Unique) &#8226; Launcher (EMP, Incendiary, Smoke, Toxbomb ) &#8226; LMG (Unique) &#8226; Machine pistol &#8226; Minigun (Unique) &#8226; Pump shotgun &#8226; Revolver (Unique) &#8226; Sniper rifle (Unique) &#8226; Hellcat rifle (Unique) &#8226; Incinerator
Spacer
Charge lance (Unique) &#8226; Charge rifle (Unique) &#8226; Beam graser &#8226; Beam repeater (Unique) 
Consumables
Doomsday rocket launcher &#8226; Triple rocket launcher
Throwables
EMP grenades &#8226; Frag grenades &#8226; Molotov cocktails &#8226; Tox grenades 
Mechanoid
Heavy charge blaster &#8226; Inferno cannon &#8226; Needle gun &#8226; Thump cannon &#8226; Charge blaster turret &#8226; Hellsphere cannon &#8226; Mini-flameblaster &#8226; Mini-shotgun &#8226; Needle launcher &#8226; Slugthrower &#8226; Spiner &#8226; Toxic needle gun 
Structures
Auto-mortar &#8226; Autocannon &#8226; Inferno cannon (Turret) &#8226; Light charge blaster &#8226; Mini-slugger &#8226; Mini-turret gun &#8226; Mortar (Weapon) &#8226; Uranium slug cannon &#8226; Tactical turret gun 
Drone
Scattergun
Related | Body part weapons
Prosthetic arm &#8226; Bionic arm &#8226; Archotech arm &#8226; Power claw &#8226; Field hand &#8226; Drill arm &#8226; Venom talon &#8226; Venom fangs &#8226; Knee spike &#8226; Elbow blade &#8226; Hand talon &#8226; Flesh whip 
Integrated weapons
Grenadier armor &#8226; Phoenix armor 

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Beer&oldid=181572"

 Categories: - Drug
- Social Drug
- Equipment
- Weapons
- Neolithic Weapons
- Melee Weapons
- Blunt Weapons
- Improvised Weapons

Hidden categories: - Unverified articles
- Pages that need fact checking
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

 
 

 

 
 - This page was last edited on 5 July 2026, at 16:13.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -