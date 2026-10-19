# Ambrosia

From RimWorld Wiki

Jump to navigation Jump to search

Ambrosia

[![Ambrosia](/images/4/4d/Ambrosia_b.png)](/wiki/File:Ambrosia_b.png "Ambrosia")

A soft, rare fruit. Ambrosia tastes wonderful and produces a subtle mood-increasing chemical high. However, if eaten too often, it can generate a mild addiction.

Base Stats

Type
    [Drug](/wiki/Drug "Drug") – [Social drug](/wiki/Social_drug "Social drug")

Tech Level
    [Neolithic](/wiki/Tech_levels "Tech levels")

Market Value
    15 [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver")

Stack Limit
    150

Mass
    0.1 kg

Beauty
    -4

HP
    50

Deterioration Rate
    4

Flammability
    100%

Days To Start Rot
    30

Rotatable
    False

Path Cost
    14 (48%)

Ingestion

Nutrition
    0.2

Food Type
    vegetable

Recreation Offset
    50%

Recreation Kind
    Chemical

Addictiveness
    1%

Maximum To Ingest
    1

Ingestion Time
    80 [ticks](/wiki/Time "Time") (1.33 secs)

Technical 

defName
    Ambrosia
tradeTags
    Drugs
Preferability
    Desperate
Drug Category
    Social 

  


**Ambrosia** is a raw [social drug](/wiki/Social_drug "Social drug") that moderately boosts mood and recreation at relatively low risk of [addiction](/wiki/Addiction "Addiction"). It can only be traded or harvested from [ambrosia bushes](/wiki/Ambrosia_bush "Ambrosia bush") that only spawn in [ambrosia sprout](/wiki/Events#Ambrosia_sprout "Events") events, but cannot be grown by the player. Ambrosia does spoil if not refrigerated. Although it also provides 0.2 [nutrition](/wiki/Nutrition "Nutrition") it is not a vegetarian food. 

## Contents

  * 1 Acquisition
  * 2 Summary
    * 2.1 Upon ingestion
    * 2.2 Ambrosia high
    * 2.3 Tolerance
    * 2.4 Addiction
    * 2.5 Withdrawal
  * 3 Analysis
    * 3.1 Trade
  * 4 Trivia
  * 5 Gallery
  * 6 Version history
  * 7 References



## Acquisition[[edit](/index.php?title=Ambrosia&action=edit&section=1 "Edit section: Acquisition")]

It is harvested from [ambrosia bushes](/wiki/Ambrosia_bush "Ambrosia bush"). They can be harvested multiple times before dying, each time yielding 4 fruit when fully grown. 

A good way to harvest them is to draw a growing zone over them, but forbid sowing. Colonists will then automatically harvest the bushes when they are fully grown. 

The ambrosia event must initially spawn in the growing season of the map tile. The event can only occur, and thus the bush can only be found, in the following [biomes](/wiki/Biomes "Biomes"): 

  * [Tropical rainforest](/wiki/Tropical_rainforest "Tropical rainforest")
  * [Tropical swamp](/wiki/Tropical_swamp "Tropical swamp")
  * [Temperate forest](/wiki/Temperate_forest "Temperate forest")
  * [Temperate swamp](/wiki/Temperate_swamp "Temperate swamp")
  * [Boreal forest](/wiki/Boreal_forest "Boreal forest")
  * [Arid shrubland](/wiki/Arid_shrubland "Arid shrubland")



## Summary[[edit](/index.php?title=Ambrosia&action=edit&section=2 "Edit section: Summary")]

Ambrosia is a moderately potent mood enhancing social drug. Its effects can be broken into effects that occur: 

  * Instantaneously and one time upon using the drug.
  * While high on the drug.
  * While having a built-up tolerance to the drug.
  * While addicted to the drug.
  * While withdrawing from the drug.



### Upon ingestion[[edit](/index.php?title=Ambrosia&action=edit&section=3 "Edit section: Upon ingestion")]

A pawn eating an ambrosia will look for a place to sit in a four tile radius first, but will also eat it while standing if it doesn't find one. Eating an ambrosia takes 80 [ticks](/wiki/Time "Time") (1.33 secs). It has the following one time effects: 

  * +50%  Chemical [recreation](/wiki/Recreation "Recreation")
  * +0.2  [Nutrition](/wiki/Nutrition "Nutrition")
  * If the pawn has the [chemical interest](/wiki/Chemical_interest "Chemical interest") or [chemical fascination](/wiki/Chemical_fascination "Chemical fascination") trait: 
    * +20% [Chemical need](/wiki/Chemical_need "Chemical need")
  * **+12.5% to +50%** Ambrosia high severity, depending on tolerance _(see "Ambrosia high" below)_
  * +3.2%  [Tolerance](/wiki/Drugs#Tolerance "Drugs") severity, divided by body size _(see "Tolerance" below)_
  * If the pawn has 15% tolerance already: 
    * 2.2% to 15% [Addiction](/wiki/Addiction "Addiction") chance _(see "Addiction" below)_
  * If the pawn has an addiction already: 
    * +90%  Ambrosia need _(see "Addiction" below)_
    * −10%  Addiction progress _(see "Addiction" below)_



### Ambrosia high[[edit](/index.php?title=Ambrosia&action=edit&section=4 "Edit section: Ambrosia high")]

> "Ambrosia chemicals in the bloodstream. It lifts the mood."
> 
> -- Ambrosia high description

Each ambrosia increases the ambrosia high severity by the following formula: 

`Increase in severity = 0.5 * (100 - (tolerance * 75 round 0))`

Therefore with 0% tolerance the severity increases by 50%, with 100% tolerance by 12.5%. It decreases by 75% per day again, meaning that the high of a single dose lasts between 4 and 16 hours. The maximum severity of an ambrosia high is 100% which is reached with 2 to 8 ambrosia. Regardless of the ambrosia high severity, the effect is always the same. Only the duration changes accordingly: 

  * +5 [Mood](/wiki/Mood "Mood") (_Ambrosia warmth: "That ambrosia makes me feel more relaxed, and gives me energy at the same time."_)



Without any tolerance, a dose of ambrosia will last for 16 hours. 

### Tolerance[[edit](/index.php?title=Ambrosia&action=edit&section=5 "Edit section: Tolerance")]

Main article: [Tolerance](/wiki/Tolerance "Tolerance")

> "A built-up tolerance to ambrosia. The more severe this tolerance is, the more ambrosia it takes to get the same effect."
> 
> -- Tolerance description

Each ambrosia consumed increases the tolerance of the pawn by the following formula: 

`Increase in tolerance = 3.2% / body size`

Thus smaller or not fully grown pawns gain more tolerance per drug use then bigger or fully grown ones. An adult [human](/wiki/Human "Human") has a body size of 1. Tolerance decreases at a rate of 2% per day. 

See sections _"Ambrosia high"_ and _"Addiction"_ for how tolerance affects ambrosia high severity and addiction chance respectively. Otherwise tolerance against ambrosia has no ongoing effects. 

### Addiction[[edit](/index.php?title=Ambrosia&action=edit&section=6 "Edit section: Addiction")]

> "A chemical addiction to ambrosia. Long-term presence of ambrosia has caused neurological adaptations at the cellular level, so the brain can no longer function properly without the drug. Without regular doses of ambrosia, withdrawal symptoms will begin. However, extended abstinence will force the brain to adapt back to its normal state, resolving the addiction."
> 
> -- Addiction description

Once a pawn has a tolerance of 15% or above, each dose carries a chance of addiction that scales with tolerance. Due to the minimum tolerance to addict, ambrosia can be safely consumed once every 1.6 days without risking addiction, so long as tolerance is not already elevated before starting the schedule. 

The chance of addiction is as follows: 

Tolerance | Addiction chance | Graph   
---|---|---  
0% | 0%  |   
15% | 2.2%   
50% | 5%   
80% | 15%   
  
The addiction progresses by 10% per day from the initial 50%. Once it reaches 100% the addiction is healed, meaning it takes about 5 days to overcome the addiction. Consuming ambrosia during an addiction will reduce the addiction progress by 10% again _(see "Upon ingestion" above)_. 

Developing an addiction means a pawn has an ambrosia [need](/wiki/Needs#Drug_addictions "Needs"). The need for ambrosia falls by 50% per day, consuming ambrosia satisfies the need by 90% _(see "Upon ingestion" above)_ , meaning the pawn will need to consume ambrosia at least every 1.8 days to prevent withdrawal symptoms. 

### Withdrawal[[edit](/index.php?title=Ambrosia&action=edit&section=7 "Edit section: Withdrawal")]

> "Because of an ambrosia addiction, this person needs to regularly consume ambrosia to avoid withdrawal symptoms."
> 
> -- Need description

As soon as the ambrosia need reaches 0% the pawn suffers from the following withdrawal symptom: 

  * −10 [Mood](/wiki/Mood "Mood") (_"I feel heavy and cold all the time. I never thought I'd want a piece of fruit so much."_)



## Analysis[[edit](/index.php?title=Ambrosia&action=edit&section=8 "Edit section: Analysis")]

With an easily avoidable addiction and relatively minor withdrawal symptoms, ambrosia is easily the safest drug to ingest in the game. Each ambrosia sprout might provide 200-300 fruits, enough to last 5 pawns an entire year. A +5 moodlet for 16 hours every 2 days can be meaningful in the early game. Unlike [beer](/wiki/Beer "Beer") and [smokeleaf joints](/wiki/Smokeleaf_joint "Smokeleaf joint"), ambrosia gives no work-related penalties. Eating the fruit also gives pawns an extra bit of nutrition. At the same time, ambrosia can be useless to a colony already in great spirits. At the very worst, ambrosia can be stored to help pawns in mood emergencies, or be sold immediately. 

Whether an ambrosia sprout is worth harvesting largely depends on how far away it is. It isn't worth it to constantly travel halfway across the map just a for a bit of ambrosia. Nearby ambrosia sprouts can be very valuable, however. 

### Trade[[edit](/index.php?title=Ambrosia&action=edit&section=9 "Edit section: Trade")]

Ambrosia is a good supplemental source of money. When considering the raw numbers, ambrosia is superior to any other drug. However, it only appears from the ambrosia sprout event, meaning that quantity is ultimately limited. 

Compared to [flake](/wiki/Flake "Flake"), each ambrosia fruit is worth [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver") 1 [silver](/wiki/Silver "Silver") more, and each bush has a base yield of 4 fruits when harvested (compared to 2 flake per [psychoid plant](/wiki/Psychoid_plant "Psychoid plant")). And there is no need (or ability) to process ambrosia any further. This makes ambrosia strictly superior to flake for cash. Of course, this is before travel time. 

## Trivia[[edit](/index.php?title=Ambrosia&action=edit&section=10 "Edit section: Trivia")]

Ambrosia was added into the game at the request of Designer-tier [Kickstarter backer](https://www.kickstarter.com/projects/tynansylvester/rimworld/rewards) AspenShadow. [1]

## Gallery[[edit](/index.php?title=Ambrosia&action=edit&section=11 "Edit section: Gallery")]

  * [![](/images/0/04/Ambrosia_a.png)](/wiki/File:Ambrosia_a.png)

One ambrosia 

  * [![](/images/4/4d/Ambrosia_b.png)](/wiki/File:Ambrosia_b.png)

Stack of ambrosia 




## Version history[[edit](/index.php?title=Ambrosia&action=edit&section=12 "Edit section: Version history")]

  * [1.3.3066](/wiki/Version/1.3.3066 "Version/1.3.3066") \- Fix: Ambrosia can be selected as food for caravans.
  * [1.4.3580](/wiki/Version/1.4.3580 "Version/1.4.3580") \- Fix: Ambrosia ingestion float menu option displays untranslated key "ConsumeThing".
  * [1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062") \- Drug tolerance gain is now divided by body size and not body size squared - this also had the effect of making the suggested safe dose intervals for children correct.



## References[[edit](/index.php?title=Ambrosia&action=edit&section=13 "Edit section: References")]

  1. ↑ " Yes! Some did do this more recently, actually. As I recall: Ambrosia plant: AspenShadow Chain shotgun: William Salt" - Tynan Sylvester, [Reddit comment](https://www.reddit.com/r/RimWorld/comments/6o2at0/comment/dkf8vu8).



* * *

[Drugs](/wiki/Drugs "Drugs")

[Social drugs](/wiki/Social_drugs "Social drugs")
    Ambrosia • [Beer](/wiki/Beer "Beer") • [Psychite tea](/wiki/Psychite_tea "Psychite tea") • [Smokeleaf joint](/wiki/Smokeleaf_joint "Smokeleaf joint") • [Psilocap](/wiki/Psilocap "Psilocap")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Hard drugs](/wiki/Hard_drugs "Hard drugs")
    [Flake](/wiki/Flake "Flake") • [Go-juice](/wiki/Go-juice "Go-juice") • [Wake-up](/wiki/Wake-up "Wake-up") • [Yayo](/wiki/Yayo "Yayo")

[Medical drugs](/wiki/Medical_drugs "Medical drugs")
    [Luciferium](/wiki/Luciferium "Luciferium") • [Penoxycyline](/wiki/Penoxycyline "Penoxycyline")

[Serums](/wiki/Serums "Serums")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")
    [Ghoul resurrection serum](/wiki/Ghoul_resurrection_serum "Ghoul resurrection serum") • [Juggernaut serum](/wiki/Juggernaut_serum "Juggernaut serum") • [Metalblood serum](/wiki/Metalblood_serum "Metalblood serum") • [Mind-numb serum](/wiki/Mind-numb_serum "Mind-numb serum") • [Voidsight serum](/wiki/Voidsight_serum "Voidsight serum")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Ambrosia&oldid=181560](https://rimworldwiki.com/index.php?title=Ambrosia&oldid=181560)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Drug](/wiki/Category:Drug "Category:Drug")
  * [Social Drug](/wiki/Category:Social_Drug "Category:Social Drug")



Hidden categories: 

  * [Unverified articles](/wiki/Category:Unverified_articles "Category:Unverified articles")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Ambrosia "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Ambrosia "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Ambrosia "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Ambrosia&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Ambrosia)
  * [Edit](/index.php?title=Ambrosia&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Ambrosia&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Ambrosia "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Ambrosia "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Ambrosia&oldid=181560 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Ambrosia&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Ambrosia)



  * This page was last edited on 5 July 2026, at 15:13.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (237,216,174)
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[28.33 secs]: real-time at 1x speed
  *[Nutrition]: Nutrition gained when this item or object is eaten
  *[Maximum To Ingest]: Maximum Number To Ingest At Once
  *[1.33 secs]: real-time at 1x speed
