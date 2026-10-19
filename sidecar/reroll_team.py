import json, requests

URL = "http://localhost:8787/"


def call(n, a=None):
    p = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": n, "arguments": a or {}}}
    r = requests.post(URL, json=p, timeout=30)
    d = r.json()
    t = d["result"]["content"][0]["text"]
    try:
        return json.loads(t)
    except Exception:
        return {"text": t}


def reroll_colonist(index):
    """Reroll the pawn at the given index. Returns the new pawn dict."""
    return call("edit_starting_pawn", {"action": "reroll", "index": index})


def pawn_score(pawn):
    """Score a pawn for colony viability. Higher is better."""
    score = 0
    skills = pawn.get("skills", [])
    skill_map = {}
    for s in skills:
        parts = s.split()
        name = parts[0].lower()
        val = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
        skill_map[name] = val

    # Critical skills: construction, plants, medical, intellectual
    score += skill_map.get("construction", 0) * 3
    score += skill_map.get("plants", 0) * 3
    score += skill_map.get("medical", 0) * 3
    score += skill_map.get("intellectual", 0) * 2
    # Useful: cooking, shooting, crafting, social
    score += skill_map.get("cooking", 0) * 2
    score += skill_map.get("shooting", 0) * 2
    score += skill_map.get("crafting", 0)
    score += skill_map.get("social", 0)
    # Penalties for incapables
    inc = pawn.get("incapableOf") or ""
    if "Violent" in inc:
        score -= 20
    if "Caring" in inc:
        score -= 20
    if "Dumb labor" in inc:
        score -= 10
    if "Intellectual" in inc:
        score -= 15
    if "Plant work" in inc or "Plant Work" in inc:
        score -= 15
    # Trait penalties
    traits = [t.get("label", "") for t in pawn.get("traits", [])]
    if "Pyromaniac" in traits:
        score -= 50
    if "Sickly" in traits:
        score -= 10
    if "Slowpoke" in traits:
        score -= 5
    if "Tortured artist" in traits:
        score -= 5
    return score


def team_score(pawns):
    """Score a 3-pawn team. Higher is better. Must cover construction, plants, medical, intellectual."""
    total = 0
    # Critical skill coverage: at least one pawn with 5+ in each
    has_construction = any(any("construction" in s.lower().split()[0] and int(s.split()[1]) >= 3 for s in p.get("skills", []) if len(s.split()) > 1 and s.split()[1].isdigit()) for p in pawns)
    has_plants = any(any("plants" in s.lower().split()[0] and int(s.split()[1]) >= 3 for s in p.get("skills", []) if len(s.split()) > 1 and s.split()[1].isdigit()) for p in pawns)
    has_medical = any(any("medical" in s.lower().split()[0] and int(s.split()[1]) >= 3 for s in p.get("skills", []) if len(s.split()) > 1 and s.split()[1].isdigit()) for p in pawns)
    has_intellectual = any(any("intellectual" in s.lower().split()[0] and int(s.split()[1]) >= 3 for s in p.get("skills", []) if len(s.split()) > 1 and s.split()[1].isdigit()) for p in pawns)

    # ALL four critical skills must be covered, otherwise disqualify
    if not (has_construction and has_plants and has_medical and has_intellectual):
        return -9999

    # No Violent or Caring incapables (can't fight or doctor)
    for p in pawns:
        inc = p.get("incapableOf") or ""
        if "Violent" in inc or "Caring" in inc:
            return -9999

    if has_construction:
        total += 30
    if has_plants:
        total += 30
    if has_medical:
        total += 30
    if has_intellectual:
        total += 30

    # Sum individual scores
    for p in pawns:
        total += pawn_score(p)

    # Bonus for no incapables of Violent or Caring
    for p in pawns:
        inc = p.get("incapableOf") or ""
        if "Violent" not in inc:
            total += 5
        if "Caring" not in inc:
            total += 5

    return total


def reroll_team(min_score=120, max_rerolls=50):
    """
    Reroll starting colonists until team_score >= min_score or max_rerolls reached.
    Returns the best team found.
    """
    best_team = None
    best_score = -9999
    rerolls = 0

    st = call("game_setup_status")
    pawns = st.get("pawns", [])
    starting = [p for p in pawns if p.get("starting")]

    while rerolls < max_rerolls:
        score = team_score(starting)
        if score > best_score:
            best_score = score
            best_team = [dict(p) for p in starting]
            print(f"  new best: score={score} team={[p['name'] for p in starting]}")

        if score >= min_score:
            print(f"  acceptable team found (score={score}) after {rerolls} rerolls")
            return starting, score

        # Reroll the weakest pawn
        scores = [(pawn_score(p), i, p) for i, p in enumerate(starting)]
        scores.sort()
        weakest_idx = scores[0][1]
        print(f"  reroll {rerolls+1}: weakest={starting[weakest_idx]['name']} (score {scores[0][0]}), team score {score}")

        result = call("edit_starting_pawn", {"action": "reroll", "index": weakest_idx})
        if not result.get("ok"):
            print(f"  reroll failed: {result}")
            break

        # Refresh pawn list
        st = call("game_setup_status")
        pawns = st.get("pawns", [])
        starting = [p for p in pawns if p.get("starting")]
        rerolls += 1

    print(f"  best score {best_score} after {rerolls} rerolls")
    return best_team, best_score


if __name__ == "__main__":
    print("Rerolling team (min_score=120, max_rerolls=50)...")
    team, score = reroll_team(min_score=150, max_rerolls=100)
    print("\nFinal team:")
    for p in team:
        print(f"  {p['name']} | {p.get('incapableOf')} | {p['skills']}")
        print(f"    traits: {[t['label'] for t in p.get('traits', [])]}")
    print(f"  team score: {score}")
