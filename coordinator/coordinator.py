import anthropic
import base64
from pathlib import Path

client = anthropic.Anthropic()

# ── Path helpers ──────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent.parent



def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def _read_pdf(path: Path) -> dict | None:
    try:
        data = base64.standard_b64encode(path.read_bytes()).decode("utf-8")
        return {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": data}}
    except FileNotFoundError:
        return None


# ── Context assembly ──────────────────────────────────────────────────────────

def _career_context() -> str:
    try:
        from career.db_career import get_context_block
        return f"### Career Data\n{get_context_block()}"
    except Exception as e:
        return f"### Career Data\n(unavailable: {e})"


def _academia_context() -> str:
    try:
        from academia.db_academia import get_context_block
        return f"### Academia Data\n{get_context_block()}"
    except Exception as e:
        return f"### Academia Data\n(unavailable: {e})"


def _finance_context() -> str:
    try:
        from finance.db_finance import get_context_block
        result = get_context_block()
        if result:
            return f"### Finance Data\n{result}"
    except Exception:
        pass
    # Finance context lives in the prose file for now (no meaningful DB yet)
    return ""


def _fitness_context() -> str:
    # Fitness DB is a stub — nothing to pull yet
    try:
        from fitness.db_fitness import get_context_block
        result = get_context_block()
        if result:
            return f"### Fitness Data\n{result}"
    except Exception:
        pass
    # Fitness context lives in the prose file for now (no meaningful DB yet)
    return ""


def build_merged_context() -> str:
    """Assemble a single context string from all available sources."""
    sections = [
        _career_context(),
        _academia_context(),
        _finance_context(),
        _fitness_context(),
    ]
    return "\n\n".join(s for s in sections if s)


def build_content_blocks(user_message: str) -> list:
    """
    Build the content list for the API call:
      - Optional: resume PDF
      - Optional: course map PDF
      - Personal context prose
      - Merged DB context
      - The user's message
    """
    blocks = []

    # PDFs (best-effort — silently skipped if missing)
    for pdf_path in [ROOT / "career" / "resume.pdf", ROOT / "academia" / "course_map.pdf"]:
        pdf = _read_pdf(pdf_path)
        if pdf:
            blocks.append(pdf)
            print(f"Included PDF context from: {pdf_path.name}")
        else:
            print(f"No PDF found at: {pdf_path}, skipping.")

    # Personal context prose (single merged file)
    personal = _read(ROOT / "personal_context.md")

    # DB context
    db_context = build_merged_context()

    blocks.append({
        "type": "text",
        "text": (
            "## PERSONAL CONTEXT\n\n"
            f"{personal}\n\n"
            "## DATABASE CONTEXT\n\n"
            f"{db_context}\n\n"
            "---\n\n"
            f"{user_message}"
        )
    })

    return blocks


# ── Public interface ──────────────────────────────────────────────────────────

def load_system_prompt() -> str:
    return _read(ROOT / "coordinator" / "system-coordinator.md")


def ask(user_message: str) -> str:
    """Single-turn query through the coordinator."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        system=load_system_prompt(),
        messages=[
            {"role": "user", "content": build_content_blocks(user_message)}
        ]
    )
    return response.content[0].text


def chat_turn(conversation_history: list, user_message: str) -> tuple[str, list]:
    """
    One turn of a multi-turn chat.

    Pass in the current history, get back (reply, updated_history).
    The full context is only injected on the first turn; subsequent turns
    just append the raw user message so the context window stays lean.
    """
    if not conversation_history:
        # First message: inject full context
        content = build_content_blocks(user_message)
    else:
        # Subsequent messages: just the text
        content = user_message

    conversation_history.append({"role": "user", "content": content})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1500,
        system=load_system_prompt(),
        messages=conversation_history
    )

    reply = response.content[0].text
    conversation_history.append({"role": "assistant", "content": reply})

    return reply, conversation_history