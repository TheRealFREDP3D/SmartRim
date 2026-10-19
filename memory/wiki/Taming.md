# Animal husbandry

From RimWorld Wiki

(Redirected from [Taming](/index.php?title=Taming&redirect=no "Taming"))

Jump to navigation Jump to search

For a more general overview, see [Animals](/wiki/Animals "Animals").

All [animals](/wiki/Animals "Animals") in Rimworld can be tamed, providing certain benefits to the colony. Some animals can be trained, others require enclosed spaces ([pen](/wiki/Pen "Pen")) to remain in the colony, and yet others can lose their tame state if left alone for too long. 

Any animal that requires a [pen](/wiki/Pen "Pen") to remain on the colony is considered a farm animal and can't be trained[1]. Farm animals don't lose tameness due to wildness. 

## Contents

  * 1 Acquisition
    * 1.1 Taming
      * 1.1.1 Tame chances
      * 1.1.2 Minimum skill
    * 1.2 Starting pets
    * 1.3 Buying
    * 1.4 Events
  * 2 Interactions
    * 2.1 Naming
    * 2.2 Nuzzling
    * 2.3 Bonding
    * 2.4 Training
    * 2.5 Combat
    * 2.6 Slaughtering
      * 2.6.1 Auto-Slaughter
    * 2.7 Other Interactions
      * 2.7.1 Caravans
      * 2.7.2 Release to Wild
      * 2.7.3 Social
      * 2.7.4 Trade goods
  * 3 Products
    * 3.1 Eggs
    * 3.2 Milk
    * 3.3 Wool
    * 3.4 Chemfuel
  * 4 Feeding
    * 4.1 Grazing wild plants
    * 4.2 Growing haygrass
    * 4.3 Making kibble
    * 4.4 Corpse freezer
  * 5 Raising
    * 5.1 Pens
    * 5.2 Pet care
  * 6 Butchering
  * 7 Notes
  * 8 Version history



## Acquisition[[edit](/index.php?title=Animal_husbandry&action=edit&section=1 "Edit section: Acquisition")]

There are five options to obtain tamed animals. Having them as starting pets, taming wild animals, buying them from traders, having them birth offspring, and getting them from events. 

### Taming[[edit](/index.php?title=Animal_husbandry&action=edit&section=2 "Edit section: Taming")]

