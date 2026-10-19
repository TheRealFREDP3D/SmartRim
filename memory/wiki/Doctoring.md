# Doctoring

From RimWorld Wiki

Jump to navigation Jump to search

[![Rewrite.png](/images/thumb/a/a3/Rewrite.png/40px-Rewrite.png)](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten") | This article is suggested to be [rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten"). **Reason:** Cleanup, fact check, [verification](/wiki/Template:Verified "Template:Verified"). You can help the RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Doctoring&action=edit)** it.__  
---|---  
  
## Contents

  * 1 Skill
  * 2 Medicines
    * 2.1 Treatment options
    * 2.2 No medical care
    * 2.3 Doctor care, but no medicine
    * 2.4 Herbal medicine
    * 2.5 Medicine
    * 2.6 Glitterworld medicine
  * 3 Treatment
    * 3.1 Tend quality
      * 3.1.1 Total tend quality
    * 3.2 Draft Tending
  * 4 Operations
    * 4.1 Operation Success Rate
    * 4.2 Calculating success
    * 4.3 Surgical inspection
    * 4.4 Failure
    * 4.5 Available targets
    * 4.6 Tips on Improving Success
  * 5 Infection
  * 6 Strategies
    * 6.1 Triage
    * 6.2 Medicine allocation
    * 6.3 Positioning
    * 6.4 Hospital design
  * 7 Version history



**Doctoring** is a type of work assigned to colonists from the [Work menu](/wiki/Work "Work"). The [Medical](/wiki/Medical "Medical") skill is the primary determinant for success. Colonists [incapable](/wiki/Incapable "Incapable") of Caring will never perform doctor work. 

Doctor work assigns pawns to the following jobs: tending to patients, tending to self (if enabled), feeding patients, performing surgical operations, rescuing downed pawns or downed tamed animals, tending to and operating on animals, feeding ill animals, and cheering up patients. 

How well a colonist performs in Doctoring mainly depends on their medical [skill](/wiki/Skill "Skill"), the quality of [medicine](/wiki/Medicine "Medicine") used, and the cleanliness of the [room](/wiki/Room "Room") in which they are operating. The doctor's physical condition plays an important role, too. 

Doctors can heal other colonists, guests, prisoners or animals and will prioritize life-threatening wounds and illnesses before tending minor conditions. 

Doctors can "self-tend" at 70% effectiveness to treat their own wounds or illnesses. Disabled by default, the self-tend option can be enabled in a pawn's Health-overview. 

## Skill[[edit](/index.php?title=Doctoring&action=edit&section=1 "Edit section: Skill")]

