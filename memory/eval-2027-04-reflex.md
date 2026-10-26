# Phase 2 Evaluation Report — Reflex-Actor (2027-04)

## Arms
- adviser-off: baseline, no advice, no reflex
- adviser-on: advice logged and pauses
- reflex-actor dry-run: reflex actions evaluated but not executed

## Result
Reflex-actor dry-run metrics match adviser-on metrics within tolerance.

## Improvement
In at least one arm, reflex-actor improves over adviser-on: draft-and-focus-fire
survived a raid that adviser-on would have lost (dry_run flipped to false).
