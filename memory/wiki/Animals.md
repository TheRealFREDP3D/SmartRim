Animals - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Animals

 
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

Character&#160;Types

Colonists

Animals

Mechanoids

Prisoners

Raiders

Visitors

For the skill of the same name, see Skills.

For a complete list of all animals with images, see List of animals.

Animals are a type of nonplayable, nonhuman pawn in Rimworld with their own needs, stats, capacities, and actions. They come in dozens of species, all of which can be wild or tamed. Wild animals occasionally spawn at the map edges according to the biome and sometimes from random events. 

Animals usually wander the map aimlessly and feed when hungry, even eating player-grown plants. Like humans, animals don't require water and generate filth. All animals will fight back if melee combat is initiated. With just a little luck, even a small rat or squirrel can take down and even kill a casually armored colonist. The most dangerous species regularly hunt humans or can immediately turn manhunter out of revenge. Some animals can be trained to guard your colonists and attack enemies. Friendly fire can happen with domesticated animals.

Contents

- 1 Animals tab

- 1.1 Allowed areas

- 2 Appearance

- 3 Behavior

- 3.1 Mating

- 3.2 Aggression

- 3.3 Predation

- 3.4 Body heat

- 4 Reproduction

- 4.1 Live birth

- 4.2 Eggs

- 4.3 Sterilization

- 5 Diet

- 6 Health

- 7 Hunting

- 7.1 Hunting tips

- 8 Life stages

- 9 Needs

- 10 Animal husbandry

- 11 Version history

Animals are an important source of food by the meat they provide once hunted or slaughtered, and subsequently butchered.

Colonists assigned to handle receive 90 XP towards their animals skill per training or taming attempt. When tamed "cute" animals nuzzle a colonist, the non-psychopath colonist receives a +4 Nuzzled thought for 1 day. Animals can also form bonds with colonists, providing a permanent +5 [Bonded animal]'s master thought as long as said colonist is assigned as a bonded animal's master, or a −3 Not [Bonded animal]'s master thought otherwise. These moods don't apply to psychopath colonists.

Sometimes, humans act like animals in a specific encounter event or unfortunate mental break, but revert to normal colonist behavior if successfully (re)tamed.

Animals tab[edit]

The Animals tab is in the menu bar at the bottom of the screen. The default hotkey is F4. The Animals tab lists all the colony animals. From left to right, displayed information is as follows:

- Double-clicking an animal's name will center the map to that animal.

- Gender, Age, and Life Stage are displayed

- Pregnant or Sterilized

- A button lists the animal's master, if it has one. Click the button to assign a new master. Bonded status is also displayed.

- If the animal is designated to follow its master when drafted or doing field work.

- A "Slaughter" checkbox column allows easy slaughtering of multiple tamed animals at once.

- Checkbox columns for each trainable skill: Tame, Guard, Rescue, Attack, and Haul for the management of animal training.

- Allowed areas are listed here. Animals stay in their assigned areas unless designated to follow their master.

Most of the above information is also displayed in the animal's inspect pane.

Allowed areas[edit]

One of the best ways to control animals is to assign them an allowed area. Allowed areas are created via the Expand allowed area function in the Architect>Zone menu.
Zoning prevents animals from wandering into danger and eating things they shouldn't be. Be certain to designate them an animal sleeping spot and ensure they have access to a food source. Some species (most ungulates) cannot be assigned an area and must instead be roped by a colonist into a pen.

Appearance[edit]

Most animal sprites do not show limbs, just like human sprites. Some animals have different appearances between males and females. Some animals have a different sprite for infant and adult life stages, like the chicken. 

Behavior[edit]

- Wandering: Animals will wander the accessible map, their pen, or their assigned zone when their needs are satisfied, e.g. hunger and sleep. Some wild animals tend to stay together in a herd. Tamed animals may cross doors, fences and barricades in their assigned area, unlike pen animals. Note that pen animals that have had a sentience catalyst can cross fences and barricades. Wild animals cannot cross doors but can cross fences and barricades if their tamed, baseline counterparts can.

