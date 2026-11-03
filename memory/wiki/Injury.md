Injury - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Injury

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 

Basics

Menus

Game&#160;Creation

Gameplay

Pawns

Plants

Resources

Gear

Mods

Pawns Menu

Character&#160;Properties

Character&#160;Types

Character&#160;Properties

Health

Mood

Needs

Skills

Thoughts

Traits

Social

Health

Body Parts

Capacities

Injury

Disease

Ailments

This article is about physical damage. For chronic health conditions, see Ailments. For treatable illnesses, see Disease.

Injuries are physical damage to a living being. Humanoids, animals, and mechanoids can sustain injuries from many sources, which each have their own Damage Type.

Contents

- 1 Injury types

- 2 Summary

- 2.1 Damage

- 2.2 Pain

- 2.3 Bleeding

- 3 Related

- 3.1 Infection

- 3.2 Scarring

- 3.2.1 Scarification (Ritual)

- 3.2.2 Efficiency loss

- 3.2.3 Pain

- 3.2.4 Pre-existing scars

- 3.2.5 Scarring mechanics in depth

- 3.2.6 Reducing the odds of scarring

- 3.2.7 Healing scars

- 3.3 Trauma savant

- 4 Healing

- 4.1 Healing Rate

- 4.2 Example

- 5 Medicine

- 6 Disfigured

- 7 Trivia

Injury types[edit]

Main article: Health Difficulties

Different weapons cause different types of injuries. For example, a mace will crush, a longsword will cut, and fire will burn. The type of injury impacts the amount of pain it causes, the rate of bleeding, and the chance of infection.

Summary[edit]

Injuries reduce a body part's health, its efficiency, and causes pain to the pawn.

Damage[edit]

Every body part has a health value, which is lowered every time it takes damage. When it reaches 0, the part is completely destroyed. 

Any damage will lower a body part's efficiency, proportional to its health remaining. For example, if an arm has 15/30 health, then that arm performs 50% worse. As each arm is responsible for 50% Manipulation, this results in the pawn having -25% Manipulation until the injury is healed. Some parts, like the torso, are not responsible for any pawn stat, but still take damage and cause pain.

Some damage can be permanent. See Scarring for more details.

Pain[edit]

Main article: Pain

The greater the damage, the greater the pain. Pain is equal to pain = (damage) * damage_type_factor. Most injuries have a damage type factor of 1.25, or 1.25% pain per 1 HP damage. This is then scaled for the pawn's health, so a thrumbo feels less pain than a human for the same damage attack. 

Pain reduces Consciousness directly, which reduces most pawn capabilities. It also gives a rapidly increasing mood penalty, unless the pawn is a masochist or follows an ideoligion with the Pain: Idealized precept.

Excessive pain causes pain shock, the most common way to down pawns in combat, which prevents them from fighting. Most pawns have a Pain Shock Threshold of 80%. Note that enemies have a chance to immediately die when downed from pain shock, but not from other means, like blood loss or heat stroke. 

Mechanoids are machines, and are immune to pain. In humans, pain can be completely eliminated with a painstopper, or reduced for a short time with go-juice or the Painblock psycast.

