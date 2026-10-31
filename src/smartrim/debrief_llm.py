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
import logging
import os
import re
import sys
import time
import urllib.error
from typing import Literal

import requests
from pydantic import BaseModel, ConfigDict, ValidationError, confloat
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from smartrim.config import CANDIDATES_DIR, DEBRIEFS_DIR
from smartrim.llm import generate

logger = logging.getLogger(__name__)

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
BUNDLE_MAX_CHARS = 65000

# How many times to re-ask the model after a schema validation failure.
SCHEMA_RETRY_ATTEMPTS = 3


FENCE_RE = re.compile(r'```json\s*(.*?)```', re.DOTALL | re.IGNORECASE)

# Lesson candidate schema (Section A of v3 bundles)
PHASES_T = Literal['early_survival', 'stabilization', 'raid_prep', 'expansion', 'crisis', 'any']
THREATS_T = Literal[
    'colonist_downed', 'mood_break_risk', 'colonist_injured', 'danger_high',
    'raid_incoming', 'predator_near_worker', 'low_food', 'medical_untreated',
    'idle_colonists', 'threat_response', 'colony_death', 'other_game_alert',
    'any'
]
RESOURCES_T = Literal['food_under_5_days', 'food_under_2_days', 'no_medicine', 'medicine_under_5', 'low_wood', 'low_steel', 'any']
DIFFICULTY_T = Literal['Peaceful', 'Community builder', 'Adventure story', 'Strive to survive', 'Blood and dust', 'Losing is fun']
STORYTELLER_T = Literal['Cassandra Classic', 'Phoebe Chillax', 'Randy Random']


class SchemaValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class TriggerCandidate(BaseModel):
    phases: list[PHASES_T]
    threats: list[THREATS_T]
    resources: list[RESOURCES_T]
    difficulty: Literal['any'] | DIFFICULTY_T | list[DIFFICULTY_T] = 'any'
    storyteller: Literal['any'] | STORYTELLER_T | list[STORYTELLER_T] = 'any'
    biome: Literal['any'] | str | list[str] = 'any'


class LessonCandidate(BaseModel):
    title: str
    cause_chain: list[str]
    trigger: TriggerCandidate
    recommendation: str
    rationale: str
    source: list[str]
    wiki_pages_used: list[str]
    unverified_claims: list[str]
    confidence: confloat(ge=0.3, le=0.7)

    model_config = ConfigDict(extra='forbid')


def _extract_first_json_fence(raw: str):
    match = FENCE_RE.search(raw or '')
    if match:
        content = match.group(1).strip()
        return json.loads(content)
    # Fallback: try to parse the first top-level JSON array in the raw text.
    text = (raw or '').strip()
    start = text.find('[')
    end = text.rfind(']')
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            pass
    raise json.JSONDecodeError('no fenced ```json block found', raw or '', 0)


def _validate_lesson_candidates(data) -> list[dict]:
    if not isinstance(data, list):
        raise SchemaValidationError(f'Expected a JSON array at top-level; got {type(data).__name__}')
    validated: list[LessonCandidate] = []
    for idx, item in enumerate(data):
        try:
            validated.append(LessonCandidate.model_validate(item))
        except ValidationError as e:
            raise SchemaValidationError(f'Candidate[{idx}] schema error: {e}') from e
    return [c.model_dump() for c in validated]


def _system_with_fence_instruction(system_text: str) -> str:
    return (system_text or '') + (
        "\n\nWhen outputting Section A, wrap the JSON array in a single fenced block: ```json ...```"
    )


RECOVERY_SUFFIX = '\nIf you cannot produce valid JSON, return {"raw": "<your analysis>"}.'

# The model's most common schema failure is inventing vocabulary for trigger fields.
# Spell out the allowed values so the retry prompt is actionable.
TRIGGER_VOCAB = (
    'Allowed values: '
    'trigger.phases: early_survival | stabilization | raid_prep | expansion | crisis | any; '
    'trigger.threats: colonist_downed | mood_break_risk | colonist_injured | danger_high | '
    'raid_incoming | predator_near_worker | low_food | medical_untreated | idle_colonists | '
    'threat_response | colony_death | other_game_alert | any; '
    'trigger.resources: food_under_5_days | food_under_2_days | no_medicine | medicine_under_5 | '
    'low_wood | low_steel | any; '
    'trigger.difficulty: Peaceful | Community builder | Adventure story | Strive to survive | '
    'Blood and dust | Losing is fun | any; '
    'trigger.storyteller: Cassandra Classic | Phoebe Chillax | Randy Random | any; '
    'trigger.biome: any or a biome name; '
    'confidence: a number between 0.3 and 0.7.'
)


