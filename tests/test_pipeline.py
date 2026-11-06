"""One-command post-run pipeline: debrief -> bundle -> LLM -> auto-promote."""

import json
import os

import pytest

from smartrim import config, pipeline, promote

RUN_ID = "run-950-adv"


def _seed_snapshot(run_dir, *, day, days_passed, idx=0):
    snaps = os.path.join(run_dir, "snapshots")
    os.makedirs(snaps, exist_ok=True)
    snap = {
        "run_id": RUN_ID,
        "day": day,
        "timestamp": f"2026-11-05T12:0{idx}:00",
        "status": {
            "daysPassed": days_passed,
            "difficulty": "adventure story",
            "storyteller": "Cassandra Classic",
            "colonistCount": 3,
            "wealthTotal": 12000,
        },
        "conditions": {"date": day, "hour": 12, "seasonLabel": "Spring",
                       "temperature": {"outdoorC": 12}},
        "colonists": {"colonists": [
            {"name": "Ana", "health": 100, "mood": 55, "downed": False},
            {"name": "Bo", "health": 90, "mood": 40, "downed": False},
        ]},
        "resources": {"resources": [{"defName": "MealSimple", "label": "Simple meal", "count": 40}],
                      "wealthTotal": 12000},
        "research": {"current": {"label": "Stonecutting", "progressPercent": 50}},
        "alerts": {"activeAlerts": [], "dangerByMap": []},
        "summary": {"days_passed": days_passed, "colonist_count": 3,
                    "food_days": 4.0, "medicine_count": 10, "min_mood": 40,
                    "difficulty": "adventure story",
                    "storyteller": "Cassandra Classic"},
    }
    with open(os.path.join(snaps, f"day-{day}.json"), "w", encoding="utf-8") as fh:
        json.dump(snap, fh)


def _seed_run():
    run_dir = config.run_dir(RUN_ID)
    _seed_snapshot(run_dir, day="5th of Aprimay, 5500", days_passed=4, idx=0)
    _seed_snapshot(run_dir, day="6th of Aprimay, 5500", days_passed=5, idx=1)
    return run_dir


def _candidate(idx, **overrides):
    topics = [
        ("Build walls before the first raid", "Wall off the colony before the first raid",
         "raid_incoming", "Walls prevent the early raid from reaching the base"),
        ("Keep medicine stockpiled for injuries", "Stockpile at least ten medicine before combat",
         "medical_untreated", "Bo bled out while the medicine shelf was empty"),
        ("Plant rice before food runs out", "Sow a rice field on day one of spring",
         "low_food", "Stores emptied by day four of Aprimay"),
        ("Give colonists recreation time", "Schedule joy exercise in the afternoons",
         "mood_break_risk", "Two colonists approached minor break risk"),
    ]
    title, rec, threat, rationale = topics[idx % len(topics)]
    cand = {
        "id": f"C-{RUN_ID}-{idx}",
        "title": title,
        "trigger": {"phases": ["early_survival"], "threats": [threat],
                    "resources": [], "difficulty": "Adventure story",
                    "storyteller": "Cassandra Classic", "biome": "any"},
        "recommendation": rec,
        "rationale": rationale,
        "source": ["6th of Aprimay, 5500"],
        "confidence": 0.3,
        "status": "needs_review",
        "tags": [],
        "times_applied": 0,
        "times_helped": 0,
        "times_failed": 0,
        "source_runs": [RUN_ID],
        "last_updated": "2026-11-05",
    }
    cand.update(overrides)
    return cand


