Doctoring - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Doctoring

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 

This article is suggested to be rewritten. Reason: Cleanup, fact check, verification. You can help the RimWorld Wiki by improving it.

Contents

- 1 Skill

- 2 Medicines

- 2.1 Treatment options

- 2.2 No medical care

- 2.3 Doctor care, but no medicine

- 2.4 Herbal medicine

- 2.5 Medicine

- 2.6 Glitterworld medicine

- 3 Treatment

- 3.1 Tend quality

- 3.1.1 Total tend quality

- 3.2 Draft Tending

- 4 Operations

- 4.1 Operation Success Rate

- 4.2 Calculating success

- 4.3 Surgical inspection

- 4.4 Failure

- 4.5 Available targets

- 4.6 Tips on Improving Success

- 5 Infection

- 6 Strategies

- 6.1 Triage

- 6.2 Medicine allocation

- 6.3 Positioning

- 6.4 Hospital design

- 7 Version history

Doctoring is a type of work assigned to colonists from the Work menu. The Medical skill is the primary determinant for success. Colonists incapable of Caring will never perform doctor work.

Doctor work assigns pawns to the following jobs: tending to patients, tending to self (if enabled), feeding patients, performing surgical operations, rescuing downed pawns or downed tamed animals, tending to and operating on animals, feeding ill animals, and cheering up patients. 

How well a colonist performs in Doctoring mainly depends on their medical skill, the quality of medicine used, and the cleanliness of the room in which they are operating. The doctor's physical condition plays an important role, too.

Doctors can heal other colonists, guests, prisoners or animals and will prioritize life-threatening wounds and illnesses before tending minor conditions.

Doctors can "self-tend" at 70% effectiveness to treat their own wounds or illnesses. Disabled by default, the self-tend option can be enabled in a pawn's Health-overview.

Skill[edit]

The Medicine skill is the center skill of doctoring in RimWorld. It directly multiplies the tend quality as well as surgery success chance and tend speed before other factors are taken in. All values in this table take post-processing into account where necessary.

Doctor Level

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

Base Tend Quality

20%
30%
40%
50%
60%
70%
80%
90%
100%
105%
110%
115%
120%
125%
130%
135%
140%
145%
150%
152.5%
155%

Medical Tend Speed

40%
46%
52%
58%
64%
70%
76%
82%
88%
94%
100%
106%
112%
118%
124%
130%
136%
142%
148%
154%
160%

Base Surgery Success Chance

10%
20%
30%
40%
50%
60%
70%
75%
80%
85%
90%
92%
94%
96%
98%
100%
102%
104%
106%
108%
110%

The following table documents a few of many possible combinations of how factors play into a colonist's performance at doctoring (needs updating for A17):

Colonist

Medicine Skill

Base Tend Quality

Manipulation &#91;1&#93;

Sight &#91;2&#93;

Final Tend Quality &#91;3&#93;

A &#91;4&#93;

6
80%
100%
100%
80%

B &#91;5&#93;

18
200%
60%
30%
62.72%

C &#91;6&#93;

3
50%
190%
140%
89.6%

D &#91;7&#93;

11
130%
50%
100%
71.5%

- ↑ 90% importance in tend quality, effective up to 140%

- ↑ 70% importance in tend quality, effective up to 140%

- ↑ To 2 decimal places

- ↑ Healthy, practitioner in medicine

- ↑ Bad back, frail, and cataracts, visionary in medicine

- ↑ Fully bionic trauma savant, basic familiarity with medicine

- ↑ Missing an arm, strong expert with medicine

The amount of XP gained from tending depends on the type of medicine used, and what it is used on (human or animal). The equation for this is:

XP = Patient XP Factor &#215; Medicine XP Factor &#215; Doctor's Learning Rate

Where:

- Patient XP Factor is a multiplier from the patient type. ×175 for animal patients, and ×500 for human patients.

- Medicine XP Factor is the medicine's potency multiplied by 0.7, and clamped in the range of 0.5 and 1.

- Doctor's Learning Rate is the doctor's own multiplier on XP gained for the medicine skill. See "Improving Skills" for more details.

Medicine

Potency

XP Factor

Tend XP from patient

Human
Animal

 None

0.30
0.5
250
87.5

 Herbal medicine

0.60
0.5
250
87.5

 Medicine

1.00
0.7
350
122.5

 Glitterworld medicine

1.60
1
500
175

Medicines[edit]

Medicine is used to improve the results of doctoring, therefore improving recovery from injuries and disease, and also allowing operations to be performed. Another perk to using medicine is that medicine is typically able to heal multiple low severity injuries (up to max of 20 damage worth of severity), which is something that 'dry-bandaging' can't do.

There are currently three types of medicine in RimWorld: the organic herbal medicine, the standard medicine, and the rare glitterworld medicine - in order from least potent to most potent.

It is possible to change the default healthcare given to pawns. Defaults to glitterworld medicine for colonists, herbal meds for everybody else, and no medicine for entities.. To do this go under assign or animals and click on the medicine icon next to a pawn, holding click and dragging allows multiple pawns to have their medicine changed. The default medicine assigned can be changed by going under a pawn's health tab and clicking "Allow medicine" and then "change defaults"

Treatment options[edit]

Five treatment options are available; none at all, doctor care, herbal medicine or worse, regular medicine or worse, or best quality medical care. 

For prisoners and guests the default is herbal medicine; colonists default to best care available.

In the early game, however, it is ideal to set the medical policy so that all pawns on the map only get basic doctor treatment. This allows precious medicine to be stockpiled for emergencies and operations, rather than wasted on minor injuries.

No medical care[edit]

This option prevents pawns from receiving any sort of medical care. Leaving them to die or rarely recover on their own.

As doctor care does not require any medicine, this option is not recommended unless your intent is to let the pawn die. If the colony has Slaughtering animals precept, this can be useful to prevent doctors from tending to pen animals that inevitably overpopulate and start starving to death, saving their time for other matters. Pawns with that precept are not affected by tamed animals dying to natural causes.

Doctor care, but no medicine[edit]

Doctors will attempt to perform a treatment without any sort of medicine, this is far slower than without medicine and treats only 1 wound at a time, due to the lower potency chances of infection occurring or immunity being outpaced by severity on diseases are higher. Note that it is not possible to do most operations without medicine.

This is also ideal to use on bruises or long-term ailments that can't cause death in-order to save resources, such as asthma, and Sensory/Fibrous Mechanites 

Attributes

Medical Potency
Max tend quality
Market Value
Mass (kg)

Values

30%
70%
N/A
N/A

Tend quality

Doctor Level

0
3
6
9
12
15
18
20

Base Avg. Quality

6%
15%
24%
31.5%
36%
40.5%
45%
46.5%

Base Surgery Success

-
-
-
-
-
-
-
-

Herbal medicine[edit]

Herbal medicine is an organic medicine which can be grown from healroots, or acquired from tribal factions. It is a cheap medicine that can be used for bleeding injuries, diseases that don't need more than 70% tend quality, and operations with a high success rate or where the patient's life doesn't matter such as organ-harvesting.

Attributes

Medical Potency
Max tend quality
Market Value
Mass (kg)

Values

60%
70%
10
0.35

Tend quality

Doctor Level

0
3
6
9
12
15
18
20

Base Avg. Quality

12%
30%
48%
63%
72%
81%
90%
93%

Base Surgery Success

12%
30%
48%
55.2%
57%
57.9%
58.8%
59.4%

Medicine[edit]

Standard medicine is the benchmark of medical treatment solutions, and is also producible at a drug lab by combining herbal medicine, neutroamine, and cloth. It can additionally be purchased from outlanders and orbital traders, and is occasionally dropped by pirate raiders and mercenaries. 

Medicine is best used for bridging the immunity gap of illnesses or for installing body parts, though the risk of failure is still present. Odds can be improved by boosting manipulation through drugs like go-juice and wake-up or implants.

It's not the best idea to excise carcinomas using ordinary medicine due to its 0.7x success factor and 25% death chance on failure. Saving it until your surgeon has at least a surgery success chance of 128.5% (achievable with a pair of bionic arms) is better as it translates to a roughly 90% success chance.

Attributes

Medical Potency
Max tend quality
Market Value
Mass (kg)

Values

100%
100%
18
0.5

Tend quality

Doctor Level

0
3
6
9
12
15
18
20

Base Avg. Quality

20%
50%
80%
100%
100%
100%
100%
100%

Base Surgery Success

20%
50%
80%
92%
95%
96.5%
98%
99%

Glitterworld medicine[edit]

Glitterworld medicine is the most powerful medicine out of the three types available, and can only be found through trading with exotic good traders and faction bases or as a quest reward. Despite the high price, Glitterworld Medicine carries a value which no other medicine can carry: enhanced medical potency. Naturally, due to the cost, Glitterworld Medicine isn't worth the price for treating trivial diseases or injuries - but it makes surgery significantly easier, and allows even mediocre doctors to guarantee success in operations.

It is mostly useful for lowering the luck factor in treatment for diseases that would be otherwise lethal or low success rate operations such as excising cancerous growths, or installing bionics. Other medicine will be satisfactory for injuries or diseases with a low immunity to severity gap.

With DLCs, Glitterworld medicines gains more uses. Treating paralytic abasia and blood rot which both cost 10 units, and the Biosculpter pod's bioregeneration cycle costs 2 and heals missing small limbs and scars.

Attributes

Medical Potency
Max tend quality
Market Value
Mass (kg)

Values

160%
130%
50
0.5

Tend quality

Doctor Level

0
3
6
9
12
15
18
20

Base Avg. Quality

32%
80%
100%
100%
100%
100%
100%
100%

Base Surgery Success

32%
80%
100%
100%
100%
100%
100%
100%

Treatment[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Tend time? how amny wounds are tended, and what controls that, what does tending do to thw injuries? etc? Has stats but little.in the way of actual mechanics.

Basic medical work involving tending to wounds and illnesses. Treating wounds stop them from bleeding and reduce the chance of infections, while tending to illnesses slows them down allowing your colonists' immune systems to catch up and pull ahead.

Each individual treatment can have any quality from 0 - 130%, depending on the medicine used. Higher quality makes infections less likely and slows down illnesses more.

After each treatment there will be text feedback showing the wound/illness tended and the quality of the treatment. Only 1 injury will generate feedback at a time even if multiple are treated at once.

Tend quality[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Does not explain what Tend Quality actually does.

First, Base Tend Quality is calculated. Then, other factors apply if relevant. Tend Quality is adjusted up to 25% up or down randomly. Finally, the Tend quality is limited to a range between 0% and the Max Tend Quality of the medicine used. 

1. Base Tend Quality

Base Tend Quality = Medical Tend Quality × Medical Potency
1.a. Offsets from hospital bed and vitals monitor
If applicable, Medical Tend Quality Offset from the bed is added to the Base Tend Quality value. This offset only exists on Hospital Beds and Vitals Monitors attached to hospital beds. No other beds have Medical Tend Quality Offset.
Laying Down is not a factor. Draft tends on injured colonists standing up will have the same Medical Tend Qualities as tends while laying in a standard bed.
Medical Tend Quality with Offset = Base Tend Quality + 0.1 Hospital Bed (if applicable) + 0.07 Vitals Monitor (if applicable)
1.b. Self tend factor
If Self Tending, Tend Quality with Offset is adjusted by 70%.
Medical Tend Quality with Self Tend = Medical Tend Quality with Offset * 0.7 Self Tend Factor (if applicable)
2. Randomization

Medical Tend Quality is then randomized.
Randomized Tend Quality = Medical Tend Quality with Self Tend * Random Value between 0.75 and 1.25
3. Maximum tend quality

The Final Tend Quality is then limited to a range of 0 to Maximum Tend Quality from Medicine used.
Final Tend Quality = Clamped 0% to Maximum Tend Quality from Medicine
The maximum tend quality of each medicine is as follows:
- 70% for herbal medicine or no medicine

- 100% for medicine

- 130% for glitterworld medicine

Notes:

- Light is not a factor of Medical Tend Quality. It is, however, a factor of Global Work Speed and thus of Medical Tend Speed and a factor of Surgery Success Chance.

- Cleanliness is not a factor of Medical Tend Quality. It is, however, a factor of Infection Chance.

- Being indoors or outdoors is not a factor of Medical Tend Quality. It is, however, a factor of cleanliness and thus Infection Chance.

Total tend quality[edit]

Some medical issues are cured when the sum of all tends performed reach a certain value. This is described as "total tend quality". The current total and the required total to cure will be displayed in the mouse-over menu on the issue in question on the pawn's health menu. The value will not be displayed for issues not cured by total tend quality, so its presence is a clear indicator of how to cure the issue. 

The following diseases use this mechanic: 

- Gut worms

- Muscle parasites

Draft Tending[edit]

Drafted colonists can be forced to tend wounds of injured pawns using right click. The injured pawn does not need to be laying down in order to be draft tended. One can even Draft Tend an injured pawn on a non-aggressive mental break or a downed enemy in the field. The tend quality of Draft Tended injuries uses the same formula as undrafted treatment. The "Tend (without medicine)" option is useful for emergency treatment. The option "Tend ___" that does not say (without medicine) will use the medicine in the doctor's inventory regardless of the targets medical settings. After using the medicine in inventory, the doctor will grab the nearest medicine of any quality.

Operations[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: More complete operations table - rough outline of one available here.

An operation is a bill to be performed on a colonist by a doctor. This may involve the removal or addition of body parts, administration of drugs or excising carcinomas. Many operations require a minimum Medical skill (e.g. excising a carcinoma requires level 10). Some operations require a minimum medicine level (Herbal medicine is the minimum required medicine for most operations).

Operation Success Rate[edit]

When an operation is performed, a degree of chance is calculated to assess the probability that the outcome of the operation will be successful.

This is determined as a product of:

- The Surgery Success Chance stat of the surgeon performing the operation

- The Medical Potency stat of the Medicine used for performing the operation

- The Surgery Success Chance Factor stat of a bed or other sleep furniture upon which the operation is performed

- The Success Rate Multiplier for the specific operation

- Inspired Surgery Factor

This may be expressed as:

Operation Success Rate = Surgery Success Chance Surgeon × Surgery Success Chance Bed × Medical Potency × Operation Success Rate Multiplier × Inspired Surgery Factor

Note that additionally:

- The resulting Operation Success Rate is capped at 98%.

- If the Operation Success Rate Multiplier is Can't fail, the Operation Success Rate will always be 100%, regardless of any other stats.

Calculating success[edit]

Surgeon's Medical Surgery Success Chance stat

- Determined by Medical skill. (see #Skill section)

- Manipulation acts as a direct multiplier. For example, 115% Manipulation = x1.15 success.

- Sight acts as a direct multiplier at 100% and below. For example, 90% Sight = x0.9 success but 110% Sight = x1 success.

Bed's Surgery Success Chance Factor stat

- Determined by type of bed and its quality. Beds and bedrolls have a modifier of 1.0. Hospital beds have a modifier of 1.15. Quality is a multiplier. Material does not matter.

- Then multiplied by the room's cleanliness stat. It is 1 for 0 cleanliness and 1.018 for a clean room with sterile flooring. The minimum is 0.6, reached at -5 cleanliness and also applied outdoors.

- Then multiplied by light factor. If the head of the bed has lighting below 50%, there is a penalty. It reaches 0.75 in complete darkness.

- If surgery is done outdoors, there is an 0.85 penalty multiplier (on top of the aforementioned 0.6 cleanliness multiplier).

Medical Potency

- Determined by the type of medicine. The medicine item (industrial medicine) has a modifier of 1.0. (see Medical Potency)

Operation Success Rate Multiplier

- Modifier dependent on the type of operation.

Operation
Operation Success Rate Multiplier (%)

Administer [drug]

Can't fail

Anesthetize

200

Cure scaria

100

Euthanize by cut

500

Excise carcinoma

100

Harvest [body part]

120

Install [body part or implant]

100

Remove [body part or implant]

120

Sterilize

100

Anti-abasia mechanite infusion 

100

Cure blood rot 

100

Blood transfusion 

100

Extract hemogen pack 

100

Extract ovum for IVF 

500

Implant embryo 

500

Implant IUD 

100

Implant xenogerm 

100

Perform tubal ligation 

100

Perform vasectomy 

100

Remove IUD 

100

Reverse vasectomy 

100

Terminate pregnancy 

200

Bliss lobotomy 

100

Ghoul infusion 

100

Surgical inspection 

150

Note that the Success Rate Multiplier for each operation is shown in-game on the Information page for an added bill in the Colonist's Health → Operations tab.

Inspired Surgery Factor

- 1 by default.

- 2 if the surgeon has inspired surgery inspiration.

Surgical inspection[edit]

This section relates to content added by Anomaly (DLC). Please note that it will not be present without the DLC enabled.

Spoiler warning: This section may contain details about the gameplay that might be considered spoilers.
If you wish to enjoy the content first hand, you probably shouldn't continue reading beyond this point. 

With the Anomaly DLC surgical inspections can be used to diagnose hediffs before they are made visible. This operation deals cut damage to a random body part including the brain and checks for any hediffs on the pawn.

Note that a doctor may lie about the results of the inspection if it is in their own self-interest. This only happens when the doctor has been implanted with a metalhorror and would otherwise discover a metalhorror in another pawn - the doctor will instead say they found nothing.

Hediff
Description

Resurrection psychosis

{PAWN_nameDef} is suffering from a terminal case of resurrection psychosis, a condition caused by the decoherence of resurrection mechanites. The condition will slowly worsen, eventually resulting in death.

Toxic buildup

{PAWN_nameDef} is showing early signs of toxic buildup. Keep {PAWN_objective} away from sources of toxins.

Rot stink exposure

{PAWN_nameDef} is beginning to suffer from exposure to rot stink gas. Keep {PAWN_objective} away from rotting corpses and other sources of rot stink.

Organ decay

{PAWN_nameDef} is showing early signs of a severe condition which will cause their organs to rapidly deteriorate. {SURGEON_nameDef} can't yet tell exactly what is causing this, but {PAWN_nameDef} will become very ill within the next few days.

Crumbling mind

{PAWN_nameDef} is showing early signs of a severe condition which will soon cause severe mental degradation. {SURGEON_nameDef} can't yet tell exactly what is causing this, but {PAWN_nameDef} will become very ill within the next few days.

Duplicate sickness

{PAWN_nameDef} is suffering from duplicate sickness. Psychic interference between this person and their duplicate is causing slow mental deterioration. As long as multiple copies of this person are alive, the condition will keep getting worse.

Psychic agony

{SURGEON_nameDef} detected a faint but painful psychic presence emanating from {PAWN_nameDef} but failed to understand what was causing it.

Metalhorrors lack a description and instead emerge if they were detected beforehand through interrogation or enough samples were collected to reveal it through a surgical inspection.

Failure[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: How are they selected?.

If an operation fails then the colonist will take damage, and materials (including prosthetics) will be wasted. For lesser failures, damage is concentrated near the site of the operation, while for the ridiculous failures they can be found anywhere in the body.

There are 3 kinds of surgical failure in-game.

- Minor: Deals a little damage, and will not destroy any body parts.

- Catastrophic: Deals great damage, and usually destroys body parts outright.

- Ridiculous: Deals great damage scattered across the entire body.

In addition, each operation has a death on failure chance; when it fails it is possible that the colonist instantly dies.

Available targets[edit]

Surgeons can perform operations on colonists, prisoners or guests. Performing harmful operations on guests or prisoners will anger the faction.

Tamed animals can be operated on as well, though there are limited options. Downed wild animals with the exception of Insectoids can also be operated on once dragged to an animal sleeping spot. Entities except for Ghouls cannot be operated on at all.

Tips on Improving Success[edit]

The difference between a level 10 surgeon (93% base surgery success chance) and a level 20 surgeon (99%) is only a 6.5% gain in surgical success rate. The difference between Herbal Medicine (60% potency) and Glitterworld Medicine (160% potency) is a 167% increase in surgical success rate.

Due to the 98% success cap, using glitterworld medicine for surgeries is mostly only worthwhile in lower-quality surgical environments (less cleanliness, lower quality hospital beds, unskilled doctors). Beyond that point, industrial medicine is sufficient for the purposes of surgery.

Infection[edit]

When a bed is set to be medical, selecting it shows the infection chance modifier of the room. The overall chance of infection is affected by tend quality, and then multiplied by the aforementioned number. Any bed, no matter what it is, has a 100% modifier on infection when outdoors, and only an incredibly dirty room can get close to this number. However, even at an 80% modifier, wounds tended by an unskilled doctor using herbal meds is likely to be around 10-20% infection chance per wound. As each infection will share the same immunity progress, this is not as bad as it may sound - if the pawn has immunity to an infection, they are effectively immune to all infections until the last one fades away.

It is much better to make the hospital as clean as possible. Start by covering or removing all natural floors (dirt, sand etc. but excluding stone) and ensure that the hospital is cleaned before tending to pawns. Keep all pawns, especially animals out to keep the room as clean as possible. Infection chance multiplier will likely become around the 40-50% mark or even lower. Next, unlock sterile tiles. A room with 0.6 cleanliness can have multipliers near 30%. To see the cleanliness of rooms, toggle on the room stats view on the bottom right corner and then mouse over the hospital (or any other room for that matter). Dirt, animal filth among other things drastically reduces cleanliness, and it also reduces beauty. This makes it possible to locate and prioritize cleaning through the beauty view. Remember to clean before the treatment when possible.

One of the most difficult things about keeping a hospital clean is bleeding. Bleeding colonists will leave blood on the floor, and blood reduces cleanliness. Someone hemorrhaging to death may create 4 or 5 blood splatters on the floor in a very short time, and if this is happening to multiple colonists after a disastrous raid, your doctor alone may not be enough to keep the room clean. Bring in another colonist or two to clean up after other patients awaiting treatment. What is important is the cleanliness at the time of treatment.

Other things like the presence of hospital beds and better medicine/doctors can reduce infection chance to next to nothing, and make it a non-issue when it does occasionally arise.

Strategies[edit]

You will often need to make the most out of the doctors you have, to ensure maximum doctoring efficiency and colonist survival rate/ well-being.

Triage[edit]

You should have doctors prioritize treating patients according to their illness/infection/injury severity.

- Bleeding colonists should receive priority care as they may bleed to death or receive nasty infections. Always prioritize colonists closer to death.
- Colonists about to die (<1 hours until death) are generally not worth saving unless you have extremely good bionic-enhanced doctors that can reach and patch them up in time.
- Strip them to recover their clothes so they won't become tainted. How you will deal with the dead colonist is up to you.

- If a Biosculpter pod is available, put them into a medic cycle. This is also useful for infections that have about a 10% immunity to severity gap.

- If you have a colonist with the Coagulate ability, such as a Sanguophage, it can even save colonists who are mere seconds away from death.

- Colonists that are very close (1-4 hours till death) to dying should have the best doctors care over them. Draft-tending on the spot may be preferable to rescue.

- Colonists with around 5-8 hours before death can be treated by regular doctors, or by good doctors without medicine.

- Colonists with 12 hours or more till death can wait.

- Colonists sick with deadly diseases should also receive priority care, especially those with wound infections or the plague.

- Non-bleeding colonists aren't in a great risk of both infections or blood loss; they should be put on the bottom of your priority list.

If left undirected, doctors will automatically tend in order:

- The nearest patients that will die from blood loss in 18 hours

- The nearest human patients

- Himself/herself if self-tend is enabled

- (Feed patients in bed)

- (Surgeries)

- (Rescue downed colonists and pets by taking them to bed)

- The nearest non-human patients

Note that this automatic priority does not take into account the overall severity and lethality of all the illnesses, infections, and injuries afflicting patients, other than the death from blood loss in 18 hours limit. Nor does it prioritize colonists over prisoners or visitors. If imminent death is a concern, it's not a good idea to rely on this default behavior.

Medicine allocation[edit]

Doctors will always tend to use the best medicine possible by default. To counteract this, set colonists' healthcare to Normal medicine or worse. Switch to Glitterworld medicine only if the colonist is down with a fast-working illness and you don't have a decent doctor on board, or they are about to receive a difficult operation.

You can also manually forbid medicine so they will be forced to use lower-tier medicine, saving your better medicine for later.

You should try to split your medicine apart into many stacks. If a doctor is about to treat a patient and someone else is getting medicine from a stack, your doctor will use medicine from another stack, or if there's none, he will try to dry-bandage the injured colonist. To combat this, you can draft doctors to go towards the medicine stacks, and manually un-draft and assign them to treat colonists when a doctor is finished taking the medicine.

Positioning[edit]

Medicine should always be put near the hospital. Don't put them right inside the hospital as it reduces beauty unless you're willing to build a shelf to put them in. 
If you're anticipating the need for a treatment, have a doctor stand near your stocks of medicine. You can immediately get the doctor to heal them without having to have him go to the medicine storage and back, saving time. If using primarily herbal meds then it is best to cool the room. It will rarely be necessary to freeze them, but it could make the difference

Hospital design[edit]

 
Compact placement of 8 hospital beds around a vitals monitor.

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: This section is good base but theres room for further develpment.

- Assuming you're constructing new beds, or comparing beds of the same quality, prioritize hospital beds over other bed types, and beds over bedrolls. Avoid using sleeping spots unless necessary. However, also see the note on quality below.

- Compare the stats of the beds placed in the hospital - while Immunity Gain Speed Factor depends solely on the type of bed, Surgery Success Chance Factor is dependent on quality. A surgery is more likely to succeed on a Good Bed than an Awful Hospital Bed, but the opposite is true for surviving or recovering from diseases.

- A well-equipped hospital will have one or more vitals monitors, which give a bonus to several doctoring-related values, including fighting infections and general healing.

- Sterile tiles improve cleanliness and thus outcomes. Steel tiles offer a lesser but still significant buff, and are significantly more accessible due to lower cost and work requirements, as well as being unlocked by a research project that is far more generally useful.

- Ensure that that every bed has 50% light around it. Consider lighting the entire room to allow you to safely place additional sleeping spots in case of overflow.

Version history[edit]

- 0.9.722 - Surgery can fail now, sometimes catastrophically. Failure chance is related to the surgeon’s medical skill and the quality of the medicine.

- Alpha 17 - It is now possible to change the default healthcare given to pawns. Defaults to best meds for colonists and herbal meds for everybody else.

- Beta 18 - all surgeries now have a minimum 2% chance of failure, no matter how good everything is.

- 1.3.3159 - Display current and required total tend qualities in the tooltip for hediffs with HediffComp_TendDuration comp.

- 1.3.3200 - Total tend quality info is now only displayed if the hediff disappears after a certain level of tend quality (since it's fairly useless otherwise).

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Doctoring&oldid=183786"

 Categories: - Pages to be rewritten
- Stubs
- Health

 

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

 
 

 

 
 - This page was last edited on 31 August 2026, at 23:40.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -