# Injury

From RimWorld Wiki

Jump to navigation Jump to search

|  |  |  | [Basics](/wiki/Basics "Basics") | [Menus](/wiki/Menus "Menus") | [Game Creation](/wiki/Game_Creation "Game Creation") | [Gameplay](/wiki/Gameplay "Gameplay") | **Pawns** | [Plants](/wiki/Plants "Plants") | [Resources](/wiki/Resources "Resources") | [Gear](/wiki/Gear "Gear") | [Mods](/wiki/Mods "Mods")  
---|---|---|---|---|---|---|---|---  
[Pawns Menu](/wiki/Pawns "Pawns") | **Character Properties** | [Character Types](/wiki/Character_Types "Character Types")  
---|---|---  
[Character Properties](/wiki/Characters "Characters") | [Health](/wiki/Health "Health") | [Mood](/wiki/Mood "Mood") | [Needs](/wiki/Needs "Needs") | [Skills](/wiki/Skills "Skills") | [Thoughts](/wiki/Thoughts "Thoughts") | [Traits](/wiki/Traits "Traits") | [Social](/wiki/Social "Social")  
---|---|---|---|---|---|---|---  
[Health](/wiki/Health "Health") | [Body Parts](/wiki/Body_Parts "Body Parts") | [Capacities](/wiki/Capacity "Capacity") | Injury | [Disease](/wiki/Disease "Disease") | [Ailments](/wiki/Ailments "Ailments")  
---|---|---|---|---|---  
  
* * *

This article is about physical damage. For chronic health conditions, see [Ailments](/wiki/Ailments "Ailments"). For treatable illnesses, see [Disease](/wiki/Disease "Disease").

[![Injury preview anim.gif](/images/e/e2/Injury_preview_anim.gif)](/wiki/File:Injury_preview_anim.gif)

**Injuries** are physical damage to a living being. [Humanoids](/wiki/Human "Human"), [animals](/wiki/Animal "Animal"), and [mechanoids](/wiki/Mechanoid "Mechanoid") can sustain injuries from many sources, which each have their own [Damage Type](/wiki/Damage_Types "Damage Types"). 

## Contents

  * 1 Injury types
  * 2 Summary
    * 2.1 Damage
    * 2.2 Pain
    * 2.3 Bleeding
  * 3 Related
    * 3.1 Infection
    * 3.2 Scarring
      * 3.2.1 Scarification (Ritual)
      * 3.2.2 Efficiency loss
      * 3.2.3 Pain
      * 3.2.4 Pre-existing scars
      * 3.2.5 Scarring mechanics in depth
      * 3.2.6 Reducing the odds of scarring
      * 3.2.7 Healing scars
    * 3.3 Trauma savant
  * 4 Healing
    * 4.1 Healing Rate
    * 4.2 Example
  * 5 Medicine
  * 6 Disfigured
  * 7 Trivia



## Injury types[[edit](/index.php?title=Injury&action=edit&section=1 "Edit section: Injury types")]

Main article: [Health Difficulties](/wiki/Health_Difficulties "Health Difficulties")

Different weapons cause different types of injuries. For example, a [mace](/wiki/Mace "Mace") will crush, a [longsword](/wiki/Longsword "Longsword") will cut, and [fire](/wiki/Fire "Fire") will burn. The type of injury impacts the amount of [pain](/wiki/Pain "Pain") it causes, the rate of bleeding, and the chance of [infection](/wiki/Infection "Infection"). 

## Summary[[edit](/index.php?title=Injury&action=edit&section=2 "Edit section: Summary")]

Injuries reduce a body part's health, its efficiency, and causes pain to the pawn. 

### Damage[[edit](/index.php?title=Injury&action=edit&section=3 "Edit section: Damage")]

Every body part has a health value, which is lowered every time it takes damage. When it reaches 0, the part is completely destroyed. 

