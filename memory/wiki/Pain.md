Pain - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Pain

 
 From RimWorld Wiki

 

 

 
 

 Jump to navigation
 Jump to search
 

This article is a stub. You can help RimWorld Wiki by expanding it. Reason: Needs detailed numbers on stat penalties. Psycasting. anomaly sources e.g. flesh body parts etc. neural heat buff.

This article is about the stat. For the ideoligious precept of the same name, see Ideoligion.
 
Pain is a pawn capacity: How much pain a person feels. 

Most biological creatures including colonists, raiders, and animals feel pain caused by injuries. A pawn's pain level ranges from 0% to 100% and is displayed on their Health tab's Overview. Pain levels are None, Little, Moderate, Severe, and Extreme.[Detail Needed] Even a little pain causes unhappy thoughts. Once pain passes 10%, it'll start to have an effect on consciousness. If a pawn's pain level meets or exceeds their Pain Shock Threshold they'll go into shock, unable to move. Pawns with the Wimp trait will be incapacitated with only minor pain of 30%.

Most pain is temporary, but scars and certain diseases can cause long-term pain. A painstopper implant or the painblock psycast will get rid of all a colonist's pain and negate any pain-related mood penalties. Note that colonists with the Masochist trait or an ideoligion with the Pain: Idealized precept get a mood bonus from pain instead of a penalty, so it's usually better to leave them alone.

Injuries to the artificial parts do not cause any pain, so colonists with a lot of bionics will generally incur less pain during combat.

Contents

- 1 Formula

- 2 Thresholds

- 3 Factors

- 3.1 Base factors

- 3.2 Offsets

- 4 Version history

Formula[edit]

Pain for a given pawn is the sum of the pain from each individual injury, with two extra steps at the end:

- pain = pain / healthFactor for pawns with a healthFactor other than 1.0 (like grizzly bears and other large animals). Humans have a healthFactor of 1.0, so this doesn't impact humans

- pain = pain * painFactor from health conditions which alter pain. This includes pain-reducing drugs like flake and yayo as well as anesthetic used during operations

Pain from an individual injury is the product of the severity of the injury (the number of HP missing for things like cuts and burns) and the pain per severity for the injury type. For example:

- 30 burn damage causes 30 damage &#215; 0.01875 pain per severity = 56.25% pain

- 30 cut damage causes 30 damage &#215; 0.0125 pain per severity = 37.5% pain

For the complete table of pain vs damage, see Health Difficulties

An exceptional kind of injury is scarification. They take the form of 0.5 HP scars, but give either 11% or 4% pain, for a pain factor of 0.08 or 0.22.

Thresholds[edit]

Pain creates moodlets of different values at 4 stages depending on pain severity.

Level
Required Pain&#160;%
Mood Penalty
(Default)
Mood Buff
(Masochist)
Mood Buff
(Pain:Idealized)

Minor

1%
−5
+5
+3

Serious

15%
−10
+10
+5

Intense

40%
−15
+15
+7

Mind-shattering

80%
−20
+20
+9

A standard pawn will go down upon reaching mind-shattering pain.

Pain inflicts a consciousness penalty that scales with the pain percentage after exceeding 10%. It conforms to the following equation:
IF Pain[%] <= 10% THEN -0% ELSE -{(Pain-0.1)/2.25}[%] For example, 15% pain is 0.15 - 0.1 = 0.05 / 2.25 = 0.02 or 2% consciousness loss.

Graph

 

