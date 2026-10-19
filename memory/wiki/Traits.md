# Traits

From RimWorld Wiki

Jump to navigation Jump to search

|  |  | [Basics](/wiki/Basics "Basics") | [Menus](/wiki/Menus "Menus") | [Game Creation](/wiki/Game_Creation "Game Creation") | [Gameplay](/wiki/Gameplay "Gameplay") | **Pawns** | [Plants](/wiki/Plants "Plants") | [Resources](/wiki/Resources "Resources") | [Gear](/wiki/Gear "Gear") | [Mods](/wiki/Mods "Mods")  
---|---|---|---|---|---|---|---|---  
[Pawns Menu](/wiki/Pawns "Pawns") | **Character Properties** | [Character Types](/wiki/Character_Types "Character Types")  
---|---|---  
[Character Properties](/wiki/Characters "Characters") | [Health](/wiki/Health "Health") | [Mood](/wiki/Mood "Mood") | [Needs](/wiki/Needs "Needs") | [Skills](/wiki/Skills "Skills") | [Thoughts](/wiki/Thoughts "Thoughts") | Traits | [Social](/wiki/Social "Social")  
---|---|---|---|---|---|---|---  
  
* * *

[![Traits preview.png](/images/1/1b/Traits_preview.png)](/wiki/File:Traits_preview.png)

**Traits** personalize and add flavor to your colonists by granting a wide variety of special bonuses or conditions to their day to day activities, and so encourage more complex player-conceived stories based on those individual characters. Traits provide physical or psychological abilities or limitations, likes/dislikes, behavior tendencies, personality quirks, and so on. Some are beneficial, some are harmful to the colonist or your colony as a whole. Some are constant, some only rarely triggered. Some can be more or less easily negated or manipulated to your advantage by catering to them (or denying them), others are more problematic or outright dangerous. 

## Contents

  * 1 Mechanics
    * 1.1 Trait acquisition
    * 1.2 Starting possessions
    * 1.3 Trait-affecting genes
  * 2 General traits
    * 2.1 Lifestyle
    * 2.2 Living space
    * 2.3 Social views
    * 2.4 Combat
    * 2.5 Skills
    * 2.6 Relationships
  * 3 Spectrum traits
    * 3.1 Drug desire
    * 3.2 Industriousness
    * 3.3 Speed traits
    * 3.4 Base mood
    * 3.5 Nerves
    * 3.6 Neurotic
    * 3.7 Shooting accuracy
    * 3.8 Beauty
    * 3.9 Psychic sensitivity
    * 3.10 Immunity
  * 4 Creepjoiner traits
    * 4.1 Positive traits
    * 4.2 Negative traits
  * 5 Obsolete traits
  * 6 Version history



## Mechanics[[edit](/index.php?title=Traits&action=edit&section=1 "Edit section: Mechanics")]

Only humans have traits. Most humans have 1-3 traits, with the possibility of an "extra" sexuality trait. Adults cannot gain new traits, and there is no way to remove traits. 

[Children](/wiki/Children "Children")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") usually only have a number of traits no higher than the number of [growth moments](/wiki/Growth_moment "Growth moment") they have reached, and babies have none. Children can attain a new trait every time they reach a new growth moment (birthdays 7, 10, and 13). 

### Trait acquisition[[edit](/index.php?title=Traits&action=edit&section=2 "Edit section: Trait acquisition")]

When a human is generated, it acquires traits according to this process: 

  * First, the pawn gains any traits that its "pawn kind" requires. _For example, the titular mechanitor[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") of [The Mechanitor](/wiki/Scenario_system#Default_Scenarios "Scenario system") start scenario always has the [Recluse](/wiki/Recluse "Recluse") trait._
  * Second, if the pawn is being generated for a quest, it gains any traits required by the quest. _For example, the imperiled noble from the[Noble wimp](/wiki/Noble_wimp "Noble wimp")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") quest always has the [Wimp](/wiki/Wimp "Wimp") trait._
  * Traits from the pawn's [backstories](/wiki/Backstories "Backstories") are then acquired, unless they would conflict with the pawn's "pawn kind". _For example, a pawn with a backstory composed of the[Cave Child](/wiki/Backstories/Tribal_Child "Backstories/Tribal Child") childhood and the [Scout](/wiki/Backstories/Tribal_Adult "Backstories/Tribal Adult") adulthood would have the [Undergrounder](/wiki/Undergrounder "Undergrounder") and [Jogger](/wiki/Jogger "Jogger") traits. However, a hypothetical backstory that grants the Brawler trait will not grant it if the pawn is a "tribal archer", as that pawn kind specifically prohibits the Brawler trait._
  * A trait count limit is chosen, based on the pawn's age. [Babies](/wiki/Babies "Babies")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") and [children](/wiki/Children "Children") under seven years of age have a limit of 0 traits; children with 7-9 birthdays, 1 trait; children with 10-12 birthdays, 1-2 traits; and anyone older, 1-3 traits, with no bias towards any particular number. If the pawn's current number of traits is lower than the trait limit, each 'missing' trait is filled in by a random trait, weighed based on each trait's commonality. The randomly gained traits cannot be any of the following: 
    * Any sexuality trait ([Asexual](/wiki/Asexual "Asexual"), [Bisexual](/wiki/Bisexual "Bisexual"), or [Gay](/wiki/Gay "Gay"))
    * [Wimp](/wiki/Wimp "Wimp"), but only if the pawn is from a [faction](/wiki/Faction "Faction") hostile to the player's faction
    * Any that the pawn already has
    * Any that conflict with a trait the pawn already has
    * Any prohibited by the pawn's "pawn kind" or backstories
    * Any that would disable a work type required by the pawn's "pawn kind"
    * Any that requires a work type disabled for the pawn
    * Any that would cause the pawn's minor [mental break threshold](/wiki/Mental_break_threshold "Mental break threshold") to rise above 50%
  * If the pawn is at least 13 years old, their sexuality is then determined. If the pawn has any romantic or ex-romantic relationship with someone of the same gender, they acquire the Gay trait. Otherwise, they may be Asexual, Bisexual, Gay, or straight (which is not a trait, merely an absence of the three sexuality traits). The random choice is weighted by each sexuality trait's commonality, or in the case of 'straight/no sexuality trait', weighted by the sum commonality of every non-sexuality trait that the pawn does not currently have. Note that since the [Biotech DLC](/wiki/Biotech_DLC "Biotech DLC") adds two traits with non-zero commonalities, sexuality traits are marginally rarer if Biotech is enabled.
  * Afterward, the pawn's [xenotype](/wiki/Xenotype "Xenotype")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") (if any) is determined. If [certain genes](/wiki/Traits#Trait-affecting_genes "Traits") are present, this can affect the pawn's trait set, either adding or suppressing traits.
  * If the [starting scenario forces any traits](/wiki/Scenario_system#Voluntary_parts "Scenario system"), the pawn gains any such traits. The "Forced trait" scenario part can be configured to apply to all pawns in the game, only the player's starting pawns, or only non-player pawns; it can also be configured to have a chance to trigger per pawn between 0-100%.
  * Finally, if the pawn is a [creepjoiner](/wiki/Creepjoiner "Creepjoiner"),[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") it gains any traits granted by its benefit and/or downside.



### Starting possessions[[edit](/index.php?title=Traits&action=edit&section=3 "Edit section: Starting possessions")]

[![Form Caravan.png](/images/thumb/d/d2/Form_Caravan.png/40px-Form_Caravan.png)](/wiki/Category:Pages_to_be_moved "Category:Pages to be moved") | This section is [suggested to be moved](/wiki/Category:Pages_to_be_moved "Category:Pages to be moved"). **Destination:** [Pawn selection](/index.php?title=Pawn_selection&action=edit&redlink=1 "Pawn selection \(page does not exist\)"). **Reason:** While some of this info can likely be kept in this page, most of it should move to [Pawn selection](/wiki/Game_Creation "Game Creation") once that page has been created.  
---|---  
  
Certain traits may influence the initial possessions of your colonists in the Pawn selection menu (either for [creating a new game](/wiki/Game_Creation "Game Creation") or [selecting new colonists after a game over](/wiki/Endings#Colony_End "Endings")). Unless you have chosen the [Naked Brutality](/wiki/Scenario_system#Default_Scenarios "Scenario system") start scenario or used the Scenario Editor to add the "no possessions" scenario part, each such colonist may have up to two possessions in their inventory. A stack of items counts as 1 possession. Possessions for each colonist are generated in the following order, ending prematurely if the colonist has two possessions: 

  * [Ghouls](/wiki/Ghoul "Ghoul")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") never have possessions.
  * [Babies](/wiki/Babies "Babies")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") have between 30-40 units of baby food.
  * If the colonist is addicted to a drug, they have enough of the drug to satiate the addiction for roughly 25-35 days.
  * If the colonist has a [genetic drug dependency](/wiki/Genes#Drugs "Genes"),[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") they have enough of the drug to satiate the dependency for roughly 25-35 days.
  * If the colonist has [hemogenic](/wiki/Hemogenic "Hemogenic") gene,[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") they have 8-12 [hemogen packs](/wiki/Hemogen_pack "Hemogen pack").
  * If the colonist has an adulthood backstory that can grant possessions, there is a 25% chance for them to have those possessions. Note that, should a backstory be capable of granting multiple possessions, this process will still stop once the colonist has two possessions, and the backstory's possessions are always granted in the order they are defined in the backstory.
  * **Traits are accounted for only after all the above steps have been performed**. There is a 25% chance for a colonist to receive possessions based on their [non-suppressed traits](/wiki/Traits#Trait-affecting_genes "Traits"). As with backstories, it is possible for this step to stop midway through once the colonist has two possessions; possessions are always granted in the order the traits present themselves, and per-trait they are granted in the order they are defined in the trait. _For example, a pawn with the Psychopath trait has a 25% chance to gain a skull and a heart, but a pawn who already has a prior stack of[flake](/wiki/Flake "Flake") due to a flake addiction would have a 25% chance to only gain a skull._
  * If the colonist still has less than two possessions, there is a 6% chance for them to have a random possession. The list of possible possessions is lengthy, but does not include every possible item in the game.



### Trait-affecting genes[[edit](/index.php?title=Traits&action=edit&section=4 "Edit section: Trait-affecting genes")]

[![BiotechIcon.png](/images/thumb/7/73/BiotechIcon.png/40px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)") | **This section relates to content added by[Biotech (DLC)](/wiki/Biotech_\(DLC\) "Biotech \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
  
Certain genes can modify a pawn's traits, either by forcing a trait to be added or suppressing a trait. Forced traits function as normal, though they are visible in the pawn's Bio tab in pale blue text. Suppressed traits do not have any effects, but are still visible in the pawn's Bio tab in dark grey text. 

If a forced trait would ordinarily conflict with non-genetically forced trait(s) the pawn already has, the latter is/are suppressed. If it would ordinarily conflict with genetic trait(s) the pawn already has, the latter is/are removed. If a trait-granting gene is removed, the trait will also be removed (unless the pawn already has the trait independent of genes); this un-suppresses any traits it had suppressed which are not suppressed by another gene or trait, and restores any genetically-forced traits that were removed by that gene and which do not conflict with any other trait the pawn has (including suppressed traits). This almost always leads to intuitive results, with one exception: if a pawn has the psychically hyper/sensitive trait, also has the psychically dull/deaf gene in their germline (e.g. due to being a [Yttakin](/wiki/Yttakin "Yttakin")), and then has the other psychic sensitivity trait gene in their xenogenes... removal of the xenogene will remove the trait it forces, but it will also not result in the restoration of the other gene's trait and will not un-suppress the psychically hyper/sensitive trait. 

* Click to 

Name  | Tooltip  | Effect on traits   
---|---|---  
[Pyrophobia](/wiki/Pyrophobia "Pyrophobia")  
[![Gene FireTerror.png](/images/thumb/2/28/Gene_FireTerror.png/64px-Gene_FireTerror.png)](/wiki/File:Gene_FireTerror.png) | _Carriers of this gene have an intense fear of fire. When fires are close, there is a chance they will have a mental breakdown at any moment._ | Suppresses the [Pyromaniac](/wiki/Pyromaniac "Pyromaniac") trait   
[Kind instinct](/wiki/Kind_instinct "Kind instinct")  
[![Gene KindInstinct.png](/images/thumb/c/c5/Gene_KindInstinct.png/64px-Gene_KindInstinct.png)](/wiki/File:Gene_KindInstinct.png) | _Carriers of this gene are high in trait agreeableness and are very conscientious. They rarely insult others or starts fights, and will sometimes offer kind words to brighten the moods of those around them. They also never judge people by their appearance._ | Forces the [Kind](/wiki/Kind "Kind") trait   
[Inbred](/wiki/Inbred "Inbred")  
[![Gene Inbred.png](/images/thumb/f/f3/Gene_Inbred.png/64px-Gene_Inbred.png)](/wiki/File:Gene_Inbred.png) | _This genetic condition affects a person's fertility, immunity, and mental capacity._ | Forces the [Slow learner](/wiki/Slow_learner "Slow learner") trait   
[Psychically deaf](/wiki/Psychically_deaf "Psychically deaf")  
[![Gene PsychicallyDeaf.png](/images/thumb/b/bb/Gene_PsychicallyDeaf.png/64px-Gene_PsychicallyDeaf.png)](/wiki/File:Gene_PsychicallyDeaf.png) | _Carriers of this gene are deaf to all psychic energy and influence outside their own minds. They cannot be affected by psychic influence, nor can they ever wield psychic power._ | Forces the [Psychically deaf](/wiki/Psychically_deaf "Psychically deaf") trait   
[Psychically dull](/wiki/Psychically_dull "Psychically dull")  
[![Gene PsychicallyDull.png](/images/thumb/2/21/Gene_PsychicallyDull.png/64px-Gene_PsychicallyDull.png)](/wiki/File:Gene_PsychicallyDull.png) | _Carriers of this gene are less psychically-sensitive than others._ | Forces the [Psychically dull](/wiki/Psychically_dull "Psychically dull") trait   
[Delicate](/wiki/Delicate "Delicate")  
[![Gene Delicate.png](/images/thumb/c/c6/Gene_Delicate.png/64px-Gene_Delicate.png)](/wiki/File:Gene_Delicate.png) | _Carriers of this gene take greater injuries than others from the same damage. They have thin, brittle bones and less binding molecules in joints and flesh._ | Forces the [Delicate](/wiki/Delicate "Delicate") trait   
[Extra pain](/wiki/Extra_pain "Extra pain")  
[![Gene ExtraPain.png](/images/thumb/d/d7/Gene_ExtraPain.png/64px-Gene_ExtraPain.png)](/wiki/File:Gene_ExtraPain.png) | _Carriers of this gene feel more pain than others given the same injuries. Neuron activity in the brain's nociception center is amplified, so pain feels extra-intense and fiery. This can be protective, but overall it's considered a negative and makes it hard to push through difficult situations._ | Forces the [Wimp](/wiki/Wimp "Wimp") trait   
  
## General traits[[edit](/index.php?title=Traits&action=edit&section=5 "Edit section: General traits")]

These traits are generalized into groups, organized roughly by topic but there are no such groupings laid out formally in the game. There are no relations or prohibitions between traits grouped together here unless noted (e.g. a colonist cannot be both "ascetic", wanting a minimal bedroom, _and_ "jealous" of those with better bedrooms). 

### Lifestyle[[edit](/index.php?title=Traits&action=edit&section=6 "Edit section: Lifestyle")]

One likes what one likes... 

Name  | Description  | Effect  | Conflicting Traits  | Commonality  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---|---|---  
Night owl  | NAME likes to work at night. S/He gets a mood bonus if awake at night and mood loss if awake during the day. S/He doesn't get a mood penalty for being in the dark.  | + **:** Negates the −5 _Darkness_ [thought](/wiki/Thought "Thought") penalty from being in the dark  
+16 _Night owl at night_ [thought](/wiki/Thought "Thought") if awake during night (23:00 - 06:00)  
−10 _Night owl in daytime_ [thought](/wiki/Thought "Thought") if awake during day (11:00 - 18:00)  
| \-  | 1.3  | 5-10 [wake-up](/wiki/Wake-up "Wake-up")  
Undergrounder  | NAME has no need to experience the outdoors or light. S/He will never feel cooped up or get cabin fever, no matter how long s/he stays inside, and is not bothered by darkness.  | + **:** Negates the −5 _Darkness_ [thought](/wiki/Thought "Thought") penalty from being in the dark  
+ **:** No [Outdoors](/wiki/Outdoors "Outdoors") or Space [need](/wiki/Need "Need")  
− **:** Added [Indoors](/wiki/Indoors_\(need\) "Indoors \(need\)") need  
+3 _Undergrounder indoors_ [thought](/wiki/Thought "Thought") when indoors / +4 _Underground_ [thought](/wiki/Thought "Thought") when underground  
−3 _Undergrounder outdoors_ [thought](/wiki/Thought "Thought") when outdoors  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | \-  | 0.2  | 30-60 [raw fungus](/wiki/Raw_fungus "Raw fungus")  
Nudist  | NAME enjoys the feeling of freedom that comes from being nude. They can handle clothing, but will be happier without it.  | +20 _Happily nude_ [thought](/wiki/Thought "Thought") when naked  
−3 _Constraining clothes_ [thought](/wiki/Thought "Thought") mood penalty for wearing any apparel, except headgear, [utility](/wiki/Utility "Utility") items, and certain nudist-friendly items like [sashes](/wiki/Sash "Sash")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") and [heavy bandoliers](/wiki/Heavy_bandolier "Heavy bandolier").[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") + **:** No −10 [opinion](/wiki/Opinion "Opinion") loss of someone who has any uncovered body parts [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | \-  | 0.7  | \-   
Masochist  | For NAME, there's something exciting about getting hurt. S/He doesn't know why, S/He's just wired differently.  | +5**/** +10**/** +15**/** +20 _Masochist in pain_ [thought](/wiki/Thought "Thought") for being in a minor/serious/intense/mind-shattering [pain](/wiki/Pain "Pain"), replacing default −5/−10/−15/−20 and +3+5+7+9 from [Pain:Idealized](/wiki/Pain_\(precept\) "Pain \(precept\)").[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+3 _Masochist body strapped_ [thought](/wiki/Thought "Thought") while wearing a [slave body strap](/wiki/Slave_body_strap "Slave body strap")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+2 _Masochist collared_ [thought](/wiki/Thought "Thought") while wearing a [slave collar](/wiki/Slave_collar "Slave collar")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
**+/- :** Negates all mood effects for both [Skullspike: Desired and Disapproved](/wiki/Skullspike_\(precept\) "Skullspike \(precept\)")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+ **:** Negates the −5 _Fed on by OTHER_ [thought](/wiki/Thought "Thought") penalty and −20 [opinion](/wiki/Opinion "Opinion") malus from being fed on by a [Bloodfeeder](/wiki/Bloodfeeder "Bloodfeeder")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | Wimp | 0.5  | \-   
Body modder  | NAME feels limited in POSSESSIVE feeble human body. NAME often dreams of being enhanced by artificial body parts.  | +4**/** +7**/** +9**/** +11**/** +12**/** +13 _Body modder pleased_ [thought](/wiki/Thought "Thought") for having [artificial body parts](/wiki/Artificial_body_parts "Artificial body parts") and [xenogenes](/wiki/Xenogenes "Xenogenes").[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") Each artificial body part grants 1 stage, and having any xenogenes also grants 1 stage.  
−4 _Body modder frustrated_ [thought](/wiki/Thought "Thought") if lacking any artificial body parts or xenogenes[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")  
+8 opinion of other pawns per artificial body part they have, capped at +40. Any number of xenogenes[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") counts as one artificial body part.  | Body purist | 0.9  | \-   
Body purist  | NAME believes the human body is limited for a reason. To her/him, artificial body parts are unethical and disgusting.  | −10**/** −15**/** −20**/** −25**/** −30**/** −35 _Body purist squeamish_ [thought](/wiki/Thought "Thought") for having [artificial body parts](/wiki/Artificial_body_parts "Artificial body parts") and [xenogenes](/wiki/Xenogenes "Xenogenes").[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") Each artificial body part grants 1 stage, and having any xenogenes also grants 1 stage.  
−8 opinion of other pawns per artificial body part they have, capped at −40. Any number of xenogenes[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") counts as one artificial body part.  
−20 _Forced to take luciferium_ [thought](/wiki/Thought "Thought") for 6 [days](/wiki/Time "Time") when administered [luciferium](/wiki/Luciferium "Luciferium") and −30 opinion of the doctor who did the operation for 120 days. Despite the description of this thought, body purists can administer luciferium to themselves and do not lose mood for doing so.  | Body modder | 0.7  | \-   
Gourmand  | NAME's life revolves around food. S/He gets hungry quickly, and if s/he is in a bad mood, s/he will often satisfy her/his-self by eating.  | +4 [Cooking](/wiki/Cooking "Cooking") skill  
**+/- :** So long as there is >10 human-edible nutrition worth of food in storage, the only possible minor mental break is food binge  
+50% hunger rate  
− **:** Food binges randomly occur with an MTB of 50 days  | Ascetic | 1  | 1-3 [fine meals](/wiki/Fine_meal "Fine meal")  
  
### Living space[[edit](/index.php?title=Traits&action=edit&section=7 "Edit section: Living space")]

How a colonist perceives the walls that they call "home"... 

Name  | Description  | Effect  | Conflicting Traits  | Commonality  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---|---|---  
Ascetic  | NAME has forsaken physical comforts and enjoyments in favor of a simple, pure lifestyle. S/He will become unhappy if s/he has a bedroom that's too impressive. S/He also dislikes fancy food and prefers to eat raw. S/He never judges others by their appearance.  | + **:** Negates the −3 _Ate without table_ [thought](/wiki/Thought "Thought") penalty  
+5**/** +4**/** +3 _Ascetic has awful-mediocre bedroom_ [thought](/wiki/Thought "Thought") for having an [Awful/Dull/Mediocre](/wiki/Impressiveness "Impressiveness") bedroom  
−5 _Ascetic has impressive bedroom_ [thought](/wiki/Thought "Thought") for having a [Somewhat Impressive](/wiki/Impressiveness "Impressiveness") or better bedroom  
**+/- :** Mood not affected by quality of [meal](/wiki/Meal "Meal"), including [raw food](/wiki/Raw_food "Raw food"), [nutrient paste meals](/wiki/Nutrient_paste_meal "Nutrient paste meal"), [baby food](/wiki/Baby_food "Baby food")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC"), and any form of [twisted meat](/wiki/Twisted_meat "Twisted meat")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")  
**+/- :** Pawn beauty of others does not change pawn's social opinion on that pawn  
**+/- :** Mood unaffected by quality of crib (as a baby)[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")  
**+/- :** Mood unaffected by gaining a royal title; losing a title; or, if currently titled, whether or not apparel, bedroom, and/or throneroom is appropriate to the title [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
+ **:** Gains the [Minimal](/wiki/Psyfocus#Minimal "Psyfocus") meditation focus type[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
− **:** Loses the [Artistic](/wiki/Psyfocus#Artistic "Psyfocus") meditation focus type, if they had it[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
×50% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | Greedy  
Gourmand  
Jealous | 0.7  | \-   
Greedy  | NAME needs a really impressive bedroom. S/He gets a mood loss if they don't get what they want.  | −8 _Greedy for impressive bedroom_ [thought](/wiki/Thought "Thought") for not having a bedroom  
−8**/** −8**/** −6**/** −4 _Greedy for impressive bedroom_ [thought](/wiki/Thought "Thought") for having an [Awful/Dull/Mediocre/Decent](/wiki/Impressiveness "Impressiveness") bedroom  
− **:** [Conceited](/wiki/Titles#Conceited_pawns "Titles") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | Ascetic  
Jealous | 1  | 10-20 [gold](/wiki/Gold "Gold")  
Jealous  | For NAME, it's degrading to have a [less impressive](/wiki/Impressiveness "Impressiveness") bedroom than someone else. NAME gets a mood loss if any colonist has a more impressive bedroom.  | −8 _Jealous of OTHER's bedroom_ [thought](/wiki/Thought "Thought") for not having the most [impressive](/wiki/Impressiveness "Impressiveness") bedroom.  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
− **:** [Conceited](/wiki/Titles#Conceited_pawns "Titles") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | Ascetic  
Greedy | 1  | \-   
Pyromaniac  | NAME loves fire. S/He will never extinguish fires, and will occasionally go on random fire starting sprees. S/He will be happy around flames, and happier when wielding an incendiary weapon.  | +2 _Pyromaniac has incendiary weapon_ [thought](/wiki/Thought "Thought") while wielding a weapon from the following list: [incendiary launcher](/wiki/Incendiary_launcher "Incendiary launcher"), [molotov cocktails](/wiki/Molotov_cocktails "Molotov cocktails"), [plasmasword](/wiki/Plasmasword "Plasmasword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [persona plasmasword](/wiki/Persona_plasmasword "Persona plasmasword"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")[flamebow](/wiki/Flamebow "Flamebow"),[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") [hellcat rifle](/wiki/Hellcat_rifle "Hellcat rifle"),[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") [incinerator](/wiki/Incinerator "Incinerator"),[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") or [unique weapons](/wiki/Unique_weapons "Unique weapons")[![Content added by the Odyssey DLC](/images/thumb/7/7b/OdysseyIcon.png/16px-OdysseyIcon.png)](/wiki/Odyssey_\(DLC\) "Content added by the Odyssey DLC") with certain traits.  
+8 _Used flame weapon_ [thought](/wiki/Thought "Thought") for 0.33 [days](/wiki/Time "Time") mood bonus for using a flame weapon either directly on a visible, non-downed enemy of the player faction who is not in a fogged region of the map, or attacking with it when such a pawn is in range of the attack anyways. This includes any weapon from the list above except for the [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")hellcat rifle.  
+2 _Beautiful fire_ [thought](/wiki/Thought "Thought"): grants 1 stack per [fire](/wiki/Fire "Fire") or lit building capable of having a 'fire overlay' ([torch lamp](/wiki/Torch_lamp "Torch lamp"), [campfire](/wiki/Campfire "Campfire"), [blood torch](/wiki/Blood_torch "Blood torch"),[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") [darktorch](/wiki/Darktorch "Darktorch"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [fungus darktorch](/wiki/Fungus_darktorch "Fungus darktorch"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [effigy](/wiki/Effigy "Effigy"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [pyre](/wiki/Pyre "Pyre"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [sacrificial flag](/wiki/Sacrificial_flag "Sacrificial flag"),[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") [brazier](/wiki/Brazier "Brazier"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") or [darklight brazier](/wiki/Darklight_brazier "Darklight brazier")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")) within 8 cells, within the same room, and not in a 'fogged' region of the map invisible to the player. Fire not from a lit building, and not on a pawn, grants 2 stacks of this mood bonus; each cell occupied by a lit pyre counts as 1 fire, granting up to 4 stacks in total.  
Incapable of firefighting  
Only possible [extreme mental break](/wiki/Extreme_break "Extreme break") is [fire starting spree](/wiki/Fire_starting_spree "Fire starting spree")  
− **:** Fire starting sprees randomly occur with an MTB of 50 days  
−20% [Market Value](/wiki/Market_Value "Market Value")  
+ **:** Gains the [Flame](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | \-  | 0.8  | [Molotov cocktails](/wiki/Molotov_cocktails "Molotov cocktails")  
10-20 [chemfuel](/wiki/Chemfuel "Chemfuel")  
  
### Social views[[edit](/index.php?title=Traits&action=edit&section=8 "Edit section: Social views")]

In a brutal world, what otherwise might be socially unacceptable or even unthinkable can be a positive survival trait for both you and your fellow colonists... See [Human resources](/wiki/Human_resources "Human resources") for comparative analysis. 

Name  | Description  | Effect  | Conflicting Traits  | Commonality  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---|---|---  
Bloodlust  | NAME gets a rush from hurting people, and never minds the sight of blood or death.  | + **:** Negates all mood penalties for: Observing fresh corpses, Observing rotting corpses, Human butchering, Organ harvesting, Executions, Colonist/innocent prisoner deaths, Wearing tainted clothes; [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Blinding ceremonies from [Blindness: Horrible](/wiki/Blindness_\(precept\) "Blindness \(precept\)"), or Scarification ceremonies from [Scarification:Horrible](/wiki/Scarification "Scarification")  
+ **:** No opinion loss of someone who Harvests an organ, Executes a prisoner, or [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")Kills a child  
+2**/** +4**/** +6**/** +8 _Human leather APPAREL_NAME_ [thought](/wiki/Thought "Thought") for wearing 1/2/3/4+ apparel items made out of human skin.  
+4 _Bloodlust organ harvested_ [thought](/wiki/Thought "Thought") for 4 [days](/wiki/Time "Time") on harvesting an organ.  
+8 _Witnessed death with bloodlust_ [thought](/wiki/Thought "Thought") for 4 [days](/wiki/Time "Time") on witnessing a human death. Witnessing means being awake, sighted, and either in the same caravan as the deceased or having line of sight within 12 cells of the deceased.  
+12 _Killed someone_ [thought](/wiki/Thought "Thought") for 4 [days](/wiki/Time "Time") on killing a human.  
− **:** Four times as likely to start a social fight  
+ **:** Unaffected by ideoligious prohibitions that would ordinarily prevent a pawn from executing prisoners [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | _Requires pawn to be[capable of Violence](/wiki/Incapable "Incapable")_ | 0.8  | [Axe](/wiki/Axe "Axe")[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
[Longsword](/wiki/Longsword "Longsword")  
Cannibal  | NAME was taught that eating human meat is wrong and horrible. But one time, long ago, S/He tried it... and S/He liked it.  | + **:** No mood penalty for: Observing fresh corpses, Human butchering, Guest or guilty prisoner deaths, Cannibalism; [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")Ingesting hemogen packs; or [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Eating meat from [Abhorrent, Horrible, or Disapproved](/wiki/Meat_eating "Meat eating")  
+2**/** +4**/** +6**/** +8 _Human leather APPAREL_NAME_ [thought](/wiki/Thought "Thought") for wearing 1/2/3/4+ apparel items made out of human skin.  
+15 _Cooked cannibalism_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") on eating a meal made with human flesh  
+20 _Raw cannibalism_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") on eating raw [human meat](/wiki/Human_meat "Human meat") (including human corpses, although this may still trigger the −12 _Ate corpse_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") penalty)  
+ **:** No opinion loss of someone who Eats meat ([Abhorrent, Horrible, or Disapproved](/wiki/Meat_eating "Meat eating")) [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type. [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | \-  | 0.6  | 30-60 [human meat](/wiki/Human_meat "Human meat")  
Psychopath  | NAME has no empathy. The suffering of others doesn't bother them at all. They don't mind if others are butchered, left unburied, imprisoned, or sold to slavery - unless it affects them. NAME also feels no mood boost from socializing.  | + **:** No mood penalty for: Observing fresh corpses, Human butchering, Organ harvesting, Executions, Unburied colonists, Prisoners sold into slavery, Relative/colonist/friend/innocent prisoner deaths, Not being a bonded animal's master, Loss/death/release of bonded pets, Wearing [human leather](/wiki/Human_leather "Human leather") or [dread leather](/wiki/Dread_leather "Dread leather")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC"); [Child](/wiki/Child "Child")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") killing, Being in a colony with sad youngsters, Having a sad/enslaved/sick/growth vat-interred child, Not having had enough play (as a baby); [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Blinding ceremonies from [Blindness: Horrible](/wiki/Blindness_\(precept\) "Blindness \(precept\)"), Scarification ceremonies from [Scarification: Horrible](/wiki/Scarification "Scarification"), or Killing innocent animals from [Killing innocent animals: Abhorrent, Horrible, or Disapproved](/wiki/Killing_innocent_animals "Killing innocent animals")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC")Participating in [Philophagy](/wiki/Philophagy "Philophagy") and [Chronophagy](/wiki/Chronophagy "Chronophagy") rituals[-ve only?]  
+ **:** No opinion loss of someone who [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")Kills a child or [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")Kills an innocent animal ([Killing innocent animals:Abhorrent, Horrible, or Disapproved](/wiki/Killing_innocent_animals "Killing innocent animals"))  
− **:** No mood bonuses from: Being nuzzled, Being a bonded animal's master; [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")Being in a colony with happy youngsters, Having happy children, Having happy parents (as a child), or Having had lots of play (as a baby)  
− **:** No opinion gain from Chitchat, Deep talk (still loses opinion from hostile interactions); [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")Teaching a child, or Taking a lesson (as a child)  
**+/- :** Prevents bonding with animals  
+ **:** Unaffected by ideoligious prohibitions that would ordinarily prevent a pawn from executing prisoners or attacking innocent animals [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Morbid "Psyfocus") meditation focus type, replacing the Artistic meditation focus type if they had it [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
×50% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | Kind | 1  | 1 [skull](/wiki/Skull "Skull")  
1 [heart](/wiki/Heart "Heart")  
  
  


### Combat[[edit](/index.php?title=Traits&action=edit&section=9 "Edit section: Combat")]

When it's us or them... 

Name  | Description  | Effect  | Conflicting Traits  | Commonality  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---|---|---  
Nimble  | NAME has remarkable kinesthetic intelligence. S/He seems to dance around danger with preternatural grace.  | +15 [Melee Dodge Chance](/wiki/Melee_Dodge_Chance "Melee Dodge Chance")  
×10% [Trap Spring Chance](/wiki/Trap_Spring_Chance "Trap Spring Chance") | \-  | 1  | \-   
Brawler  | NAME likes to fight up close and personal. S/He's accuracy is greatly increased in melee combat, but s/he'll be very unhappy if asked to carry a ranged weapon.  | +4 [Melee](/wiki/Melee "Melee") skill  
−10 [Shooting](/wiki/Shooting "Shooting") skill  
+4 [Melee Hit Chance](/wiki/Melee_Hit_Chance "Melee Hit Chance")  
−10 _Brawler has ranged weapon_ [thought](/wiki/Thought "Thought") while wielding a ranged weapon  
− **:** Disallows [shooting](/wiki/Shooting "Shooting") [passions](/wiki/Passion "Passion")  
**+/- :** Disallows [Shoot frenzy](/wiki/Shoot_frenzy "Shoot frenzy") inspiration  | Trigger-happy  
Careful Shooter   
Wimp | 1  | 1 [knife](/wiki/Knife "Knife")  
Tough  | NAME has thick skin, dense flesh, and durable bones. S/He takes much less damage than other people from the same blows. S/He is extremely hard to kill.  | ×50% [Incoming Damage Multiplier](/wiki/Incoming_Damage_Multiplier "Incoming Damage Multiplier")

  * Stacks multiplicatively with other Incoming Damage Multiplier factors. See that page for further details.

| Delicate | 1.1  | \-   
Wimp[1] | NAME is weak and cowardly. Even a little pain will immobilize her/him.  | −50% [Pain Shock Threshold](/wiki/Pain_Shock_Threshold "Pain Shock Threshold")  
−15% [Market Value](/wiki/Market_Value "Market Value")  
×200% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
− **:** Negates [Pain](/wiki/Pain "Pain") mood buffs from [Pain: Idealized](/wiki/Pain_\(precept\) "Pain \(precept\)") ,[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") reverting mood from pain to the default values.  | Brawler  
Masochist | 1  | \-   
Delicate [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | NAME has fragile skin and bones. She/He takes more damage than other people from the same blows.  | ×115% [Incoming Damage Multiplier](/wiki/Incoming_Damage_Multiplier "Incoming Damage Multiplier")

  * Stacks multiplicatively with other Incoming Damage Multiplier factors. See that page for further details. Note that the [Delicate](/wiki/Delicate_\(gene\) "Delicate \(gene\)") gene that can add this trait is incompatible with the [Robust](/wiki/Robust "Robust") gene.[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")

| Tough | 1  | \-   
  
  1. ↑ With the exception of [Genies](/wiki/Genies "Genies") (who have a gene which forces the Wimp trait), hostiles cannot spawn with the Wimp trait.



  * See also [Trigger-happy](/wiki/Trigger-happy "Trigger-happy") and [Careful shooter](/wiki/Careful_shooter "Careful shooter"), below.



### Skills[[edit](/index.php?title=Traits&action=edit&section=10 "Edit section: Skills")]

When your colonists are _not_ fighting for their lives... 

Name  | Description  | Effect  | Conflicting Traits  | Commonality  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---|---|---  
Too smart  | NAME is too smart for her/his own good. S/He learns everything much faster than everyone, but can be quite eccentric.  | +75% [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor")  
+12% [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold")  
×50% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | Nerves spectrum traits  
 _Requires pawn to be capable of[Intellectual](/wiki/Skills "Skills")_ | 1  | 1 [schematic](/wiki/Schematic "Schematic")  
Fast learner  | NAME has a knack for learning. S/He picks things up much faster than others.  | +75% [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor") | Slow Learner | 1  | 1 [textbook](/wiki/Textbook "Textbook")  
Slow learner  | NAME is slow on the uptake. S/He picks things up much slower than others.  | −75% [Global Learning Factor](/wiki/Global_Learning_Factor "Global Learning Factor")  
×50% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | Fast Learner | 1  | \-   
Quick sleeper  | NAME doesn't need as much sleep as the average person. Whether s/he's sleeping on a bed or on the ground, s/he will be fully rested in about two thirds the usual time.  | +50% [Rest Rate Multiplier](/wiki/Rest_Rate_Multiplier "Rest Rate Multiplier") | \-  | 1.1  | \-   
Great memory  | NAME has a fantastic memory for detail. S/He will lose unused skills at half the rate of other people.  | ×50% Skill loss rate  | \-  | 1.1  | \-   
Tortured artist  | NAME feels alienated and misunderstood by other human beings. S/He will get a constant mood debuff, but gain a chance (50%) to get a creativity inspiration after a mental break.  | 50% chance of receiving the [mental inspiration](/wiki/Mental_inspiration "Mental inspiration") "[Inspired creativity](/wiki/Inspired_creativity "Inspired creativity")" after a mood-caused [mental break](/wiki/Mental_break "Mental break") other than [Catatonia](/wiki/Catatonic_breakdown "Catatonic breakdown") or [Run wild](/wiki/Run_wild "Run wild") ends.  
−8 _Tortured artist_ [thought](/wiki/Thought "Thought") (permanent)  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type.[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") NOTE: Inspirations from this trait cannot be triggered by mental breaks caused by any reason other than mood, e.g. [psychic insanity lances](/wiki/Psychic_insanity_lance "Psychic insanity lance"), [psycasts](/wiki/Psycasts "Psycasts"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") [genes](/wiki/Genes "Genes"),[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") [void terror](/wiki/Void_terror "Void terror"),[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") or even randomly-induced mental breaks from other traits. [Cube sculpting](/wiki/Golden_cube#Cube_sculptures "Golden cube")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") and [tomes](/wiki/Tome "Tome")[![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") are the sole exceptions to this rule. Ending the [mental break](/wiki/Mental_break "Mental break") early by [arresting](/wiki/Prisoner#Capturing_prisoners "Prisoner") the colonist will not grant [Inspired creativity](/wiki/Inspired_creativity "Inspired creativity").  | \-  | 0.6  | 10-20 [dye](/wiki/Dye "Dye")  
  
### Relationships[[edit](/index.php?title=Traits&action=edit&section=11 "Edit section: Relationships")]

"Hey, baby. Come around often?" "Crashed here. Can't leave." "...My bad." 

Name  | Description  | Effect  | Conflicting Traits  | Commonality   
---|---|---|---|---  
Kind  | NAME is an exceptionally agreeable and giving person. S/He never insults others and will sometimes offer kind words to brighten the moods of those around her/him. S/He also never judges people by their appearance.  | + **:** Can use a unique 'Kind Words' social interaction, inflicting +5 _Kind words_ [thought](/wiki/Thought "Thought") for 2 [days](/wiki/Time "Time") and gaining +15 opinion from the recipient for 20 days. The opinion boost can stack up to 10 times from the same Kind pawn with 0.9x stacked effect multiplier (for a potential opinion bonus of up to +97.7), and up to 300 stacks can be present overall. When choosing what social interaction to perform, Kind Words has a weighting of 0.01 (as opposed e.g. to chitchat's weighting of 1.00).  
+ **:** Will not Slight or Insult others  
+ **:** Opinion of other pawns not changed by [beauty](/wiki/Beauty_\(pawn\) "Beauty \(pawn\)"), Annoying voice, Creepy breathing or [disfigurement](/wiki/Disfigurement "Disfigurement")  
×200% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") | Abrasive  
Psychopath | 2   
Abrasive  | NAME always says exactly what's on their mind, especially if it's bugging him/her. That tends to rub people the wrong way.  | − **:** 2.3x as likely to Slight or Insult others  
−15% [Market Value](/wiki/Market_Value "Market Value")  
×50% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")  
− **:** [Conceited](/wiki/Titles#Conceited_pawns "Titles") [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") | Kind  
 _Requires pawn to be capable of[Social](/wiki/Skills#Social "Skills")_ | 1   
Annoying voice  | NAME's voice has a particularly grating, nasal quality to it, and tends to talk in barked, garbled phrases. This predisposes others to dislike them.  | −25 [opinion](/wiki/Opinion "Opinion") from non-Kind, non-[deaf](/wiki/Hearing "Hearing") pawns  
−20% [Market Value](/wiki/Market_Value "Market Value") | \-  | 0.5   
Creepy breathing  | NAME breathes heavily all the time, and sweats constantly. People find it creepy.  | −25 [opinion](/wiki/Opinion "Opinion") from non-Kind, non-[deaf](/wiki/Hearing "Hearing") pawns  
−10% [Market Value](/wiki/Market_Value "Market Value") | \-  | 0.5   
Misandrist  | NAME really dislikes and distrusts men.  | −25 [opinion](/wiki/Opinion "Opinion") of men  |  | 0.3 for men  
1.7 for women   
Misogynist  | NAME really dislikes and distrusts women.  | −25 [opinion](/wiki/Opinion "Opinion") of women  |  | 1.7 for men  
0.3 for women   
Asexual  | NAME has no sexual attraction to anyone at all.  | **+/- :** Will not have romantic relationships with people.  | Gay  
Bisexual | 0.2   
Gay  | NAME is romantically attracted to people of their own gender.  | **+/- :** Will only have romantic relationships with people of the same gender.  | Asexual  
Bisexual | 0.3   
Bisexual  | NAME is romantically attracted to both men and women.  | **+/- :** Will have romantic relationships with people from either gender.  | Asexual  
Gay | 0.2   
Recluse [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") | The fewer people in NAME's faction, the happier she/he is. Being alone is best of all.  | + **:** Negates the −3 _Denied joining_ [thought](/wiki/Thought "Thought") for 6 [days](/wiki/Time "Time") penalty from rejecting a pawn that wants to join the colony  
**+/- :** Mood based on the number of human pawns (including children, guests, and prisoners) in the colony. Humans on other maps, in caravans or inside a [Cryptosleep casket](/wiki/Cryptosleep_casket "Cryptosleep casket")/[Transport pod](/wiki/Transport_pod "Transport pod")/[Biosculpter pod](/wiki/Biosculpter_pod "Biosculpter pod") [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC")/[Growth vat](/wiki/Growth_vat "Growth vat") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")/[Gene extractor](/wiki/Gene_extractor "Gene extractor") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")/[Subcore softscanner](/wiki/Subcore_softscanner "Subcore softscanner") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")/[Subcore ripscanner](/wiki/Subcore_ripscanner "Subcore ripscanner") [![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") do not count. [Ghouls](/wiki/Ghoul "Ghoul") [![Content added by the Anomaly DLC](/images/thumb/3/32/AnomalyIcon.png/16px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Content added by the Anomaly DLC") do not count.  
Starting colonists in the [The Mechanitor](/wiki/Scenario_system#Default_Scenarios "Scenario system") start scenario will always have this trait.  | Human Count | Mood | Human Count | Mood   
---|---|---|---  
1 | +12 | 11 | −2  
2 | +8 | 12 | −3  
3 | +6 | 13 | −4  
4 | +4 | 15 | −6  
5-10 | 0 | 16+ | −8  
\-  | 0.5   
  
  * The Gay/Bisexual/Asexual sexuality traits are unique in that they are the only ones that can generate after the 3 trait limit, resulting in rare pawns with 4 traits.
  * See also the Beauty category of traits, below.



## Spectrum traits[[edit](/index.php?title=Traits&action=edit&section=12 "Edit section: Spectrum traits")]

Theses are groups of related traits, that are inter-related and grouped by degree, creating a "spectrum" of good/bad/better/worse in that specific sphere of behaviour. A colonist can only have one trait from any single related spectrum for these traits, defining whether they are notably outside the norm for, for example, movement speed, or drug interest, or their physical (un)attractiveness. 

### Drug desire[[edit](/index.php?title=Traits&action=edit&section=13 "Edit section: Drug desire")]

These traits affect a colonist's likelihood to consume drugs. 

Note that despite the common misconception, chemical fascination and interest pawns no longer randomly go on [drug binges](/wiki/Mental_break "Mental break") independent of [mood](/wiki/Mood "Mood"). 

Name  | Description  | Effect   
---|---|---  
Chemical fascination  | NAME is utterly fascinated with chemical sources of enjoyment. Consuming recreational drugs will create a good mood, while abstaining will lead to increasing frustration over time and possibly drug binges. S/He will ignore directives to not use recreational drugs, and will consume more than a normal person.  | Has [Chemical need](/wiki/Chemical_need "Chemical need"): causes −4**/** −8**/** −12 _Chemical hunger_ [thought](/wiki/Thought "Thought") the longer it has gone unsatisfied, and up to +3**/** +6 _Chemical satisfaction_ [thought](/wiki/Thought "Thought") when satisfied For [Beer](/wiki/Beer "Beer"), [Smokeleaf joints](/wiki/Smokeleaf_joint "Smokeleaf joint"), and [Ambrosia](/wiki/Ambrosia "Ambrosia") only: functions as if "Take for Recreation" and "Take for Addiction" are checked on the [Drug Policies](/wiki/Drug_policy "Drug policy") tab regardless of the players choices. They will otherwise follow the Drug Policy regarding drugs carried and scheduled. NOTE: The colonist will still respect allowed areas and will not use forbidden stacks of any drug regardless of chemical need Unaffected by ideoligious prohibitions that would ordinarily prevent a pawn from taking or administering drugs [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") −30 [opinion](/wiki/Opinion "Opinion") of any pawns with teetotaler   
Chemical interest  | NAME has an unusual interest in chemical sources of enjoyment. Consuming recreational drugs will create a good mood, while abstaining will lead to increasing frustration over time and possible drug binges. S/He will ignore directives to not use recreational drugs, and will consume more than a normal person.  | Has [Chemical need](/wiki/Chemical_need "Chemical need"): causes −2**/** −4**/** −6 _Chemical hunger_ [thought](/wiki/Thought "Thought") the longer it has gone unsatisfied, and up to +1**/** +3 _Chemical satisfaction_ [thought](/wiki/Thought "Thought") when satisfied For [Beer](/wiki/Beer "Beer"), [Smokeleaf joints](/wiki/Smokeleaf_joint "Smokeleaf joint"), and [Ambrosia](/wiki/Ambrosia "Ambrosia") only: functions as if "Take for Recreation" and "Take for Addiction" are checked on the [Drug Policies](/wiki/Drug_policy "Drug policy") tab regardless of the players choices. They will otherwise follow the Drug Policy regarding drugs carried and scheduled. NOTE: The colonist will still respect allowed areas and will not use forbidden stacks of any drug regardless of chemical need [![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") Unaffected by ideoligious prohibitions that would ordinarily prevent a pawn from taking or administering drugs −20 [opinion](/wiki/Opinion "Opinion") of any pawns with teetotaler   
Teetotaler  | NAME abhors the idea of gaining pleasure from chemicals. S/He strictly avoids alcohol and recreational drugs.  | Will not go on drug binges  
Cannot be directed to take non-medical drugs unless they have a [genetic dependency](/wiki/Genes#Alcohol_dependency "Genes")[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC")  
−20 _Forced to take drugs_ [thought](/wiki/Thought "Thought") for 6 [days](/wiki/Time "Time") when administered a drug, and −30 opinion of the doctor who did the operation for 60 days.  
−25 [opinion](/wiki/Opinion "Opinion") of any pawns with any addiction −20 [opinion](/wiki/Opinion "Opinion") of any pawns with chemical interest −30 [opinion](/wiki/Opinion "Opinion") of any pawns with chemical fascination   
  
### Industriousness[[edit](/index.php?title=Traits&action=edit&section=14 "Edit section: Industriousness")]

These traits affect the colonist's [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed"). 

Name  | Description  | Effect   
---|---|---  
Industrious  | NAME has an easy time staying on-task and focused, and gets things done much faster than the average person.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") +35% −5 [opinion](/wiki/Opinion "Opinion") of any pawns without the same trait or hard worker −20 [opinion](/wiki/Opinion "Opinion") of any pawns with lazy −30 [opinion](/wiki/Opinion "Opinion") of any pawns with slothful   
Hard worker  | NAME is a natural hard worker and will finish tasks faster than most.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") +20% −5 [opinion](/wiki/Opinion "Opinion") of any pawns without the same trait or industrious −20 [opinion](/wiki/Opinion "Opinion") of any pawns with lazy −30 [opinion](/wiki/Opinion "Opinion") of any pawns with slothful   
Lazy  | NAME is a little bit lazy.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") −20%  
Slothful  | NAME loves idleness and hates anything productive. S/He moves slowly and rarely stays focused on a task.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") −35%  
  
### Speed traits[[edit](/index.php?title=Traits&action=edit&section=15 "Edit section: Speed traits")]

These traits affect a colonist's walk speed. 

Name  | Description  | Effect   
---|---|---  
Jogger  | NAME always moves with a sense of urgency - so much so that others often fail to keep up.  | [Move speed](/wiki/Move_speed "Move speed") +0.4 c/s  
Fast walker  | NAME likes to be where s/he's going. S/He walks quicker than most people.  | [Move speed](/wiki/Move_speed "Move speed") +0.2 c/s  
Slowpoke  | NAME is always falling behind the group whenever s/he goes anywhere.  | [Move speed](/wiki/Move_speed "Move speed") −0.2 c/s Disallows [Go Frenzy Inspiration](/wiki/Go_frenzy "Go frenzy")  
  
### Base mood[[edit](/index.php?title=Traits&action=edit&section=16 "Edit section: Base mood")]

These traits affect the colonist's natural, constant mood. 

Name  | Description  | Effect   
---|---|---  
Sanguine  | NAME is just naturally upbeat about HER/HIS situation, pretty much all the time, no matter what it is.  | +12 _Sanguine_ [thought](/wiki/Thought "Thought") (permanent)   
Optimist  | NAME is naturally optimistic about life. It's hard to get HER/HIM down.  | +6 _Optimist_ [thought](/wiki/Thought "Thought") (permanent)   
Pessimist  | NAME tends to look on the bad side of life.  | −6 _Pessimist_ [thought](/wiki/Thought "Thought") (permanent)   
Depressive  | NAME is perennially unhappy. S/He has trouble sustaining a good mood even when everything is fine.  | −12 _Depressive_ [thought](/wiki/Thought "Thought") (permanent)   
  
### Nerves[[edit](/index.php?title=Traits&action=edit&section=17 "Edit section: Nerves")]

These traits affect the colonist's mental break threshold. Mutually exclusive with [Too smart](/wiki/Too_smart "Too smart"). 

Name  | Description  | Effect   
---|---|---  
Iron-willed  | NAME's will is an iron shield. S/He keeps going through thick and thin, when others broke down long before.  | [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") −18% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") ×25%  
Steadfast  | NAME is mentally tough and won't break down under stresses that would crack most people.  | [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") −9% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") ×50%  
Nervous  | NAME tends to crack under pressure.  | [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") +8% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") ×200%  
Volatile  | NAME is on a hair-trigger all the time. S/He is the first to break in any tough situation.  | [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") +15% [Global Certainty Loss Factor](/wiki/Global_Certainty_Loss_Factor "Global Certainty Loss Factor")[![Content added by the Ideology DLC](/images/thumb/9/94/IdeologyIcon.png/16px-IdeologyIcon.png)](/wiki/Ideology_DLC "Content added by the Ideology DLC") ×300%  
  
### Neurotic[[edit](/index.php?title=Traits&action=edit&section=18 "Edit section: Neurotic")]

These traits affect the colonist's [mental break threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") and their [global work speed](/wiki/Global_Work_Speed "Global Work Speed"). 

Name  | Description  | Effect   
---|---|---  
Neurotic  | NAME likes to have things squared away. S/He will work harder than most to attain this state of affairs, but HER/HIS nerves can get the better of HER/HIM.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") +20% [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") +8%  
Very neurotic  | NAME feels constantly nervous about everything that has to get done. S/He will work extremely hard to attain this state of affairs, but HER/HIS nerves can easily get the better of HER/HIM.  | [Global Work Speed](/wiki/Global_Work_Speed "Global Work Speed") +40% [Mental Break Threshold](/wiki/Mental_Break_Threshold "Mental Break Threshold") +14%  
  
### Shooting accuracy[[edit](/index.php?title=Traits&action=edit&section=19 "Edit section: Shooting accuracy")]

These traits affect the colonist's [accuracy](/wiki/Shooting_Accuracy "Shooting Accuracy") in ranged combat, as well as [aiming time](/wiki/Aiming_Time "Aiming Time"). Mutually exclusive with brawler. 

Name  | Description  | Effect  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---  
Careful shooter  | NAME takes more time to aim when shooting. S/He shoots less often than others, but with more accuracy.  | [Aiming Time](/wiki/Aiming_Time "Aiming Time") +25% [Shooting Accuracy](/wiki/Shooting_Accuracy "Shooting Accuracy") +5 | 1 [bolt-action rifle](/wiki/Bolt-action_rifle "Bolt-action rifle")  
Trigger-happy  | Pew! Pew! Pew! NAME just likes pulling the trigger. S/He shoots faster than others, but less accurately.  | [Aiming Time](/wiki/Aiming_Time "Aiming Time") −50% [Shooting Accuracy](/wiki/Shooting_Accuracy "Shooting Accuracy") −5 | 1 [autopistol](/wiki/Autopistol "Autopistol")  
  
### Beauty[[edit](/index.php?title=Traits&action=edit&section=20 "Edit section: Beauty")]

Main article: [Beauty (Pawn)](/wiki/Beauty_\(Pawn\) "Beauty \(Pawn\)")

These traits influence a colonist's appearance and how it affects other colonists' opinions of them - as well as sexual attractiveness. 

Each point of beauty corresponds to +20 opinion from other colonists, e.g. a colonist with 2 beauty will have +40 opinion, while another with -1 beauty will have -20. 

Name  | Description  | Effect   
---|---|---  
Beautiful  | NAME is exceptionally beautiful, with an exotic-yet-familiar facial structure and an arresting gaze. People are attracted to her/him before s/he even opens her/his mouth.  | +2 Pawn Beauty   
Pretty  | NAME has a pretty face, which predisposes people to like her/him.  | +1 Pawn Beauty   
Ugly  | NAME is somewhat ugly. This subtly repels others during social interactions.  | −1 Pawn Beauty   
Staggeringly ugly  | NAME is staggeringly ugly. Her/His face looks like a cross between a drawing by an untalented child, a malformed fetus in a jar of formaldehyde, and a piece of modern art. Others must exert conscious effort to look at her/him while conversing.  | −2 Pawn Beauty   
  
### Psychic sensitivity[[edit](/index.php?title=Traits&action=edit&section=21 "Edit section: Psychic sensitivity")]

These traits influence how much a colonist is affected by psychic phenomena. 

Name  | Description  | Effect  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---  
Psychically hypersensitive  | NAME's mind is like a psychic tuning fork. S/He is extremely sensitive to psychic phenomena.  | +80% [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") | 1 [psychic foil helmet](/wiki/Psychic_foil_helmet "Psychic foil helmet")  
Psychically sensitive  | NAME's mind is unusually sensitive to psychic phenomena.  | +40% [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") | 1 [psychic foil helmet](/wiki/Psychic_foil_helmet "Psychic foil helmet")  
Psychically dull  | NAME's mind is psychically out of tune with others. S/He isn't as affected by psychic phenomena.  | −50% [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") | \-   
Psychically deaf  | NAME's mind works on a psychic frequency different from everyone else. S/He just isn't affected by psychic phenomena.  | −100% [Psychic Sensitivity](/wiki/Psychic_Sensitivity "Psychic Sensitivity") | \-   
  
### Immunity[[edit](/index.php?title=Traits&action=edit&section=22 "Edit section: Immunity")]

These traits influence how often colonists are infected by a disease. 

Name  | Description  | Effect  | [Possessions](/wiki/Traits#Starting_possessions "Traits")  
---|---|---|---  
Super-immune  | NAME has a naturally powerful immune system. S/He will gain immunity much faster than a normal person would, and can survive illnesses that would kill others.  | [Immunity Gain Speed](/wiki/Immunity_Gain_Speed "Immunity Gain Speed") +30% | \-   
Sickly  | NAME has an awful immune system. S/He gets sick more often than usual, frequently with illnesses that nobody in the colony has been afflicted by.  | [Medical skill](/wiki/Medical "Medical") +4  
Randomly catches diseases independently from rest of the colony, with an MTB of 30 days. The caught disease is one that can be randomly acquired in the current biome, using the same weighting system as normal random disease incidents.  | 2-5 [medicine](/wiki/Medicine "Medicine")  
5-10 [penoxycyline](/wiki/Penoxycyline "Penoxycyline")  
  
## Creepjoiner traits[[edit](/index.php?title=Traits&action=edit&section=23 "Edit section: Creepjoiner traits")]

[![AnomalyIcon.png](/images/thumb/3/32/AnomalyIcon.png/40px-AnomalyIcon.png)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)") | **This section relates to content added by[Anomaly (DLC)](/wiki/Anomaly_\(DLC\) "Anomaly \(DLC\)").** Please note that it will not be present without the [DLC](/wiki/Downloadable_content "Downloadable content") enabled.  
---|---  
  
These traits are never randomly assigned to pawns. They are normally found on [creepjoiners](/wiki/Creepjoiner "Creepjoiner"), and therefore have powerful positive or negative effects to balance out the other strengths and weaknesses creepjoiners have. 

### Positive traits[[edit](/index.php?title=Traits&action=edit&section=24 "Edit section: Positive traits")]

These traits are considered benefits, to compensate whatever mysterious downside haunts the creepjoiner. 

Name  | Description  | Effect   
---|---|---  
Perfect memory  | NAME has outstanding memory, both in terms of retaining information but also muscle memory. His/Her skills will never decay.  | Skills cannot decay  
Always and only spawns on creepjoiners with the "Perfect Human" benefit, which also comes with the Industrious trait and a starting level of 14-18 for each skill.   
Occultist  | NAME has deep knowledge of the twisted patterns of dark psychic energy. S/He can study unnatural entities faster than others. S/He will also periodically teach this inhuman knowledge to others when s/he gets the chance.  | [Study Efficiency](/wiki/Study_Efficiency "Study Efficiency") +100%  
[Entity Study Rate](/wiki/Entity_Study_Rate "Entity Study Rate") +50%  
Can perform an "occult teaching" random social interactions, giving +1 dark research. This has a cooldown of 1 day; when off cooldown, it will always be the next random social interaction chosen.   
Joyous  | NAME has the ability to make everyone feel better and inspire them to be the best version of themselves.  | +20 opinion from other pawns  
While not imprisoned or enslaved, +3 mood to all other non-prisoner colonists on the same map who are not currently in a mental break. The effect does not stack even if there are multiple Joyous pawns present. Pawns not of the player's faction cannot receive the mood buff. A Joyous pawn will not grant its mood bonus to anyone it is currently hostile to.  
Always and only spawns on creepjoiners with the "Joybringer" benefit, which precludes the "Disturbing" downside.   
Body mastery  | NAME doesn't have basic needs like eating, sleeping, or comfort. His/Her body is driven by some unknown mechanism, which has turned his/her eyes completely white.  | [Food](/wiki/Saturation "Saturation"), [Sleep](/wiki/Sleep "Sleep"), and [Comfort](/wiki/Comfort "Comfort") needs disabled. 

  * If all pawns in a [caravan](/wiki/Caravan "Caravan") have either this trait, a [circadian half-cycler](/wiki/Circadian_half-cycler "Circadian half-cycler"),[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC") or the [never sleep](/wiki/Never_sleep "Never sleep") gene,[![Content added by the Biotech DLC](/images/thumb/7/73/BiotechIcon.png/16px-BiotechIcon.png)](/wiki/Biotech_\(DLC\) "Content added by the Biotech DLC") and they travel without animals, they don't need to [stop at night](/wiki/Caravan#Caravan_schedule "Caravan").

Note: Because a pawn's mood is partially averaged by their needs, having less needs can render them more prone to mood swings.   
Eyes are white   
  
### Negative traits[[edit](/index.php?title=Traits&action=edit&section=25 "Edit section: Negative traits")]

These traits are downsides, meant to counterblance the creepjoiner's powerful benefits. Note that, unlike most other creepjoiner drawbacks, these traits are never hidden; as such, you be assured there are no other nasty surprises waiting for you. 

Name  | Description  | Effect   
---|---|---  
Disturbing  | NAME is a peculiar person who seems fixated on horrendous ideas. Talking to him/her is often upsetting.  | − **:** Only ever selects the "strange chat" type when doing random social interactions, giving −2 _OTHER rambling_ [thought](/wiki/Thought "Thought") for 1 [day](/wiki/Time "Time") to any non-[deaf](/wiki/Hearing "Hearing"), non-[inhumanized](/wiki/Inhumanized "Inhumanized") pawns in 9.9 cells radius. Unlike most other interaction types, strange chats can be performed without an explicit recipient. Non-[inhumanized](/wiki/Inhumanized "Inhumanized") recipients gain −3 opinion of the initiator for 1 day. [Talking](/wiki/Talking "Talking") capacity of 0% prevents rambling.  
+ **:** Gains the [Morbid](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type.[![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
Always and only spawns on creepjoiners with the "Disturbing" downside, which is precluded by the "Joybringer" benefit.   
Void fascination  | NAME is strangely intrigued by unnatural entities and is easily enthralled by them.  | + **:** Negates all mood penalties for: Imprisoned with entity, Monster by my bed  
+6 _Captured entity_ [thought](/wiki/Thought "Thought") while there is at least one captured entity in the colony  
Only possible [extreme mental break](/wiki/Extreme_break "Extreme break") is [entity liberator](/wiki/Mental_break#Entity_liberator "Mental break")  
− **:** Entity liberation breaks randomly occur with an MTB of 60 days  
+ **:** Gains the [Void](/wiki/Psyfocus#Meditation "Psyfocus") meditation focus type, replacing the Artistic meditation focus type if they had it [![Content added by the Royalty DLC](/images/thumb/4/41/RoyaltyIcon.png/16px-RoyaltyIcon.png)](/wiki/Royalty_DLC "Content added by the Royalty DLC")  
  
## Obsolete traits[[edit](/index.php?title=Traits&action=edit&section=26 "Edit section: Obsolete traits")]

These are no longer found as-is in the current game version, though many of them have been renamed or reworked into one of the traits found above. 

Name  | Description  | Effect  | Conflicting Traits  | Fate   
---|---|---|---|---  
Prosthophile  | NAME feels limited in their feeble human body. NAME often dreams of going bionic.  | +14 mood bonus for having a bionic body part  
−4 mood penalty for not having a bionic body part  | Body purist  | Replaced by Transhumanist  
Prosthophobe  | NAME believes the human body is limited for a reason. To them, bionic body parts are unethical.  | −10 mood penalty for having a bionic body part  | body modder  | Replaced by Body purist  
Green thumb  | NAME has a passion for gardening. They get a mood bonus for every plant they sow.  | +1 mood bonus from sowing a plant. Stackable up to 20 times.  | \-  | Removed in Beta 19   
Tunneler  | NAME has no need for space. S/He will never feel cooped up or get cabin fever, no matter how long s/he stays indoors.  | + **:** No Outdoors need  | \-  | Replaced by Undergrounder  
Transhumanist  | NAME feels limited in their feeble human body. NAME often dreams of going bionic.  | +4 to +13 [mood](/wiki/Mood "Mood") bonus for having [artificial body parts](/wiki/Artificial_body_parts "Artificial body parts")  
−4 mood penalty for not having an artificial body part  
+8 to +40 opinion of other colonists for each part installed on them  | Body purist | Replaced by Body modder  
  
## Version history[[edit](/index.php?title=Traits&action=edit&section=27 "Edit section: Version history")]

  * [0.0.245](/wiki/Version/0.0.245 "Version/0.0.245") \- Traits hidden as they did nothing.
  * [0.7.581](/wiki/Version/0.7.581 "Version/0.7.581") \- Brawler, prosthophile, and more added.
  * [0.9.722](/wiki/Version/0.9.722 "Version/0.9.722") \- Teetotaller and Chemical Fascination traits added
  * [0.12.906](/wiki/Version/0.12.906 "Version/0.12.906") \- Greedy, Jealous, Ascetic, Night Owl traits added.
  * [0.17.1546](/wiki/Version/0.17.1546 "Version/0.17.1546") \- Wimp trait added.
  * [0.19.2009](/wiki/Version/0.19.2009 "Version/0.19.2009") \- Undergrounder, Great memory, Tough, Gourmand, Sickly, Quick sleeper traits added
  * [1.1.0](/wiki/Version/1.1.0 "Version/1.1.0") \- Asexual trait added
  * [1.2.2719](/wiki/Version/1.2.2719 "Version/1.2.2719") \- Fix: Psylink counts as an artificial part for a transhumanist.
  * [1.3.3066](/wiki/Version/1.3.3066 "Version/1.3.3066") \- Transhumanist trait renamed to Body Modder. Kind description changed "_NAME is a nice person. They have a tendency to brighten everyone else's day and never insult others._ " -> _"NAME is an exceptionally agreeable and giving person. S/He never insults others and will sometimes offer kind words to brighten the moods of those around her/him. {PAWN_pronoun} also never judges people by their appearance."_. Undergrounders have a new Need_Indoors, which is increased by spending time indoors, especially inside mountains.
  * [1.4.3523](/wiki/Version/1.4.3523 "Version/1.4.3523") \- Pyromaniacs are happier around fires and get a stacking (up to 4x) mood buff for nearby fires. This includes torches and campfires. “Wimp” trait’s pain shock threshold has been increased from 50% to 60%. [Ascetics](/wiki/Ascetic "Ascetic") no longer get a negative mood debuff when eating nutrient paste meals. [Plasmaswords](/wiki/Plasmasword "Plasmasword") and [persona plasmaswords](/wiki/Persona_plasmasword "Persona plasmasword") now provide the mood bonus to [pyromaniacs](/wiki/Pyromaniac "Pyromaniac") like other incendiary weapons.
  * After [1.4.3542](/wiki/Version/1.4.3542 "Version/1.4.3542") but pre [1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062") \- Chemical Fascination and Interest now only randomly take beer, ambrosia and smokeleaf joints, instead of any drug
  * [1.4.3555](/wiki/Version/1.4.3555 "Version/1.4.3555") \- [Xenogenes](/wiki/Xenogenes "Xenogenes") count as artificial enhancements for [body modders](/wiki/Body_modder "Body modder") and [body purists](/wiki/Body_purist "Body purist"). Fix: Administer drug doesn't display that teetotalers will be unhappy if there is a chemical dependency gene present.
  * [1.4.3557](/wiki/Version/1.4.3557 "Version/1.4.3557") \- Fix typo: "yielding" -> "wielding" in pyromaniac trait description.
  * 1.5 or prior - Pyromaniac thought mood effect reduced from +5 to +2 and description changed from _"It makes me think of flame and fire. I'm so happy"_ to _"It makes me think of flame and fire. I can't wait to use it."_ New thought added for using a flame weapon.
  * [1.5.4062](/wiki/Version/1.5.4062 "Version/1.5.4062") \- Rebalance brawler trait to offset skill more than mood - mood penalty for using ranged weapon decreased from −20 to −10, shooting accuracy penalty increased from −4 to −10. Added “pyro used fire weapon” thought +8 mood. Ascetics ignore "Ate without table" thought. Fix: NRE related to pyromaniacs wielding fire weapons.
  * [1.6.4566](/wiki/Version/1.6.4566 "Version/1.6.4566") \- Fix: [Smoke launcher](/wiki/Smoke_launcher "Smoke launcher"), [EMP launcher](/wiki/EMP_launcher "EMP launcher"), and [toxbomb launcher](/wiki/Toxbomb_launcher "Toxbomb launcher") were incorrectly marked as incendiary weapons for the purpose of [pyromaniacs](/wiki/Pyromaniac "Pyromaniac").
  * [Odyssey DLC](/wiki/Odyssey_DLC "Odyssey DLC") Release- Added [unique weapon](/wiki/Unique_weapon "Unique weapon") traits that count as incendiary weapons for [pyromaniacs](/wiki/Pyromaniac "Pyromaniac").
  * [1.6.4850](/wiki/Version/1.6.4850 "Version/1.6.4850") \- Fix: Possible enumeration error with joyous thought.



Retrieved from "[https://rimworldwiki.com/index.php?title=Traits&oldid=184197](https://rimworldwiki.com/index.php?title=Traits&oldid=184197)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Pages to be moved](/wiki/Category:Pages_to_be_moved "Category:Pages to be moved")
  * [Characters](/wiki/Category:Characters "Category:Characters")



Hidden category: 

  * [Pages that need fact checking](/wiki/Category:Pages_that_need_fact_checking "Category:Pages that need fact checking")



## Navigation menu

###  Personal tools

  * Not logged in
  * [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address \[n\]")
  * [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address \[y\]")
  * [Create account](/index.php?title=Special:CreateAccount&returnto=Traits "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/index.php?title=Special:UserLogin&returnto=Traits "You are encouraged to log in; however, it is not mandatory \[o\]")



###  Namespaces

  * [Page](/wiki/Traits "View the content page \[c\]")
  * [Discussion](/wiki/Talk:Traits "Discussion about the content page \[t\]")



###  Variants




###  Views

  * [Read](/wiki/Traits)
  * [Edit](/index.php?title=Traits&action=edit "Edit this page \[e\]")
  * [View history](/index.php?title=Traits&action=history "Past revisions of this page \[h\]")



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

  * [What links here](/wiki/Special:WhatLinksHere/Traits "A list of all wiki pages that link here \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Traits "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/wiki/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Traits&oldid=184197 "Permanent link to this revision of the page")
  * [Page information](/index.php?title=Traits&action=info "More information about this page")
  * [Browse properties](/wiki/Special:Browse/:Traits)



  * This page was last edited on 1 October 2026, at 01:46.
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
  *[MTB]: mean time between
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
  *[4 secs]: real-time at 1x speed