The Medicine skill is the center skill of doctoring in RimWorld. It directly multiplies the [tend quality](/wiki/Medical_Tend_Quality "Medical Tend Quality") as well as [surgery success chance](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") and [tend speed](/wiki/Medical_Tend_Speed "Medical Tend Speed") before other factors are taken in. All values in this table take post-processing into account where necessary. 

Doctor Level  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Base Tend Quality  | 20% | 30% | 40% | 50% | 60% | 70% | 80% | 90% | 100% | 105% | 110% | 115% | 120% | 125% | 130% | 135% | 140% | 145% | 150% | 152.5% | 155%   
Medical Tend Speed  | 40% | 46% | 52% | 58% | 64% | 70% | 76% | 82% | 88% | 94% | 100% | 106% | 112% | 118% | 124% | 130% | 136% | 142% | 148% | 154% | 160%   
Base Surgery Success Chance  | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 75% | 80% | 85% | 90% | 92% | 94% | 96% | 98% | 100% | 102% | 104% | 106% | 108% | 110%   
  
The following table documents a few of many possible combinations of how factors play into a colonist's performance at doctoring (needs updating for A17): 

Colonist  | Medicine Skill  | Base Tend Quality  | Manipulation [1] | Sight [2] | Final Tend Quality [3]  
---|---|---|---|---|---  
A [4] | 6 | 80% | 100% | 100% | **80%**  
B [5] | 18 | 200% | 60% | 30% | **62.72%**  
C [6] | 3 | 50% | 190% | 140% | **89.6%**  
D [7] | 11 | 130% | 50% | 100% | **71.5%**  
  
  1. ↑ 90% importance in tend quality, effective up to 140%
  2. ↑ 70% importance in tend quality, effective up to 140%
  3. ↑ To 2 decimal places
  4. ↑ Healthy, practitioner in medicine
  5. ↑ Bad back, frail, and cataracts, visionary in medicine
  6. ↑ Fully bionic trauma savant, basic familiarity with medicine
  7. ↑ Missing an arm, strong expert with medicine



The amount of XP gained from tending depends on the type of medicine used, and what it is used on (human or animal). The equation for this is: 

XP = Patient XP Factor × Medicine XP Factor × Doctor's Learning Rate   
---  
  
Where: 

  * Patient XP Factor is a multiplier from the patient type. ×175 for animal patients, and ×500 for human patients.
  * Medicine XP Factor is the medicine's potency multiplied by 0.7, and clamped in the range of 0.5 and 1.
  * Doctor's Learning Rate is the doctor's own multiplier on XP gained for the medicine skill. See "[Improving Skills](/wiki/Skills#Improving_skills "Skills")" for more details.

Medicine  | Potency  | XP Factor | Tend XP from patient   
---|---|---|---  
Human | Animal  
[![Doctor care but no medicine.png](/images/thumb/9/92/Doctor_care_but_no_medicine.png/16px-Doctor_care_but_no_medicine.png)](/wiki/File:Doctor_care_but_no_medicine.png) None  | 0.30 | 0.5 | 250 | 87.5   
[![Herbal medicine](/images/thumb/a/af/Herbal_medicine.png/16px-Herbal_medicine.png)](/wiki/Herbal_medicine "Herbal medicine") [Herbal medicine](/wiki/Herbal_medicine "Herbal medicine") | 0.60 | 0.5 | 250 | 87.5   
[![Medicine](/images/thumb/7/79/Medicine_industrial_a.png/16px-Medicine_industrial_a.png)](/wiki/Medicine "Medicine") [Medicine](/wiki/Medicine "Medicine") | 1.00 | 0.7 | 350 | 122.5   
[![Glitterworld medicine](/images/thumb/c/c6/Glitterworld_medicine.png/16px-Glitterworld_medicine.png)](/wiki/Glitterworld_medicine "Glitterworld medicine") [Glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine") | 1.60 | 1 | 500 | 175   
  
## Medicines[[edit](/index.php?title=Doctoring&action=edit&section=2 "Edit section: Medicines")]

Medicine is used to improve the results of doctoring, therefore improving recovery from injuries and disease, and also allowing operations to be performed. Another perk to using medicine is that medicine is typically able to heal multiple low severity injuries (up to max of 20 damage worth of severity), which is something that 'dry-bandaging' can't do. 

There are currently three types of medicine in RimWorld: the organic [herbal medicine](/wiki/Herbal_medicine "Herbal medicine"), the standard [medicine](/wiki/Medicine "Medicine"), and the rare [glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine") \- in order from least potent to most potent. 

It is possible to change the default healthcare given to pawns. Defaults to glitterworld medicine for colonists, herbal meds for everybody else, and no medicine for [entities](/wiki/Entities "Entities").[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC"). To do this go under assign or animals and click on the medicine icon next to a pawn, holding click and dragging allows multiple pawns to have their medicine changed. The default medicine assigned can be changed by going under a pawn's health tab and clicking "Allow medicine" and then "change defaults" 

### Treatment options[[edit](/index.php?title=Doctoring&action=edit&section=3 "Edit section: Treatment options")]

Five treatment options are available; none at all, doctor care, herbal medicine or worse, regular medicine or worse, or best quality medical care. 

For prisoners and guests the default is herbal medicine; colonists default to best care available. 

In the early game, however, it is ideal to set the medical policy so that all pawns on the map only get basic doctor treatment. This allows precious medicine to be stockpiled for emergencies and operations, rather than wasted on minor injuries. 

### No medical care[[edit](/index.php?title=Doctoring&action=edit&section=4 "Edit section: No medical care")]

This option prevents pawns from receiving any sort of medical care. Leaving them to die or rarely recover on their own. 

As doctor care does not require any medicine, this option is not recommended unless your intent is to let the pawn die. If the colony has [Slaughtering animals](/wiki/Slaughtering_animals_\(precept\) "Slaughtering animals \(precept\)")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") precept, this can be useful to prevent doctors from tending to pen animals that inevitably overpopulate and start starving to death, saving their time for other matters. Pawns with that precept are not affected by tamed animals dying to natural causes. 

### Doctor care, but no medicine[[edit](/index.php?title=Doctoring&action=edit&section=5 "Edit section: Doctor care, but no medicine")]

[![Doctor care but no medicine.png](/images/9/92/Doctor_care_but_no_medicine.png)](/wiki/File:Doctor_care_but_no_medicine.png)

Doctors will attempt to perform a treatment without any sort of medicine, this is far slower than without medicine and treats only 1 wound at a time, due to the lower potency chances of infection occurring or immunity being outpaced by severity on diseases are higher. **Note** that it is not possible to do most operations without medicine.  
This is also ideal to use on bruises or long-term ailments that can't cause death in-order to save resources, such as [asthma](/wiki/Asthma "Asthma"), and [Sensory](/wiki/Sensory_mechanites "Sensory mechanites")/[Fibrous Mechanites](/wiki/Fibrous_mechanites "Fibrous mechanites")

Attributes  | Medical Potency | Max tend quality | Market Value | Mass (kg)   
---|---|---|---|---  
Values  | 30% | 70% | N/A | N/A   
  
**Tend quality**

Doctor Level  | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 20   
---|---|---|---|---|---|---|---|---  
Base Avg. Quality  | 6% | 15% | 24% | 31.5% | 36% | 40.5% | 45% | 46.5%   
Base Surgery Success  | - | - | - | - | - | - | - | \-   
  
### Herbal medicine[[edit](/index.php?title=Doctoring&action=edit&section=6 "Edit section: Herbal medicine")]

[![Herbal medicine.png](/images/a/af/Herbal_medicine.png)](/wiki/Herbal_medicine "Herbal medicine")

[Herbal medicine](/wiki/Herbal_medicine "Herbal medicine") is an organic medicine which can be grown from [healroots](/wiki/Healroot "Healroot"), or acquired from tribal factions. It is a cheap medicine that can be used for bleeding injuries, diseases that don't need more than 70% tend quality, and operations with a high success rate or where the patient's life doesn't matter such as organ-harvesting. 

Attributes  | Medical Potency | Max tend quality | Market Value | Mass (kg)   
---|---|---|---|---  
Values  | 60% | 70% | 10 | 0.35   
  
**Tend quality**

Doctor Level  | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 20   
---|---|---|---|---|---|---|---|---  
Base Avg. Quality  | 12% | 30% | 48% | 63% | 72% | 81% | 90% | 93%   
Base Surgery Success  | 12% | 30% | 48% | 55.2% | 57% | 57.9% | 58.8% | 59.4%   
  
### Medicine[[edit](/index.php?title=Doctoring&action=edit&section=7 "Edit section: Medicine")]

[![Medicine industrial a.png](/images/7/79/Medicine_industrial_a.png)](/wiki/Medicine "Medicine")

Standard [medicine](/wiki/Medicine "Medicine") is the benchmark of medical treatment solutions, and is also producible at a [drug lab](/wiki/Drug_lab "Drug lab") by combining herbal medicine, [neutroamine](/wiki/Neutroamine "Neutroamine"), and [cloth](/wiki/Cloth "Cloth"). It can additionally be purchased from outlanders and orbital traders, and is occasionally dropped by pirate raiders and mercenaries. 

Medicine is best used for bridging the immunity gap of illnesses or for installing body parts, though the risk of failure is still present. Odds can be improved by boosting manipulation through drugs like [go-juice](/wiki/Go-juice "Go-juice") and [wake-up](/wiki/Wake-up "Wake-up") or implants. 

It's not the best idea to excise [carcinomas](/wiki/Carcinoma "Carcinoma") using ordinary medicine due to its 0.7x success factor and 25% death chance on failure. Saving it until your surgeon has at least a surgery success chance of 128.5% (achievable with a pair of bionic arms) is better as it translates to a roughly 90% success chance. 

Attributes  | Medical Potency | Max tend quality | Market Value | Mass (kg)   
---|---|---|---|---  
Values  | 100% | 100% | 18 | 0.5   
  
**Tend quality**

Doctor Level  | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 20   
---|---|---|---|---|---|---|---|---  
Base Avg. Quality  | 20% | 50% | 80% | 100% | 100% | 100% | 100% | 100%   
Base Surgery Success  | 20% | 50% | 80% | 92% | 95% | 96.5% | 98% | 99%   
  
### Glitterworld medicine[[edit](/index.php?title=Doctoring&action=edit&section=8 "Edit section: Glitterworld medicine")]

[![Glitterworld medicine.png](/images/c/c6/Glitterworld_medicine.png)](/wiki/Glitterworld_medicine "Glitterworld medicine")

[Glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine") is the most powerful medicine out of the three types available, and can only be found through trading with exotic good traders and faction bases or as a quest reward. Despite the high price, Glitterworld Medicine carries a value which no other medicine can carry: enhanced medical potency. Naturally, due to the cost, Glitterworld Medicine isn't worth the price for treating trivial diseases or injuries - but it makes surgery _significantly_ easier, and allows even mediocre doctors to guarantee success in operations. 

It is mostly useful for lowering the luck factor in treatment for diseases that would be otherwise lethal or low success rate operations such as excising cancerous growths, or installing bionics. Other medicine will be satisfactory for injuries or diseases with a low immunity to severity gap. 

With DLCs, Glitterworld medicines gains more uses. Treating [paralytic abasia](/wiki/Paralytic_abasia "Paralytic abasia")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") and [blood rot](/wiki/Blood_rot "Blood rot")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") which both cost 10 units, and the [Biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod")'s [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [bioregeneration cycle](/wiki/Bioregeneration_cycle "Bioregeneration cycle") costs 2 and heals missing small limbs and scars. 

Attributes  | Medical Potency | Max tend quality | Market Value | Mass (kg)   
---|---|---|---|---  
Values  | 160% | 130% | 50 | 0.5   
  
**Tend quality**

Doctor Level  | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 20   
---|---|---|---|---|---|---|---|---  
Base Avg. Quality  | 32% | 80% | 100% | 100% | 100% | 100% | 100% | 100%   
Base Surgery Success  | 32% | 80% | 100% | 100% | 100% | 100% | 100% | 100%   
  
## Treatment[[edit](/index.php?title=Doctoring&action=edit&section=9 "Edit section: Treatment")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Doctoring&action=edit). Reason:** _Tend time? how amny wounds are tended, and what controls that, what does tending do to thw injuries? etc? Has stats but little.in the way of actual mechanics._  
---|---  
  
Basic medical work involving tending to wounds and illnesses. Treating wounds stop them from bleeding and reduce the chance of infections, while tending to illnesses slows them down allowing your colonists' immune systems to catch up and pull ahead. 

Each individual treatment can have any quality from 0 - 130%, depending on the medicine used. Higher quality makes infections less likely and slows down illnesses more. 

After each treatment there will be text feedback showing the wound/illness tended and the quality of the treatment. Only 1 injury will generate feedback at a time even if multiple are treated at once. 

### Tend quality[[edit](/index.php?title=Doctoring&action=edit&section=10 "Edit section: Tend quality")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Doctoring&action=edit). Reason:** _Does not explain what Tend Quality actually does._  
---|---  
  
First, Base Tend Quality is calculated. Then, other factors apply if relevant. Tend Quality is adjusted up to 25% up or down randomly. Finally, the Tend quality is limited to a range between 0% and the Max Tend Quality of the medicine used. 

**1\. Base Tend Quality**

    `**Base Tend Quality** = [Medical Tend Quality](/wiki/Medical_Tend_Quality "Medical Tend Quality") × [Medical Potency](/wiki/Medical_Potency "Medical Potency")`

    **1.a. Offsets from hospital bed and vitals monitor**

    If applicable, Medical Tend Quality Offset from the bed is added to the Base Tend Quality value. This offset only exists on Hospital Beds and Vitals Monitors attached to hospital beds. No other beds have Medical Tend Quality Offset.

    

    Laying Down is not a factor. Draft tends on injured colonists standing up will have the same Medical Tend Qualities as tends while laying in a standard bed.

    

    `**Medical Tend Quality with Offset** = Base Tend Quality + 0.1 Hospital Bed (if applicable) + 0.07 Vitals Monitor (if applicable)`

    **1.b. Self tend factor**

    If Self Tending, Tend Quality with Offset is adjusted by 70%.

    

    `**Medical Tend Quality with Self Tend** = Medical Tend Quality with Offset * 0.7 Self Tend Factor (if applicable)`

**2\. Randomization**

    Medical Tend Quality is then randomized.

    `**Randomized Tend Quality** = Medical Tend Quality with Self Tend * Random Value between 0.75 and 1.25`

**3\. Maximum tend quality**

    The Final Tend Quality is then limited to a range of 0 to Maximum Tend Quality from Medicine used.

    `**Final Tend Quality** = Clamped 0% to Maximum Tend Quality from Medicine`

    The maximum tend quality of each medicine is as follows: 

  * **70%** for [![Herbal medicine](/images/thumb/a/af/Herbal_medicine.png/16px-Herbal_medicine.png)](/wiki/Herbal_medicine "Herbal medicine") [herbal medicine](/wiki/Herbal_medicine "Herbal medicine") or no medicine
  * **100%** for [![Medicine](/images/thumb/7/79/Medicine_industrial_a.png/16px-Medicine_industrial_a.png)](/wiki/Medicine "Medicine") [medicine](/wiki/Medicine "Medicine")
  * **130%** for [![Glitterworld medicine](/images/thumb/c/c6/Glitterworld_medicine.png/16px-Glitterworld_medicine.png)](/wiki/Glitterworld_medicine "Glitterworld medicine") [glitterworld medicine](/wiki/Glitterworld_medicine "Glitterworld medicine")



**Notes:**

  * [Light](/wiki/Light "Light") is _not_ a factor of Medical Tend Quality. It is, however, a factor of [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") and thus of Medical Tend Speed and a factor of [Surgery Success Chance](/wiki/Surgery_Success_Chance "Surgery Success Chance").
  * [Cleanliness](/wiki/Cleanliness "Cleanliness") is _not_ a factor of Medical Tend Quality. It is, however, a factor of [Infection Chance](/wiki/Infection "Infection").
  * Being indoors or outdoors is _not_ a factor of Medical Tend Quality. It is, however, a factor of cleanliness and thus Infection Chance.



#### Total tend quality[[edit](/index.php?title=Doctoring&action=edit&section=11 "Edit section: Total tend quality")]

Some medical issues are cured when the sum of all tends performed reach a certain value. This is described as "total tend quality". The current total and the required total to cure will be displayed in the mouse-over menu on the issue in question on the pawn's health menu. The value will not be displayed for issues not cured by total tend quality, so its presence is a clear indicator of how to cure the issue. 

The following diseases use this mechanic: 

  * [Gut worms](/wiki/Gut_worms "Gut worms")
  * [Muscle parasites](/wiki/Muscle_parasites "Muscle parasites")



### Draft Tending[[edit](/index.php?title=Doctoring&action=edit&section=12 "Edit section: Draft Tending")]

Drafted colonists can be forced to tend wounds of injured pawns using right click. The injured pawn does not need to be laying down in order to be draft tended. One can even Draft Tend an injured pawn on a non-aggressive mental break or a downed enemy in the field. The tend quality of Draft Tended injuries uses the same formula as undrafted treatment. The "Tend (without medicine)" option is useful for emergency treatment. The option "Tend ___" that does not say (without medicine) will use the medicine in the doctor's inventory regardless of the targets medical settings. After using the medicine in inventory, the doctor will grab the nearest medicine of any quality. 

## Operations[[edit](/index.php?title=Doctoring&action=edit&section=13 "Edit section: Operations")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Doctoring&action=edit). Reason:** _More complete operations table - rough outline of one available[here](/wiki/User:Harakoni/Sandbox#Operations "User:Harakoni/Sandbox")._  
---|---  
  
[![Installing bionic arm.png](/images/thumb/0/09/Installing_bionic_arm.png/300px-Installing_bionic_arm.png)](/wiki/File:Installing_bionic_arm.png)

An **operation** is a [bill](/wiki/Bill "Bill") to be performed on a [colonist](/wiki/Colonist "Colonist") by a doctor. This may involve the removal or addition of [body parts](/wiki/Body_parts "Body parts"), administration of [drugs](/wiki/Drugs "Drugs") or excising [carcinomas](/wiki/Carcinoma "Carcinoma"). Many operations require a minimum [Medical skill](/wiki/Medical "Medical") (e.g. excising a [carcinoma](/wiki/Carcinoma "Carcinoma") requires level 10). Some operations require a minimum [medicine](/wiki/Medicine "Medicine") level ([Herbal medicine](/wiki/Herbal_medicine "Herbal medicine") is the minimum required medicine for most operations). 

### Operation Success Rate[[edit](/index.php?title=Doctoring&action=edit&section=14 "Edit section: Operation Success Rate")]

When an operation is performed, a degree of chance is calculated to assess the probability that the outcome of the operation will be successful. 

This is determined as a product of: 

  * The [Surgery Success Chance](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") stat of the surgeon performing the operation
  * The [Medical Potency](/wiki/Medical_Potency "Medical Potency") stat of the [Medicine](/wiki/Medicine "Medicine") used for performing the operation
  * The [Surgery Success Chance Factor](/wiki/Surgery_Success_Chance_Factor "Surgery Success Chance Factor") stat of a [bed](/wiki/Bed "Bed") or other [sleep furniture](/wiki/Sleep_furniture "Sleep furniture") upon which the operation is performed
  * The Success Rate Multiplier for the specific operation
  * [Inspired Surgery](/wiki/Inspired_surgery "Inspired surgery") Factor



This may be expressed as:  
`**Operation Success Rate** = [Surgery Success Chance Surgeon](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") × [Surgery Success Chance Bed](/wiki/Surgery_Success_Chance_Factor "Surgery Success Chance Factor") × [Medical Potency](/wiki/Medical_Potency "Medical Potency") × Operation Success Rate Multiplier × [Inspired Surgery](/wiki/Inspired_surgery "Inspired surgery") Factor`

Note that additionally: 

  * The resulting **Operation Success Rate** is capped at 98%.
  * If the **Operation Success Rate Multiplier** is _Can't fail_ , the **Operation Success Rate** will always be 100%, regardless of any other stats.



### Calculating success[[edit](/index.php?title=Doctoring&action=edit&section=15 "Edit section: Calculating success")]

**Surgeon's[Medical Surgery Success Chance](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") stat**

  * Determined by Medical skill. (see #Skill section)
  * [Manipulation](/wiki/Manipulation "Manipulation") acts as a direct multiplier. For example, 115% Manipulation = x1.15 success.
  * [Sight](/wiki/Sight "Sight") acts as a direct multiplier at 100% and below. For example, 90% Sight = x0.9 success but 110% Sight = x1 success.



**Bed's[Surgery Success Chance Factor](/wiki/Surgery_Success_Chance_Factor "Surgery Success Chance Factor") stat**

  * Determined by type of bed and its quality. [Beds](/wiki/Bed "Bed") and [bedrolls](/wiki/Bedroll "Bedroll") have a modifier of 1.0. [Hospital beds](/wiki/Hospital_bed "Hospital bed") have a modifier of 1.15. [Quality](/wiki/Quality "Quality") is a multiplier. Material does not matter.
  * Then multiplied by the room's [cleanliness](/wiki/Cleanliness "Cleanliness") stat. It is 1 for 0 cleanliness and 1.018 for a clean room with [sterile](/wiki/Sterile_tile "Sterile tile") flooring. The minimum is 0.6, reached at -5 cleanliness and also applied outdoors.
  * Then multiplied by [light](/wiki/Light "Light") factor. If the head of the bed has lighting below 50%, there is a penalty. It reaches 0.75 in complete darkness.
  * If surgery is done outdoors, there is an 0.85 penalty multiplier (on top of the aforementioned 0.6 cleanliness multiplier).



**[Medical Potency](/wiki/Medical_Potency "Medical Potency")**

  * Determined by the type of medicine. The [medicine](/wiki/Medicine "Medicine") item (industrial medicine) has a modifier of 1.0. (see [Medical Potency](/wiki/Medical_Potency "Medical Potency"))



**Operation Success Rate Multiplier**

  * Modifier dependent on the type of operation.

Operation | Operation Success Rate Multiplier (%)   
---|---  
Administer _[[drug](/wiki/Drugs "Drugs")]_ | _Can't fail_  
[Anesthetize](/wiki/Anesthetic "Anesthetic") | 200   
Cure [scaria](/wiki/Scaria "Scaria") | 100   
Euthanize by cut  | 500   
Excise [carcinoma](/wiki/Carcinoma "Carcinoma") | 100   
Harvest _[[body part](/wiki/Body_Parts "Body Parts")]_ | 120   
Install _[[body part](/wiki/Body_Parts "Body Parts") or [implant](/wiki/Category:Implant "Category:Implant")]_ | 100   
Remove _[[body part](/wiki/Body_Parts "Body Parts") or [implant](/wiki/Category:Implant "Category:Implant")]_ | 120   
[Sterilize](/wiki/Sterilized "Sterilized") | 100   
Anti-[abasia](/wiki/Abasia "Abasia") mechanite infusion [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | 100   
Cure [blood rot](/wiki/Blood_rot "Blood rot") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | 100   
[Blood transfusion](/wiki/Hemogen_pack#Blood_transfusion "Hemogen pack") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Extract [hemogen pack](/wiki/Hemogen_pack "Hemogen pack") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Extract [ovum](/wiki/Ovum "Ovum") for IVF [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 500   
Implant [embryo](/wiki/Embryo "Embryo") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 500   
Implant [IUD](/wiki/Reproduction#IUD "Reproduction") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Implant [xenogerm](/wiki/Xenogerm "Xenogerm") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Perform [tubal ligation](/wiki/Reproduction#Tubal_ligation "Reproduction") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Perform [vasectomy](/wiki/Reproduction#Vasectomy "Reproduction") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Remove [IUD](/wiki/Reproduction#IUD "Reproduction") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Reverse [vasectomy](/wiki/Reproduction#Vasectomy "Reproduction") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 100   
Terminate [pregnancy](/wiki/Pregnancy "Pregnancy") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 200   
[Bliss lobotomy](/wiki/Bliss_lobotomy "Bliss lobotomy") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | 100   
[Ghoul](/wiki/Ghoul "Ghoul") infusion [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | 100   
[Surgical inspection](/wiki/Surgical_inspection "Surgical inspection") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | 150   
  
_Note that the**Success Rate Multiplier** for each operation is shown in-game on the **Information** page for an added bill in the [Colonist](/wiki/Colonist "Colonist")'s **Health** → **Operations** tab._

**Inspired Surgery Factor**

  * 1 by default.
  * 2 if the surgeon has [inspired surgery](/wiki/Inspired_surgery "Inspired surgery") inspiration.



### Surgical inspection[[edit](/index.php?title=Doctoring&action=edit&section=16 "Edit section: Surgical inspection")]

[![AnomalyIcon.png](/images/thumb/3/32/AnomalyIcon.png/40px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)") | **This section relates to content added by[Anomaly (DLC)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
![](/images/thumb/0/06/Modal_Warning_Icon.png/40px-Modal_Warning_Icon.png)| **Spoiler warning:** This section may contain details about the gameplay that might be considered spoilers.  
If you wish to enjoy the content first hand, you probably shouldn't continue reading beyond this point.  
---|---  
  
With the [Anomaly](/wiki/Anomaly "Anomaly") DLC surgical inspections can be used to diagnose hediffs before they are made visible. This operation deals [cut damage](/wiki/Damage#cut "Damage") to a random body part **including the brain** and checks for any hediffs on the pawn. 

Note that a doctor may lie about the results of the inspection if it is in their own self-interest. This only happens when the doctor has been implanted with a [metalhorror](/wiki/Metalhorror "Metalhorror") and would otherwise discover a metalhorror in another pawn - the doctor will instead say they found nothing. 

Hediff | Description   
---|---  
[Resurrection psychosis](/wiki/Resurrection_psychosis "Resurrection psychosis") | {PAWN_nameDef} is suffering from a terminal case of resurrection psychosis, a condition caused by the decoherence of resurrection mechanites. The condition will slowly worsen, eventually resulting in death.   
[Toxic buildup](/wiki/Toxic_buildup "Toxic buildup") | {PAWN_nameDef} is showing early signs of toxic buildup. Keep {PAWN_objective} away from sources of toxins.   
[Rot stink exposure](/wiki/Hediffs/Core/Local/Infections/Rot_stink_exposure "Hediffs/Core/Local/Infections/Rot stink exposure") | {PAWN_nameDef} is beginning to suffer from exposure to rot stink gas. Keep {PAWN_objective} away from rotting corpses and other sources of rot stink.   
[Organ decay](/wiki/Organ_decay "Organ decay")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | {PAWN_nameDef} is showing early signs of a severe condition which will cause their organs to rapidly deteriorate. {SURGEON_nameDef} can't yet tell exactly what is causing this, but {PAWN_nameDef} will become very ill within the next few days.   
[Crumbling mind](/wiki/Crumbling_mind "Crumbling mind")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | {PAWN_nameDef} is showing early signs of a severe condition which will soon cause severe mental degradation. {SURGEON_nameDef} can't yet tell exactly what is causing this, but {PAWN_nameDef} will become very ill within the next few days.   
[Duplicate sickness](/wiki/Hediffs/Anomaly/Global/Misc/Duplicate_sickness "Hediffs/Anomaly/Global/Misc/Duplicate sickness")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | {PAWN_nameDef} is suffering from duplicate sickness. Psychic interference between this person and their duplicate is causing slow mental deterioration. As long as multiple copies of this person are alive, the condition will keep getting worse.   
[Psychic agony](/wiki/Hediffs/Anomaly/Global/Misc/Agony_pulse "Hediffs/Anomaly/Global/Misc/Agony pulse")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") | {SURGEON_nameDef} detected a faint but painful psychic presence emanating from {PAWN_nameDef} but failed to understand what was causing it.   
  
[Metalhorrors](/wiki/Metalhorror "Metalhorror")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") lack a description and instead emerge if they were detected beforehand through interrogation or enough samples were collected to reveal it through a surgical inspection. 

### Failure[[edit](/index.php?title=Doctoring&action=edit&section=17 "Edit section: Failure")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Doctoring&action=edit). Reason:** _How are they selected?._  
---|---  
  
If an operation fails then the colonist will take damage, and materials (including prosthetics) will be wasted. For lesser failures, damage is concentrated near the site of the operation, while for the ridiculous failures they can be found anywhere in the body. 

There are 3 kinds of surgical failure in-game. 

  * Minor: Deals a little damage, and will not destroy any body parts.
  * Catastrophic: Deals great damage, and usually destroys body parts outright.
  * Ridiculous: Deals great damage scattered across the entire body.



In addition, each operation has a death on failure chance; when it fails it is possible that the [colonist](/wiki/Colonist "Colonist") instantly dies. 

### Available targets[[edit](/index.php?title=Doctoring&action=edit&section=18 "Edit section: Available targets")]

Surgeons can perform operations on colonists, prisoners or guests. Performing harmful operations on guests or prisoners will anger the faction. 

Tamed animals can be operated on as well, though there are limited options. [Downed](/wiki/Downed "Downed") wild animals with the exception of [Insectoids](/wiki/Insectoids "Insectoids") can also be operated on once dragged to an animal sleeping spot. [Entities](/wiki/Entities "Entities") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") except for [Ghouls](/wiki/Ghoul "Ghoul") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") cannot be operated on at all. 

### Tips on Improving Success[[edit](/index.php?title=Doctoring&action=edit&section=19 "Edit section: Tips on Improving Success")]

The difference between a level 10 surgeon (93% base surgery success chance) and a level 20 surgeon (99%) is only a 6.5% gain in surgical success rate. The difference between Herbal Medicine (60% potency) and Glitterworld Medicine (160% potency) is a 167% increase in surgical success rate. 

Due to the 98% success cap, using glitterworld medicine for surgeries is mostly only worthwhile in lower-quality surgical environments (less cleanliness, lower quality hospital beds, unskilled doctors). Beyond that point, industrial medicine is sufficient for the purposes of surgery. 

## Infection[[edit](/index.php?title=Doctoring&action=edit&section=20 "Edit section: Infection")]

When a bed is set to be medical, selecting it shows the infection chance modifier of the room. The overall chance of infection is affected by tend quality, and then multiplied by the aforementioned number. Any bed, no matter what it is, has a 100% modifier on infection when outdoors, and only an incredibly dirty room can get close to this number. However, even at an 80% modifier, wounds tended by an unskilled doctor using herbal meds is likely to be around 10-20% infection chance **per wound**. As each infection will share the same immunity progress, this is not as bad as it may sound - if the pawn has immunity to an infection, they are effectively immune to all infections until the last one fades away. 

It is much better to make the hospital as clean as possible. Start by covering or removing all natural floors (dirt, sand etc. but excluding stone) and ensure that the hospital is cleaned before tending to pawns. Keep all pawns, especially animals out to keep the room as clean as possible. Infection chance multiplier will likely become around the 40-50% mark or even lower. Next, unlock sterile tiles. A room with 0.6 cleanliness can have multipliers near 30%. To see the cleanliness of rooms, toggle on the room stats view on the bottom right corner and then mouse over the hospital (or any other room for that matter). Dirt, animal filth among other things drastically reduces cleanliness, and it also reduces beauty. This makes it possible to locate and prioritize cleaning through the beauty view. Remember to clean before the treatment when possible. 

One of the most difficult things about keeping a hospital clean is bleeding. Bleeding colonists will leave blood on the floor, and blood reduces cleanliness. Someone hemorrhaging to death may create 4 or 5 blood splatters on the floor in a very short time, and if this is happening to multiple colonists after a disastrous raid, your doctor alone may not be enough to keep the room clean. Bring in another colonist or two to clean up after other patients awaiting treatment. What is important is the cleanliness at the time of treatment. 

Other things like the presence of hospital beds and better medicine/doctors can reduce infection chance to next to nothing, and make it a non-issue when it does occasionally arise. 

## Strategies[[edit](/index.php?title=Doctoring&action=edit&section=21 "Edit section: Strategies")]

You will often need to make the most out of the doctors you have, to ensure maximum doctoring efficiency and colonist survival rate/ well-being. 

### Triage[[edit](/index.php?title=Doctoring&action=edit&section=22 "Edit section: Triage")]

You should have doctors prioritize treating patients according to their illness/infection/injury severity. 

  1. Bleeding colonists should receive priority care as they may bleed to death or receive nasty infections. Always prioritize colonists closer to death. 
     * Colonists about to die (<1 hours until death) are generally not worth saving unless you have extremely good bionic-enhanced doctors that can reach and patch them up in time. 
       * Strip them to recover their clothes so they won't become tainted. How you will deal with the dead colonist is up to you.
       * If a [Biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") is available, put them into a [medic cycle](/wiki/Medic_cycle "Medic cycle"). This is also useful for infections that have about a 10% immunity to severity gap.
       * If you have a colonist with the [Coagulate](/wiki/Coagulate "Coagulate")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") ability, such as a [Sanguophage](/wiki/Sanguophage "Sanguophage"),[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") it can even save colonists who are mere seconds away from death.
     * Colonists that are very close (1-4 hours till death) to dying should have the best doctors care over them. Draft-tending on the spot may be preferable to rescue.
     * Colonists with around 5-8 hours before death can be treated by regular doctors, or by good doctors without medicine.
     * Colonists with 12 hours or more till death can wait.
  2. Colonists sick with deadly diseases should also receive priority care, especially those with wound [infections](/wiki/Infection "Infection") or the [plague](/wiki/Plague "Plague").
  3. Non-bleeding colonists aren't in a great risk of both infections or blood loss; they should be put on the bottom of your priority list.



If left undirected, doctors will automatically tend in order: 

  1. The nearest patients that will die from blood loss in 18 hours
  2. The nearest human patients
  3. Himself/herself if self-tend is enabled
  4. (Feed patients in bed)
  5. (Surgeries)
  6. (Rescue downed colonists and pets by taking them to bed)
  7. The nearest non-human patients



Note that this automatic priority does not take into account the overall severity and lethality of all the illnesses, infections, and injuries afflicting patients, other than the death from blood loss in 18 hours limit. Nor does it prioritize colonists over prisoners or visitors. If imminent death is a concern, it's not a good idea to rely on this default behavior. 

### Medicine allocation[[edit](/index.php?title=Doctoring&action=edit&section=23 "Edit section: Medicine allocation")]

Doctors will always tend to use the best medicine possible by default. To counteract this, set colonists' healthcare to Normal medicine or worse. Switch to Glitterworld medicine only if the colonist is down with a fast-working illness and you don't have a decent doctor on board, or they are about to receive a difficult operation. 

You can also manually forbid medicine so they will be forced to use lower-tier medicine, saving your better medicine for later. 

You should try to split your medicine apart into many stacks. If a doctor is about to treat a patient and someone else is getting medicine from a stack, your doctor will use medicine from another stack, or if there's none, he will try to dry-bandage the injured colonist. To combat this, you can draft doctors to go towards the medicine stacks, and manually un-draft and assign them to treat colonists when a doctor is finished taking the medicine. 

### Positioning[[edit](/index.php?title=Doctoring&action=edit&section=24 "Edit section: Positioning")]

Medicine should always be put near the hospital. Don't put them right inside the hospital as it reduces beauty unless you're willing to build a shelf to put them in. If you're anticipating the need for a treatment, have a doctor stand near your stocks of medicine. You can immediately get the doctor to heal them without having to have him go to the medicine storage and back, saving time. If using primarily herbal meds then it is best to cool the room. It will rarely be necessary to freeze them, but it could make the difference 

### Hospital design[[edit](/index.php?title=Doctoring&action=edit&section=25 "Edit section: Hospital design")]

[![](/images/thumb/2/26/8_hospital_beds_compact.png/150px-8_hospital_beds_compact.png)](/wiki/File:8_hospital_beds_compact.png)

[](/wiki/File:8_hospital_beds_compact.png "Enlarge")

Compact placement of 8 hospital beds around a [vitals monitor](/wiki/Vitals_monitor "Vitals monitor").

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Doctoring&action=edit). Reason:** _This section is good base but theres room for further develpment._  
---|---  
  
  * Assuming you're constructing new beds, or comparing beds of the same quality, prioritize [hospital beds](/wiki/Hospital_bed "Hospital bed") over other bed types, and beds over [bedrolls](/wiki/Bedroll "Bedroll"). Avoid using [sleeping spots](/wiki/Sleeping_spot "Sleeping spot") unless necessary. However, also see the note on quality below.
  * Compare the stats of the beds placed in the hospital - while Immunity Gain Speed Factor depends solely on the type of bed, Surgery Success Chance Factor is dependent on [quality](/wiki/Quality "Quality"). A surgery is more likely to succeed on a Good [Bed](/wiki/Bed "Bed") than an Awful Hospital Bed, but the opposite is true for surviving or recovering from [diseases](/wiki/Diseases "Diseases").
  * A well-equipped hospital will have one or more [vitals monitors](/wiki/Vitals_monitor "Vitals monitor"), which give a bonus to several doctoring-related values, including fighting [infections](/wiki/Infection "Infection") and general healing.
  * [Sterile tiles](/wiki/Sterile_tile "Sterile tile") improve cleanliness and thus outcomes. [Steel tiles](/wiki/Steel_tile "Steel tile") offer a lesser but still significant buff, and are significantly more accessible due to lower cost and work requirements, as well as being unlocked by a research project that is far more generally useful.
  * Ensure that that every bed has 50% [light](/wiki/Light "Light") around it. Consider lighting the entire room to allow you to safely place additional sleeping spots in case of overflow.



## Version history[[edit](/index.php?title=Doctoring&action=edit&section=26 "Edit section: Version history")]

  * [0.9.722](/wiki/Version/0.9.722 "Version/0.9.722") \- Surgery can fail now, sometimes catastrophically. Failure chance is related to the surgeon’s medical skill and the quality of the medicine.
  * Alpha 17 - It is now possible to change the default healthcare given to pawns. Defaults to best meds for colonists and herbal meds for everybody else.
  * Beta 18 - all surgeries now have a minimum 2% chance of failure, no matter how good everything is.
  * [1.3.3159](/wiki/Version/1.3.3159 "Version/1.3.3159") \- Display current and required total tend qualities in the tooltip for hediffs with HediffComp_TendDuration comp.
  * [1.3.3200](/wiki/Version/1.3.3200 "Version/1.3.3200") \- Total tend quality info is now only displayed if the hediff disappears after a certain level of tend quality (since it's fairly useless otherwise).



Retrieved from "[https://rimworldwiki.com/index.php?title=Doctoring&oldid=183786](https://rimworldwiki.com/index.php?title=Doctoring&oldid=183786)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Pages to be rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten")
  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Health](/wiki/Category:Health "Category:Health")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Doctoring "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Doctoring "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Doctoring "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Doctoring&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Doctoring)
  * [Edit](/index.php?title=Doctoring&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Doctoring&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Doctoring "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Doctoring "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Doctoring&oldid=183786 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Doctoring&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Doctoring)



  * This page was last edited on 31 August 2026, at 23:40.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (180,60,60)
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[28.33 secs]: real-time at 1x speed
  *[Nutrition]: Nutrition gained when this item or object is eaten
  *[Maximum To Ingest]: Maximum Number To Ingest At Once
  *[1.33 secs]: real-time at 1x speed
  *[+4]: Stacking 1 times for a maximum of 4
  *[_Nuzzled_]: It is so cute, and supportive, and loving... I feel fulfilled and refreshed.
  *[+5]: Stacking 10 times with a 0.9 multiplier for maximum of 33
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
