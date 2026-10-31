# eval_models.py — Model Evaluation (A/B Debrief)

Evaluate multiple models on same debrief bundle, score with rubric.

## Function
```python
def eval_one(bundle_path, model, provider=None, rubric_path=None) -> ScoreRow:
    # Run debrief analysis with model, score output
```

## Scoring Rubric
| Criterion | Weight | Description |
|-----------|--------|-------------|
| Cause accuracy | 1.0 | Primary cause matches known failure |
| Actionable lessons | 1.0 | Lessons are specific, triggerable |
| Confidence calibration | 0.5 | Confidence matches lesson quality |
| Format compliance | 0.5 | Valid JSON, correct schema |

## ScoreRow
```python
@dataclass
class ScoreRow:
    model: str
    provider: str
    cause_score: float
    lessons_score: float
    confidence_score: float
    format_score: float
    total: float
```

## Helpers
- `_extract_fenced_json()` — extract ```json block
- `_detect_sections()` — find bundle sections
- `_count_bullets()` — count bullet points in worked/lessons
- `score_debrief_answer()` — apply rubric to model output

## CLI
```bash
python -m smartrim.eval_models --bundle path/to/bundle.md --models gemma4-e2b-rimworld qwen3-rimworld
```

## Notes
- 465 lines
- Requires `tenacity` for retries
- Outputs CSV/JSON for comparison