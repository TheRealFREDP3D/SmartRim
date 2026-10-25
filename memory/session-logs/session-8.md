# Session 8 - Run 007 (adviser on, 2026-10-25)

## Game Setup (per RUN-PROTOCOL.md)

- **Run ID**: run-007-adv-cassandra
- **Colony**: New Arrivals
- **Scenario**: Crashlanded (3 survivors)
- **Tile**: 39 - Temperate Forest, Flat, 11.8 C, rainfall 1867mm, swampiness 0, pollution 0
  - Surroundings: 91/91 tiles temperate forest, 79 flat, river + road nearby, no hostile settlements
  - Rejected tile 5 (hostile Dozvzaz settlement 3 tiles NE)
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure story (Medium)
- **Reload Mode**: Reload Anytime (no reloading during run)
- **Ideology**: Fluid - "Deviism", generated defaults, no edits
- **Run length**: 10 full days after Day 1 (ends at daysPassed=11)
- **Monitor**: RUN_ID=run-007-adv-cassandra, adviser ON, 30s poll interval

## Colonists

| Name | Age | Gender | Top Skills | Traits | Incapable Of | Health | Role |
|------|-----|--------|------------|--------|--------------|--------|------|
| Leighton 'Speedy' Blackburn | 54 | M | Intellectual 11, Medical 9, Cooking 7, Construction 5 | Ascetic | - | 100 HP | Researcher/Medic/Cook |
| Steven Wilcox | 25 | M | Shooting 9, Melee 8, Social 8, Animals 7 | Desensitized, Kind | - | 100 HP | Fighter |
| Niklas Fischer | 34 | M | Shooting 10, Cooking 7, Construction 6, Medical 6 | Groundbreaker | Artistic | 100 HP | Shooter/Medic/Cook |

Team totals: shooting 22, melee 10, medical 15, construction 12, intellectual 13, cooking 16, crafting 11, plants 10.

Protocol gate: all three PASS (none incapable of Violent or Caring). Composition matches the
prior-run standard (2 shooters + 1 melee, critical skills covered).

### Selection notes
- Default team was rejected: only 1 shooter, a pregnant colonist (Pheanox Nickel), and no
  construction/plants coverage.
- Slot 0 rerolled twice. First roll (Samantha von Aachen: intellectual 6, medical 1) was a
  regression - rejected. Second roll used `intellectual >= 8` + healthy, matched after 7 attempts.
- Slot 1 rerolled with `shooting >= 6, melee >= 5`, avoid Pyromaniac/Slothful, healthy - matched
  after 29 attempts. This avoided a Pyromaniac who was also incapable of Firefighting.
- Slot 2 rerolled with `shooting >= 5` + healthy - matched after 34 attempts.
- Player validated the selection before `start_game` was called.

## Day 0 - Landing state (paused)

- **Colonists**: 3 alive, all 100 HP, mood 50 each
- **Alerts**: none. Danger rating: None. No letters.
- **Wealth**: 18277
- **Research**: none active, 7 completed / 164 total
- **Resources**: not yet readable (colonists have not started hauling)
- **Monitor**: wrote first snapshot `day-6th of Aprimay, 5500.json`, displayed morning status message

## Infrastructure fix needed (Day 0)

Following the session-7 lesson (items deteriorating outside, no beds, no shelter):
- [ ] Unforbid all starting items
- [ ] Set work priorities for all 3
- [ ] Build shelter with door (7x7 interior, as per prior sessions)
- [ ] Place beds, table, stove, research bench (all interior)
- [ ] Stockpile zones: interior + exterior
- [ ] Growing zones: potato + rice
- [ ] Equip: Steven = rifle, Niklas = rifle/knife, Leighton = knife (or ranged if available)
- [ ] Set research (Smithing line, mirroring run-002/run-005)

## Timeline

- Day 0 (6th of Aprimay, 5500): Colony landed, paused for player validation.

## Outcome

(In progress.)
