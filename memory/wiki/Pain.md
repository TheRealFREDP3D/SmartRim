# Pain

From RimWorld Wiki

Jump to navigation Jump to search

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This article is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Pain&action=edit). Reason:** _Needs detailed numbers on stat penalties. Psycasting. anomaly sources e.g. flesh body parts etc. neural heat buff._  
---|---  
  
This article is about the stat. For the ideoligious precept of the same name, see [Ideoligion](/wiki/Pain_\(precept\) "Pain \(precept\)").

**Pain** is a [pawn capacity](/wiki/Capacity "Capacity"): How much pain a person feels. 

Most biological creatures including [colonists](/wiki/Colonist "Colonist"), [raiders](/wiki/Raider "Raider"), and [animals](/wiki/Animals "Animals") feel pain caused by [injuries](/wiki/Injury "Injury"). A pawn's pain level ranges from 0% to 100% and is displayed on their Health tab's Overview. Pain levels are None, Little, Moderate, Severe, and Extreme.[Detail Needed] Even a little pain causes unhappy [thoughts](/wiki/Thoughts_list "Thoughts list"). Once pain passes 10%, it'll start to have an effect on [consciousness](/wiki/Consciousness "Consciousness"). If a pawn's pain level meets or exceeds their [Pain Shock Threshold](/wiki/Pain_Shock_Threshold "Pain Shock Threshold") they'll go into [shock](/wiki/Injury#Shock "Injury"), unable to move. Pawns with the [Wimp](/wiki/Wimp "Wimp") trait will be incapacitated with only minor pain of 30%. 

Most pain is temporary, but [scars](/wiki/Injury#Scarring "Injury") and certain [diseases](/wiki/Disease "Disease") can cause long-term pain. A [painstopper](/wiki/Painstopper "Painstopper") implant or the [painblock](/wiki/Painblock "Painblock") psycast [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") will get rid of all a colonist's pain and negate any pain-related mood penalties. Note that colonists with the [Masochist](/wiki/Masochist "Masochist") trait or an ideoligion with the [Pain: Idealized](/wiki/Pain_\(precept\) "Pain \(precept\)") precept[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") get a mood _bonus_ from pain instead of a penalty, so it's usually better to leave them alone. 

Injuries to the [artificial parts](/wiki/Artificial_body_parts "Artificial body parts") do not cause any pain, so colonists with a lot of bionics will generally incur less pain during combat. 

## Contents

  * 1 Formula
  * 2 Thresholds
  * 3 Factors
    * 3.1 Base factors
    * 3.2 Offsets
  * 4 Version history



### Formula[[edit](/index.php?title=Pain&action=edit&section=1 "Edit section: Formula")]

Pain for a given pawn is the sum of the pain from each individual injury, with two extra steps at the end: 

  * `pain = pain / healthFactor` for pawns with a healthFactor other than 1.0 (like [grizzly bears](/wiki/Grizzly_bear "Grizzly bear") and other large animals). Humans have a healthFactor of 1.0, so this doesn't impact humans
  * `pain = pain * painFactor` from health conditions which alter pain. This includes pain-reducing drugs like [flake](/wiki/Flake "Flake") and [yayo](/wiki/Yayo "Yayo") as well as anesthetic used during operations



Pain from an individual injury is the product of the severity of the injury (the number of HP missing for things like cuts and burns) and the pain per severity for the injury type. For example: 

  * 30 burn damage causes 30 damage × 0.01875 pain per severity = 56.25% pain
  * 30 cut damage causes 30 damage × 0.0125 pain per severity = 37.5% pain



For the complete table of pain vs damage, see [Health Difficulties](/wiki/Health_Difficulties "Health Difficulties")

An exceptional kind of injury is scarification. They take the form of 0.5 HP scars, but give either 11% or 4% pain, for a pain factor of 0.08 or 0.22. 

### Thresholds[[edit](/index.php?title=Pain&action=edit&section=2 "Edit section: Thresholds")]

Pain creates moodlets of different values at 4 stages depending on pain severity. 

Level | Required Pain % | Mood Penalty  
(Default) | Mood Buff  
([Masochist](/wiki/Masochist "Masochist")) | Mood Buff  
([Pain:Idealized](/wiki/Pain_\(precept\) "Pain \(precept\)")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"))   
---|---|---|---|---  
Minor  | 1% | −5 | +5 | +3  
Serious  | 15% | −10 | +10 | +5  
Intense  | 40% | −15 | +15 | +7  
Mind-shattering  | 80% | −20 | +20 | +9  
  
A standard pawn will go down upon reaching mind-shattering pain.  
Pain inflicts a [consciousness](/wiki/Consciousness "Consciousness") penalty that scales with the pain percentage after exceeding 10%. It conforms to the following equation: `IF Pain[%] <= 10% THEN -0% ELSE -{(Pain-0.1)/2.25}[%]` For example, 15% pain is 0.15 - 0.1 = 0.05 / 2.25 = 0.02 or 2% consciousness loss. 

Graph   
---  
  
### Factors[[edit](/index.php?title=Pain&action=edit&section=3 "Edit section: Factors")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Pain&action=edit). Reason:** _Many other hediffs cause pain or change pain factors. Also injury mechanics. Also how is PainFactor applied? Is it exactly the same as a post factor for other capacities? Math section on final calculation is needed.._  
---|---  
  
#### Base factors[[edit](/index.php?title=Pain&action=edit&section=4 "Edit section: Base factors")]

Factors cause the game code to MULTIPLY pain X a number. Small numbers reduce pain a lot. Large numbers below 100% reduce pain a little. 

  * [Painstopper](/wiki/Painstopper "Painstopper"): **×0%**
  * [Painless](/wiki/Painless "Painless") persona trait [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC"): **×0%**
  * [Go-juice](/wiki/Go-juice "Go-juice"): 
    * High: **×10%**
    * Withdrawal: **×300%**
  * [Painblock](/wiki/Painblock "Painblock") psycast: [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") **×10%**
  * [Yayo](/wiki/Yayo "Yayo"): 
    * High: **×50%**
  * [Luciferium](/wiki/Luciferium "Luciferium"): 
    * High: **×80%**
  * [Psychite tea](/wiki/Psychite_tea "Psychite tea"): 
    * High: **×90%**
  * [Beer](/wiki/Beer "Beer"): (See also Offsets) 
    * Warm: **×90%**
    * Tipsy: **×80%**
    * Drunk: **×50%**
    * Hammered: **×30%**
    * Blackout: **×10%**
  * [Psychic bond](/wiki/Psychic_bonding "Psychic bonding")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"): 
    * Psychic bond: **×50%**
  * [Reduced pain](/wiki/Reduced_pain "Reduced pain")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"): **×50%**



#### Offsets[[edit](/index.php?title=Pain&action=edit&section=5 "Edit section: Offsets")]

Offsets cause the game code to ADD OR SUBTRACT a number from the pawn's pain. Small numbers are less effective at reducing pain than large numbers. However, if the pawn only has a small amount of pain, an equally small offset will be totally effective at removing all pain. Positive numbers add pain. Negative numbers reduce pain. 

  * [Mindscrew](/wiki/Mindscrew "Mindscrew"): +20%
  * [Sensory mechanites](/wiki/Sensory_mechanites "Sensory mechanites"): 
    * Mild pain: +20%
    * Intense pain: +60%
  * [Blood rot](/wiki/Blood_rot "Blood rot"): 
    * Extreme: +5%
  * [Fibrous mechanites](/wiki/Fibrous_mechanites "Fibrous mechanites"): 
    * Mild pain: +20%
    * Intense pain: +60%
  * [Muscle parasites](/wiki/Muscle_parasites "Muscle parasites"): +20%
  * [Gut worms](/wiki/Gut_worms "Gut worms"): +20%
  * [Malaria](/wiki/Malaria "Malaria"): 
    * Major: +30%
    * Extreme: +30%
  * [Luciferium](/wiki/Luciferium "Luciferium"): 
    * Withdrawal: +40%
  * [Beer](/wiki/Beer "Beer"): (See also Factors) 
    * Blackout: +5%
  * [Stoned on smokeleaf](/wiki/Smokeleaf_joint "Smokeleaf joint"): −20%
  * [Torture crown](/wiki/Torture_crown "Torture crown"):[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") +5%
  * [Tox gas](/wiki/Tox_gas "Tox gas"):[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
    * Mild: +10%
    * Moderate: +15%
    * Severe: +25%
  * [Hemogen](/wiki/Hemogen "Hemogen") craving:[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
    * Minor: +5%
    * Moderate: +10%
    * Major: +15%
  * [Inhumanization](/wiki/Inhumanized "Inhumanized"):[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") −50%



  


## Version history[[edit](/index.php?title=Pain&action=edit&section=6 "Edit section: Version history")]

  * [0.6.532](/wiki/Version/0.6.532 "Version/0.6.532") \- Added. Pain level is tracked. A character in too much pain will become incapacitated.
  * [0.10.785](/wiki/Version/0.10.785 "Version/0.10.785") \- Pain now creates unhappiness.



* * *

[Stats](/wiki/Stat "Stat")

[Capacities](/wiki/Capacity "Capacity")
    Pain • [Consciousness](/wiki/Consciousness "Consciousness") • [Moving](/wiki/Moving "Moving") • [Manipulation](/wiki/Manipulation "Manipulation") • [Talking](/wiki/Talking "Talking") • [Eating](/wiki/Eating "Eating") • [Sight](/wiki/Sight "Sight") • [Hearing](/wiki/Hearing "Hearing") • [Breathing](/wiki/Breathing "Breathing") • [Blood Filtration](/wiki/Blood_Filtration "Blood Filtration") • [Blood Pumping](/wiki/Blood_Pumping "Blood Pumping") • [Digestion](/wiki/Digestion "Digestion")

Basics | Important
    [Market Value](/wiki/Market_Value "Market Value") • [Market Value Ignoring Hitpoints](/wiki/Market_Value_Ignoring_Hitpoints "Market Value Ignoring Hitpoints") • [Honor Value](/wiki/Honor_Value "Honor Value") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

Non Pawn Important
    [Nutrition](/wiki/Nutrition_\(Stat\) "Nutrition \(Stat\)") • [Medical Potency](/wiki/Medical_Potency "Medical Potency") • [Medical Tend Quality Maximum](/wiki/Medical_Tend_Quality_Maximum "Medical Tend Quality Maximum") • [Max Hit Points](/wiki/Max_Hit_Points "Max Hit Points")

Basics
    [Mass](/wiki/Mass "Mass") • [Flammability](/wiki/Flammability "Flammability") • [Psychic Sensitivity Factor](/wiki/Psychic_Sensitivity_Factor "Psychic Sensitivity Factor") • [Psychic Sensitivity Offset](/wiki/Psychic_Sensitivity_Offset "Psychic Sensitivity Offset") • [Neural Heat Limit Offset](/wiki/Neural_Heat_Limit_Offset "Neural Heat Limit Offset") • [Neural Heat Recovery Rate Offset](/wiki/Neural_Heat_Recovery_Rate_Offset "Neural Heat Recovery Rate Offset") • [Slave Suppression Offset](/wiki/Slave_Suppression_Offset "Slave Suppression Offset") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Terror (Source)](/wiki/Terror_\(Source\) "Terror \(Source\)") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Max Install Count](/wiki/Max_Install_Count "Max Install Count") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

[Pawn](/wiki/Pawn "Pawn")
    [Recreation Fall Rate](/wiki/Recreation_Fall_Rate "Recreation Fall Rate") • [Sleep Fall Rate](/wiki/Sleep_Fall_Rate "Sleep Fall Rate") • [Eating Speed](/wiki/Eating_Speed "Eating Speed") • [Foraged Food Amount](/wiki/Foraged_Food_Amount "Foraged Food Amount") • [Minimum Handling Skill](/wiki/Minimum_Handling_Skill "Minimum Handling Skill") • [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") • [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") • [Pain Shock Threshold](/wiki/Pain_Shock_Threshold "Pain Shock Threshold") • [Lifespan Factor](/wiki/Lifespan_Factor "Lifespan Factor") • [Minimum Comfortable Temperature](/wiki/Minimum_Comfortable_Temperature "Minimum Comfortable Temperature") • [Maximum Comfortable Temperature](/wiki/Maximum_Comfortable_Temperature "Maximum Comfortable Temperature") • [Injury Healing Factor](/wiki/Injury_Healing_Factor "Injury Healing Factor") • [Caravan Riding Speed](/wiki/Caravan_Riding_Speed "Caravan Riding Speed") • [Carrying Capacity](/wiki/Carrying_Capacity "Carrying Capacity") • [Filth Rate](/wiki/Filth_Rate "Filth Rate") • [Crawl Speed](/wiki/Crawl_Speed "Crawl Speed") • [Move Speed](/wiki/Move_Speed "Move Speed") • [Max Nutrition](/wiki/Max_Nutrition "Max Nutrition") • [Rest Rate Multiplier](/wiki/Rest_Rate_Multiplier "Rest Rate Multiplier") • [Toxic Environment Resistance](/wiki/Toxic_Environment_Resistance "Toxic Environment Resistance") • [Toxic Resistance](/wiki/Toxic_Resistance "Toxic Resistance") • [Animals Learning Factor](/wiki/Animals_Learning_Factor "Animals Learning Factor") • [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") • [Neural Heat Limit](/wiki/Neural_Heat_Limit "Neural Heat Limit") • [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") • [Leather Amount](/wiki/Leather_Amount "Leather Amount") • [Meat Amount](/wiki/Meat_Amount "Meat Amount") • [Neural Heat Recovery Rate](/wiki/Neural_Heat_Recovery_Rate "Neural Heat Recovery Rate") • [Meditation Psyfocus Gain](/wiki/Meditation_Psyfocus_Gain "Meditation Psyfocus Gain") • [Neural Heat Gain (Factor)](/wiki/Neural_Heat_Gain_\(Factor\) "Neural Heat Gain \(Factor\)") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") • [Ideoligion Spread Chance](/wiki/Ideoligion_Spread_Chance "Ideoligion Spread Chance") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Terror](/wiki/Terror "Terror") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Raw Nutrition Multiplier](/wiki/Raw_Nutrition_Multiplier "Raw Nutrition Multiplier") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Learning Rate Factor](/wiki/Learning_Rate_Factor "Learning Rate Factor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Cancer Rate Factor](/wiki/Cancer_Rate_Factor "Cancer Rate Factor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Fertility](/wiki/Fertility "Fertility") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Hemogen Gain Multiplier](/wiki/Hemogen_Gain_Multiplier "Hemogen Gain Multiplier") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Vacuum Resistance](/wiki/Vacuum_Resistance "Vacuum Resistance") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

Non Pawn
    [Construction Speed (Material Factor)](/wiki/Construction_Speed_\(Material_Factor\) "Construction Speed \(Material Factor\)") • [Deterioration Rate](/wiki/Deterioration_Rate "Deterioration Rate") • [Sell Price Multiplier](/wiki/Sell_Price_Multiplier "Sell Price Multiplier") • [Beauty](/wiki/Beauty_\(Stat\) "Beauty \(Stat\)") • [Outdoor Beauty](/wiki/Outdoor_Beauty "Outdoor Beauty") • [Cleanliness](/wiki/Cleanliness_\(Stat\) "Cleanliness \(Stat\)") • [Comfort](/wiki/Comfort_\(Stat\) "Comfort \(Stat\)") • [Work To Make](/wiki/Work_To_Make "Work To Make") • [Food Poison Chance (Food Stat)](/wiki/Food_Poison_Chance_\(Food_Stat\) "Food Poison Chance \(Food Stat\)") • [Shooting Accuracy (Turrets)](/wiki/Shooting_Accuracy_\(Turrets\) "Shooting Accuracy \(Turrets\)") • [Style Dominance](/wiki/Style_Dominance "Style Dominance") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")

[Mechanoid](/wiki/Mechanoid "Mechanoid")
    [EMP Resistance](/wiki/EMP_Resistance "EMP Resistance") • [Bandwidth Cost](/wiki/Bandwidth_Cost "Bandwidth Cost") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Energy Usage Multiplier](/wiki/Energy_Usage_Multiplier "Energy Usage Multiplier") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Wastepacks Per Recharge](/wiki/Wastepacks_Per_Recharge "Wastepacks Per Recharge") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Control Taking Time](/wiki/Control_Taking_Time "Control Taking Time") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Repair Energy Cost](/wiki/Repair_Energy_Cost "Repair Energy Cost") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

[Meditation](/wiki/Meditation "Meditation")
    [Meditation Psyfocus Bonus](/wiki/Meditation_Psyfocus_Bonus "Meditation Psyfocus Bonus") • [Meditation Plant Growth Offset](/wiki/Meditation_Plant_Growth_Offset "Meditation Plant Growth Offset") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

[Terrain](/wiki/Terrain "Terrain")
    [Cleaning Time Multiplier](/wiki/Cleaning_Time_Multiplier "Cleaning Time Multiplier") • [Filth Multiplier](/wiki/Filth_Multiplier "Filth Multiplier")

[Apparel](/wiki/Apparel "Apparel")
    [Armor - Material Effect Multiplier](/wiki/Armor_-_Material_Effect_Multiplier "Armor - Material Effect Multiplier") • [Insulation - Cold - Material Effect Multiplier](/wiki/Insulation_-_Cold_-_Material_Effect_Multiplier "Insulation - Cold - Material Effect Multiplier") • [Insulation - Heat - Material Effect Multiplier](/wiki/Insulation_-_Heat_-_Material_Effect_Multiplier "Insulation - Heat - Material Effect Multiplier") • [Equip Delay](/wiki/Equip_Delay "Equip Delay") • [Pack Radius](/wiki/Pack_Radius "Pack Radius") • [Shield Recharge Rate](/wiki/Shield_Recharge_Rate "Shield Recharge Rate") • [Shield Max Energy](/wiki/Shield_Max_Energy "Shield Max Energy") • [Insulation - Heat](/wiki/Insulation_-_Heat "Insulation - Heat") • [Insulation - Cold](/wiki/Insulation_-_Cold "Insulation - Cold") • [Armor - Heat](/wiki/Armor_-_Heat "Armor - Heat") • [Armor - Blunt](/wiki/Armor_-_Blunt "Armor - Blunt") • [Armor - Sharp](/wiki/Armor_-_Sharp "Armor - Sharp") • [Jump Range](/wiki/Jump_Range "Jump Range") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")

[Weapon](/wiki/Weapon "Weapon") ([Ranged](/wiki/Ranged_weapons "Ranged weapons"))
    [Ranged Damage Multiplier](/wiki/Ranged_Damage_Multiplier "Ranged Damage Multiplier") • [Ranged Cooldown](/wiki/Ranged_Cooldown "Ranged Cooldown") • [Accuracy (Long)](/wiki/Accuracy_\(Long\) "Accuracy \(Long\)") • [Accuracy (Medium)](/wiki/Accuracy_\(Medium\) "Accuracy \(Medium\)") • [Accuracy (Short)](/wiki/Accuracy_\(Short\) "Accuracy \(Short\)") • [Accuracy (Close)](/wiki/Accuracy_\(Close\) "Accuracy \(Close\)")

[Weapon](/wiki/Weapon "Weapon") ([Melee](/wiki/Melee_weapons "Melee weapons"))
    [Melee Damage Multiplier](/wiki/Melee_Damage_Multiplier "Melee Damage Multiplier") • [Melee Weapon Average Armor Penetration](/wiki/Melee_Weapon_Average_Armor_Penetration "Melee Weapon Average Armor Penetration") • [Melee Damage Per Second](/wiki/Melee_Damage_Per_Second "Melee Damage Per Second")

[Building](/wiki/Building "Building")
    [Research Speed Factor](/wiki/Research_Speed_Factor "Research Speed Factor") • [Max Power Output](/wiki/Max_Power_Output "Max Power Output") • [Medical Tend Quality Offset](/wiki/Medical_Tend_Quality_Offset "Medical Tend Quality Offset") • [Work Speed Factor](/wiki/Work_Speed_Factor "Work Speed Factor") • [Work Efficiency Factor](/wiki/Work_Efficiency_Factor "Work Efficiency Factor") • [Work To Build](/wiki/Work_To_Build "Work To Build") • [Door Opening Speed](/wiki/Door_Opening_Speed "Door Opening Speed") • [Rest Effectiveness](/wiki/Rest_Effectiveness "Rest Effectiveness") • [Immunity Gain Speed Factor](/wiki/Immunity_Gain_Speed_Factor "Immunity Gain Speed Factor") • [Recreation Power](/wiki/Recreation_Power "Recreation Power") • [Surgery Success Chance Factor](/wiki/Surgery_Success_Chance_Factor "Surgery Success Chance Factor") • [Reading Bonus](/wiki/Reading_Bonus "Reading Bonus") • [Trap Spring Chance](/wiki/Trap_Spring_Chance "Trap Spring Chance") • [Trap Melee Damage](/wiki/Trap_Melee_Damage "Trap Melee Damage") • [Biosculpter Pod Speed Factor](/wiki/Biosculpter_Pod_Speed_Factor "Biosculpter Pod Speed Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Assembly Speed Factor](/wiki/Assembly_Speed_Factor "Assembly Speed Factor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Baby Play Power](/wiki/Baby_Play_Power "Baby Play Power") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Birth Quality Offset](/wiki/Birth_Quality_Offset "Birth Quality Offset") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Genetic Complexity Increase](/wiki/Genetic_Complexity_Increase "Genetic Complexity Increase") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Ability
    [Detection Chance](/wiki/Detection_Chance "Detection Chance") • [Goodwill Impact](/wiki/Goodwill_Impact "Goodwill Impact") • [Effect Radius](/wiki/Effect_Radius "Effect Radius") • [Duration](/wiki/Duration "Duration") • [Range](/wiki/Range_\(Ability\) "Range \(Ability\)") • [Psyfocus Cost](/wiki/Psyfocus_Cost "Psyfocus Cost") • [Neural Heat Gain](/wiki/Neural_Heat_Gain "Neural Heat Gain") • [Casting Time](/wiki/Casting_Time "Casting Time") • [Psylink Level](/wiki/Psylink_Level "Psylink Level")

