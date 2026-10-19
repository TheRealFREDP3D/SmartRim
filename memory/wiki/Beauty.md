# Beauty

From RimWorld Wiki

Jump to navigation Jump to search

[![Rewrite.png](/images/thumb/a/a3/Rewrite.png/40px-Rewrite.png)](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten") | This article is suggested to be [rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten"). **Reason:** Fragmented and does not present the information in a new-player-friendly, or holistic fashion. It should start with the object stat and then progress to its applications. Also see other needs for reference in adequate detail re: rise and fall rates, thresholds, etc.. You can help the RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Beauty&action=edit)** it.__  
---|---  
  
This article is about beauty of all items and structures. For the beauty stat of pawns, see [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)").

**Beauty** refers to one of the following, depending on context: 

  * **Physical Beauty** : A property present on certain map objects that indicate how pleasant said object is to look at. Its subdivided in 2 types. 
    * **[Beauty Stat](/wiki/Beauty_\(Stat\) "Beauty \(Stat\)")** : A stat that determines the beauty of an object. If the object is placed outside and has a "Outdoor Beauty" value defined, it uses that instead.
    * **[Outdoor Beauty](/wiki/Outdoor_Beauty "Outdoor Beauty")** : A stat that determines the beauty of an object when placed outside. Mostly used for "natural" objects and surfaces (ex: plants, soil).
  * **Environmental beauty** : The net beauty score of a given map tile. It affects perceived beauty and room impressiveness.
  * **Perceived beauty** : Environmental beauty as perceived by a pawn. It affects "beauty need level" and depends on line of sight.
  * **Beauty need level** : A pawn's [need](/wiki/Need "Need") to live in a beautiful environment (similar to [rest](/wiki/Rest "Rest") and [comfort](/wiki/Comfort "Comfort")); affects [mood](/wiki/Mood "Mood").



## Physical beauty[[edit](/index.php?title=Beauty&action=edit&section=1 "Edit section: Physical beauty")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Beauty&action=edit). Reason:** _Mechanics of indoor/outdoor beauty divides - what is classified as as indoors? Not a room, not a roofed room, etc?._  
---|---  
  
Main articles: [Beauty (Stat)](/wiki/Beauty_\(Stat\) "Beauty \(Stat\)") and [Outdoor Beauty](/wiki/Outdoor_Beauty "Outdoor Beauty")

Physical beauty is a stat of many structures, plants, items, and other objects. Some objects have two beauty stats - one that applies when the object is indoors and another that applies when it is outdoors. 

In the case of pawn-made structures, the beauty stat is calculated from a base value, the [type of material](/wiki/Stuff "Stuff") it is made from, and the [quality](/wiki/Quality "Quality") level of the item. The exact value and calculation of the beauty stat for a specific item can be viewed by mousing over the "beauty" stat in the item's information window. 

Here, an example is given for a [_small marble sculpture_](/wiki/Small_sculpture "Small sculpture") of "good" quality: [(base value of small sculptures) 50 * (material modifier for marble) 1.35 + (material offset for marble) 1] * (quality multiplier for "good quality") 2 = (final value) 137. This sculpture adds 137 of environmental beauty to the tile it is installed on, a fairly high value. 

The most beautiful single structure in the base game is a [legendary](/wiki/Quality "Quality") (x8) [gold](/wiki/Gold "Gold") (x4 +20) [grand](/wiki/Grand_sculpture "Grand sculpture") (400 base) sculpture, which has a beauty of [400 * 4 + 20] * 8 = 12,960. However, note that this is slightly less than the [100 * 4 + 20] * 8 = 3,360 * 4 = 13,440 beauty that 4 legendary gold large sculptures occupying the same 4 tiles could provide, as the offset is applied once per item independent of the base beauty value. 

The formula for pieces of furniture is identical, but their base beauty values are usually substantially lower (ex. a [Bed](/wiki/Bed "Bed") has a base beauty value of 1) than those of works of art, whose primary purpose is to provide environmental beauty. 

Items with beauty of above 100 will have their beauty rounded to be divisible by 5, with a remainder of 2.5 being rounded down. 

## Environmental beauty[[edit](/index.php?title=Beauty&action=edit&section=2 "Edit section: Environmental beauty")]

See also: [Environment](/wiki/Environment#Beauty "Environment")

Each map tile has an integer value that expresses its beauty. This value is the sum of the beauty values of all objects on that tile. This includes include [filth](/wiki/Filth "Filth"), clutter, the [floor](/wiki/Floor "Floor"), furniture and other objects. 

[![](/images/7/79/ToggleShowBeauty.png)](/wiki/File:ToggleShowBeauty.png)

This icon of the mini toolbar toggles the **beauty display**. It shows the environmental and perceived beauty for the map tile under the mouse cursor while enabled. This is what a pawn would "see" if standing on a map tile.

## Perceived beauty[[edit](/index.php?title=Beauty&action=edit&section=3 "Edit section: Perceived beauty")]

A pawn constantly perceives the surrounding **environmental beauty** in an **8-tile radius** (241 total tiles) within its line of sight: objects such as doors or walls will reduce the effective area being evaluated. The perceived beauty is the average value of the Environmental beauty values of all the tiles within the evaluated area for a given pawn at the moment of evaluation. 

A net effect of the above is the placing high beauty objects, such as [sculptures](/wiki/Sculpture "Sculpture"), at the center of large living areas is better than at the edges. 

Pawns require a [sight](/wiki/Sight "Sight") capacity above **0%** to evaluate beauty. 

  * [![](/images/thumb/5/55/Beauty_display_radius.png/120px-Beauty_display_radius.png)](/wiki/File:Beauty_display_radius.png)

The beauty display radius 




## Beauty overlay[[edit](/index.php?title=Beauty&action=edit&section=4 "Edit section: Beauty overlay")]

By hold the 'ALT' key on your keyboard, you can view the beauty of tiles nearby your cursor, Beauty also shows up with room stats (in the button panel on the bottom right), Finally, beauty shows in a pawn's "Needs" tab, these can all be helpful tools in gauging the room's beauty to ensure [impressiveness](/wiki/Impressiveness "Impressiveness"). 

## Beauty need level[[edit](/index.php?title=Beauty&action=edit&section=5 "Edit section: Beauty need level")]

The beauty [need](/wiki/Need "Need") level of a pawn rises and falls with the perceived beauty. This is a delayed effect, and increases register much faster than decreases. 

The level is displayed in percent. A value between 35% and 65% is considered "neutral", and has no effect on the pawn. Values outside that range, either particularly low or high, generate a positive or negative [thought](/wiki/Thoughts_list#Needs_2 "Thoughts list"), influencing the pawn's [mood](/wiki/Mood "Mood") (eg. "Unsightly environment -5" or "Pretty environment +5"). A value of 6 or higher in the beauty display will be enough to move the need towards 100%. 

Keeping the colonists in beautiful surroundings will, effectively, permanently increase their mood. 

_Beauty need_ therefore works similarly to [comfort](/wiki/Comfort "Comfort") need, but can only be fulfilled while the pawn is awake (while _comfort need_ can also be fulfilled while sleeping on comfortable furniture). 

Minimum  
Beauty  
Threshold | Percent  
of Need | Mood  
Bonus   
---|---|---  
6 | 100% | +15  
4.5 | 85-100% | +10  
2.5 | 65-85% | +5  
-0.5 | 35-65% | **0**  
-3.5 | 15-35% | −5  
-3.9 | 0-15% | −10  
-4 | 0% | −15  
  
## Tips[[edit](/index.php?title=Beauty&action=edit&section=6 "Edit section: Tips")]

  * Satisfying the _beauty need_ of your pawns is one of the best ways to improve the [mood](/wiki/Mood "Mood") in your colony. **A beautiful environment can provide constant, substantial mood buffs** practically everywhere, with zero required maintenance.
  * Bedrooms only need enough beauty to keep their [impressiveness](/wiki/Impressiveness "Impressiveness") at the desired level. The beauty level of a pawn does not change during sleep, so excessively beautiful bedrooms do **not** have a strong effect on the pawn's mood in most situations.
  * Because the beauty [need](/wiki/Need "Need") level rises a lot faster than it falls, it is acceptable to have very ugly areas in your base, _if the pawns do not spend long periods of time there_. **Short or intermittent trips into ugly zones have almost no effect on pawn mood** , as long as the beauty level is kept high enough elsewhere.
  * **Naked floor (rough stone or soil) does not take dirt from foot traffic or animals** , as long as nobody is bleeding or vomiting. This can offset the -1 beauty value from the naked floor. Your cleaners will then also not have to clean those areas. Do not do this in places where cleanliness or walk speed matters.
  * Dirty floors tiles have -5 beauty, blood and vomit are a lot worse (-30 and -40). You need to clean regularly if you want a beautiful base. Because of these high negative offsets, dirty floors rapidly lower room [impressiveness](/wiki/Impressiveness "Impressiveness").
  * Strive to decorate all rooms, as well as outdoor areas that are heavily frequented, or where pawns spend extended amounts of time. Examples are the hospital, most workspaces, the recreation area, and the main walkways of the colony. A cheap and easy way of outdoors decoration during the growing season is to plant [roses](/wiki/Rose "Rose"). Decorate larger rooms by spreading the decoration evenly in the space.
  * **Smoothed floors and carpets** can effectively raise an entire room's average beauty by 2 points, a substantial increase. Use these floors in frequented areas, if you can afford it.
  * **Walls** should be smoothed (+2 beauty) or made of marble (+1 beauty). Jade walls have +10 beauty, but it is usually better to craft jade sculptures instead, unless you have excessive amounts of jade and no capable artist to use it.
  * If you need to keep stockpiles in areas that should be beautiful, like the recreation room or the hospital, put the items on [shelves](/wiki/Shelf "Shelf"). Most objects laying naked on the floor have -5 beauty, this gets absorbed by the shelf.
  * A single grand sculpture of very high quality ("masterwork" or "legendary") made of jade (or gold...) can turn even a large room full of rotten corpses into a "beautiful" environment. If you can get your hands on one of these, usually from an inspired master artist in your colony, place them strategically for the best possible impact.
  * [Room Beauty](/wiki/Rooms "Rooms") has the information about Rooms.



## Version history[[edit](/index.php?title=Beauty&action=edit&section=7 "Edit section: Version history")]

  * [1.3.3117](/wiki/Version/1.3.3117 "Version/1.3.3117") \- Some things, like rock chunks, are now considered beautiful when outdoors but ugly when indoors. This solves a problem where a person standing in a nice forest will think their surroundings are ugly.



* * *

Status levels

[Needs](/wiki/Needs "Needs")
    Beauty • [Chemical](/wiki/Chemical_\(Need\) "Chemical \(Need\)") • [Comfort](/wiki/Comfort "Comfort") • [Drug addiction](/wiki/Drug_addiction "Drug addiction") • [Food](/wiki/Saturation "Saturation") • [Indoors](/wiki/Indoors "Indoors") • [Outdoors](/wiki/Outdoors "Outdoors") • [Recreation](/wiki/Recreation "Recreation") • [Rest](/wiki/Rest "Rest") • [Deathrest](/wiki/Deathrest "Deathrest") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Energy](/index.php?title=Energy&action=edit&redlink=1 "Energy \(page does not exist\)") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Kill satiety](/wiki/Kill_satiety "Kill satiety") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Learning](/wiki/Learning "Learning") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Play](/index.php?title=Play&action=edit&redlink=1 "Play \(page does not exist\)") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
Related
    [Hemogen](/wiki/Hemogen "Hemogen") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
Other
    [Mood](/wiki/Mood "Mood") ([Mental break](/wiki/Mental_break "Mental break") • [Mental inspiration](/wiki/Mental_inspiration "Mental inspiration"))
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Beauty&oldid=158399](https://rimworldwiki.com/index.php?title=Beauty&oldid=158399)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Pages to be rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten")
  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Status Level](/wiki/Category:Status_Level "Category:Status Level")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Beauty "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Beauty "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Beauty "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Beauty&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Beauty)
  * [Edit](/index.php?title=Beauty&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Beauty&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Beauty "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Beauty "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Beauty&oldid=158399 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Beauty&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Beauty)



  * This page was last edited on 10 January 2025, at 14:12.
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
  *[[Note]]: This value is automatically calculated by the wiki and may not be correct
  *[13.33 secs]: real-time at 1x speed
  *[Deconstruct yield]: Resources recovered when deconstructing.
  *[Destroy yield]: Resources recovered when destroyed.
