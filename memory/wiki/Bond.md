Animal husbandry - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Animal husbandry

 
 From RimWorld Wiki

 (Redirected from Bond)

 

 
 

 Jump to navigation
 Jump to search
 For a more general overview, see Animals.

All animals in Rimworld can be tamed, providing certain benefits to the colony. Some animals can be trained, others require enclosed spaces (pen) to remain in the colony, and yet others can lose their tame state if left alone for too long.

Any animal that requires a pen to remain on the colony is considered a farm animal and can't be trained&#91;1&#93;. Farm animals don't lose tameness due to wildness.

Contents

- 1 Acquisition

- 1.1 Taming

- 1.1.1 Tame chances

- 1.1.2 Minimum skill

- 1.2 Starting pets

- 1.3 Buying

- 1.4 Events

- 2 Interactions

- 2.1 Naming

- 2.2 Nuzzling

- 2.3 Bonding

- 2.4 Training

- 2.5 Combat

- 2.6 Slaughtering

- 2.6.1 Auto-Slaughter

- 2.7 Other Interactions

- 2.7.1 Caravans

- 2.7.2 Release to Wild

- 2.7.3 Social

- 2.7.4 Trade goods

- 3 Products

- 3.1 Eggs

- 3.2 Milk

- 3.3 Wool

- 3.4 Chemfuel

- 4 Feeding

- 4.1 Grazing wild plants

- 4.2 Growing haygrass

- 4.3 Making kibble

- 4.4 Corpse freezer

- 5 Raising

- 5.1 Pens

- 5.2 Pet care

- 6 Butchering

- 7 Notes

- 8 Version history

Acquisition[edit]

There are five options to obtain tamed animals. Having them as starting pets, taming wild animals, buying them from traders, having them birth offspring, and getting them from events.

Taming[edit]

Wild animals can be tamed by an animal handler with sufficient Animal skill and available food. Tamed animals may be bred, trained, traded, slaughtered, or farmed.

Wild animals may be marked for taming using the Tame order.

An animal handler will attempt to tame marked animals using non-meal, non-drug food fitting that animal's diet. The chance to tame an animal depends on the animal's wildness (displayed on the info window) and the handler's 'Tame animal chance' stat. This stat is determined by the colonist's animals skill, manipulation, talking, and hearing. When a handler fails to tame an animal there is a cooldown period of 30,000&#160;ticks (8.33&#160;mins), or 12 in-game hours, before another attempt can be made. There is also a chance it will turn manhunter and start attacking the handler and others. The revenge chance is shown on the Wildlife menu. After a while the handler may drop unused food.

Tamed animals will wander around the map until they are lead to a pen with a pen marker, for pen animals, or restricted to a designated area, for all other animals. Restricting non-pen animal movement using areas is usually necessary to prevent unwanted food consumption and animal filth.

Tame chances[edit]

For the calculation details, see Tame Animal Chance.

Besides the animal handler's own skill, the wildness of the animals also counts.

Tame chances undergo a post-processing curve.

- An animal with 0% wildness has a x2 taming chance.

- An animal with 50% wildness has normal taming chance.

- An animal with 100% wildness cannot be tamed at all.

The net effect of the curve above is the expression 2*(1-wildness). The minimum value it can take is 0 at 100% wildness while the max is 2(duplicates chance) at 0% wildness.

Currently, the hardest to tame animal is the alpha thrumbo. Assuming 20 Animal skill, the base taming chance is 1.28%.

Animals with 0% wildness remain tame forever. If wildness is above 0% (shown on the wildlife tab), the animals requires maintenance to not revert into its wild state. Farm animals will remain tamed regardless of wildness.

Minimum skill[edit]

For the calculation details, see Minimum Handling Skill.

Most animal species have a Minimum handling skill stat which determines the Animal skill necessary of a handler pawn. The game will briefly produce a warning message if no colonist has enough skill to handle the animal.

Any animal with 0% wildness can be handled even with 0 skill. This list includes but is not limited to: Cat, Chicken, Cow, Donkey, Duck, Goat, Husky, Labrador retriever, Pig, Sheep, Yorkshire terrier, Barkskin dryad, Berrymaker dryad, Carrier dryad, Clawer dryad, Gaumaker dryad, Immature dryad, Medicinemaker dryad, Woodmaker dryad.

The highest minimum skill required by any animal in Core is 10, which is required by both the Megasloth (97% wildness) and Thrumbo (98.5% wildness). This increases to 14 with the DLC enabled, such as the alpha thrumbo.

Starting pets[edit]

For most scenarios, new colonies will include a random pet that is already tamed. These pets will have a random name and are sometimes bonded with a pawn. The animals available are determined by the handling skills of the starting pawn(s), as the game will not provide a pet that cannot be handled by the colony. This rule is broken when all colonists have animal handling disabled, as the game will still provide animals that require periodic taming.

The chance of getting an animal is influenced by the "petness" stat, with a higher value resulting in a higher chance. The selection of animals also influences the chances, for example a Husky has a 21.74% chance of being selected with the highest handling skill at 0, while at level 10+ the chance is only 11.06% (assuming all DLCs are active). Hares, snowhares, capybaras and cobras are all under 1% chance due to the petness being so low and the animal handling being so high.

- 

Animal

Handling skill
required

Petness

Chance with max handling skill:

0
2
3
4
5
6
8
9
Max

Arctic fox

8

0.1

-

-

-

-

-

-

1.14&#160;%

1.12&#160;%

1.11&#160;%

Arctic wolf

9

0.1

-

-

-

-

-

-

-

1.12&#160;%

1.11&#160;%

Boomrat

8

0.2

-

-

-

-

-

-

2.29&#160;%

2.24&#160;%

2.21&#160;%

Capybara

8

0.08

-

-

-

-

-

-

0.92&#160;%

0.89&#160;%

0.88&#160;%

Cat

0

1

21.74&#160;%

19.61&#160;%

17.54&#160;%

17.39&#160;%

15.75&#160;%

12.74&#160;%

11.44&#160;%

11.19&#160;%

11.06&#160;%

Chinchilla

6

0.2

-

-

-

-

-

2.55&#160;%

2.29&#160;%

2.24&#160;%

2.21&#160;%

Cobra

8

0.05

-

-

-

-

-

-

0.57&#160;%

0.56&#160;%

0.55&#160;%

Donkey

0

0.6

13.04&#160;%

11.76&#160;%

10.53&#160;%

10.43&#160;%

9.45&#160;%

7.64&#160;%

6.86&#160;%

6.71&#160;%

6.64&#160;%

Fennec fox

8

0.1

-

-

-

-

-

-

1.14&#160;%

1.12&#160;%

1.11&#160;%

Guinea pig

6

0.3

-

-

-

-

-

3.82&#160;%

3.43&#160;%

3.36&#160;%

3.32&#160;%

Hare

8

0.08

-

-

-

-

-

-

0.92&#160;%

0.89&#160;%

0.88&#160;%

Horse

3

0.6

-

-

10.53&#160;%

10.43&#160;%

9.45&#160;%

7.64&#160;%

6.86&#160;%

6.71&#160;%

6.64&#160;%

Husky

0

1

21.74&#160;%

19.61&#160;%

17.54&#160;%

17.39&#160;%

15.75&#160;%

12.74&#160;%

11.44&#160;%

11.19&#160;%

11.06&#160;%

Iguana

5

0.15

-

-

-

-

2.36&#160;%

1.91&#160;%

1.72&#160;%

1.68&#160;%

1.66&#160;%

Labrador retriever

0

1

21.74&#160;%

19.61&#160;%

17.54&#160;%

17.39&#160;%

15.75&#160;%

12.74&#160;%

11.44&#160;%

11.19&#160;%

11.06&#160;%

Monkey

6

0.5

-

-

-

-

-

6.37&#160;%

5.72&#160;%

5.59&#160;%

5.53&#160;%

Rat

5

0.15

-

-

-

-

2.36&#160;%

1.91&#160;%

1.72&#160;%

1.68&#160;%

1.66&#160;%

Red fox

8

0.1

-

-

-

-

-

-

1.14&#160;%

1.12&#160;%

1.11&#160;%

Snowhare

8

0.08

-

-

-

-

-

-

0.92&#160;%

0.89&#160;%

0.88&#160;%

Timber wolf

9

0.1

-

-

-

-

-

-

-

1.12&#160;%

1.11&#160;%

Warg

6

0.5

-

-

-

-

-

6.37&#160;%

5.72&#160;%

5.59&#160;%

5.53&#160;%

Yak

2

0.3

-

5.88&#160;%

5.26&#160;%

5.22&#160;%

4.72&#160;%

3.82&#160;%

3.43&#160;%

3.36&#160;%

3.32&#160;%

Yorkshire terrier

0

1

21.74&#160;%

19.61&#160;%

17.54&#160;%

17.39&#160;%

15.75&#160;%

12.74&#160;%

11.44&#160;%

11.19&#160;%

11.06&#160;%

Waste rat

5

0.15

-

-

-

-

2.36&#160;%

1.91&#160;%

1.72&#160;%

1.68&#160;%

1.66&#160;%

Bullfrog

8

0.05

-

-

-

-

-

-

0.57&#160;%

0.56&#160;%

0.55&#160;%

Greatwolf

10

0.1

-

-

-

-

-

-

-

-

1.11&#160;%

Macaw

2

0.2

-

3.92&#160;%

3.51&#160;%

3.48&#160;%

3.15&#160;%

2.55&#160;%

2.29&#160;%

2.24&#160;%

2.21&#160;%

Megavole

4

0.05

-

-

-

0.87&#160;%

0.79&#160;%

0.64&#160;%

0.57&#160;%

0.56&#160;%

0.55&#160;%

Monitor lizard

5

0.15

-

-

-

-

2.36&#160;%

1.91&#160;%

1.72&#160;%

1.68&#160;%

1.66&#160;%

Scimitar cat

8

0.05

-

-

-

-

-

-

0.57&#160;%

0.56&#160;%

0.55&#160;%

Buying[edit]

Main article: Trade

Animals bought from traders are always tamed. Different types of traders have different kinds of animals in stock.

Events[edit]

Main article: Events

The events animals join and animal self-tamed give your colony tamed animals.

Interactions[edit]

Some animal species can be trained by colonists. With Guard trained, they will follow their master around if designated to do so. 

Some species may be harvested to produce milk, chemfuel, or wool. Still others passively lay frequent eggs.

When injured, they will go to animal sleeping spots/ beds for rest and treatment.

Naming[edit]

Newly tamed or purchased animals are distinguished by numerical designations(“Muffalo 1”, “Muffalo 2”, etc.). When an animal forms a bond with a colonist, it is given a unique name. Names can be changed by the player from the "Training" tab in the inspect pawn pane. Names of tamed animals are not shown on the map unless the option is turned on, via Menu, Options, 'Show animal names'.

Animals may have a gender-specific name (i.e. hen, rooster, buck, doe), or a lifestage-specific name (piglet, puppy), or even a gender/lifestage-specific name (cockerel).

It is possible for animals which have been lost or sold to reappear later as part of a wild herd. This will only happen with animals which occur naturally on your colony's biome. They will still have the name you gave them (including automatic names like "Muffalo 2"), but will need to be tamed and trained again.

Nuzzling[edit]

Occasionally, some animals can nuzzle colonists, giving the colonist +4 Nuzzled thought for 1 day or +6 Nuzzled thought for 1 day [test]. Animals can nuzzle anyone regardless of handling skill unless they are a psychopath or inhumanized .

The following animals can nuzzle:

- 

Animal
Nuzzle MTB in hours

Cat

12

Guinea pig

24

Husky

12

Labrador retriever

12

Monkey

24

Yorkshire terrier

12

Bog hound

72

Megavole

72

Panda

48

Seal

24

Bonding[edit]

Animals may bond with their handlers or doctors, and starting pets have a chance to start the game bonded with a random starting colonist. A bond gives the following mood effects to non-psychopathic or inhumanized pawns. All moodlets stack with each other.

- +5 Bonded animal's master thought

- −3 Not bonded animal's master thought

- −10 Bonded animal given away thought for 60 days. This will also inflict −10 opinion of the pawns that performed the action for 60 days.

- −8 Bonded animal died thought for 20 days. This will also inflict −10 opinion of the pawns that performed the action for 60 days.

- −8 Bonded animal lost thought for 20 days

- −6 Bonded animal banished thought for 6 days

- −5 Bonded animal released thought for 15 days

Bonds can occur when:

- When an animal has its wounds tended by a colonist, there is a constant 0.4% chance that the animal will bond with the colonist, regardless of Animals skill. If the animal is wild, the animal will instantly self-tame, disregarding wildness.

- When tamed, an animal also has a 1% chance to bond with the tamer.

- When successfully trained, an animal has a 0.7% chance to bond with the trainer.

- Every 2,500&#160;ticks (41.67&#160;secs), if an animal is within 12 tiles and has line of sight to their master, there is a 0.1% chance to bond.

- For starting animals, the&#160;% to start bonded with an owner appears to be related to the innate wildness (i.e. horses and camels will start bonded more often than cobras or wargs). Domestic animals (wildness 0 - dogs, cats, some farm animals) will always start bonded.

Pawns with the Animal connection: Strong precept in their ideoligion have a ×2 multiplier on bonding chance. 
Pawns with the Bonding: Disapproved precept in their ideoligion cannot be bonded with, but they will not lose existing bonds, nor their mood effects, if the precept is added via a fluid ideoligion's reformation. Pawns converted into a non-bonding ideoligion will renounce all their bonds at the moment of conversion.

Bonded animals are also easier for their master to train (5x multiplier on chance). Animals are given a unique name upon bonding.

On the death of the pawn an animal is bonded with, it can go into one of two animal mental breaks; manhunter, in which it will attack all nearby entities, or confusion, in which it will wander around, uncontrollably, similar to dazed humans.

Training[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: Odyssey training effects.

Tamed animals may be trained depending on their trainable intelligence. Click the animal's training tab to specify training targets and view progress.

The stats of the training pawn, including Animals skill or Global Work Speed, have no effect on how fast each training session is completed. Instead, increased skill improves a pawn's Train Animal Chance, resulting in the animal requiring fewer training attempts in the first place. After a training attempt on a tamed animal, there is a 6 in-game hour waiting period before that same animal can be trained again.

Once Guard is trained, they can be assigned a master which they will follow. You can configure when the animal will follow their master, by toggling whether or not the animal will follow while doing field work (hunting/taming), or while drafted, from the Animals menu.

Many skills require multiple steps to fully train. Guard has three steps, rescue and attack have two, and haul has seven. An animal also has five stages of tameness to maintain.

Animal skills decay over time. The speed of decay ranges from 720,000&#160;ticks (12&#160;in-game days) at 0% wildness to 360,000&#160;ticks (6&#160;in-game days) at 100% wildness. Any animal with over 10.1% wildness can additionally lose the tamed status unless it is a pen animal. For this reason, if you do not have handlers meeting the animal's minimum handling skill, it is best to sell or slaughter before your animal returns to the wild.

When an animal skill decays, one point of training is subtracted from one of the 'outermost' skills at random, ie: skills with no trained dependents. 'Guard' will always remain trained until all its dependent skills have fully decayed, and only after Guard is decayed can an animal lose tameness.

Orders Table

Orders
Training 
intelligence
 required
Steps
Description

Guard

Simple
3
An animal trained in guard will follow its master and attack nearby aggressors. An animal's master is listed on the Training tab and on the Animals menu. Multiple animals may be assigned to a single master. 
Note that assigning an animal to the pawn it is bonded with will give that pawn a permanent +5 moodlet, and if a bonded animal is not assigned to its bonded pawn, that pawn gets a permanent −3 moodlet. Mood effects stack with multiple bonded animals, and one pawn can have both the positive and negative moodlets from two bonded animals

Attack

Intermediate
5
Using the 'attack' command, animals may leave their master's immediate area to attack enemies. When the 'Animals Attack' command is turned off, animals will guard their master and only attack enemies nearby.

Rescue

Advanced
2
Animals trained in rescue will rescue its master as well as nearby colonists in a radius of 75. Only species of sufficient size can rescue.

Haul

Advanced
7
Animals trained in hauling will haul just as colonists do, although each species has a specific carrying capacity according to its size. Only species of sufficient size can haul, but this requirement is lesser than for rescuing. 
Animals will perform hauling intermittently with an MTB of 1.5 hours. Apart from being able to move, animals also need an intact jaw in order to haul. Animals will only haul within their allowed area if they are assigned to one.

Animal
Move Speed
Carrying Capacity
Haul Throughput
Wildness
Hunger Rate
Filth Rate
Juvenile Age
Maturity Age
Min Temperature
Max Temperature

Alpha thrumbo

6

375

2250

99%

2.8

8

45

79.92

-65

50

Arctic wolf

5

64

320

85%

0.29

2

12

30

-55

40

Carrier dryad

2.4

50

120

0%

-

1

-

-

-50

50

Cougar

5

75

375

80%

0.32

2

15

30

-25

40

Elephant

4.8

300

1440

75%

2.57

24

18

39.96

-12

50

Gorilla

4.7

150

705

60%

0.86

4

12

15.96

-10

50

Greatwolf

5.5

112

616

95%

0.64

2

12

30

-50

40

Grizzly bear

4.6

161

740.6

80%

0.56

4

12

30

-40

40

Hive queen

3.4

337

1145.8

99%

-

28

-

-

-40

40

Husky

5

64

320

0%

0.8

1

15

30

-50

40

Labrador retriever

5

56

280

0%

0.64

1

15

30

-30

40

Mastodon

4.7

337

1583.9

75%

2.88

24

18

39.96

-55

40

Megasloth

4.8

300

1440

97%

1.6

24

19.98

40.02

-55

40

Megaspider

3.6

90

324

40%

0.56

1

1.8

12

-40

60

Panther

5

75

375

80%

0.32

2

15

30

-8

50

Polar bear

4.6

161

740.6

85%

0.56

4

12

30

-55

40

Scimitar cat

6

97

582

80%

0.42

2

15

30

-40

40

Sea lion

2.8

90

252

50%

0.48

8

6

19.98

-40

40

Seal

2.6

60

156

50%

0.48

6

6

19.98

-20

40

Spelopede

3.65

60

219

30%

0.4

1

1.8

12

-25

60

Thrumbo

5.5

300

1650

98%

2.8

8

45

79.92

-65

50

Tiger

5.2

105

546

90%

0.32

1

15

30

-8

50

Timber wolf

5

64

320

85%

0.29

2

12

30

-40

40

Attack target 

-
2

The following animals can be trained to Attack Target: Arctic wolf, Cougar, Grizzly bear, Megaspider, Panther, Polar bear, Timber wolf, Warg, Crow, Greatwolf, Scimitar cat, Tiger
Command the animal to attack a specific target
&#8212;&#160;Attack Target description

Comfort

-
2

The following animals can be trained to comfort: Cat, Husky, Labrador retriever, Yorkshire terrier, Panda, Seal
The animal will be more emotionally supportive. It will nuzzle more often, and make your colonists happier when it does so.
&#8212;&#160;Comfort description

Forage

-
3

See also: Foraging

The following animals can be trained to forage: Pig, Raccoon, Wild boar, Gorilla, Locust

"The animal will occasionally find berries, mushrooms, or food. Animals will find more food in biomes with higher forageability. Foraging can only be done on fertile terrain."
&#8212;&#160;Foraging description

Dig

-
3

The following animals can be trained to dig: Megasloth, Spelopede, Megavole
The animal will mine rock designated for mining. Animals are generally slow and inefficient at mining.
&#8212;&#160;Dig description

War trumpet

-
2

The following animals can be trained to War Trumpet: Elephant, Mastodon
Command the animal to release a powerful roar. This has a chance to cause hostile humans and animals to tremble in fear, reducing their movement speed and manipulation.
&#8212;&#160;War Trumpet description

Thrumbo roar

-
2

The following animals can be trained to Thrumbo Roar: Thrumbo
Command the thrumbo to release a deafening roar. This has a chance to cause hostile humans and animals to tremble in fear, reducing their movement speed and manipulation.
&#8212;&#160;Thrumbo Roar description

Terror roar

-
2

The following animals can be trained to Terror Roar: Alpha thrumbo
Command the alpha thrumbo to release a deafening roar. This has a chance to send nearby hostile humans and animals fleeing in terror.
&#8212;&#160;Terror Roar description

Sludge spew

-
2

The following animals can be trained to Sludge Spew: Larva
Command the larva to spray an acidic sludge all over the target area. Once trained, larva will only spew sludge when commanded.
&#8212;&#160;Sludge Spew description

Egg spew

-
2

The following animals can be trained to Egg Spew: Hive queen
Command the queen to launch an egg sac and a spray of acidic sludge at the target area. Once trained, the queen will only produce eggs when commanded
&#8212;&#160;Egg Spew description

Combat[edit]

Once Guard is trained, animals will gather around their master upon drafting, and will attack nearby threats, or (unintentionally) block ranged attacks for their master. This is configurable and can be disabled by disabling follow during drafted.

With Attack trained, animals can be released to attack threats from a distance. Even colonists incapable of Violence can send their assigned animals into battle.

Animals can be downed during combat, and can be rescued by colonists or other animals capable of Rescue.

Slaughtering[edit]

This section is a stub. You can help RimWorld Wiki by expanding it. Reason: This section is included in the Butchery project - there are a number of factors that are in need of verification and potentially addition to this section. See that page for details.

 Tamed animals may be slaughtered selecting the animal and clicking the Slaughter button, or by using the Slaughter tool from the Orders menu. An animal marked in this way will be slaughtered by an animal handler. The handler need not be equipped with a weapon but must be capable of violence. This job takes&#160;???[How long?] to perform and instantly kills the animal - the animal will not resist, flee, or fight. You can also set up an auto-slaughter order in the animals tab, configurable to limit the amount of male, female, and pregnant animals in a pen.

Animals killed through damage suffer a 66% multiplier to Meat Amount and Leather Amount. Slaughtering, throat slitting a downed-but-not-injured animal as a hunting task, the "euthanize by cut" operation, and the Animal Sacrifice ritual all result in a careful slaughter and avoid the 66% modifier.

If you try to slaughter a bonded animal, the game will warn you about it due to the mood impact this has on the animal's master.

Auto-Slaughter[edit]

 
Auto-slaughter menu

Via the Animals button on the bottom bar is a "Manage auto-slaughter.." option. Auto-slaughter allows the player to automatically cull animals above a defined threshold. 

Total Animals, Male/Female Adults, Male/Female Young are all definable amounts that the player can set. If the current animal count exceeds any of the defined amounts in any of these columns the eldest allowed animal of that exceeded type is slaughtered. These 5 left-most columns function as OR operators. The two rightmost columns allow the player to allow the slaughtering of pregnant or bonded animals if desired.

Other Interactions[edit]

Caravans[edit]

Main article: Pack animal

These animals can graze, meaning they don't usually require food during a caravan. (This may not be true when traveling across cold or inhospitable biomes, like tundra or deserts, or in winter in general.) When carrying items in their inventory, they will appear to have packs on, which disappear when unloaded.

Release to Wild[edit]

Unwanted animals can be released to the wild using a command next to the slaughter button. Releasing bonded animals also causes a mood debuff to master of the animal.

Social[edit]

Each animal has a Social tab that lists that animal's human bonds and familial relations. Clicking an entry jumps to that bond's counterpart on the map. Animals, even wild ones, have a small chance of bonding with a colonist everytime they interact. Bonded animals are given a unique name by their Master. Animals assigned to Guard a bonded human will give their master a permanent +5 mood thought. Humans who are not the master of their bonded animal receive a -5 "Not bonded animal's master" thought. Animals do not have a mood meter. Humans may have more than one bonded animal, but animals may only have one human bond.

Trade goods[edit]

Tamed animals may be sold to traders. Animals purchased from traders will be already tamed. Bulk goods traders offer pets and farm animals while exotic goods traders carry most of the wild species. Traders offering animals will attempt to at least carry a breeding pair of a core farm animal.

Products[edit]

Certain tame animals produce eggs, milk, wool, or chemfuel. Milking (including chemfuel) and shearing sometimes fails, which is indicated with a brief "product wasted" message. This and the amount of wool, milk or chemfuel respectively is dependent on the Animal Gather Yield stat of the pawn.

Eggs[edit]

Main article: Eggs

- 

Animal
Fert. Egg
Unfert. Egg
Can lay
unfertilized
Nutrition
per Egg
Avg Eggs
per Clutch
Laying
Interval
Avg Eggs
per Day
Egg Nutrition
per Day
Needed
Males / Female
Daily Hunger
Rate
Daily Egg Nutrition
per Hunger

Cassowary

0.5

1

3.33 days

0.3

0.15

0.33

0.6

0.25

Chicken

0.25

1

1 days

1

0.25

0

0.22

1.14

Cobra

0.25

1.5

10 days

0.15

0.04

0.11

0.12

0.31

Duck

0.25

1

1 days

1

0.25

0

0.28

0.89

Emu

0.5

1

3.33 days

0.3

0.15

0.33

0.6

0.25

Goose

0.5

1

2 days

0.5

0.25

0

0.45

0.56

Iguana

0.25

1.5

5.661 days

0.26

0.07

0.19

0.38

0.17

Ostrich

0.6

1

3.33 days

0.3

0.18

0.33

0.89

0.2

Tortoise

0.25

2

6.66 days

0.3

0.08

0.17

0.15

0.49

Turkey

0.5

1

1.333 days

0.75

0.38

0.83

0.82

0.46

Alligator

0.5

1.5

12 days

0.13

0.06

0.09

0.52

0.12

Bluebird

0.25

1

3 days

0.33

0.08

0.25

0.16

0.51

Crow

0.25

1

3 days

0.33

0.08

0.37

0.18

0.47

Flamingo

0.5

1

2 days

0.5

0.25

0.55

0.7

0.36

Heron

0.5

1

2 days

0.5

0.25

0.55

0.7

0.36

Macaw

0.25

1

8 days

0.13

0.03

0.09

0.21

0.15

Monitor lizard

0.25

1

6 days

0.17

0.04

0.18

0.38

0.11

Peafowl

0.25

1

2 days

0.5

0.13

0.55

0.57

0.22

Penguin

0.5

1

2 days

0.5

0.25

0.55

0.7

0.36

Quail

0.25

1

1.3 days

0.77

0.19

0.57

0.3

0.64

Sea turtle

0.5

1.5

6.66 days

0.23

0.11

0.17

0.19

0.6

Sparrow

0.25

1

3 days

0.33

0.08

0.25

0.16

0.51

Swan

0.25

1

2 days

0.5

0.13

0.37

0.62

0.2

Vulture

0.25

1

4 days

0.25

0.06

0.28

0.47

0.13

Milk[edit]

Main article: Milk

- 

Animal
Milk Amount
Milking
Interval
Milk/Day
(Average)
Milk / food consumed
per day
Nutrition / food consumed
per day

Caribou

10
2
5
11.36
0.57

Cow

14
1
14
16.28
0.81

Dromedary

18
2
9
10.47
0.52

Elk

11
1
11
12.79
0.64

Goat

12
3
4
11.11
0.56

Yak

11
1
11
12.79
0.64

Wool[edit]

Main article: Wool

Animal
Wool Name
Wool Amount
Shearing Interval
Daily Wool Average

Alpaca

Alpaca wool
45
10
4.5

Bison

Bison wool
120
15
8

Megasloth

Megasloth wool
200
20
10

Muffalo

Muffalo wool
120
15
8

Sheep

Sheep wool
45
10
4.5

Mastodon

Mastodon wool
200
20
10

Muskox

Muskox wool
120
15
8

Chemfuel[edit]

Main article: Chemfuel

Animal
Chemfuel Amount
Milking Interval
Daily Chemfuel Average

Boomalope

11
1
11

Feeding[edit]

Grazing wild plants[edit]

Letting your animals graze is one of the easiest way to feed your herbivorous, omnivorous grazer and dendrovorous animals. While the later can only "graze" live trees, the former two can eat all other living plants. Depending on the animals in the colony it might therefore be beneficial to cut all trees or other plants respectively in the grazing area.

The simplest way to feed non-strictly-carnivorous animals is to create a large pen where animals can graze on the wild grass and brambles. The pen marker will show the number of animals the wild plants can sustain (measured in cows, goats, and chickens. When the weather is too cold or too hot though, plants grow slower or even stop growing. Furthermore, plants become totally inedible when the temperature drops below -10&#160;°C (14&#160;°F), because they all are considered leafless, grass as well as trees. This mechanic is not explained in-game, and is quite puzzling to unaware players. It looks like animals starve on top of good-looking grass. See Plants for more info.

While grazing might need the least amount of work, it can also be highly inefficient for smaller animals. Most wild plants have 0.5 nutrition (except the rather uncommon Agave,&#160;Astragalus,&#160;Bryolux,&#160;Chokevine,&#160;Low shrubs,&#160;Pincushion cactus,&#160;Wild healroot,&#160;Fireweed,&#160;Magma cactus). The amount of nutrition an animal can hold is dependent on its body size and its life stage. They will start eating as soon as they hold less than 25&#160;% of the maximum nutrition they can hold (see saturation for more info). This means all adult animals with a body size below 0.67 will start eating before they can fit the full 0.5 nutrition of most plants, with the excess getting wasted. This is even more pronounced for baby and juvenile animals since they are smaller. Only species that have an adult body size of at least 0.89 will not be overeating when juvenile and with an adult body size of at least 1.11 as babies as well.

Growing haygrass[edit]

While the land can sustain a sizable population of animals grazing on it, it doesn't have an infinite supply and can still be depleted. Winter can also stop grass growth, leaving nothing for your grazing animals to eat. 

If you need to raise a lot of animals, e.g. an exponentially growing flock of chickens, you will need to grow haygrass to sustain them all. You also need to have a stock of haygrass to keep animals fed through the winter.

Haygrass gives a total of 0.9 nutrition (18 units of hay) when fully grown and harvested, compared to 0.5 of grass. However, you have to keep your hungry animals from getting to it otherwise they'll only get a max of 0.2 nutrition from eating the plant.

Making kibble[edit]

Kibble is a kind of animal feed made with both plant and animal sources. It can be made using haygrass and any kind of meat, including human or insect meat. Producing kibble at a butcher table costs 1 nutrition of vegetables or hay and 1 nutrition of meat or animal products, and produces 2.5 nutrition of kibble. 

All animals except wargs can eat it, so it makes a good way to feed your animals using mixed sources of nutrition, including those that animals won't normally eat. Kibble also lasts forever under a roof so you can store it and use it to feed animals when in need, such as in winter when there is nothing to eat.

When you feed a population of herbivorous or omnivorous animals kibble made from their own meat or milk, the formula for their nutrition efficiency can be calculated as:

nutritionEfficiency(kibble) = 2.5&#215;nutritionEfficiency(raw vegetables) - 1

In effect, this means that for any animal population that has a nutrition efficiency of at least 0.667, it is more efficient to feed them kibble rather than hay. It is worth noting, however, that this will increase the amount of butchering and cooking labour needed to support the higher animal population required.

Corpse freezer[edit]

In typical RimWorlder fashion, you can use a freezer to preserve the corpses of raiders (or dead colonists if you're desperate) so you can feed omnivorous and carnivorous animals. This allows you to make use of corpses while avoiding heavy mood penalties from butchering humans or eating their flesh.

Raising[edit]

Pens[edit]

Main article: Pens

Pens are areas which farm animals are assigned to. These pen animals will be passive, meaning that hostiles will not attack these animals, and vice versa. Tamed pen animals must be put in a pen, or they will occasionally attempt to leave the map, meaning they disappear forever. Colonists will automatically rope roaming farm animals and place them in the pen. The borders of pens can be marked with: solid walls, doors, fences, fence gates, and animal flaps. To mark an enclosed area as a pen, place a pen marker inside. The pen marker also tells you the amount of animals that can be sustained in a pen with wild plants, measured in cows, goats, and chickens. An attached, roofed, and heated/cooled coop can be built with an animal flap as a door instead of a regular door for animals to stay warm or cool down during extreme temperatures.

Pet care[edit]

Tamed animals that have a social bond to a person will affect the master's mood positively while living and negatively if killed (-8 for 20 days). This bond will either improve resistance against mental breaks or cause them. Because of the effect they cause on feelings, these creatures should be given special treatment, or any animal worth keeping alive.

These are a few tips to keep them safe:

- Keep them indoors by creating a new animal zone within a room.

- Keep them at the Home area after building a base wall.

- Prey pets should not be left wandering around in unrestricted area.

- Hunt their predators to prevent surprise attacks (or just wall the base in to prevent predators from coming in).

- Patrol your perimeter by zooming your view out to a larger scale but not to full, just enough to spot their sleeping animation of flying ZZZs while they rest at night. Sweeping your surroundings once every night shall keep you aware of threat presence.

- Animals can get into drugs, store them in specialized storage areas and use a zone to prevent them from accessing it, depending on size they may be prone to overdose or getting blackout from alcohol, being more dangerous with Boomrats which can set fire to the storage area. Pen Animals should also be kept away from storage areas for this reason.

Note: The first three of these tips only apply to pet animals. Farm animals are passive while in pens, though if the pen is built with fences, predators can still pass through.

Butchering[edit]

This section is suggested to be rewritten. Reason: This section needs to better explain the assumptions and math built into gthe different results, ideally with a worked example using property calls to stay matched to the table result. see Talk page for some discussion. You can help the RimWorld Wiki by improving it.

Animal

Diet

Tameness Decay Interval (Days)

Produces

Produce / Day

Produced Nutrition / Day

Males / Female

Baby Slaughter

Adult Slaughter

Meat Nutrition / Day

Consumption / Day

Meat Nutrition Efficiency&#91;2&#93;

Meat Nutrition / Day

Consumption / Day

Meat Nutrition Efficiency&#91;2&#93;

Alpaca

herbivorous

–

Alpaca wool 4.5

–

0.23

0.23

0.54

0.431

1.05

1.25

0.838 a)

Alphabeaver

dendrovorous

7.5

– –

–

0.18

0.24

5.66

0.042

0.74

20.23

0.037

Arctic fox

carnivorous

7.5

– –

–

0.15

0.19

0.18

1.027

0.66

0.54

1.228

Arctic wolf

carnivorous

6.9

– –

–

0.15

0.24

0.33

0.726

1.02

1.24

0.827

Bison

herbivorous

–

Bison wool 8

–

0.23

0.5

1.05

0.478

2.52

2.3

1.095

Boomalope

herbivorous

–

Chemfuel 11

–

0.23

0.42

1.05

0.4

2.1

2.44

0.862

Boomrat

omnivorous grazer

7.5

– –

–

0.18

0.22

0.26

0.819 c)

0.48

0.81

0.591 c)

Capybara

herbivorous

–

– –

–

0.27

0.29

0.46

0.629

1.16

1.32

0.882 b)

Caribou

herbivorous

–

Milk 5

0.25

0.23

0.23

0.54

0.893

1.05

1.15

1.127 a)

Cassowary

herbivorous

–

Egg (fert.)0.3

0.15

0.23

0.26

0.55

0.464 c)

1.26

1.61

0.782 c)

Cat

carnivorous, ovivorous

–

– –

–

0.15

0.16

0.28

0.596

0.44

0.97

0.451

Chicken

herbivorous

–

Egg (fert.) & (unfert.)1

0.25

0.51

0.6

0.34

1.778 c)

2.1

1.79

1.174 c)

Chinchilla

herbivorous

–

– –

–

0.18

0.28

0.24

1.18 c)

0.76

0.72

1.046 c)

Cobra

carnivorous, ovivorous

7.5

Egg (fert.)0.15

0.04

0.08

0.11

0.12

0.934

0.27

0.45

0.606

Cougar

carnivorous, ovivorous

7.2

– –

–

0.15

0.16

0.37

0.42

0.7

0.92

0.76

Cow

herbivorous

–

Milk 14

0.7

0.23

0.5

1.05

1.144

2.52

2.44

1.321

Deer

herbivorous

–

– –

–

0.27

0.31

0.41

0.762

1.48

1.14

1.307

Donkey

herbivorous

