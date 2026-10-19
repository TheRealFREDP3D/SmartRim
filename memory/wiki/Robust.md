# Genes

From RimWorld Wiki

(Redirected from [Robust](/index.php?title=Robust&redirect=no "Robust"))

Jump to navigation Jump to search

[![BiotechIcon.png](/images/thumb/7/73/BiotechIcon.png/40px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)") | **This article relates to content added by[Biotech (DLC)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
[![AncientTerminal east.png](/images/thumb/0/02/AncientTerminal_east.png/40px-AncientTerminal_east.png)](/wiki/Category:Pages_to_be_recoded "Category:Pages to be recoded") | This page has been suggested for [recoding](/wiki/Category:Pages_to_be_recoded "Category:Pages to be recoded"). **Reason:** _Thought templates_. You can help RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Genes&action=edit)** it.  
---|---  
  
This page is a list of genes. For a full explanation of the gene system see: [Genetics](/wiki/Genetics "Genetics")

**Genes** are a system for modifying [human](/wiki/Human "Human") pawns, added by the [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC"). They can be obtained from character creation or implanted via [xenogerms](/wiki/Xenogerm "Xenogerm"). 

## Contents

  * 1 Mechanics
  * 2 Gene expression
  * 3 Work Required
  * 4 Archite
  * 5 Special abilities
  * 6 Hemogen
  * 7 Health
  * 8 Psychics
  * 9 Movement
  * 10 Mood
  * 11 Temperature
  * 12 Resistance and sensitivity
  * 13 Violence
  * 14 Sleep
  * 15 Pain
  * 16 Reproduction
  * 17 Beauty
  * 18 Cosmetic
    * 18.1 Body type
    * 18.2 Hair
    * 18.3 Melanin
    * 18.4 Skin
  * 19 Miscellaneous
  * 20 Aptitudes
  * 21 Drugs
  * 22 Removed genes
  * 23 Notes
  * 24 Version history



## Mechanics[[edit](/index.php?title=Genes&action=edit&section=1 "Edit section: Mechanics")]

Genetics are limited by metabolic efficiency, denoted by the [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") symbol. This affects pawns' [hunger rate](/wiki/Hunger_rate "Hunger rate"). Harmful genes improve metabolic efficiency, lowering hunger rate, and thus consuming less food overall. Helpful genes lower metabolic efficiency, getting hungry faster. A baseline human has a metabolic efficiency of 0 (100% hunger rate), and genes can bring it as low as -5 (225% hunger rate) or up to 5 (50% hunger rate). The game will not allow the creation of xenogerms with a metabolic efficiency lower than -5. 

Note that genes with over [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") 5 cannot be extracted by themselves, and must be extracted in a pack with another gene that lowers metabolism cost. 

Complexity, denoted by the [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") symbol, affects how many [gene processors](/wiki/Gene_processor "Gene processor") you need to create a [xenogerm](/wiki/Xenogerm "Xenogerm") from a set of genes. A [gene assembler](/wiki/Gene_assembler "Gene assembler") can create xenogerms with a maximum complexity of 6, plus 2 for every attached gene processor. Complexity also determines the base time it takes to create the xenogerm, ranging from 4 hours at ≤3 complexity, to 23 hours at ≥20 complexity (which is then scaled by the [research speed](/wiki/Research_speed "Research speed") of whoever operates the gene assembler). 

## Gene expression[[edit](/index.php?title=Genes&action=edit&section=2 "Edit section: Gene expression")]

When looking at a pawn's gene tab, each gene can be considered to be in one of three categories: 

  * [![GeneBackground Endogene.png](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png) Germline Genes
  * [![GeneBackground Xenogene.png](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png) Xenogenes
  * [![GeneBackground ArchiteGene.png](/images/thumb/6/66/GeneBackground_ArchiteGene.png/32px-GeneBackground_ArchiteGene.png)](/wiki/File:GeneBackground_ArchiteGene.png) Archite genes



Germline genes are freely distributed through and only through [reproduction](/wiki/Reproduction "Reproduction"). Xenogenes are genes that have been [surgically implanted](/wiki/Operation "Operation") through a xenogerm, and can override germline genes that are identical to or conflict with the xenogene; a [Dirtmole](/wiki/Dirtmole "Dirtmole") that was converted into a [Sanguophage](/wiki/Sanguophage "Sanguophage") will have half of their genes overwritten by the Sanguophage xenotype. Xenogerms cannot be passed through reproduction. 

Note that germline and xenogenes are determined by the way they are obtained, not by the effects of the gene itself. For example, there is only one [fire resistant](/wiki/Fire_resistant "Fire resistant") gene coded into the game - "germline fire resistant" and "xenogene fire resistant" are the same gene obtained in different ways. Trying to have both would simply disable the redundant germline version. 

Archite genes are non-inheritable (even if they are forced into the germline of a [custom xenotype](/wiki/Xenotypes#Customization "Xenotypes")) and xenogerms containing them must be supplied with the requested number of [archite capsules](/wiki/Archite_capsules "Archite capsules") before being assembled. Archite genes cannot extracted through the [gene extractor](/wiki/Gene_extractor "Gene extractor"), but can be implanted using the [gene implanter](/wiki/Gene_implanter "Gene implanter") ability. 

## Work Required[[edit](/index.php?title=Genes&action=edit&section=3 "Edit section: Work Required")]

The work required to create a xenogerm is determined by its [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity"). First, a base value is obtained from the post-process curve with the points: 

     Xenogerm work   
---  
  
  * (0, 3)
  * (4, 5)
  * (8, 8)
  * (12, 12)
  * (16, 17)
  * (20, 23)

|   
  
This value is then multiplied by 2500 to obtain the final number. 

     Xenogerm work   
---  
  
  * (0, 7500)
  * (4, 12500)
  * (8, 20000)
  * (12, 30000)
  * (16, 42500)
  * (20, 57500)

|   
  
The actual time required is inversely proportional with the [research speed](/wiki/Research_speed "Research speed") of whoever operates the gene assembler. At 100% research speed, it takes between 7,500 [ticks](/wiki/Time "Time") (2.08 mins) (for 0 complexity) to 57,500 [ticks](/wiki/Time "Time") (15.97 mins) (for complexity 20 and above). 

## Archite[[edit](/index.php?title=Genes&action=edit&section=4 "Edit section: Archite")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Archite capsules](/images/thumb/9/90/Archite_capsule_required.png/20px-Archite_capsule_required.png)](/wiki/File:Archite_capsule_required.png "Archite capsules") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---|---  
Scarless  
[![Gene TotalHealing.png](/images/thumb/6/60/Gene_TotalHealing.png/64px-Gene_TotalHealing.png)](/wiki/File:Gene_TotalHealing.png) | _Carriers of this gene have a special type of regenerator cell which can heal old wounds and chronic illnesses like bad back._

* * *

  * Prevents new [scars](/wiki/Scar "Scar") from forming, even from brain damage.
  * Heals 1 scar, permanent injury, or [chronic condition](/wiki/Ailments#Chronic "Ailments") ([Alzheimer's](/wiki/Alzheimer%27s "Alzheimer's"), [asthma](/wiki/Asthma "Asthma"), [bad back](/wiki/Bad_back "Bad back"), [cataracts](/wiki/Cataract "Cataract"), [carcinoma](/wiki/Carcinoma "Carcinoma"), [dementia](/wiki/Dementia "Dementia"), [frail](/wiki/Frail "Frail"), [hearing loss](/wiki/Hearing_loss "Hearing loss"), [blindness](/wiki/Blindness "Blindness"), and [organ decay](/wiki/Organ_decay "Organ decay")) every 15-30 days, akin to (and alongside) [luciferium](/wiki/Luciferium "Luciferium"). Includes scars from a scarification [ritual](/wiki/Ritual "Ritual").[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")
    * Will _not_ automatically heal [trauma savant](/wiki/Trauma_savant "Trauma savant") conditions.

| **0** | 4 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Gene implanter  
[![Gene XenogermReimplanter.png](/images/thumb/e/eb/Gene_XenogermReimplanter.png/64px-Gene_XenogermReimplanter.png)](/wiki/File:Gene_XenogermReimplanter.png) | _Carriers of this gene can implant a copy of their xenogerm into another person through a somewhat gross-looking injector organ. Their own genetic material will then regrow very slowly. If they implant while their genes are regrowing, they will die._

* * *

  * Adds ability: [![Gene XenogermReimplanter.png](/images/thumb/e/eb/Gene_XenogermReimplanter.png/16px-Gene_XenogermReimplanter.png)](/wiki/File:Gene_XenogermReimplanter.png) Implant Genes



    _Implant this person's xenogenes into a willing subject using a special injector organ. If this person's genes are currently regrowing, they will implant their xenogerm and die in the process. When implanted, a xenogerm will overwrite the target's xenogenes. Germline genes will be unaffected._

  * Passes on a copy of all xenogenes to a target. Both pawns will start regrowing genes for a [period of around 2 years](/wiki/Time "Time"). The pawn that implants the genes will suffer [gene loss shock](/wiki/Hediffs/Biotech/Various/Gene_loss_shock "Hediffs/Biotech/Various/Gene loss shock") for 2 days as well. The pawn receiving the xenogerm will be put into [xenogermination coma](/wiki/Hediffs/Biotech/Various/Xenogermination_coma "Hediffs/Biotech/Various/Xenogermination coma") for a flat 2 days.
  * Using this ability while genes are regrowing will kill the caster and remove all of their xenogenes.
  * Cannot target a hostile pawn unless they are [downed](/wiki/Downed "Downed").
  * Cannot target members of a temporary faction, even if they are downed. This can be worked-around by [imprisoning](/wiki/Prisoner "Prisoner") the pawn then [enslaving](/wiki/Slavery "Slavery") or recruiting them, which changes their faction.
  * The caster must have xenogenes, and the target must be of a different [xenotype](/wiki/Xenotype "Xenotype").
  * If the target's [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") includes one or more [xenotype preferences](/wiki/Ideoligion#Xenotype_preferences "Ideoligion"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") the caster's xenotype must match one of target's preferred types. This restriction applies even if the target is downed, enslaved or imprisoned.
  * If the caster has the bloodfeeder gene, they cannot target a pawn whose [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") includes the [Bloodfeeders: Reviled](/wiki/Bloodfeeders_\(precept\) "Bloodfeeders \(precept\)")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") precept. This restriction applies even if the target is downed.


| **0** | 3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Perfect immunity  
[![Gene PerfectImmunity.png](/images/thumb/d/d1/Gene_PerfectImmunity.png/64px-Gene_PerfectImmunity.png)](/wiki/File:Gene_PerfectImmunity.png) | _Carriers of this gene have archite-enhanced immune systems which intelligently destroy invaders. They are totally immune to most normal illnesses._

* * *

  * Immunity to [flu](/wiki/Flu "Flu"), [malaria](/wiki/Malaria "Malaria"), [sleeping sickness](/wiki/Sleeping_sickness "Sleeping sickness"), [plague](/wiki/Plague "Plague"), [infection](/wiki/Infection "Infection"), [lung rot](/wiki/Lung_rot "Lung rot"), [gut worms](/wiki/Gut_worms "Gut worms"), [muscle parasites](/wiki/Muscle_parasites "Muscle parasites"), and [organ decay](/wiki/Organ_decay "Organ decay"). This includes all the [diseases](/wiki/Disease "Disease") that are fatal and that adult colonists can acquire. 
    * Despite the description, it only prevents new illnesses. It does _not_ affect pre-existing conditions nor boost [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed").
    * Note: Does _not_ prevent [food poisoning](/wiki/Food_poisoning "Food poisoning").

| **0** | 3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Immunity   
Non-senescent  
[![Gene NonSenescent.png](/images/thumb/9/9f/Gene_NonSenescent.png/64px-Gene_NonSenescent.png)](/wiki/File:Gene_NonSenescent.png) | _Carriers of this gene do not go through senescence in the normal way. They never get chronic age-related diseases like cancer, bad back, cataracts, or dementia._

* * *

  * Total immunity to [carcinoma](/wiki/Carcinoma "Carcinoma"), [heart attack](/wiki/Heart_attack "Heart attack"), and [chronic conditions](/wiki/Ailments#Chronic "Ailments") ([Alzheimer's](/wiki/Alzheimer%27s "Alzheimer's"), [Asthma](/wiki/Asthma "Asthma"), [Artery blockage](/wiki/Artery_blockage "Artery blockage"), [Bad back](/wiki/Bad_back "Bad back"), [Cataracts](/wiki/Cataract "Cataract"), [Dementia](/wiki/Dementia "Dementia"), [Frail](/wiki/Frail "Frail"), but not [Hearing loss](/wiki/Hearing_loss "Hearing loss")). 
    * Prevents these conditions from any source, not just aging. (e.g. [nuclear stomach](/wiki/Nuclear_stomach "Nuclear stomach"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [toxic buildup](/wiki/Toxic_buildup "Toxic buildup"))
    * Does _not_ affect pre-existing conditions.

| **0** | 3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Ageless  
[![Gene Ageless.png](/images/thumb/2/27/Gene_Ageless.png/64px-Gene_Ageless.png)](/wiki/File:Gene_Ageless.png) | _Carriers of this gene have archites in the bloodstream which continuously reverse the process of aging. Starting at the age of 13, carriers begin to biologically age slower. By 18, the aging process stops completely._

* * *

  * Aging ×1 at age 13 or lower. Rate linearly slows as the pawn gets older.
  * Aging ×0 at age 18.5 or higher.

| **0** | 3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Deathless  
[![Gene Deathless.png](/images/thumb/8/87/Gene_Deathless.png/64px-Gene_Deathless.png)](/wiki/File:Gene_Deathless.png) | _Carriers of this gene have archites in the blood which will sustain their life processes no matter what. As long as the brain remains intact, a carrier of this gene will never die._

* * *

  * If a pawn would've died, but the brain, head, or neck is not directly destroyed, they enter into either a regenerative coma or involuntary deathrest. 
    * Pawns without the Deathrest gene enter a regenerative coma. After all fatal conditions are removed, the regenerative coma lasts for 7 more days. [Hemogen](/wiki/Hemogen "Hemogen") is unaffected.
    * Pawns with the Deathrest gene enter involuntary [deathrest](/wiki/Deathrest "Deathrest") and lose all [Hemogen](/wiki/Hemogen "Hemogen"). After fatal conditions are removed, the usual deathrest mechanics take place.
    * Does not regenerate limbs or organs, except for the torso.
    * Entering the regeneration coma or involuntary deathrest will cause the pawn to lose 3% to 6% of total [skill](/wiki/Skill "Skill") XP in a random skill.
  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×200% (also multiplied by the usual ×400% for 1 Archite capsule)

| **0** | 7 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Archite metabolism  
[![Gene ArchiteMetabolism.png](/images/thumb/a/a6/Gene_ArchiteMetabolism.png/64px-Gene_ArchiteMetabolism.png)](/wiki/File:Gene_ArchiteMetabolism.png) | _Carriers of this gene have special archites in their cells that facilitate and optimize metabolism. This improves overall genetic and metabolic quality._

* * *

  * Increases metabolic efficiency by 6. No other effect.
  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×150% (also multiplied by ×700% for 2 Archite capsules)

| +6 | 6 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Breathless[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")  
[![Gene Breathless.png](/images/thumb/3/3c/Gene_Breathless.png/64px-Gene_Breathless.png)](/wiki/File:Gene_Breathless.png) | _Carriers of this gene can store concentrated oxygen in their bodies. Their cells consume much less oxygen, meaning they rarely need to breathe. These adaptations make them immune to the harmful effects of space, as well as environmental toxins, tox gas, acidic smog, and rot stink._

* * *

  * [Vacuum resistance](/wiki/Vacuum_resistance "Vacuum resistance"): +100%
  * [Toxic Environment Resistance](/wiki/Toxic_Environment_Resistance "Toxic Environment Resistance"): +100%
  * Immunity to [vacuum burns](/wiki/Vacuum_burn "Vacuum burn"), [tox gas](/wiki/Tox_gas "Tox gas"), [acidic smog](/wiki/Acidic_smog "Acidic smog"), and [rot stink](/wiki/Rot_stink "Rot stink").
  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −5 °C (9 °F)

| **0** | 3 | 1 |  | ToxicEnvironmentResistance VacuumResistance   
  
## Special abilities[[edit](/index.php?title=Genes&action=edit&section=5 "Edit section: Special abilities")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Genes&action=edit). Reason:** _Acid spray has AP and its own Damage type etc. Further mechanical detail including how it works, what armor it opposes etc is needed._  
---|---  
  
* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes")  
---|---|---|---|---  
Fire spew  
[![Gene Firespew.png](/images/thumb/e/eb/Gene_Firespew.png/64px-Gene_Firespew.png)](/wiki/File:Gene_Firespew.png) | _Carriers are able to spew flammable bile generated by a special organ in their neck. The bile sticks to anything in a small area and can ignite people, objects, and the ground._

* * *

  * Adds ability: [![FireSpew.png](/images/thumb/c/cb/FireSpew.png/16px-FireSpew.png)](/wiki/File:FireSpew.png) Fire spew



    _Spit a stream of sticky, flammable bile from the mouth. The bile can ignite anything or anyone it hits, and also form flaming pools on the ground. The bile is generated and stored by an organ in the neck, along with a separate pouch of hypergolic reactant for ignition._

  * Spits flammable liquid in a 7.9 tile triangle with a 3 tile wide end.[Detail Needed]
  * Target: Pawn or Location
  * Warmup Time: 60 [ticks](/wiki/Time "Time") (1 sec)
  * Cooldown: 300,000 [ticks](/wiki/Time "Time") (5 in-game days)
  * Charges: 1
  * AI Can Use: True. Note: AI will still target fire-immune targets.



  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×150%

| −2 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids")  
Foam spray  
[![Gene FoamSpray.png](/images/thumb/e/e6/Gene_FoamSpray.png/64px-Gene_FoamSpray.png)](/wiki/File:Gene_FoamSpray.png) | _Carriers grow glands in the neck that generate and store a fire-retardant foam. They can spew this foam over an area to extinguish fires._

* * *

  * Adds ability: [![Gene FoamSpray.png](/images/thumb/e/e6/Gene_FoamSpray.png/16px-Gene_FoamSpray.png)](/wiki/File:Gene_FoamSpray.png) Foam spray



    _Spray thick fire-retardant foam from glands in the neck up through the mouth. The foam will cover a small area and extinguish any fire it touches._

  * Spits firefoam in a 3x3 area around the target, up to 4 tiles away. This leaves [firefoam](/wiki/Firefoam "Firefoam") filth on the ground, extinguishing fires and preventing new ones from igniting.
  * Target: Pawn or Location
  * Warmup Time: 60 [ticks](/wiki/Time "Time") (1 sec)
  * Cooldown: 30,000 [ticks](/wiki/Time "Time") (12 in-game hours) for all 3 charges. Cooldown will not begin until all charges have been expended.
  * Charges: 3
  * AI Can Use: False.


| −2 | 1 | \-   
Animal warcall  
[![Gene AnimalWarcall.png](/images/thumb/3/31/Gene_AnimalWarcall.png/64px-Gene_AnimalWarcall.png)](/wiki/File:Gene_AnimalWarcall.png) | _Carriers of this gene can perform an animal warcall, using a powerful bellow and psychic connection to call an animal to fight for them._

* * *

  * Adds ability: [![AnimalWarcall.png](/images/thumb/4/4b/AnimalWarcall.png/16px-AnimalWarcall.png)](/wiki/File:AnimalWarcall.png) Animal warcall



    _With a powerful bellow and psychic connection, call an animal to fight your enemies for a few hours._

  * Turns the target berserk against all factions hostile to the caster for 12 in-game hours/30,000 [ticks](/wiki/Time "Time") (8.33 mins). -75 base goodwill when used on a friendly [faction](/wiki/Faction "Faction")'s animal.
  * Target: Any single [animal](/wiki/Animal "Animal") or [wildman](/wiki/Wildman "Wildman"). Does not require [LoS](/wiki/LoS "LoS") [Detail]
  * Range: 49.9 tiles
  * Warmup Time: 120 [ticks](/wiki/Time "Time") (2 secs)
  * Cooldown: 900,000 [ticks](/wiki/Time "Time") (15 in-game days) per charge.
  * Charges: 2
  * AI Can Use: True


| −3 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")  
Acid spray  
[![Gene AcidSpray.png](/images/thumb/5/57/Gene_AcidSpray.png/64px-Gene_AcidSpray.png)](/wiki/File:Gene_AcidSpray.png) | _Carriers grow glands in the neck that generate and store a sticky acid substance, along with acid-tolerant tissues in the mouth. They can spew this acid over an area, where it will stick to enemies and burn them._

* * *

  * Adds ability: [![AcidSpray.png](/images/thumb/f/f3/AcidSpray.png/16px-AcidSpray.png)](/wiki/File:AcidSpray.png) Acid spray



    _Spray a sticky acid substance from glands in the neck up through the mouth and all over the target area. The acid will stick to targets and burn them._

  * Spits a fast-moving acid projectile in a 3x3 area around the target. This does 30 damage to buildings and items, and creates a harmless "spent acid" filth on each affected tile. Creatures in the affected area suffer a 30 damage burn (possibly spread over multiple body parts), but suffer no persistent damage over time. The attack has an AP of 80%[Armor type?] and a [stopping power](/wiki/Stopping_power "Stopping power") of 1.
  * Target: Pawn or Location
  * Range: 8.9 tiles
  * Warmup Time: 30 [ticks](/wiki/Time "Time") (0.5 secs)
  * Cooldown: 30,000 [ticks](/wiki/Time "Time") (12 in-game hours)
  * Charges: 1
  * AI Can Use: True.



  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×150%

| −2 | 1 | \-   
  
## Hemogen[[edit](/index.php?title=Genes&action=edit&section=6 "Edit section: Hemogen")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | Prereq.  | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes")  
---|---|---|---|---|---  
Hemogenic  
[![Gene Hemogenic.png](/images/thumb/4/49/Gene_Hemogenic.png/64px-Gene_Hemogenic.png)](/wiki/File:Gene_Hemogenic.png) | _Carriers of this gene have a reserve of biological strength powered by a resource called hemogen. The resource can be gained and spent in various ways, all of which are unlocked by other genes. Carriers lose 2 hemogen per day from biological entropy._

* * *

  * Creates a [Hemogen](/wiki/Hemogen "Hemogen") need, which decreases by −2 per day. 
    * Increases by +20 per [hemogen pack](/wiki/Hemogen_pack "Hemogen pack") or Bloodfeed.
  * Receive _Hemogen Craving_ [ailment](/wiki/Ailment "Ailment") when Hemogen hits 0.   
Craving severity increases by 5% / hour with 0 hemogen. Severity decreases by 10% / hour with it. 
    * Hemogen Craving (minor, 0%): −10 [mood](/wiki/Mood "Mood"), [Consciousness](/wiki/Consciousness "Consciousness") max 90%, +5% [Pain](/wiki/Pain "Pain")
    * Hemogen Craving (moderate, 35%): −15 [mood](/wiki/Mood "Mood"), [Consciousness](/wiki/Consciousness "Consciousness") max 80%, +10% [Pain](/wiki/Pain "Pain")
    * Hemogen Craving (major, 70%): −20 [mood](/wiki/Mood "Mood"), [Consciousness](/wiki/Consciousness "Consciousness") max 50%, +15% [Pain](/wiki/Pain "Pain")

| +1 | 1 | \-  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Hemogen drain  
[![Gene HemogenDrain.png](/images/thumb/4/4b/Gene_HemogenDrain.png/64px-Gene_HemogenDrain.png)](/wiki/File:Gene_HemogenDrain.png) | _Carriers lose an additional 8 hemogen per day from biological entropy._

* * *

  * −8 [Hemogen](/wiki/Hemogen "Hemogen") per day.

| +6 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Coagulate  
[![Gene Coagulate.png](/images/thumb/f/fb/Gene_Coagulate.png/64px-Gene_Coagulate.png)](/wiki/File:Gene_Coagulate.png) | _Carriers of this gene have special glands on their hands and wrists, as well as a unique salivary compound that they can use to rapidly tend wounds._

* * *

  * Adds ability: [![Gene Coagulate.png](/images/thumb/f/fb/Gene_Coagulate.png/16px-Gene_Coagulate.png)](/wiki/File:Gene_Coagulate.png) Coagulate



    _Use special glands in the wrists to quickly tend someone's wounds._

  * Tends wounds at 40-80% [tend quality](/wiki/Tend_quality "Tend quality").
  * Target: Single target in [LoS](/wiki/LoS "LoS")
  * Range: 3.9 tiles
  * Warmup Time: 60 [ticks](/wiki/Time "Time") (1 sec)
  * [Hemogen](/wiki/Hemogen "Hemogen") Cost: 20
  * AI Can Use: ?


| −1 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Bloodfeeder  
[![Gene Bloodfeeder.png](/images/thumb/0/0c/Gene_Bloodfeeder.png/64px-Gene_Bloodfeeder.png)](/wiki/File:Gene_Bloodfeeder.png) | _Carriers of this gene have small retractable fangs and an organ on the roof of the mouth which can extract hemogen from fresh warm blood. They can bite an unresisting person, suck the blood, and gain hemogen directly._

* * *

  * Adds ability: [![Gene Bloodfeeder.png](/images/thumb/0/0c/Gene_Bloodfeeder.png/16px-Gene_Bloodfeeder.png)](/wiki/File:Gene_Bloodfeeder.png) Bloodfeed



    _Bite the target and extract hemogen directly from their blood. The target will lose blood and will be horrified by the interaction, but will be otherwise unharmed. A fast-acting coagulant will seal the wound to prevent bleeding. Can only target non-hemogenic humans. Hemogen gain is affected by the target’s body size._

  * Feed on a pawn to gain up to +20 [Hemogen](/wiki/Hemogen "Hemogen"), which scales with target body size, but not the user's. 
    * Target will gain +45% [blood loss](/wiki/Blood_loss "Blood loss") and the −5 _Fed on_ [moodlet](/wiki/Mood "Mood") (5 days, doesn't stack, negated by [masochist](/wiki/Masochist "Masochist") trait and [Bloodfeeders](/wiki/Bloodfeeders_\(precept\) "Bloodfeeders \(precept\)") precept.[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")). Also gains a bloodfeeder mark on the neck (+1% [pain](/wiki/Pain "Pain")).
    * If the target does not have enough blood, hemogen gain will be reduced accordingly.[Detail]
    * Bloodfeeder must have a non-0% [Eating](/wiki/Eating "Eating") capacity.
  * Target: Single human target. Target must not have the Bloodfeeder gene. Must be [downed](/wiki/Downed "Downed") or a [colonist](/wiki/Colonist "Colonist"), [slave](/wiki/Slave "Slave"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") or [prisoner](/wiki/Prisoner "Prisoner") not on a [mental break](/wiki/Mental_break "Mental break"). 
    * A warning will be given if it would kill the target or render them unconscious, but it will not account for continuing blood loss.



  * +2 [mood](/wiki/Mood "Mood") when near a [blood torch](/wiki/Blood_torch "Blood torch").



* * *

  * Interaction with [Bloodfeeders](/wiki/Bloodfeeders_\(precept\) "Bloodfeeders \(precept\)") precept.[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")
    * Bloodfeeders: Revered - Believers have a higher [opinion](/wiki/Opinion "Opinion") towards bloodfeeders, negates moodlet for being fed on, mood bonus when bloodfeeders are in the colony or are the [Leader](/wiki/Ideoligion#Leader "Ideoligion"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") and mood penalty when they die.
    * Bloodfeeders: Reviled. - Believers have a lower [opinion](/wiki/Opinion "Opinion") towards bloodfeeders, mood penalty when bloodfeeders are in the colony or when they are bloodfeeder, and mood bonus when they die.

| −1 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Longjump legs  
[![Gene LongJumpLegs.png](/images/thumb/a/a1/Gene_LongJumpLegs.png/64px-Gene_LongJumpLegs.png)](/wiki/File:Gene_LongJumpLegs.png) | _Carriers have special hemogen-powered muscle fibers in their legs which allow them to jump great distances._

* * *

  * Adds ability: [![Longjump.png](/images/thumb/0/0b/Longjump.png/16px-Longjump.png)](/wiki/File:Longjump.png) Longjump



    _Jump to a distant location using super-strong hemogen-powered legs._

  * Jump to the selected location, over non-LoS blocking objects, quickly but not instantly. Immune to all damage during the jump.
  * Target: Location in [LoS](/wiki/LoS "LoS")
  * Range: 19.9 tiles
  * Warmup Time: 30 [ticks](/wiki/Time "Time") (0.5 secs)
  * [Hemogen](/wiki/Hemogen "Hemogen") Cost: 5
  * AI Can Use: True


| −2 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Piercing spine  
[![Gene PiercingSpine.png](/images/thumb/8/8b/Gene_PiercingSpine.png/64px-Gene_PiercingSpine.png)](/wiki/File:Gene_PiercingSpine.png) | _Carriers grow an opening in their upper chest along with a quiver of keratin spines. Using a hemogen-powered chemical reaction, they can fire these spines at high speed at nearby targets with surprising accuracy._

* * *

  * Adds ability: [![PiercingSpine.png](/images/thumb/2/2c/PiercingSpine.png/16px-PiercingSpine.png)](/wiki/File:PiercingSpine.png) Piercing spine



    _Use a hemogenic chemical reaction to launch a bony spine at the target. The spine exits through the skin from an opening between the collarbones. Given the method of launch, it is surprisingly easy to aim._

  * Launches an unerring spine at the target, dealing 30 [RangedStab](/wiki/Damage_Types#RangedStab "Damage Types") damage, with an AP of 100% and a [stopping power](/wiki/Stopping_power "Stopping power") of 1.
  * Target: Single target in [LoS](/wiki/LoS "LoS")
  * Range: 3.9 tiles
  * Warmup Time: 30 [ticks](/wiki/Time "Time") (0.5 secs)
  * Cooldown Time: 60 [ticks](/wiki/Time "Time") (1 sec)
  * [Hemogen](/wiki/Hemogen "Hemogen") Cost: 20
  * AI Can Use: True



  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×150%

| −1 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
Deathrest  
[![Gene Deathrest.png](/images/thumb/6/60/Gene_Deathrest.png/64px-Gene_Deathrest.png)](/wiki/File:Gene_Deathrest.png) | _Carriers of this gene must periodically regenerate themselves in a special coma called deathrest. Deathrest takes days, but can confer substantial bonuses. Deathrest can be accelerated and its effects enhanced by the use of a variety of special buildings and technologies. Those who put off deathresting will suffer from deathrest exhaustion._

* * *

  * Creates a need for [deathrest](/wiki/Deathrest "Deathrest") roughly every 30 days. 
    * Deathrest is initiated at a [bed](/wiki/Bed "Bed") or [deathrest casket](/wiki/Deathrest_casket "Deathrest casket") and prevents action. It lasts for 4 days by default (3.6 days in casket), which can be interrupted for a stat penalty.
    * If need hits 0, maximum [Consciousness](/wiki/Consciousness "Consciousness") set to 50% and [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") -100%.
    * See the [deathrest article](/wiki/Deathrest "Deathrest") for more details.
    * Implanting new xenogerm, even with deathrest gene will reset pawn's deathrest capacity.

| +6 | 1 | Hemogenic  | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")  
  
## Health[[edit](/index.php?title=Genes&action=edit&section=7 "Edit section: Health")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Weak immunity  
[![Gene WeakImmunity.png](/images/thumb/f/f4/Gene_WeakImmunity.png/64px-Gene_WeakImmunity.png)](/wiki/File:Gene_WeakImmunity.png) | _Carriers of this gene gain immunity to diseases more slowly than normal. They may die from infections that others would survive._

* * *

  * [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") ×90%

| +2 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | Immunity   
Strong immunity  
[![Gene StrongImmunity.png](/images/thumb/0/08/Gene_StrongImmunity.png/64px-Gene_StrongImmunity.png)](/wiki/File:Gene_StrongImmunity.png) | _Carriers of this gene gain immunity to diseases faster than normal._

* * *

  * [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") ×110%

| −1 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Immunity   
Super immunity  
[![Gene SuperStrongImmunity.png](/images/thumb/3/35/Gene_SuperStrongImmunity.png/64px-Gene_SuperStrongImmunity.png)](/wiki/File:Gene_SuperStrongImmunity.png) | _Carriers of this gene gain immunity to diseases considerably faster than normal._

* * *

  * [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") ×150%
  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×125%

| −2 | 2 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | Immunity   
Slow wound healing  
[![Gene WoundHealingRateSlow.png](/images/thumb/c/c2/Gene_WoundHealingRateSlow.png/64px-Gene_WoundHealingRateSlow.png)](/wiki/File:Gene_WoundHealingRateSlow.png) | _Carriers of this gene heal from wounds half as fast as normal._

* * *

  * [Injury Healing Factor](/wiki/Injury_Healing_Factor "Injury Healing Factor") ×50%

| +2 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | WoundHealingRate   
Fast wound healing  
[![Gene WoundHealingRateFast.png](/images/thumb/4/45/Gene_WoundHealingRateFast.png/64px-Gene_WoundHealingRateFast.png)](/wiki/File:Gene_WoundHealingRateFast.png) | _Carriers of this gene heal from wounds twice as fast as normal._

* * *

  * Injury Healing Factor ×200%

| −2 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") | WoundHealingRate   
Superfast wound healing  
[![Gene WoundHealingRateSuperfast.png](/images/thumb/0/05/Gene_WoundHealingRateSuperfast.png/64px-Gene_WoundHealingRateSuperfast.png)](/wiki/File:Gene_WoundHealingRateSuperfast.png) | _Carriers of this gene heal from wounds four times as fast as normal._

* * *

  * Injury Healing Factor ×400%
  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×125%

| −3 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | WoundHealingRate   
Superclotting  
[![Gene Superclotting.png](/images/thumb/9/9f/Gene_Superclotting.png/64px-Gene_Superclotting.png)](/wiki/File:Gene_Superclotting.png) | _Carriers of this gene have extra-power coagulating factors in their blood, and will stop bleeding very quickly when wounded._

* * *

  * Every 6 seconds, all bleeding wounds are automatically tended at 20-70% [tend quality](/wiki/Tend_quality "Tend quality"). The exact tend quality is fully random within this range.
  * This renders it functionally impossible for the pawn to bleed out, at the minor downside of the wound being somewhat more susceptible to infection than being treated by a doctor under better conditions (e.g. by a skilled doctor, with industrial+ medicine, in a clean hospital).
  * Does not affect non-bleeding wounds.

| −1 | 1 | \-  | \-   
  
## Psychics[[edit](/index.php?title=Genes&action=edit&section=8 "Edit section: Psychics")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Psychically deaf  
[![Gene PsychicallyDeaf.png](/images/thumb/b/bb/Gene_PsychicallyDeaf.png/64px-Gene_PsychicallyDeaf.png)](/wiki/File:Gene_PsychicallyDeaf.png) | _Carriers of this gene are deaf to all psychic energy and influence outside their own minds. They cannot be affected by psychic influence, nor can they ever wield psychic power._

* * *

  * Forced [trait](/wiki/Trait "Trait"): [Psychically deaf](/wiki/Psychically_deaf "Psychically deaf")

| +2 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | PsychicAbility   
Psychically dull  
[![Gene PsychicallyDull.png](/images/thumb/2/21/Gene_PsychicallyDull.png/64px-Gene_PsychicallyDull.png)](/wiki/File:Gene_PsychicallyDull.png) | _Carriers of this gene are less psychically-sensitive than others._

* * *

  * Forced [trait](/wiki/Trait "Trait"): [Psychically dull](/wiki/Psychically_dull "Psychically dull")

| +1 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | PsychicAbility   
Psy-sensitive  
[![Gene EnhancedPsychicAbility.png](/images/thumb/a/ad/Gene_EnhancedPsychicAbility.png/64px-Gene_EnhancedPsychicAbility.png)](/wiki/File:Gene_EnhancedPsychicAbility.png) | _Carriers of this gene are more psychically-sensitive than average._

* * *

  * [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") +20%
  * Meditation psyfocus gain +10% / day [Verify]
  * +0.1 Neural Heat Recovery per second base. Effectively 0.163 Heat/s recovery at Level 6 psylink.
  * Does not suppress the [psychically dull](/wiki/Psychically_dull "Psychically dull") or [psychically deaf](/wiki/Psychically_deaf "Psychically deaf") traits, but is applied afterwards. This increases the pawn's base psychic sensitivity to 70 / 20 respectively.

| −2 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | PsychicAbility   
Super psy-sensitive  
[![Gene ExtremePsychicAbility.png](/images/thumb/2/29/Gene_ExtremePsychicAbility.png/64px-Gene_ExtremePsychicAbility.png)](/wiki/File:Gene_ExtremePsychicAbility.png) | _Carriers of this gene are much more psychically-sensitive than most._

* * *

  * [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") +40%
  * Meditation psyfocus gain +20% / day [Verify]
  * +0.2 Neural Heat Recovery per second base. Effectively 0.325 Heat/s recovery at Level 6 psylink.
  * Does not suppress the [psychically dull](/wiki/Psychically_dull "Psychically dull") or [psychically deaf](/wiki/Psychically_deaf "Psychically deaf") traits, but is applied afterwards. This increases the pawn's base psychic sensitivity to 90 / 40 respectively.

| −5 | 2 | \-  | PsychicAbility   
Psychic bonding  
[![Gene PsychicBonding.png](/images/thumb/b/b0/Gene_PsychicBonding.png/64px-Gene_PsychicBonding.png)](/wiki/File:Gene_PsychicBonding.png) | _Carriers of this gene have a special neural organ that makes them psychically bond with a lover for life. As long as the lovers are together, they will be happy. If they are physically separated, they will be disturbed by the distance. If one dies, the other's mind will be badly disrupted._

* * *

  * Romance attempts always succeed
  * Gains psychic bond with first attempted [romance](/wiki/Romance "Romance") or [lovin'](/wiki/Lovin%27 "Lovin'")



    

  * _This person has a psychic bond with another person based on the psychic bonding gene. The bond itself grants some limited psychic awareness, allowing it to connect even with the psychically deaf._
  * Bonded pawns receive gain ×50% [pain](/wiki/Pain "Pain") multiplier, +15% [consciousness](/wiki/Consciousness "Consciousness"), +12 [mood](/wiki/Mood "Mood") and +10% [psychic sensitivity](/wiki/Psychic_sensitivity "Psychic sensitivity") when on same map or in the same [caravan](/wiki/Caravan "Caravan").
  * Bonded pawns receive −10 [mood](/wiki/Mood "Mood"), +5% [psychic sensitivity](/wiki/Psychic_sensitivity "Psychic sensitivity"), and −25% [consciousness](/wiki/Consciousness "Consciousness") when not on same map or when one pawn is in stasis via [cryptosleep caskets](/wiki/Cryptosleep_casket "Cryptosleep casket") or a [biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC").
  * Bonded pawns have +50 [opinion](/wiki/Opinion "Opinion") of each other.
  * When one bonded pawn dies, the other will receive a −25 mood penalty that linearly decays over the course of 30 days. Note: if counseled, the counsel bonus will not decay, but will stay at the value it was applied with.
  * When a bonded pawn dies, the pawn with the psychic bonding gene will immediately suffer an extreme [mental break](/wiki/Mental_break "Mental break"). Violence disabled pawns can still go [berserk](/wiki/Mental_break#Berserk "Mental break").


| −1 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | \-   
  
## Movement[[edit](/index.php?title=Genes&action=edit&section=9 "Edit section: Movement")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Slow runner  
[![Gene SlowMovespeed.png](/images/thumb/6/61/Gene_SlowMovespeed.png/64px-Gene_SlowMovespeed.png)](/wiki/File:Gene_SlowMovespeed.png) | _Carriers of this gene move more slowly than normal._

* * *

  * [Move Speed](/wiki/Move_Speed "Move Speed"): −0.2 c/s

| +3 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | MoveSpeed   
Fast runner  
[![Gene QuickMovespeed.png](/images/thumb/e/e9/Gene_QuickMovespeed.png/64px-Gene_QuickMovespeed.png)](/wiki/File:Gene_QuickMovespeed.png) | _Carriers of this gene move more quickly than normal._

* * *

  * [Move Speed](/wiki/Move_Speed "Move Speed"): +0.2 c/s

| −3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | MoveSpeed   
Very fast runner  
[![Gene VeryQuickMovespeed.png](/images/thumb/0/03/Gene_VeryQuickMovespeed.png/64px-Gene_VeryQuickMovespeed.png)](/wiki/File:Gene_VeryQuickMovespeed.png) | _Carriers of this gene move much more quickly than normal._

* * *

  * [Move Speed](/wiki/Move_Speed "Move Speed"): +0.4 c/s

| −5 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | MoveSpeed   
Naked speed  
[![Gene NakedSpeed.png](/images/thumb/2/29/Gene_NakedSpeed.png/64px-Gene_NakedSpeed.png)](/wiki/File:Gene_NakedSpeed.png) | _Carriers of this gene move slower while clothed, and faster while naked._

* * *

  * [Move speed](/wiki/Move_speed "Move speed"): −0.20 c/s (clothed)
  * [Move speed](/wiki/Move_speed "Move speed"): +0.10 c/s (unclothed)

| +2 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | \-   
Webbed phalanges  
[![Gene WebbedPhalanges.png](/images/thumb/2/23/Gene_WebbedPhalanges.png/64px-Gene_WebbedPhalanges.png)](/wiki/File:Gene_WebbedPhalanges.png) | _Carriers of this gene have webbed fingers and toes, allowing them to move faster in water. Webbed fingers slightly reduce fine motor control._

* * *

  * [Manipulation](/wiki/Manipulation "Manipulation") −5%
  * [Water tiles](/wiki/Environment#Naturally_generated_surfaces "Environment") no longer hinder movement for this pawn. 
    * Mechanically, any terrain with the **water** tag will be treated as having a movement speed of 100% for pawns with this gene.

| −1 | 1 | \-  | \-   
  
## Mood[[edit](/index.php?title=Genes&action=edit&section=10 "Edit section: Mood")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Very unhappy  
[![Gene Depressive.png](/images/thumb/6/6b/Gene_Depressive.png/64px-Gene_Depressive.png)](/wiki/File:Gene_Depressive.png) | _Carriers of this gene are highly predisposed to negative emotion. They'll see the bad in every situation and have a much lower mood than others._

* * *

  * Permanent −10 _Genetic depression_ [thought](/wiki/Thought "Thought")

| +5 | 1 | \-  | Mood   
Unhappy  
[![Gene Pessimist.png](/images/thumb/b/b7/Gene_Pessimist.png/64px-Gene_Pessimist.png)](/wiki/File:Gene_Pessimist.png) | _Carriers of this gene are predisposed to pessimistic perceptions. They'll tend to interpret things negatively and have lower mood than others._

* * *

  * Permanent −5 _Genetic pessimism_ [thought](/wiki/Thought "Thought")

| +3 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | Mood   
Happy  
[![Gene Optimist.png](/images/thumb/2/21/Gene_Optimist.png/64px-Gene_Optimist.png)](/wiki/File:Gene_Optimist.png) | _Carriers of this gene are predisposed to optimistic feelings. They'll have higher mood than others._

* * *

  * Permanent +5 _Genetic optimism_ [thought](/wiki/Thought "Thought")

| −1 | 2 | \-  | Mood   
Very happy  
[![Gene Sanguine.png](/images/thumb/f/f8/Gene_Sanguine.png/64px-Gene_Sanguine.png)](/wiki/File:Gene_Sanguine.png) | _Carriers of this gene are highly predisposed to optimism and not at all inclined to think negatively. They'll have much higher mood than others._

* * *

  * Permanent +10 _Genetic joy_ [thought](/wiki/Thought "Thought")

| −2 | 3 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Mood   
  
## Temperature[[edit](/index.php?title=Genes&action=edit&section=11 "Edit section: Temperature")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Cold weakness  
[![Gene MinTemperatureSmallIncrease.png](/images/thumb/5/5c/Gene_MinTemperatureSmallIncrease.png/64px-Gene_MinTemperatureSmallIncrease.png)](/wiki/File:Gene_MinTemperatureSmallIncrease.png) | _Carriers of this gene are slightly less comfortable in cold temperatures._

* * *

  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): +5 °C (9 °F)

| +1 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | MinTemperature   
Cold tolerant  
[![Gene MinTemperatureSmallDecrease.png](/images/thumb/5/5d/Gene_MinTemperatureSmallDecrease.png/64px-Gene_MinTemperatureSmallDecrease.png)](/wiki/File:Gene_MinTemperatureSmallDecrease.png) | _Carriers of this gene are slightly more comfortable in cold temperatures._

* * *

  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −10 °C (18 °F)

| −1 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | MinTemperature   
Cold super-tolerant  
[![Gene MinTemperatureLargeDecrease.png](/images/thumb/d/da/Gene_MinTemperatureLargeDecrease.png/64px-Gene_MinTemperatureLargeDecrease.png)](/wiki/File:Gene_MinTemperatureLargeDecrease.png) | _Carriers of this gene are much more comfortable in cold temperatures._

* * *

  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −20 °C (36 °F)

| −2 | 1 | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | MinTemperature   
Heat weakness  
[![Gene MaxTemperatureSmallDecrease.png](/images/thumb/d/de/Gene_MaxTemperatureSmallDecrease.png/64px-Gene_MaxTemperatureSmallDecrease.png)](/wiki/File:Gene_MaxTemperatureSmallDecrease.png) | _Carriers of this gene are slightly less comfortable in warm temperatures._

* * *

  * [Maximum Comfortable Temperature](/wiki/Maximum_Comfortable_Temperature "Maximum Comfortable Temperature"): −5 °C (9 °F)

| +1 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | MaxTemperature   
Heat tolerant  
[![Gene MaxTemperatureSmallIncrease.png](/images/thumb/d/d0/Gene_MaxTemperatureSmallIncrease.png/64px-Gene_MaxTemperatureSmallIncrease.png)](/wiki/File:Gene_MaxTemperatureSmallIncrease.png) | _Carriers of this gene are slightly more comfortable in warm temperatures._

* * *

  * [Maximum Comfortable Temperature](/wiki/Maximum_Comfortable_Temperature "Maximum Comfortable Temperature"): +10 °C (18 °F)

| −1 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | MaxTemperature   
Heat super-tolerant  
[![Gene MaxTemperatureLargeIncrease.png](/images/thumb/6/66/Gene_MaxTemperatureLargeIncrease.png/64px-Gene_MaxTemperatureLargeIncrease.png)](/wiki/File:Gene_MaxTemperatureLargeIncrease.png) | _Carriers of this gene are much more comfortable in warm temperatures._

* * *

  * [Maximum Comfortable Temperature](/wiki/Maximum_Comfortable_Temperature "Maximum Comfortable Temperature"): +20 °C (36 °F)

| −2 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | MaxTemperature   
  
## Resistance and sensitivity[[edit](/index.php?title=Genes&action=edit&section=12 "Edit section: Resistance and sensitivity")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Tox resistance  
[![Gene PartialToxicityResistance.png](/images/thumb/1/1f/Gene_PartialToxicityResistance.png/64px-Gene_PartialToxicityResistance.png)](/wiki/File:Gene_PartialToxicityResistance.png) | _Carriers of this gene are resistant to toxic buildup from any source. This includes pollution, toxic fallout, tox gas, and direct attacks with venom or injected poison. They'll gain half the amount of toxic buildup compared to others. Cellular filters in the lung and skin reduce the dose of toxins entering the bloodstream._

* * *

  * [Toxic Resistance](/wiki/Toxic_Resistance "Toxic Resistance"): +50%

| −2 | 1 | \-  | ToxResistance   
Tox immunity  
[![Gene TotalToxicityResistance.png](/images/thumb/a/ad/Gene_TotalToxicityResistance.png/64px-Gene_TotalToxicityResistance.png)](/wiki/File:Gene_TotalToxicityResistance.png) | _Carriers of this gene are totally immune to toxic buildup from all sources including polluted terrain, toxic fallout, tox gas, and direct attacks with venom or injected poison. They are also not bothered by acidic smog. The carrier's biochemical pathways are modified to route around interference from nearly all known toxins. Along with enhancements to the kidneys and liver, this keeps carriers comfortable in even the most toxic of environments._

* * *

  * [Toxic Resistance](/wiki/Toxic_Resistance "Toxic Resistance"): +100%
  * [Tox gas](/wiki/Tox_gas "Tox gas") immunity
  * Removes mood: Toxic fallout: -5
  * Removes mood: Acidic smog: -5

| −4 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | ToxResistance   
Partial antitoxic lungs  
[![Gene PartialPollutionResistance.png](/images/thumb/5/5f/Gene_PartialPollutionResistance.png/64px-Gene_PartialPollutionResistance.png)](/wiki/File:Gene_PartialPollutionResistance.png) | _Carriers of this gene are resistant to environmental toxins. They get less toxic buildup from tox gas, polluted terrain, and toxic fallout, but are still vulnerable to direct attacks with venom or injected poison. Additionally, they build up rot stink exposure slower._

* * *

  * [Toxic Environment Resistance](/wiki/Toxic_Environment_Resistance "Toxic Environment Resistance"): +50%

| −1 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | ToxicEnvironmentResistance   
Total antitoxic lungs  
[![Gene TotalPollutionResistance.png](/images/thumb/c/c6/Gene_TotalPollutionResistance.png/64px-Gene_TotalPollutionResistance.png)](/wiki/File:Gene_TotalPollutionResistance.png) | _Carriers of this gene are immune to environmental toxins, but not from direct toxic attacks. They get no toxic buildup from tox gas, polluted terrain, or toxic fallout, and they are not bothered by acidic smog. They are still vulnerable to direct attacks like venom and injected poison. Additionally, they are immune to rot stink exposure._

* * *

  * [Toxic Environment Resistance](/wiki/Toxic_Environment_Resistance "Toxic Environment Resistance"): +100%
  * [Tox gas](/wiki/Tox_gas "Tox gas") immunity
  * Removes mood: Toxic fallout: -5
  * Removes mood: Acidic smog: -5

| −3 | 2 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | ToxicEnvironmentResistance   
Mild UV sensitivity  
[![Gene MildUVSensitivity.png](/images/thumb/b/b3/Gene_MildUVSensitivity.png/64px-Gene_MildUVSensitivity.png)](/wiki/File:Gene_MildUVSensitivity.png) | _Carriers of this gene have biological compounds in their skin that react painfully to UV radiation. They are unusually sensitive to sunlight._

* * *

  * When in sunlight (when on an unroofed tile while [light](/wiki/Light "Light") levels from natural sunlight are 11% or more): 
    * [Move Speed](/wiki/Move_Speed "Move Speed") ×90%
    * Mood: _Sunlight Sensitivity_ : −6
  * Does not cause [pain](/wiki/Pain "Pain"), despite the description.

| +3 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | UVSensitivity   
Intense UV sensitivity  
[![Gene IntenseUVSensitivity.png](/images/thumb/1/15/Gene_IntenseUVSensitivity.png/64px-Gene_IntenseUVSensitivity.png)](/wiki/File:Gene_IntenseUVSensitivity.png) | _Carriers of this gene have biological compounds in their skin that react dangerously to UV radiation. They are intensely sensitive to sunlight._

* * *

  * When in sunlight (when on an unroofed tile while [light](/wiki/Light "Light") levels from natural sunlight are 11% or more): 
    * [Move Speed](/wiki/Move_Speed "Move Speed") ×80%
    * Mood: _Sunlight Sensitivity_ : −12
  * Does not cause [pain](/wiki/Pain "Pain").

| +4 | 2 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") | UVSensitivity   
Fire resistant  
[![Gene FireResistant.png](/images/thumb/6/64/Gene_FireResistant.png/64px-Gene_FireResistant.png)](/wiki/File:Gene_FireResistant.png) | _Carriers of this gene have special fast-acting sweat glands and heat-resistant skin. They only take 25% of the normal damage from fire. The chance of them catching on fire is also drastically reduced._

* * *

  * [Flammability](/wiki/Flammability "Flammability") ×10%
  * [Flame](/wiki/Damage_Type#Flame "Damage Type") damage ×25%



    Note that this does not affect [Heat](/wiki/Damage_Type#Heat "Damage Type") or [Vaporize](/wiki/Damage_Type#Vaporize "Damage Type") damage
| −2 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | FireDamage   
Tinderskin  
[![Gene FireWeakness.png](/images/thumb/0/0f/Gene_FireWeakness.png/64px-Gene_FireWeakness.png)](/wiki/File:Gene_FireWeakness.png) | _Carriers have dry, thin skin which burns easily from fire, and their immune systems react very poorly to this kind of threat. Damage from fire is multiplied by 4._

* * *

  * [Flame](/wiki/Damage_Type#Flame "Damage Type") damage ×400%



    Note that this does not affect [Heat](/wiki/Damage_Type#Heat "Damage Type") or [Vaporize](/wiki/Damage_Type#Vaporize "Damage Type") damage
| +2 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | FireDamage   
Pyrophobia  
[![Gene FireTerror.png](/images/thumb/2/28/Gene_FireTerror.png/64px-Gene_FireTerror.png)](/wiki/File:Gene_FireTerror.png) | _Carriers of this gene have an intense fear of fire. When fires are close, there is a chance they will have a mental breakdown at any moment._

* * *

  * If the pawn has line of sight of a fire within 19.9 tiles, it is considered "near fire" and the following happens: 
    * −10 _Afraid of fire_ [moodlet](/wiki/Mood "Mood")
    * 0.1 day mtb chance of "Fire terror" mental break that cause "panic-fleeing fire" mental state, ends when not "near fire" for 500 [ticks](/wiki/Time "Time") (8.33 secs)
  * Suppresses [Pyromaniac](/wiki/Pyromaniac "Pyromaniac") trait



    Note that blind pawns are still affected by pyrophobia, and will still flee
| +4 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Vacuum resistant  
[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")  
[![Gene VacuumResistance.png](/images/thumb/f/f4/Gene_VacuumResistance.png/64px-Gene_VacuumResistance.png)](/wiki/File:Gene_VacuumResistance.png) | _Carriers of this gene have skin that releases a waxy substance when air pressure is low, preventing vacuum burns and allowing them to survive longer when exposed to vacuum._

* * *

  * Immune to vacuum burns
  * [Vacuum resistance](/wiki/Vacuum_resistance "Vacuum resistance"): +45%
  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −5 °C (9 °F)

| −1 | 1 | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | VacuumResistance   
  
## Violence[[edit](/index.php?title=Genes&action=edit&section=13 "Edit section: Violence")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Dead calm  
[![Gene DeadCalm.png](/images/thumb/a/a1/Gene_DeadCalm.png/64px-Gene_DeadCalm.png)](/wiki/File:Gene_DeadCalm.png) | Carriers of this gene feel calm in every situation and have a very placid demeanor. They will never start social fights or have aggressive mental breaks. 

* * *

  * Effects: 
    * Will never do social fights
    * Mental breaks are never violent (Tantrum, Berserk, Slaughterer, Murderous Rage)
    * Will never prison break
    * [Arresting](/wiki/Arrest "Arrest") never fails, and will never berserk on arrest.

| −1 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies") | Aggression   
Aggressive  
[![Gene Aggressive.png](/images/thumb/8/8f/Gene_Aggressive.png/64px-Gene_Aggressive.png)](/wiki/File:Gene_Aggressive.png) | Carriers of this gene are quick to anger. They are twice as likely to start social fights. When they have mental breaks, they are twice as likely to choose an aggressive kind of break. 

* * *

  * Effects: 
    * Social fight chance factor ×200%
    * Chance mental break is violent ×200% (Tantrum, Berserk, Slaughterer, Murderous Rage) [Wb minor breaks?]
    * Prison break interval factor ×60%

| +2 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Aggression  
Aggressive   
Hyper-aggressive  
[![Gene HyperAggressive.png](/images/thumb/4/4b/Gene_HyperAggressive.png/64px-Gene_HyperAggressive.png)](/wiki/File:Gene_HyperAggressive.png) | Carriers of this gene are hormonally high-strung and very aggressive. They are three times as likely to start social fights. Any mental break they have will be of an aggressive type. 

* * *

  * Effects: 
    * Social fight chance factor ×300%
    * Mental breaks are always[Verify] violent where possible.(Tantrum, Berserk, Slaughterer, Murderous Rage) Tiers without violent options, i.e. Minor breaks, non-violent breaks are chosen instead.[All types?]
    * Prison break interval factor ×40%

| +3 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | Aggression  
Aggressive   
Weak melee damage  
[![Gene WeakMeleeDamage.png](/images/thumb/1/19/Gene_WeakMeleeDamage.png/64px-Gene_WeakMeleeDamage.png)](/wiki/File:Gene_WeakMeleeDamage.png) | Carriers of this gene do less damage in close-quarters combat. Weak fast-twitch muscle fibers make their strikes shaky and weak. 

* * *

  * [Melee damage factor](/wiki/Melee_damage_factor "Melee damage factor") ×50% 
    * This also affects melee AP when calculated from damage. It does not affect the AP of weapons that are set independently of damage, such as: [Spears](/wiki/Spear "Spear"), [Monoswords](/wiki/Monosword "Monosword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Persona monoswords](/wiki/Persona_monosword "Persona monosword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Hand talon](/wiki/Hand_talon "Hand talon"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Knee spikes](/wiki/Knee_spike "Knee spike"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and [flesh whips](/wiki/Flesh_whip "Flesh whip")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC").

| +1 | 1 | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | MeleeDamage   
Strong melee damage  
[![Gene StrongMeleeDamage.png](/images/thumb/b/b9/Gene_StrongMeleeDamage.png/64px-Gene_StrongMeleeDamage.png)](/wiki/File:Gene_StrongMeleeDamage.png) | Carriers of this gene do more damage in close-quarters combat. Extra-strong fast-twitch muscle fibers make their strikes accurate and powerful. 

* * *

  * [Melee damage factor](/wiki/Melee_damage_factor "Melee damage factor") ×150% 
    * This also affects melee AP when calculated from damage. It does not affect the AP of weapons that are set independently of damage, such as: [Spears](/wiki/Spear "Spear"), [Monoswords](/wiki/Monosword "Monosword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Persona monoswords](/wiki/Persona_monosword "Persona monosword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Hand talon](/wiki/Hand_talon "Hand talon"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [Knee spikes](/wiki/Knee_spike "Knee spike"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and [flesh whips](/wiki/Flesh_whip "Flesh whip")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC").

| −2 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | MeleeDamage   
Violence disabled  
[![Gene ViolenceDisabled.png](/images/thumb/0/02/Gene_ViolenceDisabled.png/64px-Gene_ViolenceDisabled.png)](/wiki/File:Gene_ViolenceDisabled.png) | Carriers of this gene are emotionally and mentally incapable of engaging in violence. They are overwhelmingly resistant to and horrified by the idea of hurting another. 

* * *

  * Disables work: 
    * Hunt
    * Violent

| +3 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | MeleeDamage  
ShootingAccuracy  
Aggressive  
KillThirst   
Kind instinct  
[![Gene KindInstinct.png](/images/thumb/c/c5/Gene_KindInstinct.png/64px-Gene_KindInstinct.png)](/wiki/File:Gene_KindInstinct.png) | Carriers of this gene are high in trait agreeableness and are very conscientious. They rarely insult others and will sometimes offer kind words to brighten the moods of those around them. They also never judge people by their appearance. 

* * *

  * Forced [trait](/wiki/Trait "Trait"): [Kind](/wiki/Kind "Kind")
  * Suppresses [Abrasive](/wiki/Abrasive "Abrasive") and [Psychopath](/wiki/Psychopath "Psychopath") traits

| −1 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | \-   
Kill thirst  
[![Gene Killthirst.png](/images/thumb/f/fd/Gene_Killthirst.png/64px-Gene_Killthirst.png)](/wiki/File:Gene_Killthirst.png) | Carriers of this gene lust for the feeling of ending another's life. They will become irritated if they go for too long without killing someone in close combat. 

* * *

  * Causes [need](/wiki/Need "Need"): [Kill satiety](/wiki/Kill_satiety "Kill satiety"). Inflicts an increasing mood penalty during long periods between melee kills. See the [Kill satiety](/wiki/Kill_satiety "Kill satiety") page for details.

| +4 | 1 | \-  | KillThirst   
  
## Sleep[[edit](/index.php?title=Genes&action=edit&section=14 "Edit section: Sleep")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Very sleepy  
[![Gene VerySleepy.png](/images/thumb/1/1f/Gene_VerySleepy.png/64px-Gene_VerySleepy.png)](/wiki/File:Gene_VerySleepy.png) | Carriers of this gene get tired much faster than others. 

* * *

  * [Sleep Fall Rate](/wiki/Sleep_Fall_Rate "Sleep Fall Rate"): ×180%

| +4 | 1 | \-  | Sleep   
Sleepy  
[![Gene Sleepy.png](/images/thumb/f/f9/Gene_Sleepy.png/64px-Gene_Sleepy.png)](/wiki/File:Gene_Sleepy.png) | Carriers of this gene get tired somewhat faster than others. 

* * *

  * [Sleep Fall Rate](/wiki/Sleep_Fall_Rate "Sleep Fall Rate"): ×140%

| +2 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | Sleep   
Low sleep  
[![Gene QuickSleeper.png](/images/thumb/b/bc/Gene_QuickSleeper.png/64px-Gene_QuickSleeper.png)](/wiki/File:Gene_QuickSleeper.png) | Carriers of this gene get tired less quickly than others. 

* * *

  * [Sleep Fall Rate](/wiki/Sleep_Fall_Rate "Sleep Fall Rate"): ×40%

| −4 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Sleep   
Never sleep  
[![Gene Neversleep.png](/images/thumb/7/77/Gene_Neversleep.png/64px-Gene_Neversleep.png)](/wiki/File:Gene_Neversleep.png) | Carriers of this gene have a unique metabolic process which allows clusters of neurons to sleep while the rest of the brain stays awake. They never need to sleep. 

* * *

  * Effects: 
    * Disables [need](/wiki/Need "Need"): [Sleep](/wiki/Sleep "Sleep")
    * If all pawns in a [caravan](/wiki/Caravan "Caravan") have either this gene, a [circadian half-cycler](/wiki/Circadian_half-cycler "Circadian half-cycler"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") or the [body mastery](/wiki/Body_mastery "Body mastery")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") trait, and they travel without animals, they don't need to [stop at night](/wiki/Caravan#Caravan_schedule "Caravan").
  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×125%

| −6 | 3 | \-  | Sleep   
  
## Pain[[edit](/index.php?title=Genes&action=edit&section=15 "Edit section: Pain")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Delicate  
[![Gene Delicate.png](/images/thumb/c/c6/Gene_Delicate.png/64px-Gene_Delicate.png)](/wiki/File:Gene_Delicate.png) | Carriers of this gene take greater injuries than others from the same damage. They have thin, brittle bones and less binding molecules in joints and flesh. 

* * *

  * Forced [trait](/wiki/Trait "Trait"): [Delicate](/wiki/Delicate "Delicate")
  * Suppresses [Tough](/wiki/Tough "Tough") trait

| +3 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Toughness   
Robust  
[![Gene Tough.png](/images/thumb/7/7b/Gene_Tough.png/64px-Gene_Tough.png)](/wiki/File:Gene_Tough.png) | Carriers of this gene take less injuries than others from the same damage. They have thickened, densified bones, nearly-solid ribcages, and strengthened binding factors in joints and flesh. 

* * *

  * ×75% [Incoming Damage Multiplier](/wiki/Incoming_Damage_Multiplier "Incoming Damage Multiplier")
    * Note that despite being incompatible with the Delicate gene, it stacks multiplicatively with other Incoming Damage Multiplier factors, including the [Delicate](/wiki/Delicate "Delicate") _trait_. See for [Incoming Damage Multiplier](/wiki/Incoming_Damage_Multiplier "Incoming Damage Multiplier") further details on stacking.

| −2 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Toughness   
Extra pain  
[![Gene ExtraPain.png](/images/thumb/d/d7/Gene_ExtraPain.png/64px-Gene_ExtraPain.png)](/wiki/File:Gene_ExtraPain.png) | Carriers of this gene feel more pain than others given the same injuries. Neuron activity in the brain's nociception center is amplified, so pain feels extra-intense and fiery. This can be protective, but overall it's considered a negative and makes it hard to push through difficult situations. 

* * *

  * Forced [trait](/wiki/Trait "Trait"): [Wimp](/wiki/Wimp "Wimp")
  * Suppresses [Masochist](/wiki/Masochist "Masochist") and [Brawler](/wiki/Brawler "Brawler") traits

| +2 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies") | Pain   
Reduced pain  
[![Gene PainReduced.png](/images/thumb/9/9a/Gene_PainReduced.png/64px-Gene_PainReduced.png)](/wiki/File:Gene_PainReduced.png) | Carriers of this gene feel half as much pain compared to a baseliner. Reduced neuron activity in the brain's nociception centers makes pain dull and faint. This can be advantageous sometimes, and dangerous other times. 

* * *

  * Pain ×50%

| −1 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Pain   
  
## Reproduction[[edit](/index.php?title=Genes&action=edit&section=16 "Edit section: Reproduction")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Low libido  
[![Gene LowLibido.png](/images/thumb/0/0d/Gene_LowLibido.png/64px-Gene_LowLibido.png)](/wiki/File:Gene_LowLibido.png) | Carriers of this gene are less likely to engage in lovin' with their partner. 

* * *

  * MTB [Lovin'](/wiki/Lovin%27 "Lovin'") Factor: ×2

| **0** | 1 | \-  | Libido   
High libido  
[![Gene HighLibido.png](/images/thumb/f/f4/Gene_HighLibido.png/64px-Gene_HighLibido.png)](/wiki/File:Gene_HighLibido.png) | Carriers of this gene are more likely to engage in lovin' with their partner. 

* * *

  * MTB [Lovin'](/wiki/Lovin%27 "Lovin'") Factor: ×0.5

| **0** | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Libido   
Sterile  
[![Gene Sterile.png](/images/thumb/d/d4/Gene_Sterile.png/64px-Gene_Sterile.png)](/wiki/File:Gene_Sterile.png) | Carriers of this gene cannot reproduce by natural means. 

* * *

  * Fertility ×0%

| +1 | 1 | \-  | Fertility   
Fertile  
[![Gene Fertile.png](/images/thumb/0/02/Gene_Fertile.png/64px-Gene_Fertile.png)](/wiki/File:Gene_Fertile.png) | Carriers of this gene have a higher chance of becoming pregnant or impregnating others. 

* * *

  * Fertility ×200%

| **0** | 1 | \-  | Fertility   
  
## Beauty[[edit](/index.php?title=Genes&action=edit&section=17 "Edit section: Beauty")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Very unattractive  
[![Gene StaggeringlyUgly.png](/images/thumb/a/ad/Gene_StaggeringlyUgly.png/64px-Gene_StaggeringlyUgly.png)](/wiki/File:Gene_StaggeringlyUgly.png) | _Carriers of this gene have misshapen, asymmetrical facial structures and blotchy skin. They're hard to look at._

* * *

  * [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)"): −2
  * [Market Value](/wiki/Market_Value "Market Value"): −700

| +2 | 1 | \-  | Beauty   
Unattractive  
[![Gene Ugly.png](/images/thumb/f/f8/Gene_Ugly.png/64px-Gene_Ugly.png)](/wiki/File:Gene_Ugly.png) | _Carriers of this gene have exaggerated facial features and poor skin that are generally considered ugly._

* * *

  * [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)"): −1
  * [Market Value](/wiki/Market_Value "Market Value"): −350

| +1 | 1 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | Beauty   
Attractive  
[![Gene Pretty.png](/images/thumb/3/34/Gene_Pretty.png/64px-Gene_Pretty.png)](/wiki/File:Gene_Pretty.png) | _Carriers of this gene have unusually symmetrical, balanced facial features and extra-clear skin which gives them a pleasing appearance._

* * *

  * [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)"): +1
  * [Market Value](/wiki/Market_Value "Market Value"): +350

| −1 | 1 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Beauty   
Very attractive  
[![Gene Beautiful.png](/images/thumb/c/cf/Gene_Beautiful.png/64px-Gene_Beautiful.png)](/wiki/File:Gene_Beautiful.png) | _Carriers of this gene have remarkably precise and symmetrical faces. Their features are distinctive and strong without being exaggerated, and their skin is nearly perfect. They are generally seen as beautiful._

* * *

  * [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)"): +2
  * [Market Value](/wiki/Market_Value "Market Value"): +700

| −2 | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Beauty   
  
## Cosmetic[[edit](/index.php?title=Genes&action=edit&section=18 "Edit section: Cosmetic")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Red eyes  
[![Gene RedEyes.png](/images/thumb/8/84/Gene_RedEyes.png/64px-Gene_RedEyes.png)](/wiki/File:Gene_RedEyes.png) | _Carriers of this gene have deeply red-pigmented eyes._ | **0** | **0** | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | EyeColor   
Gray eyes  
[![Gene GrayEyes.png](/images/thumb/4/46/Gene_GrayEyes.png/64px-Gene_GrayEyes.png)](/wiki/File:Gene_GrayEyes.png) | _Carriers of this gene have pale white-gray eyes._ | **0** | **0** | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") | EyeColor   
No hair  
[![Gene HairStyleBaldOnly.png](/images/thumb/1/14/Gene_HairStyleBaldOnly.png/64px-Gene_HairStyleBaldOnly.png)](/wiki/File:Gene_HairStyleBaldOnly.png) | _Carriers of this gene grow no hair on the head._ | **0** | **0** | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | HairStyle   
Short-haired  
[![Gene HairStyleShortOnly.png](/images/thumb/a/ab/Gene_HairStyleShortOnly.png/64px-Gene_HairStyleShortOnly.png)](/wiki/File:Gene_HairStyleShortOnly.png) | _Carriers of this gene can only grow short hair._ | **0** | **0** | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | HairStyle   
Long-haired  
[![Gene HairStyleLongOnly.png](/images/thumb/3/31/Gene_HairStyleLongOnly.png/64px-Gene_HairStyleLongOnly.png)](/wiki/File:Gene_HairStyleLongOnly.png) | _Carriers of this gene grow hair on the head very quickly._ | **0** | **0** | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | HairStyle   
Only bushy beards  
[![Gene BeardStyleBushyOnly.png](/images/thumb/6/66/Gene_BeardStyleBushyOnly.png/64px-Gene_BeardStyleBushyOnly.png)](/wiki/File:Gene_BeardStyleBushyOnly.png) | _Male carriers of this gene experience rapid beard growth and are uncomfortable cutting their beards._ | **0** | **0** | \-  | BeardStyle   
Beardless  
[![Gene BeardStyleNone.png](/images/thumb/2/21/Gene_BeardStyleNone.png/64px-Gene_BeardStyleNone.png)](/wiki/File:Gene_BeardStyleNone.png) | _Carriers of this gene grow no facial hair._ | **0** | **0** | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | BeardStyle   
Unisex beards  
[![Gene UnisexBeards.png](/images/thumb/3/3d/Gene_UnisexBeards.png/64px-Gene_UnisexBeards.png)](/wiki/File:Gene_UnisexBeards.png) | _Carriers of this gene always have thick facial hair, even women._ | **0** | **0** | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | BeardStyle   
Human ears  
[![Gene EarHuman.png](/images/thumb/5/59/Gene_EarHuman.png/64px-Gene_EarHuman.png)](/wiki/File:Gene_EarHuman.png) | _Carriers of this gene have regular human ears._ | **0** | **0** | \-  | Ears   
Pointed ears  
[![Gene EarPointed.png](/images/thumb/d/db/Gene_EarPointed.png/64px-Gene_EarPointed.png)](/wiki/File:Gene_EarPointed.png) | _Carriers of this gene have pointed ears._ | **0** | **0** | \-  | Ears   
Cat ears  
[![Gene EarCat.png](/images/thumb/7/7c/Gene_EarCat.png/64px-Gene_EarCat.png)](/wiki/File:Gene_EarCat.png) | _Carriers of this gene have cat-like ears._ | **0** | **0** | \-  | Ears   
Floppy ears  
[![Gene EarFloppy.png](/images/thumb/1/17/Gene_EarFloppy.png/64px-Gene_EarFloppy.png)](/wiki/File:Gene_EarFloppy.png) | _Carriers of this gene grow long, floppy hound-like ears._ | **0** | **0** | \-  | Ears   
Pig ears  
[![Gene EarPig.png](/images/thumb/5/53/Gene_EarPig.png/64px-Gene_EarPig.png)](/wiki/File:Gene_EarPig.png) | _Carriers of this gene will grow pointed pig-like ears._ | **0** | **0** | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Ears   
Human nose  
[![Gene NoseHuman.png](/images/thumb/1/19/Gene_NoseHuman.png/64px-Gene_NoseHuman.png)](/wiki/File:Gene_NoseHuman.png) | _Carriers of this gene have regular human noses._ | **0** | **0** | \-  | Nose   
Human jaw  
[![Gene JawBaseline.png](/images/thumb/9/91/Gene_JawBaseline.png/64px-Gene_JawBaseline.png)](/wiki/File:Gene_JawBaseline.png) | _Carriers of this gene have regularly-shaped jaws._ | **0** | **0** | \-  | Jaw   
Heavy jaw  
[![Gene JawHeavy.png](/images/thumb/a/a6/Gene_JawHeavy.png/64px-Gene_JawHeavy.png)](/wiki/File:Gene_JawHeavy.png) | _Carriers of this gene have large jaws._ | **0** | **0** | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | Jaw   
Gaunt head  
[![Gene GauntHead.png](/images/thumb/5/58/Gene_GauntHead.png/64px-Gene_GauntHead.png)](/wiki/File:Gene_GauntHead.png) | _Carriers of this gene have a pinched, gaunt appearance in their face and head._ | **0** | **0** | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | Jaw   
Heavy brow  
[![Gene HeavyBrow.png](/images/thumb/b/b3/Gene_HeavyBrow.png/64px-Gene_HeavyBrow.png)](/wiki/File:Gene_HeavyBrow.png) | _Carriers of this gene have a prominent brow._ | **0** | **0** | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | \-   
Center-horn  
[![Gene HeadboneCenterhorn.png](/images/thumb/1/1e/Gene_HeadboneCenterhorn.png/64px-Gene_HeadboneCenterhorn.png)](/wiki/File:Gene_HeadboneCenterhorn.png) | _Carriers of this gene grow a single horn protruding from the center of the forehead._ | **0** | **0** | \-  | Headbone   
Mini-horns  
[![Gene HeadboneMinihorns.png](/images/thumb/2/20/Gene_HeadboneMinihorns.png/64px-Gene_HeadboneMinihorns.png)](/wiki/File:Gene_HeadboneMinihorns.png) | _Carriers of this gene grow two small horns protruding from the forehead._ | **0** | **0** | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | Headbone   
Human headbone  
[![Gene HeadboneHuman.png](/images/thumb/3/31/Gene_HeadboneHuman.png/64px-Gene_HeadboneHuman.png)](/wiki/File:Gene_HeadboneHuman.png) | _Carriers of this gene have regular human skulls._ | **0** | **0** | \-  | Headbone   
Human voice  
[![Gene VoiceHuman.png](/images/thumb/3/36/Gene_VoiceHuman.png/64px-Gene_VoiceHuman.png)](/wiki/File:Gene_VoiceHuman.png) | _Carriers of this gene have regular human vocal cords._ | **0** | **0** | \-  | Voice   
Pig voice  
[![Gene VoicePig.png](/images/thumb/b/bf/Gene_VoicePig.png/64px-Gene_VoicePig.png)](/wiki/File:Gene_VoicePig.png) | _Carriers have a squealing voice like that of a pig._  
<https://rimworldwiki.com/wiki/File:Pawn_Pigskin_Call_02e.wav> | **0** | **0** | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Voice   
Roar voice  
[![Gene VoiceRoar.png](/images/thumb/4/47/Gene_VoiceRoar.png/64px-Gene_VoiceRoar.png)](/wiki/File:Gene_VoiceRoar.png) | _Carriers have an animal-like roaring voice._  
<https://rimworldwiki.com/wiki/File:Roar_Voice_Call_B02.wav> | **0** | **0** | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | Voice   
Facial ridges  
[![Gene FacialRidges.png](/images/thumb/8/8f/Gene_FacialRidges.png/64px-Gene_FacialRidges.png)](/wiki/File:Gene_FacialRidges.png) | _Carriers of this gene grow raised ridges of skin on their face._ | **0** | **0** | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | \-   
  
### Body type[[edit](/index.php?title=Genes&action=edit&section=19 "Edit section: Body type")]

Since people without these genes can have any of the four body types, these genes effectively limit what body types a xenotype can have. For example, [![Neanderthal.png](/images/thumb/9/91/Neanderthal.png/20px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[Neanderthals](/wiki/Neanderthals "Neanderthals") cannot be thin, because they have all three of the other genes. 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Standard body  
[![Gene BodyStandard.png](/images/thumb/2/2b/Gene_BodyStandard.png/64px-Gene_BodyStandard.png)](/wiki/File:Gene_BodyStandard.png) | _Carriers can have average-shaped bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed._ | **0** | **0** | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | BodyType   
Thin body  
[![Gene BodyThin.png](/images/thumb/4/41/Gene_BodyThin.png/64px-Gene_BodyThin.png)](/wiki/File:Gene_BodyThin.png) | _Carriers can have thin bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed._ | **0** | **0** | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | BodyType   
Fat body  
[![Gene BodyFat.png](/images/thumb/d/d4/Gene_BodyFat.png/64px-Gene_BodyFat.png)](/wiki/File:Gene_BodyFat.png) | _Carriers can have fat bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed._ | **0** | **0** | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | BodyType   
Hulk body  
[![Gene BodyHulk.png](/images/thumb/3/33/Gene_BodyHulk.png/64px-Gene_BodyHulk.png)](/wiki/File:Gene_BodyHulk.png) | _Carriers can have large bodies. A person can have more than one body type gene; one body type will be chosen among those that are allowed._ | **0** | **0** | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins")[![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | BodyType   
  
### Hair[[edit](/index.php?title=Genes&action=edit&section=20 "Edit section: Hair")]

These genes are defined in Core, not Biotech. 

All of them have a "random brightness factor" of 0.12 unless otherwise specified. 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | Weight  | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---|---  
Snow-white hair  
[![Hair SnowWhite.png](/images/thumb/c/c7/Hair_SnowWhite.png/64px-Hair_SnowWhite.png)](/wiki/File:Hair_SnowWhite.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (250, 250, 250)
  * Random brightness factor: 0

| **0** | **0** | 0.05  | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | HairColor   
Gray hair  
[![Hair Grey.png](/images/thumb/8/8b/Hair_Grey.png/64px-Hair_Grey.png)](/wiki/File:Hair_Grey.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (0.65, 0.65, 0.65)

| **0** | **0** | 0.02  | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | HairColor   
Blonde hair  
[![Hair Blonde.png](/images/thumb/c/c3/Hair_Blonde.png/64px-Hair_Blonde.png)](/wiki/File:Hair_Blonde.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (237, 202, 156)
  * Selection weight factor with dark skin: 0

| **0** | **0** | 1?  | \-  | HairColor   
Sandy-blonde hair  
[![Hair SandyBlonde.png](/images/thumb/1/1a/Hair_SandyBlonde.png/64px-Hair_SandyBlonde.png)](/wiki/File:Hair_SandyBlonde.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (193, 146, 85)
  * Selection weight factor with dark skin: 0

| **0** | **0** | 1?  | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | HairColor   
Orange hair  
[![Hair Orange.png](/images/thumb/8/80/Hair_Orange.png/64px-Hair_Orange.png)](/wiki/File:Hair_Orange.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (189, 133, 49)

| **0** | **0** | 0.05  | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | HairColor   
Reddish-brown hair  
[![Hair ReddishBrown.png](/images/thumb/1/1d/Hair_ReddishBrown.png/64px-Hair_ReddishBrown.png)](/wiki/File:Hair_ReddishBrown.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (132, 83, 47)

| **0** | **0** | 1?  | \-  | HairColor   
Brown hair  
[![Hair Brown.png](/images/thumb/e/e4/Hair_Brown.png/64px-Hair_Brown.png)](/wiki/File:Hair_Brown.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (90, 58, 32)

| **0** | **0** | 1?  | \-  | HairColor   
Dark-brown hair  
[![Hair DarkBrown.png](/images/thumb/0/0a/Hair_DarkBrown.png/64px-Hair_DarkBrown.png)](/wiki/File:Hair_DarkBrown.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (56, 36, 18)

| **0** | **0** | 1.5  | \-  | HairColor   
Dark-reddish hair  
[![Hair DarkReddish.png](/images/thumb/3/31/Hair_DarkReddish.png/64px-Hair_DarkReddish.png)](/wiki/File:Hair_DarkReddish.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (0.25, 0.2, 0.15)

| **0** | **0** | 1.5  | \-  | HairColor   
Mid-black hair  
[![Hair MidBlack.png](/images/thumb/f/f7/Hair_MidBlack.png/64px-Hair_MidBlack.png)](/wiki/File:Hair_MidBlack.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (0.31, 0.28, 0.26)

| **0** | **0** | 1.5  | \-  | HairColor   
Dark-black hair  
[![Hair DarkBlack.png](/images/thumb/5/54/Hair_DarkBlack.png/64px-Hair_DarkBlack.png)](/wiki/File:Hair_DarkBlack.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (0.2, 0.2, 0.2)

| **0** | **0** | 1.5  | \-  | HairColor   
Ink-black hair  
[![Hair InkBlack.png](/images/thumb/2/2e/Hair_InkBlack.png/64px-Hair_InkBlack.png)](/wiki/File:Hair_InkBlack.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (25, 25, 25)
  * Random brightness factor: 0

| **0** | **0** | 0.05  | \-  | HairColor   
Blue hair  
[![Hair Blue.png](/images/thumb/4/46/Hair_Blue.png/64px-Hair_Blue.png)](/wiki/File:Hair_Blue.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (34, 63, 227)

| **0** | **0** | 0.05  | \-  | HairColor   
Teal hair  
[![Hair Teal.png](/images/thumb/c/ce/Hair_Teal.png/64px-Hair_Teal.png)](/wiki/File:Hair_Teal.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (52, 191, 182)

| **0** | **0** | 0.05  | \-  | HairColor   
Green hair  
[![Hair Green.png](/images/thumb/8/87/Hair_Green.png/64px-Hair_Green.png)](/wiki/File:Hair_Green.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (72, 201, 40)

| **0** | **0** | 0.05  | \-  | HairColor   
Pink hair  
[![Hair Pink.png](/images/thumb/c/c5/Hair_Pink.png/64px-Hair_Pink.png)](/wiki/File:Hair_Pink.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (191, 86, 149)

| **0** | **0** | 0.05  | \-  | HairColor   
Purple hair  
[![Hair Purple.png](/images/thumb/e/e1/Hair_Purple.png/64px-Hair_Purple.png)](/wiki/File:Hair_Purple.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (227, 115, 255)

| **0** | **0** | 0.05  | \-  | HairColor   
Red hair  
[![Hair Red.png](/images/thumb/7/7a/Hair_Red.png/64px-Hair_Red.png)](/wiki/File:Hair_Red.png) | _Carriers of this gene have a particular hair color. With multiple hair color genes, one is randomly selected._

* * *

  * Hair color override: (191, 86, 86)

| **0** | **0** | 0.05  | \-  | HairColor   
  
### Melanin[[edit](/index.php?title=Genes&action=edit&section=21 "Edit section: Melanin")]

These natural skin colors are **not available in the xenotype editor and cannot be extracted**. Every person gets one of these as a germline gene unless they already have a skin-color germline gene (e.g. [![Dirtmole.png](/images/thumb/c/c4/Dirtmole.png/20px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[Dirtmoles](/wiki/Dirtmoles "Dirtmoles") have light gray skin instead of these). 

These genes are defined in Core, not Biotech. They are all named "Skin color" in-game. 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | Weight  | Exclude   
---|---|---|---|---|---  
Skin_Melanin1  
[![Skin Melanin1.png](/images/thumb/d/d8/Skin_Melanin1.png/64px-Skin_Melanin1.png)](/wiki/File:Skin_Melanin1.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (242, 237, 224)
  * Min melanin: 0

| **0** | **0** | 0.2  | SkinColor   
Skin_Melanin2  
[![Skin Melanin2.png](/images/thumb/7/71/Skin_Melanin2.png/64px-Skin_Melanin2.png)](/wiki/File:Skin_Melanin2.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (255, 239, 213)
  * Min melanin: 0.1

| **0** | **0** | 0.5  | SkinColor   
Skin_Melanin3  
[![Skin Melanin3.png](/images/thumb/0/0b/Skin_Melanin3.png/64px-Skin_Melanin3.png)](/wiki/File:Skin_Melanin3.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (255, 239, 201)
  * Min melanin: 0.25

| **0** | **0** | 0.5  | SkinColor   
Skin_Melanin4  
[![Skin Melanin4.png](/images/thumb/b/bf/Skin_Melanin4.png/64px-Skin_Melanin4.png)](/wiki/File:Skin_Melanin4.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (255, 239, 189)
  * Min melanin: 0.45

| **0** | **0** | 0.5  | SkinColor   
Skin_Melanin5  
[![Skin Melanin5.png](/images/thumb/a/a7/Skin_Melanin5.png/64px-Skin_Melanin5.png)](/wiki/File:Skin_Melanin5.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (249, 219, 165)
  * Min melanin: 0.58

| **0** | **0** | 0? 1?  | SkinColor   
Skin_Melanin6  
[![Skin Melanin6.png](/images/thumb/b/bb/Skin_Melanin6.png/64px-Skin_Melanin6.png)](/wiki/File:Skin_Melanin6.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (242, 199, 140)
  * Min melanin: 0.63

| **0** | **0** | 0? 1?  | SkinColor   
Skin_Melanin7  
[![Skin Melanin7.png](/images/thumb/5/51/Skin_Melanin7.png/64px-Skin_Melanin7.png)](/wiki/File:Skin_Melanin7.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (228, 158, 90)
  * Min melanin: 0.75

| **0** | **0** | 0? 1?  | SkinColor   
Skin_Melanin8  
[![Skin Melanin8.png](/images/thumb/4/4f/Skin_Melanin8.png/64px-Skin_Melanin8.png)](/wiki/File:Skin_Melanin8.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (130, 91, 48)
  * Min melanin: 0.83

| **0** | **0** | 0.5  | SkinColor   
Skin_Melanin9  
[![Skin Melanin9.png](/images/thumb/1/1f/Skin_Melanin9.png/64px-Skin_Melanin9.png)](/wiki/File:Skin_Melanin9.png) | _Carriers of this gene have a particular skin color. With multiple skin color genes, one is randomly selected._

* * *

  * Skin color base: (99, 70, 36)
  * Min melanin: 0.9

| **0** | **0** | 0.2  | SkinColor   
  
### Skin[[edit](/index.php?title=Genes&action=edit&section=22 "Edit section: Skin")]

These exotic (non-natural) skin colors do not appear on anyone without the gene. Like body type genes and hair genes, a person can have more than one skin color gene (e.g. [![Impid.png](/images/thumb/d/d8/Impid.png/20px-Impid.png)](/wiki/Impids "Impids")[Impids](/wiki/Impids "Impids") have three), and one will be chosen. 

All of these genes have a "random brightness factor" of 0.18 unless otherwise specified. 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Green skin  
[![FanGene SkinColor Green.png](/images/thumb/e/e2/FanGene_SkinColor_Green.png/64px-FanGene_SkinColor_Green.png)](/wiki/File:FanGene_SkinColor_Green.png) | _Carriers of this gene produce a pigment that gives their skin a green color._

* * *

  * Skin color override: (169,182,108)

| **0** | **0** | \-  | SkinColorOverride   
Deep yellow skin  
[![FanGene SkinColor Yellow Deep.png](/images/thumb/3/34/FanGene_SkinColor_Yellow_Deep.png/64px-FanGene_SkinColor_Yellow_Deep.png)](/wiki/File:FanGene_SkinColor_Yellow_Deep.png) | _Carriers of this gene produce a pigment that gives their skin a deep yellow color._

* * *

  * Skin color override: (204, 199, 65)

| **0** | **0** | \-  | SkinColorOverride   
Pale yellow skin  
[![FanGene SkinColor Yellow Pale.png](/images/thumb/3/3d/FanGene_SkinColor_Yellow_Pale.png/64px-FanGene_SkinColor_Yellow_Pale.png)](/wiki/File:FanGene_SkinColor_Yellow_Pale.png) | _Carriers of this gene produce a pigment that turns their skin a grayish yellow color._

* * *

  * Skin color override: (193, 165, 99)

| **0** | **0** | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | SkinColorOverride   
Orange skin  
[![FanGene SkinColor Orange.png](/images/thumb/4/4e/FanGene_SkinColor_Orange.png/64px-FanGene_SkinColor_Orange.png)](/wiki/File:FanGene_SkinColor_Orange.png) | _Carriers of this gene produce a pigment that gives their skin an orange color._

* * *

  * Skin color override: (210, 114, 63)
  * Random brightness factor: 0

| **0** | **0** | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | SkinColorOverride   
Deep red skin  
[![FanGene SkinColor Red Deep.png](/images/thumb/6/65/FanGene_SkinColor_Red_Deep.png/64px-FanGene_SkinColor_Red_Deep.png)](/wiki/File:FanGene_SkinColor_Red_Deep.png) | _Carriers of this gene produce a deep-red pigment that gives their skin an almost bloody appearance._

* * *

  * Skin color override: (150, 62, 62)

| **0** | **0** | [![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | SkinColorOverride   
Pale red skin  
[![FanGene SkinColor Red Pale.png](/images/thumb/b/b6/FanGene_SkinColor_Red_Pale.png/64px-FanGene_SkinColor_Red_Pale.png)](/wiki/File:FanGene_SkinColor_Red_Pale.png) | _Carriers of this gene produce a pigment that turns their skin a moderate red color._

* * *

  * Skin color override: (222, 106, 106)

| **0** | **0** | \-  | SkinColorOverride   
Purple skin  
[![FanGene SkinColor Purple.png](/images/thumb/5/50/FanGene_SkinColor_Purple.png/64px-FanGene_SkinColor_Purple.png)](/wiki/File:FanGene_SkinColor_Purple.png) | _Carriers of this gene produce a pigment that gives their skin a purple color._

* * *

  * Skin color override: (97, 87, 195)

| **0** | **0** | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | SkinColorOverride   
Blue skin  
[![FanGene SkinColor Blue.png](/images/thumb/c/cd/FanGene_SkinColor_Blue.png/64px-FanGene_SkinColor_Blue.png)](/wiki/File:FanGene_SkinColor_Blue.png) | _Carriers of this gene produce a pigment that turns their skin a blue color._

* * *

  * Skin color override: (100, 165, 193)

| **0** | **0** | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | SkinColorOverride   
Sheer white skin  
[![FanGene SkinColor White.png](/images/thumb/0/03/FanGene_SkinColor_White.png/64px-FanGene_SkinColor_White.png)](/wiki/File:FanGene_SkinColor_White.png) | _Carriers of this gene have sheer white skin, unlike natural skin tones, due to a special engineered reflective cell covering._

* * *

  * Skin color override: (250, 240, 240)
  * Random brightness factor: 0

| **0** | **0** | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | SkinColorOverride   
Light gray skin  
[![FanGene SkinColor Light Gray.png](/images/thumb/0/01/FanGene_SkinColor_Light_Gray.png/64px-FanGene_SkinColor_Light_Gray.png)](/wiki/File:FanGene_SkinColor_Light_Gray.png) | _Carriers of this produce a light-gray pigment in their skin._

* * *

  * Skin color override: (200, 200, 200)

| **0** | **0** | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") | SkinColorOverride   
Slate gray skin  
[![FanGene SkinColor Gray.png](/images/thumb/2/2c/FanGene_SkinColor_Gray.png/64px-FanGene_SkinColor_Gray.png)](/wiki/File:FanGene_SkinColor_Gray.png) | _Carriers of this gene produce a pigment that turns their skin slate gray._

* * *

  * Skin color override: (90, 90, 90)

| **0** | **0** | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | SkinColorOverride   
Ink black skin  
[![FanGene SkinColor Black.png](/images/thumb/5/57/FanGene_SkinColor_Black.png/64px-FanGene_SkinColor_Black.png)](/wiki/File:FanGene_SkinColor_Black.png) | _Carriers of this gene produce a pigment that turns their skin a pale black color almost as dark as ink._

* * *

  * Skin color override: (55, 55, 55)
  * Random brightness factor: 0

| **0** | **0** | \-  | SkinColorOverride   
  
## Miscellaneous[[edit](/index.php?title=Genes&action=edit&section=23 "Edit section: Miscellaneous")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Exclude   
---|---|---|---|---|---  
Strong stomach  
[![Gene StrongStomach.png](/images/thumb/e/e6/Gene_StrongStomach.png/64px-Gene_StrongStomach.png)](/wiki/File:Gene_StrongStomach.png) | _Carriers of this gene have an extra toxin-filtering organ in their stomach and will never suffer from food poisoning even after eating rotten food._

* * *

  * Immune to [food poisoning](/wiki/Food_poisoning "Food poisoning"). 
    * Does _not_ affect pre-existing conditions. Only prevents new illnesses.

| −1 | 1 | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | \-   
Robust digestion  
[![Gene RobustDigestion.png](/images/thumb/0/0c/Gene_RobustDigestion.png/64px-Gene_RobustDigestion.png)](/wiki/File:Gene_RobustDigestion.png) | _Carriers of this gene grow a multi-fold stomach, allowing them to digest raw foods more efficiently than baseline humans. In general, they get the same nutrition from raw food as from if it is cooked. They also don't mind the taste of raw food at all._

* * *

  * [Raw Nutrition Multiplier](/wiki/Raw_Nutrition_Multiplier "Raw Nutrition Multiplier") ×180%
    * Note: Does not apply to [insect jelly](/wiki/Insect_jelly "Insect jelly") or fertilized [eggs](/wiki/Eggs "Eggs"). _Does_ apply to unfertilized eggs.
  * Removes mood: Ate raw food: -7
  * Note: Does _not_ prevent [food poisoning](/wiki/Food_poisoning "Food poisoning").

| −2 | 2 | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | \-   
Slow study  
[![Gene SlowLearning.png](/images/thumb/3/39/Gene_SlowLearning.png/64px-Gene_SlowLearning.png)](/wiki/File:Gene_SlowLearning.png) | _Carriers of this gene have deficient long-term memories and don't understand new ideas quickly. They are slow at learning new skills and knowledge._

* * *

  * [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") ×50%

| +2 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | Learning   
Quick study  
[![Gene FastLearning.png](/images/thumb/a/ac/Gene_FastLearning.png/64px-Gene_FastLearning.png)](/wiki/File:Gene_FastLearning.png) | _Carriers of this gene have excellent memories and grasp new ideas quickly. They learn faster than others._

* * *

  * [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") +50%

| −3 | 2 | \-  | Learning   
Nearsighted  
[![Gene Nearsighted.png](/images/thumb/7/7f/Gene_Nearsighted.png/64px-Gene_Nearsighted.png)](/wiki/File:Gene_Nearsighted.png) | _Carriers of this gene have difficulty seeing at a distance. Their shooting accuracy at long ranges is reduced._

* * *

  * Accuracy factor (long) ×25%
  * Accuracy factor (medium) ×50%

| +2 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | ShootingAccuracy   
Dark vision  
[![Gene Darkvision.png](/images/thumb/6/6b/Gene_Darkvision.png/64px-Gene_Darkvision.png)](/wiki/File:Gene_Darkvision.png) | _Carriers of this gene see well in low light and are unaffected by mood penalties related to darkness. They have a reflective layer behind the retina that amplifies their ability to see in the dark._

* * *

  * Negates the [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") penalty from [darkness](/wiki/Light "Light").
  * Negates the [Move Speed](/wiki/Move_Speed "Move Speed") penalty from darkness. **Note:** This effect is not mentioned by the in-game description
  * Removes [mood](/wiki/Mood "Mood"): Darkness: −5

| −1 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | \-   
Inbred  
[![Gene Inbred.png](/images/thumb/f/f3/Gene_Inbred.png/64px-Gene_Inbred.png)](/wiki/File:Gene_Inbred.png) | _This genetic condition affects a person's fertility, immunity, and mental capacity._

* * *

  * Forced trait: [Slow learner](/wiki/Slow_learner "Slow learner")
  * [Fertility](/wiki/Fertility "Fertility") ×50%
  * [Immunity gain speed](/wiki/Immunity_gain_speed "Immunity gain speed") ×85%
  * Note: Despite being harmful, this gene also lowers metabolic efficiency.
  * See [inbreeding](/wiki/Reproduction#Inbreeding "Reproduction") for full details.

| −2 | 1 | \-  | \-   
Mild cell instability  
[![Gene MildCellInstability.png](/images/thumb/1/1c/Gene_MildCellInstability.png/64px-Gene_MildCellInstability.png)](/wiki/File:Gene_MildCellInstability.png) | _Carriers of this gene need less metabolic energy to stay alive, at the cost of reduced stability in their cell-replication machinery._

* * *

  * [Lifespan Factor](/wiki/Lifespan_Factor "Lifespan Factor") ×80%
    * Note this means age-related diseases come earlier, e.g. [Frail](/wiki/Ailments#Frail "Ailments") can happen at 40 instead of 50
  * [Cancer Rate Factor](/wiki/Cancer_Rate_Factor "Cancer Rate Factor") ×300%
  * [Immunity gain speed](/wiki/Immunity_gain_speed "Immunity gain speed") ×96%

| +2 | 1 | \-  | CellInstability   
Major cell instability  
[![Gene MajorCellInstability.png](/images/thumb/a/ad/Gene_MajorCellInstability.png/64px-Gene_MajorCellInstability.png)](/wiki/File:Gene_MajorCellInstability.png) | _Carriers of this gene need much less metabolic energy to stay alive, at the cost of greatly-reduced stability in their cell-replication machinery._

* * *

  * [Lifespan Factor](/wiki/Lifespan_Factor "Lifespan Factor") ×60%
    * Note this means age-related diseases come earlier, e.g. [Frail](/wiki/Ailments#Frail "Ailments") can happen at 30 instead of 50
  * [Cancer Rate Factor](/wiki/Cancer_Rate_Factor "Cancer Rate Factor") ×500%
  * [Immunity gain speed](/wiki/Immunity_gain_speed "Immunity gain speed") ×92%

| +4 | 1 | \-  | CellInstability   
Grayless hair  
[![Gene GreylessHair.png](/images/thumb/7/7e/Gene_GreylessHair.png/64px-Gene_GreylessHair.png)](/wiki/File:Gene_GreylessHair.png) | _Carriers of this gene keep their natural hair color as they age._

* * *

  * No age-related gray hair.

| **0** | 1 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | \-   
Human hands  
[![Gene HandsHuman.png](/images/thumb/f/f9/Gene_HandsHuman.png/64px-Gene_HandsHuman.png)](/wiki/File:Gene_HandsHuman.png) | _Carriers of this gene have regular human hands._

* * *

| **0** | **0** | \-  | Hands   
Trotter hands  
[![Gene HandsTrotter.png](/images/thumb/0/01/Gene_HandsTrotter.png/64px-Gene_HandsTrotter.png)](/wiki/File:Gene_HandsTrotter.png) | _Carriers of this gene have hands that partially resemble pig trotters. This reduces their ability to manipulate objects._

* * *

  * [Manipulation](/wiki/Manipulation "Manipulation") ×85%

| +1 | 1 | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Hands   
Elongated fingers  
[![Gene ElongatedFingers.png](/images/thumb/e/e2/Gene_ElongatedFingers.png/64px-Gene_ElongatedFingers.png)](/wiki/File:Gene_ElongatedFingers.png) | _Long, delicate fingers improve the carrier's manipulation capacity. This aids with many tasks, especially crafting and construction._

* * *

  * [Manipulation](/wiki/Manipulation "Manipulation") ×110%

| −1 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies") | Hands   
Furskin  
[![Gene Furskin.png](/images/thumb/7/73/Gene_Furskin.png/64px-Gene_Furskin.png)](/wiki/File:Gene_Furskin.png) | _Carriers of this gene grow thick fur all over their body, which protects them from cold temperatures._

* * *

  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −10 °C (18 °F)
  * [Non-furskin romance chance](/wiki/Romance "Romance") ×20%
  * [![Content from Rimworld core game only](/images/thumb/1/19/RimWorldLogo.png/16px-RimWorldLogo.png)](/wiki/File:RimWorldLogo.png "Content from Rimworld core game only")Removes mood: Naked: -6
  * [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Removes mood: Uncovered (body part): -4
  * [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Removes opinion: Uncovered (body part): -10 of any other pawns

| −1 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | HairStyle  
Fur  
BeardStyle  
  
Pig nose  
[![Gene NosePig.png](/images/thumb/0/08/Gene_NosePig.png/64px-Gene_NosePig.png)](/wiki/File:Gene_NosePig.png) | _Carriers of this gene have pig-like snouts._

* * *

  * [Non-pig nose romance chance](/wiki/Romance "Romance") ×20%

| **0** | **0** | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins") | Nose   
Pollution stimulus  
[![Gene PollutionRush.png](/images/thumb/6/66/Gene_PollutionRush.png/64px-Gene_PollutionRush.png)](/wiki/File:Gene_PollutionRush.png) | _Carriers of this gene get a chemical rush from being exposed to pollution. This makes them move faster and helps them think clearer. A similar gene is found in combat-engineered mega-insects._

* * *

  * Gain stat bonuses when exposed to pollution. 
    * Increases move speed and consciousness. See [Pollution stimulus](/wiki/Pollution_stimulus "Pollution stimulus") for full details.

| −1 | 1 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | \-   
Unstoppable  
[![Gene Unstoppable.png](/images/thumb/2/2d/Gene_Unstoppable.png/64px-Gene_Unstoppable.png)](/wiki/File:Gene_Unstoppable.png) | _Carriers of this gene are not slowed down when taking damage._

* * *

  * [Stagger Time Multiplier](/wiki/Stagger_Time_Multiplier "Stagger Time Multiplier") ×0%

| −2 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | \-   
Furry tail  
[![Gene TailFurry.png](/images/thumb/0/0e/Gene_TailFurry.png/64px-Gene_TailFurry.png)](/wiki/File:Gene_TailFurry.png) | _Carriers of this gene grow a fluffy tail which partially protects them from cold temperatures._

* * *

  * [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −10 °C (−18 °F)
  * Adds an aesthetic only tail to the pawn's sprite
  * Note: Does **not** add a targetable or damageable [body part](/wiki/Body_part "Body part")

| −1 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | Tail   
Smooth tail  
[![Gene TailSmooth.png](/images/thumb/c/c6/Gene_TailSmooth.png/64px-Gene_TailSmooth.png)](/wiki/File:Gene_TailSmooth.png) | _Carriers of this gene grow a slender tail that can act as a dexterous fifth limb._

* * *

  * [Manipulation](/wiki/Manipulation "Manipulation"): +5%
  * Adds an aesthetic only tail to the pawn's sprite
  * Note: Does **not** add a targetable or damageable [body part](/wiki/Body_part "Body part")

| −1 | 1 | \-  | Tail   
Indoor dweller  
[![Gene CaveDweller.png](/images/thumb/e/e0/Gene_CaveDweller.png/64px-Gene_CaveDweller.png)](/wiki/File:Gene_CaveDweller.png) | _Carriers of this gene have no need for the outdoors and will never feel cooped up no matter how long they stay inside._

* * *

  * Disables need: [Outdoors](/wiki/Outdoors "Outdoors")

| −1 | 1 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | \-   
Low gravity adapted [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")  
[![Gene LowGravityAdapted.png](/images/thumb/d/d6/Gene_LowGravityAdapted.png/64px-Gene_LowGravityAdapted.png)](/wiki/File:Gene_LowGravityAdapted.png) | _Carriers of this gene move and work more easily in low-gravity environments. However They're slower and less efficient when planetside._

* * *

  * [Move Speed](/wiki/Move_Speed "Move Speed"): −0.2 c/s (planetside)
  * [Global work speed](/wiki/Global_work_speed "Global work speed") −10% (planetside)
  * [Move Speed](/wiki/Move_Speed "Move Speed"): +0.4 c/s (in space)
  * [Global work speed](/wiki/Global_work_speed "Global work speed") +10% (in space)

| +1 | 1 | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | \-   
  
## Aptitudes[[edit](/index.php?title=Genes&action=edit&section=24 "Edit section: Aptitudes")]

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes") | Skill   
---|---|---|---|---|---  
Awful Animals  
[![Gene AwfulAnimals.png](/images/thumb/4/43/Gene_AwfulAnimals.png/64px-Gene_AwfulAnimals.png)](/wiki/File:Gene_AwfulAnimals.png) | _The carrier's aptitude in Animals is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Animals._

* * *

  * [Animals](/wiki/Skills#Animals "Skills"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Animals](/wiki/Skills#Animals "Skills")

| +2 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | Animals   
Awful Artistic  
[![Gene AwfulArtistic.png](/images/thumb/5/5b/Gene_AwfulArtistic.png/64px-Gene_AwfulArtistic.png)](/wiki/File:Gene_AwfulArtistic.png) | _The carrier's aptitude in Artistic is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Artistic._

* * *

  * [Artistic](/wiki/Artistic "Artistic"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Artistic](/wiki/Artistic "Artistic")

| +2 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | Artistic   
Awful Construction  
[![Gene AwfulConstruction.png](/images/thumb/d/dc/Gene_AwfulConstruction.png/64px-Gene_AwfulConstruction.png)](/wiki/File:Gene_AwfulConstruction.png) | _The carrier's aptitude in Construction is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Construction._

* * *

  * [Construction](/wiki/Construction "Construction"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Construction](/wiki/Construction "Construction")

| +2 | 1 | \-  | Construction   
Awful Cooking  
[![Gene AwfulCooking.png](/images/thumb/d/d1/Gene_AwfulCooking.png/64px-Gene_AwfulCooking.png)](/wiki/File:Gene_AwfulCooking.png) | _The carrier's aptitude in Cooking is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Cooking._

* * *

  * [Cooking](/wiki/Cooking "Cooking"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Cooking](/wiki/Cooking "Cooking")

| +2 | 1 | \-  | Cooking   
Awful Crafting  
[![Gene AwfulCrafting.png](/images/thumb/4/44/Gene_AwfulCrafting.png/64px-Gene_AwfulCrafting.png)](/wiki/File:Gene_AwfulCrafting.png) | _The carrier's aptitude in Crafting is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Crafting._

* * *

  * [Crafting](/wiki/Crafting "Crafting"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Crafting](/wiki/Crafting "Crafting")

| +2 | 1 | \-  | Crafting   
Awful Medical  
[![Gene AwfulMedical.png](/images/thumb/5/55/Gene_AwfulMedical.png/64px-Gene_AwfulMedical.png)](/wiki/File:Gene_AwfulMedical.png) | _The carrier's aptitude in Medical is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Medical._

* * *

  * [Medical](/wiki/Medical "Medical"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Medical](/wiki/Medical "Medical")

| +2 | 1 | \-  | Medical   
Awful Melee  
[![Gene AwfulMelee.png](/images/thumb/1/12/Gene_AwfulMelee.png/64px-Gene_AwfulMelee.png)](/wiki/File:Gene_AwfulMelee.png) | _The carrier's aptitude in Melee is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Melee._

* * *

  * [Melee](/wiki/Melee "Melee"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Melee](/wiki/Melee "Melee")

| +2 | 1 | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | Melee   
Awful Mining  
[![Gene AwfulMining.png](/images/thumb/a/a7/Gene_AwfulMining.png/64px-Gene_AwfulMining.png)](/wiki/File:Gene_AwfulMining.png) | _The carrier's aptitude in Mining is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Mining._

* * *

  * [Mining](/wiki/Mining "Mining"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Mining](/wiki/Mining "Mining")

| +2 | 1 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin")[![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates")[![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | Mining   
Awful Intellectual  
[![Gene AwfulIntellectual.png](/images/thumb/8/81/Gene_AwfulIntellectual.png/64px-Gene_AwfulIntellectual.png)](/wiki/File:Gene_AwfulIntellectual.png) | _The carrier's aptitude in Intellectual is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Intellectual._

* * *

  * [Intellectual](/wiki/Intellectual "Intellectual"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Intellectual](/wiki/Intellectual "Intellectual")

| +2 | 1 | \-  | Intellectual   
Awful Plants  
[![Gene AwfulPlants.png](/images/thumb/f/f6/Gene_AwfulPlants.png/64px-Gene_AwfulPlants.png)](/wiki/File:Gene_AwfulPlants.png) | _The carrier's aptitude in Plants is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Plants._

* * *

  * [Plants](/wiki/Skills#Plants "Skills"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Plants](/wiki/Skills#Plants "Skills")

| +2 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")[![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Plants   
Awful Shooting  
[![Gene AwfulShooting.png](/images/thumb/8/8e/Gene_AwfulShooting.png/64px-Gene_AwfulShooting.png)](/wiki/File:Gene_AwfulShooting.png) | _The carrier's aptitude in Shooting is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Shooting._

* * *

  * [Shooting](/wiki/Shooting "Shooting"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Shooting](/wiki/Shooting "Shooting")

| +2 | 1 | \-  | Shooting   
Awful Social  
[![Gene AwfulSocial.png](/images/thumb/c/c4/Gene_AwfulSocial.png/64px-Gene_AwfulSocial.png)](/wiki/File:Gene_AwfulSocial.png) | _The carrier's aptitude in Social is reduced by 8. Aptitude acts like an offset on skill level. Additionally, all passion is removed from Social._

* * *

  * [Social](/wiki/Skills#Social "Skills"): −8. Note: Experience gain and decay applies as if this offset did not exist.
  * Removes all [passions](/wiki/Passion "Passion") for [Social](/wiki/Skills#Social "Skills")

| +2 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | Social   
  
Poor Animals  
[![Gene PoorAnimals.png](/images/thumb/d/d4/Gene_PoorAnimals.png/64px-Gene_PoorAnimals.png)](/wiki/File:Gene_PoorAnimals.png) | _The carrier's aptitude in Animals is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Animals](/wiki/Skills#Animals "Skills"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | Animals   
Poor Artistic  
[![Gene PoorArtistic.png](/images/thumb/4/43/Gene_PoorArtistic.png/64px-Gene_PoorArtistic.png)](/wiki/File:Gene_PoorArtistic.png) | _The carrier's aptitude in Artistic is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Artistic](/wiki/Artistic "Artistic"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | Artistic   
Poor Construction  
[![Gene PoorConstruction.png](/images/thumb/8/88/Gene_PoorConstruction.png/64px-Gene_PoorConstruction.png)](/wiki/File:Gene_PoorConstruction.png) | _The carrier's aptitude in Construction is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Construction](/wiki/Construction "Construction"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | \-  | Construction   
Poor Cooking  
[![Gene PoorCooking.png](/images/thumb/4/46/Gene_PoorCooking.png/64px-Gene_PoorCooking.png)](/wiki/File:Gene_PoorCooking.png) | _The carrier's aptitude in Cooking is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Cooking](/wiki/Cooking "Cooking"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Pigskins](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Pigskins") [![Pigskins](/images/thumb/6/67/PigskinXenotype.png/32px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins")[![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters") | Cooking   
Poor Crafting  
[![Gene PoorCrafting.png](/images/thumb/a/ab/Gene_PoorCrafting.png/64px-Gene_PoorCrafting.png)](/wiki/File:Gene_PoorCrafting.png) | _The carrier's aptitude in Crafting is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Crafting](/wiki/Crafting "Crafting"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | \-  | Crafting   
Poor Medical  
[![Gene PoorMedical.png](/images/thumb/4/4a/Gene_PoorMedical.png/64px-Gene_PoorMedical.png)](/wiki/File:Gene_PoorMedical.png) | _The carrier's aptitude in Medical is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Medical](/wiki/Medical "Medical"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | \-  | Medical   
Poor Melee  
[![Gene PoorMelee.png](/images/thumb/9/93/Gene_PoorMelee.png/64px-Gene_PoorMelee.png)](/wiki/File:Gene_PoorMelee.png) | _The carrier's aptitude in Melee is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Melee](/wiki/Melee "Melee"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | \-  | Melee   
Poor Mining  
[![Gene PoorMining.png](/images/thumb/8/81/Gene_PoorMining.png/64px-Gene_PoorMining.png)](/wiki/File:Gene_PoorMining.png) | _The carrier's aptitude in Mining is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Mining](/wiki/Mining "Mining"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | \-  | Mining   
Poor Intellectual  
[![Gene PoorIntellectual.png](/images/thumb/9/99/Gene_PoorIntellectual.png/64px-Gene_PoorIntellectual.png)](/wiki/File:Gene_PoorIntellectual.png) | _The carrier's aptitude in Intellectual is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Intellectual](/wiki/Intellectual "Intellectual"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | Intellectual   
Poor Plants  
[![Gene PoorPlants.png](/images/thumb/6/6d/Gene_PoorPlants.png/64px-Gene_PoorPlants.png)](/wiki/File:Gene_PoorPlants.png) | _The carrier's aptitude in Plants is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Plants](/wiki/Skills#Plants "Skills"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies")[![Impids](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Impids") [![Impids](/images/thumb/d/d8/Impid.png/32px-Impid.png)](/wiki/Impids "Impids") | Plants   
Poor Shooting  
[![Gene PoorShooting.png](/images/thumb/d/dd/Gene_PoorShooting.png/64px-Gene_PoorShooting.png)](/wiki/File:Gene_PoorShooting.png) | _The carrier's aptitude in Shooting is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Shooting](/wiki/Shooting "Shooting"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | Shooting   
Poor Social  
[![Gene PoorSocial.png](/images/thumb/9/95/Gene_PoorSocial.png/64px-Gene_PoorSocial.png)](/wiki/File:Gene_PoorSocial.png) | _The carrier's aptitude in Social is reduced by 4. Aptitude acts like an offset on skill level._

* * *

  * [Social](/wiki/Skills#Social "Skills"): −4. Note: Experience gain and decay applies as if this offset did not exist.

| +1 | 1 | [![Neanderthals](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Neanderthals") [![Neanderthals](/images/thumb/9/91/Neanderthal.png/32px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals") | Social   
Strong Animals  
[![Gene StrongAnimals.png](/images/thumb/7/7a/Gene_StrongAnimals.png/64px-Gene_StrongAnimals.png)](/wiki/File:Gene_StrongAnimals.png) | _The carrier's aptitude in Animals is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Animals](/wiki/Skills#Animals "Skills"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Animals   
Strong Artistic  
[![Gene StrongArtistic.png](/images/thumb/5/59/Gene_StrongArtistic.png/64px-Gene_StrongArtistic.png)](/wiki/File:Gene_StrongArtistic.png) | _The carrier's aptitude in Artistic is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Artistic](/wiki/Artistic "Artistic"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Artistic   
Strong Construction  
[![Gene StrongConstruction.png](/images/thumb/e/e0/Gene_StrongConstruction.png/64px-Gene_StrongConstruction.png)](/wiki/File:Gene_StrongConstruction.png) | _The carrier's aptitude in Construction is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Construction](/wiki/Construction "Construction"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Construction   
Strong Cooking  
[![Gene StrongCooking.png](/images/thumb/7/72/Gene_StrongCooking.png/64px-Gene_StrongCooking.png)](/wiki/File:Gene_StrongCooking.png) | _The carrier's aptitude in Cooking is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Cooking](/wiki/Cooking "Cooking"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Cooking   
Strong Crafting  
[![Gene StrongCrafting.png](/images/thumb/4/45/Gene_StrongCrafting.png/64px-Gene_StrongCrafting.png)](/wiki/File:Gene_StrongCrafting.png) | _The carrier's aptitude in Crafting is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Crafting](/wiki/Crafting "Crafting"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Crafting   
Strong Medical  
[![Gene StrongMedical.png](/images/thumb/d/d7/Gene_StrongMedical.png/64px-Gene_StrongMedical.png)](/wiki/File:Gene_StrongMedical.png) | _The carrier's aptitude in Medical is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Medical](/wiki/Medical "Medical"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Medical   
Strong Melee  
[![Gene StrongMelee.png](/images/thumb/2/23/Gene_StrongMelee.png/64px-Gene_StrongMelee.png)](/wiki/File:Gene_StrongMelee.png) | _The carrier's aptitude in Melee is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Melee](/wiki/Melee "Melee"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Melee   
Strong Mining  
[![Gene StrongMining.png](/images/thumb/1/13/Gene_StrongMining.png/64px-Gene_StrongMining.png)](/wiki/File:Gene_StrongMining.png) | _The carrier's aptitude in Mining is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Mining](/wiki/Mining "Mining"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Mining   
Strong Intellectual  
[![Gene StrongIntellectual.png](/images/thumb/d/d5/Gene_StrongIntellectual.png/64px-Gene_StrongIntellectual.png)](/wiki/File:Gene_StrongIntellectual.png) | _The carrier's aptitude in Intellectual is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Intellectual](/wiki/Intellectual "Intellectual"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Intellectual   
Strong Plants  
[![Gene StrongPlants.png](/images/thumb/6/6e/Gene_StrongPlants.png/64px-Gene_StrongPlants.png)](/wiki/File:Gene_StrongPlants.png) | _The carrier's aptitude in Plants is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Plants](/wiki/Skills#Plants "Skills"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Plants   
Strong Shooting  
[![Gene StrongShooting.png](/images/thumb/e/ef/Gene_StrongShooting.png/64px-Gene_StrongShooting.png)](/wiki/File:Gene_StrongShooting.png) | _The carrier's aptitude in Shooting is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Shooting](/wiki/Shooting "Shooting"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | \-  | Shooting   
Strong Social  
[![Gene StrongSocial.png](/images/thumb/4/47/Gene_StrongSocial.png/64px-Gene_StrongSocial.png)](/wiki/File:Gene_StrongSocial.png) | _The carrier's aptitude in Social is increased by 4. Aptitude acts like an offset on skill level._

* * *

  * [Social](/wiki/Skills#Social "Skills"): +4. Note: Experience gain and decay applies as if this offset did not exist.

| −1 | 2 | [![Sanguophages](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Sanguophages") [![Sanguophages](/images/thumb/8/8c/Sanguophage.png/32px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages") | Social   
  
Great Animals  
[![Gene GreatAnimals.png](/images/thumb/5/59/Gene_GreatAnimals.png/64px-Gene_GreatAnimals.png)](/wiki/File:Gene_GreatAnimals.png) | _The carrier's aptitude in Animals is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Animals._

* * *

  * [Animals](/wiki/Skills#Animals "Skills"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Animals](/wiki/Skills#Animals "Skills")

| −3 | 2 | [![Yttakin](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Yttakin") [![Yttakin](/images/thumb/e/ee/Yttakin.png/32px-Yttakin.png)](/wiki/Yttakin "Yttakin") | Animals[A]  
Great Artistic  
[![Gene GreatArtistic.png](/images/thumb/8/83/Gene_GreatArtistic.png/64px-Gene_GreatArtistic.png)](/wiki/File:Gene_GreatArtistic.png) | _The carrier's aptitude in Artistic is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Artistic._

* * *

  * [Artistic](/wiki/Artistic "Artistic"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Artistic](/wiki/Artistic "Artistic")

| −3 | 2 | \-  | Artistic[A]  
Great Construction  
[![Gene GreatConstruction.png](/images/thumb/0/0a/Gene_GreatConstruction.png/64px-Gene_GreatConstruction.png)](/wiki/File:Gene_GreatConstruction.png) | _The carrier's aptitude in Construction is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Construction._

* * *

  * [Construction](/wiki/Construction "Construction"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Construction](/wiki/Construction "Construction")

| −3 | 2 | [![Starjack](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Starjack") [![Starjack](/images/thumb/3/30/Starjack.png/32px-Starjack.png)](/wiki/Starjack "Starjack") | Construction[A]  
Great Cooking  
[![Gene GreatCooking.png](/images/thumb/b/b9/Gene_GreatCooking.png/64px-Gene_GreatCooking.png)](/wiki/File:Gene_GreatCooking.png) | _The carrier's aptitude in Cooking is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Cooking._

* * *

  * [Cooking](/wiki/Cooking "Cooking"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Cooking](/wiki/Cooking "Cooking")

| −3 | 2 | \-  | Cooking[A]  
Great Crafting  
[![Gene GreatCrafting.png](/images/thumb/9/91/Gene_GreatCrafting.png/64px-Gene_GreatCrafting.png)](/wiki/File:Gene_GreatCrafting.png) | _The carrier's aptitude in Crafting is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Crafting._

* * *

  * [Crafting](/wiki/Crafting "Crafting"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Crafting](/wiki/Crafting "Crafting")

| −3 | 2 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies") | Crafting[A]  
Great Medical  
[![Gene GreatMedical.png](/images/thumb/5/5d/Gene_GreatMedical.png/64px-Gene_GreatMedical.png)](/wiki/File:Gene_GreatMedical.png) | _The carrier's aptitude in Medical is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Medical._

* * *

  * [Medical](/wiki/Medical "Medical"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Medical](/wiki/Medical "Medical")

| −3 | 2 | \-  | Medical[A]  
Great Melee  
[![Gene GreatMelee.png](/images/thumb/9/95/Gene_GreatMelee.png/64px-Gene_GreatMelee.png)](/wiki/File:Gene_GreatMelee.png) | _The carrier's aptitude in Melee is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Melee._

* * *

  * [Melee](/wiki/Melee "Melee"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Melee](/wiki/Melee "Melee")

| −3 | 2 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | Melee[A]  
Great Mining  
[![Gene GreatMining.png](/images/thumb/6/6f/Gene_GreatMining.png/64px-Gene_GreatMining.png)](/wiki/File:Gene_GreatMining.png) | _The carrier's aptitude in Mining is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Mining._

* * *

  * [Mining](/wiki/Mining "Mining"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Mining](/wiki/Mining "Mining")

| −3 | 2 | [![Dirtmoles](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Dirtmoles") [![Dirtmoles](/images/thumb/c/c4/Dirtmole.png/32px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles") | Mining[A]  
Great Intellectual  
[![Gene GreatIntellectual.png](/images/thumb/6/6d/Gene_GreatIntellectual.png/64px-Gene_GreatIntellectual.png)](/wiki/File:Gene_GreatIntellectual.png) | _The carrier's aptitude in Intellectual is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Intellectual._

* * *

  * [Intellectual](/wiki/Intellectual "Intellectual"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Intellectual](/wiki/Intellectual "Intellectual")

| −3 | 2 | [![Genies](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Genies") [![Genies](/images/thumb/8/8c/Genie.png/32px-Genie.png)](/wiki/Genies "Genies") | Intellectual[A]  
Great Plants  
[![Gene GreatPlants.png](/images/thumb/2/28/Gene_GreatPlants.png/64px-Gene_GreatPlants.png)](/wiki/File:Gene_GreatPlants.png) | _The carrier's aptitude in Plants is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Plants._

* * *

  * [Plants](/wiki/Skills#Plants "Skills"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Plants](/wiki/Skills#Plants "Skills")

| −3 | 2 | \-  | Plants[A]  
Great Shooting  
[![Gene GreatShooting.png](/images/thumb/8/83/Gene_GreatShooting.png/64px-Gene_GreatShooting.png)](/wiki/File:Gene_GreatShooting.png) | _The carrier's aptitude in Shooting is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Shooting._

* * *

  * [Shooting](/wiki/Shooting "Shooting"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Shooting](/wiki/Shooting "Shooting")

| −3 | 2 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars") | Shooting[A]  
Great Social  
[![Gene GreatSocial.png](/images/thumb/2/2f/Gene_GreatSocial.png/64px-Gene_GreatSocial.png)](/wiki/File:Gene_GreatSocial.png) | _The carrier's aptitude in Social is increased by 8. Aptitude acts like an offset on skill level. Additionally, one level of passion is added to Social._

* * *

  * [Social](/wiki/Skills#Social "Skills"): +8. Note: Experience gain and decay applies as if this offset did not exist.
  * Adds one additional [passion](/wiki/Passion "Passion") for [Social](/wiki/Skills#Social "Skills")

| −3 | 2 | [![Highmates](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Highmates") [![Highmates](/images/thumb/9/9c/Highmate.png/32px-Highmate.png)](/wiki/Highmates "Highmates") | Social[A]  
  
    **^A** If overridden by strong or poor aptitude gene, passion from great aptitude gene is added anyway.

## Drugs[[edit](/index.php?title=Genes&action=edit&section=25 "Edit section: Drugs")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Genes&action=edit). Reason:** _How does impervious eliminate tolerance build up - is it -100% or x0%. Both are listed._  
---|---  
[![AncientTerminal east.png](/images/thumb/0/02/AncientTerminal_east.png/40px-AncientTerminal_east.png)](/wiki/Category:Pages_to_be_recoded "Category:Pages to be recoded") | This section has been suggested for [recoding](/wiki/Category:Pages_to_be_recoded "Category:Pages to be recoded"). **Reason:** _The patch notes for 1.5 say that drug-related genes no longer prevent overdose across all drugs. Verify if true, then edit this section to reflect the change_. You can help RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Genes&action=edit)** it.  
---|---  
  
There are one of each of these for each drug, except for [ambrosia](/wiki/Ambrosia "Ambrosia"), [luciferium](/wiki/Luciferium "Luciferium") and [penoxycyline](/wiki/Penoxycyline "Penoxycyline"). 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Baseliner.png](/images/thumb/8/84/Baseliner.png/20px-Baseliner.png)](/wiki/Xenotypes "Xenotypes")  
---|---|---|---|---  
Alcohol resistant  
[![AddictionResistant Alcohol.png](/images/thumb/e/e9/AddictionResistant_Alcohol.png/64px-AddictionResistant_Alcohol.png)](/wiki/File:AddictionResistant_Alcohol.png) | _Carriers are only half as likely to become addicted to Alcohol._

* * *

  * [Alcohol](/wiki/Beer "Beer") addiction factor: ×50%
  * Alcohol tolerance gain: ×50%

| −1 | 1 | \-   
Smokeleaf resistant  
[![AddictionResistant Smokeleaf.png](/images/thumb/a/ad/AddictionResistant_Smokeleaf.png/64px-AddictionResistant_Smokeleaf.png)](/wiki/File:AddictionResistant_Smokeleaf.png) | _Carriers are only half as likely to become addicted to Smokeleaf._

* * *

  * [Smokeleaf](/wiki/Smokeleaf_joint "Smokeleaf joint") addiction factor: ×50%
  * Smokeleaf tolerance gain: ×50%

| −1 | 1 | \-   
Psychite resistant  
[![AddictionResistant Psychite.png](/images/thumb/b/b0/AddictionResistant_Psychite.png/64px-AddictionResistant_Psychite.png)](/wiki/File:AddictionResistant_Psychite.png) | _Carriers are only half as likely to become addicted to Psychite._

* * *

  * [Psychite](/wiki/Psychite "Psychite") addiction factor: ×50%
  * Psychite tolerance gain: ×50%
  * Overdose chance: ×50% [Random or All]

| −2 | 1 | \-   
Go-juice resistant  
[![AddictionResistant Go Juice.png](/images/thumb/5/57/AddictionResistant_Go_Juice.png/64px-AddictionResistant_Go_Juice.png)](/wiki/File:AddictionResistant_Go_Juice.png) | _Carriers are only half as likely to become addicted to Go-juice._

* * *

  * [Go-juice](/wiki/Go-juice "Go-juice") addiction factor: ×50%
  * Overdose chance: ×50% [Random or All]

| −2 | 1 | \-   
Wake-up resistant  
[![AddictionResistant Wake Up.png](/images/thumb/2/21/AddictionResistant_Wake_Up.png/64px-AddictionResistant_Wake_Up.png)](/wiki/File:AddictionResistant_Wake_Up.png) | _Carriers are only half as likely to become addicted to Wake-up._

* * *

  * [Wake-up](/wiki/Wake-up "Wake-up") addiction factor: ×50%
  * Overdose chance: ×50% [Only this drug?] [Random or All?]

| −2 | 1 | \-   
Alcohol impervious  
[![AddictionImmune Alcohol.png](/images/thumb/8/8e/AddictionImmune_Alcohol.png/64px-AddictionImmune_Alcohol.png)](/wiki/File:AddictionImmune_Alcohol.png) | _Carriers of this gene never get addicted to Alcohol._

* * *

  * Alcohol addiction factor: x0%
  * Tolerance build-up for Alcohol: -100%

| −3 | 2 | \-   
Smokeleaf impervious  
[![AddictionImmune Smokeleaf.png](/images/thumb/c/cd/AddictionImmune_Smokeleaf.png/64px-AddictionImmune_Smokeleaf.png)](/wiki/File:AddictionImmune_Smokeleaf.png) | _Carriers of this gene never get addicted to Smokeleaf._

* * *

  * Smokeleaf addiction factor: x0%
  * Tolerance build-up for Smokeleaf: -100%

| −3 | 2 | \-   
Psychite impervious  
[![AddictionImmune Psychite.png](/images/thumb/d/d5/AddictionImmune_Psychite.png/64px-AddictionImmune_Psychite.png)](/wiki/File:AddictionImmune_Psychite.png) | _Carriers of this gene never get addicted to Psychite._

* * *

  * Psychite addiction factor: x0%
  * Tolerance build-up for Psychite: ×0%
  * Cumulative [overdose severity](/wiki/Overdose "Overdose") and random, per-dose overdose chance from Psychite based drugs eliminated.

| −5 | 2 | \-   
Go-juice impervious  
[![AddictionImmune Go Juice.png](/images/thumb/4/4c/AddictionImmune_Go_Juice.png/64px-AddictionImmune_Go_Juice.png)](/wiki/File:AddictionImmune_Go_Juice.png) | _Carriers of this gene never get addicted to Go-juice._

* * *

  * Go-juice addiction factor: x0%
  * Cumulative [overdose severity](/wiki/Overdose "Overdose") and random, per-dose overdose chance from Go-juice eliminated.

| −5 | 2 | \-   
Wake-up impervious  
[![AddictionImmune Wake Up.png](/images/thumb/d/df/AddictionImmune_Wake_Up.png/64px-AddictionImmune_Wake_Up.png)](/wiki/File:AddictionImmune_Wake_Up.png) | _Carriers of this gene never get addicted to Wake-up._

* * *

  * Wake-up addiction factor: x0%
  * Cumulative [overdose severity](/wiki/Overdose "Overdose") and random, per-dose overdose chance from Wake-up eliminated.

| −5 | 2 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters")  
Alcohol dependency  
[![ChemicalDependency Alcohol.png](/images/thumb/8/85/ChemicalDependency_Alcohol.png/64px-ChemicalDependency_Alcohol.png)](/wiki/File:ChemicalDependency_Alcohol.png) | _Carriers of this gene need to ingest alcohol on a regular basis to survive. After 5 days without alcohol, carriers will suffer from drug deficiency. After 30 days, they will fall into a coma. After 60 days, they will die._

* * *

  * Teetotalers will take the required drug without penalties, but ideoligion can still block taking them.
  * Chemical dependency severity increases by 0.2 per day. Reduced to 0% upon taking [beer](/wiki/Beer "Beer"). 
    * Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85
    * **Severity 1 (5 days):** [Consciousness](/wiki/Consciousness "Consciousness") 70% max, [Moving](/wiki/Moving "Moving") 80% max, [Manipulation](/wiki/Manipulation "Manipulation") 50% max,
    * **Severity 6 (30 days):** Consciousness 10% max (Unconsciousness)
    * **Severity 12 (60 days):** Consciousness 0% max ([Death](/wiki/Death "Death"))
  * Alcohol addiction factor: x0%


  * Teetotalers can take the required drug without penalties. However, [ideoligions](/wiki/Ideoligion "Ideoligion") against drug use will apply the −15 _Used drug_ moodlet.
  * Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

| +3 | 1 | \-   
Smokeleaf dependency  
[![ChemicalDependency Smokeleaf.png](/images/thumb/d/db/ChemicalDependency_Smokeleaf.png/64px-ChemicalDependency_Smokeleaf.png)](/wiki/File:ChemicalDependency_Smokeleaf.png) | _Carriers of this gene need to ingest Smokeleaf on a regular basis to survive. After 5 days without smokeleaf, carriers will suffer from smokeleaf deficiency. After 30 days, they will fall into a coma. After 60 days, they will die._

* * *

  * Teetotalers will take the required drug without penalties, but ideoligion can still block taking them.
  * Chemical dependency severity increases by 0.2 per day. Reduced to 0% upon taking a [smokeleaf joint](/wiki/Smokeleaf_joint "Smokeleaf joint"). 
    * Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85
    * **Severity 1 (5 days):** [Consciousness](/wiki/Consciousness "Consciousness") 70% max, [Moving](/wiki/Moving "Moving") 80% max, [Manipulation](/wiki/Manipulation "Manipulation") 50% max,
    * **Severity 6 (30 days):** Consciousness 10% max (Unconsciousness)
    * **Severity 12 (60 days):** Consciousness 0% max ([Death](/wiki/Death "Death"))
  * Smokeleaf addiction factor: x0%


  * Teetotalers can take the required drug without penalties. However, [ideoligions](/wiki/Ideoligion "Ideoligion") against drug use will apply the −15 _Used drug_ moodlet.
  * Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

| +3 | 1 | \-   
Psychite dependency  
[![ChemicalDependency Psychite.png](/images/thumb/5/56/ChemicalDependency_Psychite.png/64px-ChemicalDependency_Psychite.png)](/wiki/File:ChemicalDependency_Psychite.png) | _Carriers of this gene need to ingest psychite on a regular basis to survive. After 5 days without Psychite, carriers will suffer from psychite deficiency. After 30 days, they will fall into a coma. After 60 days, they will die._

* * *

  * Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking [psychite tea](/wiki/Psychite_tea "Psychite tea"), [flake](/wiki/Flake "Flake"), or [yayo](/wiki/Yayo "Yayo"). 
    * Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85
    * **Severity 1 (5 days):** [Consciousness](/wiki/Consciousness "Consciousness") 70% max, [Moving](/wiki/Moving "Moving") 80% max, [Manipulation](/wiki/Manipulation "Manipulation") 50% max,
    * **Severity 6 (30 days):** Consciousness 10% max (Unconsciousness)
    * **Severity 12 (60 days):** Consciousness 0% max ([Death](/wiki/Death "Death"))
  * Psychite addiction factor: x0%


  * Teetotalers can take the required drug without penalties. However, [ideoligions](/wiki/Ideoligion "Ideoligion") against drug use will apply the −15 _Used drug_ moodlet.
  * Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

| +4 | 1 | [![Wasters](/images/thumb/7/7c/GeneBackground_Endogene.png/32px-GeneBackground_Endogene.png)](/wiki/File:GeneBackground_Endogene.png "Wasters") [![Wasters](/images/thumb/a/ab/Waster.png/32px-Waster.png)](/wiki/Wasters "Wasters")  
Go-juice dependency  
[![ChemicalDependency Go Juice.png](/images/thumb/6/67/ChemicalDependency_Go_Juice.png/64px-ChemicalDependency_Go_Juice.png)](/wiki/File:ChemicalDependency_Go_Juice.png) | _Carriers of this gene need to ingest Go-juice on a regular basis to survive. After 5 days without Go-juice, carriers will suffer from Go-juice deficiency. After 30 days, they will fall into a coma. After 60 days, they will die._

* * *

  * Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking [go-juice](/wiki/Go-juice "Go-juice"). 
    * Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85
    * **Severity 1 (5 days):** [Consciousness](/wiki/Consciousness "Consciousness") 70% max, [Moving](/wiki/Moving "Moving") 80% max, [Manipulation](/wiki/Manipulation "Manipulation") 50% max,
    * **Severity 6 (30 days):** Consciousness 10% max (Unconsciousness)
    * **Severity 12 (60 days):** Consciousness 0% max ([Death](/wiki/Death "Death"))
  * Go-juice addiction factor: x0%


  * Teetotalers can take the required drug without penalties. However, [ideoligions](/wiki/Ideoligion "Ideoligion") against drug use will apply the −15 _Used drug_ moodlet.
  * Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

| +4 | 1 | [![Hussars](/images/thumb/f/fc/GeneBackground_Xenogene.png/32px-GeneBackground_Xenogene.png)](/wiki/File:GeneBackground_Xenogene.png "Hussars") [![Hussars](/images/thumb/a/ad/Hussar.png/32px-Hussar.png)](/wiki/Hussars "Hussars")  
Wake-up dependency  
[![ChemicalDependency Wake Up.png](/images/thumb/c/c6/ChemicalDependency_Wake_Up.png/64px-ChemicalDependency_Wake_Up.png)](/wiki/File:ChemicalDependency_Wake_Up.png) | _Carriers of this gene need to ingest wake-up on a regular basis to survive. After 5 days without wake-up, carriers will suffer from wake-up deficiency. After 30 days, they will fall into a coma. After 60 days, they will die._

* * *

  * Chemical dependency severity increases by 0.2 per day. Reduced to 0 upon taking [wake-up](/wiki/Wake-up "Wake-up"). 
    * Mood debuff starting with -4 at Severity 1.0 gradually scaling up to -20 at severity 5.85
    * **Severity 1 (5 days):** [Consciousness](/wiki/Consciousness "Consciousness") 70% max, [Moving](/wiki/Moving "Moving") 80% max, [Manipulation](/wiki/Manipulation "Manipulation") 50% max.
    * **Severity 6 (30 days):** Consciousness 10% max (Unconsciousness)
    * **Severity 12 (60 days):** Consciousness 0% max ([Death](/wiki/Death "Death"))
  * Wake-up addiction factor: x0%


  * Teetotalers can take the required drug without penalties. However, [ideoligions](/wiki/Ideoligion "Ideoligion") against drug use will apply the −15 _Used drug_ moodlet.
  * Children under 13 do not get any of the ill effects from not using these drugs. The timer for penalties only starts on their 13th birthday.

| +4 | 1 | \-   
  
## Removed genes[[edit](/index.php?title=Genes&action=edit&section=26 "Edit section: Removed genes")]

This table contains genes that are no longer found as-is in the current game version. They may have been removed or migrated in an update, or cut during development before a release. 

* Click to 

Name  | Description  | [![Metabolism](/images/thumb/c/c7/Metabolism.png/20px-Metabolism.png)](/wiki/File:Metabolism.png "Metabolism") | [![Complexity](/images/thumb/9/9b/Complexity.png/20px-Complexity.png)](/wiki/File:Complexity.png "Complexity") | [![Archite capsules](/images/thumb/9/90/Archite_capsule_required.png/20px-Archite_capsule_required.png)](/wiki/File:Archite_capsule_required.png "Archite capsules") | Removed  | Reason   
---|---|---|---|---|---|---  
Resurrect  
[![Gene Resurrect.png](/images/thumb/9/9d/Gene_Resurrect.png/64px-Gene_Resurrect.png)](/wiki/File:Gene_Resurrect.png) | Carriers have a reserve of unique resurrector archites which can infuse a corpse, rebuild degenerated tissue and kickstart the vital processes. This brings the dead back to life - though possibly with health issues. This can only be done very rarely, and comes at a steep hemogen cost. 

* * *

  * Requires Hemogenic
  * Adds ability: [![Resurrect gene ability.png](/images/thumb/6/60/Resurrect_gene_ability.png/16px-Resurrect_gene_ability.png)](/wiki/File:Resurrect_gene_ability.png) Resurrect



    _Use archites in the bloodstream to infuse a corpse's body with new life, repairing degenerated cell structures and kickstarting vital functions. The older and worse-preserved the corpse is, the more likely it is that they will come back with memory loss or health conditions. This ability seems to exhaust the archites somehow, so it can only be used very rarely._

  * Resurrects the targeted corpse, similarly to [Resurrector mech serum](/wiki/Resurrector_mech_serum "Resurrector mech serum")
  * Target: Any non-mechanoid corpse
  * Warmup Time: 2 [ticks](/wiki/Time "Time") (0.03 secs)
  * Cooldown: 6,840,000 [ticks](/wiki/Time "Time") (1.9 years) to 7,560,000 [ticks](/wiki/Time "Time") (2.1 years)
  * Charges: 1
  * AI Can Use: False



  * Market value of [genepacks](/wiki/Genepack "Genepack") containing this gene: ×150%

| **0** | 4 | 1 | Before [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") release  | Unknown.   
Skill apathy  
[![Skills PassionDrop Loop.gif](/images/thumb/9/9a/Skills_PassionDrop_Loop.gif/64px-Skills_PassionDrop_Loop.gif)](/wiki/File:Skills_PassionDrop_Loop.gif) | The carrier will have no passion in (skill).  | 2 | 1 | **-** | Before [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") release  | From an XML comment: _"Removed since the downsides are too easy and boring to avoid, and synergize with skill loss genes too much. If you already aren't using the skill it's too easy to just kill passion on it too. -Ty"_  
Drug addict-sensitive  | Carriers of this gene get addicted to (drug) very easily. 

  * Specific drug addiction factor: x9999%

| 2 | 1 | **-** | Before [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") Release  | From an XML comment: _"Removed since these just aren't very interesting, very narrow in application, and the downsides are too easy and boring to avoid. Just not much interaction or story here. -Ty"_  
  
## Notes[[edit](/index.php?title=Genes&action=edit&section=27 "Edit section: Notes")]

  * Certain genes will not be properly negated by other genes. For example, a drug dependency germline gene, while appearing to be negated by the same drug dependency as a xenogene, will instead cause the negative mood from the lack of the drug to start at 2.5 days instead of at 5 days.



## Version history[[edit](/index.php?title=Genes&action=edit&section=28 "Edit section: Version history")]

  * [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") Release - Added.
  * [1.4.3524](/wiki/Version/1.4.3524 "Version/1.4.3524") \- Children no longer get adult body types from genes.
  * [1.4.3525](/wiki/Version/1.4.3525 "Version/1.4.3525") \- Fix: Suppressed genes contributing to romance chance still apply. Fix: Attempting to absorb a xenogerm of your own colonist displays a warning message saying you'll anger your faction.
  * [1.4.3527](/wiki/Version/1.4.3527 "Version/1.4.3527") \- Fix: Never sleep xenohumans still rest when caravanning alone.
  * [1.4.3530](/wiki/Version/1.4.3530 "Version/1.4.3530") \- Fix: Removing passion-adding genes doesn't revert effect. Fix: Psychically bonded pawns in the same caravan still get "psychic bond distance" mood malus in some circumstances.
  * [1.4.3531](/wiki/Version/1.4.3531 "Version/1.4.3531") \- Fix: AI sanguophages can use longjump without any remaining hemogen. Increase the effect of the temperature genes. From 3/?[Value?]/10 to 5/10/20. Fix: Some hemogenic abilities can be queued without enough hemogen.
  * [1.4.3534](/wiki/Version/1.4.3534 "Version/1.4.3534") \- Fix: Melanin genes can be extracted by gene extractor. Reduced volume and frequency of yttakin sounds.
  * [1.4.3541](/wiki/Version/1.4.3541 "Version/1.4.3541") \- Fix: Victims of bloodfeeder bites can gain hemogen from the interaction.
  * [1.4.3542](/wiki/Version/1.4.3542 "Version/1.4.3542") \- Fix: Coagulate can still be queued if hemogen is below casting cost.
  * [1.4.3555](/wiki/Version/1.4.3555 "Version/1.4.3555") \- 
    * Psychic bond now gives +10% [psychic sensitivity](/wiki/Psychic_sensitivity "Psychic sensitivity"), or +5% if on different maps. Hediff description changed from _This person has a psychic bond with another person based on the psychic bonding gene._ to _This person has a psychic bond with another person based on the psychic bonding gene. The bond itself grants some limited psychic awareness, allowing it to connect even with the psychically deaf_. Bonds can now be created during lovin' allowing pawns already in a relationship when the gene was implanted to bond.
    * Many genes now give direct boosts instead of forcing traits, which allows genes and traits to stack: 
      * **Depressive** gene renamed to Very unhappy, no longer forces [Depressive](/wiki/Depressive "Depressive") trait instead decreases mood by −10. **Pessimist** gene renamed to Unhappy, no longer forces [Pessimist](/wiki/Pessimist "Pessimist") trait instead decreases mood by −5. **Optimist** gene renamed to Happy, no longer forces [Optimist](/wiki/Optimist "Optimist") trait instead increases mood by +5. **Sanguine** gene renamed to Very happy, no longer forces [Sanguine](/wiki/Sanguine "Sanguine") trait instead increases mood by +10.
      * Slow runner no longer forces [Slowpoke](/wiki/Slowpoke "Slowpoke") trait instead decreases move speed by −0.2 c/s. Fast runner no longer forces [Fast walker](/wiki/Fast_walker "Fast walker") trait instead increases move speed by +0.2 c/s. Very fast runner no longer forces [Jogger](/wiki/Jogger "Jogger") trait instead increases move speed by +0.4 c/s.
      * **Slow learner** renamed to Slow study, no longer forces [Slow learner](/wiki/Slow_learner "Slow learner") trait instead multiplies [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") ×50%. **Fast learner** renamed to Quick study, no longer forces [Fast learner](/wiki/Fast_learner "Fast learner") trait instead increases [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") +50%.
      * **Staggeringly ugly** gene renamed to Very unattractive, no longer forces [Staggeringly ugly](/wiki/Staggeringly_ugly "Staggeringly ugly") trait instead decreases beauty by −2. **Ugly** gene renamed to Unattractive, no longer forces [Ugly](/wiki/Ugly "Ugly") trait instead decreases beauty by −1. **Pretty** gene renamed to Attractive, no longer forces [Pretty](/wiki/Pretty "Pretty") trait instead increase beauty by +1. **Beautiful** gene renamed to Very attractive, no longer forces [Beautiful](/wiki/Beautiful "Beautiful") trait instead increase beauty by +2.
    * **< Drug> addict-resist** genes renamed to <Drug> resistant, Addiction-resistant genes for alcohol, smokeleaf and psychite provide a 50% reduction in tolerance buildup. Addiction-resistant genes for psychite, wake-up and go juice have a 50% multiplier on overdose chance. Smokeleaf and Alcohol resistant metabolism cost reduced from −2 to −1.
    * **< Drug> addict-immune** genes renamed to <Drug> impervious. Addiction-immune genes for psychite, wake-up and go juice grants immunity to overdoses from the drug. Addiction-immune genes for alcohol, smokeleaf and psychite provides a 100% reduction in tolerance buildup. Smokeleaf and Alcohol impervious metabolism cost reduced from −5 to −3.
    * Smokeleaf and Alcohol dependency metabolism gain reduced from +4 to +3.
    * Fix: Remove reference to damage over time in acid spray ability description. _[...] stick to targets and burn them over time._ to _[...] stick to targets and burn them._
    * Furskin and beardless genes are now mutually exclusive.
    * Buffed furry tail minimum comfy temperature offset from −5 °C (−9 °F) to −10 °C (−18 °F).
    * When a deathless pawn takes damage that would have been lethal and falls into a deathrest coma instead, as an additional consequence they lose 3-6% of XP in a random skill. This should make non-death less trivial for these characters and preserve the sense of risk and danger. We’ll tuned this ongoing as needed.
    * Fix: Bloodfeed can be used on pawns in mental states.
  * [1.4.3557](/wiki/Version/1.4.3557 "Version/1.4.3557") \- Slow study gene applies a ×50% factor to [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") instead of a −50% offset.
  * [1.4.3563](/wiki/Version/1.4.3563 "Version/1.4.3563") \- Fix: Pawns with "dead calm" gene can get into fights over botched conversion attempts. Fix: Genes that remove all passions don't save previous values, causing passions to reset on removal. Fix: Pawns being carried by other pawns strains psychic bond.
  * [1.4.3580](/wiki/Version/1.4.3580 "Version/1.4.3580") \- Fix: Furskin_Average3 head uses the wrong graphic. Fix: Tattoos render below heavy brow. Fix: Furskin gene hair/fur color not staying when implanted with a skin color xenogene. Fix: Exception trying to visit sick pawn with neversleep gene.
  * [1.4.3613](/wiki/Version/1.4.3613 "Version/1.4.3613") \- Fix: Reimplant ability not working with custom xenotypes.
  * [1.4.3641](/wiki/Version/1.4.3641 "Version/1.4.3641") \- Fix: Inactive sterile gene affects fertility.
  * [1.4.3682](/wiki/Version/1.4.3682 "Version/1.4.3682") \- [Arresting](/wiki/Arrest "Arrest") dead calm pawns now never fails, to prevent them going berserk.
  * [1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062") \- 
    * Made psychic bond distance thought more permissive. As long as both pawns are on the same map and not suspended (cryptosleep casket) they get the positive thought.
    * Remove reference to damage over time in acid spray gene description. ("...it will stick to enemies and burn them over time." to "...it will stick to enemies and burn them.")
    * Added more acid filth texture options for acid spray so it never looks tiled.
    * Attached helpful text to mouse when selected pawn is aiming animal warcall ability.
    * Updated fire spew LOS highlighting.
    * Updated psychic bonding hediff tooltip to factor in pawns contained in buildings.
    * Clarify that pawns with no xenogenes cannot implant their xenogerm into another person. Show correct warning message on attempt.
    * Fix: Pawns with genetic drug needs aren't getting mothballed. Can improve performance in late-game saves.
    * Fix: Chemical genes affect tolerance buildup and addiction chance of all chemicals, not just the specified one.
    * Fix: On colonist selection, wasters and hussars are currently generating without their drug dependencies.
    * Fix: Small increments of pawn speed differences are lost due to integer calculations. Very quick and quick genes were effectively the same on an otherwise unmodified pawn.
    * Fix: Drug dependency endogenes aren't properly being overridden by other drug-related xenogenes of the same chemical.
    * Fix: Psychic bonds can form between two pawns that have the psychic bonding genes even if they are bonded to other people.
    * Fix: Pawns still carry a weapon after getting incapable of violence gene.
    * Fix: Pawns incapable of violence still can use combat gene abilities
    * Fix: Fire spew can shoot through walls.
    * Fix: Fire spew ability not leaning like other ranged attacks.
    * Fix: Fire spew ability can't target walls.
    * Fix: Perfect immunity doesn't block gut worms or muscle parasites.
  * [1.6.4518](/wiki/Version/1.6.4518 "Version/1.6.4518") \- Added 2 new genes: Indoor dweller (Disables the outdoors need) and webbed phalanges (Ignores movement speed penalties from water terrain Decreases manipulation by 5%). The former is added to dirtmoles, resulting in complexity increasing from 9 -> 10, Net metabolism decreasing from +1 -> 0, hunger rate increasing from 90% -> 100%.
  * [1.6.4535](/wiki/Version/1.6.4535 "Version/1.6.4535") \- Made the breathless gene suppress the normal vacuum resistant gene, removing its metabolic impact.
  * [1.6.4566](/wiki/Version/1.6.4566 "Version/1.6.4566") \- Rebalanced the starjack xenotype, added the [Low gravity adapted](/wiki/Low_gravity_adapted "Low gravity adapted") gene. Removed [Awful plants](/wiki/Awful_plants "Awful plants"), replaced [Poor melee](/wiki/Poor_melee "Poor melee") with [Awful melee](/wiki/Awful_melee "Awful melee") and replaced [Cold tolerant](/wiki/Cold_tolerant "Cold tolerant") with [Cold super-tolerant](/wiki/Cold_super-tolerant "Cold super-tolerant"). Net metabolism decreasing from +1 -> 0, hunger rate increasing from 90% -> 100%. [Breathless](/wiki/Breathless "Breathless") and [Vacuum resistant](/wiki/Vacuum_resistant "Vacuum resistant") now grants [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature"): −5 °C (9 °F)
  * [1.6.4850](/wiki/Version/1.6.4850 "Version/1.6.4850") \- 
    * Fix: Pawns can infinitely desire a looks-change if their ideoligion and genes clash.
    * Fix: Having an endogene and an overriding xenogene with the same trait can cause the trait to never be applied at all.



* * *

[Biotech (DLC)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)") [![BiotechIcon.png](/images/thumb/7/73/BiotechIcon.png/26px-BiotechIcon.png)](/wiki/File:BiotechIcon.png)

Families
    **Relationships** ([Reproduction](/wiki/Reproduction "Reproduction") • [Children](/wiki/Children "Children"))  
**Life stages** ([Babies](/wiki/Babies "Babies") • [Children](/wiki/Children "Children") • [Adults](/wiki/Human "Human"))  
**Furniture** ([Crib](/wiki/Crib "Crib") • [Baby sleeping spot](/wiki/Baby_sleeping_spot "Baby sleeping spot") • [Growth vat](/wiki/Growth_vat "Growth vat") • [Toy box](/wiki/Toy_box "Toy box") • [Baby decoration](/wiki/Baby_decoration "Baby decoration") • [School desk](/wiki/School_desk "School desk") • [Blackboard](/wiki/Blackboard "Blackboard"))  

Mechanoids
    **Laborers** ([Agrihand](/wiki/Agrihand "Agrihand") • [Cleansweeper](/wiki/Cleansweeper "Cleansweeper") • [Constructoid](/wiki/Constructoid "Constructoid") • [Fabricor](/wiki/Fabricor "Fabricor") • [Lifter](/wiki/Lifter "Lifter") • [Paramedic](/wiki/Paramedic "Paramedic") • [Tunneler](/wiki/Tunneler "Tunneler"))  
**Combatants** ([Centurion](/wiki/Centurion "Centurion") • [Legionary](/wiki/Legionary "Legionary") • [Militor](/wiki/Militor "Militor") • [Scorcher](/wiki/Scorcher "Scorcher") • [Tesseron](/wiki/Tesseron "Tesseron"))  
**Commanders** ([Apocriton](/wiki/Apocriton "Apocriton") • [Diabolus](/wiki/Diabolus "Diabolus") • [War queen](/wiki/War_queen "War queen") • [War urchin](/wiki/War_urchin "War urchin"))
Mechanitors
    **Control** ([Mechlink](/wiki/Mechlink "Mechlink") • [Band node](/wiki/Band_node "Band node") • [Mech boosters](/wiki/Mech_booster "Mech booster") • [Mech signallers](/wiki/Mech_signaller "Mech signaller") • [Control pack](/wiki/Control_pack "Control pack") • [Airwire headset](/wiki/Airwire_headset "Airwire headset"))  
**Mechanoid creation** ([Basic subcore](/wiki/Basic_subcore "Basic subcore") • [Standard subcore](/wiki/Standard_subcore "Standard subcore") • [High subcore](/wiki/High_subcore "High subcore") • [Subcore encoder](/wiki/Subcore_encoder "Subcore encoder") • [Subcore softscanner](/wiki/Subcore_softscanner "Subcore softscanner") • [Subcore ripscanner](/wiki/Subcore_ripscanner "Subcore ripscanner") • [Mech gestator](/wiki/Mech_gestator "Mech gestator"))  
**Maintenance** ([Mech recharger](/wiki/Mech_recharger "Mech recharger"))
Genetics
    **Xenohumans** ([![Dirtmole.png](/images/thumb/c/c4/Dirtmole.png/18px-Dirtmole.png)](/wiki/Dirtmoles "Dirtmoles")[Dirtmoles](/wiki/Dirtmoles "Dirtmoles") • [![Genie.png](/images/thumb/8/8c/Genie.png/18px-Genie.png)](/wiki/Genies "Genies")[Genies](/wiki/Genies "Genies") • [![Highmate.png](/images/thumb/9/9c/Highmate.png/18px-Highmate.png)](/wiki/Highmates "Highmates")[Highmates](/wiki/Highmates "Highmates") • [![Hussar.png](/images/thumb/a/ad/Hussar.png/18px-Hussar.png)](/wiki/Hussars "Hussars")[Hussars](/wiki/Hussars "Hussars") • [![Impid.png](/images/thumb/d/d8/Impid.png/18px-Impid.png)](/wiki/Impids "Impids")[Impids](/wiki/Impids "Impids") • [![Neanderthal.png](/images/thumb/9/91/Neanderthal.png/18px-Neanderthal.png)](/wiki/Neanderthals "Neanderthals")[Neanderthals](/wiki/Neanderthals "Neanderthals") • [![PigskinXenotype.png](/images/thumb/6/67/PigskinXenotype.png/18px-PigskinXenotype.png)](/wiki/Pigskins "Pigskins")[Pigskins](/wiki/Pigskins "Pigskins") • [![Sanguophage.png](/images/thumb/8/8c/Sanguophage.png/18px-Sanguophage.png)](/wiki/Sanguophages "Sanguophages")[Sanguophages](/wiki/Sanguophages "Sanguophages") • [![Waster.png](/images/thumb/a/ab/Waster.png/18px-Waster.png)](/wiki/Wasters "Wasters")[Wasters](/wiki/Wasters "Wasters") • [![Yttakin.png](/images/thumb/e/ee/Yttakin.png/18px-Yttakin.png)](/wiki/Yttakin "Yttakin")[Yttakin](/wiki/Yttakin "Yttakin") • [![Starjack.png](/images/thumb/3/30/Starjack.png/18px-Starjack.png)](/wiki/Starjack "Starjack")[Starjack](/wiki/Starjack "Starjack")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"))   
**Genes** [Germline](/wiki/Germline "Germline") • [Xenogene](/wiki/Xenogene "Xenogene") • [Metabolic efficiency](/wiki/Metabolic_efficiency "Metabolic efficiency")  
**Genetic Modification** [Genepack](/wiki/Genepack "Genepack") • [Gene extractor](/wiki/Gene_extractor "Gene extractor") • [Gene bank](/wiki/Gene_bank "Gene bank") • [Gene assembler](/wiki/Gene_assembler "Gene assembler") • [Gene processor](/wiki/Gene_processor "Gene processor") • [Xenogerm](/wiki/Xenogerm "Xenogerm") • [Archite capsules](/wiki/Archite_capsules "Archite capsules")  
**Deathrest** ([Deathrest accelerator](/wiki/Deathrest_accelerator "Deathrest accelerator") • [Deathrest capacity serum](/wiki/Deathrest_capacity_serum "Deathrest capacity serum") • [Deathrest casket](/wiki/Deathrest_casket "Deathrest casket") • [Glucosoid pump](/wiki/Glucosoid_pump "Glucosoid pump") • [Hemogen amplifier](/wiki/Hemogen_amplifier "Hemogen amplifier") • [Hemopump](/wiki/Hemopump "Hemopump") • [Psychofluid pump](/wiki/Psychofluid_pump "Psychofluid pump"))
[Pollution](/wiki/Pollution "Pollution")
    **Nature** ([Toxalope](/wiki/Toxalope "Toxalope") • [Toxipotato plant](/wiki/Toxipotato_plant "Toxipotato plant") • [Waste rat](/wiki/Waste_rat "Waste rat") • [Gray pine tree](/wiki/Gray_pine_tree "Gray pine tree") • [Pebble cactus](/wiki/Pebble_cactus "Pebble cactus") • [Rat palm tree](/wiki/Rat_palm_tree "Rat palm tree") • [Witchwood tree](/wiki/Witchwood_tree "Witchwood tree") • [Stasis cocoon](/wiki/Stasis_cocoon "Stasis cocoon"))  
**Mitigation** ([Wastepacks](/wiki/Wastepack "Wastepack") • [Atomizers](/wiki/Wastepack_atomizer "Wastepack atomizer") • [Pollution pumps](/wiki/Pollution_pump "Pollution pump") • [Polux trees](/wiki/Polux_trees "Polux trees"))  
**Adaptation** [Face mask](/wiki/Face_mask "Face mask") • [Gas mask](/wiki/Gas_mask "Gas mask") • [Tox grenades](/wiki/Tox_grenades "Tox grenades") • [Tox pack](/wiki/Tox_pack "Tox pack") • [Tox shell](/wiki/Tox_shell "Tox shell") • [Toxic needle gun](/wiki/Toxic_needle_gun "Toxic needle gun") • [Toxbomb launcher](/wiki/Toxbomb_launcher "Toxbomb launcher") • [Detoxifier kidney](/wiki/Detoxifier_kidney "Detoxifier kidney") • [Detoxifier lung](/wiki/Detoxifier_lung "Detoxifier lung")  
**Nonchalance** [Toxifier generator](/wiki/Toxifier_generator "Toxifier generator")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Genes&oldid=184104#Robust](https://rimworldwiki.com/index.php?title=Genes&oldid=184104#Robust)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Biotech](/wiki/Category:Biotech "Category:Biotech")
  * [Pages to be recoded](/wiki/Category:Pages_to_be_recoded "Category:Pages to be recoded")
  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Game mechanics](/wiki/Category:Game_mechanics "Category:Game mechanics")



Hidden categories: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Genes "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Genes "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Genes "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Genes "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Genes)
  * [Edit](/index.php?title=Genes&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Genes&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Genes "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Genes "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Genes&oldid=184104 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Genes&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Genes)



  * This page was last edited on 24 September 2026, at 15:24.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: RGB: (85, 85, 85)
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
  *[+2]: Stacking 3 times for a maximum of 6
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
  *[−2]: Stacking 3 times for a maximum of -6
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
  *[11.11 mins]: real-time at 1x speed
  *[5.95 mins]: real-time at 1x speed
  *[19.44 mins]: real-time at 1x speed
  *[10.42 mins]: real-time at 1x speed
  *[25.4 mins]: real-time at 1x speed
  *[35.81 mins]: real-time at 1x speed
  *[1.39 mins]: real-time at 1x speed
  *[25 secs]: real-time at 1x speed
  *[1.74 mins]: real-time at 1x speed
  *[_Soaking wet_]: I'm soaking wet.
  *[+30]: Stacking 1 times for a maximum of 30
  *[_Joywire_]: It feels amazing
  *[Product Amount]: The amount of this item produced from the required resources
  *[11.67 secs]: real-time at 1x speed
  *[_Was imprisoned_]: The colony had me in jail for a while, like a caged animal.
  *[40]: Stacking 5 times with a 0.75 multiplier for maximum of 122
  *[_Catharsis_]: It felt good to finally unbottle my feelings.
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
  *[Profitability]: Market value/Combined material market value when selling
  *[22 secs]: real-time at 1x speed
  *[24 secs]: real-time at 1x speed
  *[5.33 secs]: real-time at 1x speed
  *[_Beautiful aurora_]: The view is amazing.
  *[_Psychic emanator soothe_]: The psychic emanator makes me feel strange, but also very relaxed.
  *[_Sad youngsters_]: It's sad to see that the young folk are struggling.
  *[_Happy youngsters_]: It's nice to see that the young folk are doing well.
  *[40 secs]: real-time at 1x speed
  *[1.33 mins]: real-time at 1x speed
  *[1 in-game day]: there are 60,000 ticks in a day
  *[15.97 mins]: real-time at 1x speed
  *[2 secs]: real-time at 1x speed
  *[0.5 secs]: real-time at 1x speed
  *[_Genetic depression_]: Natural penalty from 'very unhappy' gene.
  *[_Genetic pessimism_]: Natural penalty from 'unhappy' gene.
  *[_Genetic optimism_]: Natural bonus from 'happy' gene.
  *[_Genetic joy_]: Natural bonus from 'very happy' gene.
  *[0.03 secs]: real-time at 1x speed
  *[1.9 years]: there are 3,600,000 ticks in a year
  *[2.1 years]: there are 3,600,000 ticks in a year
