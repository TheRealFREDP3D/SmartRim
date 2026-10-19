# Beer

From RimWorld Wiki

Jump to navigation Jump to search

Beer

[![Beer](/images/a/a2/Beer_b.png)](/wiki/File:Beer_b.png "Beer")

The first beverage besides water ever consumed by mankind. Beer can taste good, but its main effect is intoxication. Excessive consumption can lead to alcohol blackouts and, over time, addiction.

Base Stats

Type
    [Drug](/wiki/Drug "Drug") – [Social drug](/wiki/Social_drug "Social drug")

Tech Level
    [Neolithic](/wiki/Tech_levels "Tech levels")

Market Value
    12 [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver")

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
    0 [ticks](/wiki/Time "Time") (0 secs)

Melee Combat

Mode
    Melee

Melee Attack 1
    Bottle  
9 dmg ([Blunt](/wiki/Damage_Types#Blunt "Damage Types"))  
13% AP  
2 seconds cooldown

Melee Attack 2
    Neck  
9 dmg ([Poke](/wiki/Damage_Types#Poke "Damage Types"))  
13% AP  
2 seconds cooldown

Creation

Crafted At
    [![Fermenting barrel](/images/thumb/d/d5/FermentingBarrel.png/16px-FermentingBarrel.png)](/wiki/Fermenting_barrel "Fermenting barrel")

Work To Make
    0 [ticks](/wiki/Time "Time") (0 secs)

Resources to make
    [![Wort](/images/thumb/9/94/Wort.png/16px-Wort.png)](/wiki/Wort "Wort") 1

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

  


**Beer** is a beverage that functions as a [drug](/wiki/Drug "Drug"). It provides some [recreation](/wiki/Recreation "Recreation"), and inebriates the user. The more intoxicated a pawn is, the greater their [mood](/wiki/Mood "Mood"), but the worse it is for health and performance. In addition to its intoxicating effects, beer is considered [food](/wiki/Food "Food"), as it gives a small amount of [nutrition](/wiki/Nutrition "Nutrition"). 

It can also be used as a somewhat ineffectual [melee weapon](/wiki/Weapons#Base_melee_stats "Weapons"), doing less DPS than a [club](/wiki/Club "Club") or even a lump of [wood](/wiki/Wood "Wood"), but still more than a normal [human](/wiki/Human "Human") fist. Conveniently, the beer is not lost after using it as a weapon. 

## Contents

  * 1 Acquisition
    * 1.1 Critical temperature
  * 2 Summary
    * 2.1 Upon drinking
    * 2.2 Alcohol high
      * 2.2.1 Hangover
    * 2.3 Tolerance
    * 2.4 Addiction
    * 2.5 Withdrawal
  * 3 Attack table
  * 4 Analysis
    * 4.1 Brewing temperature
    * 4.2 Trade
  * 5 Production math
  * 6 Trivia
  * 7 Gallery
  * 8 Version history



## Acquisition[[edit](/index.php?title=Beer&action=edit&section=1 "Edit section: Acquisition")]

Beer is produced in three steps. It requires the [Beer brewing](/wiki/Research#Beer_brewing "Research") research to create. 

  1. Plant and harvest [hops](/wiki/Hops "Hops"), which is an easy task and can be done without Research (min [Plants Skill](/wiki/Skills#Plants "Skills") 3).
  2. Turn 25 hops into 5 [wort](/wiki/Wort "Wort") at a [brewery](/wiki/Brewery "Brewery"). This is a [Cooking task](/wiki/Work#Cook "Work"), and its [speed](/wiki/Drug_Cooking_Speed "Drug Cooking Speed") dependent on cooking skill. There is no chance of [food poisoning](/wiki/Food_poisoning "Food poisoning"), so unskilled cooks can create wort, just slower.
  3. Place up to 25 units of wort (125 hops) into a [fermenting barrel](/wiki/Fermenting_barrel "Fermenting barrel") for 6 days. Filling the barrel is considered a [Hauling task](/wiki/Work#Haul "Work"). Partial loads of wort are possible, but less efficient. The size of the load relatively to total capacity is represented by the length of the bar displayed on the barrel once any wort has been added.  
If more wort is added to a barrel already fermenting, progress will be delayed proportional to both the wort added and already in the barrel. For example, adding 5 wort to a barrel with 5 wort would halve existing progress. Each wort is converted to 1 beer. If temperatures get too hot or cold, the brewing will fail and no beer will be produced.
  4. When the fermentation is complete, represented by the fill bar changing color from brown to yellow, the completed beer can be removed. This is considered a [Hauling task](/wiki/Work#Haul "Work").



[![](/images/8/8c/Fermenting_progress.png)](/wiki/File:Fermenting_progress.png)

[](/wiki/File:Fermenting_progress.png "Enlarge")

[Fermenting barrels](/wiki/Fermenting_barrel "Fermenting barrel").  
Top: Fermenting, 0% progress  
Bottom: Fermenting, 100% progress  
Bar _length_ shows # of wort inside.

### Critical temperature[[edit](/index.php?title=Beer&action=edit&section=2 "Edit section: Critical temperature")]

The process of brewing involves a living organism, so difficulty can increase greatly depending on your biome's weather conditions. Avoiding delays or failure requires following temperature requirements: 

     Temperature  | Effect   
---|---  
7 °C – 32 °C (44.6 °F – 89.6 °F)  | Ideal fermenting temperature range   
-1 °C – 7 °C (30.2 °F – 44.6 °F)  | Temporarily halts fermentation process, process continues when ideal temperature restored   
> 32 °C (89.6 °F)  
< -1 °C (30.2 °F)  | Freezing or "too hot" is fatal to the brewing process, all product is lost, all the previous work wasted   
  
The inspect pane will indicate 'Overheating' or 'Freezing', increasing by 0.001% per 1 °C (1.8 °F) outside the safe temperature range each [tick](/wiki/Tick "Tick"). This is halted when safe temperature is restored, but not reset. If it reaches 100%, the contents are 'ruined by temperature' and no beer can be obtained. 

## Summary[[edit](/index.php?title=Beer&action=edit&section=3 "Edit section: Summary")]

Beer is a mood enhancing drug that has a variety of effects. These can be broken into effects that occur: 

  * Instantaneously and one time upon using the drug.
  * While high on the drug.
  * After being high on the drug.
  * While having a built-up tolerance to the drug.
  * While addicted to the drug.
  * While withdrawing from the drug.



### Upon drinking[[edit](/index.php?title=Beer&action=edit&section=4 "Edit section: Upon drinking")]

A pawn consuming beer will look for a place to sit in a twenty tile radius first, but will also drink it while standing if it doesn't find one. Drinking a beer takes 0 [ticks](/wiki/Time "Time") (0 secs). It has the following one time effects: 

  * +17% Chemical [recreation](/wiki/Recreation "Recreation")
  * +0.08  [Nutrition](/wiki/Nutrition "Nutrition")
  * If the pawn has the [chemical interest](/wiki/Chemical_interest "Chemical interest") or [chemical fascination](/wiki/Chemical_fascination "Chemical fascination") trait: 
    * +20% [Chemical need](/wiki/Chemical_need "Chemical need")
  * **+3.75% to +15%** Alcohol high severity, depending on tolerance _(see "Alcohol high" below)_
  * +1.6% [Tolerance](/wiki/Drugs#Tolerance "Drugs") severity, divided by body size _(see "Tolerance" below)_
  * If the pawn has 25% tolerance already: 
    * 3% to 15% [Addiction](/wiki/Addiction "Addiction") chance _(see "Addiction" below)_
  * If the pawn has an addiction already: 
    * +90% Alcohol need _(see "Addiction" below)_
    * −20% Addiction progress _(see "Addiction" below)_



### Alcohol high[[edit](/index.php?title=Beer&action=edit&section=5 "Edit section: Alcohol high")]

> "Alcohol in the bloodstream. It makes people happy, but reduces capacities."
> 
> -- Alcohol high description

Each beer increases the alcohol high severity by the following formula: 

`Increase in severity = 0.15 * (100 - (tolerance * 75 round 0))`

Therefore with 0% tolerance the severity increases by 15%, with 100% tolerance by 3.75%. It decreases by 75% per day again, meaning that the high of a single dose lasts between 1.2 and **4.8 hours**. The maximum severity of an alcohol high is 100% which is reached with 6.7 to 26.7 beer. 

The alcohol high severity not only sets the length of the high but also affects the symptoms. 

Level  | Alcohol high severity  | [Mood](/wiki/Mood "Mood") | [Pain](/wiki/Pain "Pain") | [Consciousness](/wiki/Consciousness "Consciousness") | [Moving](/wiki/Moving "Moving") | Social fight chance  | Other effects   
---|---|---|---|---|---|---|---  
Warm  | >0%  | +10 _Alcohol warmth_ [thought](/wiki/Thought "Thought") | ×90% | – | – | ×1.5 | −2% [Manipulation](/wiki/Manipulation "Manipulation")  
Tipsy  | >25%  | +14 _Quite inebriated_ [thought](/wiki/Thought "Thought") | ×80% | ×90% | −5% | ×2.5 | –   
Drunk  | >40%  | +20 _Drunk_ [thought](/wiki/Thought "Thought") | ×50% | ×65% | −10% | ×4 | Vomiting: on average every 0.75 days.  
Hangover once the alcohol high severity drops below 40% (see _"Hangover"_ below).   
Hammered  | >70%  | +26 _Hammered_ [thought](/wiki/Thought "Thought") | ×30% | ×50% | −10% | ×5 | Vomiting: on average every 0.2 days.   
Blackout  | >90%  | –  | ×10% | max. 10% | – | –  | Chemical damage (moderate):  
The [chemical damage](/wiki/Chemical_damage "Chemical damage") occurs on average every 10 days and affects the brain.   
  
Assuming the beers are consumed right after each other with initially 0% tolerance, the different stages last the following times: 

Beers Consumed | Hours Warm | Hours Tipsy | Hours Drunk | Hours Hammered | Hours Blackout   
---|---|---|---|---|---  
1  | 4.8  | 0  | 0  | 0  | 0   
2  | 8  | 1.6  | 0  | 0  | 0   
3  | 8  | 4.8  | 1.5  | 0  | 0   
4  | 8  | 4.8  | 6.1  | 0  | 0   
5  | 8  | 4.8  | 9.6  | 1  | 0   
6  | 8  | 4.8  | 9.6  | 5.5  | 0   
7  | 8  | 4.8  | 9.6  | 6.4  | 3.2   
  
#### Hangover[[edit](/index.php?title=Beer&action=edit&section=6 "Edit section: Hangover")]

> "An unpleasant delayed after-effect of alcohol intoxication."
> 
> -- Hangover description

Once a colonist reaches at least the drunk state, they will go through the hangover stages after their alcohol high severity drops below 40% again. It isn't visible until after the alcohol effect is fully gone however. If a colonist drinks beer while hungover they will be both hungover and inebriated. Severity starts at 100% and decreases consistently to 0% over the course of a full day, 

Level | Severity % | Mood | Consciousness | Other effects   
---|---|---|---|---  
Pounding  | >40%  | −12 _Pounding hangover_ [thought](/wiki/Thought "Thought") | −18% | Vomiting: on average every 0.4 days.   
Strong/serious  | >15%  | −6 _Serious hangover_ [thought](/wiki/Thought "Thought") | −8% |   
Slight/mild  | >0%  | −3 _Mild hangover_ [thought](/wiki/Thought "Thought") | −3% |   
  
### Tolerance[[edit](/index.php?title=Beer&action=edit&section=7 "Edit section: Tolerance")]

Main article: [Tolerance](/wiki/Tolerance "Tolerance")

> "A built-up tolerance to alcohol. The more severe this tolerance is, the more alcohol it takes to get the same effect."
> 
> -- Tolerance description

Each beer consumed increases the tolerance of the pawn by the following formula: 

`Increase in tolerance = 1.6% / body size`

Thus smaller or not fully grown pawns gain more tolerance per drug use then bigger or fully grown ones. An adult [human](/wiki/Human "Human") has a body size of 1. Tolerance decreases at a rate of 1.6% per day. 

See sections _"Alcohol high"_ and _"Addiction"_ for how tolerance affects alcohol high severity and addiction chance respectively. 

If the tolerance is above a certain thresholds it imposes a chance over time to gain the following [ailments](/wiki/Ailments "Ailments"): 

  * Cirrhosis  
**Tolerance above 45%** imposes a chance to get [cirrhosis](/wiki/Cirrhosis "Cirrhosis") in the liver proportional to the tolerance held.  Tolerance | Average cirrhosis interval | Graph   
---|---|---  
45% | 99999 Days  |   
50% | 60 Days   
100% | 45 Days   
  * Carcinoma  
**Tolerance above 45%** imposes a chance to get [carcinoma](/wiki/Carcinoma "Carcinoma") in the liver proportional to the tolerance held.  Tolerance | Average carcinoma interval | Graph   
---|---|---  
45% | 99999 Days  |   
50% | 180 Days   
100% | 150 Days   



### Addiction[[edit](/index.php?title=Beer&action=edit&section=8 "Edit section: Addiction")]

> "A chemical addiction to alcohol. Long-term presence of alcohol has caused neurological adaptations at the cellular level, so the brain can no longer function properly without the drug. Without regular doses of alcohol, withdrawal symptoms will begin. However, extended abstinence will force the brain to adapt back to its normal state, resolving the addiction."
> 
> -- Addiction description

Once a pawn has a alcohol tolerance of 25% or above, each dose carries a chance of alcohol addiction that scales with tolerance. Due to the minimum tolerance to addict, beer can be safely consumed once every 1 day without risking addiction, so long as the pawn has a body size of 1 or higher and their tolerance is not already elevated before starting the schedule. 

The chance of addiction is as follows: 

Tolerance | Addiction chance | Graph   
---|---|---  
0% | 0%  |   
25% | 3%   
50% | 5%   
80% | 15%   
  
The addiction progresses by 3.33% per day from the initial 50%. Once it reaches 100% the addiction is healed, meaning it takes about 15 days to overcome the addiction. Drinking beer during an alcohol addiction will reduce the addiction progress by 20% again _(see "Upon drinking" above)_. 

Developing an addiction also means a pawn has an alcohol [need](/wiki/Needs#Drug_addictions "Needs"). The need for alcohol falls by 50% per day, drinking beer satisfies the need by 90% _(see "Upon drinking" above)_ , meaning the pawn will need to drink beer at least every 1.8 days to prevent withdrawal symptoms. 

### Withdrawal[[edit](/index.php?title=Beer&action=edit&section=9 "Edit section: Withdrawal")]

> "Because of an alcohol addiction, this person needs to regularly consume alcohol to avoid withdrawal symptoms."
> 
> -- Need description

As soon as the alcohol need reaches 0%, the pawn suffers from the following withdrawal symptoms: 

  * −35 [Mood](/wiki/Mood "Mood") (_"Feeling shaky. Everything pisses me off. I keep thinking of drinking."_)
  * −20% [Consciousness](/wiki/Consciousness "Consciousness")
  * −30% [Moving](/wiki/Moving "Moving")
  * −50% [Manipulation](/wiki/Manipulation "Manipulation")
  * Mental break chance: 
    * [Social drug binge](/wiki/Social_drug_binge "Social drug binge"): on average every 40 days. This averages to 0.8 social drug binges during each withdrawal.



##  Attack table 

Feature | Toggle   
---|---  
Attacks| ![Ritual Quality Check Off.png](/images/thumb/3/33/Ritual_Quality_Check_Off.png/24px-Ritual_Quality_Check_Off.png)![Ritual Quality Check On.png](/images/thumb/9/90/Ritual_Quality_Check_On.png/24px-Ritual_Quality_Check_On.png)  
  
* ![Beer](/images/thumb/a/a2/Beer_b.png/32px-Beer_b.png) Beer | Bottle ([Blunt](/wiki/Damage_types#Blunt "Damage types"))|  Neck ([Poke](/wiki/Damage_types#Poke "Damage types"))  | [Human](/wiki/Human "Human"): Left & right fist ([Blunt](/wiki/Damage_types#Blunt "Damage types"))  | HP | Value   
---|---|---|---|---|---  
DPS[1] |  AP[1] |  Dam.  |  Cool.  |  AP  |  DPS  |  Wt.[2] |  Chc.[3] |  Dam.  |  Cool.  |  AP  |  DPS  |  Wt.[2] |  Chc.[3] |  Dam.  |  Cool.  |  AP  |  DPS  |  Wt.[2] |  Chc.[3]  
4.4  | 12.75%  | 9  | 2s  | 13%  | 4.5  | 5.1  | 37.5%  | 9  | 2s  | 13%  | 4.5  | 5.1  | 37.5%  | 8.2  | 2s  | 12%  | 4.1  | 4.6  | **2×** 12.5%  | 50  | 12 [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver")  
  
  1. ↑ 1.0 1.1 Note: This is the actual base average derived from the [melee verb system](/wiki/Weapons#Listed_DPS_on_pawns "Weapons") updated in [1.1.2610](/wiki/Version/1.1.2610 "Version/1.1.2610"), it may sometimes disagree with the listed value in the in-game infobox.  
It may also change depending on the stats and the melee verbs available to the wielder if the weapon is wielded by some other than a baseline [human](/wiki/Human "Human").
  2. ↑ Base selection weight for the attack, used for [melee verb selection](/wiki/Melee_verb_selection "Melee verb selection"). While this weight is consistent for these stats, the resultant category depends on the melee verbs available to the wielder
  3. ↑ Chance for attack to be selected, assuming the weapon is wielded by a baseline [human](/wiki/Human "Human"). It may change depending on the melee verbs available to the wielder



## Analysis[[edit](/index.php?title=Beer&action=edit&section=10 "Edit section: Analysis")]

Beer is one of the most difficult drugs to get addicted to - a pawn at 0% tolerance would need to drink _15_ beers to get addicted. Therefore, beer is great for [chemical interest](/wiki/Chemical_interest "Chemical interest") pawns and [High Life](/wiki/Ideoligions#High_life "Ideoligions") [ideoligions](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"). Note that alcohol binges can still lead to blackouts, which can lead to permanent brain damage. 

Even for ordinary pawns, beer can be a good source of mood increase. One beer per day gives +10 mood for 4.8 hours with no chance for addiction and a tiny −2% Manipulation. It is recommended to set the [drug policy](/wiki/Drug_policy "Drug policy") to remove "Take for Recreation". Instead, set a schedule for pawns to take beer once per day. You can also set pawns to drink beer only when mood is low (while still only once per day) to conserve on beer. 

In some cases, you can use beer to down animals - they will drink it if they have no other food source. This technique can even down [thrumbos](/wiki/Thrumbo "Thrumbo"), allowing for an easy kill. Note that this will take multiple bottles depending on the creature and they will _only_ attempt to drink the beer when there is no other food source that they can reach. This also applies to colony animals, so watch out. 

### Brewing temperature[[edit](/index.php?title=Beer&action=edit&section=11 "Edit section: Brewing temperature")]

Because the "fatal" range is unforgiving even for a moment, it's recommended to keep your temperatures well within the "ideal" range and have a separate, emergency power/temperature system so that an open door or short-term power loss will not cause the loss of the batch. Double-walling your brewery to insulate from extreme temperatures, and/or installing a long* entry hall/room as an "air lock" with doors at each end is not a bad idea. Also, when planning the location of your brewing, be aware that a kitchen will often be quite warm, as active stoves produce excess heat. 

    (* 6 tiles long gives time for the first door to shut before your colonist opens the next, so that your brewery is not exposed to "outside" temperatures. [Autodoors](/wiki/Autodoor "Autodoor") would shorten this required length.)

### Trade[[edit](/index.php?title=Beer&action=edit&section=12 "Edit section: Trade")]

Beer is more or less equal to [smokeleaf joints](/wiki/Smokeleaf_joint "Smokeleaf joint"). Beer takes +40.6% more planter work per item for −44.4% less cook work per item. Beer is worth +9.1% more silver, but it takes longer to load. Therefore, smokeleaf can be better with a better cook, and beer better with a better planter. Beer brewing requires research, though [drug labs](/wiki/Drug_lab "Drug lab") are needed to make smokeleaf at 100% speed, and they are unlocked with [Drug production](/wiki/Research#Drug_production "Research") research. 

Beer is almost completely inferior to [flake](/wiki/Flake "Flake") as a trade drug, as beer takes +25% more planter work per item, is worth −16.7% less per item, for −20% less work per item created (not including extra loading). Flake creation is based off Intellectual skill, so beer may have a niche if you have a pawn great at Cooking, but no intellectual pawn. 

Regardless - if your colony already uses beer, then you can sell any excess beer to traders. 

## Production math[[edit](/index.php?title=Beer&action=edit&section=13 "Edit section: Production math")]

Don't worry, we'll walk you through it... 

  * 25 [hops](/wiki/Hops "Hops") makes 5 [wort](/wiki/Wort "Wort")
  * A single [fermenting barrel](/wiki/Fermenting_barrel "Fermenting barrel") can hold up to 25 wort
  * 1 wort = 1 beer



That means that 125 hops items = 25 wort = 1 full barrel = 25 beer. 

  * Fermentation takes 6 days for 25 beer.
  * 1 pawn can drink 1 beer/day without risk of [addiction](/wiki/Addiction "Addiction").



Due to inefficiency, let's assume that the entire loading process takes 7 days. 1 barrel can therefore support 3.5 pawns (25 beer/7 days). It would not be too hard to have everything in place and approach something just over 6 days/run, which, _if maintained_ , would give you a production rate closer to 1 barrel = beer for 4 pawns. 

Before [difficulty](/wiki/Difficulty "Difficulty") multipliers and the [Plant Harvest Yield](/wiki/Plant_Harvest_Yield "Plant Harvest Yield") stat, and assuming hops are grown in regular soil: 

  * 1 barrel can hold up to 16 [hop plants](/wiki/Hop_plant "Hop plant")' worth of yield at a time.
  * 24 [hop plants](/wiki/Hop_plant "Hop plant") are enough to sustain 1 barrel indefinitely. (This is more than enough to fill a barrel, but hops grow slower than the fermentation process) 
    * In Losing is Fun, a grower with 8 Plants skill would require 30 hop plants to fill 1 barrel indefinitely.



## Trivia[[edit](/index.php?title=Beer&action=edit&section=14 "Edit section: Trivia")]

In real life, beer is brewed from malted barley/wheat, not hops. Hops are used in the brewing of beer to provide flavor and as a preservative. 

Also unlike its RimWorld counterpart, real beer is typically not flammable as it does not have sufficient alcohol content. In fact, a bottle of beer being placed in a fire would be more likely to extinguish it when the bottle broke. 

This, along with [wood](/wiki/Wood "Wood"), is one of only two items that serves dual purposes as both a usable item and an improvised weapons. 

## Gallery[[edit](/index.php?title=Beer&action=edit&section=15 "Edit section: Gallery")]

  * [![](/images/e/e2/Beer_a.png)](/wiki/File:Beer_a.png)

One beer 

  * [![](/images/a/a2/Beer_b.png)](/wiki/File:Beer_b.png)

Stack of beer 




## Version history[[edit](/index.php?title=Beer&action=edit&section=16 "Edit section: Version history")]

  * [0.9.722](/wiki/Version/0.9.722 "Version/0.9.722") \- Possibly Added. Beer brewing, beer drinking, inebriated thoughts, ability impacts and hangovers added.
  * ? - No longer produced directly from hops at the brewery, now must be placed in barrels to ferment.
  * Beta 19/1.0 - Beer fermenting time 10 days -> 6 days. Buffed beer bottles slightly (~10%) above fists in terms of DPS. Alcohol loses hidden ‘buzzed’ stage;‘warm’ begins from 0 severity. Alcohol severity per day -1.0 -> 0.75, so it lasts longer. Alcohol mood gains all increase +2.
  * [1.1.0](/wiki/Version/1.1.0 "Version/1.1.0") \- Fix: Pawn with alcohol-induced brain damage are doomed to die.[Actual change?]
  * [1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062") \- Drug tolerance gain is now divided by body size and not body size squared - this also had the effect of making the suggested safe dose intervals for children correct.



* * *

[Drugs](/wiki/Drugs "Drugs")

[Social drugs](/wiki/Social_drugs "Social drugs")
    [Ambrosia](/wiki/Ambrosia "Ambrosia") • Beer • [Psychite tea](/wiki/Psychite_tea "Psychite tea") • [Smokeleaf joint](/wiki/Smokeleaf_joint "Smokeleaf joint") • [Psilocap](/wiki/Psilocap "Psilocap")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Hard drugs](/wiki/Hard_drugs "Hard drugs")
    [Flake](/wiki/Flake "Flake") • [Go-juice](/wiki/Go-juice "Go-juice") • [Wake-up](/wiki/Wake-up "Wake-up") • [Yayo](/wiki/Yayo "Yayo")

[Medical drugs](/wiki/Medical_drugs "Medical drugs")
    [Luciferium](/wiki/Luciferium "Luciferium") • [Penoxycyline](/wiki/Penoxycyline "Penoxycyline")

[Serums](/wiki/Serums "Serums")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")
    [Ghoul resurrection serum](/wiki/Ghoul_resurrection_serum "Ghoul resurrection serum") • [Juggernaut serum](/wiki/Juggernaut_serum "Juggernaut serum") • [Metalblood serum](/wiki/Metalblood_serum "Metalblood serum") • [Mind-numb serum](/wiki/Mind-numb_serum "Mind-numb serum") • [Voidsight serum](/wiki/Voidsight_serum "Voidsight serum")
  


* * *

[Weapons](/wiki/Weapons "Weapons")

**Melee |** Neolithic
    [Breach axe](/wiki/Breach_axe "Breach axe") • [Club](/wiki/Club "Club") • [Ikwa](/wiki/Ikwa "Ikwa") • [Knife](/wiki/Knife "Knife") ([Jade](/wiki/Jade_knife "Jade knife")) • [Spear](/wiki/Spear "Spear")

Medieval
    [Gladius](/wiki/Gladius "Gladius") • [Longsword](/wiki/Longsword "Longsword") • [Mace](/wiki/Mace "Mace") • [Axe](/wiki/Axe "Axe") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Warhammer](/wiki/Warhammer "Warhammer") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

Ultra
    [Eltex staff](/wiki/Eltex_staff "Eltex staff") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Monosword](/wiki/Monosword "Monosword") ([Persona](/wiki/Persona_monosword "Persona monosword")) [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Plasmasword](/wiki/Plasmasword "Plasmasword") ([Persona](/wiki/Persona_plasmasword "Persona plasmasword")) [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Zeushammer](/wiki/Zeushammer "Zeushammer") ([Persona](/wiki/Persona_zeushammer "Persona zeushammer")) [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

Improvised
    Beer • [Elephant tusk](/wiki/Elephant_tusk "Elephant tusk") • [Thrumbo horn](/wiki/Thrumbo_horn "Thrumbo horn") • [Wood](/wiki/Wood "Wood") • [Alpha thrumbo horn](/wiki/Alpha_thrumbo_horn "Alpha thrumbo horn")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Mastodon tusk](/wiki/Mastodon_tusk "Mastodon tusk")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

**Ranged |** Neolithic
    [Greatbow](/wiki/Greatbow "Greatbow") ([Unique](/wiki/Unique_greatbow "Unique greatbow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Pila](/wiki/Pila "Pila") • [Recurve bow](/wiki/Recurve_bow "Recurve bow") • [Short bow](/wiki/Short_bow "Short bow") • [Flamebow](/wiki/Flamebow "Flamebow") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Medieval
    [Nerve spiker](/wiki/Nerve_spiker "Nerve spiker")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

Industrial
    [Assault rifle](/wiki/Assault_rifle "Assault rifle") ([Unique](/wiki/Unique_assault_rifle "Unique assault rifle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Autopistol](/wiki/Autopistol "Autopistol") • [Bolt-action rifle](/wiki/Bolt-action_rifle "Bolt-action rifle") ([Unique](/wiki/Unique_bolt-action_rifle "Unique bolt-action rifle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Chain shotgun](/wiki/Chain_shotgun "Chain shotgun") ([Unique](/wiki/Unique_chain_shotgun "Unique chain shotgun")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Heavy SMG](/wiki/Heavy_SMG "Heavy SMG") ([Unique](/wiki/Unique_heavy_SMG "Unique heavy SMG")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • Launcher ([EMP](/wiki/EMP_launcher "EMP launcher"), [Incendiary](/wiki/Incendiary_launcher "Incendiary launcher"), [Smoke](/wiki/Smoke_launcher "Smoke launcher"), [Toxbomb](/wiki/Toxbomb_launcher "Toxbomb launcher") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")) • [LMG](/wiki/LMG "LMG") ([Unique](/wiki/Unique_LMG "Unique LMG")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Machine pistol](/wiki/Machine_pistol "Machine pistol") • [Minigun](/wiki/Minigun "Minigun") ([Unique](/wiki/Unique_minigun "Unique minigun")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Pump shotgun](/wiki/Pump_shotgun "Pump shotgun") • [Revolver](/wiki/Revolver "Revolver") ([Unique](/wiki/Unique_revolver "Unique revolver")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Sniper rifle](/wiki/Sniper_rifle "Sniper rifle") ([Unique](/wiki/Unique_sniper_rifle "Unique sniper rifle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Hellcat rifle](/wiki/Hellcat_rifle "Hellcat rifle") ([Unique](/wiki/Unique_hellcat_rifle "Unique hellcat rifle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Incinerator](/wiki/Incinerator "Incinerator")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

Spacer
    [Charge lance](/wiki/Charge_lance "Charge lance") ([Unique](/wiki/Unique_charge_lance "Unique charge lance")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Charge rifle](/wiki/Charge_rifle "Charge rifle") ([Unique](/wiki/Unique_charge_rifle "Unique charge rifle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")) • [Beam graser](/wiki/Beam_graser "Beam graser") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Beam repeater](/wiki/Beam_repeater "Beam repeater") ([Unique](/wiki/Unique_beam_repeater "Unique beam repeater")) [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

Consumables
    [Doomsday rocket launcher](/wiki/Doomsday_rocket_launcher "Doomsday rocket launcher") • [Triple rocket launcher](/wiki/Triple_rocket_launcher "Triple rocket launcher")

Throwables
    [EMP grenades](/wiki/EMP_grenades "EMP grenades") • [Frag grenades](/wiki/Frag_grenades "Frag grenades") • [Molotov cocktails](/wiki/Molotov_cocktails "Molotov cocktails") • [Tox grenades](/wiki/Tox_grenades "Tox grenades") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Mechanoid
    [Heavy charge blaster](/wiki/Heavy_charge_blaster "Heavy charge blaster") • [Inferno cannon](/wiki/Inferno_cannon "Inferno cannon") • [Needle gun](/wiki/Needle_gun "Needle gun") • [Thump cannon](/wiki/Thump_cannon "Thump cannon") • [Charge blaster turret](/wiki/Charge_blaster_turret "Charge blaster turret") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Hellsphere cannon](/wiki/Hellsphere_cannon "Hellsphere cannon") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mini-flameblaster](/wiki/Mini-flameblaster "Mini-flameblaster") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mini-shotgun](/wiki/Mini-shotgun "Mini-shotgun") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Needle launcher](/wiki/Needle_launcher "Needle launcher") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Slugthrower](/wiki/Slugthrower "Slugthrower") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Spiner](/wiki/Spiner "Spiner") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Toxic needle gun](/wiki/Toxic_needle_gun "Toxic needle gun") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Structures
    [Auto-mortar](/wiki/Auto-mortar "Auto-mortar") • [Autocannon](/wiki/Autocannon "Autocannon") • [Inferno cannon (Turret)](/wiki/Inferno_cannon_\(Turret\) "Inferno cannon \(Turret\)") • [Light charge blaster](/wiki/Light_charge_blaster "Light charge blaster") • [Mini-slugger](/wiki/Mini-slugger "Mini-slugger") • [Mini-turret gun](/wiki/Mini-turret_gun "Mini-turret gun") • [Mortar (Weapon)](/wiki/Mortar_\(Weapon\) "Mortar \(Weapon\)") • [Uranium slug cannon](/wiki/Uranium_slug_cannon "Uranium slug cannon") • [Tactical turret gun](/wiki/Tactical_turret_gun "Tactical turret gun") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

Drone
    [Scattergun](/wiki/Scattergun "Scattergun")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

**Related |** [Body part weapons](/wiki/Body_part_weapons "Body part weapons")
    [Prosthetic arm](/wiki/Prosthetic_arm "Prosthetic arm") • [Bionic arm](/wiki/Bionic_arm "Bionic arm") • [Archotech arm](/wiki/Archotech_arm "Archotech arm") • [Power claw](/wiki/Power_claw "Power claw") • [Field hand](/wiki/Field_hand "Field hand") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Drill arm](/wiki/Drill_arm "Drill arm") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Venom talon](/wiki/Venom_talon "Venom talon") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Venom fangs](/wiki/Venom_fangs "Venom fangs") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Knee spike](/wiki/Knee_spike "Knee spike") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Elbow blade](/wiki/Elbow_blade "Elbow blade") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Hand talon](/wiki/Hand_talon "Hand talon") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Flesh whip](/wiki/Flesh_whip "Flesh whip") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

Integrated weapons
    [Grenadier armor](/wiki/Grenadier_armor "Grenadier armor") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Phoenix armor](/wiki/Phoenix_armor "Phoenix armor") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Beer&oldid=181572](https://rimworldwiki.com/index.php?title=Beer&oldid=181572)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Drug](/wiki/Category:Drug "Category:Drug")
  * [Social Drug](/wiki/Category:Social_Drug "Category:Social Drug")
  * [Equipment](/wiki/Category:Equipment "Category:Equipment")
  * [Weapons](/wiki/Category:Weapons "Category:Weapons")
  * [Neolithic Weapons](/wiki/Category:Neolithic_Weapons "Category:Neolithic Weapons")
  * [Melee Weapons](/wiki/Category:Melee_Weapons "Category:Melee Weapons")
  * [Blunt Weapons](/wiki/Category:Blunt_Weapons "Category:Blunt Weapons")
  * [Improvised Weapons](/wiki/Category:Improvised_Weapons "Category:Improvised Weapons")



Hidden categories: 

  * [Unverified articles](/wiki/Category:Unverified_articles "Category:Unverified articles")
  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Beer "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Beer "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Beer "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Beer "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Beer)
  * [Edit](/index.php?title=Beer&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Beer&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Beer "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Beer "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Beer&oldid=181572 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Beer&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Beer)



  * This page was last edited on 5 July 2026, at 16:13.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (237,216,174)
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[28.33 secs]: real-time at 1x speed
  *[Nutrition]: Nutrition gained when this item or object is eaten
  *[Maximum To Ingest]: Maximum Number To Ingest At Once
  *[1.33 secs]: real-time at 1x speed
  *[+4]: Stacking 3 times with a 0.5 multiplier for maximum of 7
  *[_Nuzzled_]: A cute animal nuzzled me.
  *[+5]: Stacking 1 times for a maximum of 5
  *[_[Bonded animal]'s master_]: Being together with my bonded animal makes me feel better.
  *[−3]: Stacking 1 times for a maximum of -3
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