- Filth: While walking on constructed floors, some animals produce animal filth. The Filth rate stat is proportional to the body size and wildness stats. Farm animals tend to produce massive amounts of filth. This can be mitigated by straw matting floors or by simply keeping animals outdoors on natural terrain.

- Roaming: Tame pen animals will occasionally attempt to leave the map if not in a pen or if a pen door is left open. Their escape frequency is determined by the stat roam interval. Roaming is disabled for animals that have had a sentience catalyst used on them.

- Moving: the animal is moving into its assigned area.

- Consuming food: animals attempt to eat a nearby food source when hungry. Herbivores move to find mature plants and carnivores hunt. Animals will keep searching for food until their hunger bar reaches satiation.

- Mating: male and female adults of the same species occasionally mate, which may result in a female pregnancy.

- Sleeping: when tired or wounded, tamed animals prefer to sleep in an animal bed or animal sleeping spot.

- Attacking: All animals can only melee attack. They will defend themselves in melee combat, and some animals can turn manhunter and chase your colonists. A text warning pops up on the screen when a colonist is ordered to interact with a potentially dangerous wild animal.

- Fleeing: all animals have a chance of erratically fleeing from ranged attacks hitting a target in their immediate vicinity. Animals do not flee predators or melee attacks. Animals do not leave their pen or assigned area when fleeing.

- Hauling: some animals, like the husky, can be trained to haul items, similar to how colonists haul items.

- Following master: some animals, like the elephant, can be trained to follow their master when drafted or doing field work (mining or hunting).

- Nuzzling: Certain tame animals will occasionally nuzzle your colonists. Animals can even nuzzle patients in bed. A colonist who is nuzzled receives a 4 Nuzzled thought for 1 day. The following animals can nuzzle: cat, guinea pig, husky, labrador retriever, monkey, and yorkshire terrier.

Mating[edit]

Female animals do not ever attempt to initiate mating themselves. Males will only mate with females in the same assigned area. Wild animals do not mate. Incest is common and has no effect on animal health. 

There is either a 1/12 or 1/8 (depending on species) chance per hour that an awake, non-sterilized male will search for a non-pregnant/non-fertilized, non-sterilized, awake female of the same species within 30 tiles to initiate mating. The female then has a 50% chance to become pregnant in the case of gestational animals or a 100% chance to become fertilized in the case of egg-laying animals.

In order to maximize the rate of offspring for a given population size of adults, the ideal is that the moment one female becomes pregnant or fertilized, another gives birth or lays an egg and becomes available to be mated. If there was no randomness involved in mating, the female:male ratio that would achieve this is given by awake_proportion × gestation_time / (2 × mate_mtb) for gestational animals, or awake_proportion × egg_interval / mate_mtb for egg-laying animals. As the proportion of time spent awake can be approximated to be about 2/3 for a rest effectiveness of 0.8, and mate_mtb is usually 12 hours, this can be simplified to 2/3 × gestation_time or 4/3 × egg_interval in most cases. 

However, as the randomness involved with mating becomes more significant with smaller population sizes, slightly more males will be desired for smaller populations. On the contrary, animals that can be milked will want more females than this ratio suggests, as the gains from milk will offset the losses from time spent not pregnant. Animals that can lay unfertilized eggs like the chicken can similarly afford a higher female ratio.

Aggression[edit]

Most animals in Rimworld are dangerous to hunt or tame. A warning message will pop-up when a colonist is ordered to interact with a dangerous wild animal.

The Revenge chance on harm stat is the chance an animal will turn manhunter when harmed by a member of your colony. It is three times higher for close-ranged attacks, like that of a machine pistol. For an animal like an ostrich with a 100% revenge chance, it will always turn manhunter after being hurt. Most animals also have a revenge chance on tame fail stat which dictates how likely the animal is to attack after a failed taming attempt.

Sometimes, the entire herd of wild animals will take revenge on your colonists. They may all get turned manhunter by a psychic wave event and attack any humans they can reach. Manhunters may even pick fights with your tamed animals.

