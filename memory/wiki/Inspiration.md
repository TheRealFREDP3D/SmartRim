Mental inspiration - RimWorld Wiki
 
 
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
 

 
 

 
 

 

 Mental inspiration

 
 From RimWorld Wiki

 (Redirected from Inspiration)

 

 
 

 Jump to navigation
 Jump to search
 
Icon for inspired colonists.

 
An inspired colonist in the colonist bar.

Colonists with a high mood can randomly have mental inspirations, giving a stat boost for some time or a special one time benefit. Unlike mental breaks, you retain full control of the mentally inspired colonist.

Contents

- 1 Mechanics

- 2 Inspirations

- 2.1 Go frenzy

- 2.2 Inspired creativity

- 2.3 Inspired recruitment

- 2.4 Inspired surgery

- 2.5 Inspired taming

- 2.6 Inspired trade

- 2.7 Shoot frenzy

- 2.8 Work frenzy

- 3 Analysis

- 3.1 Acquiring inspirations

- 4 Legacy inspirations

- 4.1 Inspired art

- 5 Version history

Mechanics[edit]

Colonists have a chance, dependent on their mood, to have a random mental inspiration. There are 8 different types of inspirations that can occur, chosen at random from all the options for which the affected colonist meets the requirements. Colonists can only have one inspiration at a time. Having an inspiration prevents any others until the current inspiration ends. 

The mean number of days between inspirations is dependent on the current mood of the colonist, and is controlled by the following equation: 

Inspiration MTB = If{Current Mood ≥ 50} Then {410 - (400 × (Current Mood/100)} Else {0}

Where Current Mood is the mood of the colonist in question, expressed as real number between 0 and 100, inclusive.

Therefore, inspirations cannot occur unless a colonist's mood is above 49%.

Mood
MTB Inspirations
Graph

50%
210 Days
 

60%
170 Days

70%
130 Days

80%
90 Days

90%
50 Days

100%
10 Days

Some traits prevent certain types of inspirations. Additionally, the pawns with the Tortured artist trait have a 50% to gain an Inspired Creativity inspiration after a mental break ends, with a possible exception of "Run Wild" mental breaks.[Verify] 

The word of inspiration psycast gives the target an inspiration. This inspiration is selected randomly by the same rules as any other natural inspiration. Psilocaps immediately grant a 2% chance of a random inspiration upon consumption, also following the rules of natural inspiration.

If an inspiration is available (see below), it gets a probability weight based on corresponding skill passion level: 1 for none or no corresponding skill, 2.5 for minor and 5 for major passion. Inspired creativity weight is only based on artistic skill passion.

Inspirations[edit]

Go frenzy[edit]

<NAME> will move faster for the next 8 days.

- Base duration: 8 day

- Minimum skill: None

- Incompatible Trait: Slowpoke

A colonist's great mood lifts them up and improves their move speed by ×140%, applied after additive offsets, for the duration of the inspiration. This does not improve the Moving stat, so Melee Dodge Chance is not improved by this inspiration.

Inspired creativity[edit]

<NAME> The next item, art, or furniture [PAWN_pronoun] creates will be two quality levels higher than it would otherwise be. This even allows the creation of legendary items. The inspiration will end after 8 days, or when the creation is completed.

See also: Quality

- Base duration: 8 days

- Minimum skill: Artistic 3 / Crafting 3 / Construction 3

A sudden burst of inspiration gives colonist insight on how to make a quality item. The next finished item will be 2 Quality levels higher than it would otherwise be, allowing for the creation of legendary items. The inspiration is only good for the next single object created, after which the inspiration ends.

Inspired recruitment[edit]

<NAME> will successfully recruit the next prisoner regardless of difficulty or resistance. The inspiration will end after 8 days, or when the prisoner is recruited.

- Base duration: 8 days

- Minimum skill: Social 3

A colonist gains insight on how to recruit prisoners into the colony. They will successfully recruit (or enslave) the next prisoner they attempt to recruit, regardless of difficulty or remaining resistance. With multiple prisoners, it is recommended to manually control the warden so that the desired prisoner is recruited.

The inspiration ends after a prisoner is recruited.

Inspired surgery[edit]

The next time <NAME> performs a surgery, [PAWN_possessive] chance of success will be doubled. A small minimum chance of failure still applies. The inspiration will end after 8 days, or when the surgery is performed.

- Base duration: 8 days

- Minimum skill: Medical 3

A colonist becomes more concentrated in surgeries after being inspired, doubling the Medical Surgery Success Chance stat. Note however that the 98% success rate maximum still applies i.e. there will always be a 2% chance of failure. Thus high skill doctors operating in high quality hospitals can receive no benefit from this inspiration, but it can make a great difference for those with lower Medicine skill who are not good surgeons yet.

The inspiration ends after a surgery is performed, even if the surgery fails.

Inspired taming[edit]

<NAME> will successfully tame the next animal regardless of difficulty. The inspiration will end after 8 days, or when an animal was tamed.

- Base duration: 8 days

- Minimum skill: Animals 3

A colonist is inspired to tame an animal. They will successfully tame the next animal regardless of difficulty. They will not be able to tame any animal that they do not have the requisite skill level to tame however. 

The inspiration ends when an animal is tamed.

Even if no new tamed animals are required, this inspiration can be used to tame and then slaughter large animals, avoiding the penalties to meat amount for missing body parts and not carefully slaughtering. This results in at least 50% more meat compared to hunting.

Inspired trade[edit]

<NAME> will get a significant trade price bonus when closing [PAWN_possessive] next trade deal. The inspiration will expire after 8 days, or when the deal is done.

- Base duration: 8 days

- Minimum skill: Social 3

A colonist is inspired to obtain a great deal. They will get a great 18% boost in trade prices, essentially meaning 12 more levels of Social skill.

After one successful trade deal, the inspiration ends. This includes trading with Royal Tribute Collectors, despite Trade Price Improvement not providing any benefit for such trades.[Verify]

Shoot frenzy[edit]

<NAME> will shoot more accurately for the next 8 days.

- Base duration: 8 days

- Minimum skill: None

- Incompatible Trait: Brawler, non-violent

A colonist is inspired to shoot more accurately, gaining +8 Shooting Accuracy, or the equivalent of +8 Shooting Skill, for the duration.

Work frenzy[edit]

<NAME> will work faster for the next 8 days.

- Base duration: 8 day

- Minimum skill: None

A colonist suddenly becomes significantly more productive and will have their Global Work Speed multiplied by 1.8x, multiplying after considering other bonuses to the stat, for the duration of the inspiration. For a more comprehensive view of how the stat is modified by different effects, see the Global Work Speed page.

Global Work Speed is applied as a multiplier to the following stats:

- Animal Gather Speed
- Butchery Speed
- Construction Speed
- Cooking Speed
- Deep Drilling Speed
- Drug Synthesis Speed
- Entity Study Rate
- General Labor Speed
- Hacking Speed
- Mechanoid Shredding Speed
- Medical Operation Speed
- Medical Tend Speed
- Mining Speed
- Plant Work Speed
- Pruning Speed
- Research Speed
- Smelting Speed
- Smoothing Speed

Analysis[edit]

Inspirations can be a huge bonus to the colony. They can occur naturally by improving the colony's overall mood, though if you find some of your colonists' moods are running pretty high, that might be a good time to rigorously enforce more recreation for them, to reach 100% mood and the quickest inspirations.

Because inspirations are chosen based on passions, if deciding to use word of inspiration or psilocaps, it is wise to choose a colonist who has a passion in the inspiration's skill and few passions/levels in the other inspiration skills. For example, if wanting to obtain inspired taming, a colonist with a burning passion in Animals and no other passions will be more likely to obtain it.

Inspired creativity is particularly strong. It provides an permanent or near-permanent buff to the colony, creating powerful weapons and armor, beds to reduce sleep time, sculptures for room boosts, etc. Legendary quality items are difficult to obtain normally but provide massive boosts and are very common with a high skill crafter + inspired creativity. For crafters, it is best used on weapons first, as weapons do not lose durability when held and provide a major impact to combat. Before an inspiration is obtained, big items like grand sculptures can be partially worked on, stopped, and "saved" for when inspired creativity happens.

Acquiring inspirations[edit]

Beyond the tortured artist trait, word of inspiration, and the unfarmable psilocaps, the only way to encourage inspirations is to improve their mood. Having impressive and beautiful rooms will help, as will setting a multi-phasic schedule to improve average comfort and sleep. Beer, psychite tea, and smokeleaf can all be consumed safely and stack with each other. Hard drugs like yayo can provide a temporary boost for the duration at the risk of addiction. Romance can potentially help, as weddings provide +40 mood to the pair and +20 mood to everyone present.

Tortured artists that are good or passionate at Crafting/Construction are particularly valuable colonists. They can be abused and locked up into a confined, walled-in space; this makes mental breaks likely while reducing the impact of breaks when they do happen. 

Word of inspiration can be spammed if a kill-focused persona weapon is obtained, as kill-focused provides ample psyfocus for killing any pawn, even chickens and other colony animals. It is still necessary to wait 8 days for inspirations like shoot frenzy that aren't one-time use.

Legacy inspirations[edit]

These no longer exist in the current version of the game.

Inspired art[edit]

- Base duration: 8 days 

Minimum skill: Artistic 6
A sudden burst of inspiration gives colonists a great idea for a piece of art, and after it is completed, that piece of art will be 3 levels higher than it would otherwise be. The inspiration is only good for 1 piece of art. Replaced by Inspired Creativity in Beta 19.

Version history[edit]

- 0.18.1722 - Added with the following inspirations: Work frenzy, Go frenzy, Shoot frenzy, Inspired trade, Inspired recruitment, Inspired surgery, Inspired art. At the time, incapacitation would end the inspiration.

- Beta 19/ 1.0 - Inspired colonists now get a special icon in the colonist bar

- 1.1 - "Inspired taming" inspiration added.

- 1.2.2719 - Fix: Pawn can get random inspirations while not capable of being conscious.

- 1.6.4850 - Fix: "Inspired recruitment" pawns interacting incorrectly with prisoners with "Reduce will" setting.

Status levels

Needs
Beauty &#8226; Chemical &#8226; Comfort &#8226; Drug addiction &#8226; Food &#8226; Indoors &#8226; Outdoors &#8226; Recreation &#8226; Rest &#8226; Deathrest &#8226; Energy &#8226; Kill satiety &#8226; Learning &#8226; Play 
Related
Hemogen 
Other
Mood (Mental break &#8226; Mental inspiration)

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Mental_inspiration&oldid=182326"

 Categories: - Characters
- Status Level

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

 
 

 

 
 - This page was last edited on 25 July 2026, at 21:32.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -