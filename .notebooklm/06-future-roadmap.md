# SmartRim Future Roadmap

## Current Status

SmartRim is an active research project in Phase 1 (Advisor Mode). The system successfully:
- Connects to RimWorld via RimMolt MCP
- Monitors colony state with configurable intervals
- Detects urgent alerts (food, health, combat, mood)
- Generates context-aware advice from lessons
- Completes 10-day evaluation runs under fixed protocol
- Extracts lessons from debrief analysis

## Vision

The ultimate goal is a system that **auto-plays RimWorld**. The human is a spectator who can intervene at any time: give orders, change parameters, pause/resume, or override decisions. The advisor-only stance from Phase 1 is a stepping stone, not the destination.

## Phase Roadmap

### Phase 1: Advisor Mode (Current)

**Status**: Active development

**Goal**: Prove that the system can observe, detect threats, and provide useful advice.

**Completed**:
- ✅ MCP integration with RimMolt
- ✅ Snapshot system
- ✅ Urgent alert detection
- ✅ Lesson store and retrieval
- ✅ Advice generation
- ✅ Debrief system
- ✅ Evaluation protocol
- ✅ 10-day run automation

**In Progress**:
- 🔄 Lesson refinement based on run outcomes
- 🔄 Improving advice quality
- 🔄 Expanding lesson coverage
- 🔄 Testing on diverse scenarios

**Remaining**:
- ⏳ Baseline performance metrics (adviser off vs adviser on)
- ⏳ Comprehensive lesson library
- ⏳ Robust error handling for edge cases
- ⏳ Documentation for external contributors

**Success Criteria**:
- Adviser-on runs show measurable improvement over adviser-off
- Lesson store covers 80% of early-game threats
- Debrief rubric scores consistently above 3.5/5
- 10-day runs complete without manual intervention

### Phase 2: Action Mode

**Status**: Planned

**Goal**: The system can take direct actions via MCP tools, not just advise.

**Key Capabilities**:
- Issue orders via MCP (build, prioritize, draft, etc.)
- Make autonomous decisions on base building
- Manage work priorities dynamically
- Handle combat without human intervention
- Execute multi-step strategies

**Technical Work**:
- Action executor module (similar to counselor but for actions)
- Action validation and safety checks
- Rollback mechanism for failed actions
- Action outcome tracking
- Conflict resolution (multiple competing actions)

**New Components**:
- `sidecar/executor.py` - Action execution engine
- `sidecar/planner.py` - Strategic planning
- `sidecar/safety.py` - Action validation
- `schemas/action.schema.json` - Action structure

**Evaluation Protocol Changes**:
- Compare autonomous runs vs human runs
- Measure decision quality
- Track action success/failure rates
- Assess colony performance (wealth, happiness, survival)

**Success Criteria**:
- Autonomous runs survive 10 days at 80% rate
- Autonomous decisions are no worse than median human decisions
- No catastrophic failures (burning base, starving colony)
- Action success rate > 70%

### Phase 3: Strategy Mode

**Status**: Future

**Goal**: The system can plan and execute long-term strategies.

**Key Capabilities**:
- Research path optimization
- Economic planning (wealth accumulation)
- Social management (mood, relationships)
- DLC integration (royalty titles, ideology reforms)
- Multi-map operations (caravans, quests)

**Technical Work**:
- Strategic planner with lookahead
- Economic simulation models
- Social relationship tracking
- DLC-specific action modules
- Multi-map coordination

**New Components**:
- `sidecar/strategist.py` - Long-term planning
- `sidecar/economist.py` - Economic optimization
- `sidecar/diplomat.py` - Faction and social management
- `sidecar/dlc/` - DLC-specific modules

**Evaluation Protocol Changes**:
- 30-day runs (to see mid-game)
- Wealth accumulation metrics
- Research efficiency metrics
- DLC-specific scenarios

**Success Criteria**:
- Autonomous runs reach day 30 at 60% rate
- Wealth accumulation matches or exceeds human baseline
- Research completion optimized (no wasted research)
- DLC mechanics handled correctly

### Phase 4: Mastery Mode

**Status**: Future

**Goal**: The system can play RimWorld at expert level.

**Key Capabilities**:
- Handle all game mechanics and edge cases
- Optimize for specific goals (wealth, population, research)
- Adapt to different storytellers and biomes
- Handle late-game threats (mechanoid raids, ancient dangers)
- Manage complex social systems (ideology, royalty)

**Technical Work**:
- Generalized AI architecture
- Reinforcement learning for decision optimization
- Transfer learning across scenarios
- Meta-learning for adaptation
- Extensive testing across all game configurations

**Success Criteria**:
- Autonomous runs survive 100+ days
- Performance matches top 10% of human players
- Adapts to all storytellers and biomes
- Handles all DLC content effectively

## Technical Roadmap

### Short-Term (Next 3 months)

**Phase 1 Completion**:
1. Complete baseline evaluation (10 runs adviser on, 10 runs adviser off)
2. Expand lesson library to cover common early-game threats
3. Improve advice quality through lesson refinement
4. Add comprehensive error handling
5. Document Phase 1 results

**Infrastructure**:
1. Add automated testing pipeline
2. Set up continuous integration
3. Create performance dashboard
4. Implement lesson versioning
5. Add snapshot compression

### Medium-Term (3-6 months)

**Phase 2 Development**:
1. Design action execution framework
2. Implement safety checks and rollback
3. Build action executor module
4. Create action validation system
5. Test on limited scenarios (build, prioritize)

**Phase 2 Evaluation**:
1. Define new evaluation metrics
2. Create action-specific rubric
3. Run baseline autonomous runs
4. Compare against human baseline
5. Iterate on action quality

### Long-Term (6-12 months)

**Phase 3 Development**:
1. Build strategic planner
2. Implement economic optimization
3. Add social management
4. Integrate DLC modules
5. Test on 30-day runs

**Phase 4 Research**:
1. Explore reinforcement learning approaches
2. Research transfer learning techniques
3. Investigate meta-learning for adaptation
4. Prototype generalized AI architecture

## Research Directions

### 1. Lesson Learning

**Current**: Manual lesson creation and debrief extraction

**Future**: Automated lesson discovery
- Unsupervised learning from successful runs
- Clustering similar situations
- Identifying patterns in successful vs failed runs
- A/B testing lesson effectiveness

### 2. Decision Quality

**Current**: Rule-based advice with LLM synthesis

**Future**: Learned decision policies
- Reinforcement learning for action selection
- Imitation learning from expert replays
- Monte Carlo Tree Search for planning
- Neural network approximation of value functions

### 3. Adaptation

**Current**: Fixed protocol, single scenario

**Future**: Adaptive system
- Dynamic parameter adjustment
- Biome-specific strategies
- Storyteller-specific behavior
- Custom scenario support

### 4. Multi-Agent

**Current**: Single agent controlling colony

**Future**: Multi-agent architecture
- Specialized agents (builder, fighter, researcher)
- Hierarchical control (strategist → executors)
- Negotiation between competing goals
- Distributed decision making

## Challenges and Risks

### Technical Challenges

**MCP Reliability**:
- Risk: MCP server instability or crashes
- Mitigation: Robust error handling, connection retry, graceful degradation

**LLM Quality**:
- Risk: Poor advice from local LLMs
- Mitigation: Model selection, fine-tuning, ensemble methods

**Action Safety**:
- Risk: Catastrophic actions (burning base, starving colony)
- Mitigation: Safety checks, rollbacks, human override

**Complexity Explosion**:
- Risk: Game complexity overwhelms the system
- Mitigation: Modular architecture, phased rollout, focus on core mechanics

### Research Challenges

**Evaluation**:
- Risk: Hard to measure "success" objectively
- Mitigation: Multiple metrics, human evaluation, comparison baselines

**Generalization**:
- Risk: System overfits to specific scenarios
- Mitigation: Diverse training data, regularization, transfer learning

**Interpretability**:
- Risk: Decisions become inscrutable
- Mitigation: Explainable AI, decision logging, human-in-the-loop

### Project Risks

**Scope Creep**:
- Risk: Project becomes too ambitious
- Mitigation: Clear phase boundaries, incremental delivery, regular review

**Maintenance**:
- Risk: Game updates break compatibility
- Mitigation: Modular design, abstraction layers, community support

**Adoption**:
- Risk: No external interest or contributors
- Mitigation: Open source, clear documentation, engaging demos

## Collaboration Opportunities

### Open Source
- Release as open source project
- Welcome external contributors
- Build community around the project
- Create extension points for mods and DLCs

### Academic Research
- Publish results on AI for games
- Collaborate with game AI researchers
- Benchmark against other game-playing systems
- Contribute to game AI literature

### Industry Partnerships
- Partner with LedgeNine (RimMolt developers)
- Explore integration with other games
- Consider commercial applications
- Build tools for game developers

## Milestones

### Q4 2026
- [ ] Complete Phase 1 baseline evaluation
- [ ] Publish Phase 1 results
- [ ] Open source initial release
- [ ] Begin Phase 2 development

### Q1 2027
- [ ] Complete Phase 2 action executor
- [ ] Run first autonomous 10-day runs
- [ ] Publish Phase 2 results
- [ ] Begin Phase 3 planning

### Q2 2027
- [ ] Complete Phase 3 strategic planner
- [ ] Run first 30-day autonomous runs
- [ ] Integrate DLC modules
- [ ] Publish Phase 3 results

### Q3 2027
- [ ] Begin Phase 4 research
- [ ] Explore reinforcement learning
- [ ] Test on diverse scenarios
- [ ] Prepare for expert-level play

### Q4 2027
- [ ] Achieve expert-level performance
- [ ] Publish comprehensive results
- [ ] Release production version
- [ ] Plan long-term maintenance

## Success Metrics

### Quantitative Metrics
- **Survival Rate**: Percentage of runs reaching target length
- **Decision Quality**: Comparison to human baselines
- **Wealth Accumulation**: Resources at end of run
- **Research Efficiency**: Research completed vs time
- **Happiness**: Average colonist mood
- **Action Success**: Percentage of successful actions

### Qualitative Metrics
- **Advice Usefulness**: Human evaluation of advice quality
- **Action Appropriateness**: Human review of autonomous actions
- **Strategic Insight**: Novel strategies discovered
- **Adaptability**: Performance across scenarios
- **Interpretability**: Ability to explain decisions

## Conclusion

SmartRim is an ambitious project with a clear roadmap from advisor to autonomous player. The phased approach ensures each stage builds on the previous one, with clear success criteria and evaluation protocols. The project has the potential to advance both game AI research and practical applications of AI in complex simulation environments.

The journey from Phase 1 to Phase 4 will take approximately 12-18 months, with regular milestones and publications. Success will require careful attention to technical challenges, research rigor, and community engagement.

The ultimate vision - an AI that can play RimWorld at expert level - is ambitious but achievable with the right approach, incremental progress, and sustained effort.
