"""A/B harness: run the same debrief bundle against two models.

Writes both responses to memory/debriefs/<run>.<model>.response.md for rubric scoring.
Usage:
    python -m smartrim.ab_debrief --run run-006-obs-cassandra --models gemma4-e2b-rimworld qwen3-rimworld
"""
import argparse
import os
import sys

from smartrim import debrief_llm
from smartrim.config import DEBRIEFS_DIR


def main():
    parser = argparse.ArgumentParser(description="A/B debrief harness")
    parser.add_argument("--run", required=True, help="Run ID")
    parser.add_argument("--models", nargs=2, required=True, help="Two model names to compare")
    parser.add_argument("--temperature", type=float, default=0.3)
    args = parser.parse_args()

    bundle_path = debrief_llm.find_bundle(args.run)
    if not bundle_path or not os.path.exists(bundle_path):
        print(f"Bundle not found: {bundle_path}")
        sys.exit(1)
    with open(bundle_path, encoding="utf-8") as f:
        bundle = f.read()
    is_bundle = ("Section A" in bundle) and ("## 8. Task" in bundle or "## 8." in bundle)

    for model in args.models:
        print(f"Running model: {model}")
        analysis = debrief_llm.analyze_debrief(bundle, model=model, temperature=args.temperature,
                                             system=debrief_llm.BUNDLE_SYSTEM if is_bundle else None)
        # Write response file named <run>.<model>.response.md
        safe_model = model.replace(":", "_").replace("/", "_")
        out_path = os.path.join(DEBRIEFS_DIR, f"{args.run}.{safe_model}.response.md")
        os.makedirs(DEBRIEFS_DIR, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            if isinstance(analysis, dict) and "raw" in analysis:
                f.write(analysis["raw"])
            else:
                f.write("## Section A\n\n```json\n")
                import json
                f.write(json.dumps(analysis, indent=2))
                f.write("\n```\n")
        print(f"  Written: {out_path}")


if __name__ == "__main__":
    main()