Bleeding[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: How is blood loss rate calculated from damage?.

Bleeding is a common occurrence from certain damage types. While an injury is bleeding, pawns will gain blood loss, scaling with the wound and amount of wounds. Total blood loss is listed under whole body, with a tooltip showing the percent and time until death. If blood loss reaches 100%, the pawn will die. Bleeding pawns will also leave blood on the ground, making the area dirty. 

Bleeding always stops immediately with tending, regardless of the tend quality or medicine used. Higher quality medicine can cover more wounds at once, which can stop a pawn from bleeding out faster. Injuries will also heal on their own, though a lost limb will always continue to bleed until tended to.

The coagulator implant halves the rate of blood loss, while the Superclotting gene rapidly tends bleeding wounds. A human carrying the Coagulate gene or unnatural healing ability can also immediately tend all bleeding wounds.

Amount of bleeding equal to Bleeding = damage * body_size_factor%. Body_size_factor for humans shown in the graph below:

Dependence of bleeding factor on damage for humans

 

For animals, althrough, these factors may differ, but usually not much. For example, rat with bodysize 0.2 has body_size_factor approximately equal to 20, which is 67% of human's baby with the same size. Between animals this factor also may differ, for example thrumbo has this factor near 2 times lower, than megasloth.

Also there are some additional factors. Damaged heart bleeds x5 times more and neck x4 times more than other limbs. Also, if part of body is completely lost, then damage for bleeding calculation equals max hp of bodypart x2.

Related[edit]

Infection[edit]

Main article: Infection#Mechanics

Infections can occur whenever a pawn is hurt by a bite, burn, frostbite, or any damage type that causes bleeding. A completely destroyed body part cannot become infected. Once a pawn recieves these injuries, the game starts a random timer between 15,000&#160;ticks (4.17&#160;mins) to 45,000&#160;ticks (12.5&#160;mins), per injury before checking for infection. The chance of infection depends on:

- Damage type. Bite, burn or frostbite wounds have a 25% chance, other bleeding wounds have a 10% to infect.

- Tend quality. The multiplier is 85% at 0% tend quality, linearly decreasing to 5% at 100% tend quality.

- Location. The higher the Cleanliness, the lower the chance for infection (50% at 0 Cleanliness).

Animals are 20% as likely to receive an infection. Mechanoids can't get diseases.

Scarring[edit]

Scars are lasting markers of injuries. When an injury scars, it permanently lowers the health of the scarred body part, reducing its efficiency. A scar may also cause pain.

Scarification (Ritual)[edit]

The pain is virtue meme enables scarring via this ritual, offering a reliable way of attaining them without risk for combat. Halfway through the ritual, the target will get a random scar of 0.5hp in any of the following Body Parts: Torso (~20%), Left Eye (~12.5%), Right Eye (~12.5%), Left Arm (~12.5%), Right Arm (~12.5%), Left Leg (~10%), Right Leg (~10%), Nose (~8%), Head (~2%). This scar will NOT affect the body part's efficiency, though will still reduce effective Hitpoints by 0.5
Additionally, the scar will always cause a set amount of pain, being +4% pain (itchy) or +11% pain (aching), with a 75% and 25% chance of occurring, respectively.

- Since consciousness is only affected when Pain is ±15%, this means you can have 1 scar while avoiding this debuff on your pawns, though this will still reduce your effective Pain threshold by -4%/-11% when sustaining injuries from combat.

- For Ideoligions with the precept “Scarification: Minor”, this will permanently improve mood by 4 to any non-wimp, non-masochist pawn, allowing up to +8 mood when in intense pain, for a relatively low cost.

Note: This ritual will NOT work/appear if the ideology has no rank for the moral guide.

Efficiency loss[edit]

Efficiency is merely the fraction of the HP remaining in a body part. For example, an arm normally has 30 HP. If a scar causes the arm to have only 25 HP, the arm's efficiency will be 25/30 = ~83% efficiency (with rounding errors in RimWorld's displayed numbers).

Pain[edit]

When a scar is created, it is randomly assigned a pain category: Painless 50%, Low Pain 20%, Medium Pain 20%, High Pain 10%. The scar will be called "painful" in the High pain category, "aching" in the Medium pain category, and "itchy" in the Low pain category. Pain causes a Mood malus in non-Masochistic pawns.

Pre-existing scars[edit]

In addition to injury, pawns may start with scars on them. When you hover your mouse over such a scar, there will be no "cause" of the scar in the tooltip.

Scarring mechanics in depth[edit]

Scars are randomly created at the moment of injury. They are revealed after the wound heals to the scarred HP. The odds of scarring are a function of the number of HP lost from the injury, and whether the body part is "delicate". Eyes are delicate and more likely to scar. Brain damage will always scar. Bruises will never cause a scar. Artificial body parts never scar. Bone cracks will very rarely cause a scar (a "permanent crack").

Taking an additional blow to a highly injured body part does not increase the odds of scarring. Scars are rolled merely as a function of HP lost by a particular injury.

Injuries causing less than 5 HP of damage have 0% chance of scarring. Injuries causing 5 HP or more damage linearly scale up the odds of scarring, capping at 14 HP or more damage with 2% chance of scarring. The formula for a non-delicate body part:

odds_of_scarring = 2% * clamp( (hp_lost-4)/10, 0, 1)

Odds that a new injury becomes a permanent scar (non‑delicate parts):

Lost HP
Odds of scarring

< 5 HP
0%

5 HP
0.2%

8 HP
0.8%

12 HP
1.6%

14 HP
2.0% (cap reached)

50 HP
2.0% (capped)

The severity of the scar is a value between 1 and half of the damage of the injury. If the injury was -10 HP, the worst possible scar would be -5 HP.

For example, if an arm is reduced to 6/30 HP by a -24 HP gun shot:

- It will have a 2% chance of scarring (exceeding the cap of -14 HP of damage).

- If the injury rolls a scar, the scar will have a severity between 1 HP and 12 HP (half of the -24 HP from the shot).

- If the scar rolls 7 HP severity, it will be revealed when the arm heals to 23 HP.

- The scar will also roll a pain category: Painless 50%, Low 20%, Medium 20%, High 10%.

If a body part receives multiple injuries, a scar is independently rolled for each injury. 

There are many myths surrounding scars. Examples of things that do not affect the odds of scars forming:

- Quickly tending a wound.

- Tending a wound with Glitterworld medicine.

- Resting in a Legendary hospital bed in a clean room.

None of these will help. A scar is created at the moment of injury. Once a scar has been rolled, tending or rest will not stop the scar from eventually being revealed.

Reducing the odds of scarring[edit]

If a body part can't be made bionic, and if a pawn doesn't have the Scarless gene, your only option is maximizing armor strength and coverage with Apparel, and to use a skin hardening implant like a Stoneskin gland. The less HP that is lost from each injury, the less the chance of scarring. <5 HP lost will have no chance of scarring on non-delicate body parts.

Healing scars[edit]

Your options to heal a scar in a human:

- Replacing the part with a healthy or artificial body part.

- Luciferium and the Scarless gene heal 1 scar every 15-30 days.

- A biosculpter pod can remove scars with Bioregeneration, which costs 2 glitterworld medicine and takes time to complete.

- A Creepjoiner with the Unnatural healing ability can heal scars.

- A healer mech serum can heal scars.

- The Chronophagy ritual will cure 1-2 scars on the ritual's invoker.

Your options to heal a scar in an animal:

- A healer mech serum is an effective, if rare, option.

- Creepjoiners with the Unnatural healing ability. Unlike when used on human, it will never trigger a flesh tentacle mutation.

- Luciferium can be administered, but you'll have to either forevermore micro the animal's treatment, or trust the animal to eat future doses when needed and to not snack on Luciferium too frequently.

Trauma savant[edit]

Main article: Trauma savant

 
Being shot in the brain can cause the trauma savant condition.

If a pawn receives physical damage to the brain, they have a 2 to 12% chance of receiving trauma savant, depending on part damage taken. 12% chance is a maximum value for 10 damage, but since the brain only has 10 hit points, it will be instantly destroyed, so the actual maximum chance of receiving the condition is a little higher than 10% for 9 points of brain damage. This ailment causes the following effects:

- A ×0% multiplier to Talking and Hearing, making the pawn unable to socialize.

- +50% to Manipulation, increasing effectiveness in many tasks.

- Brain scarring no longer has any impact on brain functionality.

Trauma savant can be cured with a healer mech serum. However, healer mech serum will always cure scars before trauma savant. As this ailment always occurs with a brain scar, you'll need multiple serums, or a serum with another way of curing scars (such as luciferium).

It can also be cured with a resurrector mech serum. If a pawn dies, and their corpse doesn't have a head or brain, then using a resurrector serum will restore usual brain function. With the Ideology DLC, you can use the 'extract skull' option to always remove a human corpse's head. In Core RimWorld, you can eat the corpse, though this risks eating the entire corpse. Subcore ripscanners can offer an easy method of frying a brain as well.

Healing[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Verification via C#, Preach health, Healing enhancer, with full math equation showing how the factors stack (both the different stats, which are likely multiplicative with each other, and the individual changes to those stats..

Injured colonists will recover from their wounds over time. Tending to a wound and resting in bed speeds up recovery.

Healing Rate[edit]

A pawn's heal rate is the amount of damage the pawn can heal from non-permanent wounds in one day, given in hit points. Every 600&#160;ticks (10&#160;secs), heal rate &#215; 0.01 points of damage are healed from a randomly selected (non-permanent) wound. This healing reduces the severity of the injury, until the body part is fully recovered. In the event that a pawn has more than one wound, the selection of which wound heals first is random.

The exact heal rate is determined by first adding together the following bonuses to HP gain:

- Default healing rate: All pawns have a base heal rate of 8 HP per day. This is multiplied by the health scale of the pawn; so a caribou (health scale 200%) will have a base heal rate of 16 HP per day.

- Healing enhancer: Adds +4 HP per day.

- If the pawn is lying down or in a bed:
- +4 HP per day for resting on a sleeping spot or the ground

- +8 HP per day for resting on a bed / double bed / bedroll / double bedroll

- +14 HP per day for resting on a hospital bed.

It does not matter if the bed is marked for Medical use or not, the bonuses it provides are the same.

- If the wound is tended: +4 for 0% tend quality and +0.08 per percentage of quality, up to +12 at 100% tend quality.

Next, multiply the HP gain by the pawn's Injury Healing Factor to get the total healing rate. Injury Healing Factor is determined by:

Offsets

Offsets are added before factors.

- Hediffs
- Preach health&#91;1&#93;: +25%

- ↑ Applied by the Preach health ability available to the Moral guide Role

Factors

- Hediffs
- Juggernaut serum: ×200%

- Genes
- Slow wound healing: ×50%

- Fast wound healing: ×200%

- Superfast wound healing: ×400%

- Injury Healing Factor Stat Parts
- Deathresting: ×500%

Because the effects of Injury Healing Factor on Healing rate are multiplicative, it is possible to achieve a maximum Injury Healing Factor of 5000% when Preach Health, Juggernaut Serum, and Superfast Wound Healing are stacked while actively Deathresting. This allows a pawn to heal as much as 38 * 5000% = 1900 hit points of regeneration per day.

Example[edit]

To put this in perspective, consider a colonist who has taken 20hp of damage to various body parts, given different recovery scenarios:

- Do nothing: With no tending or rest, they get the base heal rate of 8, so it will take (20 &#215; 60,000) / 8 = 150,000 ticks (2.5 in-game days) to fully heal.

- Basic tend and resting: With a 40% tend quality (+7.2) and rest in a non-hospital bed (+8), they'll have a heal rate of 8 + 7.2 + 8 = 23.2, so it will take 51,724 ticks to heal (approximately 21 in-game hours)

- Best quality care: With 100% tend quality (+12) and rest in a hospital bed (+14), they'll have a heal rate of 8 + 12 + 14 = 34, so it will take 35,294 ticks to heal (approximately 14 hours in game)

- Best quality care with Healing enhancer Superfast Wound Healing, Serums, and Preach Health: With a Healing enhancer (+4) 100% tend quality (+12) and rest in a hospital bed (+14), they'll have a heal rate of (8 + 4 + 12 + 14) * ((100% + 25%) * 200% * 400%) = 380, so it will take 3,157 ticks to heal (approximately 1.5 hours in game)

Medicine[edit]

Medicine does not directly cause healing, but it increases the average tend quality. When a wound is tended, the quality is in part determined by the medicine given:

Medicine
Potency
Maximum Tend Quality

 None
0.30
70%

 Herbal medicine
0.60
70%

 Medicine
1.00
100%

 Glitterworld medicine
1.60
130%

Each type of medicine has a cap on its tend quality, improving the type available improves outcomes if all other factors are equal. Even so, better medicines are often precious to hold onto and the effectiveness of herbal medicine in a regular bed reaching its 70% maximum can (mostly) suffice.

While bleeding wounds can be stopped by any quality of treatment, herbal or better medicines can treat multiple small wounds in a single "batch" of tending. For patients with many bleeding wounds where the best treatment is usually "as much as soon as possible", the difference can easily be life or death.

Medicine is also useful for treating disease, where tend quality is more impactful, and performing surgery, which is boosted greatly by medicine.

Disfigured[edit]

 
Damage to the nose caused Hairy to become disfigured

Disfigurement is caused by damage or destruction to any beauty related part. These include the nose, eyes, ears, jaw, and, since version Version/1.3.3101, tongue. Destruction of the parent of any of the previously mentioned parts also cause this malus (ex: a missing jaw also counts as missing a tongue). It adds the "Disfigured −15" opinion modifier. Disfigurement can be treated by healing/replacing the injured/destroyed body part. Since Version/1.5.4062, replacing the parent part also removes this opinion penalty (ex: Dentures and Bionic jaws prevents the penalty from a missing tongue).

While disfigurement does not have a direct impact on a pawn's beauty, it does disable the positive opinion for positive beauty, while stacking with negative beauty.

Even while Disfigured, the opinion modifier won't apply to pawns that are either:

- Blind

- Kind

- Inhumanized

- Belongs to an ideoligion with the Scarification precept AND the affected part is a scarification.

- Belongs to an ideoligion with the Blindsight meme AND the affected part is an eye.

Trivia[edit]

Brain injuries in Rimworld cause large amounts of pain (20% or higher for a 5 hp wound), which can render a pawn permanently comatose in certain cases. This is a result of the reduction in Consciousness from the pain being added on top of the direct reduction in Consciousness from the brain injury itself due to the reduced part efficiency. However, in real life the human brain has no pain receptors. Despite their perceived location, headaches are usually caused by receptors triggering elsewhere in the head or neck, not by receptors in the brain. Certain types of headaches are due to irritation or swelling in the meninges, which is the membrane enveloping the brain and which does have pain receptors.

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Injury&oldid=183496"

 Categories: - Stubs
- Health

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

 
 

 

 
 - This page was last edited on 23 August 2026, at 22:09.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -