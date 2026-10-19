# Wiki audit of memory and knowledge base

Date: 2026-10-18. Source of truth: `memory/wiki/*.md` (RimWorld Wiki, 147 cached pages, fetched 2026-10-18).
Scope: `memory/*.md`, `memory/session-logs/*.md`, `MCP-REFERENCE.md`.

## A. Errors corrected (wiki contradicts the old note)

| # | Old claim | Where | Wiki says | Fixed in |
|---|---|---|---|---|
| 1 | Below 25% minor breaks; below 10% major; above 50% safe | mechanics.md | Minor 35%, major 20%, extreme 5% (base). Traits shift it. | mechanics.md |
| 2 | Mood table: 50%+ safe, 25-50 warning, 10-25 critical, <10 imminent | colonist-management.md | Same thresholds as #1, with break MTBs | colonist-management.md |
| 3 | "Medicine research is called Drug Production" | research-tree.md | Drug production (drug lab) and Medicine production (industrial medicine) are two separate research projects. Medicine production requires Drug production. | research-tree.md |
| 4 | Drug lab: healroot + cloth + neutroamine → herbal medicine | research-tree.md, lessons-learned.md, beginner-guide.md | Herbal medicine comes from healroot. Cloth 3 + herbal 1 + neutroamine 1 makes industrial medicine (needs a crafter with 4 Intellectual + 4 Crafting). | all three |
| 5 | Raid points cap at 10,000 "(unverified)" | mechanics.md | Confirmed: raid point cap is 10,000 (Raid_points) | mechanics.md |
| 6 | Shared barracks = "mood penalty" (no number) | base-design.md | Dull barracks -5, Awful barracks -7 vs private bedroom | base-design.md |
| 7 | Guinea pig killed Vlad / "even guinea pigs can kill" | lessons-learned.md, beginner-guide.md, session logs | Guinea pigs are herbivores (Guinea_pig, Animals). Predators are a separate class. Cause of Vlad's death is not confirmed. | lessons, beginner-guide (cause marked unconfirmed) |
| 8 | "4 different recreation types" | lessons-learned.md | Recommended number is 2 to 6, depending on wealth expectations (Wealth). 10 recreation types exist (Recreation). | lessons-learned.md |
| 9 | Recipe on Day 5+ "healroot + cloth" | beginner-guide.md, lessons-learned.md | See #4 | both |

## B. Claims with no support in the wiki (kept, marked unverified)

| Claim | Where | Status |
|---|---|---|
| First raid window Days 8-15 | beginner-guide, combat, lessons, session-2/3/4 logs | Not in the wiki. AI_Storytellers gives raid frequency by preset but no days. Session 5 saw a raid on Day 5 under Phoebe (Community builder). Marked unverified in the active notes. Historical logs keep the original wording. |
| Corpse -10 mood per corpse | colonist-management, beginner-guide, lessons #4, session-1 | The wiki's Thoughts page gives a "left unburied" thought after 4 game days, but the cached text does not show a numeric value for "Observed corpse". Marked unverified. |
| Ate without table -3 | Earlier notes | Not in the cached text. Unverified. |
| Healroot 60% potency | lessons-learned | Not in the cached text. Unverified. |
| Packaged meals ~8 days for 3 pawns | mechanics | Not in the cached text. Marked unverified. |
| Community Builder pre-researched list (Electricity, Stonecutting, ...) | research-tree | Not in the wiki. Marked UNVERIFIED. Wiki-verified facts: research speed 120%, threat scale 30%. |
| Sniper rifle range | combat | Already marked unverified. |
| Ghoul companions | DLC notes | Already marked unverified. |

## C. Conflicts between the wiki and our own tool gotchas

| Item | Wiki | Our note | Status |
|---|---|---|---|
| Sandbag material | 5 units of Fabric or Leathery | "stuff=Cloth only" (MCP gotcha #9) | Kept as a tool observation, marked to re-test. Wiki is the rule. |
| Work-type names (Firefighting, Bed Rest) | Not in the wiki (game UI names) | Conflicting notes in lessons and session 2 | Still unresolved. Needs an in-game check, not a wiki check. |

## D. Verified and kept (wiki agrees)

- Wealth raid cap 1,000,000 storyteller wealth; raid point cap 10,000.
- Freezing point 0 °C prevents spoilage; coolers keep food cold (Cooler).
- Predators hunt colonists when hungry and keep attacking downed prey; rescue quickly (Animals).
- Raw food food-poisoning chance 2%; cooked food depends on cook skill and kitchen cleanliness (Rice, Blood_loss/Food poisoning).
- Rice: 5.54 days to mature, 6 units per plant (Rice). Our "~6 days" matches. The farming note "17 tiles per pawn" (Farming) matches our "40-60 tiles for 3 pawns".
- Incapable of Violent cannot equip weapons or hunt (Incapable).
- Mood base by difficulty (Mood page) and difficulty research speed (AI_Storytellers).
- Smithing research 700 and Battery research 400 match in-game costs (Research; Session 5 showed 400).
- Unburied colonist corpse thought after 4 game days (Thoughts).
- Recreation has 10 types and builds tolerance (Recreation).
- Barracks penalty exists (Thoughts).
- Our early-game shelter, research, and beds advice is consistent with the wiki (no contradiction found).

## E. Wiki gaps

- Medical bed and Bed rest pages are not in the wiki (404). Medical beds are documented only by in-game experience (Session 5).
- AI_Storytellers gives raid frequency per preset in a table that did not survive text extraction. Re-fetch if needed.
- Not in cache: Packaged survival meal nutrition values, Cotton, Hunting (404 under that name).

## F. Next steps

1. Re-test sandbag material in-game (Fabric vs cloth) and record the result.
2. Resolve work-type names in-game and record the result in MCP-REFERENCE.md.
3. Record Community Builder pre-research in-game.
4. Keep this report updated when new wiki pages are fetched.