def _schema_retry_prompt(error: str) -> str:
    """Build an actionable retry prompt from a schema validation error."""
    return (
        f"\n\nYour last response failed schema validation: {error}\n"
        f"{TRIGGER_VOCAB}\n"
        "Use only those values (use 'any' when a field does not apply). "
        "Re-emit the full JSON array in a single ```json fenced block, and nothing else."
    )


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30),
       retry=retry_if_exception_type((requests.exceptions.Timeout, requests.exceptions.RequestException,
                                     json.JSONDecodeError, urllib.error.URLError, TimeoutError, OSError)),
       before_sleep=before_sleep_log(logger, logging.INFO))
def _generate_once(bundle_text, model, system, temperature, provider=None):
    prompt = f"Analyze this RimWorld colony debrief bundle:\n\n{bundle_text}"
    raw = generate(
        prompt,
        task="debrief",
        provider=provider,
        model=model,
        system=system,
        temperature=temperature,
        num_ctx=16384,
        cache_system=bool(system and system.startswith(BUNDLE_SYSTEM)),
    )
    return raw, _extract_first_json_fence(raw)


def analyze_debrief(bundle_text, model=None, temperature=0.3, system=None, task="debrief", provider=None):
    """Send a debrief bundle to the LLM and return the analysis.

    Uses fenced ```json blocks for structured extraction, then validates
    Section A candidate lessons with a Pydantic schema.

    If schema validation fails, retries once more with a validation error
    message embedded in the system prompt.
    """
    if len(bundle_text) > BUNDLE_MAX_CHARS:
        bundle_text = bundle_text[:BUNDLE_MAX_CHARS] + "\n\n[... truncated ...]"

    base_system = system or DEBRIEF_SYSTEM
    sys1 = _system_with_fence_instruction(base_system)
    expect_candidates = ("Section A" in bundle_text) and ("## 8. Task" in bundle_text or "## 8." in bundle_text)

    try:
        raw, data = _generate_once(bundle_text, model, sys1, temperature, provider=provider)
        if not expect_candidates:
            return {"raw": raw, "json": data}
        lessons = _validate_lesson_candidates(data)
        return {"raw": raw, "lessons": lessons}
    except SchemaValidationError as ve:
        logger.info(
            "Debrief LLM failed schema validation; retrying with validation error: %s",
            ve.message,
        )
        prompt = f"Analyze this RimWorld colony debrief bundle:\n\n{bundle_text}"
        # Give the model a few chances: each retry carries the exact schema error
        # plus the allowed vocabulary, so it can converge on a valid answer.
        last_error = ve.message
        raw = ""
        for attempt in range(1, SCHEMA_RETRY_ATTEMPTS + 1):
            sys2 = sys1 + _schema_retry_prompt(last_error)
            raw = generate(
                prompt,
                task=task,
                provider=provider,
                model=model,
                system=sys2,
                temperature=temperature,
                num_ctx=16384,
                cache_system=False,
            )
            try:
                data2 = _extract_first_json_fence(raw)
                lessons2 = _validate_lesson_candidates(data2)
                return {"raw": raw, "lessons": lessons2}
            except (json.JSONDecodeError, SchemaValidationError, ValidationError) as e:
                last_error = str(e)[:800]
                logger.info("Schema retry %d failed: %s", attempt, last_error[:200])
                if attempt < SCHEMA_RETRY_ATTEMPTS:
                    time.sleep(2)
        return {"raw": raw, "schema_error": last_error}
    except (requests.exceptions.Timeout, requests.exceptions.RequestException, json.JSONDecodeError,
            urllib.error.URLError, TimeoutError, OSError) as e:
        logger.info("Debrief LLM failed after retries (%s); retrying with recovery prompt", e)
        recovery_system = sys1 + RECOVERY_SUFFIX
        prompt = f"Analyze this RimWorld colony debrief bundle:\n\n{bundle_text}"
        raw = generate(
            prompt,
            task=task,
            provider=provider,
            model=model,
            system=recovery_system,
            temperature=temperature,
            num_ctx=16384,
            cache_system=False,
        )
        try:
            data = _extract_first_json_fence(raw)
            return {"raw": raw, "json": data}
        except json.JSONDecodeError:
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
    """Write the LLM analysis to a file.

    Also writes candidate lessons to memory/candidates/<run>-<timestamp>.jsonl
    if the analysis contains validated lesson candidates.
    """
    if not DEBRIEFS_DIR:
        return None
    os.makedirs(DEBRIEFS_DIR, exist_ok=True)
    path = os.path.join(DEBRIEFS_DIR, f"{run_id}-llm.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# LLM Debrief Analysis: {run_id}\n\n")
        f.write(f"Model: {model}\n")
        f.write(f"Generated: {__import__('datetime').datetime.now().isoformat()}\n\n")
        if isinstance(analysis, dict) and "raw" in analysis:
            f.write(analysis["raw"])
        elif isinstance(analysis, list):
            f.write("```json\n")
            f.write(json.dumps(analysis, indent=2, default=str))
            f.write("\n```\n")
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

    # Write candidate lessons to JSONL if available
    if isinstance(analysis, dict) and "lessons" in analysis:
        candidates_path = _write_candidate_lessons(run_id, analysis["lessons"], candidates_dir=CANDIDATES_DIR)
        if candidates_path:
            logger.info(f"Wrote candidate lessons to: {candidates_path}")

    return path


def _write_candidate_lessons(run_id, lessons, candidates_dir=None):
    """Write candidate lessons to memory/candidates/<run>-<timestamp>.jsonl.

    Each lesson is converted to the full lesson schema with:
    - id: auto-generated as "C-<run_id>-<index>" (candidate format, not lesson format)
    - status: "needs_review"
    - confidence: 0.3 (floor for single observations)
    - times_applied/helped/failed: 0
    - last_updated: current date

    Args:
        run_id: Run identifier
        lessons: List of lesson candidate dicts
        candidates_dir: Override CANDIDATES_DIR (for testing)

    Returns:
        Path to written file, or None if candidates_dir is None
    """
    output_dir = candidates_dir
    if not output_dir:
        return None

    os.makedirs(output_dir, exist_ok=True)
    timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d-%H%M%S")
    candidates_path = os.path.join(output_dir, f"{run_id}-{timestamp}.jsonl")

    from smartrim.situation import validate_lesson

    with open(candidates_path, "w", encoding="utf-8") as f:
        for idx, candidate in enumerate(lessons):
            # Convert candidate to full lesson schema
            lesson = {
                "id": f"C-{run_id}-{idx}",  # Candidate ID format (not L-XXXX)
                "title": candidate.get("title", ""),
                "trigger": _normalize_trigger(candidate.get("trigger", {})),
                "recommendation": candidate.get("recommendation", ""),
                "rationale": candidate.get("rationale", ""),
                "source": candidate.get("source", []),
                "confidence": 0.3,  # Floor for single observations
                "status": "needs_review",
                "tags": [],  # Tags can be added during review
                "times_applied": 0,
                "times_helped": 0,
                "times_failed": 0,
                "source_runs": [run_id],
                "last_updated": __import__('datetime').datetime.now().strftime("%Y-%m-%d"),
            }

            # Validate before writing (skip ID validation for candidates)
            # We'll re-validate with proper L-XXXX ID during promotion
            errors = validate_lesson(lesson)
            # Filter out ID validation errors since candidates use C- format
            errors = [e for e in errors if not e.startswith("bad id")]

            if errors:
                logger.warning(f"Lesson candidate {idx} validation errors: {errors}")
                # Still write it, but note the errors in a comment
                f.write(f"# Validation errors: {errors}\n")

            f.write(json.dumps(lesson) + "\n")

    return candidates_path


def _normalize_trigger(trigger):
    """Normalize trigger object to match lesson schema."""
    # Ensure all required fields exist
    normalized = {
        "phases": trigger.get("phases", []),
        "threats": trigger.get("threats", []),
        "resources": trigger.get("resources", []),
        "difficulty": trigger.get("difficulty", "any"),
        "storyteller": trigger.get("storyteller", "any"),
        "biome": trigger.get("biome", "any"),
    }
    return normalized


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
    analysis = analyze_debrief(
        bundle,
        model=_model,
        provider=_provider,
        system=BUNDLE_SYSTEM if is_bundle else None,
    )
    print(json.dumps(analysis, indent=2))

    if not args.no_write:
        run_id = args.run or os.path.splitext(os.path.basename(bundle_path))[0]
        path = write_analysis(run_id, analysis, _model)
        if path:
            print(f"\nWritten: {path}")


if __name__ == "__main__":
    main()