–

– –

–

0.23

0.29

0.64

0.458

1.47

1.4

1.051

Dromedary

herbivorous

–

Milk 9

0.45

0.23

0.44

1.05

0.849

2.21

2.3

1.153

Duck

herbivorous

–

Egg (fert.) & (unfert.)1

0.25

0.51

0.6

0.42

1.422 c)

2.1

2.24

0.939 c)

Elephant

herbivorous

7.5

– –

–

0.11

0.42

2.86

0.147

2.1

7.42

0.283

Elk

herbivorous

–

Milk 11

0.55

0.23

0.44

1.05

0.944

2.21

2.44

1.13

Emu

herbivorous

–

Egg (fert.)0.3

0.15

0.23

0.26

0.55

0.464 c)

1.26

1.61

0.782 c)

Fennec fox

carnivorous

7.5

– –

–

0.15

0.19

0.18

1.027

0.66

0.54

1.228

Gazelle

herbivorous

–

– –

–

0.27

0.22

0.3

0.725

0.87

0.64

1.354 b)

Goat

herbivorous

–

Milk 4

0.2

0.27

0.23

0.46

0.944

0.94

1.09

1.041 b)

Goose

herbivorous

–

Egg (fert.) & (unfert.)0.5

0.25

0.25

0.43

0.56

