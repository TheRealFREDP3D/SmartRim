"""LLM-backed debrief analysis. Replaces the manual paste-into-model step.

Usage:
    python sidecar/debrief_llm.py <bundle_file> [--model gemma4-e2b-rimworld]
    python sidecar/debrief_llm.py --run run-005-adv-cassandra

Reads a debrief bundle markdown, sends it to the local Ollama model, and
writes the analysis to memory/debriefs/<run>-llm.md (or prints to stdout).
"""
import argparse
import glob
import json
import os
import sys

from smartrim.config import CANDIDATES_DIR, DEBRIEFS_DIR
from smartrim.llm import generate

DEBRIEF_SYSTEM = """You are a RimWorld colony analyst. Given a colony run debrief
bundle (timeline, alerts, resources, advice log), provide a structured analysis:

1. PRIMARY CAUSE: What was the main cause of failure or current risk? (1-2 sentences)
2. WHAT WORKED: What strategies/skills/decisions succeeded? (bullet list)
3. LESSONS: 3-5 lessons to add to the lesson store. Each as:
   {trigger, recommendation, rationale, confidence (0.3-0.8)}
4. NEXT COLONY: What should the next colony do differently? (2-3 sentences)

Output as JSON with keys: cause, worked (list), lessons (list of objects), next_colony.
Be concise and specific. Reference actual game events from the bundle."""


# A v3 bundle carries its own task and output contract (section 8), so in bundle mode we do
# not impose the free-form DEBRIEF_SYSTEM prompt on top of it.
BUNDLE_SYSTEM = ("You are a careful analyst. Follow the instructions in the user message "
                 "exactly and output only what they ask for.")

# A real v3 bundle is ~28K characters (~7K tokens). The old 12K cutoff dropped the advice-log
# causes (section 7, ~offset 21K) and the task itself (section 8, ~offset 28K), so the model
# could never follow the format. Keep the whole bundle for num_ctx=16384.
BUNDLE_MAX_CHARS = 48000


def analyze_debrief(bundle_text, model=None, temperature=0.3, system=None, task="debrief"):
    """Send a debrief bundle to the LLM and return the analysis.

    system overrides DEBRIEF_SYSTEM. Pass BUNDLE_SYSTEM when the input is a full bundle whose
    own section 8 defines the required output.
    """
    if len(bundle_text) > BUNDLE_MAX_CHARS:
        bundle_text = bundle_text[:BUNDLE_MAX_CHARS] + "\n\n[... truncated ...]"
    prompt = f"Analyze this RimWorld colony debrief bundle:\n\n{bundle_text}"
    raw = generate(prompt, task=task, model=model,
                   system=system or DEBRIEF_SYSTEM, temperature=temperature, num_ctx=16384)
    # Try to parse JSON from response
    try:
        # Find JSON in response (may have markdown wrapping)
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(raw[start:end])
    except json.JSONDecodeError:
        pass
    return {"raw": raw}


def find_bundle(run_id):
    """Find the debrief bundle file for a run."""
    if os.path.exists(run_id):
        return run_id
    # Search in debriefs dir (bundle files are named <run_id>.bundle.md)
    if DEBRIEFS_DIR:
        for name in (f"{run_id}.bundle.md", f"{run_id}.md"):
            path = os.path.join(DEBRIEFS_DIR, name)
            if os.path.exists(path):
                return path
    # Search in candidates
    if CANDIDATES_DIR:
        for f in glob.glob(os.path.join(CANDIDATES_DIR, f"*{run_id}*")):
            return f
    return None


def write_analysis(run_id, analysis, model):
    """Write the LLM analysis to a file."""
    if not DEBRIEFS_DIR:
        return None
    os.makedirs(DEBRIEFS_DIR, exist_ok=True)
    path = os.path.join(DEBRIEFS_DIR, f"{run_id}-llm.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# LLM Debrief Analysis: {run_id}\n\n")
        f.write(f"Model: {model}\n")
        f.write(f"Generated: {__import__('datetime').datetime.now().isoformat()}\n\n")
        if "raw" in analysis:
            f.write(analysis["raw"])
        else:
            f.write(f"## Primary Cause\n{analysis.get('cause', 'N/A')}\n\n")
            f.write("## What Worked\n")
            f.writelines(f"- {w}\n" for w in analysis.get("worked", []))
            f.write("\n## Lessons\n")
            for lesson in analysis.get("lessons", []):
                f.write(f"- **Trigger**: {lesson.get('trigger', '?')}\n")
                f.write(f"  **Recommendation**: {lesson.get('recommendation', '?')}\n")
                f.write(f"  **Rationale**: {lesson.get('rationale', '?')}\n")
                f.write(f"  **Confidence**: {lesson.get('confidence', 0.3)}\n\n")
            f.write(f"\n## Next Colony\n{analysis.get('next_colony', 'N/A')}\n")
    return path


def main():
    parser = argparse.ArgumentParser(description="LLM-backed debrief analysis")
    parser.add_argument("bundle_file", nargs="?", help="Path to debrief bundle markdown")
    parser.add_argument("--run", help="Run ID (looks up bundle automatically)")
    parser.add_argument("--model", default=None, help="Override model (default: task-based)")
    parser.add_argument("--no-write", action="store_true", help="Print to stdout only")
    args = parser.parse_args()

    # Find bundle
    bundle_path = args.bundle_file
    if args.run:
        bundle_path = find_bundle(args.run)
    if not bundle_path or not os.path.exists(bundle_path):
        print(f"Bundle not found: {bundle_path}")
        sys.exit(1)

    print(f"Analyzing: {bundle_path}")
    with open(bundle_path, encoding="utf-8") as f:
        bundle = f.read()

    # A full v3 bundle defines its own output contract (Section A JSON + Section B summary in
    # its section 8). Use a neutral system prompt so the bundle's contract wins.
    is_bundle = ("Section A" in bundle) and ("## 8. Task" in bundle or "## 8." in bundle)
    from smartrim.llm import resolve_model
    _provider, _model = resolve_model(task="debrief", model=args.model)
    analysis = analyze_debrief(bundle, model=_model,
                               system=BUNDLE_SYSTEM if is_bundle else None)
    print(json.dumps(analysis, indent=2))

    if not args.no_write:
        run_id = args.run or os.path.splitext(os.path.basename(bundle_path))[0]
        path = write_analysis(run_id, analysis, _model)
        if path:
            print(f"\nWritten: {path}")


if __name__ == "__main__":
    main()