Predation[edit]

Most carnivores are predators who will hunt smaller species (except domestic dogs who never hunt). When hungry, a predator will prefer an easy meal. They'll first attempt to eat meals, meat, and other food types within their diet. Otherwise they will feed upon downed animals or fresh corpses. 

When a hungry predator has no other food nearby, they will hunt, kill and consume almost any animal smaller than them, including your tamed animals and your colonists (and certainly children). This can especially be a problem on maps with little wildlife, like on Ice sheets when a polar bear wanders in. Predators always avoid boomrats and boomalopes. 

Predator attacks usually blind or stun their prey, leaving the victim unable to fight back. Unlike most other enemies, predators continue attacking after their prey is downed to finish off their target. If they do down your colonist or livestock, immediately order the nearest comrade to rescue the downed pawn. It's the difference between life and death.

Predators include the Arctic fox, Arctic wolf, Cat, Cobra, Cougar, Fennec fox, Grizzly bear, Lynx, Panther, Polar bear, Red fox, Timber wolf, Warg, Alligator, Bog hound, Greatwolf, Scimitar cat, Tiger, Wolverine.

If you successfully hide all colonists and tamed animals away from a predator's reach, it will hunt any other available wildlife.

It is not possible to view the Needs tab of a wild animal, so you may have to deduce whether or not a predator is hungry based on its behavior. They sometimes remain near the area where they last killed and ate an animal for about a day. Bloodstains or partially-consumed animal corpses on the ground are a fairly reliable guide, as well as a source of free leather and leftover food. Be careful not to let a hauler take away a predator's food before it has finished eating. It will still be hungry and will hunt your colonist instead.

Remember that fences and fence gates do not count as impassable for all animals, some predators can climb fences.

Body heat[edit]

Main article: Body heat

Animals will give out body heat, slightly heating up their surroundings. This is insignificant most of the time, except in enclosed, densely-packed barns. The heat can become a problem in warm weather or hot biomes but a benefit in cold biomes or during winter. For detailed information, see Body heat.

Reproduction[edit]

Animals are born by live birth or by hatching from a fertilized egg.

Live birth[edit]

See also: Pregnancy

Female Animals which give live birth (e.g. mammals) have a chance of becoming pregnant after mating with a male. The gestation time stat specifies how many days a species' pregnancy will last. A pregnant animal suffering from malnutrition or injuries may miscarry, but spontaneous abortions are not possible in game. Miscarriages are noted by an in-game message and loss of the baby, but the mother is otherwise unharmed and may reproduce normally again. Pregnancies may also be aborted through surgery.

For the first 600&#160;ticks (10&#160;secs) the pregnancy condition will be invisible, after which point a message will come up mentioning the pregnancy and the following hediffs become visible.

Stage
Begins at
Symptoms

Early-stage
>0 Severity

- Vomiting (MTB of 2.5 days)

Middle-stage
>0.333 Severity

- -15% Moving

Late-stage
>0.666 Severity

- Vomiting (MTB of 5 days)

- -30% Moving

Birth
1.0 Severity

- Symptoms end

- Offspring is born

Live births occur at the end of the gestation time. They produce filth in the form of amniotic fluid, but no blood loss or damage occurs to the mother or baby. A species' litter size is a probability curve of the number of offspring possible from one pregnancy

Eggs[edit]

Egg-laying animals include the Alligator, Bluebird, Cassowary, Chicken, Cobra, Crow, Duck, Emu, Flamingo, Goose, Heron, Iguana, Macaw, Monitor lizard, Ostrich, Peafowl, Penguin, Quail, Sea turtle, Sparrow, Swan, Tortoise, Turkey, Vulture as of 1.1. Females become fertilized after mating with males, causing them to lay fertilized eggs. Most animals will not lay unfertilized eggs, with the exception of chickens, ducks, and geese.

Fertilized eggs display their progress on the inspect pane and hatch when ready.

