# Mental inspiration

From RimWorld Wiki

(Redirected from [Inspiration](/index.php?title=Inspiration&redirect=no "Inspiration"))

Jump to navigation Jump to search

[![](/images/b/bb/IconsColonistBarInspired.png)](/wiki/File:IconsColonistBarInspired.png)

[](/wiki/File:IconsColonistBarInspired.png "Enlarge")

Icon for inspired colonists.

[![](/images/1/15/Colonist_icon_with_inspiration.png)](/wiki/File:Colonist_icon_with_inspiration.png)

[](/wiki/File:Colonist_icon_with_inspiration.png "Enlarge")

An inspired colonist in the colonist bar.

Colonists with a high [mood](/wiki/Mood "Mood") can randomly have **mental inspirations** , giving a stat boost for some time or a special one time benefit. Unlike [mental breaks](/wiki/Mental_break "Mental break"), you retain full control of the mentally inspired colonist. 

## Contents

  * 1 Mechanics
  * 2 Inspirations
    * 2.1 Go frenzy
    * 2.2 Inspired creativity
    * 2.3 Inspired recruitment
    * 2.4 Inspired surgery
    * 2.5 Inspired taming
    * 2.6 Inspired trade
    * 2.7 Shoot frenzy
    * 2.8 Work frenzy
  * 3 Analysis
    * 3.1 Acquiring inspirations
  * 4 Legacy inspirations
    * 4.1 Inspired art
  * 5 Version history



## Mechanics[[edit](/index.php?title=Mental_inspiration&action=edit&section=1 "Edit section: Mechanics")]

Colonists have a chance, dependent on their mood, to have a random mental inspiration. There are 8 different types of inspirations that can occur, chosen at random from all the options for which the affected colonist meets the requirements. Colonists can only have one inspiration at a time. Having an inspiration prevents any others until the current inspiration ends. 

The mean number of days between inspirations is dependent on the current mood of the colonist, and is controlled by the following equation: 

**Inspiration MTB = If**{Current Mood ≥ 50**} Then {** 410 - (400 × (Current Mood/100)**} Else {** 0**}**  
---  
  
Where **Current Mood** is the mood of the colonist in question, expressed as real number between 0 and 100, inclusive. 

Therefore, inspirations cannot occur unless a colonist's mood is above 49%. 

Mood | MTB Inspirations | Graph   
---|---|---  
50% | 210 Days |   
60% | 170 Days   
70% | 130 Days   
80% | 90 Days   
90% | 50 Days   
100% | 10 Days   
  
Some [traits](/wiki/Traits "Traits") prevent certain types of inspirations. Additionally, the pawns with the [Tortured artist](/wiki/Tortured_artist "Tortured artist") trait have a 50% to gain an Inspired Creativity inspiration after a [mental break](/wiki/Mental_break "Mental break") ends, with a possible exception of "Run Wild" mental breaks.[Verify]

The [word of inspiration](/wiki/Word_of_inspiration "Word of inspiration") psycast [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") gives the target an inspiration. This inspiration is selected randomly by the same rules as any other natural inspiration. [Psilocaps](/wiki/Psilocap "Psilocap")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") immediately grant a 2% chance of a random inspiration upon consumption, also following the rules of natural inspiration. 

If an inspiration is available (see below), it gets a probability weight based on corresponding skill passion level: 1 for none or no corresponding skill, 2.5 for minor and 5 for major passion. Inspired creativity weight is only based on artistic skill passion. 

## Inspirations[[edit](/index.php?title=Mental_inspiration&action=edit&section=2 "Edit section: Inspirations")]

### Go frenzy[[edit](/index.php?title=Mental_inspiration&action=edit&section=3 "Edit section: Go frenzy")]

> <NAME> will move faster for the next 8 days.

  * **Base duration:** 8 day
  * **Minimum skill:** None
  * **Incompatible Trait:** [Slowpoke](/wiki/Slowpoke "Slowpoke")



A colonist's great mood lifts them up and improves their [move speed](/wiki/Move_speed "Move speed") by ×140%, applied after additive offsets, for the duration of the inspiration. This does not improve the [Moving](/wiki/Moving "Moving") stat, so [Melee Dodge Chance](/wiki/Melee_Dodge_Chance "Melee Dodge Chance") is not improved by this inspiration. 

### Inspired creativity[[edit](/index.php?title=Mental_inspiration&action=edit&section=4 "Edit section: Inspired creativity")]

> <NAME> The next item, art, or furniture [PAWN_pronoun] creates will be two quality levels higher than it would otherwise be. This even allows the creation of legendary items. The inspiration will end after 8 days, or when the creation is completed.

See also: [Quality](/wiki/Quality "Quality")

  * **Base duration:** 8 days
  * **Minimum skill:** [Artistic](/wiki/Artistic "Artistic") 3 / [Crafting](/wiki/Crafting "Crafting") 3 / [Construction](/wiki/Construction "Construction") 3



A sudden burst of inspiration gives colonist insight on how to make a quality item. The next finished item will be [2 Quality levels higher](/wiki/Quality#Quality_with_Inspired_Creativity "Quality") than it would otherwise be, allowing for the creation of legendary items. The inspiration is only good for the next single object created, after which the inspiration ends. 

### Inspired recruitment[[edit](/index.php?title=Mental_inspiration&action=edit&section=5 "Edit section: Inspired recruitment")]

> <NAME> will successfully recruit the next prisoner regardless of difficulty or resistance. The inspiration will end after 8 days, or when the prisoner is recruited.

  * **Base duration:** 8 days
  * **Minimum skill:** [Social](/wiki/Skills#Social "Skills") 3



A colonist gains insight on how to recruit prisoners into the colony. They will successfully recruit (or [enslave](/wiki/Slavery#Ideology "Slavery")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")) the next prisoner they attempt to recruit, regardless of difficulty or remaining resistance. With multiple prisoners, it is recommended to manually control the warden so that the desired prisoner is recruited. 

The inspiration ends after a prisoner is recruited. 

### Inspired surgery[[edit](/index.php?title=Mental_inspiration&action=edit&section=6 "Edit section: Inspired surgery")]

> The next time <NAME> performs a surgery, [PAWN_possessive] chance of success will be doubled. A small minimum chance of failure still applies. The inspiration will end after 8 days, or when the surgery is performed.

  * **Base duration:** 8 days
  * **Minimum skill:** [Medical](/wiki/Medical "Medical") 3



A colonist becomes more concentrated in surgeries after being inspired, doubling the [Medical Surgery Success Chance](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") stat. **Note** however that the 98% success rate maximum still applies i.e. there will always be a 2% chance of failure. Thus high skill doctors operating in high quality hospitals can receive no benefit from this inspiration, but it can make a great difference for those with lower Medicine skill who are not good surgeons yet. 

The inspiration ends after a surgery is performed, even if the surgery fails. 

### Inspired taming[[edit](/index.php?title=Mental_inspiration&action=edit&section=7 "Edit section: Inspired taming")]

> <NAME> will successfully tame the next animal regardless of difficulty. The inspiration will end after 8 days, or when an animal was tamed.

  * **Base duration:** 8 days
  * **Minimum skill:** [Animals](/wiki/Skills#Animals "Skills") 3



A colonist is inspired to tame an animal. They will successfully tame the next animal regardless of difficulty. They will not be able to tame any animal that they do not have the requisite skill level to tame however. 

The inspiration ends when an animal is tamed. 

Even if no new tamed animals are required, this inspiration can be used to tame and then slaughter large animals, avoiding the penalties to [meat amount](/wiki/Meat_amount "Meat amount") for missing body parts and not carefully slaughtering. This results in at least 50% more meat compared to hunting. 

### Inspired trade[[edit](/index.php?title=Mental_inspiration&action=edit&section=8 "Edit section: Inspired trade")]

> <NAME> will get a significant trade price bonus when closing [PAWN_possessive] next trade deal. The inspiration will expire after 8 days, or when the deal is done.

  * **Base duration:** 8 days
  * **Minimum skill:** [Social](/wiki/Skills#Social "Skills") 3



A colonist is inspired to obtain a great deal. They will get a great 18% boost in [trade prices](/wiki/Trade_Price_Improvement "Trade Price Improvement"), essentially meaning 12 more levels of [Social skill](/wiki/Skills#Social "Skills"). 

After one successful trade deal, the inspiration ends. This includes trading with [Royal Tribute Collectors](/wiki/Empire#Royal_Tribute_Collector "Empire"), despite Trade Price Improvement not providing any benefit for such trades.[Verify]

### Shoot frenzy[[edit](/index.php?title=Mental_inspiration&action=edit&section=9 "Edit section: Shoot frenzy")]

> <NAME> will shoot more accurately for the next 8 days.

  * **Base duration:** 8 days
  * **Minimum skill:** None
  * **Incompatible Trait:** [Brawler](/wiki/Brawler "Brawler"), non-violent



A colonist is inspired to shoot more accurately, gaining +8 [Shooting Accuracy](/wiki/Shooting_Accuracy "Shooting Accuracy"), or the equivalent of +8 Shooting Skill, for the duration. 

### Work frenzy[[edit](/index.php?title=Mental_inspiration&action=edit&section=10 "Edit section: Work frenzy")]

> <NAME> will work faster for the next 8 days.

  * **Base duration:** 8 day
  * **Minimum skill:** None



A colonist suddenly becomes significantly more productive and will have their [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") multiplied by 1.8x, multiplying after considering other bonuses to the stat, for the duration of the inspiration. For a more comprehensive view of how the stat is modified by different effects, see the [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") page. 

Global Work Speed is applied as a multiplier to the following stats: 

  * [Animal Gather Speed](/wiki/Animal_Gather_Speed "Animal Gather Speed")
  * [Butchery Speed](/wiki/Butchery_Speed "Butchery Speed")
  * [Construction Speed](/wiki/Construction_Speed "Construction Speed")
  * [Cooking Speed](/wiki/Cooking_Speed "Cooking Speed")
  * [Deep Drilling Speed](/wiki/Deep_Drilling_Speed "Deep Drilling Speed")
  * [Drug Synthesis Speed](/wiki/Drug_Synthesis_Speed "Drug Synthesis Speed")
  * [Entity Study Rate](/wiki/Entity_Study_Rate "Entity Study Rate")
  * [General Labor Speed](/wiki/General_Labor_Speed "General Labor Speed")
  * [Hacking Speed](/wiki/Hacking_Speed "Hacking Speed")
  * [Mechanoid Shredding Speed](/wiki/Mechanoid_Shredding_Speed "Mechanoid Shredding Speed")
  * [Medical Operation Speed](/wiki/Medical_Operation_Speed "Medical Operation Speed")
  * [Medical Tend Speed](/wiki/Medical_Tend_Speed "Medical Tend Speed")
  * [Mining Speed](/wiki/Mining_Speed "Mining Speed")
  * [Plant Work Speed](/wiki/Plant_Work_Speed "Plant Work Speed")
  * [Pruning Speed](/wiki/Pruning_Speed "Pruning Speed")
  * [Research Speed](/wiki/Research_Speed "Research Speed")
  * [Smelting Speed](/wiki/Smelting_Speed "Smelting Speed")
  * [Smoothing Speed](/wiki/Smoothing_Speed "Smoothing Speed")



## Analysis[[edit](/index.php?title=Mental_inspiration&action=edit&section=11 "Edit section: Analysis")]

Inspirations can be a huge bonus to the colony. They can occur naturally by improving the colony's overall [mood](/wiki/Mood "Mood"), though if you find some of your colonists' moods are running pretty high, that might be a good time to rigorously enforce _more_ recreation for them, to reach 100% mood and the quickest inspirations. 

Because inspirations are chosen based on passions, if deciding to use [word of inspiration](/wiki/Word_of_inspiration "Word of inspiration")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") or [psilocaps](/wiki/Psilocap "Psilocap"),[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") it is wise to choose a colonist who has a passion in the inspiration's skill and few passions/levels in the other inspiration skills. For example, if wanting to obtain inspired taming, a colonist with a burning passion in Animals and no other passions will be more likely to obtain it. 

Inspired creativity is particularly strong. It provides an permanent or near-permanent buff to the colony, creating powerful weapons and armor, [beds](/wiki/Bed "Bed") to reduce sleep time, [sculptures](/wiki/Sculpture "Sculpture") for room boosts, etc. Legendary [quality](/wiki/Quality "Quality") items are difficult to obtain normally but provide massive boosts and are very common with a high skill crafter + inspired creativity. For crafters, it is best used on weapons first, as weapons do not lose durability when held and provide a major impact to combat. Before an inspiration is obtained, big items like [grand sculptures](/wiki/Grand_sculpture "Grand sculpture") can be partially worked on, stopped, and "saved" for when inspired creativity happens. 

### Acquiring inspirations[[edit](/index.php?title=Mental_inspiration&action=edit&section=12 "Edit section: Acquiring inspirations")]

Beyond the [tortured artist](/wiki/Tortured_artist "Tortured artist") trait, [word of inspiration](/wiki/Word_of_inspiration "Word of inspiration"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and the unfarmable [psilocaps](/wiki/Psilocap "Psilocap"),[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") the only way to encourage inspirations is to improve their mood. Having impressive and beautiful rooms will help, as will setting a multi-phasic schedule to improve average comfort and sleep. [Beer](/wiki/Beer "Beer"), [psychite tea](/wiki/Psychite_tea "Psychite tea"), and [smokeleaf](/wiki/Smokeleaf "Smokeleaf") can all be consumed safely and stack with each other. Hard drugs like [yayo](/wiki/Yayo "Yayo") can provide a temporary boost for the duration at the risk of addiction. Romance can potentially help, as weddings provide +40 mood to the pair and +20 mood to everyone present. 

[Tortured artists](/wiki/Tortured_artist "Tortured artist") that are good or passionate at Crafting/Construction are particularly valuable colonists. They can be abused and locked up into a confined, walled-in space; this makes mental breaks likely while reducing the impact of breaks when they do happen. 

Word of inspiration can be spammed if a [kill-focused](/wiki/Kill-focused "Kill-focused") [persona weapon](/wiki/Persona_weapon "Persona weapon")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") is obtained, as kill-focused provides ample psyfocus for killing any pawn, even [chickens](/wiki/Chicken "Chicken") and other colony animals. It is still necessary to wait 8 days for inspirations like shoot frenzy that aren't one-time use. 

## Legacy inspirations[[edit](/index.php?title=Mental_inspiration&action=edit&section=13 "Edit section: Legacy inspirations")]

These no longer exist in the current version of the game. 

### Inspired art[[edit](/index.php?title=Mental_inspiration&action=edit&section=14 "Edit section: Inspired art")]

  * **Base duration:** 8 days   




    **Minimum skill:** Artistic 6

A sudden burst of inspiration gives colonists a great idea for a piece of art, and after it is completed, that piece of art will be 3 levels higher than it would otherwise be. The inspiration is only good for 1 piece of art. Replaced by [Inspired Creativity](/wiki/Mental_inspiration#Inspired_creativity "Mental inspiration") in Beta 19. 

## Version history[[edit](/index.php?title=Mental_inspiration&action=edit&section=15 "Edit section: Version history")]

  * [0.18.1722](/wiki/Version/0.18.1722 "Version/0.18.1722") \- Added with the following inspirations: Work frenzy, Go frenzy, Shoot frenzy, Inspired trade, Inspired recruitment, Inspired surgery, Inspired art. At the time, incapacitation would end the inspiration.
  * Beta 19/ 1.0 - Inspired colonists now get a special icon in the colonist bar
  * 1.1 - "Inspired taming" inspiration added.
  * [1.2.2719](/wiki/Version/1.2.2719 "Version/1.2.2719") \- Fix: Pawn can get random inspirations while not capable of being conscious.
  * [1.6.4850](/wiki/Version/1.6.4850 "Version/1.6.4850") \- Fix: "Inspired recruitment" pawns interacting incorrectly with prisoners with "Reduce will" setting.



* * *

Status levels

[Needs](/wiki/Needs "Needs")
    [Beauty](/wiki/Beauty "Beauty") • [Chemical](/wiki/Chemical_\(Need\) "Chemical \(Need\)") • [Comfort](/wiki/Comfort "Comfort") • [Drug addiction](/wiki/Drug_addiction "Drug addiction") • [Food](/wiki/Saturation "Saturation") • [Indoors](/wiki/Indoors "Indoors") • [Outdoors](/wiki/Outdoors "Outdoors") • [Recreation](/wiki/Recreation "Recreation") • [Rest](/wiki/Rest "Rest") • [Deathrest](/wiki/Deathrest "Deathrest") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Energy](/index.php?title=Energy&action=edit&redlink=1 "Energy \(page does not exist\)") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Kill satiety](/wiki/Kill_satiety "Kill satiety") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Learning](/wiki/Learning "Learning") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Play](/index.php?title=Play&action=edit&redlink=1 "Play \(page does not exist\)") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
Related
    [Hemogen](/wiki/Hemogen "Hemogen") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
Other
    [Mood](/wiki/Mood "Mood") ([Mental break](/wiki/Mental_break "Mental break") • Mental inspiration)
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Mental_inspiration&oldid=182326](https://rimworldwiki.com/index.php?title=Mental_inspiration&oldid=182326)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Characters](/wiki/Category:Characters "Category:Characters")
  * [Status Level](/wiki/Category:Status_Level "Category:Status Level")



Hidden categories: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Mental+inspiration "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Mental+inspiration "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Mental_inspiration "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Mental_inspiration&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Mental_inspiration)
  * [Edit](/index.php?title=Mental_inspiration&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Mental_inspiration&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Mental_inspiration "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Mental_inspiration "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Mental_inspiration&oldid=182326 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Mental_inspiration&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Mental-5Finspiration)



  * This page was last edited on 25 July 2026, at 21:32.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (0,106,126)
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
  *[+2]: Stacking 1 times for a maximum of 2
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
  *[_Ate kibble_]: I had to eat animal kibble. It's like I don't get to be human any more.
  *[Light Radius]: The furthest away a tile can be before it falls below 30% light
  *[16.67 secs]: real-time at 1x speed
  *[−15]: Stacking 1 times for a maximum of -15
  *[_Ate human meat_]: I ate human meat! The world is right, and I am as I should be.
  *[−7]: Stacking 1 times for a maximum of -7
  *[_Ate raw food_]: I had to eat raw food. We should be cooking that kind of food before eating it. We're not animals.
  *[_Ate insect meat_]: I ate some insect meat. So smooth and succulent.
  *[_Ate cooked insect meat_]: I ate a meal that contained insect meat. I could still taste hints of bug-slime!
  *[_Ate nutrient paste meal_]: I had to eat a disgusting, tasteless meal. I know it keeps you alive, but nobody wants to swallow that glop.