Wild animals can be tamed by an [animal handler](/wiki/Work#Handle "Work") with sufficient Animal skill and available food. Tamed animals may be bred, trained, traded, slaughtered, or farmed. 

![TameButton.png](/images/thumb/5/5f/TameButton.png/64px-TameButton.png)

Wild animals may be marked for taming using the Tame order. 

An [animal handler](/wiki/Work#Handle "Work") will attempt to tame marked animals using non-meal, non-drug food fitting that animal's diet. The chance to tame an animal depends on the animal's wildness (displayed on the info window) and the handler's 'Tame animal chance' stat. This stat is determined by the colonist's [animals skill](/wiki/Skills#Animals "Skills"), [manipulation](/wiki/Health#Manipulation "Health"), [talking](/wiki/Health#Talking "Health"), and [hearing](/wiki/Health#Hearing "Health"). When a handler fails to tame an animal there is a cooldown period of 30,000 [ticks](/wiki/Time "Time") (8.33 mins), or 12 in-game [hours](/wiki/Time "Time"), before another attempt can be made. There is also a chance it will turn [manhunter](/wiki/Manhunter "Manhunter") and start attacking the handler and others. The revenge chance is shown on the [Wildlife](/wiki/Menu#Wildlife "Menu") menu. After a while the handler may drop unused food. 

Tamed animals will wander around the map until they are lead to a pen with a [pen marker](/wiki/Pen_marker "Pen marker"), for pen animals, or restricted to a designated [area](/wiki/Area "Area"), for all other animals. Restricting non-pen animal movement using areas is usually necessary to prevent unwanted food consumption and animal [filth](/wiki/Filth "Filth"). 

#### Tame chances[[edit](/index.php?title=Animal_husbandry&action=edit&section=3 "Edit section: Tame chances")]

For the calculation details, see [Tame Animal Chance](/wiki/Tame_Animal_Chance "Tame Animal Chance").

Besides the animal handler's own skill, the wildness of the animals also counts. 

Tame chances undergo a post-processing curve. 

  * An animal with 0% wildness has a x2 taming chance.
  * An animal with 50% wildness has normal taming chance.
  * An animal with 100% wildness cannot be tamed at all.



The net effect of the curve above is the expression `2*(1-wildness)`. The minimum value it can take is **0** at 100% wildness while the max is **2**(duplicates chance) at 0% wildness. 

Currently, the hardest to tame animal is the [alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo").[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") Assuming 20 [Animal skill](/wiki/Skill#Animal_skill "Skill"), the base taming chance is 1.28%. 

[Animals](/wiki/List_of_animals "List of animals") with 0% wildness remain tame forever. If wildness is above 0% (shown on the wildlife tab), the animals requires maintenance to not revert into its wild state. Farm animals will remain tamed regardless of wildness. 

#### Minimum skill[[edit](/index.php?title=Animal_husbandry&action=edit&section=4 "Edit section: Minimum skill")]

For the calculation details, see [Minimum Handling Skill](/wiki/Minimum_Handling_Skill "Minimum Handling Skill").

Most animal species have a **Minimum handling skill** stat which determines the Animal [skill](/wiki/Skill "Skill") necessary of a handler pawn. The game will briefly produce a warning message if no colonist has enough skill to handle the animal. 

Any animal with 0% wildness can be handled even with 0 skill. This list includes but is not limited to: [Cat](/wiki/Cat "Cat"), [Chicken](/wiki/Chicken "Chicken"), [Cow](/wiki/Cow "Cow"), [Donkey](/wiki/Donkey "Donkey"), [Duck](/wiki/Duck "Duck"), [Goat](/wiki/Goat "Goat"), [Husky](/wiki/Husky "Husky"), [Labrador retriever](/wiki/Labrador_retriever "Labrador retriever"), [Pig](/wiki/Pig "Pig"), [Sheep](/wiki/Sheep "Sheep"), [Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier"), [Barkskin dryad](/wiki/Barkskin_dryad "Barkskin dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Berrymaker dryad](/wiki/Berrymaker_dryad "Berrymaker dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Carrier dryad](/wiki/Carrier_dryad "Carrier dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Clawer dryad](/wiki/Clawer_dryad "Clawer dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Gaumaker dryad](/wiki/Gaumaker_dryad "Gaumaker dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Immature dryad](/wiki/Immature_dryad "Immature dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Medicinemaker dryad](/wiki/Medicinemaker_dryad "Medicinemaker dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"), [Woodmaker dryad](/wiki/Woodmaker_dryad "Woodmaker dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC"). 

The highest minimum skill required by any animal in Core is 10, which is required by both the [Megasloth](/wiki/Megasloth "Megasloth") (97% wildness) and [Thrumbo](/wiki/Thrumbo "Thrumbo") (98.5% wildness). This increases to 14 with the [DLC](/wiki/DLC "DLC") enabled, such as the [alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo").[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

### Starting pets[[edit](/index.php?title=Animal_husbandry&action=edit&section=5 "Edit section: Starting pets")]

For most [scenarios](/wiki/Scenario_system "Scenario system"), new colonies will include a random pet that is already tamed. These pets will have a random name and are sometimes bonded with a pawn. The animals available are determined by the handling skills of the starting pawn(s), as the game will not provide a pet that cannot be handled by the colony. This rule is broken when all colonists have animal handling disabled, as the game will still provide animals that require periodic taming. 

The chance of getting an animal is influenced by the "petness" stat, with a higher value resulting in a higher chance. The selection of animals also influences the chances, for example a Husky has a 21.74% chance of being selected with the highest handling skill at 0, while at level 10+ the chance is only 11.06% (assuming all DLCs are active). Hares, snowhares, capybaras and cobras are all under 1% chance due to the petness being so low and the animal handling being so high. 

* Animal  | Handling skill  
required  | Petness  | Chance with max handling skill:   
---|---|---|---  
0 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | Max   
[Arctic fox](/wiki/Arctic_fox "Arctic fox") | 8  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | 1.14 %  | 1.12 %  | 1.11 %   
[Arctic wolf](/wiki/Arctic_wolf "Arctic wolf") | 9  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | \-  | 1.12 %  | 1.11 %   
[Boomrat](/wiki/Boomrat "Boomrat") | 8  | 0.2  | \-  | \-  | \-  | \-  | \-  | \-  | 2.29 %  | 2.24 %  | 2.21 %   
[Capybara](/wiki/Capybara "Capybara") | 8  | 0.08  | \-  | \-  | \-  | \-  | \-  | \-  | 0.92 %  | 0.89 %  | 0.88 %   
[Cat](/wiki/Cat "Cat") | 0  | 1  | 21.74 %  | 19.61 %  | 17.54 %  | 17.39 %  | 15.75 %  | 12.74 %  | 11.44 %  | 11.19 %  | 11.06 %   
[Chinchilla](/wiki/Chinchilla "Chinchilla") | 6  | 0.2  | \-  | \-  | \-  | \-  | \-  | 2.55 %  | 2.29 %  | 2.24 %  | 2.21 %   
[Cobra](/wiki/Cobra "Cobra") | 8  | 0.05  | \-  | \-  | \-  | \-  | \-  | \-  | 0.57 %  | 0.56 %  | 0.55 %   
[Donkey](/wiki/Donkey "Donkey") | 0  | 0.6  | 13.04 %  | 11.76 %  | 10.53 %  | 10.43 %  | 9.45 %  | 7.64 %  | 6.86 %  | 6.71 %  | 6.64 %   
[Fennec fox](/wiki/Fennec_fox "Fennec fox") | 8  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | 1.14 %  | 1.12 %  | 1.11 %   
[Guinea pig](/wiki/Guinea_pig "Guinea pig") | 6  | 0.3  | \-  | \-  | \-  | \-  | \-  | 3.82 %  | 3.43 %  | 3.36 %  | 3.32 %   
[Hare](/wiki/Hare "Hare") | 8  | 0.08  | \-  | \-  | \-  | \-  | \-  | \-  | 0.92 %  | 0.89 %  | 0.88 %   
[Horse](/wiki/Horse "Horse") | 3  | 0.6  | \-  | \-  | 10.53 %  | 10.43 %  | 9.45 %  | 7.64 %  | 6.86 %  | 6.71 %  | 6.64 %   
[Husky](/wiki/Husky "Husky") | 0  | 1  | 21.74 %  | 19.61 %  | 17.54 %  | 17.39 %  | 15.75 %  | 12.74 %  | 11.44 %  | 11.19 %  | 11.06 %   
[Iguana](/wiki/Iguana "Iguana") | 5  | 0.15  | \-  | \-  | \-  | \-  | 2.36 %  | 1.91 %  | 1.72 %  | 1.68 %  | 1.66 %   
[Labrador retriever](/wiki/Labrador_retriever "Labrador retriever") | 0  | 1  | 21.74 %  | 19.61 %  | 17.54 %  | 17.39 %  | 15.75 %  | 12.74 %  | 11.44 %  | 11.19 %  | 11.06 %   
[Monkey](/wiki/Monkey "Monkey") | 6  | 0.5  | \-  | \-  | \-  | \-  | \-  | 6.37 %  | 5.72 %  | 5.59 %  | 5.53 %   
[Rat](/wiki/Rat "Rat") | 5  | 0.15  | \-  | \-  | \-  | \-  | 2.36 %  | 1.91 %  | 1.72 %  | 1.68 %  | 1.66 %   
[Red fox](/wiki/Red_fox "Red fox") | 8  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | 1.14 %  | 1.12 %  | 1.11 %   
[Snowhare](/wiki/Snowhare "Snowhare") | 8  | 0.08  | \-  | \-  | \-  | \-  | \-  | \-  | 0.92 %  | 0.89 %  | 0.88 %   
[Timber wolf](/wiki/Timber_wolf "Timber wolf") | 9  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | \-  | 1.12 %  | 1.11 %   
[Warg](/wiki/Warg "Warg") | 6  | 0.5  | \-  | \-  | \-  | \-  | \-  | 6.37 %  | 5.72 %  | 5.59 %  | 5.53 %   
[Yak](/wiki/Yak "Yak") | 2  | 0.3  | \-  | 5.88 %  | 5.26 %  | 5.22 %  | 4.72 %  | 3.82 %  | 3.43 %  | 3.36 %  | 3.32 %   
[Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier") | 0  | 1  | 21.74 %  | 19.61 %  | 17.54 %  | 17.39 %  | 15.75 %  | 12.74 %  | 11.44 %  | 11.19 %  | 11.06 %   
[Waste rat](/wiki/Waste_rat "Waste rat")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | 5  | 0.15  | \-  | \-  | \-  | \-  | 2.36 %  | 1.91 %  | 1.72 %  | 1.68 %  | 1.66 %   
[Bullfrog](/wiki/Bullfrog "Bullfrog")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 8  | 0.05  | \-  | \-  | \-  | \-  | \-  | \-  | 0.57 %  | 0.56 %  | 0.55 %   
[Greatwolf](/wiki/Greatwolf "Greatwolf")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 10  | 0.1  | \-  | \-  | \-  | \-  | \-  | \-  | \-  | \-  | 1.11 %   
[Macaw](/wiki/Macaw "Macaw")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 2  | 0.2  | \-  | 3.92 %  | 3.51 %  | 3.48 %  | 3.15 %  | 2.55 %  | 2.29 %  | 2.24 %  | 2.21 %   
[Megavole](/wiki/Megavole "Megavole")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 4  | 0.05  | \-  | \-  | \-  | 0.87 %  | 0.79 %  | 0.64 %  | 0.57 %  | 0.56 %  | 0.55 %   
[Monitor lizard](/wiki/Monitor_lizard "Monitor lizard")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 5  | 0.15  | \-  | \-  | \-  | \-  | 2.36 %  | 1.91 %  | 1.72 %  | 1.68 %  | 1.66 %   
[Scimitar cat](/wiki/Scimitar_cat "Scimitar cat")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 8  | 0.05  | \-  | \-  | \-  | \-  | \-  | \-  | 0.57 %  | 0.56 %  | 0.55 %   
  
### Buying[[edit](/index.php?title=Animal_husbandry&action=edit&section=6 "Edit section: Buying")]

Main article: [Trade](/wiki/Trade "Trade")

Animals bought from [traders](/wiki/Trader "Trader") are always tamed. Different types of traders have different kinds of animals in stock. 

### Events[[edit](/index.php?title=Animal_husbandry&action=edit&section=7 "Edit section: Events")]

Main article: [Events](/wiki/Events "Events")

The events [animals join](/wiki/Events#Animal_self-tamed "Events") and [animal self-tamed](/wiki/Animal_self-tamed "Animal self-tamed") give your colony tamed animals. 

## Interactions[[edit](/index.php?title=Animal_husbandry&action=edit&section=8 "Edit section: Interactions")]

Some animal species can be trained by colonists. With Guard trained, they will follow their master around if designated to do so. 

Some species may be harvested to produce [milk](/wiki/Milk "Milk"), [chemfuel](/wiki/Chemfuel "Chemfuel"), or [wool](/wiki/Wool "Wool"). Still others passively lay frequent eggs. 

When injured, they will go to animal sleeping spots/ beds for rest and treatment. 

### Naming[[edit](/index.php?title=Animal_husbandry&action=edit&section=9 "Edit section: Naming")]

Newly tamed or purchased animals are distinguished by numerical designations(“Muffalo 1”, “Muffalo 2”, etc.). When an animal forms a bond with a colonist, it is given a unique name. Names can be changed by the player from the "Training" tab in the inspect pawn pane. Names of tamed animals are not shown on the map unless the option is turned on, via Menu, Options, 'Show animal names'. 

Animals may have a gender-specific name (i.e. hen, rooster, buck, doe), or a lifestage-specific name (piglet, puppy), or even a gender/lifestage-specific name (cockerel). 

It is possible for animals which have been lost or sold to reappear later as part of a wild herd. This will only happen with animals which occur naturally on your colony's biome. They will still have the name you gave them (including automatic names like "Muffalo 2"), but will need to be tamed and trained again. 

### Nuzzling[[edit](/index.php?title=Animal_husbandry&action=edit&section=10 "Edit section: Nuzzling")]

Occasionally, some animals can nuzzle colonists, giving the colonist +4 _Nuzzled_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") or +6 _Nuzzled_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") [test]. Animals can nuzzle anyone regardless of handling skill unless they are a [psychopath](/wiki/Psychopath "Psychopath") or [inhumanized](/wiki/Inhumanized "Inhumanized") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC"). 

The following animals can nuzzle: 

* Animal | Nuzzle MTB in hours   
---|---  
[Cat](/wiki/Cat "Cat") | 12   
[Guinea pig](/wiki/Guinea_pig "Guinea pig") | 24   
[Husky](/wiki/Husky "Husky") | 12   
[Labrador retriever](/wiki/Labrador_retriever "Labrador retriever") | 12   
[Monkey](/wiki/Monkey "Monkey") | 24   
[Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier") | 12   
[Bog hound](/wiki/Bog_hound "Bog hound")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 72   
[Megavole](/wiki/Megavole "Megavole")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 72   
[Panda](/wiki/Panda "Panda")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 48   
[Seal](/wiki/Seal "Seal")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | 24   
  
### Bonding[[edit](/index.php?title=Animal_husbandry&action=edit&section=11 "Edit section: Bonding")]

Animals may **bond** with their handlers or doctors, and starting pets have a chance to start the game bonded with a random starting colonist. A bond gives the following [mood](/wiki/Mood "Mood") effects to non-[psychopathic](/wiki/Psychopath "Psychopath") or [inhumanized](/wiki/Inhumanized "Inhumanized")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") pawns. All moodlets stack with each other. 

  * +5 _Bonded animal'smaster_ [thought](/wiki/Thought "Thought")
  * −3 _Not bonded animal's master_ [thought](/wiki/Thought "Thought")
  * −10 _Bonded animal given away_ [thought](/wiki/Thought "Thought") for 60 [days](/wiki/Time "Time"). This will also inflict −10 [opinion](/wiki/Opinion "Opinion") of the pawns that performed the action for 60 days.
  * −8 _Bonded animal died_ [thought](/wiki/Thought "Thought") for 20 [days](/wiki/Time "Time"). This will also inflict −10 [opinion](/wiki/Opinion "Opinion") of the pawns that performed the action for 60 days.
  * −8 _Bonded animal lost_ [thought](/wiki/Thought "Thought") for 20 [days](/wiki/Time "Time")
  * −6 _Bonded animal banished_ [thought](/wiki/Thought "Thought") for 6 [days](/wiki/Time "Time")
  * −5 _Bonded animal released_ [thought](/wiki/Thought "Thought") for 15 [days](/wiki/Time "Time")



Bonds can occur when: 

  * When an animal has its wounds tended by a colonist, there is a constant 0.4% chance that the animal will bond with the colonist, regardless of Animals skill. If the animal is wild, the animal will instantly self-tame, disregarding wildness.
  * When tamed, an animal also has a 1% chance to bond with the tamer.
  * When successfully trained, an animal has a 0.7% chance to bond with the trainer.
  * Every 2,500 [ticks](/wiki/Time "Time") (41.67 secs), if an animal is within 12 tiles and has line of sight to their master, there is a 0.1% chance to bond.
  * For starting animals, the % to start bonded with an owner appears to be related to the innate [wildness](/wiki/Property:Wildness "Property:Wildness") (i.e. horses and camels will start bonded more often than cobras or wargs). Domestic animals (wildness 0 - dogs, cats, some farm animals) will always start bonded.



Pawns with the [Animal connection: Strong](/wiki/Ideoligion#Animal_connection "Ideoligion") precept in their [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") have a ×2 [multiplier on bonding chance](/wiki/Bond_Chance_Factor "Bond Chance Factor"). Pawns with the [Bonding: Disapproved](/wiki/Ideoligion#Bonding "Ideoligion") precept in their [ideoligion](/wiki/Ideoligion "Ideoligion")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") cannot be bonded with, but they will not lose existing bonds, nor their mood effects, if the precept is added via a fluid ideoligion's reformation. Pawns converted into a non-bonding ideoligion will renounce all their bonds at the moment of conversion. 

Bonded animals are also easier for their master to train (5x multiplier on chance). Animals are given a unique name upon bonding. 

On the death of the pawn an animal is bonded with, it can go into one of two animal mental breaks; [manhunter](/wiki/Manhunter "Manhunter"), in which it will attack all nearby entities, or [confusion](/wiki/Confusion "Confusion"), in which it will wander around, uncontrollably, similar to dazed humans. 

### Training[[edit](/index.php?title=Animal_husbandry&action=edit&section=12 "Edit section: Training")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Animal_husbandry&action=edit). Reason:** _Odyssey training effects._  
---|---  
  
Tamed animals may be trained depending on their trainable intelligence. Click the animal's training tab to specify training targets and view progress. 

The stats of the training pawn, including Animals skill or [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed"), have no effect on how fast each training session is completed. Instead, increased skill improves a pawn's [Train Animal Chance](/wiki/Train_Animal_Chance "Train Animal Chance"), resulting in the animal requiring fewer training attempts in the first place. After a training attempt on a tamed animal, there is a 6 in-game hour waiting period before that same animal can be trained again. 

Once Guard is trained, they can be assigned a master which they will follow. You can configure when the animal will follow their master, by toggling whether or not the animal will follow while doing field work (hunting/taming), or while drafted, from the Animals menu. 

Many skills require multiple steps to fully train. Guard has three steps, rescue and attack have two, and haul has seven. An animal also has five stages of tameness to maintain. 

Animal skills decay over time. The speed of decay ranges from 720,000 [ticks](/wiki/Time "Time") (12 in-game days) at 0% [wildness](/wiki/Wildness "Wildness") to 360,000 [ticks](/wiki/Time "Time") (6 in-game days) at 100% wildness. Any animal with over 10.1% [wildness](/wiki/Wildness "Wildness") can additionally lose the tamed status unless it is a [pen animal](/wiki/Pen_animal "Pen animal"). For this reason, if you do not have handlers meeting the animal's minimum handling skill, it is best to sell or slaughter before your animal returns to the wild. 

When an animal skill decays, one point of training is subtracted from one of the 'outermost' skills at random, ie: skills with no trained dependents. 'Guard' will always remain trained until all its dependent skills have fully decayed, and only after Guard is decayed can an animal lose tameness. 

**Orders Table** Orders | Training   
intelligence  
required | Steps | Description   
---|---|---|---  
Guard | ![Obedience.png](/images/6/6b/Obedience.png) | Simple | 3 | An animal trained in guard will follow its master and attack nearby aggressors. An animal's master is listed on the Training tab and on the Animals menu. Multiple animals may be assigned to a single master.   
Note that assigning an animal to the pawn it is bonded with will give that pawn a permanent +5 moodlet, and if a bonded animal is _not_ assigned to its bonded pawn, that pawn gets a permanent −3 moodlet. Mood effects stack with multiple bonded animals, and one pawn can have both the positive and negative moodlets from two bonded animals   
Attack | ![Release.png](/images/1/18/Release.png) | Intermediate | 5 | Using the 'attack' command, animals may leave their master's immediate area to attack enemies. When the 'Animals Attack' command is turned off, animals will guard their master and only attack enemies nearby.   
Rescue | ![Rescue.png](/images/3/30/Rescue.png) | Advanced | 2 | Animals trained in rescue will rescue its master as well as nearby colonists in a radius of 75. Only species of sufficient size can rescue.   
Haul | ![Haul animal.png](/images/7/79/Haul_animal.png) | Advanced | 7 | Animals trained in hauling will [haul](/wiki/Haul "Haul") just as colonists do, although each species has a specific carrying capacity according to its size. Only species of sufficient size can haul, but this requirement is lesser than for rescuing.   
Animals will perform hauling intermittently with an MTB of 1.5 hours. Apart from being able to move, animals also need an intact jaw in order to haul. Animals will only haul within their allowed area if they are assigned to one.  | Animal | Move Speed | Carrying Capacity | Haul Throughput | Wildness | Hunger Rate | Filth Rate | Juvenile Age | Maturity Age | Min Temperature | Max Temperature  
---|---|---|---|---|---|---|---|---|---|---  
[Alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo") | 6  | 375  | 2250  | 99%  | 2.8  | 8  | 45  | 79.92  | -65  | 50   
[Arctic wolf](/wiki/Arctic_wolf "Arctic wolf") | 5  | 64  | 320  | 85%  | 0.29  | 2  | 12  | 30  | -55  | 40   
[Carrier dryad](/wiki/Carrier_dryad "Carrier dryad") | 2.4  | 50  | 120  | 0%  | \-  | 1  | \-  | \-  | -50  | 50   
[Cougar](/wiki/Cougar "Cougar") | 5  | 75  | 375  | 80%  | 0.32  | 2  | 15  | 30  | -25  | 40   
[Elephant](/wiki/Elephant "Elephant") | 4.8  | 300  | 1440  | 75%  | 2.57  | 24  | 18  | 39.96  | -12  | 50   
[Gorilla](/wiki/Gorilla "Gorilla") | 4.7  | 150  | 705  | 60%  | 0.86  | 4  | 12  | 15.96  | -10  | 50   
[Greatwolf](/wiki/Greatwolf "Greatwolf") | 5.5  | 112  | 616  | 95%  | 0.64  | 2  | 12  | 30  | -50  | 40   
[Grizzly bear](/wiki/Grizzly_bear "Grizzly bear") | 4.6  | 161  | 740.6  | 80%  | 0.56  | 4  | 12  | 30  | -40  | 40   
[Hive queen](/wiki/Hive_queen "Hive queen") | 3.4  | 337  | 1145.8  | 99%  | \-  | 28  | \-  | \-  | -40  | 40   
[Husky](/wiki/Husky "Husky") | 5  | 64  | 320  | 0%  | 0.8  | 1  | 15  | 30  | -50  | 40   
[Labrador retriever](/wiki/Labrador_retriever "Labrador retriever") | 5  | 56  | 280  | 0%  | 0.64  | 1  | 15  | 30  | -30  | 40   
[Mastodon](/wiki/Mastodon "Mastodon") | 4.7  | 337  | 1583.9  | 75%  | 2.88  | 24  | 18  | 39.96  | -55  | 40   
[Megasloth](/wiki/Megasloth "Megasloth") | 4.8  | 300  | 1440  | 97%  | 1.6  | 24  | 19.98  | 40.02  | -55  | 40   
[Megaspider](/wiki/Megaspider "Megaspider") | 3.6  | 90  | 324  | 40%  | 0.56  | 1  | 1.8  | 12  | -40  | 60   
[Panther](/wiki/Panther "Panther") | 5  | 75  | 375  | 80%  | 0.32  | 2  | 15  | 30  | -8  | 50   
[Polar bear](/wiki/Polar_bear "Polar bear") | 4.6  | 161  | 740.6  | 85%  | 0.56  | 4  | 12  | 30  | -55  | 40   
[Scimitar cat](/wiki/Scimitar_cat "Scimitar cat") | 6  | 97  | 582  | 80%  | 0.42  | 2  | 15  | 30  | -40  | 40   
[Sea lion](/wiki/Sea_lion "Sea lion") | 2.8  | 90  | 252  | 50%  | 0.48  | 8  | 6  | 19.98  | -40  | 40   
[Seal](/wiki/Seal "Seal") | 2.6  | 60  | 156  | 50%  | 0.48  | 6  | 6  | 19.98  | -20  | 40   
[Spelopede](/wiki/Spelopede "Spelopede") | 3.65  | 60  | 219  | 30%  | 0.4  | 1  | 1.8  | 12  | -25  | 60   
[Thrumbo](/wiki/Thrumbo "Thrumbo") | 5.5  | 300  | 1650  | 98%  | 2.8  | 8  | 45  | 79.92  | -65  | 50   
[Tiger](/wiki/Tiger "Tiger") | 5.2  | 105  | 546  | 90%  | 0.32  | 1  | 15  | 30  | -8  | 50   
[Timber wolf](/wiki/Timber_wolf "Timber wolf") | 5  | 64  | 320  | 85%  | 0.29  | 2  | 12  | 30  | -40  | 40   
Attack target [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to Attack Target: [Arctic wolf](/wiki/Arctic_wolf "Arctic wolf"), [Cougar](/wiki/Cougar "Cougar"), [Grizzly bear](/wiki/Grizzly_bear "Grizzly bear"), [Megaspider](/wiki/Megaspider "Megaspider"), [Panther](/wiki/Panther "Panther"), [Polar bear](/wiki/Polar_bear "Polar bear"), [Timber wolf](/wiki/Timber_wolf "Timber wolf"), [Warg](/wiki/Warg "Warg"), [Crow](/wiki/Crow "Crow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Greatwolf](/wiki/Greatwolf "Greatwolf")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Scimitar cat](/wiki/Scimitar_cat "Scimitar cat")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Tiger](/wiki/Tiger "Tiger")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> Command the animal to attack a specific target-- Attack Target description  
  
Comfort[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to comfort: [Cat](/wiki/Cat "Cat"), [Husky](/wiki/Husky "Husky"), [Labrador retriever](/wiki/Labrador_retriever "Labrador retriever"), [Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier"), [Panda](/wiki/Panda "Panda")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Seal](/wiki/Seal "Seal")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> The animal will be more emotionally supportive. It will nuzzle more often, and make your colonists happier when it does so.-- Comfort description  
  
Forage[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Forage.png](/images/2/21/Forage.png) | - | 3  | See also: [Foraging](/wiki/Foraging "Foraging") The following animals can be trained to forage: [Pig](/wiki/Pig "Pig"), [Raccoon](/wiki/Raccoon "Raccoon"), [Wild boar](/wiki/Wild_boar "Wild boar"), [Gorilla](/wiki/Gorilla "Gorilla")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Locust](/wiki/Locust "Locust")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> "The animal will occasionally find berries, mushrooms, or food. Animals will find more food in biomes with higher forageability. Foraging can only be done on fertile terrain."-- Foraging description  
  
Dig[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 3  | The following animals can be trained to dig: [Megasloth](/wiki/Megasloth "Megasloth"), [Spelopede](/wiki/Spelopede "Spelopede"), [Megavole](/wiki/Megavole "Megavole")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> The animal will mine rock designated for mining. Animals are generally slow and inefficient at mining.-- Dig description  
  
War trumpet[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to War Trumpet: [Elephant](/wiki/Elephant "Elephant"), [Mastodon](/wiki/Mastodon "Mastodon")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> Command the animal to release a powerful roar. This has a chance to cause hostile humans and animals to tremble in fear, reducing their movement speed and manipulation.-- War Trumpet description  
  
Thrumbo roar[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to Thrumbo Roar: [Thrumbo](/wiki/Thrumbo "Thrumbo")

> Command the thrumbo to release a deafening roar. This has a chance to cause hostile humans and animals to tremble in fear, reducing their movement speed and manipulation.-- Thrumbo Roar description  
  
Terror roar[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to Terror Roar: [Alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> Command the alpha thrumbo to release a deafening roar. This has a chance to send nearby hostile humans and animals fleeing in terror.-- Terror Roar description  
  
Sludge spew[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to Sludge Spew: [Larva](/wiki/Larva "Larva")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> Command the larva to spray an acidic sludge all over the target area. Once trained, larva will only spew sludge when commanded.-- Sludge Spew description  
  
Egg spew[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | ![Special.png](/images/2/24/Special.png) | - | 2  | The following animals can be trained to Egg Spew: [Hive queen](/wiki/Hive_queen "Hive queen")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

> Command the queen to launch an egg sac and a spray of acidic sludge at the target area. Once trained, the queen will only produce eggs when commanded-- Egg Spew description  
  
### Combat[[edit](/index.php?title=Animal_husbandry&action=edit&section=13 "Edit section: Combat")]

Once Guard is trained, animals will gather around their master upon drafting, and will attack nearby threats, or (unintentionally) block ranged attacks for their master. This is configurable and can be disabled by disabling follow during drafted. 

With Attack trained, animals can be released to attack threats from a distance. Even colonists incapable of Violence can send their assigned animals into battle. 

Animals can be downed during combat, and can be rescued by colonists or other animals capable of Rescue. 

### Slaughtering[[edit](/index.php?title=Animal_husbandry&action=edit&section=14 "Edit section: Slaughtering")]

[![StumpChoppedA \(cropped\).png](/images/thumb/6/6a/StumpChoppedA_%28cropped%29.png/40px-StumpChoppedA_%28cropped%29.png)](/wiki/Category:Stubs "Category:Stubs") | **This section is a[stub](/wiki/Category:Stubs "Category:Stubs").** You can help RimWorld Wiki by **[expanding it](https://rimworldwiki.com/index.php?title=Animal_husbandry&action=edit). Reason:** _This section is included in the[Butchery project](/wiki/RimWorld_Wiki:To-do#Butchery_project "RimWorld Wiki:To-do") \- there are a number of factors that are in need of verification and potentially addition to this section. See that page for details._  
---|---  
  
![SlaughterButton.png](/images/thumb/f/fd/SlaughterButton.png/64px-SlaughterButton.png)

Tamed animals may be slaughtered selecting the animal and clicking the Slaughter button, or by using the Slaughter tool from the Orders menu. An animal marked in this way will be slaughtered by an animal handler. The handler need not be equipped with a weapon but must be [capable of violence](/wiki/Incapable "Incapable"). This job takes ???[How long?] to perform and instantly kills the animal - the animal will not resist, flee, or fight. You can also set up an auto-slaughter order in the animals tab, configurable to limit the amount of male, female, and pregnant animals in a pen. 

Animals killed through damage suffer a 66% multiplier to [Meat Amount](/wiki/Meat_Amount "Meat Amount") and [Leather Amount](/wiki/Leather_Amount "Leather Amount"). Slaughtering, throat slitting a downed-but-not-injured animal as a hunting task, the "euthanize by cut" [operation](/wiki/Operation "Operation"), and the [Animal Sacrifice](/wiki/Rituals#Animal_sacrifice "Rituals") ritual[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") all result in a careful slaughter and avoid the 66% modifier. 

If you try to slaughter a bonded animal, the game will warn you about it due to the mood impact this has on the animal's master. 

#### Auto-Slaughter[[edit](/index.php?title=Animal_husbandry&action=edit&section=15 "Edit section: Auto-Slaughter")]

[![](/images/thumb/f/f5/Autoslaughter.png/200px-Autoslaughter.png)](/wiki/File:Autoslaughter.png)

[](/wiki/File:Autoslaughter.png "Enlarge")

Auto-slaughter menu

Via the Animals button on the bottom bar is a "Manage auto-slaughter.." option. Auto-slaughter allows the player to automatically cull animals above a defined threshold. 

Total Animals, Male/Female Adults, Male/Female Young are all definable amounts that the player can set. If the current animal count exceeds any of the defined amounts in any of these columns the eldest allowed animal of that exceeded type is slaughtered. These 5 left-most columns function as OR operators. The two rightmost columns allow the player to allow the slaughtering of pregnant or bonded animals if desired. 

### Other Interactions[[edit](/index.php?title=Animal_husbandry&action=edit&section=16 "Edit section: Other Interactions")]

#### Caravans[[edit](/index.php?title=Animal_husbandry&action=edit&section=17 "Edit section: Caravans")]

Main article: [Pack animal](/wiki/Pack_animal "Pack animal")

These animals can graze, meaning they don't usually require food during a [caravan](/wiki/Caravan "Caravan"). (This may not be true when traveling across cold or inhospitable [biomes](/wiki/Biome "Biome"), like tundra or deserts, or in winter in general.) When carrying items in their inventory, they will appear to have packs on, which disappear when unloaded. 

#### Release to Wild[[edit](/index.php?title=Animal_husbandry&action=edit&section=18 "Edit section: Release to Wild")]

Unwanted animals can be released to the wild using a command next to the slaughter button. Releasing bonded animals also causes a mood debuff to master of the animal. 

#### Social[[edit](/index.php?title=Animal_husbandry&action=edit&section=19 "Edit section: Social")]

Each animal has a Social tab that lists that animal's human [bonds](/wiki/Bond "Bond") and familial relations. Clicking an entry jumps to that bond's counterpart on the map. Animals, even wild ones, have a small chance of bonding with a colonist everytime they interact. Bonded animals are given a unique name by their Master. Animals assigned to Guard a bonded human will give their master a permanent +5 mood thought. Humans who are not the master of their bonded animal receive a -5 "Not bonded animal's master" thought. Animals do not have a mood meter. Humans may have more than one bonded animal, but animals may only have one human bond. 

#### Trade goods[[edit](/index.php?title=Animal_husbandry&action=edit&section=20 "Edit section: Trade goods")]

Tamed animals may be sold to [traders](/wiki/Trade "Trade"). Animals purchased from traders will be already tamed. Bulk goods traders offer pets and farm animals while exotic goods traders carry most of the wild species. Traders offering animals will attempt to at least carry a breeding pair of a core farm animal. 

## Products[[edit](/index.php?title=Animal_husbandry&action=edit&section=21 "Edit section: Products")]

Certain tame animals produce [![Eggs](/images/thumb/8/88/Egg_small_a.png/16px-Egg_small_a.png)](/wiki/Eggs "Eggs") [eggs](/wiki/Eggs "Eggs"), [![Milk](/images/thumb/9/92/Milk.png/16px-Milk.png)](/wiki/Milk "Milk") [milk](/wiki/Milk "Milk"), [![Wool](/images/thumb/3/34/Wool.png/16px-Wool.png)](/wiki/Wool "Wool") [wool](/wiki/Wool "Wool"), or [![Chemfuel](/images/thumb/7/72/Chemfuel.png/16px-Chemfuel.png)](/wiki/Chemfuel "Chemfuel") [chemfuel](/wiki/Chemfuel "Chemfuel"). Milking (including chemfuel) and shearing sometimes fails, which is indicated with a brief "product wasted" message. This and the amount of wool, milk or chemfuel respectively is dependent on the [Animal Gather Yield](/wiki/Animal_Gather_Yield "Animal Gather Yield") stat of the pawn. 

### Eggs[[edit](/index.php?title=Animal_husbandry&action=edit&section=22 "Edit section: Eggs")]

Main article: [Eggs](/wiki/Eggs "Eggs")

* Animal | Fert. Egg | Unfert. Egg | Can lay  
unfertilized | Nutrition  
per Egg | Avg Eggs  
per Clutch | Laying  
Interval | Avg Eggs  
per Day | Egg Nutrition  
per Day | Needed  
Males / Female | Daily Hunger  
Rate | Daily Egg Nutrition  
per Hunger   
---|---|---|---|---|---|---|---|---|---|---|---  
[Cassowary](/wiki/Cassowary "Cassowary") | [![Cassowary egg \(fert.\)](/images/thumb/7/77/Cassowary_egg_%28fert.%29_b.png/32px-Cassowary_egg_%28fert.%29_b.png)](/wiki/Cassowary_egg_\(fert.\) "Cassowary egg \(fert.\)") | [![Cassowary egg \(unfert.\)](/images/thumb/7/77/Cassowary_egg_%28fert.%29_b.png/32px-Cassowary_egg_%28fert.%29_b.png)](/wiki/Cassowary_egg_\(unfert.\) "Cassowary egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 3.33 days  | 0.3  | 0.15  | 0.33  | 0.6  | 0.25   
[Chicken](/wiki/Chicken "Chicken") | [![Chicken egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Chicken_egg_\(fert.\) "Chicken egg \(fert.\)") | [![Chicken egg \(unfert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Chicken_egg_\(unfert.\) "Chicken egg \(unfert.\)") | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | 0.25  | 1  | 1 days  | 1  | 0.25  | 0  | 0.22  | 1.14   
[Cobra](/wiki/Cobra "Cobra") | [![Cobra egg \(fert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Cobra_egg_\(fert.\) "Cobra egg \(fert.\)") | [![Cobra egg \(unfert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Cobra_egg_\(unfert.\) "Cobra egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1.5  | 10 days  | 0.15  | 0.04  | 0.11  | 0.12  | 0.31   
[Duck](/wiki/Duck "Duck") | [![Duck egg \(fert.\)](/images/thumb/c/ce/Duck_egg_%28fert.%29_b.png/32px-Duck_egg_%28fert.%29_b.png)](/wiki/Duck_egg_\(fert.\) "Duck egg \(fert.\)") | [![Duck egg \(unfert.\)](/images/thumb/b/ba/Duck_egg_%28unfert.%29_b.png/32px-Duck_egg_%28unfert.%29_b.png)](/wiki/Duck_egg_\(unfert.\) "Duck egg \(unfert.\)") | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | 0.25  | 1  | 1 days  | 1  | 0.25  | 0  | 0.28  | 0.89   
[Emu](/wiki/Emu "Emu") | [![Emu egg \(fert.\)](/images/thumb/9/91/Emu_egg_%28fert.%29_b.png/32px-Emu_egg_%28fert.%29_b.png)](/wiki/Emu_egg_\(fert.\) "Emu egg \(fert.\)") | [![Emu egg \(unfert.\)](/images/thumb/9/91/Emu_egg_%28fert.%29_b.png/32px-Emu_egg_%28fert.%29_b.png)](/wiki/Emu_egg_\(unfert.\) "Emu egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 3.33 days  | 0.3  | 0.15  | 0.33  | 0.6  | 0.25   
[Goose](/wiki/Goose "Goose") | [![Goose egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Goose_egg_\(fert.\) "Goose egg \(fert.\)") | [![Goose egg \(unfert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Goose_egg_\(unfert.\) "Goose egg \(unfert.\)") | ![Check.png](/images/thumb/2/2a/Check.png/24px-Check.png) | 0.5  | 1  | 2 days  | 0.5  | 0.25  | 0  | 0.45  | 0.56   
[Iguana](/wiki/Iguana "Iguana") | [![Iguana egg \(fert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Iguana_egg_\(fert.\) "Iguana egg \(fert.\)") | [![Iguana egg \(unfert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Iguana_egg_\(unfert.\) "Iguana egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1.5  | 5.661 days  | 0.26  | 0.07  | 0.19  | 0.38  | 0.17   
[Ostrich](/wiki/Ostrich "Ostrich") | [![Ostrich egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Ostrich_egg_\(fert.\) "Ostrich egg \(fert.\)") | [![Ostrich egg \(unfert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Ostrich_egg_\(unfert.\) "Ostrich egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.6  | 1  | 3.33 days  | 0.3  | 0.18  | 0.33  | 0.89  | 0.2   
[Tortoise](/wiki/Tortoise "Tortoise") | [![Tortoise egg \(fert.\)](/images/thumb/1/17/Tortoise_egg_%28fert.%29_b.png/32px-Tortoise_egg_%28fert.%29_b.png)](/wiki/Tortoise_egg_\(fert.\) "Tortoise egg \(fert.\)") | [![Tortoise egg \(unfert.\)](/images/thumb/1/17/Tortoise_egg_%28fert.%29_b.png/32px-Tortoise_egg_%28fert.%29_b.png)](/wiki/Tortoise_egg_\(unfert.\) "Tortoise egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 2  | 6.66 days  | 0.3  | 0.08  | 0.17  | 0.15  | 0.49   
[Turkey](/wiki/Turkey "Turkey") | [![Turkey egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Turkey_egg_\(fert.\) "Turkey egg \(fert.\)") | [![Turkey egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Turkey_egg_\(unfert.\) "Turkey egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 1.333 days  | 0.75  | 0.38  | 0.83  | 0.82  | 0.46   
[Alligator](/wiki/Alligator "Alligator")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Alligator egg \(fert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Alligator_egg_\(fert.\) "Alligator egg \(fert.\)") | [![Alligator egg \(unfert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Alligator_egg_\(unfert.\) "Alligator egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1.5  | 12 days  | 0.13  | 0.06  | 0.09  | 0.52  | 0.12   
[Bluebird](/wiki/Bluebird "Bluebird")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Bluebird egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Bluebird_egg_\(fert.\) "Bluebird egg \(fert.\)") | [![Bluebird egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Bluebird_egg_\(unfert.\) "Bluebird egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 3 days  | 0.33  | 0.08  | 0.25  | 0.16  | 0.51   
[Crow](/wiki/Crow "Crow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Crow egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Crow_egg_\(fert.\) "Crow egg \(fert.\)") | [![Crow egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Crow_egg_\(unfert.\) "Crow egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 3 days  | 0.33  | 0.08  | 0.37  | 0.18  | 0.47   
[Flamingo](/wiki/Flamingo "Flamingo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Flamingo egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Flamingo_egg_\(fert.\) "Flamingo egg \(fert.\)") | [![Flamingo egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Flamingo_egg_\(unfert.\) "Flamingo egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 2 days  | 0.5  | 0.25  | 0.55  | 0.7  | 0.36   
[Heron](/wiki/Heron "Heron")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Heron egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Heron_egg_\(fert.\) "Heron egg \(fert.\)") | [![Heron egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Heron_egg_\(unfert.\) "Heron egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 2 days  | 0.5  | 0.25  | 0.55  | 0.7  | 0.36   
[Macaw](/wiki/Macaw "Macaw")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Macaw egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Macaw_egg_\(fert.\) "Macaw egg \(fert.\)") | [![Macaw egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Macaw_egg_\(unfert.\) "Macaw egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 8 days  | 0.13  | 0.03  | 0.09  | 0.21  | 0.15   
[Monitor lizard](/wiki/Monitor_lizard "Monitor lizard")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Monitor lizard egg \(fert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Monitor_lizard_egg_\(fert.\) "Monitor lizard egg \(fert.\)") | [![Monitor lizard egg \(unfert.\)](/images/thumb/3/34/Egg_oval_b.png/32px-Egg_oval_b.png)](/wiki/Monitor_lizard_egg_\(unfert.\) "Monitor lizard egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 6 days  | 0.17  | 0.04  | 0.18  | 0.38  | 0.11   
[Peafowl](/wiki/Peafowl "Peafowl")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Peafowl egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Peafowl_egg_\(fert.\) "Peafowl egg \(fert.\)") | [![Peafowl egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Peafowl_egg_\(unfert.\) "Peafowl egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 2 days  | 0.5  | 0.13  | 0.55  | 0.57  | 0.22   
[Penguin](/wiki/Penguin "Penguin")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Penguin egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Penguin_egg_\(fert.\) "Penguin egg \(fert.\)") | [![Penguin egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Penguin_egg_\(unfert.\) "Penguin egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1  | 2 days  | 0.5  | 0.25  | 0.55  | 0.7  | 0.36   
[Quail](/wiki/Quail "Quail")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Quail egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Quail_egg_\(fert.\) "Quail egg \(fert.\)") | [![Quail egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Quail_egg_\(unfert.\) "Quail egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 1.3 days  | 0.77  | 0.19  | 0.57  | 0.3  | 0.64   
[Sea turtle](/wiki/Sea_turtle "Sea turtle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Sea turtle egg \(fert.\)](/images/thumb/b/bc/Sea_turtle_egg_%28fert.%29_b.png/32px-Sea_turtle_egg_%28fert.%29_b.png)](/wiki/Sea_turtle_egg_\(fert.\) "Sea turtle egg \(fert.\)") | [![Sea turtle egg \(unfert.\)](/images/thumb/6/67/Sea_turtle_egg_%28unfert.%29_b.png/32px-Sea_turtle_egg_%28unfert.%29_b.png)](/wiki/Sea_turtle_egg_\(unfert.\) "Sea turtle egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.5  | 1.5  | 6.66 days  | 0.23  | 0.11  | 0.17  | 0.19  | 0.6   
[Sparrow](/wiki/Sparrow "Sparrow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Sparrow egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Sparrow_egg_\(fert.\) "Sparrow egg \(fert.\)") | [![Sparrow egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Sparrow_egg_\(unfert.\) "Sparrow egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 3 days  | 0.33  | 0.08  | 0.25  | 0.16  | 0.51   
[Swan](/wiki/Swan "Swan")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Swan egg \(fert.\)](/images/thumb/5/5d/Egg_small_b.png/32px-Egg_small_b.png)](/wiki/Swan_egg_\(fert.\) "Swan egg \(fert.\)") | [![Swan egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Swan_egg_\(unfert.\) "Swan egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 2 days  | 0.5  | 0.13  | 0.37  | 0.62  | 0.2   
[Vulture](/wiki/Vulture "Vulture")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | [![Vulture egg \(fert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Vulture_egg_\(fert.\) "Vulture egg \(fert.\)") | [![Vulture egg \(unfert.\)](/images/thumb/6/68/Turkey_egg_%28fert.%29_b.png/32px-Turkey_egg_%28fert.%29_b.png)](/wiki/Vulture_egg_\(unfert.\) "Vulture egg \(unfert.\)") | ![Ex.png](/images/thumb/9/9e/Ex.png/24px-Ex.png) | 0.25  | 1  | 4 days  | 0.25  | 0.06  | 0.28  | 0.47  | 0.13   
  
### Milk[[edit](/index.php?title=Animal_husbandry&action=edit&section=23 "Edit section: Milk")]

Main article: [Milk](/wiki/Milk "Milk")

* Animal | Milk Amount | Milking  
Interval | Milk/Day  
(Average) | Milk / food consumed  
per day | Nutrition / food consumed  
per day   
---|---|---|---|---|---  
[Caribou](/wiki/Caribou "Caribou") | 10 | 2 | 5 | 11.36 | 0.57   
[Cow](/wiki/Cow "Cow") | 14 | 1 | 14 | 16.28 | 0.81   
[Dromedary](/wiki/Dromedary "Dromedary") | 18 | 2 | 9 | 10.47 | 0.52   
[Elk](/wiki/Elk "Elk") | 11 | 1 | 11 | 12.79 | 0.64   
[Goat](/wiki/Goat "Goat") | 12 | 3 | 4 | 11.11 | 0.56   
[Yak](/wiki/Yak "Yak") | 11 | 1 | 11 | 12.79 | 0.64   
  
### Wool[[edit](/index.php?title=Animal_husbandry&action=edit&section=24 "Edit section: Wool")]

Main article: [Wool](/wiki/Wool "Wool")

Animal | Wool Name | Wool Amount | Shearing Interval | Daily Wool Average   
---|---|---|---|---  
[Alpaca](/wiki/Alpaca "Alpaca") | Alpaca wool | 45 | 10 | 4.5   
[Bison](/wiki/Bison "Bison") | Bison wool | 120 | 15 | 8   
[Megasloth](/wiki/Megasloth "Megasloth") | Megasloth wool | 200 | 20 | 10   
[Muffalo](/wiki/Muffalo "Muffalo") | Muffalo wool | 120 | 15 | 8   
[Sheep](/wiki/Sheep "Sheep") | Sheep wool | 45 | 10 | 4.5   
[Mastodon](/wiki/Mastodon "Mastodon")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | Mastodon wool | 200 | 20 | 10   
[Muskox](/wiki/Muskox "Muskox")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | Muskox wool | 120 | 15 | 8   
  
### Chemfuel[[edit](/index.php?title=Animal_husbandry&action=edit&section=25 "Edit section: Chemfuel")]

Main article: [Chemfuel](/wiki/Chemfuel "Chemfuel")

Animal | Chemfuel Amount | Milking Interval | Daily Chemfuel Average   
---|---|---|---  
[Boomalope](/wiki/Boomalope "Boomalope") | 11 | 1 | 11   
  
## Feeding[[edit](/index.php?title=Animal_husbandry&action=edit&section=26 "Edit section: Feeding")]

### Grazing wild plants[[edit](/index.php?title=Animal_husbandry&action=edit&section=27 "Edit section: Grazing wild plants")]

Letting your animals graze is one of the easiest way to feed your [herbivorous](/wiki/Herbivorous "Herbivorous"), omnivorous grazer and dendrovorous animals. While the later can only "graze" live [trees](/wiki/Tree "Tree"), the former two can eat all other living [plants](/wiki/Plant "Plant"). Depending on the animals in the colony it might therefore be beneficial to cut all trees or other plants respectively in the grazing area. 

The simplest way to feed non-strictly-carnivorous animals is to create a large [pen](/wiki/Pens "Pens") where animals can graze on the wild grass and brambles. The [pen marker](/wiki/Pen_marker "Pen marker") will show the number of animals the wild plants can sustain (measured in [cows](/wiki/Cow "Cow"), [goats](/wiki/Goat "Goat"), and [chickens](/wiki/Chicken "Chicken"). When the weather is too cold or too hot though, plants grow slower or even stop growing. Furthermore, plants become totally inedible when the temperature drops below -10 °C (14 °F), because they all are considered leafless, grass as well as trees. This mechanic is not explained in-game, and is quite puzzling to unaware players. It looks like animals starve on top of good-looking grass. See [Plants](/wiki/Plants#Temperature "Plants") for more info. 

While grazing might need the least amount of work, it can also be highly inefficient for smaller animals. Most wild plants have 0.5 nutrition (except the rather uncommon [Agave](/wiki/Agave "Agave"), [Astragalus](/wiki/Astragalus "Astragalus"), [Bryolux](/wiki/Bryolux "Bryolux"), [Chokevine](/wiki/Chokevine "Chokevine"), [Low shrubs](/wiki/Low_shrubs "Low shrubs"), [Pincushion cactus](/wiki/Pincushion_cactus "Pincushion cactus"), [Wild healroot](/wiki/Wild_healroot "Wild healroot"), [Fireweed](/wiki/Fireweed "Fireweed")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC"), [Magma cactus](/wiki/Magma_cactus "Magma cactus")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")). The amount of nutrition an animal can hold is dependent on its [body size](/wiki/Body_size "Body size") and its life stage. They will start eating as soon as they hold less than 25 % of the maximum nutrition they can hold (see [saturation](/wiki/Saturation "Saturation") for more info). This means all adult animals with a body size below 0.67 will start eating before they can fit the full 0.5 nutrition of most plants, with the excess getting wasted. This is even more pronounced for baby and juvenile animals since they are smaller. Only species that have an adult body size of at least 0.89 will not be overeating when juvenile and with an adult body size of at least 1.11 as babies as well. 

### Growing haygrass[[edit](/index.php?title=Animal_husbandry&action=edit&section=28 "Edit section: Growing haygrass")]

While the land can sustain a sizable population of animals grazing on it, it doesn't have an infinite supply and can still be depleted. Winter can also stop grass growth, leaving nothing for your grazing animals to eat. 

If you need to raise a lot of animals, e.g. an exponentially growing flock of [chickens](/wiki/Chicken "Chicken"), you will need to grow haygrass to sustain them all. You also need to have a stock of haygrass to keep animals fed through the winter. 

Haygrass gives a total of 0.9 nutrition (18 units of [hay](/wiki/Hay "Hay")) when fully grown and harvested, compared to 0.5 of grass. However, you have to keep your hungry animals from getting to it otherwise they'll only get a max of 0.2 nutrition from eating the plant. 

### Making kibble[[edit](/index.php?title=Animal_husbandry&action=edit&section=29 "Edit section: Making kibble")]

[Kibble](/wiki/Kibble "Kibble") is a kind of animal feed made with both plant and animal sources. It can be made using haygrass and any kind of meat, including human or insect meat. Producing kibble at a [butcher table](/wiki/Butcher_table "Butcher table") costs 1 nutrition of vegetables or hay and 1 nutrition of meat or animal products, and produces 2.5 nutrition of kibble. 

All animals except [wargs](/wiki/Warg "Warg") can eat it, so it makes a good way to feed your animals using mixed sources of nutrition, including those that animals won't normally eat. Kibble also lasts forever under a roof so you can store it and use it to feed animals when in need, such as in winter when there is nothing to eat. 

When you feed a population of herbivorous or omnivorous animals kibble made from their own meat or milk, the formula for their nutrition efficiency can be calculated as: 

_nutritionEfficiency(kibble)_ = 2.5× _nutritionEfficiency(raw vegetables)_ \- 1

In effect, this means that for any animal population that has a nutrition efficiency of at least 0.667, it is more efficient to feed them kibble rather than hay. It is worth noting, however, that this will increase the amount of butchering and cooking labour needed to support the higher animal population required. 

### Corpse freezer[[edit](/index.php?title=Animal_husbandry&action=edit&section=30 "Edit section: Corpse freezer")]

In typical RimWorlder fashion, you can use a freezer to preserve the corpses of raiders (or dead colonists if you're desperate) so you can feed omnivorous and carnivorous animals. This allows you to make use of corpses while avoiding heavy mood penalties from butchering humans or eating their flesh. 

## Raising[[edit](/index.php?title=Animal_husbandry&action=edit&section=31 "Edit section: Raising")]

### Pens[[edit](/index.php?title=Animal_husbandry&action=edit&section=32 "Edit section: Pens")]

Main article: [Pens](/wiki/Pens "Pens")

Pens are areas which farm animals are assigned to. These [pen animals](/wiki/Pen_animals "Pen animals") will be passive, meaning that hostiles will not attack these animals, and vice versa. Tamed pen animals must be put in a pen, or they will occasionally attempt to leave the map, meaning they disappear forever. Colonists will automatically rope roaming farm animals and place them in the pen. The borders of pens can be marked with: solid [walls](/wiki/Wall "Wall"), [doors](/wiki/Door "Door"), [fences](/wiki/Fence "Fence"), [fence gates](/wiki/Fence_gate "Fence gate"), and [animal flaps](/wiki/Animal_flap "Animal flap"). To mark an enclosed area as a pen, place a pen marker inside. The pen marker also tells you the amount of animals that can be sustained in a pen with wild plants, measured in [cows](/wiki/Cow "Cow"), [goats](/wiki/Goat "Goat"), and [chickens](/wiki/Chicken "Chicken"). An attached, roofed, and heated/cooled coop can be built with an [animal flap](/wiki/Animal_flap "Animal flap") as a door instead of a regular [door](/wiki/Door "Door") for animals to stay warm or cool down during extreme temperatures. 

### Pet care[[edit](/index.php?title=Animal_husbandry&action=edit&section=33 "Edit section: Pet care")]

Tamed animals that have a social bond to a person will affect the master's mood positively while living and negatively if killed (-8 for 20 days). This bond will either improve resistance against mental breaks or cause them. Because of the effect they cause on feelings, these creatures should be given special treatment, or any animal worth keeping alive. 

These are a few tips to keep them safe: 

  * Keep them indoors by creating a new animal zone within a room.
  * Keep them at the Home area after building a base wall.
  * Prey pets should not be left wandering around in unrestricted area.
  * Hunt their predators to prevent surprise attacks (or just wall the base in to prevent predators from coming in).
  * Patrol your perimeter by zooming your view out to a larger scale but not to full, just enough to spot their sleeping animation of flying ZZZs while they rest at night. Sweeping your surroundings once every night shall keep you aware of threat presence.
  * Animals can get into drugs, store them in specialized storage areas and use a zone to prevent them from accessing it, depending on size they may be prone to overdose or getting blackout from alcohol, being more dangerous with [Boomrats](/wiki/Boomrat "Boomrat") which can set fire to the storage area. Pen Animals should also be kept away from storage areas for this reason.



Note: The first three of these tips only apply to pet animals. Farm animals are passive while in pens, though if the pen is built with [fences](/wiki/Fence "Fence"), predators can still pass through. 

## Butchering[[edit](/index.php?title=Animal_husbandry&action=edit&section=34 "Edit section: Butchering")]

[![Rewrite.png](/images/thumb/a/a3/Rewrite.png/40px-Rewrite.png)](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten") | This section is suggested to be [rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten"). **Reason:** This section needs to better explain the assumptions and math built into gthe different results, ideally with a worked example using property calls to stay matched to the table result. see Talk page for some discussion. You can help the RimWorld Wiki by **[improving](https://rimworldwiki.com/index.php?title=Animal_husbandry&action=edit)** it.__  
---|---  
Animal  | Diet  | Tameness Decay Interval (Days) | Produces  | Produce / Day  | Produced Nutrition / Day  | Males / Female | Baby Slaughter  | Adult Slaughter   
---|---|---|---|---|---|---|---|---  
Meat Nutrition / Day | Consumption / Day | Meat Nutrition Efficiency[2] | Meat Nutrition / Day | Consumption / Day | Meat Nutrition Efficiency[2]  
[Alpaca](/wiki/Alpaca "Alpaca") | herbivorous  | –  | [Alpaca wool](/wiki/Alpaca_wool "Alpaca wool") | 4.5 | –  | 0.23  | 0.23  | 0.54  | 0.431  | 1.05  | 1.25  | 0.838 a)  
[Alphabeaver](/wiki/Alphabeaver "Alphabeaver") | dendrovorous  | 7.5  | – | – | –  | 0.18  | 0.24  | 5.66  | 0.042  | 0.74  | 20.23  | 0.037   
[Arctic fox](/wiki/Arctic_fox "Arctic fox") | carnivorous  | 7.5  | – | – | –  | 0.15  | 0.19  | 0.18  | 1.027  | 0.66  | 0.54  | 1.228   
[Arctic wolf](/wiki/Arctic_wolf "Arctic wolf") | carnivorous  | 6.9  | – | – | –  | 0.15  | 0.24  | 0.33  | 0.726  | 1.02  | 1.24  | 0.827   
[Bison](/wiki/Bison "Bison") | herbivorous  | –  | [Bison wool](/wiki/Bison_wool "Bison wool") | 8 | –  | 0.23  | 0.5  | 1.05  | 0.478  | 2.52  | 2.3  | 1.095   
[Boomalope](/wiki/Boomalope "Boomalope") | herbivorous  | –  | [Chemfuel](/wiki/Chemfuel "Chemfuel") | 11 | –  | 0.23  | 0.42  | 1.05  | 0.4  | 2.1  | 2.44  | 0.862   
[Boomrat](/wiki/Boomrat "Boomrat") | omnivorous grazer  | 7.5  | – | – | –  | 0.18  | 0.22  | 0.26  | 0.819 c) | 0.48  | 0.81  | 0.591 c)  
[Capybara](/wiki/Capybara "Capybara") | herbivorous  | –  | – | – | –  | 0.27  | 0.29  | 0.46  | 0.629  | 1.16  | 1.32  | 0.882 b)  
[Caribou](/wiki/Caribou "Caribou") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 5 | 0.25  | 0.23  | 0.23  | 0.54  | 0.893  | 1.05  | 1.15  | 1.127 a)  
[Cassowary](/wiki/Cassowary "Cassowary") | herbivorous  | –  | [Egg (fert.)](/wiki/Cassowary_egg_\(fert.\) "Cassowary egg \(fert.\)")| 0.3 | 0.15  | 0.23  | 0.26  | 0.55  | 0.464 c) | 1.26  | 1.61  | 0.782 c)  
[Cat](/wiki/Cat "Cat") | carnivorous, ovivorous  | –  | – | – | –  | 0.15  | 0.16  | 0.28  | 0.596  | 0.44  | 0.97  | 0.451   
[Chicken](/wiki/Chicken "Chicken") | herbivorous  | –  | [Egg (fert.)](/wiki/Chicken_egg_\(fert.\) "Chicken egg \(fert.\)") & [(unfert.)](/wiki/Chicken_egg_\(unfert.\) "Chicken egg \(unfert.\)")| 1 | 0.25  | 0.51  | 0.6  | 0.34  | 1.778 c) | 2.1  | 1.79  | 1.174 c)  
[Chinchilla](/wiki/Chinchilla "Chinchilla") | herbivorous  | –  | – | – | –  | 0.18  | 0.28  | 0.24  | 1.18 c) | 0.76  | 0.72  | 1.046 c)  
[Cobra](/wiki/Cobra "Cobra") | carnivorous, ovivorous  | 7.5  | [Egg (fert.)](/wiki/Cobra_egg_\(fert.\) "Cobra egg \(fert.\)")| 0.15 | 0.04  | 0.08  | 0.11  | 0.12  | 0.934  | 0.27  | 0.45  | 0.606   
[Cougar](/wiki/Cougar "Cougar") | carnivorous, ovivorous  | 7.2  | – | – | –  | 0.15  | 0.16  | 0.37  | 0.42  | 0.7  | 0.92  | 0.76   
[Cow](/wiki/Cow "Cow") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 14 | 0.7  | 0.23  | 0.5  | 1.05  | 1.144  | 2.52  | 2.44  | 1.321   
[Deer](/wiki/Deer "Deer") | herbivorous  | –  | – | – | –  | 0.27  | 0.31  | 0.41  | 0.762  | 1.48  | 1.14  | 1.307   
[Donkey](/wiki/Donkey "Donkey") | herbivorous  | –  | – | – | –  | 0.23  | 0.29  | 0.64  | 0.458  | 1.47  | 1.4  | 1.051   
[Dromedary](/wiki/Dromedary "Dromedary") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 9 | 0.45  | 0.23  | 0.44  | 1.05  | 0.849  | 2.21  | 2.3  | 1.153   
[Duck](/wiki/Duck "Duck") | herbivorous  | –  | [Egg (fert.)](/wiki/Duck_egg_\(fert.\) "Duck egg \(fert.\)") & [(unfert.)](/wiki/Duck_egg_\(unfert.\) "Duck egg \(unfert.\)")| 1 | 0.25  | 0.51  | 0.6  | 0.42  | 1.422 c) | 2.1  | 2.24  | 0.939 c)  
[Elephant](/wiki/Elephant "Elephant") | herbivorous  | 7.5  | – | – | –  | 0.11  | 0.42  | 2.86  | 0.147  | 2.1  | 7.42  | 0.283   
[Elk](/wiki/Elk "Elk") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 11 | 0.55  | 0.23  | 0.44  | 1.05  | 0.944  | 2.21  | 2.44  | 1.13   
[Emu](/wiki/Emu "Emu") | herbivorous  | –  | [Egg (fert.)](/wiki/Emu_egg_\(fert.\) "Emu egg \(fert.\)")| 0.3 | 0.15  | 0.23  | 0.26  | 0.55  | 0.464 c) | 1.26  | 1.61  | 0.782 c)  
[Fennec fox](/wiki/Fennec_fox "Fennec fox") | carnivorous  | 7.5  | – | – | –  | 0.15  | 0.19  | 0.18  | 1.027  | 0.66  | 0.54  | 1.228   
[Gazelle](/wiki/Gazelle "Gazelle") | herbivorous  | –  | – | – | –  | 0.27  | 0.22  | 0.3  | 0.725  | 0.87  | 0.64  | 1.354 b)  
[Goat](/wiki/Goat "Goat") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 4 | 0.2  | 0.27  | 0.23  | 0.46  | 0.944  | 0.94  | 1.09  | 1.041 b)  
[Goose](/wiki/Goose "Goose") | herbivorous  | –  | [Egg (fert.)](/wiki/Goose_egg_\(fert.\) "Goose egg \(fert.\)") & [(unfert.)](/wiki/Goose_egg_\(unfert.\) "Goose egg \(unfert.\)")| 0.5 | 0.25  | 0.25  | 0.43  | 0.56  | 0.757 c) | 2.1  | 2.01  | 1.043 c)  
[Grizzly bear](/wiki/Grizzly_bear "Grizzly bear") | omnivorous, ovivorous  | 7.2  | – | – | –  | 0.15  | 0.3  | 0.65  | 0.465  | 1.51  | 1.67  | 0.901   
[Guinea pig](/wiki/Guinea_pig "Guinea pig") | herbivorous  | 8.4  | – | – | –  | 0.15  | 0.18  | 0.18  | 0.998 c) | 0.41  | 0.43  | 0.947 c)  
[Hare](/wiki/Hare "Hare") | herbivorous  | 7.5  | – | – | –  | 0.18  | 0.22  | 0.22  | 0.998 c) | 0.48  | 0.67  | 0.719 c)  
[Horse](/wiki/Horse "Horse") | herbivorous  | –  | – | – | –  | 0.23  | 0.5  | 1.05  | 0.478  | 2.52  | 2.3  | 1.095   
[Husky](/wiki/Husky "Husky") | omnivorous, ovivorous  | –  | – | – | –  | 0.15  | 0.24  | 0.92  | 0.261  | 1.03  | 3.3  | 0.313   
[Ibex](/wiki/Ibex "Ibex") | herbivorous  | –  | – | – | –  | 0.27  | 0.27  | 0.41  | 0.675  | 1.24  | 0.85  | 1.451 a)  
[Iguana](/wiki/Iguana "Iguana") | omnivorous grazer  | 9  | [Egg (fert.)](/wiki/Iguana_egg_\(fert.\) "Iguana egg \(fert.\)")| 0.26 | 0.07  | 0.13  | 0.25  | 0.36  | 0.694 c) | 0.74  | 1.03  | 0.718 c)  
[Labrador retriever](/wiki/Labrador_retriever "Labrador retriever") | omnivorous, ovivorous  | –  | – | – | –  | 0.15  | 0.25  | 0.74  | 0.342  | 1.02  | 2.88  | 0.354   
[Lynx](/wiki/Lynx "Lynx") | carnivorous, ovivorous  | 7.2  | – | – | –  | 0.15  | 0.12  | 0.22  | 0.52  | 0.42  | 0.57  | 0.734   
[Megasloth](/wiki/Megasloth "Megasloth") | herbivorous  | 6.18  | [Megasloth wool](/wiki/Megasloth_wool "Megasloth wool") | 10 | –  | 0.11  | 0.42  | 1.78  | 0.236  | 2.1  | 4.55  | 0.463   
[Monkey](/wiki/Monkey "Monkey") | omnivorous grazer  | 8.4  | – | – | –  | 0.23  | 0.14  | 0.25  | 0.55 c) | 0.37  | 0.48  | 0.768 c)  
[Muffalo](/wiki/Muffalo "Muffalo") | herbivorous  | –  | [Muffalo wool](/wiki/Muffalo_wool "Muffalo wool") | 8 | –  | 0.23  | 0.5  | 1.05  | 0.478  | 2.52  | 2.3  | 1.095   
[Ostrich](/wiki/Ostrich "Ostrich") | herbivorous  | –  | [Egg (fert.)](/wiki/Ostrich_egg_\(fert.\) "Ostrich egg \(fert.\)")| 0.3 | 0.18  | 0.23  | 0.32  | 0.83  | 0.382  | 2.1  | 2.42  | 0.869 a)  
[Panther](/wiki/Panther "Panther") | carnivorous, ovivorous  | 7.2  | – | – | –  | 0.15  | 0.16  | 0.37  | 0.42  | 0.7  | 0.92  | 0.76   
[Pig](/wiki/Pig "Pig") | omnivorous grazer  | –  | – | – | –  | 0.27  | 0.56  | 1.01  | 0.551  | 2.77  | 3.42  | 0.811   
[Polar bear](/wiki/Polar_bear "Polar bear") | omnivorous, ovivorous  | 6.9  | – | – | –  | 0.15  | 0.3  | 0.65  | 0.465  | 1.51  | 1.67  | 0.901   
[Raccoon](/wiki/Raccoon "Raccoon") | omnivorous grazer  | 7.5  | – | – | –  | 0.18  | 0.25  | 0.38  | 0.667 c) | 0.74  | 1.05  | 0.709 c)  
[Rat](/wiki/Rat "Rat") | omnivorous grazer  | 9  | – | – | –  | 0.18  | 0.2  | 0.19  | 1.058 c) | 0.44  | 0.55  | 0.805 c)  
[Red fox](/wiki/Red_fox "Red fox") | carnivorous  | 7.5  | – | – | –  | 0.15  | 0.19  | 0.18  | 1.027  | 0.66  | 0.54  | 1.228   
[Rhinoceros](/wiki/Rhinoceros "Rhinoceros") | herbivorous  | 6.6  | – | – | –  | 0.11  | 0.32  | 1.91  | 0.165  | 1.58  | 4.28  | 0.368   
[Sheep](/wiki/Sheep "Sheep") | herbivorous  | –  | [Sheep wool](/wiki/Sheep_wool "Sheep wool") | 4.5 | –  | 0.27  | 0.3  | 0.46  | 0.663  | 1.22  | 1.27  | 0.96 b)  
[Snowhare](/wiki/Snowhare "Snowhare") | herbivorous  | 7.5  | – | – | –  | 0.18  | 0.22  | 0.22  | 0.998 c) | 0.48  | 0.67  | 0.719 c)  
[Squirrel](/wiki/Squirrel "Squirrel") | herbivorous  | 7.5  | – | – | –  | 0.27  | 0.18  | 0.2  | 0.88 c) | 0.4  | 0.52  | 0.765 c)  
[Thrumbo](/wiki/Thrumbo "Thrumbo") | herbivorous, dendrovorous  | 6.12  | – | – | –  | 0.08  | 0.28  | 3.01  | 0.093  | 1.4  | 9.2  | 0.152   
[Timber wolf](/wiki/Timber_wolf "Timber wolf") | carnivorous  | 6.9  | – | – | –  | 0.15  | 0.24  | 0.33  | 0.726  | 1.02  | 1.24  | 0.827   
[Tortoise](/wiki/Tortoise "Tortoise") | omnivorous grazer  | 7.5  | [Egg (fert.)](/wiki/Tortoise_egg_\(fert.\) "Tortoise egg \(fert.\)")| 0.3 | 0.08  | 0.11  | 0.32  | 0.15  | 2.144 c) | 1.05  | 0.42  | 2.511 c)  
[Turkey](/wiki/Turkey "Turkey") | herbivorous  | –  | [Egg (fert.)](/wiki/Turkey_egg_\(fert.\) "Turkey egg \(fert.\)")| 0.75 | 0.38  | 0.57  | 0.64  | 0.7  | 0.907 c) | 3.15  | 2.88  | 1.094 c)  
[Warg](/wiki/Warg "Warg") | strict carnivorous  | 8.4  | – | – | –  | 0.15  | 0.34  | 0.46  | 0.728  | 1.69  | 1.72  | 0.98   
[Wild boar](/wiki/Wild_boar "Wild boar") | omnivorous grazer  | –  | – | – | –  | 0.27  | 0.31  | 0.61  | 0.508  | 1.31  | 1.98  | 0.665 b)  
[Yak](/wiki/Yak "Yak") | herbivorous  | –  | [Milk](/wiki/Milk "Milk") | 11 | 0.55  | 0.23  | 0.44  | 1.05  | 0.944  | 2.21  | 2.44  | 1.13   
[Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier") | omnivorous, ovivorous  | –  | – | – | –  | 0.15  | 0.16  | 0.28  | 0.596  | 0.44  | 0.81  | 0.54   
[Toxalope](/wiki/Toxalope "Toxalope")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | herbivorous  | –  | – | – | –  | 0.23  | 0.29  | 1.05  | 0.279  | 1.05  | 2.44  | 0.431   
[Waste rat](/wiki/Waste_rat "Waste rat")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | omnivorous grazer  | 9  | – | – | –  | 0.18  | 0.24  | 0.19  | 1.285 c) | 0.6  | 0.55  | 1.091 c)  
[Alligator](/wiki/Alligator "Alligator")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 6.6  | [Egg (fert.)](/wiki/Alligator_egg_\(fert.\) "Alligator egg \(fert.\)")| 0.13 | 0.06  | 0.06  | 0.26  | 0.51  | 0.514  | 1.31  | 0.98  | 1.333   
[Alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous, dendrovorous  | 6.06  | – | – | –  | 0.08  | 0.35  | 3.01  | 0.116  | 1.75  | 9.2  | 0.19   
[Armadillo](/wiki/Armadillo "Armadillo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.5  | – | – | –  | 0.27  | 0.27  | 0.41  | 0.662 c) | 0.79  | 1.12  | 0.706 c)  
[Badger](/wiki/Badger "Badger")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.2  | – | – | –  | 0.27  | 0.33  | 0.41  | 0.801 c) | 1.19  | 1.12  | 1.06 c)  
[Bluebird](/wiki/Bluebird "Bluebird")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 8.4  | [Egg (fert.)](/wiki/Bluebird_egg_\(fert.\) "Bluebird egg \(fert.\)")| 0.33 | 0.08  | 0.17  | 0.2  | 0.15  | 1.337 c) | 0.43  | 0.43  | 1.017 c)  
[Bog hound](/wiki/Bog_hound "Bog hound")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous, ovivorous  | 9  | – | – | –  | 0.15  | 0.27  | 0.33  | 0.817  | 1.15  | 1.29  | 0.891   
[Bullfrog](/wiki/Bullfrog "Bullfrog")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.5  | – | – | –  | 0.27  | 0.12  | 0.2  | 0.609 c) | 0.27  | 0.43  | 0.642 c)  
[Colossus toad](/wiki/Colossus_toad "Colossus toad")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 10.5  | – | – | –  | 0.27  | 0.24  | 0.41  | 0.588  | 0.99  | 0.85  | 1.161 b)  
[Crow](/wiki/Crow "Crow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous, ovivorous  | 10.5  | [Egg (fert.)](/wiki/Crow_egg_\(fert.\) "Crow egg \(fert.\)")| 0.33 | 0.08  | 0.25  | 0.2  | 0.16  | 1.247  | 0.43  | 0.44  | 0.992   
[Flamingo](/wiki/Flamingo "Flamingo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 9.3  | [Egg (fert.)](/wiki/Flamingo_egg_\(fert.\) "Flamingo egg \(fert.\)")| 0.5 | 0.25  | 0.38  | 0.58  | 0.62  | 0.93 c) | 2.1  | 2.07  | 1.015 c)  
[Gorilla](/wiki/Gorilla "Gorilla")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 8.4  | – | – | –  | 0.23  | 0.42  | 1.06  | 0.396  | 2.1  | 2.07  | 1.016   
[Greatwolf](/wiki/Greatwolf "Greatwolf")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 6.3  | – | – | –  | 0.15  | 0.36  | 0.74  | 0.49  | 1.81  | 2.75  | 0.656   
[Hermit crab](/wiki/Hermit_crab "Hermit crab")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.5  | – | – | –  | 0.27  | 0.22  | 0.17  | 1.292 c) | 0.48  | 0.45  | 1.072 c)  
[Heron](/wiki/Heron "Heron")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 9.3  | [Egg (fert.)](/wiki/Heron_egg_\(fert.\) "Heron egg \(fert.\)")| 0.5 | 0.25  | 0.38  | 0.58  | 0.62  | 0.93 c) | 2.1  | 2.07  | 1.015 c)  
[Hippo](/wiki/Hippo "Hippo")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 6.6  | – | – | –  | 0.11  | 0.29  | 1.78  | 0.164  | 1.47  | 4  | 0.368   
[Lava snail](/wiki/Lava_snail "Lava snail")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | –  | – | – | –  | 0.23  | 0.39  | 0.39  | 1.003  | 1.71  | 1.08  | 1.585 a)  
[Macaw](/wiki/Macaw "Macaw")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 10.5  | [Egg (fert.)](/wiki/Macaw_egg_\(fert.\) "Macaw egg \(fert.\)")| 0.13 | 0.03  | 0.06  | 0.11  | 0.2  | 0.551 c) | 0.31  | 0.68  | 0.448 c)  
[Mastodon](/wiki/Mastodon "Mastodon")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 7.5  | [Mastodon wool](/wiki/Mastodon_wool "Mastodon wool") | 10 | –  | 0.11  | 0.45  | 3.19  | 0.141  | 2.25  | 8.06  | 0.279   
[Megavole](/wiki/Megavole "Megavole")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 9.6  | – | – | –  | 0.27  | 0.38  | 1.01  | 0.376  | 1.58  | 2.8  | 0.565 b)  
[Mink](/wiki/Mink "Mink")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous, ovivorous  | 7.5  | – | – | –  | 0.27  | 0.22  | 0.2  | 1.097  | 0.61  | 0.51  | 1.195   
[Monitor lizard](/wiki/Monitor_lizard "Monitor lizard")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 9  | [Egg (fert.)](/wiki/Monitor_lizard_egg_\(fert.\) "Monitor lizard egg \(fert.\)")| 0.17 | 0.04  | 0.13  | 0.19  | 0.36  | 0.532 c) | 0.7  | 0.78  | 0.895 c)  
[Moose](/wiki/Moose "Moose")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | –  | – | – | –  | 0.23  | 0.53  | 1.05  | 0.5  | 2.63  | 2.44  | 1.077   
[Muskox](/wiki/Muskox "Muskox")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | –  | [Muskox wool](/wiki/Muskox_wool "Muskox wool") | 8 | –  | 0.23  | 0.53  | 1.05  | 0.5  | 2.63  | 2.44  | 1.077   
[Otter](/wiki/Otter "Otter")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 9  | – | – | –  | 0.18  | 0.27  | 0.28  | 0.949 c) | 0.79  | 0.82  | 0.967 c)  
[Panda](/wiki/Panda "Panda")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 9.6  | – | – | –  | 0.15  | 0.21  | 0.37  | 0.57  | 1.05  | 0.95  | 1.1   
[Peafowl](/wiki/Peafowl "Peafowl")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | –  | [Egg (fert.)](/wiki/Peafowl_egg_\(fert.\) "Peafowl egg \(fert.\)")| 0.5 | 0.13  | 0.38  | 0.58  | 0.51  | 1.132 c) | 2.1  | 1.7  | 1.235 c)  
[Penguin](/wiki/Penguin "Penguin")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 9.3  | [Egg (fert.)](/wiki/Penguin_egg_\(fert.\) "Penguin egg \(fert.\)")| 0.5 | 0.25  | 0.38  | 0.58  | 0.62  | 0.93  | 2.1  | 2.07  | 1.015   
[Porcupine](/wiki/Porcupine "Porcupine")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 7.5  | – | – | –  | 0.18  | 0.25  | 0.28  | 0.899 c) | 0.69  | 0.82  | 0.846 c)  
[Prairie dog](/wiki/Prairie_dog "Prairie dog")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 9  | – | – | –  | 0.18  | 0.2  | 0.19  | 1.049 c) | 0.44  | 0.55  | 0.803 c)  
[Quail](/wiki/Quail "Quail")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | –  | [Egg (fert.)](/wiki/Quail_egg_\(fert.\) "Quail egg \(fert.\)")| 0.77 | 0.19  | 0.39  | 0.58  | 0.27  | 2.162 c) | 1.38  | 1.22  | 1.131 c)  
[Scimitar cat](/wiki/Scimitar_cat "Scimitar cat")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous, ovivorous  | 7.2  | – | – | –  | 0.15  | 0.19  | 0.48  | 0.386  | 0.91  | 1.2  | 0.76   
[Sea lion](/wiki/Sea_lion "Sea lion")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 9  | – | – | –  | 0.27  | 0.39  | 0.61  | 0.635  | 1.85  | 1.98  | 0.939   
[Sea turtle](/wiki/Sea_turtle "Sea turtle")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.5  | [Egg (fert.)](/wiki/Sea_turtle_egg_\(fert.\) "Sea turtle egg \(fert.\)")| 0.23 | 0.11  | 0.11  | 0.24  | 0.18  | 1.327 c) | 0.79  | 0.43  | 1.855 c)  
[Seal](/wiki/Seal "Seal")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 9  | – | – | –  | 0.27  | 0.3  | 0.61  | 0.49  | 1.24  | 1.98  | 0.626   
[Sparrow](/wiki/Sparrow "Sparrow")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 8.4  | [Egg (fert.)](/wiki/Sparrow_egg_\(fert.\) "Sparrow egg \(fert.\)")| 0.33 | 0.08  | 0.17  | 0.15  | 0.15  | 1.003 c) | 0.38  | 0.43  | 0.9 c)  
[Stone crab](/wiki/Stone_crab "Stone crab")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | omnivorous grazer  | 7.5  | – | – | –  | 0.27  | 0.26  | 0.24  | 1.079 c) | 0.65  | 0.65  | 0.999 c)  
[Swan](/wiki/Swan "Swan")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | herbivorous  | 9.3  | [Egg (fert.)](/wiki/Swan_egg_\(fert.\) "Swan egg \(fert.\)")| 0.5 | 0.13  | 0.25  | 0.58  | 0.56  | 1.024 c) | 2.1  | 2.01  | 1.043 c)  
[Tiger](/wiki/Tiger "Tiger")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous, ovivorous  | 6.6  | – | – | –  | 0.15  | 0.2  | 0.37  | 0.529  | 0.98  | 0.92  | 1.064   
[Vulture](/wiki/Vulture "Vulture")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | strict carnivorous  | 9.3  | [Egg (fert.)](/wiki/Vulture_egg_\(fert.\) "Vulture egg \(fert.\)")| 0.25 | 0.06  | 0.19  | 0.29  | 0.44  | 0.657  | 1.05  | 1.03  | 1.015   
[Walrus](/wiki/Walrus "Walrus")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | carnivorous  | 7.5  | – | – | –  | 0.23  | 0.53  | 1.06  | 0.495  | 2.63  | 3.15  | 0.833   
[Wolverine](/wiki/Wolverine "Wolverine")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") | strict carnivorous  | 6.3  | – | – | –  | 0.13  | 0.23  | 0.41  | 0.565  | 0.92  | 0.96  | 0.957   
  
