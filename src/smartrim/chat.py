"""Interactive colony chat using local LLM.

Usage:
    python sidecar/chat.py
    python sidecar/chat.py --model gemma4-e2b-rimworld

Type questions about the colony. The LLM has access to current game state.
Commands: quit/exit to leave, status to refresh colony state, say to display last answer in-game.
"""
import argparse
import json
import urllib.error

from smartrim.counselor import game_state, say
from smartrim.llm import generate

SYSTEM = """You are SmartRim, a RimWorld colony advisor. You have access to the
current colony state (provided below). Answer questions concisely and practically.
When suggesting actions, be specific (work types, priorities, coordinates).
Keep answers under 200 words. If you don't know, say so."""


def get_context():
    """Gather current colony state for the LLM."""
    gs = game_state()
    return gs


def chat_loop(model="gemma4-e2b-rimworld"):
    print("SmartRim Chat (type 'quit' to exit, 'status' to refresh, 'say' to display last answer in-game)")
    print("Model:", model)
    print("-" * 60)

    last_answer = ""
    while True:
        try:
            q = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not q:
            continue
        if q.lower() in ("quit", "exit", "q"):
            print("Goodbye.")
            break
        if q.lower() == "status":
            gs = get_context()
            print(json.dumps(gs, indent=2, default=str)[:2000])
            continue
        if q.lower() == "say" and last_answer:
            say(last_answer[:480])
            print("(Displayed in-game)")
            continue

        gs = get_context()
        prompt = f"Colony state:\n{json.dumps(gs, default=str, indent=1)[:3500]}\n\nQuestion: {q}"
        try:
            answer = generate(prompt, provider="ollama", model=model,
                             system=SYSTEM, temperature=0.5, num_ctx=8192)
        except (urllib.error.URLError, json.JSONDecodeError, OSError, ValueError) as e:
            answer = f"(LLM error: {e})"
        last_answer = answer
        print(f"\nSmartRim: {answer}")


def main():
    parser = argparse.ArgumentParser(description="Interactive colony chat via local LLM")
    parser.add_argument("--model", default="gemma4-e2b-rimworld")
    parser.add_argument("--say", action="store_true", help="Display answers in-game")
    args = parser.parse_args()
    chat_loop(model=args.model)


if __name__ == "__main__":
    main()