def _write_candidates(cand_dir, candidates):
    os.makedirs(cand_dir, exist_ok=True)
    path = os.path.join(cand_dir, f"{RUN_ID}-20261105-120000.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for cand in candidates:
            fh.write(json.dumps(cand) + "\n")
    return path


def _seed_lessons(tmp_path, lessons=None):
    path = tmp_path / "lessons.jsonl"
    with open(path, "w", encoding="utf-8") as fh:
        for lesson in (lessons or []):
            fh.write(json.dumps(lesson) + "\n")
    return str(path)


@pytest.fixture()
def seeded_run():
    return _seed_run()


def test_pipeline_promotes_rule_passing_candidates(tmp_path, seeded_run, monkeypatch):
    lessons_file = _seed_lessons(tmp_path)
    cand_dir = config.candidates_dir(RUN_ID, create=True)
    _write_candidates(cand_dir, [_candidate(0), _candidate(1)])

    report = pipeline.run_pipeline(
        RUN_ID, use_llm=False, lessons_file=lessons_file,
        render_path=str(tmp_path / "lessons-learned.md"),
    )
    assert report is not None
    assert len(report["promoted"]) == 2
    assert report["skipped"] == []

    with open(lessons_file, encoding="utf-8") as fh:
        lessons = [json.loads(line) for line in fh if line.strip()]
    assert [lesson["id"] for lesson in lessons] == ["L-0001", "L-0002"]
    assert all(lesson["status"] == "needs_review" for lesson in lessons)

    # Candidates file annotated so re-runs don't double-promote.
    remaining = promote.load_candidates(report["candidates_path"])
    assert all(c.get("promoted_as") for c in remaining)


def test_pipeline_skips_duplicates_and_uncited(tmp_path, seeded_run):
    existing = {
        "id": "L-0001", "title": "Build walls before the first raid",
        "trigger": {"phases": ["early_survival"], "threats": ["raid_incoming"], "resources": []},
        "recommendation": "Wall off the colony before the first raid",
        "rationale": "x", "source": ["x"], "confidence": 0.5,
        "times_applied": 0, "times_helped": 0, "times_failed": 0,
        "status": "active", "tags": [], "source_runs": [], "last_updated": "2026-01-01",
    }
    lessons_file = _seed_lessons(tmp_path, [existing])
    cand_dir = config.candidates_dir(RUN_ID, create=True)
    _write_candidates(cand_dir, [
        _candidate(0),                          # duplicate of L-0001
        _candidate(1, source=[]),                # no citation -> skipped
        _candidate(2, title="", recommendation=""),  # missing fields
        _candidate(3, trigger={"phases": [], "threats": [], "resources": [],
                               "difficulty": "any", "storyteller": "any", "biome": "any"}),  # too broad
    ])

    report = pipeline.run_pipeline(
        RUN_ID, use_llm=False, lessons_file=lessons_file,
        render_path=str(tmp_path / "lessons-learned.md"),
    )
    assert report["promoted"] == []
    skipped = dict(report["skipped"])
    assert any("duplicate" in reason for reasons in skipped.values() for reason in reasons)
    assert any("no source" in reason for reasons in skipped.values() for reason in reasons)
    assert any("too broad" in reason for reasons in skipped.values() for reason in reasons)
    # Lessons file untouched.
    with open(lessons_file, encoding="utf-8") as fh:
        assert len(fh.readlines()) == 1


def test_pipeline_rerun_is_idempotent(tmp_path, seeded_run):
    lessons_file = _seed_lessons(tmp_path)
    cand_dir = config.candidates_dir(RUN_ID, create=True)
    _write_candidates(cand_dir, [_candidate(0)])
    render_path = str(tmp_path / "lessons-learned.md")

    first = pipeline.run_pipeline(RUN_ID, use_llm=False, lessons_file=lessons_file,
                                  render_path=render_path)
    second = pipeline.run_pipeline(RUN_ID, use_llm=False, lessons_file=lessons_file,
                                   render_path=render_path)
    assert len(first["promoted"]) == 1
    assert second["promoted"] == []
    with open(lessons_file, encoding="utf-8") as fh:
        assert len([line for line in fh if line.strip()]) == 1


def test_pipeline_dry_run_writes_nothing(tmp_path, seeded_run):
    lessons_file = _seed_lessons(tmp_path)
    cand_dir = config.candidates_dir(RUN_ID, create=True)
    path = _write_candidates(cand_dir, [_candidate(0)])
    before = open(path, encoding="utf-8").read()

    report = pipeline.run_pipeline(RUN_ID, use_llm=False, dry_run=True,
                                   lessons_file=lessons_file,
                                   render_path=str(tmp_path / "lessons-learned.md"))
    assert len(report["promoted"]) == 1  # reported...
    with open(lessons_file, encoding="utf-8") as fh:
        assert fh.read() == ""            # ...but not written
    assert open(path, encoding="utf-8").read() == before  # candidates untouched


def test_pipeline_full_llm_path_with_stubbed_model(tmp_path, seeded_run, monkeypatch):
    lessons_file = _seed_lessons(tmp_path)
    monkeypatch.setattr(pipeline, "resolve_model", lambda task, model=None: ("fake", "fake-model"))
    monkeypatch.setattr(
        pipeline, "analyze_debrief",
        lambda *a, **kw: {"raw": "analysis", "lessons": [dict(_candidate(0), id="C-x-0")]},
    )
    report = pipeline.run_pipeline(
        RUN_ID, use_llm=True, lessons_file=lessons_file,
        render_path=str(tmp_path / "lessons-learned.md"),
    )
    assert report is not None
    assert len(report["promoted"]) == 1
    assert os.path.isfile(os.path.join(config.debriefs_dir(RUN_ID), f"{RUN_ID}-llm.md"))
    assert os.path.isfile(os.path.join(config.debriefs_dir(RUN_ID), f"{RUN_ID}.bundle.md"))


def test_pipeline_schema_failure_writes_nothing(tmp_path, seeded_run, monkeypatch):
    lessons_file = _seed_lessons(tmp_path)
    monkeypatch.setattr(pipeline, "resolve_model", lambda task, model=None: ("fake", "fake-model"))
    monkeypatch.setattr(pipeline, "analyze_debrief",
                        lambda *a, **kw: {"raw": "bad", "schema_error": "nope"})
    report = pipeline.run_pipeline(RUN_ID, use_llm=True, lessons_file=lessons_file)
    assert report["candidates_path"] is None
    with open(lessons_file, encoding="utf-8") as fh:
        assert fh.read() == ""


def test_pipeline_no_llm_without_candidates_errors(tmp_path, seeded_run, capsys):
    lessons_file = _seed_lessons(tmp_path)
    report = pipeline.run_pipeline(RUN_ID, use_llm=False, lessons_file=lessons_file)
    assert report["error"] == "no candidates"
    assert "run with LLM first" in capsys.readouterr().out


def test_pipeline_requires_snapshots(tmp_path):
    lessons_file = _seed_lessons(tmp_path)
    report = pipeline.run_pipeline("run-951-adv", use_llm=False, lessons_file=lessons_file)
    assert report is None


def test_load_candidates_skips_comments(tmp_path):
    path = tmp_path / "c.jsonl"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write('# Validation errors: ["bad id"]\n')
        fh.write(json.dumps(_candidate(0)) + "\n")
        fh.write("not json\n")
    candidates = promote.load_candidates(str(path))
    assert len(candidates) == 1


def test_similarity_detects_near_duplicates():
    a = "Build walls before the first raid"
    b = "Build walls before first raid strikes"
    assert promote.similarity(a, b) > 0.6
    assert promote.similarity(a, "Cooking precise meals") < 0.3