[Stuff](/wiki/Stuff "Stuff") Stat Factors (Multipliers when made of this)
    [Melee Cooldown](/wiki/Melee_Cooldown "Melee Cooldown") • [Sharp Damage](/wiki/Sharp_Damage "Sharp Damage") • [Blunt Damage](/wiki/Blunt_Damage "Blunt Damage") • [Insulation - Heat (Material Factor)](/wiki/Insulation_-_Heat_\(Material_Factor\) "Insulation - Heat \(Material Factor\)") • [Insulation - Cold (Material Factor)](/wiki/Insulation_-_Cold_\(Material_Factor\) "Insulation - Cold \(Material Factor\)") • [Armor - Heat (Material Factor)](/wiki/Armor_-_Heat_\(Material_Factor\) "Armor - Heat \(Material Factor\)") • [Armor - Blunt (Material Factor)](/wiki/Armor_-_Blunt_\(Material_Factor\) "Armor - Blunt \(Material Factor\)") • [Armor - Sharp (Material Factor)](/wiki/Armor_-_Sharp_\(Material_Factor\) "Armor - Sharp \(Material Factor\)")

[Mechanitor](/wiki/Mechanitor "Mechanitor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")
    [Mech Bandwidth](/wiki/Mech_Bandwidth "Mech Bandwidth") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Control Groups](/wiki/Mech_Control_Groups "Mech Control Groups") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Gestation Speed](/wiki/Mech_Gestation_Speed "Mech Gestation Speed") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Remote Repair Distance](/wiki/Mech_Remote_Repair_Distance "Mech Remote Repair Distance") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Remote Shield Distance](/wiki/Mech_Remote_Shield_Distance "Mech Remote Shield Distance") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Remote Shield Energy](/wiki/Mech_Remote_Shield_Energy "Mech Remote Shield Energy") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Repair Speed](/wiki/Mech_Repair_Speed "Mech Repair Speed") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Subcore Encoding Speed](/wiki/Subcore_Encoding_Speed "Subcore Encoding Speed") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Mech Work Speed Offset](/wiki/Mech_Work_Speed_Offset "Mech Work Speed Offset") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