0.757 c)

2.1

2.01

1.043 c)

Grizzly bear

omnivorous, ovivorous

7.2

– –

–

0.15

0.3

0.65

0.465

1.51

1.67

0.901

Guinea pig

herbivorous

8.4

– –

–

0.15

0.18

0.18

0.998 c)

0.41

0.43

0.947 c)

Hare

herbivorous

7.5

– –

–

0.18

0.22

0.22

0.998 c)

0.48

0.67

0.719 c)

Horse

herbivorous

–

– –

–

0.23

0.5

1.05

0.478

2.52

2.3

1.095

Husky

omnivorous, ovivorous

–

– –

–

0.15

0.24

0.92

0.261

1.03

3.3

0.313

Ibex

herbivorous

–

– –

–

0.27

0.27

0.41

0.675

1.24

0.85

1.451 a)

Iguana

omnivorous grazer

9

Egg (fert.)0.26

0.07

0.13

0.25

0.36

0.694 c)

0.74

1.03

0.718 c)

Labrador retriever

omnivorous, ovivorous

–

– –

–

0.15

0.25

0.74

0.342

1.02

2.88

0.354

Lynx

carnivorous, ovivorous

7.2

– –

–

0.15

0.12

0.22

0.52

0.42

0.57

0.734

Megasloth

herbivorous

6.18

Megasloth wool 10

–

0.11

0.42

1.78

0.236

2.1

4.55

0.463

Monkey

omnivorous grazer

8.4

– –

–

0.23

0.14

0.25

0.55 c)

0.37

0.48

0.768 c)

Muffalo

herbivorous

–

Muffalo wool 8

–

0.23

0.5

1.05

0.478

2.52

2.3

1.095

Ostrich

herbivorous

–

Egg (fert.)0.3

0.18

0.23

0.32

0.83

0.382

2.1

2.42

0.869 a)

Panther

carnivorous, ovivorous

7.2

– –

–

0.15

0.16

0.37

0.42

0.7

0.92

0.76

Pig

omnivorous grazer

–

– –

–

0.27

0.56

1.01

0.551

2.77

3.42

0.811

Polar bear

omnivorous, ovivorous

6.9

– –

–

0.15

0.3

0.65

0.465

1.51

1.67

0.901

Raccoon

omnivorous grazer

7.5

– –

–

0.18

0.25

0.38

0.667 c)

0.74

1.05

0.709 c)

Rat

omnivorous grazer

9

– –

–

0.18

0.2

0.19

1.058 c)

0.44

0.55

0.805 c)

Red fox

carnivorous

7.5

– –

–

0.15

0.19

0.18

1.027

0.66

0.54

1.228

Rhinoceros

herbivorous

6.6

– –

–

0.11

0.32

1.91

0.165

1.58

4.28

0.368

Sheep

herbivorous

–

Sheep wool 4.5

–

0.27

0.3

0.46

0.663

1.22

1.27

0.96 b)

Snowhare

herbivorous

7.5

– –

–

0.18

0.22

0.22

0.998 c)

0.48

0.67

0.719 c)

Squirrel

herbivorous

7.5

– –

–

0.27

0.18

0.2

0.88 c)

0.4

0.52

0.765 c)

Thrumbo

herbivorous, dendrovorous

6.12

– –

–

0.08

0.28

3.01

0.093

1.4

9.2

0.152

Timber wolf

carnivorous

6.9

– –

–

0.15

0.24

0.33

0.726

1.02

1.24

0.827

Tortoise

omnivorous grazer

7.5

Egg (fert.)0.3

0.08

0.11

0.32

0.15

2.144 c)

1.05

0.42

2.511 c)

Turkey

herbivorous

–

Egg (fert.)0.75

0.38

0.57

0.64

0.7

0.907 c)

3.15

2.88

1.094 c)

Warg

strict carnivorous

8.4

– –

–

0.15

0.34

0.46

0.728

1.69

1.72

0.98

Wild boar

omnivorous grazer

–

– –

–

0.27

0.31

0.61

0.508

1.31

1.98

0.665 b)

Yak

herbivorous

–

Milk 11

0.55

0.23

0.44

1.05

0.944

2.21

2.44

1.13

Yorkshire terrier

omnivorous, ovivorous

–

– –

–

0.15

0.16

0.28

0.596

0.44

0.81

0.54

Toxalope

herbivorous

–

– –

–

0.23

0.29

1.05

0.279

1.05

2.44

0.431

Waste rat

omnivorous grazer

9

– –

–

0.18

0.24

0.19

1.285 c)

0.6

0.55

1.091 c)

Alligator

carnivorous

6.6

Egg (fert.)0.13

0.06

0.06

0.26

0.51

0.514

1.31

0.98

1.333

Alpha thrumbo

herbivorous, dendrovorous

6.06

– –

–

0.08

0.35

3.01

0.116

1.75

9.2

0.19

Armadillo

omnivorous grazer

7.5

– –

–

0.27

0.27

0.41

0.662 c)

0.79

1.12

0.706 c)

Badger

omnivorous grazer

7.2

– –

–

0.27

0.33

0.41

0.801 c)

1.19

1.12

1.06 c)

Bluebird

herbivorous

8.4

Egg (fert.)0.33

0.08

0.17

0.2

0.15

1.337 c)

0.43

0.43

1.017 c)

Bog hound

omnivorous, ovivorous

9

– –

–

0.15

0.27

0.33

0.817

1.15

1.29

0.891

Bullfrog

omnivorous grazer

7.5

– –

–

0.27

0.12

0.2

0.609 c)

0.27

0.43

0.642 c)

Colossus toad

omnivorous grazer

10.5

– –

–

0.27

0.24

0.41

0.588

0.99

0.85

1.161 b)

Crow

omnivorous, ovivorous

10.5

Egg (fert.)0.33

0.08

0.25

0.2

0.16

1.247

0.43

0.44

0.992

Flamingo

omnivorous grazer

9.3

Egg (fert.)0.5

0.25

0.38

0.58

0.62

0.93 c)

2.1

2.07

1.015 c)

Gorilla

omnivorous grazer

8.4

– –

–

0.23

0.42

1.06

0.396

2.1

2.07

1.016

Greatwolf

carnivorous

6.3

– –

–

0.15

0.36

0.74

0.49

1.81

2.75

0.656

Hermit crab

omnivorous grazer

7.5

– –

–

0.27

0.22

0.17

1.292 c)

0.48

0.45

1.072 c)

Heron

omnivorous grazer

9.3

Egg (fert.)0.5

0.25

0.38

0.58

0.62

0.93 c)

2.1

2.07

1.015 c)

Hippo

herbivorous

6.6

– –

–

0.11

0.29

1.78

0.164

1.47

4

0.368

Lava snail

herbivorous

–

– –

–

0.23

0.39

0.39

1.003

1.71

1.08

1.585 a)

Macaw

herbivorous

10.5

Egg (fert.)0.13

0.03

0.06

0.11

0.2

0.551 c)

0.31

0.68

0.448 c)

Mastodon

herbivorous

7.5

Mastodon wool 10

–

0.11

0.45

3.19

0.141

2.25

8.06

0.279

Megavole

omnivorous grazer

9.6

– –

–

0.27

0.38

1.01

0.376

1.58

2.8

0.565 b)

Mink

omnivorous, ovivorous

7.5

– –

–

0.27

0.22

0.2

1.097

0.61

0.51

1.195

Monitor lizard

omnivorous grazer

9

Egg (fert.)0.17

0.04

0.13

0.19

0.36

0.532 c)

0.7

0.78

0.895 c)

Moose

herbivorous

–

– –

–

0.23

0.53

1.05

0.5

2.63

2.44

1.077

Muskox

herbivorous

–

Muskox wool 8

–

0.23

0.53

1.05

0.5

2.63

2.44

1.077

Otter

omnivorous grazer

9

– –

–

0.18

0.27

0.28

0.949 c)

0.79

0.82

0.967 c)

Panda

herbivorous

9.6

– –

–

0.15

0.21

0.37

0.57

1.05

0.95

1.1

Peafowl

herbivorous

–

Egg (fert.)0.5

0.13

0.38

0.58

0.51

1.132 c)

2.1

1.7

1.235 c)

Penguin

carnivorous

9.3

Egg (fert.)0.5

0.25

0.38

0.58

0.62

0.93

2.1

2.07

1.015

Porcupine

herbivorous

7.5

– –

–

0.18

0.25

0.28

0.899 c)

0.69

0.82

0.846 c)

Prairie dog

herbivorous

9

– –

–

0.18

0.2

0.19

1.049 c)

0.44

0.55

0.803 c)

Quail

herbivorous

–

Egg (fert.)0.77

0.19

0.39

0.58

0.27

2.162 c)

1.38

1.22

1.131 c)

Scimitar cat

carnivorous, ovivorous

7.2

– –

–

0.15

0.19

0.48

0.386

0.91

1.2

0.76

Sea lion

carnivorous

9

– –

–

0.27

0.39

0.61

0.635

1.85

1.98

0.939

Sea turtle

omnivorous grazer

7.5

Egg (fert.)0.23

0.11

0.11

0.24

0.18

1.327 c)

0.79

0.43

1.855 c)

Seal

carnivorous

9

– –

–

0.27

0.3

0.61

0.49

1.24

1.98

0.626

Sparrow

herbivorous

8.4

Egg (fert.)0.33

0.08

0.17

0.15

0.15

1.003 c)

0.38

0.43

0.9 c)

Stone crab

omnivorous grazer

7.5

– –

–

0.27

0.26

0.24

1.079 c)

0.65

0.65

0.999 c)

Swan

herbivorous

9.3

Egg (fert.)0.5

0.13

0.25

0.58

0.56

1.024 c)

2.1

2.01

1.043 c)

Tiger

carnivorous, ovivorous

6.6

– –

–

0.15

0.2

0.37

0.529

0.98

0.92

1.064

Vulture

strict carnivorous

9.3

Egg (fert.)0.25

0.06

0.19

0.29

0.44

0.657

1.05

1.03

1.015

Walrus

carnivorous

7.5

– –

–

0.23

0.53

1.06

0.495

2.63

3.15

0.833

Wolverine

strict carnivorous

6.3

– –

–

0.13

0.23

0.41

0.565

0.92

0.96

0.957

a) Babies will overeat when grazing most wild plants. See above or saturation for more info.

b) Babies and juveniles will overeat when grazing most wild plants. See above or saturation for more info.

c) Babies, juveniles and adults will overeat when grazing most wild plants. See above or saturation for more info.

Notes[edit]

- ↑ This is not an intrinsic property, just so happens that every currently implemented pen animal lacks the ability to be trained.

- ↑ 2.0 2.1 For a list that does include milking see List of animals.

Version history[edit]

- 0.12.906 - Animals can now be tamed and trained. Animals now sleep. Animals can be pregnant and give birth. Animals can be named when tamed or when nuzzling. Animals produce animal filth. Animals have “life stages” related to their ages. Eggs, Milk and Wool production added. Nuzzling added. Animals have life expectancies.

- 0.12.910 - Rebalanced animal hunger rate and animal hauling.

- 0.13.1135 - Added new animals, some of which will hunt people. Some animals are now predators, including colony pets (e.g. cats catch squirrels). Animals can gnaw corpses apart directly now. Animal bonding added.

- Beta 19/1.0 Update - Obedience training steps 1 -> 3. Nuzzle target search distance 15 -> 40. Nuzzled memory duration 0.5 days->1 day, stacked effect multiplier 0.95->0.5, stack limit 10

- 1.1.0 - Changed animal rescue radius from 30 to 75. Fix: Jawless animals can still haul.

- 1.2.2719 - Removed naming animals through nuzzling. Animals only get names by bonding, or if given names by the player (so you can implicitly tell which animals are bonded by seeing which have names).

- 1.3.3066 - Major overhaul to animals: added multiple animal-related buildings, added pens, decreased trainability of boomalope to none, added sterilization, added release to wild.

Animals

Herbivorous
Alpaca &#8226; Bison &#8226; Boomalope &#8226; Capybara &#8226; Caribou &#8226; Cassowary &#8226; Chicken &#8226; Chinchilla &#8226; Cow &#8226; Deer &#8226; Donkey &#8226; Dromedary &#8226; Duck &#8226; Elephant &#8226; Elk &#8226; Emu &#8226; Gazelle &#8226; Goat &#8226; Goose &#8226; Guinea pig &#8226; Hare &#8226; Horse &#8226; Ibex &#8226; Megasloth &#8226; Muffalo &#8226; Ostrich &#8226; Rhinoceros &#8226; Sheep &#8226; Snowhare &#8226; Squirrel &#8226; Turkey &#8226; Yak &#8226; Toxalope &#8226; Bluebird &#8226; Hippo &#8226; Lava snail &#8226; Macaw &#8226; Mastodon &#8226; Moose &#8226; Muskox &#8226; Panda &#8226; Peafowl &#8226; Porcupine &#8226; Prairie dog &#8226; Quail &#8226; Sparrow &#8226; Swan 
Dendrovorous
Alphabeaver &#8226; Thrumbo &#8226; Alpha thrumbo 
Omnivorous
Boomrat &#8226; Grizzly bear &#8226; Human &#8226; Husky &#8226; Iguana &#8226; Labrador retriever &#8226; Megascarab &#8226; Megaspider &#8226; Monkey &#8226; Pig &#8226; Polar bear &#8226; Spelopede &#8226; Raccoon &#8226; Rat &#8226; Tortoise &#8226; Wild boar &#8226; Yorkshire terrier &#8226; Waste rat &#8226; Bog hound &#8226; Monitor lizard &#8226; Armadillo &#8226; Badger &#8226; Bullfrog &#8226; Colossus toad &#8226; Crow &#8226; Flamingo &#8226; Gorilla &#8226; Hermit crab &#8226; Heron &#8226; Hive queen &#8226; Larva &#8226; Locust &#8226; Megavole &#8226; Mink &#8226; Otter &#8226; Sea turtle &#8226; Stone crab 
Carnivorous
Arctic fox &#8226; Arctic wolf &#8226; Cat &#8226; Cobra &#8226; Cougar &#8226; Fennec fox &#8226; Lynx &#8226; Panther &#8226; Red fox &#8226; Timber wolf &#8226; Warg &#8226; Alligator &#8226; Greatwolf &#8226; Penguin &#8226; Scimitar cat &#8226; Sea lion &#8226; Seal &#8226; Tiger &#8226; Vulture &#8226; Walrus &#8226; Wolverine 
Dryads
Barkskin &#8226; Berrymaker &#8226; Carrier &#8226; Clawer &#8226; Gaumaker &#8226; Immature dryad &#8226; Medicinemaker &#8226; Woodmaker

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Animal_husbandry&oldid=184272#Bonding"

 Categories: - Stubs
- Pages to be rewritten
- Creatures

Hidden category: - Pages that need fact checking

 

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

 
 

 

 
 - This page was last edited on 2 October 2026, at 18:46.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -