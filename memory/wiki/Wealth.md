# Wealth

From RimWorld Wiki

Jump to navigation Jump to search

For strategies on limiting wealth, see [wealth management](/wiki/Wealth_management "Wealth management").

**Wealth** is a sum of the [Market Value](/wiki/Market_Value "Market Value") from your items, buildings, and pawns. A colony's total wealth can be viewed in the [History](/wiki/History "History") tab and going to the [Statistics](/wiki/History#Statistics "History") tab. It has a few impacts on the game. 

## Contents

  * 1 Raids
    * 1.1 Wealth points
    * 1.2 Pawn points
    * 1.3 In total
  * 2 Expectations
  * 3 Room stat
  * 4 Archonexus quest
  * 5 Analysis
    * 5.1 Practical examples



## Raids[[edit](/index.php?title=Wealth&action=edit&section=1 "Edit section: Raids")]

Main article: [Raid points](/wiki/Raid_points "Raid points")

Wealth is a key factor in determining the size of [raids](/wiki/Raid "Raid"). Specifically, a colony's entire wealth is converted into "Storyteller Wealth", as follows: 

"Storyteller Wealth" = (Colony Wealth Items + Colony Wealth Creatures + (Colony Wealth Buildings * 0.5))   
---  
  
In practice, this just means that buildings placed on the ground count as half wealth for the purposes of raids. 

Once you get "Storyteller Wealth", it is converted into "Wealth Points" and "Pawn Points", which are added together. 

### Wealth points[[edit](/index.php?title=Wealth&action=edit&section=2 "Edit section: Wealth points")]

"Storyteller Wealth" is linearly interpolated on a graph to create "Wealth Points". 

Graph | Points | Storyteller Wealth   
---|---|---  
| 0 | 0   
0 | 14,000   
2,400 | 400,000   
3,600 | 700,000   
4,200 | 1,000,000   
  
At 14,000 "Storyteller Wealth" there are "0 Wealth Points". At 400,000 "Storyteller Wealth" there are "2,400 Wealth Points". Between 14k and 400k wealth, points will increase by `(2,400 - 0) / (400,000 - 14,000)`, or about `1/160.83`, per wealth. This means that 1 raid point is worth ~ 160.83 wealth _solely from wealth points_. 

Wealth _also_ has an impact on ["pawn points"](/wiki/Raid_points#Pawn_points "Raid points") factor. 

### Pawn points[[edit](/index.php?title=Wealth&action=edit&section=3 "Edit section: Pawn points")]

"Pawn points" has a similar curve to wealth points. 

Graph | Points | Storyteller Wealth   
---|---|---  
| 15 | 0   
15 | 10,000   
140 | 400,000   
200 | 1,000,000   
  
To cut to the chase: below 400k wealth, 1 pawn point/colonist = 3120 wealth. So at 10 healthy adult colonists, 312 wealth = 1 raid point from "Pawn Points". This is added to wealth points. Therefore, the true amount of wealth per raid point depends on your colonist count. 

### In total[[edit](/index.php?title=Wealth&action=edit&section=4 "Edit section: In total")]

Assuming wealth < 400k, 1 storyteller wealth gives a total of `(1/160.83) + (colonist count/3120)` base raid points. 

Therefore, 1 raid point would roughly equal to `(19.4 + colonist count) / 3120` wealth. 

  * At 0 colonists, each raid point is worth ~ 160.83 storyteller wealth.
  * At 3 colonists, each raid point is worth ~ 139.29 storyteller wealth.
  * At 10 colonists, each raid point is worth ~ 106.12 storyteller wealth.



Base raid points are then modified by a number of other factors, and then converted into raiders. 

The most important modifier to raid points is [difficulty](/wiki/Difficulty "Difficulty"). Specifically, the "[threat scale](/wiki/AI_Storytellers#Threat_scale "AI Storytellers")" setting is a multiplier to raid points. A colony at 200% threat scale will double the raid points, meaning wealth matters twice as much. Once processed, these points are converted directly into raiders. Each raider has a "Combat Points" value, where 1 raid point = 1 combat point. For example, a [scyther](/wiki/Scyther "Scyther") is worth 150 combat points. The weakest possible raider is worth 30 combat points. For a list of what raiders the storyteller can "buy", see [Raiders](/wiki/Raiders#human "Raiders"). 

The storyteller setting, [Wealth-independent progress mode](/wiki/AI_Storytellers#Wealth-independent_progress_mode "AI Storytellers") will make colony wealth have no impact on the game. Instead, "Storyteller Wealth" will be separate from colony wealth. Storyteller Wealth instead will increase linearly over time, until reaching $1,000,000 wealth at the desired [Years until maximum threat](/wiki/AI_Storytellers#Years_until_maximum_threat "AI Storytellers"). 

## Expectations[[edit](/index.php?title=Wealth&action=edit&section=5 "Edit section: Expectations")]

Colony wealth directly impacts the [mood](/wiki/Mood "Mood") and [recreation tolerance loss](/wiki/Recreation#Recreation_tolerance "Recreation") of your colonists. The higher your wealth, the less innately happy a colonist will be and the more bored they will become with their recreation sources. 

Name | Mood | Wealth Limits | Recreation Tolerance  
Loss/Day | Num. of Recommended  
Recreation Types   
---|---|---|---|---  
Extremely low expectations | +30 | 0 - 15,000 | 18% | 2   
Very low expectations | +24 | 15,000 - 31,000 | 13% | 3   
Low expectations | +18 | 31,000 - 81,000 | 11% | 3   
Moderate expectations | +12 | 81,000 - 182,000 | 10% | 4   
High expectations | \+ 6 | 182,000 - 308,000 | 8% | 5   
Sky-high expectations | **0** | 308,000 - 1,000,000,000 | 7% | 6   
Elite expectations[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | − 6 | High expectations as [leader](/wiki/Leader "Leader") or [moral guide](/wiki/Moral_guide "Moral guide") | 7% | 6   
Supreme expectations[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | −12 | Sky-high expectations as [leader](/wiki/Leader "Leader") or [moral guide](/wiki/Moral_guide "Moral guide") | 7% | 6   
  
The [Ideoligious Roles](/wiki/Roles "Roles")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") of [leader](/wiki/Leader "Leader") and [moral guide](/wiki/Moral_guide "Moral guide") instead act as an _offset_ to mood, acting as if they had expectations 2 levels higher. 

[Conceited nobles](/wiki/Conceited_noble "Conceited noble")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") have a minimum expectation level, replacing their expectations (after considering role) if they'd be lower than the title's expectations. Conceited Acolytes start at Moderate expectations, increasing by 1 level per title until reaching −6 _Noble Expectations_ at Baron and −12 _Royal Expectations_ at Archon or higher. 

In addition, a pawn's [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") may desire certain things at certain expectation levels. For example, a [Transhumanist](/wiki/Transhumanist "Transhumanist") ideoligion will desire artificial body parts once expectations reach Moderate. 

## Room stat[[edit](/index.php?title=Wealth&action=edit&section=6 "Edit section: Room stat")]

Main article: [Impressiveness](/wiki/Impressiveness "Impressiveness")

Wealth is a [room stat](/wiki/Room_stats "Room stats"). The sum of all items, buildings, and walls in a room contributes towards wealth. Wealth has no impact on its own, but it increases [Impressiveness](/wiki/Impressiveness "Impressiveness"). Certain [types of rooms](/wiki/Room_roles "Room roles") give positive [moodlets](/wiki/Mood "Mood") if they are impressive, such as a +5 _Very impressive[dining room](/wiki/Table "Table")_ or +6 _Extremely impressive[bedroom](/wiki/Bed "Bed")_. 

Like the other room stats, wealth on its own has a diminishing impact in making a room impressive. Typically, ways of increasing wealth also increase its [beauty](/wiki/Beauty "Beauty"). 

## Archonexus quest[[edit](/index.php?title=Wealth&action=edit&section=7 "Edit section: Archonexus quest")]

[![IdeologyIcon.png](/images/thumb/9/94/IdeologyIcon.png/40px-IdeologyIcon.png)](/wiki/Ideology_\(DLC\) "Ideology \(DLC\)") | **This section relates to content added by[Ideology (DLC)](/wiki/Ideology_\(DLC\) "Ideology \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
  
Main article: [Endings#The Archonexus](/wiki/Endings#The_Archonexus "Endings")

A total colony wealth of $350,000 is required to accept each part of The Archonexus quest. In exchange for your entire colony, you will get an archonexus map piece. Three map pieces are required in total, meaning you'll need 3 separate colonies at this wealth threshold. You don't need to restart again for the third colony. 

## Analysis[[edit](/index.php?title=Wealth&action=edit&section=8 "Edit section: Analysis")]

    _For strategies on limiting wealth, see[wealth management](/wiki/Wealth_management "Wealth management"). For strategies on increasing wealth, see [money making guide](/wiki/Money_making_guide "Money making guide")._

To put it simply, you shouldn't feel the need to micromanage wealth, even in Losing is Fun. Extreme forms of wealth management are only really required when playing in an extreme custom [difficulty](/wiki/Difficulty "Difficulty"). Wealth scaling means that, as your colony becomes stronger, raids become stronger - a simple relationship. So long as you invest reasonably into good weapons and armor, you should catch up. The expectations moodlets can be countered by placing [sculptures](/wiki/Sculpture "Sculpture") and making rooms more beautiful. 

### Practical examples[[edit](/index.php?title=Wealth&action=edit&section=9 "Edit section: Practical examples")]

In some scenarios, wealth can be helpful. For small rooms, like bedrooms, increasing wealth has a key impact on overall Impressiveness without impacting space. 

  * **Example 1:**



In a 6x7 room, going from [wood floor](/wiki/Wood_floor "Wood floor") to [carpet](/wiki/Carpet "Carpet") can turn a room from **+0** _Dull_ to +3 _Slightly impressive_ , from both the [beauty](/wiki/Beauty "Beauty") and the wealth itself. 42 tiles of carpet would be worth [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver") 520, which is then halved for raid points because it is a placed building. 

In Strive to Survive, the upgrade to carpet is less than 1/18th of the cheapest possible raider (per bedroom). This is almost negligible. On the flip side, wealth can matter massively at high difficulties. At 500% difficulty, upgrading just 3 bedrooms to carpet would lead to an extra raider. With 9 colonists, that's 3 tribal raiders by using carpet bedrooms. With pirates, this could potentially lead to an extra [doomsday rocket launcher](/wiki/Doomsday_rocket_launcher "Doomsday rocket launcher") or so. 

  * **Example 2:**



The effects of wealth alone, and the effect of wealth and beauty combined, is demonstrated in the pictures below: 

  * [![](/images/thumb/7/7d/Bedroom_wealth.png/489px-Bedroom_wealth.png)](/wiki/File:Bedroom_wealth.png)

The _direct_ impact of wealth in a small 5x5 room, ignoring [beauty](/wiki/Beauty "Beauty") completely.   
Ignore it being a "barracks"; bedrolls were used for demonstration purposes.  
(Bedrolls do not impact space or beauty) 

  * [![](/images/thumb/5/53/Bedroom_wealth2.png/463px-Bedroom_wealth2.png)](/wiki/File:Bedroom_wealth2.png)

A wooden [large sculpture](/wiki/Large_sculpture "Large sculpture") (normal quality) adds [![Silver](/images/thumb/5/57/Silver_c.png/16px-Silver_c.png)](/wiki/Silver "Silver") 196, and turns the same room from _Mediocre_ to _Slightly impressive_ , mostly due to beauty.  
In Strive to Survive and below, this wealth won't seriously improve raids, even when using multiple sculptures in multiple rooms. At this difficulty, it takes 49 of the same sculpture to add a single extra raider. 




Retrieved from "[https://rimworldwiki.com/index.php?title=Wealth&oldid=176573](https://rimworldwiki.com/index.php?title=Wealth&oldid=176573)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [Game mechanics](/wiki/Category:Game_mechanics "Category:Game mechanics")



Hidden category: 

  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Wealth "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Wealth "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Wealth "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Wealth&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Wealth)
  * [Edit](/index.php?title=Wealth&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Wealth&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Wealth "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Wealth "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Wealth&oldid=176573 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Wealth&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Wealth)



  * This page was last edited on 4 March 2026, at 18:01.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[+4]: Stacking 1 times for a maximum of 4
  *[_Nuzzled_]: A cute animal nuzzled me.
  *[+5]: Stacking 10 times with a 0.9 multiplier for maximum of 33
  *[_[Bonded animal]'s master_]: Being together with my bonded animal makes me feel better.
  *[−3]: Stacking 5 times with a 0.75 multiplier for maximum of -9
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
  *[−2]: Stacking 20 times with a 0.75 multiplier for maximum of -8
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
  *[4 secs]: real-time at 1x speed
  *[11.11 mins]: real-time at 1x speed
  *[−5]: Stacking 1 times for a maximum of -5
  *[_Darkness_]: I've been in the dark for a while. I don't like it.
  *[+16]: Stacking 1 times for a maximum of 16
  *[_Night owl at night_]: I feel much better at night.
  *[−10]: Stacking 1 times for a maximum of -10
  *[_Night owl in daytime_]: I don't like working during the day.
  *[+3]: Stacking 1 times for a maximum of 3
  *[_Undergrounder indoors_]: I like working or simply being indoors.
  *[_Underground_]: I love working or simply being in the underground.
  *[_Undergrounder outdoors_]: I don't like being outside. I want to get back to the underground.
  *[+20]: Stacking 1 times for a maximum of 20
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
  *[−12]: Stacking 1 times for a maximum of -12
  *[_Ate corpse_]: I had to eat the flesh of a dead creature without even butchering or cooking it.
  *[_Brawler has ranged weapon_]: I hate shooting from a distance. I want to get up close and personal!
  *[_Kind words_]: I've been bestowed with kind words! What a nice person!
  *[_Denied joining_]: We just denied someone's request to join us. I hope they make it.
  *[_Chemical hunger_]: I'm interested in drugs. I want to try more./I'm interested in drugs. I want to experience a lot more./I'm interested in drugs. I want to consume drugs really badly.
  *[_Chemical satisfaction_]: I'm interested in drugs. I enjoyed satisfying my desire./I'm interested in drugs. I am really satisfied with all the drugs I've gotten recently.
  *[_Forced to take drugs_]: I'm a teetotaler; I would never take drugs by choice. But I was forced! I feel unclean.
  *[c/s]: cells per second
  *[_Sanguine_]: Natural bonus from 'sanguine' trait.
  *[+6]: Stacking 1 times for a maximum of 6
  *[_Optimist_]: Natural bonus from 'optimist' trait.
  *[_Pessimist_]: Natural penalty from 'optimist' trait.
  *[_Depressive_]: Natural penalty from 'optimist' trait.
  *[_OTHER rambling_]: OTHER is talking nonsense. Is s/he insane?
  *[_Captured entity_]: Such a magnificent creature. So much mystery. So much power.
