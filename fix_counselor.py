content = open('src/smartrim/counselor.py', encoding='utf-8').read()
start = content.find('# === Game Flow (new game setup) ===')
pause = content.find('\ndef pause()')
if start == -1 or pause == -1:
    raise SystemExit('bad')
fixed = '''# === Game Flow (new game setup) ===

def main_menu(action: str = "new_colony") -> dict:
    """Main menu actions (new colony, load, return to title, etc.)."""
    return _call("main_menu", {"action": action})


def game_setup_status() -> dict:
    """Report where in the new-game flow the game currently is."""
    return _call("game_setup_status")


def select_scenario(name: str) -> dict:
    """Pick a scenario for a new game (e.g. "Crashlanded")."""
    return _call("select_scenario", {"name": name})


def select_storyteller(storyteller: str, difficulty: str | None = None) -> dict:
    """Choose storyteller + difficulty for a new game."""
    args: dict[str, str] = {"storyteller": storyteller}
    if difficulty:
        args["difficulty"] = difficulty
    return _call("select_storyteller", args)


def create_world() -> dict:
    """Generate the planet for a new game."""
    return _call("create_world")


def select_starting_site(tile_id: int | None = None, x: int | None = None, z: int | None = None) -> dict:
    """Choose a colony tile on the world map.

    Supply either ``tile_id`` or world-map ``x``/``z`` coordinates.
    """
    args: dict[str, int] = {}
    if tile_id is not None:
        args["tileId"] = tile_id
    if x is not None:
        args["x"] = x
    if z is not None:
        args["z"] = z
    return _call("select_starting_site", args)


def start_game() -> dict:
    """Finalize character creation and start the game."""
    return _call("start_game")


def edit_starting_pawn(action: str, index: int | None = None, to: int | None = None) -> dict:
    """Adjust starting colonists in the new-game pawn pool."""
    args: dict[str, str | int] = {"action": action}
    if index is not None:
        args["index"] = index
    if to is not None:
        args["to"] = to
    return _call("edit_starting_pawn", args)


'''
open('src/smartrim/counselor.py', 'w', encoding='utf-8').write(content[:start] + fixed + content[pause:])
print('done')
