Genes - RimWorld Wiki
 
 
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
- 
 

 
 

 
 

 

 Genes

 
 From RimWorld Wiki

 (Redirected from Robust)

 

 
 

 Jump to navigation
 Jump to search
 

This article relates to content added by Biotech (DLC). Please note that it will not be present without the DLC enabled.

This page has been suggested for recoding. Reason: Thought templates. You can help RimWorld Wiki by improving it.

This page is a list of genes. For a full explanation of the gene system see: Genetics

Genes are a system for modifying human pawns, added by the Biotech DLC. They can be obtained from character creation or implanted via xenogerms.

Contents

- 1 Mechanics

- 2 Gene expression

- 3 Work Required

- 4 Archite

- 5 Special abilities

- 6 Hemogen

- 7 Health

- 8 Psychics

- 9 Movement

- 10 Mood

- 11 Temperature

- 12 Resistance and sensitivity

- 13 Violence

- 14 Sleep

- 15 Pain

- 16 Reproduction

- 17 Beauty

- 18 Cosmetic

- 18.1 Body type

- 18.2 Hair

- 18.3 Melanin

- 18.4 Skin

- 19 Miscellaneous

- 20 Aptitudes

- 21 Drugs

- 22 Removed genes

- 23 Notes

- 24 Version history

Mechanics[edit]

Genetics are limited by metabolic efficiency, denoted by the symbol. This affects pawns' hunger rate. Harmful genes improve metabolic efficiency, lowering hunger rate, and thus consuming less food overall. Helpful genes lower metabolic efficiency, getting hungry faster. A baseline human has a metabolic efficiency of 0 (100% hunger rate), and genes can bring it as low as -5 (225% hunger rate) or up to 5 (50% hunger rate). The game will not allow the creation of xenogerms with a metabolic efficiency lower than -5.

Note that genes with over 5 cannot be extracted by themselves, and must be extracted in a pack with another gene that lowers metabolism cost.

Complexity, denoted by the symbol, affects how many gene processors you need to create a xenogerm from a set of genes. A gene assembler can create xenogerms with a maximum complexity of 6, plus 2 for every attached gene processor. Complexity also determines the base time it takes to create the xenogerm, ranging from 4 hours at ≤3 complexity, to 23 hours at ≥20 complexity (which is then scaled by the research speed of whoever operates the gene assembler).

Gene expression[edit]

When looking at a pawn's gene tab, each gene can be considered to be in one of three categories:

- Germline Genes

- Xenogenes

- Archite genes

Germline genes are freely distributed through and only through reproduction. Xenogenes are genes that have been surgically implanted through a xenogerm, and can override germline genes that are identical to or conflict with the xenogene; a Dirtmole that was converted into a Sanguophage will have half of their genes overwritten by the Sanguophage xenotype. Xenogerms cannot be passed through reproduction. 

Note that germline and xenogenes are determined by the way they are obtained, not by the effects of the gene itself. For example, there is only one fire resistant gene coded into the game - "germline fire resistant" and "xenogene fire resistant" are the same gene obtained in different ways. Trying to have both would simply disable the redundant germline version.

Archite genes are non-inheritable (even if they are forced into the germline of a custom xenotype) and xenogerms containing them must be supplied with the requested number of archite capsules before being assembled. Archite genes cannot extracted through the gene extractor, but can be implanted using the gene implanter ability.

Work Required[edit]

The work required to create a xenogerm is determined by its . First, a base value is obtained from the post-process curve with the points:

Xenogerm work

- (0, 3)

- (4, 5)

- (8, 8)

- (12, 12)

- (16, 17)

- (20, 23)

 

This value is then multiplied by 2500 to obtain the final number.

Xenogerm work

- (0, 7500)

- (4, 12500)

- (8, 20000)

- (12, 30000)

- (16, 42500)

- (20, 57500)

- 

The actual time required is inversely proportional with the research speed of whoever operates the gene assembler. At 100% research speed, it takes between 7,500&#160;ticks (2.08&#160;mins) (for 0 complexity) to 57,500&#160;ticks (15.97&#160;mins) (for complexity 20 and above).

Archite[edit]

- 
Click to 

Name

Description

Exclude

Scarless

Carriers of this gene have a special type of regenerator cell which can heal old wounds and chronic illnesses like bad back.

- Prevents new scars from forming, even from brain damage.

- Heals 1 scar, permanent injury, or chronic condition (Alzheimer's, asthma, bad back, cataracts, carcinoma, dementia, frail, hearing loss, blindness, and organ decay) every 15-30 days, akin to (and alongside) luciferium. Includes scars from a scarification ritual.
- Will not automatically heal trauma savant conditions.

0

4

1

-

Gene implanter

Carriers of this gene can implant a copy of their xenogerm into another person through a somewhat gross-looking injector organ. Their own genetic material will then regrow very slowly. If they implant while their genes are regrowing, they will die. 

- Adds ability: Implant Genes

Implant this person's xenogenes into a willing subject using a special injector organ. If this person's genes are currently regrowing, they will implant their xenogerm and die in the process. When implanted, a xenogerm will overwrite the target's xenogenes. Germline genes will be unaffected.
- Passes on a copy of all xenogenes to a target. Both pawns will start regrowing genes for a period of around 2 years. The pawn that implants the genes will suffer gene loss shock for 2 days as well. The pawn receiving the xenogerm will be put into xenogermination coma for a flat 2 days.

- Using this ability while genes are regrowing will kill the caster and remove all of their xenogenes.

- Cannot target a hostile pawn unless they are downed.

- Cannot target members of a temporary faction, even if they are downed. This can be worked-around by imprisoning the pawn then enslaving or recruiting them, which changes their faction.

- The caster must have xenogenes, and the target must be of a different xenotype.

- If the target's ideoligion includes one or more xenotype preferences, the caster's xenotype must match one of target's preferred types. This restriction applies even if the target is downed, enslaved or imprisoned.

- If the caster has the bloodfeeder gene, they cannot target a pawn whose ideoligion includes the Bloodfeeders: Reviled precept. This restriction applies even if the target is downed.

0

3

1

-

Perfect immunity

Carriers of this gene have archite-enhanced immune systems which intelligently destroy invaders. They are totally immune to most normal illnesses.

- Immunity to flu, malaria, sleeping sickness, plague, infection, lung rot, gut worms, muscle parasites, and organ decay. This includes all the diseases that are fatal and that adult colonists can acquire.
- Despite the description, it only prevents new illnesses. It does not affect pre-existing conditions nor boost Immunity Gain Speed.

- Note: Does not prevent food poisoning.

0

3

1

Immunity

Non-senescent

Carriers of this gene do not go through senescence in the normal way. They never get chronic age-related diseases like cancer, bad back, cataracts, or dementia.

- Total immunity to carcinoma, heart attack, and chronic conditions (Alzheimer's, Asthma, Artery blockage, Bad back, Cataracts, Dementia, Frail, but not Hearing loss).
- Prevents these conditions from any source, not just aging. (e.g. nuclear stomach, toxic buildup)

- Does not affect pre-existing conditions.

 0

3

1

-

Ageless

Carriers of this gene have archites in the bloodstream which continuously reverse the process of aging. Starting at the age of 13, carriers begin to biologically age slower. By 18, the aging process stops completely.

- Aging ×1 at age 13 or lower. Rate linearly slows as the pawn gets older.

- Aging ×0 at age 18.5 or higher.

0

3

1

-

Deathless

Carriers of this gene have archites in the blood which will sustain their life processes no matter what. As long as the brain remains intact, a carrier of this gene will never die.

- If a pawn would've died, but the brain, head, or neck is not directly destroyed, they enter into either a regenerative coma or involuntary deathrest.
- Pawns without the Deathrest gene enter a regenerative coma. After all fatal conditions are removed, the regenerative coma lasts for 7 more days. Hemogen is unaffected.

- Pawns with the Deathrest gene enter involuntary deathrest and lose all Hemogen. After fatal conditions are removed, the usual deathrest mechanics take place.

- Does not regenerate limbs or organs, except for the torso.

- Entering the regeneration coma or involuntary deathrest will cause the pawn to lose 3% to 6% of total skill XP in a random skill.

- Market value of genepacks containing this gene: ×200% (also multiplied by the usual ×400% for 1 Archite capsule)

0

7

1

-

Archite metabolism

Carriers of this gene have special archites in their cells that facilitate and optimize metabolism. This improves overall genetic and metabolic quality.

- Increases metabolic efficiency by 6. No other effect.

- Market value of genepacks containing this gene: ×150% (also multiplied by ×700% for 2 Archite capsules)

+6

6

2

-

Breathless

Carriers of this gene can store concentrated oxygen in their bodies. Their cells consume much less oxygen, meaning they rarely need to breathe. These adaptations make them immune to the harmful effects of space, as well as environmental toxins, tox gas, acidic smog, and rot stink.

- Vacuum resistance: +100%

- Toxic Environment Resistance: +100%

- Immunity to vacuum burns, tox gas, acidic smog, and rot stink.

- Minimum Comfortable Temperature: −5&#160;°C (9&#160;°F)

0

3

1

ToxicEnvironmentResistance
VacuumResistance

Special abilities[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Acid spray has AP and its own Damage type etc. Further mechanical detail including how it works, what armor it opposes etc is needed.

- 
Click to 

Name

Description

Fire spew

Carriers are able to spew flammable bile generated by a special organ in their neck. The bile sticks to anything in a small area and can ignite people, objects, and the ground.

- Adds ability: Fire spew

Spit a stream of sticky, flammable bile from the mouth. The bile can ignite anything or anyone it hits, and also form flaming pools on the ground. The bile is generated and stored by an organ in the neck, along with a separate pouch of hypergolic reactant for ignition.
- Spits flammable liquid in a 7.9 tile triangle with a 3 tile wide end.[Detail Needed]

- Target: Pawn or Location

- Warmup Time: 60&#160;ticks (1&#160;sec)

- Cooldown: 300,000&#160;ticks (5&#160;in-game days)

- Charges: 1

- AI Can Use: True. Note: AI will still target fire-immune targets.

- Market value of genepacks containing this gene: ×150%

−2

1

Foam spray

Carriers grow glands in the neck that generate and store a fire-retardant foam. They can spew this foam over an area to extinguish fires.

- Adds ability: Foam spray

Spray thick fire-retardant foam from glands in the neck up through the mouth. The foam will cover a small area and extinguish any fire it touches.
- Spits firefoam in a 3x3 area around the target, up to 4 tiles away. This leaves firefoam filth on the ground, extinguishing fires and preventing new ones from igniting.

- Target: Pawn or Location

- Warmup Time: 60&#160;ticks (1&#160;sec)

- Cooldown: 30,000&#160;ticks (12&#160;in-game hours) for all 3 charges. Cooldown will not begin until all charges have been expended.

- Charges: 3

- AI Can Use: False.

−2

1

-

Animal warcall

Carriers of this gene can perform an animal warcall, using a powerful bellow and psychic connection to call an animal to fight for them.

- Adds ability: Animal warcall

With a powerful bellow and psychic connection, call an animal to fight your enemies for a few hours.
- Turns the target berserk against all factions hostile to the caster for 12 in-game hours/30,000&#160;ticks (8.33&#160;mins). -75 base goodwill when used on a friendly faction's animal.

- Target: Any single animal or wildman. Does not require LoS [Detail]

- Range: 49.9 tiles

- Warmup Time: 120&#160;ticks (2&#160;secs)

- Cooldown: 900,000&#160;ticks (15&#160;in-game days) per charge.

- Charges: 2

- AI Can Use: True

−3

1

Acid spray

Carriers grow glands in the neck that generate and store a sticky acid substance, along with acid-tolerant tissues in the mouth. They can spew this acid over an area, where it will stick to enemies and burn them.

- Adds ability: Acid spray

Spray a sticky acid substance from glands in the neck up through the mouth and all over the target area. The acid will stick to targets and burn them.
- Spits a fast-moving acid projectile in a 3x3 area around the target. This does 30 damage to buildings and items, and creates a harmless "spent acid" filth on each affected tile. Creatures in the affected area suffer a 30 damage burn (possibly spread over multiple body parts), but suffer no persistent damage over time. The attack has an AP of 80%[Armor type?] and a stopping power of 1.

- Target: Pawn or Location

- Range: 8.9 tiles

- Warmup Time: 30&#160;ticks (0.5&#160;secs)

- Cooldown: 30,000&#160;ticks (12&#160;in-game hours)

- Charges: 1

- AI Can Use: True.

- Market value of genepacks containing this gene: ×150%

−2

1

-

Hemogen[edit]

- 
Click to 

Name

Description

Prereq.

Hemogenic

Carriers of this gene have a reserve of biological strength powered by a resource called hemogen. The resource can be gained and spent in various ways, all of which are unlocked by other genes. Carriers lose 2 hemogen per day from biological entropy.

- Creates a Hemogen need, which decreases by −2 per day.
- Increases by +20 per hemogen pack or Bloodfeed.

- Receive Hemogen Craving ailment when Hemogen hits 0. 
Craving severity increases by 5% / hour with 0 hemogen. Severity decreases by 10% / hour with it.
- Hemogen Craving (minor, 0%): −10 mood, Consciousness max 90%, +5% Pain

- Hemogen Craving (moderate, 35%): −15 mood, Consciousness max 80%, +10% Pain

- Hemogen Craving (major, 70%): −20 mood, Consciousness max 50%, +15% Pain

+1

1

-

Hemogen drain

Carriers lose an additional 8 hemogen per day from biological entropy.

- −8 Hemogen per day.

+6

1

Hemogenic

Coagulate

Carriers of this gene have special glands on their hands and wrists, as well as a unique salivary compound that they can use to rapidly tend wounds.

- Adds ability: Coagulate

Use special glands in the wrists to quickly tend someone's wounds.
- Tends wounds at 40-80% tend quality.

- Target: Single target in LoS

- Range: 3.9 tiles

- Warmup Time: 60&#160;ticks (1&#160;sec)

- Hemogen Cost: 20

- AI Can Use:&#160;?

−1

1

Hemogenic

Bloodfeeder

Carriers of this gene have small retractable fangs and an organ on the roof of the mouth which can extract hemogen from fresh warm blood. They can bite an unresisting person, suck the blood, and gain hemogen directly.

- Adds ability: Bloodfeed

Bite the target and extract hemogen directly from their blood. The target will lose blood and will be horrified by the interaction, but will be otherwise unharmed. A fast-acting coagulant will seal the wound to prevent bleeding. Can only target non-hemogenic humans. Hemogen gain is affected by the target’s body size.
- Feed on a pawn to gain up to +20 Hemogen, which scales with target body size, but not the user's.
- Target will gain +45% blood loss and the −5 Fed on moodlet (5 days, doesn't stack, negated by masochist trait and Bloodfeeders precept.). Also gains a bloodfeeder mark on the neck (+1% pain).

- If the target does not have enough blood, hemogen gain will be reduced accordingly.[Detail]

- Bloodfeeder must have a non-0% Eating capacity.

- Target: Single human target. Target must not have the Bloodfeeder gene. Must be downed or a colonist, slave, or prisoner not on a mental break.
- A warning will be given if it would kill the target or render them unconscious, but it will not account for continuing blood loss.

- +2 mood when near a blood torch.

- Interaction with Bloodfeeders precept.
- Bloodfeeders: Revered - Believers have a higher opinion towards bloodfeeders, negates moodlet for being fed on, mood bonus when bloodfeeders are in the colony or are the Leader, and mood penalty when they die.

- Bloodfeeders: Reviled. - Believers have a lower opinion towards bloodfeeders, mood penalty when bloodfeeders are in the colony or when they are bloodfeeder, and mood bonus when they die.

−1

1

Hemogenic

Longjump legs

Carriers have special hemogen-powered muscle fibers in their legs which allow them to jump great distances.

- Adds ability: Longjump

Jump to a distant location using super-strong hemogen-powered legs.
- Jump to the selected location, over non-LoS blocking objects, quickly but not instantly. Immune to all damage during the jump.

- Target: Location in LoS

- Range: 19.9 tiles

- Warmup Time: 30&#160;ticks (0.5&#160;secs)

- Hemogen Cost: 5

- AI Can Use: True

−2

1

Hemogenic

Piercing spine

Carriers grow an opening in their upper chest along with a quiver of keratin spines. Using a hemogen-powered chemical reaction, they can fire these spines at high speed at nearby targets with surprising accuracy.

- Adds ability: Piercing spine

Use a hemogenic chemical reaction to launch a bony spine at the target. The spine exits through the skin from an opening between the collarbones. Given the method of launch, it is surprisingly easy to aim.
- Launches an unerring spine at the target, dealing 30 RangedStab damage, with an AP of 100% and a stopping power of 1.

- Target: Single target in LoS

- Range: 3.9 tiles

- Warmup Time: 30&#160;ticks (0.5&#160;secs)

- Cooldown Time: 60&#160;ticks (1&#160;sec)

- Hemogen Cost: 20

- AI Can Use: True

- Market value of genepacks containing this gene: ×150%

−1

1

Hemogenic

Deathrest

Carriers of this gene must periodically regenerate themselves in a special coma called deathrest. Deathrest takes days, but can confer substantial bonuses. Deathrest can be accelerated and its effects enhanced by the use of a variety of special buildings and technologies. Those who put off deathresting will suffer from deathrest exhaustion.

- Creates a need for deathrest roughly every 30 days.
- Deathrest is initiated at a bed or deathrest casket and prevents action. It lasts for 4 days by default (3.6 days in casket), which can be interrupted for a stat penalty.

- If need hits 0, maximum Consciousness set to 50% and Psychic Sensitivity -100%.

- See the deathrest article for more details.

- Implanting new xenogerm, even with deathrest gene will reset pawn's deathrest capacity.

+6

1

Hemogenic

Health[edit]

- 
Click to 

Name

Description

Exclude

Weak immunity

Carriers of this gene gain immunity to diseases more slowly than normal. They may die from infections that others would survive.

- Immunity Gain Speed ×90%

+2

1

Immunity

Strong immunity

Carriers of this gene gain immunity to diseases faster than normal.

- Immunity Gain Speed ×110%

−1

1

Immunity

Super immunity

Carriers of this gene gain immunity to diseases considerably faster than normal.

- Immunity Gain Speed ×150%

- Market value of genepacks containing this gene: ×125%

−2

2

Immunity

Slow wound healing

Carriers of this gene heal from wounds half as fast as normal.

- Injury Healing Factor ×50%

+2

1

WoundHealingRate

Fast wound healing

Carriers of this gene heal from wounds twice as fast as normal.

- Injury Healing Factor ×200%

−2

1

WoundHealingRate

Superfast wound healing

Carriers of this gene heal from wounds four times as fast as normal.

- Injury Healing Factor ×400%

- Market value of genepacks containing this gene: ×125%

−3

1

WoundHealingRate

Superclotting

Carriers of this gene have extra-power coagulating factors in their blood, and will stop bleeding very quickly when wounded.

- Every 6 seconds, all bleeding wounds are automatically tended at 20-70% tend quality. The exact tend quality is fully random within this range.

- This renders it functionally impossible for the pawn to bleed out, at the minor downside of the wound being somewhat more susceptible to infection than being treated by a doctor under better conditions (e.g. by a skilled doctor, with industrial+ medicine, in a clean hospital).

- Does not affect non-bleeding wounds.

−1

1

-

-

Psychics[edit]

- 
Click to 

Name

Description

Exclude

Psychically deaf

Carriers of this gene are deaf to all psychic energy and influence outside their own minds. They cannot be affected by psychic influence, nor can they ever wield psychic power.

- Forced trait: Psychically deaf

+2

1

PsychicAbility

Psychically dull

Carriers of this gene are less psychically-sensitive than others.

- Forced trait: Psychically dull

+1

1

PsychicAbility

Psy-sensitive

Carriers of this gene are more psychically-sensitive than average.

- Psychic Sensitivity +20%

- Meditation psyfocus gain +10% / day [Verify]

- +0.1 Neural Heat Recovery per second base. Effectively 0.163 Heat/s recovery at Level 6 psylink.

- Does not suppress the psychically dull or psychically deaf traits, but is applied afterwards. This increases the pawn's base psychic sensitivity to 70 / 20 respectively.

−2

1

PsychicAbility

Super psy-sensitive

Carriers of this gene are much more psychically-sensitive than most.

- Psychic Sensitivity +40%

- Meditation psyfocus gain +20% / day [Verify]

- +0.2 Neural Heat Recovery per second base. Effectively 0.325 Heat/s recovery at Level 6 psylink.

- Does not suppress the psychically dull or psychically deaf traits, but is applied afterwards. This increases the pawn's base psychic sensitivity to 90 / 40 respectively.

−5

2

-

PsychicAbility

Psychic bonding

Carriers of this gene have a special neural organ that makes them psychically bond with a lover for life. As long as the lovers are together, they will be happy. If they are physically separated, they will be disturbed by the distance. If one dies, the other's mind will be badly disrupted.

- Romance attempts always succeed

- Gains psychic bond with first attempted romance or lovin'

- This person has a psychic bond with another person based on the psychic bonding gene. The bond itself grants some limited psychic awareness, allowing it to connect even with the psychically deaf.

- Bonded pawns receive gain ×50% pain multiplier, +15% consciousness, +12 mood and +10% psychic sensitivity when on same map or in the same caravan.

- Bonded pawns receive −10 mood, +5% psychic sensitivity, and −25% consciousness when not on same map or when one pawn is in stasis via cryptosleep caskets or a biosculpter pod.

- Bonded pawns have +50 opinion of each other.

- When one bonded pawn dies, the other will receive a −25 mood penalty that linearly decays over the course of 30 days. Note: if counseled, the counsel bonus will not decay, but will stay at the value it was applied with.

- When a bonded pawn dies, the pawn with the psychic bonding gene will immediately suffer an extreme mental break. Violence disabled pawns can still go berserk.

−1

1

-

Movement[edit]

- 
Click to 

Name

Description

Exclude

Slow runner

Carriers of this gene move more slowly than normal.

- Move Speed: −0.2 c/s

+3

1

MoveSpeed

Fast runner

Carriers of this gene move more quickly than normal.

- Move Speed: +0.2 c/s

−3

1

MoveSpeed

Very fast runner

Carriers of this gene move much more quickly than normal.

- Move Speed: +0.4 c/s

−5

1

MoveSpeed

Naked speed

Carriers of this gene move slower while clothed, and faster while naked.

- Move speed: −0.20 c/s (clothed)

- Move speed: +0.10 c/s (unclothed)

+2

1

-

Webbed phalanges

Carriers of this gene have webbed fingers and toes, allowing them to move faster in water. Webbed fingers slightly reduce fine motor control.

- Manipulation −5%

- Water tiles no longer hinder movement for this pawn.
- Mechanically, any terrain with the water tag will be treated as having a movement speed of 100% for pawns with this gene.

−1

1

-

-

Mood[edit]

- 
Click to 

Name

Description

Exclude

Very unhappy

Carriers of this gene are highly predisposed to negative emotion. They'll see the bad in every situation and have a much lower mood than others.

- Permanent −10 Genetic depression thought

+5

1

-

Mood

Unhappy

Carriers of this gene are predisposed to pessimistic perceptions. They'll tend to interpret things negatively and have lower mood than others.

- Permanent −5 Genetic pessimism thought

+3

1

Mood

Happy

Carriers of this gene are predisposed to optimistic feelings. They'll have higher mood than others.

- Permanent +5 Genetic optimism thought

−1

2

-

Mood

Very happy

Carriers of this gene are highly predisposed to optimism and not at all inclined to think negatively. They'll have much higher mood than others.

- Permanent +10 Genetic joy thought

−2

3

Mood

Temperature[edit]

- 
Click to 

Name

Description

Exclude

Cold weakness

Carriers of this gene are slightly less comfortable in cold temperatures.

- Minimum Comfortable Temperature: +5&#160;°C (9&#160;°F)

+1

1

MinTemperature

Cold tolerant

Carriers of this gene are slightly more comfortable in cold temperatures.

- Minimum Comfortable Temperature: −10&#160;°C (18&#160;°F)

−1

1

MinTemperature

Cold super-tolerant

Carriers of this gene are much more comfortable in cold temperatures.

- Minimum Comfortable Temperature: −20&#160;°C (36&#160;°F)

−2

1

MinTemperature

Heat weakness

Carriers of this gene are slightly less comfortable in warm temperatures.

- Maximum Comfortable Temperature: −5&#160;°C (9&#160;°F)

+1

1

MaxTemperature

Heat tolerant

Carriers of this gene are slightly more comfortable in warm temperatures.

- Maximum Comfortable Temperature: +10&#160;°C (18&#160;°F)

−1

1

MaxTemperature

Heat super-tolerant

Carriers of this gene are much more comfortable in warm temperatures.

- Maximum Comfortable Temperature: +20&#160;°C (36&#160;°F)

−2

1

MaxTemperature

Resistance and sensitivity[edit]

- 
Click to 

Name

Description

Exclude

Tox resistance

Carriers of this gene are resistant to toxic buildup from any source. This includes pollution, toxic fallout, tox gas, and direct attacks with venom or injected poison. They'll gain half the amount of toxic buildup compared to others. Cellular filters in the lung and skin reduce the dose of toxins entering the bloodstream.

- Toxic Resistance: +50%

−2

1

-

ToxResistance

Tox immunity

Carriers of this gene are totally immune to toxic buildup from all sources including polluted terrain, toxic fallout, tox gas, and direct attacks with venom or injected poison. They are also not bothered by acidic smog. The carrier's biochemical pathways are modified to route around interference from nearly all known toxins. Along with enhancements to the kidneys and liver, this keeps carriers comfortable in even the most toxic of environments.

- Toxic Resistance: +100%

- Tox gas immunity

- Removes mood: Toxic fallout: -5

- Removes mood: Acidic smog: -5

−4

2

ToxResistance

Partial antitoxic lungs

Carriers of this gene are resistant to environmental toxins. They get less toxic buildup from tox gas, polluted terrain, and toxic fallout, but are still vulnerable to direct attacks with venom or injected poison. Additionally, they build up rot stink exposure slower.

- Toxic Environment Resistance: +50%

−1

1

ToxicEnvironmentResistance

Total antitoxic lungs

Carriers of this gene are immune to environmental toxins, but not from direct toxic attacks. They get no toxic buildup from tox gas, polluted terrain, or toxic fallout, and they are not bothered by acidic smog. They are still vulnerable to direct attacks like venom and injected poison. Additionally, they are immune to rot stink exposure.

- Toxic Environment Resistance: +100%

- Tox gas immunity

- Removes mood: Toxic fallout: -5

- Removes mood: Acidic smog: -5

−3

2

ToxicEnvironmentResistance

Mild UV sensitivity

Carriers of this gene have biological compounds in their skin that react painfully to UV radiation. They are unusually sensitive to sunlight.

- When in sunlight (when on an unroofed tile while light levels from natural sunlight are 11% or more):
- Move Speed ×90%

- Mood: Sunlight Sensitivity: −6

- Does not cause pain, despite the description.

+3

1

UVSensitivity

Intense UV sensitivity

Carriers of this gene have biological compounds in their skin that react dangerously to UV radiation. They are intensely sensitive to sunlight.

- When in sunlight (when on an unroofed tile while light levels from natural sunlight are 11% or more):
- Move Speed ×80%

- Mood: Sunlight Sensitivity: −12

- Does not cause pain.

+4

2

UVSensitivity

Fire resistant

Carriers of this gene have special fast-acting sweat glands and heat-resistant skin. They only take 25% of the normal damage from fire. The chance of them catching on fire is also drastically reduced.

- Flammability ×10%

- Flame damage ×25%

Note that this does not affect Heat or Vaporize damage

−2

1

FireDamage

Tinderskin

Carriers have dry, thin skin which burns easily from fire, and their immune systems react very poorly to this kind of threat. Damage from fire is multiplied by 4.

- Flame damage ×400%

Note that this does not affect Heat or Vaporize damage

+2

1

FireDamage

Pyrophobia

Carriers of this gene have an intense fear of fire. When fires are close, there is a chance they will have a mental breakdown at any moment.

- If the pawn has line of sight of a fire within 19.9 tiles, it is considered "near fire" and the following happens:
- −10 Afraid of fire moodlet

- 0.1 day mtb chance of "Fire terror" mental break that cause "panic-fleeing fire" mental state, ends when not "near fire" for 500&#160;ticks (8.33&#160;secs)

- Suppresses Pyromaniac trait

Note that blind pawns are still affected by pyrophobia, and will still flee

+4

1

-

Vacuum resistant

Carriers of this gene have skin that releases a waxy substance when air pressure is low, preventing vacuum burns and allowing them to survive longer when exposed to vacuum.

- Immune to vacuum burns

- Vacuum resistance: +45%

- Minimum Comfortable Temperature: −5&#160;°C (9&#160;°F)

−1

1

VacuumResistance

Violence[edit]

- 
Click to 

Name

Description

Exclude

Dead calm

Carriers of this gene feel calm in every situation and have a very placid demeanor. They will never start social fights or have aggressive mental breaks.

- Effects:
- Will never do social fights

- Mental breaks are never violent (Tantrum, Berserk, Slaughterer, Murderous Rage)

- Will never prison break

- Arresting never fails, and will never berserk on arrest.

−1

1

Aggression

Aggressive

Carriers of this gene are quick to anger. They are twice as likely to start social fights. When they have mental breaks, they are twice as likely to choose an aggressive kind of break.

- Effects:
- Social fight chance factor ×200%

- Chance mental break is violent ×200% (Tantrum, Berserk, Slaughterer, Murderous Rage) [Wb minor breaks?]

- Prison break interval factor ×60%

+2

1

Aggression
Aggressive

Hyper-aggressive

Carriers of this gene are hormonally high-strung and very aggressive. They are three times as likely to start social fights. Any mental break they have will be of an aggressive type.

- Effects:
- Social fight chance factor ×300%

- Mental breaks are always[Verify] violent where possible.(Tantrum, Berserk, Slaughterer, Murderous Rage) Tiers without violent options, i.e. Minor breaks, non-violent breaks are chosen instead.[All types?]

- Prison break interval factor ×40%

+3

1

Aggression
Aggressive

Weak melee damage

Carriers of this gene do less damage in close-quarters combat. Weak fast-twitch muscle fibers make their strikes shaky and weak.

- Melee damage factor ×50%
- This also affects melee AP when calculated from damage. It does not affect the AP of weapons that are set independently of damage, such as: Spears, Monoswords, Persona monoswords, Hand talon, Knee spikes, and flesh whips.

+1

1

MeleeDamage

Strong melee damage

Carriers of this gene do more damage in close-quarters combat. Extra-strong fast-twitch muscle fibers make their strikes accurate and powerful.

- Melee damage factor ×150%
- This also affects melee AP when calculated from damage. It does not affect the AP of weapons that are set independently of damage, such as: Spears, Monoswords, Persona monoswords, Hand talon, Knee spikes, and flesh whips.

−2

1

MeleeDamage

Violence disabled

Carriers of this gene are emotionally and mentally incapable of engaging in violence. They are overwhelmingly resistant to and horrified by the idea of hurting another.

- Disables work:
- Hunt

- Violent

+3

1

MeleeDamage
ShootingAccuracy
Aggressive
KillThirst

Kind instinct

Carriers of this gene are high in trait agreeableness and are very conscientious. They rarely insult others and will sometimes offer kind words to brighten the moods of those around them. They also never judge people by their appearance.

- Forced trait: Kind

- Suppresses Abrasive and Psychopath traits

−1

1

-

Kill thirst

Carriers of this gene lust for the feeling of ending another's life. They will become irritated if they go for too long without killing someone in close combat.
 
- Causes need: Kill satiety. Inflicts an increasing mood penalty during long periods between melee kills. See the Kill satiety page for details.

+4

1

-

KillThirst

Sleep[edit]

- 
Click to 

Name

Description

Exclude

Very sleepy

Carriers of this gene get tired much faster than others.

- Sleep Fall Rate: ×180%

+4

1

-

Sleep

Sleepy

Carriers of this gene get tired somewhat faster than others.

- Sleep Fall Rate: ×140%

+2

1

Sleep

Low sleep

Carriers of this gene get tired less quickly than others.

- Sleep Fall Rate: ×40%

−4

2

Sleep

Never sleep

Carriers of this gene have a unique metabolic process which allows clusters of neurons to sleep while the rest of the brain stays awake. They never need to sleep.

- Effects:
- Disables need: Sleep

- If all pawns in a caravan have either this gene, a circadian half-cycler, or the body mastery trait, and they travel without animals, they don't need to stop at night.

- Market value of genepacks containing this gene: ×125%

−6

3

-

Sleep

Pain[edit]

- 
Click to 

Name

Description

Exclude

Delicate

Carriers of this gene take greater injuries than others from the same damage. They have thin, brittle bones and less binding molecules in joints and flesh.

- Forced trait: Delicate

- Suppresses Tough trait

+3

1

Toughness

Robust

Carriers of this gene take less injuries than others from the same damage. They have thickened, densified bones, nearly-solid ribcages, and strengthened binding factors in joints and flesh.

- ×75% Incoming Damage Multiplier
- Note that despite being incompatible with the Delicate gene, it stacks multiplicatively with other Incoming Damage Multiplier factors, including the Delicate trait. See for Incoming Damage Multiplier further details on stacking.

−2

1

Toughness

Extra pain

Carriers of this gene feel more pain than others given the same injuries. Neuron activity in the brain's nociception center is amplified, so pain feels extra-intense and fiery. This can be protective, but overall it's considered a negative and makes it hard to push through difficult situations.

- Forced trait: Wimp

- Suppresses Masochist and Brawler traits

+2

1

Pain

Reduced pain

Carriers of this gene feel half as much pain compared to a baseliner. Reduced neuron activity in the brain's nociception centers makes pain dull and faint. This can be advantageous sometimes, and dangerous other times.

- Pain ×50%

−1

1

Pain

Reproduction[edit]

- 
Click to 

Name

Description

Exclude

Low libido

Carriers of this gene are less likely to engage in lovin' with their partner.

- MTB Lovin' Factor: ×2

0

1

-

Libido

High libido

Carriers of this gene are more likely to engage in lovin' with their partner.

- MTB Lovin' Factor: ×0.5

0

1

Libido

Sterile

Carriers of this gene cannot reproduce by natural means.

- Fertility ×0%

+1

1

-

Fertility

Fertile

Carriers of this gene have a higher chance of becoming pregnant or impregnating others.

- Fertility ×200%

0

1

-

Fertility

Beauty[edit]

- 
Click to 

Name

Description

Exclude

Very unattractive

Carriers of this gene have misshapen, asymmetrical facial structures and blotchy skin. They're hard to look at.

- Beauty (Pawn): −2

- Market Value: −700

+2

1

-

Beauty

Unattractive

Carriers of this gene have exaggerated facial features and poor skin that are generally considered ugly.

- Beauty (Pawn): −1

- Market Value: −350

+1

1

Beauty

Attractive

Carriers of this gene have unusually symmetrical, balanced facial features and extra-clear skin which gives them a pleasing appearance.

- Beauty (Pawn): +1

- Market Value: +350

−1

1

Beauty

Very attractive

Carriers of this gene have remarkably precise and symmetrical faces. Their features are distinctive and strong without being exaggerated, and their skin is nearly perfect. They are generally seen as beautiful.

- Beauty (Pawn): +2

- Market Value: +700

−2

1

Beauty

Cosmetic[edit]

- 
Click to 

Name

Description

Exclude

Red eyes

Carriers of this gene have deeply red-pigmented eyes.

0

0

EyeColor

Gray eyes

Carriers of this gene have pale white-gray eyes.

0

0

EyeColor

No hair

Carriers of this gene grow no hair on the head.

0

0

HairStyle

Short-haired

Carriers of this gene can only grow short hair.

0

0

HairStyle

Long-haired

Carriers of this gene grow hair on the head very quickly.

0

0

HairStyle

Only bushy beards

Male carriers of this gene experience rapid beard growth and are uncomfortable cutting their beards.

0

0

-

BeardStyle

Beardless

Carriers of this gene grow no facial hair.

0

0

BeardStyle

Unisex beards

Carriers of this gene always have thick facial hair, even women.

0

0

BeardStyle

Human ears

Carriers of this gene have regular human ears.

0

0

-

Ears

Pointed ears

Carriers of this gene have pointed ears.

0

0

-

Ears

Cat ears

Carriers of this gene have cat-like ears.

0

0

-

Ears

Floppy ears

Carriers of this gene grow long, floppy hound-like ears.

0

0

-

Ears

Pig ears

Carriers of this gene will grow pointed pig-like ears.

0

0

Ears

Human nose

Carriers of this gene have regular human noses.

0

0

-

Nose

Human jaw

Carriers of this gene have regularly-shaped jaws.

0

0

-

Jaw

Heavy jaw

Carriers of this gene have large jaws.

0

0

Jaw

Gaunt head

Carriers of this gene have a pinched, gaunt appearance in their face and head.

0

0

Jaw

Heavy brow

Carriers of this gene have a prominent brow.

0

0

-

Center-horn

Carriers of this gene grow a single horn protruding from the center of the forehead.

0

0

-

Headbone

Mini-horns

Carriers of this gene grow two small horns protruding from the forehead.

0

0

Headbone

Human headbone

Carriers of this gene have regular human skulls.

0

0

-

Headbone

Human voice

Carriers of this gene have regular human vocal cords.

0

0

-

Voice

Pig voice

Carriers have a squealing voice like that of a pig.
https://rimworldwiki.com/wiki/File:Pawn_Pigskin_Call_02e.wav

0

0

Voice

Roar voice

Carriers have an animal-like roaring voice.
https://rimworldwiki.com/wiki/File:Roar_Voice_Call_B02.wav

0

0

Voice

Facial ridges

Carriers of this gene grow raised ridges of skin on their face.

0

0

-

Body type[edit]

Since people without these genes can have any of the four body types, these genes effectively limit what body types a xenotype can have. For example, Neanderthals cannot be thin, because they have all three of the other genes.

- 
Click to 

Name

Description

Exclude

Standard body

Carriers can have average-shaped bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed.

0

0

BodyType

Thin body

Carriers can have thin bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed.

0

0

BodyType

Fat body

Carriers can have fat bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed.

0

0

BodyType

Hulk body

Carriers can have large bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed.

0

0

BodyType

Hair[edit]

These genes are defined in Core, not Biotech.

All of them have a "random brightness factor" of 0.12 unless otherwise specified. 

- 
Click to 

Name

Description

Weight

Exclude

Snow-white hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (250, 250, 250)

- Random brightness factor: 0

0

0

0.05

HairColor

Gray hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (0.65, 0.65, 0.65)

0

0

0.02

HairColor

Blonde hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (237, 202, 156)

- Selection weight factor with dark skin: 0

0

0

1?

-

HairColor

Sandy-blonde hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (193, 146, 85)

- Selection weight factor with dark skin: 0

0

0

1?

HairColor

Orange hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (189, 133, 49)

0

0

0.05

HairColor

Reddish-brown hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (132, 83, 47)

0

0

1?

-

HairColor

Brown hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (90, 58, 32)

0

0

1?

-

HairColor

Dark-brown hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (56, 36, 18)

0

0

1.5

-

HairColor

Dark-reddish hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (0.25, 0.2, 0.15)

0

0

1.5

-

HairColor

Mid-black hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (0.31, 0.28, 0.26)

0

0

1.5

-

HairColor

Dark-black hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (0.2, 0.2, 0.2)

0

0

1.5

-

HairColor

Ink-black hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (25, 25, 25)

- Random brightness factor: 0

0

0

0.05

-

HairColor

Blue hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (34, 63, 227)

0

0

0.05

-

HairColor

Teal hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (52, 191, 182)

0

0

0.05

-

HairColor

Green hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (72, 201, 40)

0

0

0.05

-

HairColor

Pink hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (191, 86, 149)

0

0

0.05

-

HairColor

Purple hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (227, 115, 255)

0

0

0.05

-

HairColor

Red hair

Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected.

- Hair color override: (191, 86, 86)

0

0

0.05

-

HairColor

Melanin[edit]

These natural skin colors are not available in the xenotype editor and cannot be extracted. Every person gets one of these as a germline gene unless they already have a skin-color germline gene (e.g. Dirtmoles have light gray skin instead of these).

These genes are defined in Core, not Biotech. They are all named "Skin color" in-game.

- 
Click to 

Name

Description

Weight

Exclude

Skin_Melanin1

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (242, 237, 224)

- Min melanin: 0

0

0

0.2

SkinColor

Skin_Melanin2

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (255, 239, 213)

- Min melanin: 0.1

0

0

0.5

SkinColor

Skin_Melanin3

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (255, 239, 201)

- Min melanin: 0.25

0

0

0.5

SkinColor

Skin_Melanin4

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (255, 239, 189)

- Min melanin: 0.45

0

0

0.5

SkinColor

Skin_Melanin5

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (249, 219, 165)

- Min melanin: 0.58

0

0

0? 1?

SkinColor

Skin_Melanin6

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (242, 199, 140)

- Min melanin: 0.63

0

0

0? 1?

SkinColor

Skin_Melanin7

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (228, 158, 90)

- Min melanin: 0.75

0

0

0? 1?

SkinColor

Skin_Melanin8

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (130, 91, 48)

- Min melanin: 0.83

0

0

0.5

SkinColor

Skin_Melanin9

Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected.

- Skin color base: (99, 70, 36)

- Min melanin: 0.9

0

0

0.2

SkinColor

Skin[edit]

These exotic (non-natural) skin colors do not appear on anyone without the gene. Like body type genes and hair genes, a person can have more than one skin color gene (e.g. Impids have three), and one will be chosen.

All of these genes have a "random brightness factor" of 0.18 unless otherwise specified.

- 
Click to 

Name

Description

Exclude

Green skin

Carriers of this gene produce a pigment that gives their skin a green color.

- Skin color override: (169,182,108)

0

0

-

SkinColorOverride

Deep yellow skin

Carriers of this gene produce a pigment that gives their skin a deep yellow color.

- Skin color override: (204, 199, 65)

0

0

-

SkinColorOverride

Pale yellow skin

Carriers of this gene produce a pigment that turns their skin a grayish yellow color.

- Skin color override: (193, 165, 99)

0

0

SkinColorOverride

Orange skin

Carriers of this gene produce a pigment that gives their skin an orange color.

- Skin color override: (210, 114, 63)

- Random brightness factor: 0

0

0

SkinColorOverride

Deep red skin

Carriers of this gene produce a deep-red pigment that gives their skin an almost bloody appearance.

- Skin color override: (150, 62, 62)

0

0

SkinColorOverride

Pale red skin

Carriers of this gene produce a pigment that turns their skin a moderate red color.

- Skin color override: (222, 106, 106)

0

0

-

SkinColorOverride

Purple skin

Carriers of this gene produce a pigment that gives their skin a purple color.

- Skin color override: (97, 87, 195)

0

0

SkinColorOverride

Blue skin

Carriers of this gene produce a pigment that turns their skin a blue color.

- Skin color override: (100, 165, 193)

0

0

SkinColorOverride

Sheer white skin

Carriers of this gene have sheer white skin, unlike natural skin tones, due to a special engineered reflective cell covering.

- Skin color override: (250, 240, 240)

- Random brightness factor: 0

0

0

SkinColorOverride

Light gray skin

Carriers of this produce a light-gray pigment in their skin.

- Skin color override: (200, 200, 200)

0

0

SkinColorOverride

Slate gray skin

Carriers of this gene produce a pigment that turns their skin slate gray.

- Skin color override: (90, 90, 90)

0

0

SkinColorOverride

Ink black skin

Carriers of this gene produce a pigment that turns their skin a pale black color almost as dark as ink.

- Skin color override: (55, 55, 55)

- Random brightness factor: 0

0

0

-

SkinColorOverride

Miscellaneous[edit]

- 
Click to 

Name

Description

Exclude

Strong stomach

Carriers of this gene have an extra toxin-filtering organ in their stomach and will never suffer from food poisoning even after eating rotten food.

- Immune to food poisoning.
- Does not affect pre-existing conditions. Only prevents new illnesses.

−1

1

-

Robust digestion

Carriers of this gene grow a multi-fold stomach, allowing them to digest raw foods more efficiently than baseline humans. In general, they get the same nutrition from raw food as from if it is cooked. They also don't mind the taste of raw food at all.

- Raw Nutrition Multiplier ×180%
- Note: Does not apply to insect jelly or fertilized eggs. Does apply to unfertilized eggs.

- Removes mood: Ate raw food: -7

- Note: Does not prevent food poisoning.

−2

2

-

Slow study

Carriers of this gene have deficient long-term memories and don't understand new ideas quickly. They are slow at learning new skills and knowledge.

- Global Learning Factor ×50%

+2

1

Learning

Quick study

Carriers of this gene have excellent memories and grasp new ideas quickly. They learn faster than others.

- Global Learning Factor +50%

−3

2

-

Learning

Nearsighted

Carriers of this gene have difficulty seeing at a distance. Their shooting accuracy at long ranges is reduced.

- Accuracy factor (long) ×25%

- Accuracy factor (medium) ×50%

+2

1

ShootingAccuracy

Dark vision

Carriers of this gene see well in low light and are unaffected by mood penalties related to darkness. They have a reflective layer behind the retina that amplifies their ability to see in the dark.

- Negates the Global Work Speed penalty from darkness.

- Negates the Move Speed penalty from darkness. Note: This effect is not mentioned by the in-game description

- Removes mood: Darkness: −5

−1

1

-

Inbred

This genetic condition affects a person's fertility, immunity, and mental capacity.

- Forced trait: Slow learner

- Fertility ×50%

- Immunity gain speed ×85%

- Note: Despite being harmful, this gene also lowers metabolic efficiency.

- See inbreeding for full details.

−2

1

-

-

Mild cell instability

Carriers of this gene need less metabolic energy to stay alive, at the cost of reduced stability in their cell-replication machinery.

- Lifespan Factor ×80%
- Note this means age-related diseases come earlier, e.g. Frail can happen at 40 instead of 50

- Cancer Rate Factor ×300%

- Immunity gain speed ×96%

+2

1

-

CellInstability

Major cell instability

Carriers of this gene need much less metabolic energy to stay alive, at the cost of greatly-reduced stability in their cell-replication machinery.

- Lifespan Factor ×60%
- Note this means age-related diseases come earlier, e.g. Frail can happen at 30 instead of 50

- Cancer Rate Factor ×500%

- Immunity gain speed ×92%

+4

1

-

CellInstability

Grayless hair

Carriers of this gene keep their natural hair color as they age.

- No age-related gray hair.

0

1

-

Human hands

Carriers of this gene have regular human hands.

0

0

-

Hands

Trotter hands

Carriers of this gene have hands that partially resemble pig trotters. This reduces their ability to manipulate objects.

- Manipulation ×85%

+1

1

Hands

Elongated fingers

Long, delicate fingers improve the carrier's manipulation capacity. This aids with many tasks, especially crafting and construction.

- Manipulation ×110%

−1

1

Hands

Furskin

Carriers of this gene grow thick fur all over their body, which protects them from cold temperatures.

- Minimum Comfortable Temperature: −10&#160;°C (18&#160;°F)

- Non-furskin romance chance ×20%

- Removes mood: Naked: -6

- Removes mood: Uncovered (body part): -4

- Removes opinion: Uncovered (body part): -10 of any other pawns

−1

1

HairStyle
Fur
BeardStyle

Pig nose

Carriers of this gene have pig-like snouts.

- Non-pig nose romance chance ×20%

0

0

Nose

Pollution stimulus

Carriers of this gene get a chemical rush from being exposed to pollution. This makes them move faster and helps them think clearer. A similar gene is found in combat-engineered mega-insects.

- Gain stat bonuses when exposed to pollution.
- Increases move speed and consciousness. See Pollution stimulus for full details.

−1

1

-

Unstoppable

Carriers of this gene are not slowed down when taking damage.

- Stagger Time Multiplier ×0%

−2

1

-

Furry tail

Carriers of this gene grow a fluffy tail which partially protects them from cold temperatures.

- Minimum Comfortable Temperature: −10&#160;°C (−18&#160;°F)

- Adds an aesthetic only tail to the pawn's sprite

- Note: Does not add a targetable or damageable body part

−1

1

Tail

Smooth tail

Carriers of this gene grow a slender tail that can act as a dexterous fifth limb.

- Manipulation: +5%

- Adds an aesthetic only tail to the pawn's sprite

- Note: Does not add a targetable or damageable body part

−1

1

-

Tail

Indoor dweller

Carriers of this gene have no need for the outdoors and will never feel cooped up no matter how long they stay inside.

- Disables need: Outdoors

−1

1

 
 

-

Low gravity adapted 

Carriers of this gene move and work more easily in low-gravity environments. However They're slower and less efficient when planetside.

- Move Speed: −0.2 c/s (planetside)

- Global work speed −10% (planetside)

- Move Speed: +0.4 c/s (in space)

- Global work speed +10% (in space)

+1

1

-

Aptitudes[edit]

- 
Click to 

Name

Description

Skill

Awful Animals

The carrier's aptitude in Animals is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Animals.

- Animals: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Animals

+2

1

Animals

Awful Artistic

The carrier's aptitude in Artistic is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Artistic.

- Artistic: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Artistic

+2

1

Artistic

Awful Construction

The carrier's aptitude in Construction is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Construction.

- Construction: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Construction

+2

1

-

Construction

Awful Cooking

The carrier's aptitude in Cooking is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Cooking.

- Cooking: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Cooking

+2

1

-

Cooking

Awful Crafting

The carrier's aptitude in Crafting is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Crafting.

- Crafting: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Crafting

+2

1

-

Crafting

Awful Medical

The carrier's aptitude in Medical is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Medical.

- Medical: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Medical

+2

1

-

Medical

Awful Melee

The carrier's aptitude in Melee is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Melee.

- Melee: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Melee

+2

1

Melee

Awful Mining

The carrier's aptitude in Mining is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Mining.

- Mining: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Mining

+2

1

Mining

Awful Intellectual

The carrier's aptitude in Intellectual is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Intellectual.

- Intellectual: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Intellectual

+2

1

-

Intellectual

Awful Plants

The carrier's aptitude in Plants is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Plants.

- Plants: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Plants

+2

1

Plants

Awful Shooting

The carrier's aptitude in Shooting is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Shooting.

- Shooting: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Shooting

+2

1

-

Shooting

Awful Social

The carrier's aptitude in Social is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Social.

- Social: −8. Note: Experience gain and decay applies as if this offset did not exist.

- Removes all passions for Social

+2

1

Social

Poor Animals

The carrier's aptitude in Animals is reduced by 4. Aptitude acts like an offset on skill level.

- Animals: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Animals

Poor Artistic

The carrier's aptitude in Artistic is reduced by 4. Aptitude acts like an offset on skill level.

- Artistic: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Artistic

Poor Construction

The carrier's aptitude in Construction is reduced by 4. Aptitude acts like an offset on skill level.

- Construction: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

-

Construction

Poor Cooking

The carrier's aptitude in Cooking is reduced by 4. Aptitude acts like an offset on skill level.

- Cooking: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Cooking

Poor Crafting

The carrier's aptitude in Crafting is reduced by 4. Aptitude acts like an offset on skill level.

- Crafting: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

-

Crafting

Poor Medical

The carrier's aptitude in Medical is reduced by 4. Aptitude acts like an offset on skill level.

- Medical: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

-

Medical

Poor Melee

The carrier's aptitude in Melee is reduced by 4. Aptitude acts like an offset on skill level.

- Melee: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

-

Melee

Poor Mining

The carrier's aptitude in Mining is reduced by 4. Aptitude acts like an offset on skill level.

- Mining: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

-

Mining

Poor Intellectual

The carrier's aptitude in Intellectual is reduced by 4. Aptitude acts like an offset on skill level.

- Intellectual: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Intellectual

Poor Plants

The carrier's aptitude in Plants is reduced by 4. Aptitude acts like an offset on skill level.

- Plants: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Plants

Poor Shooting

The carrier's aptitude in Shooting is reduced by 4. Aptitude acts like an offset on skill level.

- Shooting: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Shooting

Poor Social

The carrier's aptitude in Social is reduced by 4. Aptitude acts like an offset on skill level.

- Social: −4. Note: Experience gain and decay applies as if this offset did not exist.

+1

1

Social

Strong Animals

The carrier's aptitude in Animals is increased by 4. Aptitude acts like an offset on skill level.

- Animals: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Animals

Strong Artistic

The carrier's aptitude in Artistic is increased by 4. Aptitude acts like an offset on skill level.

- Artistic: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Artistic

Strong Construction

The carrier's aptitude in Construction is increased by 4. Aptitude acts like an offset on skill level.

- Construction: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Construction

Strong Cooking

The carrier's aptitude in Cooking is increased by 4. Aptitude acts like an offset on skill level.

- Cooking: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Cooking

Strong Crafting

The carrier's aptitude in Crafting is increased by 4. Aptitude acts like an offset on skill level.

- Crafting: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Crafting

Strong Medical

The carrier's aptitude in Medical is increased by 4. Aptitude acts like an offset on skill level.

- Medical: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Medical

Strong Melee

The carrier's aptitude in Melee is increased by 4. Aptitude acts like an offset on skill level.

- Melee: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

Melee

Strong Mining

The carrier's aptitude in Mining is increased by 4. Aptitude acts like an offset on skill level.

- Mining: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Mining

Strong Intellectual

The carrier's aptitude in Intellectual is increased by 4. Aptitude acts like an offset on skill level.

- Intellectual: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

Intellectual

Strong Plants

The carrier's aptitude in Plants is increased by 4. Aptitude acts like an offset on skill level.

- Plants: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Plants

Strong Shooting

The carrier's aptitude in Shooting is increased by 4. Aptitude acts like an offset on skill level.

- Shooting: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

-

Shooting

Strong Social

The carrier's aptitude in Social is increased by 4. Aptitude acts like an offset on skill level.

- Social: +4. Note: Experience gain and decay applies as if this offset did not exist.

−1

2

Social

Great Animals

The carrier's aptitude in Animals is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Animals.

- Animals: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Animals

−3

2

Animals[A]

Great Artistic

The carrier's aptitude in Artistic is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Artistic.

- Artistic: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Artistic

−3

2

-

Artistic[A]

Great Construction

The carrier's aptitude in Construction is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Construction.

- Construction: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Construction

−3

2

Construction[A]

Great Cooking

The carrier's aptitude in Cooking is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Cooking.

- Cooking: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Cooking

−3

2

-

Cooking[A]

Great Crafting

The carrier's aptitude in Crafting is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Crafting.

- Crafting: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Crafting

−3

2

Crafting[A]

Great Medical

The carrier's aptitude in Medical is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Medical.

- Medical: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Medical

−3

2

-

Medical[A]

Great Melee

The carrier's aptitude in Melee is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Melee.

- Melee: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Melee

−3

2

Melee[A]

Great Mining

The carrier's aptitude in Mining is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Mining.

- Mining: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Mining

−3

2

Mining[A]

Great Intellectual

The carrier's aptitude in Intellectual is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Intellectual.

- Intellectual: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Intellectual

−3

2

Intellectual[A]

Great Plants

The carrier's aptitude in Plants is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Plants.

- Plants: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Plants

−3

2

-

Plants[A]

Great Shooting

The carrier's aptitude in Shooting is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Shooting.

- Shooting: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Shooting

−3

2

Shooting[A]

Great Social

The carrier's aptitude in Social is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Social.

- Social: +8. Note: Experience gain and decay applies as if this offset did not exist.

- Adds one additional passion for Social

−3

2

Social[A]

^A If overridden by strong or poor aptitude gene, passion from great aptitude gene is added anyway.
Drugs[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: How does impervious eliminate tolerance build up - is it -100% or x0%. Both are listed.

This section has been suggested for recoding. Reason: The patch notes for 1.5 say that drug-related genes no longer prevent overdose across all drugs. Verify if true, then edit this section to reflect the change. You can help RimWorld Wiki by improving it.

There are one of each of these for each drug, except for ambrosia, luciferium and penoxycyline.

- 
Click to 

Name

Description

Alcohol resistant

Carriers are only half as likely to become addicted to Alcohol.

- Alcohol addiction factor: ×50%

- Alcohol tolerance gain: ×50%

−1

1

-

Smokeleaf resistant

Carriers are only half as likely to become addicted to Smokeleaf.

- Smokeleaf addiction factor: ×50%

- Smokeleaf tolerance gain: ×50%

−1

1

-

Psychite resistant

Carriers are only half as likely to become addicted to Psychite.

- Psychite addiction factor: ×50%

- Psychite tolerance gain: ×50%

- Overdose chance: ×50% [Random or All]

−2

1

-

Go-juice resistant

Carriers are only half as likely to become addicted to Go-juice.

- Go-juice addiction factor: ×50%

- Overdose chance: ×50% [Random or All]

−2

1

-

Wake-up resistant

Carriers are only half as likely to become addicted to Wake-up.

- Wake-up addiction factor: ×50%

- Overdose chance: ×50% [Only this drug?] [Random or All?]

−2

1

-

Alcohol impervious

Carriers of this gene never get addicted to Alcohol.

- Alcohol addiction factor: x0%

- Tolerance build-up for Alcohol: -100%

−3

2

-

Smokeleaf impervious

Carriers of this gene never get addicted to Smokeleaf.

- Smokeleaf addiction factor: x0%

- Tolerance build-up for Smokeleaf: -100%

−3

2

-

Psychite impervious

Carriers of this gene never get addicted to Psychite.

- Psychite addiction factor: x0%

- Tolerance build-up for Psychite: ×0%

- Cumulative overdose severity and random, per-dose overdose chance from Psychite based drugs eliminated.

−5

2

-

Go-juice impervious

Carriers of this gene never get addicted to Go-juice.

- Go-juice addiction factor: x0%

- Cumulative overdose severity and random, per-dose overdose chance from Go-juice eliminated.

−5

2

-

Wake-up impervious

Carriers of this gene never get addicted to Wake-up.

- Wake-up addiction factor: x0%

- Cumulative overdose severity and random, per-dose overdose chance from Wake-up eliminated.

−5

2

Alcohol dependency

Carriers of this gene need to ingest alcohol on a regular basis to survive. After 5 days without alcohol, carriers will suffer from drug deficiency. After 30 days, they will fall into a coma. After 60 days, they will die.

- Teetotalers will take the required drug without penalties, but ideoligion can still block taking them.

- Chemical dependency severity increases by 0.2 per day. Reduced to 0% upon taking beer.
- Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85

- Severity 1 (5 days): Consciousness 70% max, Moving 80% max, Manipulation 50% max,

- Severity 6 (30 days): Consciousness 10% max (Unconsciousness)

- Severity 12 (60 days): Consciousness 0% max (Death)

- Alcohol addiction factor: x0%

- Teetotalers can take the required drug without penalties. However, ideoligions against drug use will apply the −15 Used drug moodlet.

- Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

+3

1

-

Smokeleaf dependency

Carriers of this gene need to ingest Smokeleaf on a regular basis to survive. After 5 days without smokeleaf, carriers will suffer from smokeleaf deficiency. After 30 days, they will fall into a coma. After 60 days, they will die.

- Teetotalers will take the required drug without penalties, but ideoligion can still block taking them.

- Chemical dependency severity increases by 0.2 per day. Reduced to 0% upon taking a smokeleaf joint.
- Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85

- Severity 1 (5 days): Consciousness 70% max, Moving 80% max, Manipulation 50% max,

- Severity 6 (30 days): Consciousness 10% max (Unconsciousness)

- Severity 12 (60 days): Consciousness 0% max (Death)

- Smokeleaf addiction factor: x0%

- Teetotalers can take the required drug without penalties. However, ideoligions against drug use will apply the −15 Used drug moodlet.

- Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

+3

1

-

Psychite dependency

Carriers of this gene need to ingest psychite on a regular basis to survive. After 5 days without Psychite, carriers will suffer from psychite deficiency. After 30 days, they will fall into a coma. After 60 days, they will die.

- Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking psychite tea, flake, or yayo.
- Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85

- Severity 1 (5 days): Consciousness 70% max, Moving 80% max, Manipulation 50% max,

- Severity 6 (30 days): Consciousness 10% max (Unconsciousness)

- Severity 12 (60 days): Consciousness 0% max (Death)

- Psychite addiction factor: x0%

- Teetotalers can take the required drug without penalties. However, ideoligions against drug use will apply the −15 Used drug moodlet.

- Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

+4

1

Go-juice dependency

Carriers of this gene need to ingest Go-juice on a regular basis to survive. After 5 days without Go-juice, carriers will suffer from Go-juice deficiency. After 30 days, they will fall into a coma. After 60 days, they will die.

- Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking go-juice.
- Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85

- Severity 1 (5 days): Consciousness 70% max, Moving 80% max, Manipulation 50% max,

- Severity 6 (30 days): Consciousness 10% max (Unconsciousness)

- Severity 12 (60 days): Consciousness 0% max (Death)

- Go-juice addiction factor: x0%

- Teetotalers can take the required drug without penalties. However, ideoligions against drug use will apply the −15 Used drug moodlet.

- Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

+4

1

Wake-up dependency

Carriers of this gene need to ingest wake-up on a regular basis to survive. After 5 days without wake-up, carriers will suffer from wake-up deficiency. After 30 days, they will fall into a coma. After 60 days, they will die.
 
- Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking wake-up.
- Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85

- Severity 1 (5 days): Consciousness 70% max, Moving 80% max, Manipulation 50% max.

- Severity 6 (30 days): Consciousness 10% max (Unconsciousness)

- Severity 12 (60 days): Consciousness 0% max (Death)

- Wake-up addiction factor: x0%

- Teetotalers can take the required drug without penalties. However, ideoligions against drug use will apply the −15 Used drug moodlet.

- Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

+4

1

-

Removed genes[edit]

This table contains genes that are no longer found as-is in the current game version. They may have been removed or migrated in an update, or cut during development before a release.

- 
Click to 

Name

Description

Removed

Reason

Resurrect

Carriers have a reserve of unique resurrector archites which can infuse a corpse, rebuild degenerated tissue and kickstart the vital processes. This brings the dead back to life - though possibly with health issues. This can only be done very rarely, and comes at a steep hemogen cost.

- Requires Hemogenic

- Adds ability: Resurrect

Use archites in the bloodstream to infuse a corpse's body with new life, repairing degenerated cell structures and kickstarting vital functions. The older and worse-preserved the corpse is, the more likely it is that they will come back with memory loss or health conditions. This ability seems to exhaust the archites somehow, so it can only be used very rarely.
- Resurrects the targeted corpse, similarly to Resurrector mech serum

- Target: Any non-mechanoid corpse

- Warmup Time: 2&#160;ticks (0.03&#160;secs)

- Cooldown: 6,840,000&#160;ticks (1.9&#160;years) to 7,560,000&#160;ticks (2.1&#160;years)

- Charges: 1

- AI Can Use: False

- Market value of genepacks containing this gene: ×150%

0

4

1

Before Biotech DLC release

Unknown.

Skill apathy

The carrier will have no passion in (skill).

2

1

-

Before Biotech DLC release

From an XML comment:
"Removed since the downsides are too easy and boring to avoid, and synergize with skill loss genes too much. If you already aren't using the skill it's too easy to just kill passion on it too. -Ty"

Drug addict-sensitive

Carriers of this gene get addicted to (drug) very easily.
- Specific drug addiction factor: x9999%

2

1

-

Before Biotech DLC Release

From an XML comment:
"Removed since these just aren't very interesting, very narrow in application, and the downsides are too easy and boring to avoid. Just not much interaction or story here. -Ty"

Notes[edit]

- Certain genes will not be properly negated by other genes. For example, a drug dependency germline gene, while appearing to be negated by the same drug dependency as a xenogene, will instead cause the negative mood from the lack of the drug to start at 2.5 days instead of at 5 days.

Version history[edit]

- Biotech DLC Release - Added.

- 1.4.3524 - Children no longer get adult body types from genes.

- 1.4.3525 - Fix: Suppressed genes contributing to romance chance still apply. Fix: Attempting to absorb a xenogerm of your own colonist displays a warning message saying you'll anger your faction.

- 1.4.3527 - Fix: Never sleep xenohumans still rest when caravanning alone.

- 1.4.3530 - Fix: Removing passion-adding genes doesn't revert effect. Fix: Psychically bonded pawns in the same caravan still get "psychic bond distance" mood malus in some circumstances.

- 1.4.3531 - Fix: AI sanguophages can use longjump without any remaining hemogen. Increase the effect of the temperature genes. From 3/?[Value?]/10 to 5/10/20. Fix: Some hemogenic abilities can be queued without enough hemogen.

- 1.4.3534 - Fix: Melanin genes can be extracted by gene extractor. Reduced volume and frequency of yttakin sounds.

- 1.4.3541 - Fix: Victims of bloodfeeder bites can gain hemogen from the interaction.

- 1.4.3542 - Fix: Coagulate can still be queued if hemogen is below casting cost.

- 1.4.3555 -
- Psychic bond now gives +10% psychic sensitivity, or +5% if on different maps. Hediff description changed from This person has a psychic bond with another person based on the psychic bonding gene. to This person has a psychic bond with another person based on the psychic bonding gene. The bond itself grants some limited psychic awareness, allowing it to connect even with the psychically deaf. Bonds can now be created during lovin' allowing pawns already in a relationship when the gene was implanted to bond.

- Many genes now give direct boosts instead of forcing traits, which allows genes and traits to stack:
- Depressive gene renamed to Very unhappy, no longer forces Depressive trait instead decreases mood by −10. Pessimist gene renamed to Unhappy, no longer forces Pessimist trait instead decreases mood by −5. Optimist gene renamed to Happy, no longer forces Optimist trait instead increases mood by +5. Sanguine gene renamed to Very happy, no longer forces Sanguine trait instead increases mood by +10.

- Slow runner no longer forces Slowpoke trait instead decreases move speed by −0.2 c/s. Fast runner no longer forces Fast walker trait instead increases move speed by +0.2 c/s. Very fast runner no longer forces Jogger trait instead increases move speed by +0.4 c/s.

- Slow learner renamed to Slow study, no longer forces Slow learner trait instead multiplies Global Learning Factor ×50%. Fast learner renamed to Quick study, no longer forces Fast learner trait instead increases Global Learning Factor +50%.

- Staggeringly ugly gene renamed to Very unattractive, no longer forces Staggeringly ugly trait instead decreases beauty by −2. Ugly gene renamed to Unattractive, no longer forces Ugly trait instead decreases beauty by −1. Pretty gene renamed to Attractive, no longer forces Pretty trait instead increase beauty by +1. Beautiful gene renamed to Very attractive, no longer forces Beautiful trait instead increase beauty by +2.

- <Drug> addict-resist genes renamed to <Drug> resistant, Addiction-resistant genes for alcohol, smokeleaf and psychite provide a 50% reduction in tolerance buildup. Addiction-resistant genes for psychite, wake-up and go juice have a 50% multiplier on overdose chance. Smokeleaf and Alcohol resistant metabolism cost reduced from −2 to −1.

- <Drug> addict-immune genes renamed to <Drug> impervious. Addiction-immune genes for psychite, wake-up and go juice grants immunity to overdoses from the drug. Addiction-immune genes for alcohol, smokeleaf and psychite provides a 100% reduction in tolerance buildup. Smokeleaf and Alcohol impervious metabolism cost reduced from −5 to −3.

- Smokeleaf and Alcohol dependency metabolism gain reduced from +4 to +3.

- Fix: Remove reference to damage over time in acid spray ability description. [...] stick to targets and burn them over time. to [...] stick to targets and burn them.

- Furskin and beardless genes are now mutually exclusive.

- Buffed furry tail minimum comfy temperature offset from −5&#160;°C (−9&#160;°F) to −10&#160;°C (−18&#160;°F).

- When a deathless pawn takes damage that would have been lethal and falls into a deathrest coma instead, as an additional consequence they lose 3-6% of XP in a random skill. This should make non-death less trivial for these characters and preserve the sense of risk and danger. We’ll tuned this ongoing as needed.

- Fix: Bloodfeed can be used on pawns in mental states.

- 1.4.3557 - Slow study gene applies a ×50% factor to Global Learning Factor instead of a −50% offset.

- 1.4.3563 - Fix: Pawns with "dead calm" gene can get into fights over botched conversion attempts. Fix: Genes that remove all passions don't save previous values, causing passions to reset on removal. Fix: Pawns being carried by other pawns strains psychic bond.

- 1.4.3580 - Fix: Furskin_Average3 head uses the wrong graphic. Fix: Tattoos render below heavy brow. Fix: Furskin gene hair/fur color not staying when implanted with a skin color xenogene. Fix: Exception trying to visit sick pawn with neversleep gene.

- 1.4.3613 - Fix: Reimplant ability not working with custom xenotypes.

- 1.4.3641 - Fix: Inactive sterile gene affects fertility.

- 1.4.3682 - Arresting dead calm pawns now never fails, to prevent them going berserk.

- 1.5.4062 -
- Made psychic bond distance thought more permissive. As long as both pawns are on the same map and not suspended (cryptosleep casket) they get the positive thought.

- Remove reference to damage over time in acid spray gene description. ("...it will stick to enemies and burn them over time." to "...it will stick to enemies and burn them.")

- Added more acid filth texture options for acid spray so it never looks tiled.

- Attached helpful text to mouse when selected pawn is aiming animal warcall ability.

- Updated fire spew LOS highlighting.

- Updated psychic bonding hediff tooltip to factor in pawns contained in buildings.

- Clarify that pawns with no xenogenes cannot implant their xenogerm into another person. Show correct warning message on attempt.

- Fix: Pawns with genetic drug needs aren't getting mothballed. Can improve performance in late-game saves.

- Fix: Chemical genes affect tolerance buildup and addiction chance of all chemicals, not just the specified one.

- Fix: On colonist selection, wasters and hussars are currently generating without their drug dependencies.

- Fix: Small increments of pawn speed differences are lost due to integer calculations. Very quick and quick genes were effectively the same on an otherwise unmodified pawn.

- Fix: Drug dependency endogenes aren't properly being overridden by other drug-related xenogenes of the same chemical.

- Fix: Psychic bonds can form between two pawns that have the psychic bonding genes even if they are bonded to other people.

- Fix: Pawns still carry a weapon after getting incapable of violence gene.

- Fix: Pawns incapable of violence still can use combat gene abilities

- Fix: Fire spew can shoot through walls.

- Fix: Fire spew ability not leaning like other ranged attacks.

- Fix: Fire spew ability can't target walls.

- Fix: Perfect immunity doesn't block gut worms or muscle parasites.

- 1.6.4518 - Added 2 new genes: Indoor dweller (Disables the outdoors need) and webbed phalanges (Ignores movement speed penalties from water terrain Decreases manipulation by 5%). The former is added to dirtmoles, resulting in complexity increasing from 9 -> 10, Net metabolism decreasing from +1 -> 0, hunger rate increasing from 90% -> 100%.

- 1.6.4535 - Made the breathless gene suppress the normal vacuum resistant gene, removing its metabolic impact.

- 1.6.4566 - Rebalanced the starjack xenotype, added the Low gravity adapted gene. Removed Awful plants, replaced Poor melee with Awful melee and replaced Cold tolerant with Cold super-tolerant. Net metabolism decreasing from +1 -> 0, hunger rate increasing from 90% -> 100%. Breathless and Vacuum resistant now grants Minimum Comfortable Temperature: −5&#160;°C (9&#160;°F)

- 1.6.4850 -
- Fix: Pawns can infinitely desire a looks-change if their ideoligion and genes clash.

- Fix: Having an endogene and an overriding xenogene with the same trait can cause the trait to never be applied at all.

Biotech (DLC) 

Families
Relationships (Reproduction &#8226; Children)
Life stages (Babies &#8226; Children &#8226; Adults)
Furniture (Crib &#8226; Baby sleeping spot &#8226; Growth vat &#8226; Toy box &#8226; Baby decoration &#8226; School desk &#8226; Blackboard)

Mechanoids
Laborers (Agrihand &#8226; Cleansweeper &#8226; Constructoid &#8226; Fabricor &#8226; Lifter &#8226; Paramedic &#8226; Tunneler)
Combatants (Centurion &#8226; Legionary &#8226; Militor &#8226; Scorcher &#8226; Tesseron)
Commanders (Apocriton &#8226; Diabolus &#8226; War queen &#8226; War urchin)
Mechanitors
Control (Mechlink &#8226; Band node &#8226; Mech boosters &#8226; Mech signallers &#8226; Control pack &#8226; Airwire headset)
Mechanoid creation (Basic subcore &#8226; Standard subcore &#8226; High subcore &#8226; Subcore encoder &#8226; Subcore softscanner &#8226; Subcore ripscanner &#8226; Mech gestator)
Maintenance (Mech recharger)
Genetics
Xenohumans (Dirtmoles &#8226; Genies &#8226; Highmates &#8226; Hussars &#8226; Impids &#8226; Neanderthals &#8226; Pigskins &#8226; Sanguophages &#8226; Wasters &#8226; Yttakin &#8226; Starjack) 
Genes Germline &#8226; Xenogene &#8226; Metabolic efficiency
Genetic Modification Genepack &#8226; Gene extractor &#8226; Gene bank &#8226; Gene assembler &#8226; Gene processor &#8226; Xenogerm &#8226; Archite capsules
Deathrest (Deathrest accelerator &#8226; Deathrest capacity serum &#8226; Deathrest casket &#8226; Glucosoid pump &#8226; Hemogen amplifier &#8226; Hemopump &#8226; Psychofluid pump)
Pollution
Nature (Toxalope &#8226; Toxipotato plant &#8226; Waste rat &#8226; Gray pine tree &#8226; Pebble cactus &#8226; Rat palm tree &#8226; Witchwood tree &#8226; Stasis cocoon)
Mitigation (Wastepacks &#8226; Atomizers &#8226; Pollution pumps &#8226; Polux trees)
Adaptation Face mask &#8226; Gas mask &#8226; Tox grenades &#8226; Tox pack &#8226; Tox shell &#8226; Toxic needle gun &#8226; Toxbomb launcher &#8226; Detoxifier kidney &#8226; Detoxifier lung
Nonchalance Toxifier generator

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Genes&oldid=184104#Robust"

 Categories: - Biotech
- Pages to be recoded
- Stubs
- Game mechanics

Hidden categories: - Pages that need fact checking
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

 
 

 

 
 - This page was last edited on 24 September 2026, at 15:24.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -