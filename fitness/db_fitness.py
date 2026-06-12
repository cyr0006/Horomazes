from pathlib import Path

CONTEXT_PATH = Path(__file__).parent / "system-fitness.md"

def init_db():
    pass  # No DB yet

def get_context_block():
    try:
        return CONTEXT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""