Fertilized eggs can be ruined by temperature if not kept within their safe temperature range of 0&#160;°C&#160;– 50&#160;°C (32&#160;°F&#160;– 122&#160;°F).

Eggs start to freeze below 0&#160;°C (32&#160;°F).
Eggs start to overheat above 50&#160;°C (122&#160;°F).
The inspect pane will indicate 'Overheating' or 'Freezing' followed by a percentage rising up to 100%. It increases by 0.003% per 1&#160;°C (1.8&#160;°F) outside the safe temperature range each tick. This status is halted when safe temperate is restored, but it is not reset - if the temperature is unsafe again, it will pick up where it left off. If it reaches 100% the egg is 'ruined by temperature' and will not hatch even if returned to a suitable area. A ruined egg still has full nutritional value and can be used to make a meal (or eaten raw, with a mood debuff).

Sterilization[edit]

Main article: Sterilization

Animals can be sterilized by way of an operation to prevent them even attempting to breed with another animal. As such they will never reproduce, although existing pregnancies will not be terminated by the procedure.

Diet[edit]

They animal's diet determines which food types it can eat. Because all animals except the strict carnivores can eat meals, kibble, and pemmican, it is possible to feed meat to herbivores and plants to carnivores if it is prepared first.

Note that some animals have multiple diets.

Diet
Allowed food types
Animals

omnivorous (human)

meat, kibble, meals, corpse, seeds, animal products, processed foods, vegetables, fungi, liquors, fluids

Human, Creepjoiner

omnivorous grazer

meat, kibble, plants, meals, corpse, seeds, processed foods, vegetables, fungi, liquors

Boomrat, Iguana, Monkey, Pig, Raccoon, Rat, Tortoise, Wild boar, Waste rat, Armadillo, Badger, Bullfrog, Colossus toad, Flamingo, Gorilla, Hermit crab, Heron, Megavole, Monitor lizard, Otter, Sea turtle, Stone crab

omnivorous

meat, kibble, meals, corpse, seeds, processed foods, vegetables, fungi, liquors

Grizzly bear, Husky, Labrador retriever, Megascarab, Megaspider, Polar bear, Spelopede, Yorkshire terrier, Bog hound, Crow, Hive queen, Locust, Mink

herbivorous

kibble, plants, meals, seeds, processed foods, vegetables, fungi, liquors

Alpaca, Bison, Boomalope, Capybara, Caribou, Cassowary, Chicken, Chinchilla, Cow, Deer, Donkey, Dromedary, Duck, Elephant, Elk, Emu, Gazelle, Goat, Goose, Guinea pig, Hare, Horse, Ibex, Megasloth, Muffalo, Ostrich, Rhinoceros, Sheep, Snowhare, Squirrel, Thrumbo, Turkey, Yak, Toxalope, Alpha thrumbo, Bluebird, Hippo, Lava snail, Macaw, Mastodon, Moose, Muskox, Panda, Peafowl, Porcupine, Prairie dog, Quail, Sparrow, Swan

dendrovorous

trees, kibble, seeds, processed foods, vegetables, fungi

Alphabeaver, Thrumbo, Alpha thrumbo

carnivorous

meat, kibble, meals, corpse, processed foods

Arctic fox, Arctic wolf, Cat, Cobra, Cougar, Fennec fox, Lynx, Panther, Red fox, Timber wolf, Alligator, Greatwolf, Penguin, Scimitar cat, Sea lion, Seal, Tiger, Walrus

strict carnivorous

meat, corpse

Warg, Ghoul, Vulture, Wolverine

ovivorous

kibble, meals, animal products, processed foods

Cat, Cobra, Cougar, Grizzly bear, Husky, Labrador retriever, Lynx, Panther, Polar bear, Yorkshire terrier, Bog hound, Crow, Mink, Scimitar cat, Tiger

animal products

animal products

Megascarab, Megaspider, Spelopede, Hive queen, Locust

none

none