Factors[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Many other hediffs cause pain or change pain factors. Also injury mechanics. Also how is PainFactor applied? Is it exactly the same as a post factor for other capacities? Math section on final calculation is needed..

Base factors[edit]

Factors cause the game code to MULTIPLY pain X a number. Small numbers reduce pain a lot. Large numbers below 100% reduce pain a little.

- Painstopper: ×0%

- Painless persona trait : ×0%

- Go-juice:
- High: ×10%

- Withdrawal: ×300%

- Painblock psycast: ×10%

- Yayo:
- High: ×50%

- Luciferium:
- High: ×80%

- Psychite tea:
- High: ×90%

- Beer: (See also Offsets)
- Warm: ×90%

- Tipsy: ×80%

- Drunk: ×50%

- Hammered: ×30%

- Blackout: ×10%

- Psychic bond:
- Psychic bond: ×50%

- Reduced pain: ×50%

Offsets[edit]

Offsets cause the game code to ADD OR SUBTRACT a number from the pawn's pain. Small numbers are less effective at reducing pain than large numbers. However, if the pawn only has a small amount of pain, an equally small offset will be totally effective at removing all pain. Positive numbers add pain. Negative numbers reduce pain.

- Mindscrew: +20%

- Sensory mechanites:
- Mild pain: +20%

- Intense pain: +60%

- Blood rot:
- Extreme: +5%

- Fibrous mechanites:
- Mild pain: +20%

- Intense pain: +60%

- Muscle parasites: +20%

- Gut worms: +20%

- Malaria:
- Major: +30%

- Extreme: +30%

- Luciferium:
- Withdrawal: +40%

- Beer: (See also Factors)
- Blackout: +5%

- Stoned on smokeleaf: −20%

- Torture crown: +5%

- Tox gas:
- Mild: +10%

- Moderate: +15%

- Severe: +25%

- Hemogen craving:
- Minor: +5%

- Moderate: +10%

- Major: +15%

- Inhumanization: −50%

Version history[edit]

- 0.6.532 - Added. Pain level is tracked. A character in too much pain will become incapacitated.

- 0.10.785 - Pain now creates unhappiness.

Stats

Capacities
Pain &#8226; Consciousness &#8226; Moving &#8226; Manipulation &#8226; Talking &#8226; Eating &#8226; Sight &#8226; Hearing &#8226; Breathing &#8226; Blood Filtration &#160;&#8226; Blood Pumping &#8226; Digestion
Basics | Important
Market Value &#8226; Market Value Ignoring Hitpoints &#8226; Honor Value 
Non Pawn Important
Nutrition &#8226; Medical Potency &#8226; Medical Tend Quality Maximum &#8226; Max Hit Points
Basics
Mass &#8226; Flammability &#8226; Psychic Sensitivity Factor &#8226; Psychic Sensitivity Offset &#8226; Neural Heat Limit Offset &#8226; Neural Heat Recovery Rate Offset &#8226; Slave Suppression Offset &#8226; Terror (Source) &#8226; Max Install Count 
Pawn
Recreation Fall Rate &#8226; Sleep Fall Rate &#8226; Eating Speed &#8226; Foraged Food Amount &#8226; Minimum Handling Skill &#8226; Mental Break Threshold &#8226; Immunity Gain Speed &#8226; Pain Shock Threshold &#8226; Lifespan Factor &#8226; Minimum Comfortable Temperature &#8226; Maximum Comfortable Temperature &#8226; Injury Healing Factor &#8226; Caravan Riding Speed &#8226; Carrying Capacity &#8226; Filth Rate &#8226; Crawl Speed &#8226; Move Speed &#8226; Max Nutrition &#8226; Rest Rate Multiplier &#8226; Toxic Environment Resistance &#8226; Toxic Resistance &#8226; Animals Learning Factor &#8226; Global Learning Factor &#8226; Neural Heat Limit &#8226; Psychic Sensitivity &#8226; Leather Amount &#8226; Meat Amount &#8226; Neural Heat Recovery Rate &#8226; Meditation Psyfocus Gain &#8226; Neural Heat Gain (Factor) &#8226; Ideoligion Spread Chance &#8226; Global Certainty Loss Factor &#8226; Terror &#8226; Raw Nutrition Multiplier &#8226; Learning Rate Factor &#8226; Cancer Rate Factor &#8226; Fertility &#8226; Hemogen Gain Multiplier &#8226; Vacuum Resistance 
Non Pawn
Construction Speed (Material Factor) &#8226; Deterioration Rate &#8226; Sell Price Multiplier &#8226; Beauty &#8226; Outdoor Beauty &#8226; Cleanliness &#8226; Comfort &#8226; Work To Make &#8226; Food Poison Chance (Food Stat) &#8226; Shooting Accuracy (Turrets) &#8226; Style Dominance 
Mechanoid
EMP Resistance &#8226; Bandwidth Cost &#8226; Energy Usage Multiplier &#8226; Wastepacks Per Recharge &#8226; Control Taking Time &#8226; Repair Energy Cost 
Meditation
Meditation Psyfocus Bonus &#8226; Meditation Plant Growth Offset 
Terrain
Cleaning Time Multiplier &#8226; Filth Multiplier
Apparel
Armor - Material Effect Multiplier &#8226; Insulation - Cold - Material Effect Multiplier &#8226; Insulation - Heat - Material Effect Multiplier &#8226; Equip Delay &#8226; Pack Radius &#8226; Shield Recharge Rate &#8226; Shield Max Energy &#8226; Insulation - Heat &#8226; Insulation - Cold &#8226; Armor - Heat &#8226; Armor - Blunt &#8226; Armor - Sharp &#8226; Jump Range 
Weapon (Ranged)
Ranged Damage Multiplier &#8226; Ranged Cooldown &#8226; Accuracy (Long) &#8226; Accuracy (Medium) &#8226; Accuracy (Short) &#8226; Accuracy (Close)
Weapon (Melee)
Melee Damage Multiplier &#8226; Melee Weapon Average Armor Penetration &#8226; Melee Damage Per Second
Building
Research Speed Factor &#8226; Max Power Output &#8226; Medical Tend Quality Offset &#8226; Work Speed Factor &#8226; Work Efficiency Factor &#8226; Work To Build &#8226; Door Opening Speed &#8226; Rest Effectiveness &#8226; Immunity Gain Speed Factor &#8226; Recreation Power &#8226; Surgery Success Chance Factor &#8226; Reading Bonus &#8226; Trap Spring Chance &#8226; Trap Melee Damage &#8226; Biosculpter Pod Speed Factor &#8226; Assembly Speed Factor &#8226; Baby Play Power &#8226; Birth Quality Offset &#8226; Genetic Complexity Increase 
Ability
Detection Chance &#8226; Goodwill Impact &#8226; Effect Radius &#8226; Duration &#8226; Range &#8226; Psyfocus Cost &#8226; Neural Heat Gain &#8226; Casting Time &#8226; Psylink Level
Stuff Stat Factors (Multipliers when made of this)
Melee Cooldown &#8226; Sharp Damage &#8226; Blunt Damage &#8226; Insulation - Heat (Material Factor) &#8226; Insulation - Cold (Material Factor) &#8226; Armor - Heat (Material Factor) &#8226; Armor - Blunt (Material Factor) &#8226; Armor - Sharp (Material Factor)
Mechanitor 
Mech Bandwidth &#8226; Mech Control Groups &#8226; Mech Gestation Speed &#8226; Mech Remote Repair Distance &#8226; Mech Remote Shield Distance &#8226; Mech Remote Shield Energy &#8226; Mech Repair Speed &#8226; Subcore Encoding Speed &#8226; Mech Work Speed Offset 
Pawn | Combat
Stagger Time Multiplier &#8226; Ranged Cooldown Multiplier &#8226; Aiming Time &#8226; Pawn Trap Spring Chance &#8226; Incoming Damage Multiplier &#8226; Accuracy Factor (Long) &#8226; Accuracy Factor (Medium) &#8226; Accuracy Factor (Short) &#8226; Accuracy Factor (Close) &#8226; Shooting Accuracy (Indoors Dark &#8226; Indoors Lit &#8226; Outdoors Dark &#8226; Outdoors Lit ) &#8226; Mortar Miss Radius Multiplier &#8226; Melee Armor Penetration &#8226; Melee Dodge Chance (Indoors Dark &#8226; Indoors Lit &#8226; Outdoors Night &#8226; Outdoors Day ) &#8226; Melee Hit Chance (Indoors Dark &#8226; Indoors Lit &#8226; Outdoors Dark &#8226; Outdoors Lit ) &#8226; Melee DPS &#8226; Melee Damage Factor &#8226; Melee Cooldown &#8226; Melee Door Damage Factor &#8226; Shooting Accuracy Multiplier (Child) 
Social
Bond Chance Factor &#8226; Train Animal Chance &#8226; Tame Animal Chance &#8226; Arrest Success Chance &#8226; Beauty (Pawn) &#8226; Social Impact &#8226; Drug Sell Price Improvement &#8226; Trade Price Improvement &#8226; Negotiation Ability &#8226; Suppression Power &#8226; Conversion Power &#8226; Slave Suppression Fall Rate &#8226; Animal Products Price Improvement 
Misc
Biosculpter Occupant Speed &#8226; Growth Vat Occupant Speed 
Work
Cleaning Speed Multiplier &#8226; Butchery Speed &#8226; Mechanoid Shredding Speed &#8226; Hunting Stealth &#8226; Research Speed &#8226; Smelting Speed &#8226; Smoothing Speed &#8226; Animal Gather Speed &#8226; Animal Gather Yield &#8226; Hacking Speed &#8226; Drug Cooking Speed &#8226; Drug Synthesis Speed &#8226; Butchery Efficiency &#8226; Mechanoid Shredding Efficiency &#8226; Cooking Speed &#8226; Food Poison Chance &#8226; Plant Work Speed &#8226; Plant Harvest Yield &#8226; Drug Crop Harvest Yield &#8226; Reading Speed &#8226; Repair Success Chance &#8226; Construct Success Chance &#8226; Construction Speed &#8226; Medical Tend Speed &#8226; Medical Tend Quality &#8226; Medical Operation Speed &#8226; Medical Surgery Success Chance &#8226; Mining Speed &#8226; Deep Drilling Speed &#8226; Mining Yield &#8226; General Labor Speed &#8226; Global Work Speed &#8226; Pruning Speed &#8226; Activity Suppression Speed &#8226; Study Efficiency &#8226; Entity Study Rate &#8226; Fishing Speed &#8226; Fishing Yield &#8226; Piloting Ability 
Psychic Ritual 
Psychic Ritual Quality &#8226; Psychic Ritual Quality Offset 
Containment 
Cold Containment Bonus &#8226; Containment Strength &#8226; Minimum Containment Strength 
Hidden
Bed Hunger Rate Multiplier

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Pain&oldid=183459"

 Categories: - Stubs
- Capacity

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

 
 

 

 
 - This page was last edited on 23 August 2026, at 00:00.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -