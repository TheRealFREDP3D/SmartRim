# ab_debrief.py — A/B Debrief Harness

Run same debrief bundle against two models for comparison.

## Function

```python
def main():
    # Parse args: bundle_path, model_a, model_b, [provider]
    # Run analyze_debrief for both models
    # Print side-by-side comparison
```

## Usage

```bash
python -m smartrim.ab_debrief path/to/bundle.md gemma4-e2b-rimworld qwen3-rimworld
python -m smartrim.ab_debrief --run run-005 --model-a gemma4-e2b-rimworld --model-b qwen3-rimworld
```

## Output

- Both model analyses printed
- Candidate lessons from each
- Manual comparison aid

## Notes

- 50 lines (thin wrapper)
- Uses `debrief_llm.analyze_debrief()`
- Quick A/B testing for model selection