a) Babies will overeat when grazing most wild plants. See [above](/wiki/Animal_husbandry#Grazing_wild_plants "Animal husbandry") or [saturation](/wiki/Saturation "Saturation") for more info.  
b) Babies and juveniles will overeat when grazing most wild plants. See [above](/wiki/Animal_husbandry#Grazing_wild_plants "Animal husbandry") or [saturation](/wiki/Saturation "Saturation") for more info.  
c) Babies, juveniles and adults will overeat when grazing most wild plants. See [above](/wiki/Animal_husbandry#Grazing_wild_plants "Animal husbandry") or [saturation](/wiki/Saturation "Saturation") for more info. 

## Notes[[edit](/index.php?title=Animal_husbandry&action=edit&section=35 "Edit section: Notes")]

  1. ↑ This is not an intrinsic property, just so happens that every currently implemented pen animal lacks the ability to be trained.
  2. ↑ 2.0 2.1 For a list that does include milking see [List of animals](/wiki/List_of_animals "List of animals").



## Version history[[edit](/index.php?title=Animal_husbandry&action=edit&section=36 "Edit section: Version history")]

  * [0.12.906](/wiki/Version/0.12.906 "Version/0.12.906") \- Animals can now be tamed and trained. Animals now sleep. Animals can be pregnant and give birth. Animals can be named when tamed or when nuzzling. Animals produce animal filth. Animals have “life stages” related to their ages. Eggs, Milk and Wool production added. Nuzzling added. Animals have life expectancies.
  * [0.12.910](/wiki/Version/0.12.910 "Version/0.12.910") \- Rebalanced animal hunger rate and animal hauling.
  * [0.13.1135](/wiki/Version/0.13.1135 "Version/0.13.1135") \- Added new animals, some of which will hunt people. Some animals are now predators, including colony pets (e.g. cats catch squirrels). Animals can gnaw corpses apart directly now. Animal bonding added.
  * Beta 19/1.0 Update - Obedience training steps 1 -> 3\. Nuzzle target search distance 15 -> 40\. Nuzzled memory duration 0.5 days->1 day, stacked effect multiplier 0.95->0.5, stack limit 10
  * [1.1.0](/wiki/Version/1.1.0 "Version/1.1.0") \- Changed animal rescue radius from 30 to 75. Fix: Jawless animals can still haul.
  * [1.2.2719](/wiki/Version/1.2.2719 "Version/1.2.2719") \- Removed naming animals through nuzzling. Animals only get names by bonding, or if given names by the player (so you can implicitly tell which animals are bonded by seeing which have names).
  * [1.3.3066](/wiki/Version/1.3.3066 "Version/1.3.3066") \- Major overhaul to animals: added multiple animal-related buildings, added pens, decreased trainability of [boomalope](/wiki/Boomalope "Boomalope") to none, added sterilization, added release to wild.



* * *

[Animals](/wiki/Animals "Animals")

[Herbivorous](/wiki/Herbivore "Herbivore")
    [Alpaca](/wiki/Alpaca "Alpaca") • [Bison](/wiki/Bison "Bison") • [Boomalope](/wiki/Boomalope "Boomalope") • [Capybara](/wiki/Capybara "Capybara") • [Caribou](/wiki/Caribou "Caribou") • [Cassowary](/wiki/Cassowary "Cassowary") • [Chicken](/wiki/Chicken "Chicken") • [Chinchilla](/wiki/Chinchilla "Chinchilla") • [Cow](/wiki/Cow "Cow") • [Deer](/wiki/Deer "Deer") • [Donkey](/wiki/Donkey "Donkey") • [Dromedary](/wiki/Dromedary "Dromedary") • [Duck](/wiki/Duck "Duck") • [Elephant](/wiki/Elephant "Elephant") • [Elk](/wiki/Elk "Elk") • [Emu](/wiki/Emu "Emu") • [Gazelle](/wiki/Gazelle "Gazelle") • [Goat](/wiki/Goat "Goat") • [Goose](/wiki/Goose "Goose") • [Guinea pig](/wiki/Guinea_pig "Guinea pig") • [Hare](/wiki/Hare "Hare") • [Horse](/wiki/Horse "Horse") • [Ibex](/wiki/Ibex "Ibex") • [Megasloth](/wiki/Megasloth "Megasloth") • [Muffalo](/wiki/Muffalo "Muffalo") • [Ostrich](/wiki/Ostrich "Ostrich") • [Rhinoceros](/wiki/Rhinoceros "Rhinoceros") • [Sheep](/wiki/Sheep "Sheep") • [Snowhare](/wiki/Snowhare "Snowhare") • [Squirrel](/wiki/Squirrel "Squirrel") • [Turkey](/wiki/Turkey "Turkey") • [Yak](/wiki/Yak "Yak") • [Toxalope](/wiki/Toxalope "Toxalope") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Bluebird](/wiki/Bluebird "Bluebird") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Hippo](/wiki/Hippo "Hippo") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Lava snail](/wiki/Lava_snail "Lava snail") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Macaw](/wiki/Macaw "Macaw") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Mastodon](/wiki/Mastodon "Mastodon") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Moose](/wiki/Moose "Moose") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Muskox](/wiki/Muskox "Muskox") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Panda](/wiki/Panda "Panda") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Peafowl](/wiki/Peafowl "Peafowl") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Porcupine](/wiki/Porcupine "Porcupine") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Prairie dog](/wiki/Prairie_dog "Prairie dog") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Quail](/wiki/Quail "Quail") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Sparrow](/wiki/Sparrow "Sparrow") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Swan](/wiki/Swan "Swan") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Dendrovorous](/wiki/Dendrovore "Dendrovore")
    [Alphabeaver](/wiki/Alphabeaver "Alphabeaver") • [Thrumbo](/wiki/Thrumbo "Thrumbo") • [Alpha thrumbo](/wiki/Alpha_thrumbo "Alpha thrumbo") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Omnivorous](/wiki/Omnivore "Omnivore")
    [Boomrat](/wiki/Boomrat "Boomrat") • [Grizzly bear](/wiki/Grizzly_bear "Grizzly bear") • [Human](/wiki/Human "Human") • [Husky](/wiki/Husky "Husky") • [Iguana](/wiki/Iguana "Iguana") • [Labrador retriever](/wiki/Labrador_retriever "Labrador retriever") • [Megascarab](/wiki/Megascarab "Megascarab") • [Megaspider](/wiki/Megaspider "Megaspider") • [Monkey](/wiki/Monkey "Monkey") • [Pig](/wiki/Pig "Pig") • [Polar bear](/wiki/Polar_bear "Polar bear") • [Spelopede](/wiki/Spelopede "Spelopede") • [Raccoon](/wiki/Raccoon "Raccoon") • [Rat](/wiki/Rat "Rat") • [Tortoise](/wiki/Tortoise "Tortoise") • [Wild boar](/wiki/Wild_boar "Wild boar") • [Yorkshire terrier](/wiki/Yorkshire_terrier "Yorkshire terrier") • [Waste rat](/wiki/Waste_rat "Waste rat") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") • [Bog hound](/wiki/Bog_hound "Bog hound") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Monitor lizard](/wiki/Monitor_lizard "Monitor lizard") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Armadillo](/wiki/Armadillo "Armadillo") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Badger](/wiki/Badger "Badger") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Bullfrog](/wiki/Bullfrog "Bullfrog") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Colossus toad](/wiki/Colossus_toad "Colossus toad") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Crow](/wiki/Crow "Crow") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Flamingo](/wiki/Flamingo "Flamingo") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Gorilla](/wiki/Gorilla "Gorilla") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Hermit crab](/wiki/Hermit_crab "Hermit crab") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Heron](/wiki/Heron "Heron") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Hive queen](/wiki/Hive_queen "Hive queen") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Larva](/wiki/Larva "Larva") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Locust](/wiki/Locust "Locust") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Megavole](/wiki/Megavole "Megavole") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Mink](/wiki/Mink "Mink") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Otter](/wiki/Otter "Otter") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Sea turtle](/wiki/Sea_turtle "Sea turtle") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Stone crab](/wiki/Stone_crab "Stone crab") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Carnivorous](/wiki/Carnivore "Carnivore")
    [Arctic fox](/wiki/Arctic_fox "Arctic fox") • [Arctic wolf](/wiki/Arctic_wolf "Arctic wolf") • [Cat](/wiki/Cat "Cat") • [Cobra](/wiki/Cobra "Cobra") • [Cougar](/wiki/Cougar "Cougar") • [Fennec fox](/wiki/Fennec_fox "Fennec fox") • [Lynx](/wiki/Lynx "Lynx") • [Panther](/wiki/Panther "Panther") • [Red fox](/wiki/Red_fox "Red fox") • [Timber wolf](/wiki/Timber_wolf "Timber wolf") • [Warg](/wiki/Warg "Warg") • [Alligator](/wiki/Alligator "Alligator") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Greatwolf](/wiki/Greatwolf "Greatwolf") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Penguin](/wiki/Penguin "Penguin") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Scimitar cat](/wiki/Scimitar_cat "Scimitar cat") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Sea lion](/wiki/Sea_lion "Sea lion") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Seal](/wiki/Seal "Seal") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Tiger](/wiki/Tiger "Tiger") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Vulture](/wiki/Vulture "Vulture") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Walrus](/wiki/Walrus "Walrus") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") • [Wolverine](/wiki/Wolverine "Wolverine") [![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC")

[Dryads](/wiki/Dryads "Dryads")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")
    [Barkskin](/wiki/Barkskin "Barkskin")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Berrymaker](/wiki/Berrymaker "Berrymaker")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Carrier](/wiki/Carrier "Carrier")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Clawer](/wiki/Clawer "Clawer")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Gaumaker](/wiki/Gaumaker "Gaumaker")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Immature dryad](/wiki/Immature_dryad "Immature dryad")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Medicinemaker](/wiki/Medicinemaker "Medicinemaker")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") • [Woodmaker](/wiki/Woodmaker "Woodmaker")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")
  


Retrieved from "[https://rimworldwiki.com/index.php?title=Animal_husbandry&oldid=184272#Taming](https://rimworldwiki.com/index.php?title=Animal_husbandry&oldid=184272#Taming)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Stubs](/wiki/Category:Stubs "Category:Stubs")
  * [Pages to be rewritten](/wiki/Category:Pages_to_be_rewritten "Category:Pages to be rewritten")
  * [Creatures](/wiki/Category:Creatures "Category:Creatures")



Hidden category: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Animal+husbandry "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Animal+husbandry "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Animal_husbandry "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Animal_husbandry "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Animal_husbandry)
  * [Edit](/index.php?title=Animal_husbandry&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Animal_husbandry&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Animal_husbandry "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Animal_husbandry "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Animal_husbandry&oldid=184272 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Animal_husbandry&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Animal-5Fhusbandry)



  * This page was last edited on 2 October 2026, at 18:46.
  * Content is available under [CC BY-SA 3.0](/wiki/RimWorld_Wiki:Copyrights "RimWorld Wiki:Copyrights") unless otherwise noted.


  * [Privacy policy](/wiki/RimWorld_Wiki:Privacy_policy "RimWorld Wiki:Privacy policy")
  * [About RimWorld Wiki](/wiki/RimWorld_Wiki:About "RimWorld Wiki:About")
  * [Disclaimers](/wiki/RimWorld_Wiki:General_disclaimer "RimWorld Wiki:General disclaimer")


  * [![CC BY-SA 3.0](/resources/assets/licenses/cc-by-sa.png)](https://creativecommons.org/licenses/by-sa/3.0/)
  * [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)[![Powered by Semantic MediaWiki](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAfCAMAAABUFvrSAAACJVBMVEXe3t62trbLy8vGxsbAwMDX19e6urqsrKxHcEzQ0NC2tratra2oqKixsbHd3eDFxcXe3t7U1NTa2trX19fQ0NDV1dWNjY2dnZ2UlJSUlJTS0tKUlJSWlpbR0dGenp79/f38/Pz+/v7t7e3v7+/u7u7s7Oz19fX29vb6+vr7+/vz8/Pz8/P4+fnw8PD39/gWTq/09PX6+vktX7b/sg8XT7F6mc/f5OwhVrNvkMthhsfT2+j7rQ/M1eZqjcmFotPs7e9Cb722xuFResK/zOObstnu7/Grvd3M1+mNqNY6aLoaUbEaUbZWfsTk6fE2Zrnp7O8bTq0kWLQuYcpcg8Xh5/Byk83a4eukud1/nM+6yeQkWcGwwuDxnRQyYrigttvI0+gpW7XGyttLdsBni8geVLo0Z9XlkCPb4u+QqtcfVLLo7PNHcr73phFGX6HsmBnpkxg6bNwnXcbX3er19vnr7/SVrdhuhLl+j70vVqY6Xqv0oxJVcbQhV76DjKTz9ffQ2evE0OZAbbzu7/PS1uFufrDnrGgpSZjy8/SQnMFddrKuekXSiCsgTKRaaZHejy9yang3VptNaqspWbnmliy3j2/m6OzT3e7x8fL4+v3p6uwaN2re0cifqLiLiZWYhYGYb0xXYn+5g0xwiMKYpc2BcHZmW2srRXpGWIhecKfilz4+WID2+PyosMywqbGqss1aVnLZq33p1sGklZqrp7dkfr7CpY9yg59Ud6QZAAAAH3RSTlPfBN/f39/f2wDf39vV3/7N2rrEz5D5c8ONuHaPuXXDImoxqwAABO1JREFUSMe1kQdz01gQgBXaBS4w9OtHwMFSdPKTUNxkW+61xN2Je4tLHJNOGukkAUINJTzaUIbO9fr7TpLtS44DZiC5b6Sn3dW+TysJaWz4cv9eZFPZu/+bhkakYR88WqP59u3vjxzdDCT7GpCD4qNH3sEGzOhB5MCR/4PmA8j25uZ33t0A23lxff5hZTIzOrz2Ph8qK936l7i1tT7hk8DAoHNsbeLWKjPdQcZ+qvX9tHMNXca1XBDXHtL6x2Bh0HWtuXUo8oTgC1gVpcdsdpew92PUYtjwzFq+E9mJYfXxx1x5l2/l5Vhy0DW6TuyQCZcR2hnswXJM0h+203471u5WKMIE5mDpspIIO8sZTMZiIbczY6+JCaI+/sJZ38qjP28+nQjkx/mcqGJ26rW3iKg/fYphCL1jNk5WbqXI0nBnu00RJ2j9bNRp6MmFS0SYIXLuUlQ5w22qizHr5MTyy2u/3XxVvHHlwtWVa/xTCQIIlEaMzrgswzA5P9BrAciYASqNoiNdjL8b0GYAHN3AGAEgzPSQc9UtYCeyBQAMO2G9PhhzXfp9qdifSCT6Lj788QQnrvWEuNPI2um0LW0D+m4A6E4AnIZOeq7ksQuJvi6eUXRW+8EWXsxNPhkYGJiSXr7Rd1qtVp9MXHkgIurzAkdFxjrj7cmKbN4K5v8RGxT2sJMTpwBflNHhUJgBdoUylzy3TuwIDBRi0hf9p9VtbW3qk30X7q2Je1IybZq7mLVWFKTSADXPoqi9AzVorda0kKTS6KkRbSgaR1GT1h5CObYiW1GU27yc5z6F9Fn/yTYedeLi9AIA6AbgxGIxAMPZcZeUHH9cFavVfY97FaNA/DbazRZVV89/61at2BTlg1JXiFtrYoBmRyd7p6/UP0XxaSDmy4pt0jmuh8qx6wQ2MmRz18TaJCUWO9xisUVhMMsoZZDiGHLLuXUbso2iatP/1HvhYu3n3bh6Pe/LUjZSj1NUJ8lSlNwahRRlMRjmyFDICikVn8+SacomdbZTVj+0mQSxweS1WqpiHK/Ncubs858f9idOJ/qKS1cv+RbFuIbMmHEvTbO4QeF25CxyD62nSbmJ1MUzRrpiwR0RPBJMpnCGxWVGXBn8TkarNGQHjuPrxOeWY4GY9FmxWHy19Gvv+ayYF6f8oYi7i8U93bjFkYokvbhWEFu8Og2ZxrUe3NMpc3vLhqqYpVV4XbwDQkpgoVwYKOR9N5d+eXB5vJevQA0pD7oVqi4WOj16vX6EYSA08WKvyeOZJw1cQ6rsnXOa/RYoM0Kls0zLuVoHhHAHL8YFXkwVCoE8uXhvMVCY8mW5Ci8eKkcgJ9azOl0UajNDFiUpj5JeloEqTgwd/iCUJP0sFMSejkpO96b4zl1fPuYiyd6Vs4GBmHSsJoYmLy/WeBTlis5rlJYrgjhe1s+XOXGEtHJOMl4VB2EHLauKdyG7JBLIc//uslRKkhOrcGJqyiU9z5UkOpVOwiGXSyQizRAfqlRc7Y5KJFnV6FReiWSV7xAWeQd/SOSq6qY18eVHq4vjlyazEJ73ScmJPVxJVKdF9MFwYpFIEL+ehvDOcSH8YXRsAa4XfwS7kd0tLfw7Sp7fl7xJywbYjTTVotfTb+849lEcb0K+2lMN/5o+tons+Rxp+PrQ8U3n0BcNSGPj4W+bPuX5ZLNo+uxwY+PfoLJHX1KXgyMAAAAASUVORK5CYII=)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)


  *[]: Buildings and items made with this as stuff will have the color RGB: (174,219,228)
  *[°C]: Celsius
  *[°F]: Fahrenheit
  *[28.33 secs]: real-time at 1x speed
  *[Nutrition]: Nutrition gained when this item or object is eaten
  *[Maximum To Ingest]: Maximum Number To Ingest At Once
  *[1.33 secs]: real-time at 1x speed
  *[+4]: Stacking 3 times with a 0.5 multiplier for maximum of 7
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
  *[−6]: Stacking 5 times for a maximum of -30
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
  *[MTB]: mean time between
  *[5 secs]: real-time at 1x speed
  *[15 secs]: real-time at 1x speed
  *[4.17 mins]: real-time at 1x speed
  *[25 mins]: real-time at 1x speed
  *[41.67 mins]: real-time at 1x speed
  *[+6]: Stacking 3 times with a 0.5 multiplier for maximum of 11
  *[_Bonded animal'smaster_]: Being together with my bonded animal makes me feel better.
  *[_Not bonded animal's master_]: I should be together with my bonded animals.
  *[−10]: Stacking 300 times for a maximum of -3000 or 10 times for a maximum of -100 for the same other pawn
  *[_Bonded animal given away_]: My special bonded animal was given away!
  *[−8]: Stacking 5 times for a maximum of -40
  *[_Bonded animal died_]: Such a tender, unique animal. This universe is evil!
  *[_Bonded animal lost_]: Such a tender, unique animal. This universe is evil!
  *[_Bonded animal banished_]: My bonded animal was banished!
  *[−5]: Stacking 5 times for a maximum of -25
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
  *[−4]: Stacking 10 times for a maximum of -40
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
  *[3 secs]: real-time at 1x speed
  *[4.8 secs]: real-time at 1x speed
  *[34.33 secs]: real-time at 1x speed
  *[31.67 secs]: real-time at 1x speed
  *[11.73 secs]: real-time at 1x speed
  *[29 secs]: real-time at 1x speed
  *[10.13 secs]: real-time at 1x speed
  *[3.73 secs]: real-time at 1x speed
  *[_Insulted_]: I've been directly insulted! What an awful person!
  *[_Unsettling conversation_]: An unsettling conversation made me very creeped out. Nobody should think or speak of such things.
  *[7 secs]: real-time at 1x speed
  *[Rescued me]: Rescued by stranger: I was rescued by someone! I almost thought I was done for back there. I'm so thankful.
  *[Sold my loved one]: Someone I love was sold to a trader like a piece of meat!
  *[Gave away my bonded animal]: My special bonded animal was given away!