[Pawn](/wiki/Pawn "Pawn") | Combat
    [Stagger Time Multiplier](/wiki/Stagger_Time_Multiplier "Stagger Time Multiplier") • [Ranged Cooldown Multiplier](/wiki/Ranged_Cooldown_Multiplier "Ranged Cooldown Multiplier") • [Aiming Time](/wiki/Aiming_Time "Aiming Time") • [Pawn Trap Spring Chance](/wiki/Pawn_Trap_Spring_Chance "Pawn Trap Spring Chance") • [Incoming Damage Multiplier](/wiki/Incoming_Damage_Multiplier "Incoming Damage Multiplier") • [Accuracy Factor (Long)](/wiki/Accuracy_Factor_\(Long\) "Accuracy Factor \(Long\)") • [Accuracy Factor (Medium)](/wiki/Accuracy_Factor_\(Medium\) "Accuracy Factor \(Medium\)") • [Accuracy Factor (Short)](/wiki/Accuracy_Factor_\(Short\) "Accuracy Factor \(Short\)") • [Accuracy Factor (Close)](/wiki/Accuracy_Factor_\(Close\) "Accuracy Factor \(Close\)") • [Shooting Accuracy](/wiki/Shooting_Accuracy "Shooting Accuracy") ([Indoors Dark](/wiki/Shooting_Accuracy_Indoors_Dark "Shooting Accuracy Indoors Dark") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Indoors Lit](/wiki/Shooting_Accuracy_Indoors_Lit "Shooting Accuracy Indoors Lit") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Dark](/wiki/Shooting_Accuracy_Outdoors_Dark "Shooting Accuracy Outdoors Dark") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Lit](/wiki/Shooting_Accuracy_Outdoors_Lit "Shooting Accuracy Outdoors Lit") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")) • [Mortar Miss Radius Multiplier](/wiki/Mortar_Miss_Radius_Multiplier "Mortar Miss Radius Multiplier") • [Melee Armor Penetration](/wiki/Melee_Armor_Penetration "Melee Armor Penetration") • [Melee Dodge Chance](/wiki/Melee_Dodge_Chance "Melee Dodge Chance") ([Indoors Dark](/wiki/Melee_Dodge_Chance_Indoors_Dark "Melee Dodge Chance Indoors Dark") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Indoors Lit](/wiki/Melee_Dodge_Chance_Indoors_Lit "Melee Dodge Chance Indoors Lit") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Night](/wiki/Melee_Dodge_Chance_Outdoors_Night "Melee Dodge Chance Outdoors Night") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Day](/wiki/Melee_Dodge_Chance_Outdoors_Day "Melee Dodge Chance Outdoors Day") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")) • [Melee Hit Chance](/wiki/Melee_Hit_Chance "Melee Hit Chance") ([Indoors Dark](/wiki/Melee_Hit_Chance_Indoors_Dark "Melee Hit Chance Indoors Dark") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Indoors Lit](/wiki/Melee_Hit_Chance_Indoors_Lit "Melee Hit Chance Indoors Lit") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Dark](/wiki/Melee_Hit_Chance_Outdoors_Dark "Melee Hit Chance Outdoors Dark") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Outdoors Lit](/wiki/Melee_Hit_Chance_Outdoors_Lit "Melee Hit Chance Outdoors Lit") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")) • [Melee DPS](/wiki/Melee_DPS "Melee DPS") • [Melee Damage Factor](/wiki/Melee_Damage_Factor "Melee Damage Factor") • [Melee Cooldown](/wiki/Melee_Cooldown_\(Pawn\) "Melee Cooldown \(Pawn\)") • [Melee Door Damage Factor](/wiki/Melee_Door_Damage_Factor "Melee Door Damage Factor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Shooting Accuracy Multiplier (Child)](/wiki/Shooting_Accuracy_Multiplier_\(Child\) "Shooting Accuracy Multiplier \(Child\)") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Social
    [Bond Chance Factor](/wiki/Bond_Chance_Factor "Bond Chance Factor") • [Train Animal Chance](/wiki/Train_Animal_Chance "Train Animal Chance") • [Tame Animal Chance](/wiki/Tame_Animal_Chance "Tame Animal Chance") • [Arrest Success Chance](/wiki/Arrest_Success_Chance "Arrest Success Chance") • [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)") • [Social Impact](/wiki/Social_Impact "Social Impact") • [Drug Sell Price Improvement](/wiki/Drug_Sell_Price_Improvement "Drug Sell Price Improvement") • [Trade Price Improvement](/wiki/Trade_Price_Improvement "Trade Price Improvement") • [Negotiation Ability](/wiki/Negotiation_Ability "Negotiation Ability") • [Suppression Power](/wiki/Suppression_Power "Suppression Power") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Conversion Power](/wiki/Conversion_Power "Conversion Power") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Slave Suppression Fall Rate](/wiki/Slave_Suppression_Fall_Rate "Slave Suppression Fall Rate") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Animal Products Price Improvement](/wiki/Animal_Products_Price_Improvement "Animal Products Price Improvement") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")

Misc
    [Biosculpter Occupant Speed](/wiki/Biosculpter_Occupant_Speed "Biosculpter Occupant Speed") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Growth Vat Occupant Speed](/wiki/Growth_Vat_Occupant_Speed "Growth Vat Occupant Speed") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

Work
    [Cleaning Speed Multiplier](/wiki/Cleaning_Speed_Multiplier "Cleaning Speed Multiplier") • [Butchery Speed](/wiki/Butchery_Speed "Butchery Speed") • [Mechanoid Shredding Speed](/wiki/Mechanoid_Shredding_Speed "Mechanoid Shredding Speed") • [Hunting Stealth](/wiki/Hunting_Stealth "Hunting Stealth") • [Research Speed](/wiki/Research_Speed "Research Speed") • [Smelting Speed](/wiki/Smelting_Speed "Smelting Speed") • [Smoothing Speed](/wiki/Smoothing_Speed "Smoothing Speed") • [Animal Gather Speed](/wiki/Animal_Gather_Speed "Animal Gather Speed") • [Animal Gather Yield](/wiki/Animal_Gather_Yield "Animal Gather Yield") • [Hacking Speed](/wiki/Hacking_Speed "Hacking Speed") • [Drug Cooking Speed](/wiki/Drug_Cooking_Speed "Drug Cooking Speed") • [Drug Synthesis Speed](/wiki/Drug_Synthesis_Speed "Drug Synthesis Speed") • [Butchery Efficiency](/wiki/Butchery_Efficiency "Butchery Efficiency") • [Mechanoid Shredding Efficiency](/wiki/Mechanoid_Shredding_Efficiency "Mechanoid Shredding Efficiency") • [Cooking Speed](/wiki/Cooking_Speed "Cooking Speed") • [Food Poison Chance](/wiki/Food_Poison_Chance "Food Poison Chance") • [Plant Work Speed](/wiki/Plant_Work_Speed "Plant Work Speed") • [Plant Harvest Yield](/wiki/Plant_Harvest_Yield "Plant Harvest Yield") • [Drug Crop Harvest Yield](/wiki/Drug_Crop_Harvest_Yield "Drug Crop Harvest Yield") • [Reading Speed](/wiki/Reading_Speed "Reading Speed") • [Repair Success Chance](/wiki/Repair_Success_Chance "Repair Success Chance") • [Construct Success Chance](/wiki/Construct_Success_Chance "Construct Success Chance") • [Construction Speed](/wiki/Construction_Speed "Construction Speed") • [Medical Tend Speed](/wiki/Medical_Tend_Speed "Medical Tend Speed") • [Medical Tend Quality](/wiki/Medical_Tend_Quality "Medical Tend Quality") • [Medical Operation Speed](/wiki/Medical_Operation_Speed "Medical Operation Speed") • [Medical Surgery Success Chance](/wiki/Medical_Surgery_Success_Chance "Medical Surgery Success Chance") • [Mining Speed](/wiki/Mining_Speed "Mining Speed") • [Deep Drilling Speed](/wiki/Deep_Drilling_Speed "Deep Drilling Speed") • [Mining Yield](/wiki/Mining_Yield "Mining Yield") • [General Labor Speed](/wiki/General_Labor_Speed "General Labor Speed") • [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") • [Pruning Speed](/wiki/Pruning_Speed "Pruning Speed") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Activity Suppression Speed](/wiki/Activity_Suppression_Speed "Activity Suppression Speed") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Study Efficiency](/wiki/Study_Efficiency "Study Efficiency") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Entity Study Rate](/wiki/Entity_Study_Rate "Entity Study Rate") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Fishing Speed](/wiki/Fishing_Speed "Fishing Speed") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Fishing Yield](/wiki/Fishing_Yield "Fishing Yield") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Piloting Ability](/wiki/Piloting_Ability "Piloting Ability") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Psychic Ritual](/wiki/Psychic_rituals "Psychic rituals") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")
    [Psychic Ritual Quality](/wiki/Psychic_Ritual_Quality "Psychic Ritual Quality") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Psychic Ritual Quality Offset](/wiki/Psychic_Ritual_Quality_Offset "Psychic Ritual Quality Offset") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

[Containment](/wiki/Containment "Containment") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")
    [Cold Containment Bonus](/wiki/Cold_Containment_Bonus "Cold Containment Bonus") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Containment Strength](/wiki/Containment_Strength "Containment Strength") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") • [Minimum Containment Strength](/wiki/Minimum_Containment_Strength "Minimum Containment Strength") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")

Hidden
    [Bed Hunger Rate Multiplier](/wiki/Bed_Hunger_Rate_Multiplier "Bed Hunger Rate Multiplier")
  


  


Retrieved from "[https://rimworldwiki.com/index.php?title=Pain&oldid=183459](https://rimworldwiki.com/index.php?title=Pain&oldid=183459)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Capacity](/wiki/Category:Capacity "Category:Capacity")



Hidden categories: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")
  * [Pages with graphs](/wiki/Category:Pages_with_graphs "Category:Pages with graphs")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Pain "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Pain "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Pain "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Pain&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Pain)
  * [Edit](/index.php?title=Pain&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Pain&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Pain "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Pain "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Pain&oldid=183459 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Pain&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Pain)



  * This page was last edited on 23 August 2026, at 00:00.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,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)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (179,192,186)
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
