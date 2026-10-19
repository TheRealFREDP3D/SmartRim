# Infection

From RimWorld Wiki

Jump to navigation Jump to search

## Contents

  * 1 Overview
    * 1.1 Mechanics
    * 1.2 Prevention
  * 2 Progression
    * 2.1 Stages
    * 2.2 Humans & Animals
    * 2.3 Case studies
    * 2.4 Default warning
  * 3 Treatment
    * 3.1 Vulnerable
  * 4 See also
  * 5 Version history



> Bacterial infection in a wound. Without treatment, the bacteria will multiply, killing local tissue, and eventually causing blood poisoning and death. Through aeons of human warfare, infections have often taken more lives than the wounds themselves.
> 
> -- Description

**Infection** is a fast-acting [fatal](/wiki/Death "Death") [disease](/wiki/Disease "Disease") that can be contracted from open [wounds](/wiki/Injuries "Injuries"). 

## Overview[[edit](/index.php?title=Infection&action=edit&section=1 "Edit section: Overview")]

Infections can occur on most wounds. It is the fastest working illness in [RimWorld](/wiki/RimWorld "RimWorld"), taking little more than a day to kill the victim if left [untended](/wiki/Doctoring#Treatment "Doctoring"). [Animals](/wiki/Animals "Animals") can also contract infections, moving just as fast as human infections, although at a reduced chance. 

It is possible to have multiple infections simultaneously across different [body parts](/wiki/Body_parts "Body parts"). Each infection progresses at its own rate, while immunity against infections progresses at the same rate across the whole body. If the patient can become immune before their worst infection reaches 100%, they have beaten _all_ their infections. 

If untreated, the patient loses this race in **less than a day and a half** , so any infection needs to be treated immediately and consistently. A pawn with 100% [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") will become immune in around 1.5 days. 

### Mechanics[[edit](/index.php?title=Infection&action=edit&section=2 "Edit section: Mechanics")]

The chance of a pawn getting an infection depends on the wound type and various other factors: 

  * [Bite](/wiki/Bite "Bite"), [burns](/wiki/Burn "Burn"), and chemical burns have a 30% chance.
  * [Frostbite](/wiki/Frostbite "Frostbite") has a 25% chance.
  * Shredding injuries have a 20% chance.
  * Most other [bleeding](/wiki/Bleeding "Bleeding") wounds have a 15% chance.
  * Neither missing body parts, nor injuries from [blunt](/wiki/Blunt "Blunt") traumas such as bruises and cracks, can become infected.
  * Colonists are more likely to get wound infections at higher [difficulties](/wiki/Difficulty "Difficulty").



Treated wounds can still get infected, at a reduced chance. The multiplier is 85% at 0% [tend quality](/wiki/Tend_quality "Tend quality"), and linearly decreases to 5% at 100% tend quality. Animals have 20% of a colonist's chance to get an infection. Cleaner rooms further reduce the chance of infection. A regular, [floored](/wiki/Floor "Floor") room without any [filth](/wiki/Filth "Filth") has a 50% multiplier, a clean room with [sterile tiles](/wiki/Sterile_tile "Sterile tile") has a 32% multiplier, while caravans and outdoor spaces have the standard 100%. 

When a colonist has an infectable wound, the game will count down randomly from 15,000 [ticks](/wiki/Time "Time") (4.17 mins) to 45,000 [ticks](/wiki/Time "Time") (12.5 mins). The game will also keep track of if the wound was tended, and, if so, what percent chance of an infection would arise from the room stats and the tend quality. Once it reaches this timer, it will decide if the wound will be infected, based on that percent chance. Once an infection sets in, it _immediately_ becomes a life-or-[death](/wiki/Death "Death") race between the infection rates vs. the patient's immunity progression; the first to a value of 1.00 (100%) "wins". 

### Prevention[[edit](/index.php?title=Infection&action=edit&section=3 "Edit section: Prevention")]

The [perfect immunity](/wiki/Perfect_immunity "Perfect immunity") gene[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") will prevent the acquisition of this disease but will not cure pre-existing conditions present at the time of implantation. However, creating a [xenogerm](/wiki/Xenogerm "Xenogerm") with it requires an [archite capsule](/wiki/Archite_capsule "Archite capsule"), so modifying every pawn with it is expensive. For pawns without the gene, the chances of infection can be greatly reduced by making sure to tend quickly, in a clean/sterile environment. Any constructed [floor](/wiki/Floors "Floors") is better than dirt, and [sterile tiles](/wiki/Sterile_tile "Sterile tile") are better than generic floors. You should also have pawns [clean](/wiki/Orders#Clean "Orders") the room in question. See [cleanliness](/wiki/Cleanliness "Cleanliness") for more details. 

A triage area can be established near a killbox to tend to pawns quickly without having to trudge halfway across the map carrying the pawn to tend - the utility of this depends on the distance to a hospital and the number of pawns needing treatment. More pawns and larger distance make it more relevant, while a single pawn getting downed in the room next to the hospital would be better off taken to the clean room. 

## Progression[[edit](/index.php?title=Infection&action=edit&section=4 "Edit section: Progression")]

Infection and immunity progression begin as soon as the disease is detected; the first to 100% (1.0 severity) "wins", either saving or killing the pawn. The current status of both progressions can be viewed in the sick colonist's Health tab by mouse-hovering over the word "Infection". Unfortunately, the disease progresses faster without good treatment and rest. 

Note that the immunity only applies to the current infection, not future infections. Any new infection will cause the process to begin again from scratch. 

### Stages[[edit](/index.php?title=Infection&action=edit&section=5 "Edit section: Stages")]

Stage | Severity | Symptoms   
---|---|---  
**Infection (minor)** | 0% - 32% | 

  * [Pain](/wiki/Pain "Pain"): +5%

  
**Infection (major)** | 33% - 77% | 

  * [Pain](/wiki/Pain "Pain"): +8%

  
**Infection (Extreme)** | 78% - 86% | 

  * [Pain](/wiki/Pain "Pain"): +12%
  * [Consciousness](/wiki/Consciousness "Consciousness"): −5%

  
**Infection (Extreme)** | 87% - 99% | 

  * [Consciousness](/wiki/Consciousness "Consciousness"): Max 10% (Unconsciousness)
  * [Pain](/wiki/Pain "Pain"): +85%
  * [Breathing](/wiki/Breathing "Breathing"): −5%

  
**Infection (Extreme)** | 100% | 

  * [Death](/wiki/Death "Death")

  
  
### Humans & Animals[[edit](/index.php?title=Infection&action=edit&section=6 "Edit section: Humans & Animals")]

  * When not immune or treated, severity increases by +0.84 per day (+0.035 per hour).
  * Treatment slows progression by a maximum of −0.53 per day (less with poor treatment). 
    * At 100% treatment, the disease will progress by +0.31 per day.
  * When immune, severity decreases by −0.7 per day.
  * Immunity increases by +0.6441 per day when sick.



This means that an infection can kill less than 1.19 days from first symptoms. A pawn with 100% [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") will become immune in 1.55 days on average - meaning that they will die without treatment slowing severity gain or improving IGS to at least 130.4%. Note that this ignores the effect of InfectionLuck. For a full breakdown on [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") and the factors that affect it, see that page. 

### Case studies[[edit](/index.php?title=Infection&action=edit&section=7 "Edit section: Case studies")]

  * It has been observed in patients with normal beds, a room with "slightly dirty" to "dirty" [cleanliness](/wiki/Cleanliness "Cleanliness"), well nourished, [Medical](/wiki/Medical "Medical") care with skill ~6-10 and only herbal medicine (Tend quality ~40-50), will recover from their infections, even despite some few hours delay in starting treatment. It sometimes is a near thing, and may result in a longer recovery time from an end infection near/over 90% when they reach immunity, depending on the delay, their feeding schedule and the "luck" of the attending doctor. Malnutrition (from hunger) definitely slows the immunity process, as listed under [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed").


  * It has also been observed that a prisoner in good health (age < 50, no health issues), well fed, in an excellent-quality [hospital bed](/wiki/Hospital_bed "Hospital bed") with a [vitals monitor](/wiki/Vitals_monitor "Vitals monitor"), and a Tend quality of 99% (high Medical skill using [glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine")), gained Immunity more than 2:1 over Infection gain (from a 68 Immunity and 83 Infection, +32 v. +15). That's not a "maximum", but it may be close to a reasonably practical one, just as a benchmark.



All this math also means that it will take a patient almost 3 days, or more, to go through the process of first fighting and then recovering from an infection, besides recovering from whatever wound or ailment caused the infection in the first place. Yet another reason to provide prompt, sterile treatment for all colonists' wounds to avoid this in the first place. 

### Default warning[[edit](/index.php?title=Infection&action=edit&section=8 "Edit section: Default warning")]

Toward the end of a bad infection, once the infection becomes "extreme" (80% or more), you will get a bright red warning among the other notices on the right side of the screen saying: 

    "**Medical emergency** People are at risk for [death](/wiki/Death "Death") because of severe illness..."

This alert appears regardless of whether that colonist is currently beating the infection or not, or will do so - the game doesn't do the math to predict whether the infection or the immunity will reach 100% first, but you should be able to. The warning is simply there to remind you that now may be the time to take drastic action, just in case you are losing the race. The notice will disappear when immunity reaches 100% (regardless of the current level of infection), or when the victim dies. 

## Treatment[[edit](/index.php?title=Infection&action=edit&section=9 "Edit section: Treatment")]

Prevention is the best treatment - a capable doctor and clean environment for treatment are critical to avoiding this deadly ailment before it happens. Even after successful treatment of a bad infection there can be a fairly lengthy recovery time, so prevention really _is_ the best medicine in this case. 

If left untreated, infections kill in a little over a day - untreated infections move _fast!_ For resting colonists with 100% immunity gain speed and immediate treatment, you will need at least 15% average treatment quality to ensure that one doesn't succumb to their infected wound(s). 

As with any other disease, make sure that the patient is rested, well-fed, and treated whenever possible. A single infection will take multiple treatments, administered once every 12 hours, per infection. Infections progress very quickly, and missing or delaying a treatment can be a _very_ costly mistake. Due to the rate at which infections progress, you'll want at least a competent doctor using [herbal medicine](/wiki/Herbal_medicine "Herbal medicine") or better in order to ensure that the affected person survives an infection. 

Once you beat the infection, that value then begins to (slowly) drop back to "0", from where ever it was; no further treatment is necessary once this starts. However, better treatment quality results will stop the infection before it progresses to a higher value, saving recovery time for the patient, so the more bonuses you can scrape together* during treatment, the faster the recovery. 

    (* better Medical skill, better medicine, a [clean room](/wiki/Rooms#Cleanliness "Rooms"), a higher quality [bed](/wiki/Bed#Surgery_Success_Chance_Factor "Bed"), upgrading to a [hospital bed](/wiki/Hospital_bed "Hospital bed"), adding a connected [vitals monitor](/wiki/Vitals_monitor "Vitals monitor"), etc. See [Doctoring](/wiki/Doctoring#Treatment "Doctoring") for more details.)

This disease is unique in that it only affects a specific, isolated body part, making infections curable by removing that part. It is not possible to amputate vital organs, though some can be replaced with [artificial versions](/wiki/Artificial_body_parts#Body "Artificial body parts"). It's (usually) better to have a colonist missing a part or two than to lose the colonist entirely, and there is no [mood](/wiki/Mood "Mood") debuff if you remove an infected part. If the infection has progressed to over 97%, there is little to no chance your surgeons can successfully pull off an amputation in time, so plan accordingly. As with any operation, amputations (and organ replacements) can fail, leaving the infected part attached, so if you make the decision to do this, try to operate before 90% or earlier so you have time to try again. 

    

  * To amputate: Under the patient's Health tab is the Operations tab; "Add a bill" to amputate the infected body part. You may also have to/want to upgrade the patient's default "medicine" used for procedures - that's under their Health/Overview tab. If an arm/leg/kidney is the target, make sure to amputate the _correct_ (left/right) part - surgeons just do what they're told.



### Vulnerable[[edit](/index.php?title=Infection&action=edit&section=10 "Edit section: Vulnerable")]

For those with a base immunity gain rate of 39% or less, it will be very difficult to survive infection. This includes people well past their [Life Expectancy](/wiki/Immunity_Gain_Speed#Age "Immunity Gain Speed"), and/or people with severe kidney and liver damage. Even with 100% [treatment quality](/wiki/Doctoring#Tend_quality "Doctoring") for all treatments and rest in a [hospital bed](/wiki/Hospital_bed "Hospital bed") with a [vitals monitor](/wiki/Vitals_monitor "Vitals monitor") connected, they will die without extra care. To save the colonist, you can do one or more of the following: 

  * Amputate the affected limb if possible. This will leave your colonist without a limb but it instantly cures the infection.
  * Tend with [glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine")
  * Administer [healer mech serum](/wiki/Healer_mech_serum "Healer mech serum") \- instantly treats the disease
  * Use the [medic cycle](/wiki/Medic_cycle "Medic cycle") of a [Biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") curing the infection completely after the cycle finishes.
  * Administer [luciferium](/wiki/Luciferium "Luciferium")
  * Perform an [organ transplant](/wiki/Health#Transplants "Health") for pawns with damage to their [liver](/wiki/Liver "Liver") or [kidneys](/wiki/Kidney "Kidney").
  * Install up to two [immunoenhancers](/wiki/Immunoenhancer "Immunoenhancer") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") for 8% per enhancer installed. Note that these require a kidney to be present for them to be installed into, so a transplant might be required if they are missing. Damaged kidneys are sufficient however.
  * Install [detoxifier kidneys](/wiki/Detoxifier_kidney "Detoxifier kidney"). these improve immunity gain speed by 2.5% each. Prioritize installing detoxifier kidneys on already damaged kidneys.
  * Use the [preach health](/wiki/Preach_health "Preach health")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") ability on the affected person
  * Use the [medical specialist](/wiki/Medical_specialist "Medical specialist")'s[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") immunity drive
  * Place the patient in a [cryptosleep casket](/wiki/Cryptosleep_casket "Cryptosleep casket") until you have one of the above.



## See also[[edit](/index.php?title=Infection&action=edit&section=11 "Edit section: See also")]

  * [Scaria infection](/wiki/Scaria_infection "Scaria infection") \- uses the same mechanics as regular infections, but with less symptoms, and causing [scaria](/wiki/Scaria "Scaria") instead of death.



## Version history[[edit](/index.php?title=Infection&action=edit&section=12 "Edit section: Version history")]

  * [0.7.581](/wiki/Version/0.7.581 "Version/0.7.581") \- Added.
  * [1.0.0](/wiki/Version/1.0.0 "Version/1.0.0") \- Reduced various infection chances (around 25%). Animal infection chance factor 0.20 -> 0.10.



At around Beta 18 infections caused a reduction in part efficiency, allowing them to kill much earlier than usual if a critically injured vital body part is infected and the infection causes the efficiency of that body part to drop below zero. 

  


* * *

[Disease](/wiki/Disease "Disease")

Deadly diseases
    [Flu](/wiki/Flu "Flu") • Infection • [Lung rot](/wiki/Lung_rot "Lung rot") • [Malaria](/wiki/Malaria "Malaria") • [Plague](/wiki/Plague "Plague") • [Sleeping sickness](/wiki/Sleeping_sickness "Sleeping sickness") • [Organ decay](/wiki/Organ_decay "Organ decay") • [Blood rot](/wiki/Blood_rot "Blood rot") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Infant illness](/wiki/Infant_illness "Infant illness")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Non-fatal diseases
    [Fibrous mechanites](/wiki/Fibrous_mechanites "Fibrous mechanites") • [Gut worms](/wiki/Gut_worms "Gut worms") • [Muscle parasites](/wiki/Muscle_parasites "Muscle parasites") • [Sensory mechanites](/wiki/Sensory_mechanites "Sensory mechanites") • [Paralytic abasia](/wiki/Paralytic_abasia "Paralytic abasia") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

Animal diseases
    [Scaria](/wiki/Scaria "Scaria")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Infection&oldid=183215](https://rimworldwiki.com/index.php?title=Infection&oldid=183215)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [Disease](/wiki/Category:Disease "Category:Disease")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Infection "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Infection "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Infection "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Infection "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Infection)
  * [Edit](/index.php?title=Infection&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Infection&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Infection "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Infection "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Infection&oldid=183215 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Infection&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Infection)



  * This page was last edited on 20 August 2026, at 04:04.
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
