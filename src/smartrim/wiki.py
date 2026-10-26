"""Fetch RimWorld wiki pages and convert them to clean markdown.

Two-step tool, split because the raw scrape and the HTML->MD conversion are
independent concerns:

  1. ``python -m smartrim.wiki fetch``   -> writes ``memory/wiki/raw/<slug>.html``
  2. ``python -m smartrim.wiki convert`` -> writes ``memory/wiki/<slug>.md``

The cleaned ``.md`` files in ``memory/wiki/`` are what the LLM reads and are
tracked in git. The ``raw/`` HTML is only needed to re-scrape or re-convert,
so it is gitignored (see ``memory/wiki/raw/`` in ``.gitignore``).

Both steps are idempotent: ``fetch`` skips pages it already has unless
``--force`` is given, and ``convert`` rewrites every ``.md`` it can produce.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request

from smartrim.config import BASE_DIR

WIKI_BASE = "https://rimworldwiki.com/wiki/"
WIKI_DIR = os.path.join(BASE_DIR, "memory", "wiki")
RAW_DIR = os.path.join(WIKI_DIR, "raw")
MANIFEST_PATH = os.path.join(WIKI_DIR, "manifest.json")

USER_AGENT = "RimWorldCounselor/1.0"
REQUEST_TIMEOUT = 30
FETCH_DELAY = 0.5

# Every page we track. Kept explicit so the cache is reproducible and a
# missing page is a known gap rather than a silent absence.
#
# A few pages 404 on the wiki today but are cached and in use by the LLM
# (AI_Storytellers, Difficulty, Guinea_pig, Incapable, Pyromaniac, Rice).
# They are kept so a re-scrape does not silently drop them.
PAGES: list[str] = [
    "Main_Page",
    "Wealth",
    "Mood",
    "Research",
    "Medicine",
    "Herbal_medicine",
    "Cover",
    "Animals",
    "Stockpile",
    "Zones",
    "Temperature",
    "Electricity",
    "Raid",
    "Raid_points",
    "Mental_break",
    "Thoughts",
    "Traits",
    "Skills",
    "Health",
    "Food",
    "Nutrition",
    "Defense",
    "Turret",
    "Sandbags",
    "Growing",
    "Farming",
    "Batteries",
    "Solar_panel",
    "Wind_turbine",
    "Power",
    "Room",
    "Room_roles",
    "Impressiveness",
    "Beauty",
    "Prisoner",
    "Trade",
    "Caravan",
    "Quests",
    "Ideology_(DLC)",
    "Royalty_(DLC)",
    "Biotech_(DLC)",
    "Anomaly_(DLC)",
    "Cooler",
    "Heater",
    "Base",
    "Sowing",
    "Harvest",
    "Cooking",
    "Meals",
    "Nutrient_paste",
    "Recreation",
    "Bed",
    "Bedroom",
    "Stockpile_zone",
    "Growing_zone",
    "Hospital",
    "Doctoring",
    "Surgery",
    "Infection",
    "Disease",
    "Plague",
    "Malaria",
    "Flu",
    "Injury",
    "Blood_loss",
    "Pain",
    "Inspiration",
    "Joy",
    "Joywire",
    "Drug",
    "Beer",
    "Smokeleaf",
    "Luciferium",
    "Psychite",
    "Yayo",
    "Flake",
    "Go-juice",
    "Wake-up",
    "Penoxycyline",
    "Ambrosia",
    "Neutroamine",
    "Cloth",
    "Devilstrand",
    "Hyperweave",
    "Synthread",
    "Megasloth_wool",
    "Alpaca_wool",
    "Muffalo_wool",
    "Wool",
    "Leather",
    "Fur",
    "Meat",
    "Human_meat",
    "Insect_meat",
    "Raw_food",
    "Simple_meal",
    "Fine_meal",
    "Lavish_meal",
    "Packaged_survival_meal",
    "Kibble",
    "Hay",
    "Taming",
    "Training",
    "Bond",
    "Slaughter",
    "Egg",
    "Hauling",
    "Cleaning",
    "Firefighting",
    "Construction",
    "Mining",
    "Crafting",
    "Art",
    "Intellectual",
    "Social",
    "Animals_skill",
    "Shooting",
    "Melee",
    "Brawler",
    "Careful_shooter",
    "Trigger-happy",
    "Nimble",
    "Tough",
    "Robust",
    "Delicate",
    "Frail",
    "Sickly",
    "Glitterworld_medicine",
    "Prosthetic",
    "Bionic",
    "Archotech",
    "Peg_leg",
    "Bionic_arm",
    "Bionic_leg",
    "Bionic_eye",
    "Bionic_heart",
    "Power_claw",
    "Scyther_blade",
    "Drill_arm",
    "Field_hand",
    "Hand_talon",
    "Venom_talon",
    "Psychic_soothe_pulser",
    "Psychic_animal_pulser",
    "Psychic_emanator",
    "Psychic_drone",
    "Psychic_ship",
    "Mechanoid",
    "Scyther",
    "Lancer",
    "Centipede",
    "Pikeman",
    "Termite",
    "Inferno_cannon",
    "Heavy_charge_blaster",
    "Charge_lance",
    "Charge_rifle",
    "Minigun",
    "Doomsday_rocket_launcher",
    "Triple_rocket_launcher",
    "Incendiary_launcher",
    "Smoke_launcher",
    "Antigrain_warhead",
    "Orbital_power_beam_targeter",
    "Tornado_generator",
    "Weather_controller",
    "Climate_adjuster",
    "Vanometric_power_cell",
    "Infinite_chemreactor",
    "Techprof_subpersona_core",
    "AI_persona_core",
    "Mechanitor",
    "Mechlink",
    "Mech",
    "Constructoid",
    "Paramedic",
    "Agrihand",
    "Lifter",
    "Cleansweeper",
    "Fabricor",
    "Militor",
    "Scorcher",
    "Tunneler",
    "War_urchin",
    "War_queen",
    "Apocriton",
    "Diabolus",
    "Centurion",
    "Band_node",
    "Wastepack",
    "Pollution",
]


def _load_manifest() -> dict:
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def _save_manifest(manifest: dict) -> None:
    os.makedirs(WIKI_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)


def fetch_pages(pages: list[str], force: bool = False) -> int:
    """Download raw HTML for each page into ``memory/wiki/raw/``."""
    os.makedirs(RAW_DIR, exist_ok=True)
    manifest = _load_manifest()
    fetched = 0

    for slug in pages:
        url = WIKI_BASE + slug
        raw_path = os.path.join(RAW_DIR, f"{slug}.html")

        if os.path.exists(raw_path) and not force:
            print(f"SKIP {slug} (already cached)")
            continue

        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(html)
            manifest[slug] = {
                "url": url,
                "fetched": time.strftime("%Y-%m-%d"),
                "size": len(html),
            }
            fetched += 1
            print(f"OK   {slug} ({len(html)} bytes)")
        except Exception as e:
            # One bad page must not abort the whole scrape.
            print(f"FAIL {slug}: {str(e)[:80]}")
        time.sleep(FETCH_DELAY)

    _save_manifest(manifest)
    print(f"fetched {fetched} pages; manifest holds {len(manifest)} entries")
    return fetched


def _strip_html(html: str) -> str:
    """Convert wiki HTML to markdown-ish text without external dependencies."""
    try:
        import html2text  # type: ignore[import-not-found]

        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)
    except ImportError:
        pass

    # Fallback: crude tag stripper so the tool works without html2text.
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
    text = re.sub(r"(?s)<!--.*?-->", " ", text)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</(p|div|li|h[1-6]|tr)>", "\n", text)
    text = re.sub(r"(?i)<li[^>]*>", "- ", text)
    text = re.sub(r"(?s)<[^>]+>", "", text)
    text = (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&nbsp;", " ")
    )
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def convert_pages() -> int:
    """Convert every cached raw HTML page into a cleaned ``.md`` file."""
    if not os.path.isdir(RAW_DIR):
        print(f"No raw cache at {RAW_DIR}; run 'fetch' first.")
        return 0

    os.makedirs(WIKI_DIR, exist_ok=True)
    converted = 0
    for name in sorted(os.listdir(RAW_DIR)):
        if not name.endswith(".html"):
            continue
        slug = name[: -len(".html")]
        raw_path = os.path.join(RAW_DIR, name)
        md_path = os.path.join(WIKI_DIR, f"{slug}.md")
        try:
            with open(raw_path, encoding="utf-8") as f:
                md = _strip_html(f.read())
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            converted += 1
        except OSError as e:
            print(f"FAIL {slug}: {str(e)[:80]}")

    print(f"converted {converted} pages to markdown in {WIKI_DIR}")
    return converted


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch and convert RimWorld wiki pages")
    sub = parser.add_subparsers(dest="command", required=True)

    p_fetch = sub.add_parser("fetch", help="download raw HTML into memory/wiki/raw/")
    p_fetch.add_argument("--pages", nargs="*", help="slugs to fetch (default: all tracked pages)")
    p_fetch.add_argument("--force", action="store_true", help="re-download even if cached")

    sub.add_parser("convert", help="convert memory/wiki/raw/*.html into memory/wiki/*.md")

    args = parser.parse_args(argv)

    if args.command == "fetch":
        pages = args.pages or PAGES
        fetch_pages(pages, force=args.force)
    elif args.command == "convert":
        convert_pages()
    return 0


if __name__ == "__main__":
    sys.exit(main())