Any damage will lower a body part's efficiency, proportional to its health remaining. For example, if an arm has 15/30 health, then that arm performs 50% worse. As each arm is responsible for 50% [Manipulation](/wiki/Manipulation "Manipulation"), this results in the pawn having -25% Manipulation until the injury is healed. Some parts, like the torso, are not responsible for any pawn [stat](/wiki/Stat "Stat"), but still take damage and cause pain. 

Some damage can be permanent. See Scarring for more details. 

### Pain[[edit](/index.php?title=Injury&action=edit&section=4 "Edit section: Pain")]

Main article: [Pain](/wiki/Pain "Pain")

The greater the damage, the greater the [pain](/wiki/Pain "Pain"). Pain is equal to `pain = (damage) * [damage_type_factor](/wiki/Health_Difficulties "Health Difficulties")`. Most injuries have a damage type factor of 1.25, or 1.25% pain per 1 HP damage. This is then scaled for the pawn's health, so a [thrumbo](/wiki/Thrumbo "Thrumbo") feels less pain than a human for the same damage attack. 

Pain reduces [Consciousness](/wiki/Consciousness "Consciousness") directly, which reduces most pawn capabilities. It also gives a rapidly increasing [mood](/wiki/Mood "Mood") penalty, unless the pawn is a [masochist](/wiki/Masochist "Masochist") or follows an [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") with the [Pain: Idealized](/wiki/Pain_\(precept\) "Pain \(precept\)") precept. 

Excessive pain causes [pain shock](/wiki/Pain_shock "Pain shock"), the most common way to [down](/wiki/Downed "Downed") pawns in combat, which prevents them from fighting. Most pawns have a [Pain Shock Threshold](/wiki/Pain_Shock_Threshold "Pain Shock Threshold") of 80%. Note that enemies have a chance to immediately die when downed from pain shock, but not from other means, like [blood loss](/wiki/Blood_loss "Blood loss") or [heat stroke](/wiki/Heat_stroke "Heat stroke"). 

[Mechanoids](/wiki/Mechanoid "Mechanoid") are machines, and are immune to pain. In humans, pain can be completely eliminated with a [painstopper](/wiki/Painstopper "Painstopper"), or reduced for a short time with [go-juice](/wiki/Go-juice "Go-juice") or the [Painblock](/wiki/Painblock "Painblock") psycast[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"). 

### Bleeding[[edit](/index.php?title=Injury&action=edit&section=5 "Edit section: Bleeding")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Injury&action=edit). Reason:** _How is blood loss rate calculated from damage?._  
---|---  
  
Bleeding is a common occurrence from certain damage types. While an injury is bleeding, pawns will gain [blood loss](/wiki/Blood_loss "Blood loss"), scaling with the wound and amount of wounds. Total blood loss is listed under whole body, with a tooltip showing the percent and time until death. If blood loss reaches 100%, the pawn will die. Bleeding pawns will also leave [blood](/wiki/Filth#Blood "Filth") on the ground, making the area [dirty](/wiki/Cleanliness "Cleanliness"). 

Bleeding always stops immediately with tending, regardless of the tend quality or medicine used. Higher quality medicine can cover more wounds at once, which can stop a pawn from bleeding out faster. Injuries will also heal on their own, though a lost limb will always continue to bleed until tended to. 

The [coagulator](/wiki/Coagulator "Coagulator") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") implant halves the rate of blood loss, while the [Superclotting](/wiki/Superclotting "Superclotting") gene[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") rapidly tends bleeding wounds. A human carrying the [Coagulate](/wiki/Coagulate "Coagulate") gene[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") or [unnatural healing](/wiki/Unnatural_healing "Unnatural healing")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") ability can also immediately tend all bleeding wounds. 

Amount of bleeding equal to `Bleeding = damage * body_size_factor`%. Body_size_factor for humans shown in the graph below: 

Dependence of bleeding factor on damage for humans   
---  
  
For animals, althrough, these factors may differ, but usually not much. For example, [rat](/wiki/Rat "Rat") with bodysize 0.2 has body_size_factor approximately equal to 20, which is 67% of human's baby with the same size. Between animals this factor also may differ, for example [thrumbo](/wiki/Thrumbo "Thrumbo") has this factor near 2 times lower, than [megasloth](/wiki/Megasloth "Megasloth"). 

Also there are some additional factors. Damaged heart bleeds x5 times more and neck x4 times more than other limbs. Also, if part of body is completely lost, then damage for bleeding calculation equals max hp of bodypart x2. 

## Related[[edit](/index.php?title=Injury&action=edit&section=6 "Edit section: Related")]

### Infection[[edit](/index.php?title=Injury&action=edit&section=7 "Edit section: Infection")]

Main article: [Infection#Mechanics](/wiki/Infection#Mechanics "Infection")

[Infections](/wiki/Infection "Infection") can occur whenever a pawn is hurt by a bite, burn, frostbite, or any damage type that causes bleeding. A completely destroyed body part cannot become infected. Once a pawn recieves these injuries, the game starts a random timer between 15,000 [ticks](/wiki/Time "Time") (4.17 mins) to 45,000 [ticks](/wiki/Time "Time") (12.5 mins), per injury before checking for infection. The chance of infection depends on: 

  * Damage type. Bite, burn or frostbite wounds have a 25% chance, other bleeding wounds have a 10% to infect.
  * Tend quality. The multiplier is 85% at 0% tend quality, linearly decreasing to 5% at 100% tend quality.
  * Location. The higher the [Cleanliness](/wiki/Cleanliness "Cleanliness"), the lower the chance for infection (50% at 0 Cleanliness).



[Animals](/wiki/Animal "Animal") are 20% as likely to receive an infection. [Mechanoids](/wiki/Mechanoid "Mechanoid") can't get diseases. 

### Scarring[[edit](/index.php?title=Injury&action=edit&section=8 "Edit section: Scarring")]

Scars are lasting markers of injuries. When an injury scars, it _permanently_ lowers the health of the scarred body part, reducing its efficiency. A scar may also cause pain. 

#### Scarification (Ritual)[[edit](/index.php?title=Injury&action=edit&section=9 "Edit section: Scarification \(Ritual\)")]

The [pain is virtue](/wiki/Pain_is_virtue "Pain is virtue") [meme](/wiki/Meme "Meme")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") enables scarring via this [ritual](/wiki/Ritual "Ritual"), offering a reliable way of attaining them without risk for combat. Halfway through the ritual, the target will get a random scar of 0.5hp in any of the following [Body Parts](/wiki/Body_Parts "Body Parts"): Torso (~20%), Left Eye (~12.5%), Right Eye (~12.5%), Left Arm (~12.5%), Right Arm (~12.5%), Left Leg (~10%), Right Leg (~10%), Nose (~8%), Head (~2%). This scar will **NOT** affect the body part's efficiency, though will still reduce effective Hitpoints by 0.5 Additionally, the scar will always cause a set amount of pain, being +4% pain (itchy) or +11% pain (aching), with a 75% and 25% chance of occurring, respectively. 

  * Since [consciousness](/wiki/Consciousness "Consciousness") is only affected when [Pain](/wiki/Pain "Pain") is ±15%, this means you can have 1 scar while avoiding this debuff on your [pawns](/wiki/Colonist "Colonist"), though this will still reduce your effective Pain threshold by -4%/-11% when sustaining injuries from combat.
  * For [Ideoligions](/wiki/Ideoligions "Ideoligions") with the precept “Scarification: Minor”, this will permanently improve mood by 4 to any [non-wimp](/wiki/Traits#Wimp "Traits"), [non-masochist pawn](/wiki/Traits#Masochist "Traits"), allowing up to +8 mood when in intense pain, for a relatively _low_ cost.



Note: This ritual will **NOT** work/appear if the ideology has no rank for the [moral guide](/wiki/Roles#Moral_guide "Roles"). 

#### Efficiency loss[[edit](/index.php?title=Injury&action=edit&section=10 "Edit section: Efficiency loss")]

Efficiency is merely the fraction of the HP remaining in a body part. For example, an arm normally has 30 HP. If a scar causes the arm to have only 25 HP, the arm's efficiency will be 25/30 = ~83% efficiency (with rounding errors in RimWorld's displayed numbers). 

#### Pain[[edit](/index.php?title=Injury&action=edit&section=11 "Edit section: Pain")]

When a scar is created, it is randomly assigned a pain category: Painless 50%, Low Pain 20%, Medium Pain 20%, High Pain 10%. The scar will be called "painful" in the High pain category, "aching" in the Medium pain category, and "itchy" in the Low pain category. Pain causes a [Mood](/wiki/Mood "Mood") malus in non-Masochistic pawns. 

#### Pre-existing scars[[edit](/index.php?title=Injury&action=edit&section=12 "Edit section: Pre-existing scars")]

In addition to injury, pawns may start with scars on them. When you hover your mouse over such a scar, there will be no "cause" of the scar in the tooltip. 

#### Scarring mechanics in depth[[edit](/index.php?title=Injury&action=edit&section=13 "Edit section: Scarring mechanics in depth")]

Scars are randomly created at the moment of injury. They are revealed after the wound heals to the scarred HP. The odds of scarring are a function of the number of HP lost from the injury, and whether the body part is "delicate". Eyes are delicate and more likely to scar. Brain damage will always scar. Bruises will never cause a scar. [Artificial body parts](/wiki/Artificial_body_part "Artificial body part") never scar. Bone cracks will very rarely cause a scar (a "permanent crack"). 

Taking an additional blow to a highly injured body part does **not** increase the odds of scarring. Scars are rolled merely as a function of HP lost by a particular injury. 

Injuries causing less than 5 HP of damage have 0% chance of scarring. Injuries causing 5 HP or more damage linearly scale up the odds of scarring, capping at 14 HP or more damage with 2% chance of scarring. The formula for a non-delicate body part: 
    
    
    odds_of_scarring = 2% * clamp( (hp_lost-4)/10, 0, 1)
    

Odds that a new injury becomes a permanent scar (non‑delicate parts): 

Lost HP | Odds of scarring   
---|---  
< 5 HP | 0%   
5 HP | 0.2%   
8 HP | 0.8%   
12 HP | 1.6%   
14 HP | 2.0% (cap reached)   
50 HP | 2.0% (capped)   
  
The severity of the scar is a value between 1 and half of the damage of the injury. If the injury was -10 HP, the worst possible scar would be -5 HP. 

For example, if an arm is reduced to 6/30 HP by a -24 HP gun shot: 

  * It will have a 2% chance of scarring (exceeding the cap of -14 HP of damage).
  * If the injury rolls a scar, the scar will have a severity between 1 HP and 12 HP (half of the -24 HP from the shot).
  * If the scar rolls 7 HP severity, it will be revealed when the arm heals to 23 HP.
  * The scar will also roll a pain category: Painless 50%, Low 20%, Medium 20%, High 10%.



If a body part receives multiple injuries, a scar is independently rolled for each injury. 

There are many myths surrounding scars. Examples of things that **do not** affect the odds of scars forming: 

  * Quickly tending a wound.
  * Tending a wound with Glitterworld medicine.
  * Resting in a Legendary hospital bed in a clean room.



None of these will help. A scar is created at the moment of injury. Once a scar has been rolled, tending or rest will not stop the scar from eventually being revealed. 

#### Reducing the odds of scarring[[edit](/index.php?title=Injury&action=edit&section=14 "Edit section: Reducing the odds of scarring")]

If a body part can't be made bionic, and if a pawn doesn't have the Scarless gene, your only option is maximizing armor strength and coverage with [Apparel](/wiki/Apparel "Apparel"), and to use a skin hardening implant like a [Stoneskin gland](/wiki/Stoneskin_gland "Stoneskin gland"). The less HP that is lost from each injury, the less the chance of scarring. <5 HP lost will have no chance of scarring on non-delicate body parts. 

#### Healing scars[[edit](/index.php?title=Injury&action=edit&section=15 "Edit section: Healing scars")]

Your options to heal a scar in a human: 

  * Replacing the part with a healthy or [artificial body part](/wiki/Artificial_body_part "Artificial body part").
  * [Luciferium](/wiki/Luciferium "Luciferium") and the [Scarless](/wiki/Scarless "Scarless") [gene](/wiki/Gene "Gene")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") heal 1 scar every 15-30 days.
  * A [biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") can remove scars with [Bioregeneration](/wiki/Biosculpter_pod#Bioregeneration "Biosculpter pod"), which costs [![Glitterworld medicine](/images/thumb/c/c6/Glitterworld_medicine.png/16px-Glitterworld_medicine.png)](/wiki/Glitterworld_medicine "Glitterworld medicine") 2 [glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine") and takes time to complete.
  * A [Creepjoiner](/wiki/Creepjoiner "Creepjoiner")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") with the [![UnnaturalHealing.png](/images/thumb/0/07/UnnaturalHealing.png/16px-UnnaturalHealing.png)](/wiki/File:UnnaturalHealing.png)Unnatural healing ability can heal scars.
  * A [healer mech serum](/wiki/Healer_mech_serum "Healer mech serum") can heal scars.
  * The [Chronophagy](/wiki/Chronophagy "Chronophagy")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") ritual will cure 1-2 scars on the ritual's invoker.



Your options to heal a scar in an animal: 

  * A [healer mech serum](/wiki/Healer_mech_serum "Healer mech serum") is an effective, if rare, option.
  * [Creepjoiners](/wiki/Creepjoiner "Creepjoiner")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") with the [![UnnaturalHealing.png](/images/thumb/0/07/UnnaturalHealing.png/16px-UnnaturalHealing.png)](/wiki/File:UnnaturalHealing.png) Unnatural healing ability. Unlike when used on human, it will never trigger a [flesh tentacle](/wiki/Flesh_tentacle "Flesh tentacle") mutation.
  * [Luciferium](/wiki/Luciferium "Luciferium") can be administered, but you'll have to either forevermore micro the animal's treatment, or trust the animal to eat future doses when needed and to not snack on Luciferium too frequently.



### Trauma savant[[edit](/index.php?title=Injury&action=edit&section=16 "Edit section: Trauma savant")]

Main article: [Trauma savant](/wiki/Trauma_savant "Trauma savant")

[![](/images/thumb/3/34/Trauma_savant.png/400px-Trauma_savant.png)](/wiki/File:Trauma_savant.png)

[](/wiki/File:Trauma_savant.png "Enlarge")

Being shot in the brain can cause the trauma savant condition.

If a pawn receives physical damage to the brain, they have a 2 to 12% chance of receiving trauma savant, depending on part damage taken. 12% chance is a maximum value for 10 damage, but since the brain only has 10 hit points, it will be instantly destroyed, so the actual maximum chance of receiving the condition is a little higher than 10% for 9 points of brain damage. This [ailment](/wiki/Ailment "Ailment") causes the following effects: 

  * A ×0% multiplier to [Talking](/wiki/Talking "Talking") and [Hearing](/wiki/Hearing "Hearing"), making the pawn unable to socialize.
  * +50% to [Manipulation](/wiki/Manipulation "Manipulation"), increasing effectiveness in many tasks.
  * Brain scarring no longer has any impact on brain functionality.



Trauma savant can be cured with a [healer mech serum](/wiki/Healer_mech_serum "Healer mech serum"). However, healer mech serum will always cure scars before trauma savant. As this ailment always occurs with a brain scar, you'll need multiple serums, or a serum with another way of curing scars (such as luciferium). 

It can also be cured with a [resurrector mech serum](/wiki/Resurrector_mech_serum "Resurrector mech serum"). If a pawn dies, and their [corpse](/wiki/Corpse "Corpse") doesn't have a head or brain, then using a resurrector serum will restore usual brain function. With the [Ideology DLC](/wiki/Ideology_DLC "Ideology DLC"), you can use the 'extract skull' option to always remove a human corpse's head. In Core RimWorld, you can eat the corpse, though this risks eating the entire corpse. [Subcore ripscanners](/wiki/Subcore_ripscanner "Subcore ripscanner") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") can offer an easy method of frying a brain as well. 

## Healing[[edit](/index.php?title=Injury&action=edit&section=17 "Edit section: Healing")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Injury&action=edit). Reason:** _Verification via C#,[Preach health](/wiki/Preach_health "Preach health"), [Healing enhancer](/wiki/Healing_enhancer "Healing enhancer"), with full math equation showing how the factors stack (both the different stats, which are likely multiplicative with each other, and the individual changes to those stats.._  
---|---  
  
Injured colonists will recover from their wounds over time. [Tending](/wiki/Doctoring "Doctoring") to a wound and resting in bed speeds up recovery. 

### Healing Rate[[edit](/index.php?title=Injury&action=edit&section=18 "Edit section: Healing Rate")]

A pawn's heal rate is the amount of damage the pawn can heal from non-permanent wounds in one day, given in hit points. Every 600 [ticks](/wiki/Time "Time") (10 secs), **_heal rate_ × 0.01** points of damage are healed from a randomly selected (non-permanent) wound. This healing reduces the severity of the injury, until the body part is fully recovered. In the event that a pawn has more than one wound, the selection of which wound heals first is random. 

  
The exact heal rate is determined by first adding together the following bonuses to HP gain: 

  * **Default healing rate:** All pawns have a base heal rate of 8 HP per day. This is multiplied by the health scale of the pawn; so a [caribou](/wiki/Caribou "Caribou") (health scale 200%) will have a base heal rate of 16 HP per day.
  * **[Healing enhancer](/wiki/Healing_enhancer "Healing enhancer")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") :** Adds +4 HP per day.
  * **If the pawn is lying down or in a bed:**
    * +4 HP per day for resting on a [sleeping spot](/wiki/Sleeping_spot "Sleeping spot") or the ground
    * +8 HP per day for resting on a [bed](/wiki/Bed "Bed") / [double bed](/wiki/Double_bed "Double bed") / [bedroll](/wiki/Bedroll "Bedroll") / [double bedroll](/wiki/Double_bedroll "Double bedroll")
    * +14 HP per day for resting on a [hospital bed](/wiki/Hospital_bed "Hospital bed").



It does not matter if the bed is marked for Medical use or not, the bonuses it provides are the same. 

  * **If the wound is tended:** +4 for 0% [tend quality](/wiki/Tend_quality "Tend quality") and +0.08 per percentage of quality, up to +12 at 100% tend quality.



  
Next, multiply the HP gain by the pawn's [Injury Healing Factor](/wiki/Injury_Healing_Factor "Injury Healing Factor") to get the total healing rate. Injury Healing Factor is determined by: 

**Offsets**

Offsets are added before factors. 

  * [Hediffs](/wiki/Hediffs "Hediffs")
    * [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")[Preach health](/wiki/Hediffs#Preach_health "Hediffs")[1]: +25%



  1. ↑ Applied by the [Preach health](/wiki/Preach_health "Preach health") ability available to the [Moral guide](/wiki/Moral_guide "Moral guide") [Role](/wiki/Role "Role")



  
**Factors**

  * [Hediffs](/wiki/Hediffs "Hediffs")
    * [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")[Juggernaut serum](/wiki/Hediffs#Juggernaut_serum "Hediffs"): ×200%


  * [Genes](/wiki/Genes "Genes")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
    * [Slow wound healing](/wiki/Slow_wound_healing "Slow wound healing"): ×50%
    * [Fast wound healing](/wiki/Fast_wound_healing "Fast wound healing"): ×200%
    * [Superfast wound healing](/wiki/Superfast_wound_healing "Superfast wound healing"): ×400%


  * [Injury Healing Factor Stat Parts](/wiki/Injury_Healing_Factor "Injury Healing Factor")
    * [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")[Deathresting](/wiki/Hediffs#Deathresting "Hediffs"): ×500%



Because the effects of Injury Healing Factor on Healing rate are multiplicative, it is possible to achieve a maximum Injury Healing Factor of 5000% when Preach Health, Juggernaut Serum, and Superfast Wound Healing are stacked while actively Deathresting. This allows a pawn to heal as much as 38 * 5000% = 1900 hit points of regeneration per day. 

### Example[[edit](/index.php?title=Injury&action=edit&section=19 "Edit section: Example")]

To put this in perspective, consider a colonist who has taken 20hp of damage to various body parts, given different recovery scenarios: 

  * **Do nothing** : With no tending or rest, they get the base heal rate of **8** , so it will take (20 × 60,000) / 8 = 150,000 ticks (2.5 in-game days) to fully heal.
  * **Basic tend and resting** : With a 40% tend quality (**+7.2**) and rest in a non-hospital bed (**+8**), they'll have a heal rate of 8 + 7.2 + 8 = **23.2** , so it will take 51,724 ticks to heal (approximately 21 in-game hours)
  * **Best quality care** : With 100% tend quality (**+12**) and rest in a hospital bed (**+14**), they'll have a heal rate of 8 + 12 + 14 = **34** , so it will take 35,294 ticks to heal (approximately 14 hours in game)
  * **Best quality care with[Healing enhancer](/wiki/Healing_enhancer "Healing enhancer") [Superfast Wound Healing](/wiki/Genes "Genes"), [Serums](/wiki/Serums "Serums"), and [Preach Health](/wiki/Preach_health "Preach health")**: With a Healing enhancer (**+4**) 100% tend quality (**+12**) and rest in a hospital bed (**+14**), they'll have a heal rate of (8 + 4 + 12 + 14) * ((100% + 25%) * 200% * 400%) = **380** , so it will take 3,157 ticks to heal (approximately 1.5 hours in game)



## Medicine[[edit](/index.php?title=Injury&action=edit&section=20 "Edit section: Medicine")]

Medicine does not _directly_ cause healing, but it increases the average [tend quality](/wiki/Tend_quality "Tend quality"). When a wound is tended, the quality is in part determined by the medicine given: 

Medicine | Potency | Maximum Tend Quality   
---|---|---  
[![Doctor care but no medicine.png](/images/thumb/9/92/Doctor_care_but_no_medicine.png/16px-Doctor_care_but_no_medicine.png)](/wiki/File:Doctor_care_but_no_medicine.png) None | 0.30 | 70%   
[![Herbal medicine](/images/thumb/a/af/Herbal_medicine.png/16px-Herbal_medicine.png)](/wiki/Herbal_medicine "Herbal medicine") [Herbal medicine](/wiki/Herbal_medicine "Herbal medicine") | 0.60 | 70%   
[![Medicine](/images/thumb/7/79/Medicine_industrial_a.png/16px-Medicine_industrial_a.png)](/wiki/Medicine "Medicine") [Medicine](/wiki/Medicine "Medicine") | 1.00 | 100%   
[![Glitterworld medicine](/images/thumb/c/c6/Glitterworld_medicine.png/16px-Glitterworld_medicine.png)](/wiki/Glitterworld_medicine "Glitterworld medicine") [Glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine") | 1.60 | 130%   
  
Each type of medicine has a cap on its tend quality, improving the type available improves outcomes if all other factors are equal. Even so, better medicines are often precious to hold onto and the effectiveness of herbal medicine in a regular [bed](/wiki/Bed "Bed") reaching its 70% maximum can (mostly) suffice. 

While bleeding wounds can be stopped by any quality of treatment, herbal or better medicines can treat multiple small wounds in a single "batch" of tending. For patients with many bleeding wounds where the best treatment is usually "as much as soon as possible", the difference can easily be life or death. 

Medicine is also useful for treating [disease](/wiki/Disease "Disease"), where tend quality is more impactful, and performing [surgery](/wiki/Surgery "Surgery"), which is boosted greatly by medicine. 

## Disfigured[[edit](/index.php?title=Injury&action=edit&section=21 "Edit section: Disfigured")]

[![](/images/thumb/d/de/Disfigured.jpg/400px-Disfigured.jpg)](/wiki/File:Disfigured.jpg)

[](/wiki/File:Disfigured.jpg "Enlarge")

Damage to the nose caused Hairy to become disfigured

Disfigurement is caused by damage or destruction to any beauty related part. These include the nose, eyes, ears, jaw, and, since version [Version/1.3.3101](/wiki/Version/1.3.3101 "Version/1.3.3101"), tongue. Destruction of the parent of any of the previously mentioned parts also cause this malus (ex: a missing jaw also counts as missing a tongue). It adds the "**Disfigured −15**" [opinion](/wiki/Opinion "Opinion") modifier. Disfigurement can be treated by healing/replacing the injured/destroyed body part. Since [Version/1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062"), replacing the parent part also removes this opinion penalty (ex: [Dentures](/wiki/Denture "Denture") and [Bionic jaws](/wiki/Bionic_jaw "Bionic jaw") prevents the penalty from a missing tongue). 

While disfigurement does not have a direct impact on a pawn's [beauty](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)"), it does disable the positive opinion for positive beauty, while stacking with negative beauty. 

Even while Disfigured, the opinion modifier won't apply to pawns that are either: 

  * Blind
  * [Kind](/wiki/Kind "Kind")
  * [Inhumanized](/wiki/Inhumanized "Inhumanized")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")
  * Belongs to an ideoligion[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") with the [Scarification](/wiki/Scarification "Scarification") precept AND the affected part is a scarification.
  * Belongs to an ideoligion[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") with the [Blindsight](/wiki/Blindsight "Blindsight") meme AND the affected part is an eye.



## Trivia[[edit](/index.php?title=Injury&action=edit&section=22 "Edit section: Trivia")]

Brain injuries in Rimworld cause large amounts of pain (20% or higher for a 5 hp wound), which can render a pawn permanently comatose in certain cases. This is a result of the reduction in Consciousness from the pain being added on top of the direct reduction in Consciousness from the brain injury itself due to the reduced part efficiency. However, in real life the human brain has no pain receptors. Despite their perceived location, headaches are usually caused by receptors triggering elsewhere in the head or neck, not by receptors in the brain. Certain types of headaches are due to irritation or swelling in the meninges, which is the membrane enveloping the brain and which _does_ have pain receptors. 

Retrieved from "[https://rimworldwiki.com/index.php?title=Injury&oldid=183496](https://rimworldwiki.com/index.php?title=Injury&oldid=183496)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Health](/wiki/Category:Health "Category:Health")



Hidden category: 

  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Injury "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Injury "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Injury "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Injury "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Injury)
  * [Edit](/index.php?title=Injury&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Injury&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Injury "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Injury "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Injury&oldid=183496 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Injury&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Injury)



  * This page was last edited on 23 August 2026, at 22:09.
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