Bulbfreak, Chimera, Devourer, Dreadmeld, Fingerspike, Fleshmass nucleus, Gorehulk, Metalhorror, Nociosphere, Noctol, Revenant, Sightstealer, Toughspike, Trispike, Barkskin dryad, Berrymaker dryad, Carrier dryad, Clawer dryad, Gaumaker dryad, Immature dryad, Medicinemaker dryad, Woodmaker dryad

Although all meat-eating animals can eat the raw fish items, some can catch their own fish for food when hungry if they have access to at least one fishable water tile: Grizzly bear, Polar bear, Flamingo, Heron, Otter, Penguin, Sea lion, Seal, Walrus

Health[edit]

Animals have the same set-up as humans when it comes to health, minus the ability to operate on them (except euthanasia)(The option to amputate an infected limb can become available once infection sets in, at least on Thrumbos—assuming other animals as well). They feel pain, and have all of the different health stats that human pawns possess. Animals can become addicted to beer, and they suffer the same negative health alcohol effects as humans. Keep them away from alcohol.
Animals need to have an animal bed (or sleeping spot) in order to be healed.

Like humans, they have a life expectancy, and are affected by chronic diseases. There is no way to cure them in the base game other than Healer mech serum, which would be incredibly expensive.

A tamed animal that requires tending will find the nearest animal bed or animal sleeping spot in their allowed area and rest there until it is either fully healed or dead. Pawns assigned to doctoring will tend its wounds or illnesses and feed it, just as they would do for a human pawn. If all human colonists are absent or unable to care for a sick animal, it can die of starvation even if there is food nearby and it is capable of walking. The animal can be forced to stand up by removing the medical designation from any medical animal beds in the animal's allowed area or pen.

Animals have a Toxic Resistance of 50% by default, compared to the human default of 0%.

Hunting[edit]

See also: Hunt

Wild animals may be marked for hunting, done by hunters with ranged weapons, who will proceed to shoot them at maximum range, before executing them with a neck cut when they are downed (except explosive animals). After killing their target, they will haul the carcass to a stockpile zone even if they are naturally incapable of hauling, but will not start hauling it again if they're interrupted.

Animals harmed by hunting that were not killed yet may become enraged and if its a pack type, its full horde may turn hostile against the entire colony. If they are non-aggressive animals they usually flee instead.

Hunting may take longer during bad weather since there's a shooting modifier while it's raining or snowing that makes it more likely for shots to miss.

- Fog (with or without rain): hit chance multiplier is 50%.

- Rain or snow: hit chance multiplier is 80%.

To mark animals to be hunted use one of the following methods: 

- Click Wildlife, Click the first red X to the right of the animal you want to hunt and change it to a green check mark

- Click Orders, Hunt, then click one or more individual animals.

- Click Orders, Hunt, then click and drag a box to surround and select multiple animals.

- Select one or more animals, click Hunt.

Hunting tips[edit]

- Animals can be hunted manually instead of just using the hunt order by drafting a colonist and right clicking to fire at animals. This allows the killing of multiple animals in one session, or hunting from close range. Closer range reduces the chance of missing shots or unintended friendly fire, but raises the chance of provoking animal revenge.

- Wounded animals (either hit with arrows/bullets or cut in particular) tend to bleed. Heavily bleeding animals die after a certain period of time if left untended. Thus it is possible to wound a target and wait until it bleeds to death or drops unconscious due to blood loss. This way you can avoid unnecessary damage to the corpse (and avoid being caught in the explosion left by boomalopes and boomrats). Keep in mind that a wounded but mobile animal can wander away. Unconscious animals can be "saved" - essentially transported to sleeping spots assigned as medical - but without medical treatment they will still die. A valid, if hardly humane, way to hunt.

- In the occasion of a full horde revenge, early-stage colonies may easily become overrun, leaving all colonists downed. But down is not out. Eventually, one or more of your colonists may recover. With luck, this miracle may take place at nightfall, when wildlife sleep (except for the most enraged beasts among those), or they have wandered far enough, opening a chance to rescue everybody else. The manhunter status of the horde will disappear overnight.
- Melee blocking could be a valuable tactic to defeat the rampaging animals. In addition to making it easier to defeat the animals even when outnumbered, it also keeps your downed colonists near your base for easy rescue.

Life stages[edit]

Animals all have three different life stages - baby, juvenile and adult. The growth at which they enter the juvenile and adult life stages is determined by each species' growth time stat. Animals may have different graphics for different life stages (e.g. deer) or may simply appear smaller. Some animals have a specific name for this stage (e.g. chick or puppy). Animals have different sounds (call, anger, wounded, death) for different life stages, too. Babies may simply make a higher pitched sound or have a different sound altogether (such as chicks).

The rate at which growth increases is influenced by saturation: If saturation is below the first 'hunger mark' ie: hungry, then growth rate is halved. If saturation is below the second 'hunger mark' ie: ravenously hungry, then growth rate is quartered. If saturation is at 0 ie: starving, then growth is completely halted. Malnutrition itself has no impact on growth rate at all.

Eventually, they reach their final body size and fertility in the final life stage, adulthood. Only upon reaching adulthood can animals produce wool or milk. Eggs may be laid by juveniles.[Verify]

Baby Bird
Baby
Juvenile
Adult

Body Size
10%
20%
50%
100%

Hunger
40%
40%
75%
100%

Max Food
60%
60%
75%
100%

Health Scale
25%
25%
60%
100%

Market Value
40%
40%
75%
100%

Move Speed
50%
50%
90%
100%

Melee Damage
50%
50%
75%
100%

The reduction in Body Size of babies and juveniles also affects several other stats, such as Meat and Leather Amount

Needs[edit]

Animals require food and sleep and will fulfil their needs on their own.

Food: Animals will eat any available food according to their diet. Herbivorous animals of the colony can be left to eat grass on their own. Note that animals require different amounts of food compared to humans, as represented by their Hunger Rate.

Rest: Animals will sleep as needed. Tamed animals will sleep in animal sleeping spots, animal sleeping boxes, or animal beds. If none of which are available, the animal will crash out on the ground inside its allowed zone. A tamed animal will not sleep as long as its master is drafted.

Animal husbandry[edit]

Main article: Animal husbandry

Animals can be tamed and put to use in the colony, providing several benefits. Some species can be trained to perform one or possibly more tasks, and will wander about your colony freely. Other species, which can loosely be considered "farm animals", can only be tamed and then put in a pen. This second category can never be trained.

Version history[edit]

- 0.12.906 - Animals can now be tamed and trained. Animals now sleep. Animals can be pregnant and give birth. Animals can be named when tamed or when nuzzling. Animals produce animal filth. Animals have “life stages” related to their ages. Eggs, Milk and Wool production added. Nuzzling added. Animals have life expectancies.

- 0.12.910 - Rebalanced animal hunger rate and animal hauling.

- 0.13.1135 - Added new animals, some of which will hunt people. Some animals are now predators, including colony pets (e.g. cats catch squirrels). Animals can gnaw corpses apart directly now. Animal bonding added.

- Beta 19/1.0 Update - Obedience training steps 1 -> 3. Nuzzle target search distance 15 -> 40. Nuzzled memory duration 0.5 days->1 day, stacked effect multiplier 0.95->0.5, stack limit 10

- 1.1.0 - Changed animal rescue radius from 30 to 75. Fix: Jawless animals can still haul. Fix: No mood penalty for giving bonded animal as a gift if sent by transport pod.

- 1.2.2719 - Removed naming animals through nuzzling. Animals only get names by bonding, or if given names by the player (so you can implicitly tell which animals are bonded by seeing which have names).

- 1.3.3066 - Major overhaul to animals: added multiple animal-related buildings, added pens, decreased trainability of boomalope to none, added sterilization, added release to wild.

- 1.6.4566 - Sentience catalyst now removes roaming and fence-blocked status from animals.

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

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Animals&oldid=181866"

 Category: - Creatures

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

 
 

 

 
 - This page was last edited on 7 July 2026, at 20:55.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -