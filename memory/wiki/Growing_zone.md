# Growing zone

From RimWorld Wiki

Jump to navigation Jump to search

[![Rewrite.png](/images/thumb/a/a3/Rewrite.png/40px-Rewrite.png)](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten") | This article is suggested to be [rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten"). **Reason:** Format standardization - complete separation of Summary and Analysis, cleanup, and stub - growing zone options and their gizmo images, mechanics inc. harvesting/cutting/crop swapping/etc, harvest yield factors (difficulty, skill, RNG, etc). You can help the RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Growing_zone&action=edit)** it.__  
---|---  
  
Growing zone

[![Growing zone](/images/a/ad/Zone4.png)](/wiki/File:Zone4.png "Growing zone")

A zone where your colonists will try to grow a certain kind of plant.

Base Stats

Type
    [Zones](/wiki/Zones "Zones")

Building

Size
    1 × 1 +

Placeable
    True

Blocks Wind
    False
  


A **growing zone** , or grow zone, designates where [grower](/wiki/Work#Grow "Work") pawns can **sow** and/or **harvest** [plants](/wiki/Plants "Plants"), including [trees](/wiki/Trees "Trees") and [decorative plants](/wiki/Decorative_plants "Decorative plants"). They are a major source of [food](/wiki/Food "Food"), [wood](/wiki/Wood "Wood"), [herbal medicine](/wiki/Herbal_medicine "Herbal medicine"), [drugs](/wiki/Drugs "Drugs"), [tinctoria](/wiki/Tinctoria "Tinctoria"), and textiles like [devilstrand](/wiki/Devilstrand "Devilstrand") for a colony. 

## Contents

  * 1 Acquisition
  * 2 Summary
    * 2.1 Contextual menu
  * 3 Analysis
    * 3.1 Design
    * 3.2 Risk Management
    * 3.3 Harvesting wild plants
  * 4 Version history
  * 5 See also



## Acquisition[[edit](/index.php?title=Growing_zone&action=edit&section=1 "Edit section: Acquisition")]

Growing zones do not require a [colonist](/wiki/Colonist "Colonist") to construct or deconstruct, nor is there a cost, work time, or [skill](/wiki/Skill "Skill") requirements for placing them. Instead, they are simply selected from the Architect > Zone [menu](/wiki/User_interface "User interface") and placed directly on the ground by the player, similar to other [zones](/wiki/Zones "Zones"). 

[Environment](/wiki/Environment "Environment") dictates growing zone placement. Growing zones can only be placed on cells of **fertile** terrain. Terrain type is displayed in the lower left corner of the screen **[cell info](/wiki/User_interface "User interface")** by hovering the mouse over a cell with no object selected. Grow zones can't be placed on roofed or unfertile cells: sand, mud, ice, natural stone, water, or constructed [floors](/wiki/Floors "Floors").[Detail]

Colonists will never sow growing zones on days outside of the **growing period** , which is a period of time varying in length according to tile latitude and [biome](/wiki/Biome "Biome"). For example, the growing period in the northern hemisphere of the rimworld usually begins early in the month of [Aprimay](/wiki/Time "Time") (spring) and ends in mid or late Septober (autumn). The local growing period is shown in the [inspect pane](/wiki/User_interface "User interface") when a growing zone is selected. The inspect pane will also detail the quantity and age of plants within the zone and a UI for zone settings. 

Most plants have a **Min growth temperature** of 0 °C (32 °F) and a **Max growth temperature** of 58 °C (136.4 °F). Growing zones outside these temperatures result in growth stagnation and eventual plant death. 

Most plants cannot grow below a light level of 51%, visible in the cell info. Colonists will not sow these squares, and existing plants will die. However, fungi crops like [glowstool](/wiki/Glowstool "Glowstool"), [agarilux](/wiki/Agarilux "Agarilux") and [nutrifungus](/wiki/Nutrifungus "Nutrifungus")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") only grow in darkness. 

## Summary[[edit](/index.php?title=Growing_zone&action=edit&section=2 "Edit section: Summary")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Growing_zone&action=edit). Reason:** _Proper description of options like cutting and sowing. description of what is cut when (mentions cutting edge trees when trees are selected, but doesn't it cut them when trees are the selected crop)._  
---|---  
  
Terrain fertility is shown in the cell info. Fertility determines speed of plant growth, with higher fertility generally resulting in faster growth rates. All plants also have a **minimum fertility requirement** below which they will not grow. Fertility does not affect harvest yield, though. Types of growable terrain include rich soil, normal soil, stoney soil, lichen-covered soil in [Ideology](/wiki/Ideology "Ideology"), and gravel. See [Fertility](/wiki/Plants#Fertility "Plants") for more details. 

Trees planted in growing zones need a 1 tile radius in all directions free of other objects or plants, even those in a separate zone. Growers will remove wild trees and plants next to growing zones to accommodate this radius. Zones set to no cutting will not cut these edge plants. 

  * **Note** : If a colonist is given an order to sow a crop, and that field's plant-type is then changed, the colonist will sow the _original_ plant type, the one that existed _when the order was given_. This is working as intended; you can change a productive growing zone's plant-type, and the new type will be automatically sown _after_ the current crop is harvested so no current planting will be affected, only future planting. So if you change your mind _before_ planting, make sure to cancel/renew any pre-existing sowing orders!



Growing zones do not require any "maintenance" from pawns, such as watering or fertilization. 

If none of your growers have the **required minimum skill** to grow a species of crop, the plant will simply not be sown. 

Colonists will automatically clear growing zones of [stone chunks](/wiki/Stone_chunk "Stone chunk") and place them around the edge of the zone without need for manual [haul](/wiki/Orders#Haul_things "Orders") orders per item. Colonists also remove plants not of the type designated by the zone without the need to designate [chop wood](/wiki/Chop_wood "Chop wood"), [harvest](/wiki/Harvest "Harvest"), or [cut plants](/wiki/Cut_plants "Cut plants"). 

### Contextual menu[[edit](/index.php?title=Growing_zone&action=edit&section=3 "Edit section: Contextual menu")]

[![](/images/thumb/0/03/Growing_zone_gizmos.png/300px-Growing_zone_gizmos.png)](/wiki/File:Growing_zone_gizmos.png)

[](/wiki/File:Growing_zone_gizmos.png "Enlarge")

Growing zone gizmos for a potato field

When a growing zone is selected, an inspect pane and UI appears to allow the player to configure the growing zone's individual settings, including plant species to sow, renaming, resizing, hiding, toggle allowing sowing, and toggle cutting. The inspect pane will also detail the quantity and age of plants within the zone. 

If the zone's crop is changed and sowing and cutting are both allowed, colonists will cut any existing plants and re-sow the zone. 

## Analysis[[edit](/index.php?title=Growing_zone&action=edit&section=4 "Edit section: Analysis")]

_Allow sowing_ after [Raids](/wiki/Raid "Raid"). This is true for [Cassandra Classic](/wiki/Cassandra_Classic "Cassandra Classic") and [Phoebe Chillax](/wiki/Phoebe_Chillax "Phoebe Chillax"). 

### Design[[edit](/index.php?title=Growing_zone&action=edit&section=5 "Edit section: Design")]

Areas of rich soil should generally be prioritized for growing zone placement, but since only growth rate is affected not yield, planting larger fields of crops is roughly as work efficient. It simply takes longer to get a return, with more time and thus risk for crop damage to occur, and more travel and hauling time. Thus, while rich soil should be prioritized if convenient, it is not generally worth planting fields on the other side of the map just to exploit it. Fields nearby to your freezer or kitchen are recommended. 

[Flooring](/wiki/Floor "Floor") to prevent wild plant growth allows for faster movement between your fields, while [roofed](/wiki/Roof "Roof") walkways for the same purpose can also come in handy during [winter](/wiki/Winter "Winter") or [toxic fallout](/wiki/Events_Guide#toxic_fallout "Events Guide"). Both can be combined. 

Estimating the correct size of a growing zone is not easy with so many [factors](/wiki/Plants#Growth_rate_factors "Plants") and [events](/wiki/Events#Generally_Bad "Events") affecting harvest. A quick rule of thumb is to grow 10+ tiles of food crops per colonist in a biome with year-round growing. If the colony hunts as well, it will accumulate some food reserves, which can be saved for winter, fed to prisoners, or sold. More crops should be planted if other factors reduce yields, such as when pawns have low average [Growing skill](/wiki/Skill#Grow "Skill") and in biomes and latitudes with shorter growing periods. 

### Risk Management[[edit](/index.php?title=Growing_zone&action=edit&section=6 "Edit section: Risk Management")]

Random [blight](/wiki/Blight "Blight") epidemics can spread to other crops of any species within a 4 tile radius. Leaving 4 tile wide gaps between your crop fields will mitigate its spread. 

Drought cannot kills crops, but [toxic fallout](/wiki/Toxic_fallout "Toxic fallout") can. Plants do not grow under light levels of 51%, such as during a solar eclipse or at night. 

Hostile raiders will set fire to growing zones if they get the chance. Clear all wild plants and flammable items within at least 2 tiles of growing zones to prevent the spread of [fire](/wiki/Fire "Fire"). The use of nearby [firefoam poppers](/wiki/Firefoam_popper "Firefoam popper") or [foam turrets](/wiki/Foam_turret "Foam turret") is also recommended. 

Bad temperatures will stop plant growth and kill your crops. Below their Min growth temperature, individual plants will spontaneously despawn with a warning note: "_x_ plant has died due to cold.". Thus, it is a waste of time to sow fields at the end of the growing season, as the cold will prevent your crops from reaching harvest maturity (~66% maturity.) 

Wild and tamed animals will eat most plants in growing zones once the plant reaches harvest age (~66% total maturity). It is advisable to use Zones to restrict tamed animals and walls/[fences](/wiki/Fence "Fence") to keep wild beasts out. Harvesting a plant at full maturity generally yields more [nutrition](/wiki/Nutrition "Nutrition") than consuming the growing plant. 

### Harvesting wild plants[[edit](/index.php?title=Growing_zone&action=edit&section=7 "Edit section: Harvesting wild plants")]

Growing zones can be used to automatically harvest [ambrosia](/wiki/Ambrosia "Ambrosia") sprouts or wild [healroot](/wiki/Healroot "Healroot") and chop trees when they reach maturity. Forbid sowing in the growing zone but allow cutting, and colonists will automatically harvest plants within the zone when they grow to full maturity. 

You can double-click an empty tile inside a growing zone to highlight all growing zones on the visible portion of the map. This can be handy in a biome with winter to forbid sowing as winter approaches - but be sure to turn sowing back on before spring! 

[![](/images/thumb/4/48/Growing_zones_example.png/600px-Growing_zones_example.png)](/wiki/File:Growing_zones_example.png)

[](/wiki/File:Growing_zones_example.png "Enlarge")

An example of different growing zones, growing potatoes, cotton, rice, and trees

## Version history[[edit](/index.php?title=Growing_zone&action=edit&section=8 "Edit section: Version history")]

  * [1.3.3067](/wiki/Version/1.3.3067 "Version/1.3.3067") \- Fix: Trees adjacent to no-cut growing zones are cut down.
  * [1.6.4850](/wiki/Version/1.6.4850 "Version/1.6.4850") \- Fix: Error with grow zones in pocket maps.



## See also[[edit](/index.php?title=Growing_zone&action=edit&section=9 "Edit section: See also")]

  * [Hydroponics basin](/wiki/Hydroponics_basin "Hydroponics basin")



* * *

[Architect](/wiki/Architect "Architect")

[Zone/Area](/wiki/Zone/Area "Zone/Area")
    [Stockpile zone](/wiki/Stockpile_zone "Stockpile zone") • [Dumping stockpile zone](/wiki/Dumping_stockpile_zone "Dumping stockpile zone") • Growing zone • [Allowed area](/wiki/Allowed_area "Allowed area") • [Home area](/wiki/Home_area "Home area") • [Build roof area](/wiki/Build_roof_area "Build roof area") • [Remove roof area](/wiki/Remove_roof_area "Remove roof area") • [Snow clear area](/wiki/Zone/Area#Snow_clear_area "Zone/Area")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Growing_zone&oldid=180741](https://rimworldwiki.com/index.php?title=Growing_zone&oldid=180741)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Pages to be rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten")
  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Zones](/wiki/Category:Zones "Category:Zones")



Hidden categories: 

  * [Unverified articles](/wiki/Category:Unverified_articles "Category:Unverified articles")
  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Growing+zone "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Growing+zone "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Growing_zone "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Growing_zone&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Growing_zone)
  * [Edit](/index.php?title=Growing_zone&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Growing_zone&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Growing_zone "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Growing_zone "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Growing_zone&oldid=180741 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Growing_zone&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Growing-5Fzone)



  * This page was last edited on 8 June 2026, at 21:23.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (180,60,60)
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
  *[[Note]]: This number is taken from decompiled code. Being a floating-point decimal, the actual value may have been changed in translation.
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
