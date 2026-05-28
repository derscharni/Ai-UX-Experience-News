#!/usr/bin/env python3
"""Daily AI UX Experience News Research Agent

Researches today's AI UX news via the Claude API (web search beta)
and writes a daily briefing in the repository style.

Usage:
    python scripts/research_agent.py
    python scripts/research_agent.py --date 2026-05-28

Requires:
    ANTHROPIC_API_KEY environment variable
    pip install anthropic
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
README_PATH = REPO_ROOT / "README.md"
THEMES_PATH = Path(__file__).parent / "monthly_themes.json"

# ── Known monthly themes ───────────────────────────────────────────────────────

BUILTIN_THEMES: dict[str, tuple[str, str]] = {
    "2026-02": ("operationalization-of-agentic-ai", "The Operationalization of Agentic AI"),
    "2026-03": ("the-agent-becomes-the-os", "The Agent Becomes the OS"),
    "2026-04": ("formalizing-the-agentic-workspace", "Formalizing the Agentic Workspace"),
}

# ── Helpers ────────────────────────────────────────────────────────────────────

def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:max_len].rstrip("-")


def load_themes() -> dict[str, tuple[str, str]]:
    themes: dict[str, tuple[str, str]] = dict(BUILTIN_THEMES)
    if THEMES_PATH.exists():
        try:
            stored = json.loads(THEMES_PATH.read_text())
            for k, v in stored.items():
                themes[k] = (v[0], v[1])
        except Exception:
            pass
    return themes


def save_theme(month_key: str, slug: str, title: str) -> None:
    stored: dict = {}
    if THEMES_PATH.exists():
        try:
            stored = json.loads(THEMES_PATH.read_text())
        except Exception:
            pass
    stored[month_key] = [slug, title]
    THEMES_PATH.write_text(json.dumps(stored, indent=2, ensure_ascii=False) + "\n")


def get_monthly_folder(date: datetime, themes: dict) -> tuple[Path | None, str | None, str | None]:
    """Return (folder, slug, title) for the month. Folder is None for a brand-new month."""
    month_key = date.strftime("%Y-%m")
    existing = sorted(BRIEFINGS_DIR.glob(f"{month_key}-*"))
    if existing:
        folder = existing[0]
        slug = folder.name.split("-", 2)[2] if len(folder.name.split("-", 2)) > 2 else "agentic-developments"
        _, title = themes.get(month_key, (slug, slug.replace("-", " ").title()))
        return folder, slug, title

    if month_key in themes:
        slug, title = themes[month_key]
        folder = BRIEFINGS_DIR / f"{month_key}-{slug}"
        folder.mkdir(parents=True, exist_ok=True)
        return folder, slug, title

    return None, None, None


def briefing_exists(date: datetime) -> bool:
    date_str = date.strftime("%Y-%m-%d")
    return bool(list(BRIEFINGS_DIR.glob(f"*/{date_str}-*.md")))


def load_recent_examples(n: int = 2) -> str:
    all_files = sorted(BRIEFINGS_DIR.glob("*/*.md"))
    if not all_files:
        return ""
    examples = []
    for path in all_files[-n:]:
        examples.append(f"=== EXAMPLE ({path.name}) ===\n\n{path.read_text()}")
    return "\n\n---\n\n".join(examples)


# ── Research & Writing ─────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are the editor of "Ai-UX-Experience-News", a daily briefing tracking UX and \
interaction design developments for the leading AI agent products.

Your editorial lens is exclusively Agent2Agent2Human Experience Design:
- Interface Evolution (generative UI, canvases, specialized workspaces)
- Interaction Patterns (delegation, clarification, control handoff between human and agent)
- Trust & Safety Design (transparency, audit trails, confidence signals, intent previews)
- Agentic Workflows (multi-step tasks, proactive assistance, background agents)
- Temporal UX (async long-running tasks, progress management)

You do NOT cover: model benchmark scores, parameter counts, training data, fundraising, \
or financial news unless it directly changes how users interact with the product."""


def research_and_write(date: datetime, examples: str) -> tuple[str, str]:
    """Return (briefing_markdown, briefing_title)."""
    client = anthropic.Anthropic()
    date_display = date.strftime("%B %d, %Y")
    month_display = date.strftime("%B %Y")

    # Cached block: examples don't change day-to-day → reuse across runs.
    # The date-specific instruction is a separate, non-cached block.
    cached_context = (
        f"Here are 2 recent example briefings showing the EXACT required format and editorial tone:\n\n"
        f"{examples}\n\n"
        f"---\n\n"
        f"Format rules (follow precisely):\n"
        f"# UX Briefing: [4–7 word title capturing today's macro UX theme]\n\n"
        f"**DATE**\n\n"
        f"Good morning. Today's briefing [one sentence on the macro trend].\n\n"
        f"## At a Glance\n\n"
        f"| Product | Key Development |\n| --- | --- |\n"
        f"| **Claude** | [one sentence + [N]] |\n"
        f"| **ChatGPT** | [one sentence + [N]] |\n"
        f"| **Google Gemini** | [one sentence + [N]] |\n"
        f"| **Microsoft Copilot** | [one sentence + [N]] |\n"
        f"| **Grok (xAI)** | [one sentence + [N]] |\n"
        f"| **Perplexity** | [one sentence + [N]] |\n\n"
        f"## Product Highlights\n\n"
        f"### [Title] — 2–3 analysis paragraphs per section (2–3 sections total)\n\n"
        f"## References\n\n"
        f"[N] Publisher. (Year, Month Day). *Title*. [url](url)\n\n"
        f"Rules: only real URLs from web searches · analyse UX implications not just features · "
        f"output ONLY the markdown, no preamble"
    )

    daily_instruction = (
        f"Today is {date_display}.\n\n"
        f"Research the last 48 hours for each product and write the briefing.\n\n"
        f"Products: Claude (Anthropic) · ChatGPT/OpenAI · Google Gemini · "
        f"Microsoft Copilot · Grok (xAI) · Perplexity\n\n"
        f"Search terms (adapt as needed):\n"
        f'- "Claude Anthropic update {month_display}"\n'
        f'- "ChatGPT OpenAI feature {month_display}"\n'
        f'- "Google Gemini interface {month_display}"\n'
        f'- "Microsoft Copilot UX {month_display}"\n'
        f'- "Grok xAI update {month_display}"\n'
        f'- "Perplexity AI {month_display}"\n\n'
        f"Focus: interface changes, interaction patterns, trust/safety UX, agentic workflows, multimodal UX.\n"
        f"Ignore: model benchmarks, pricing, financials unless they directly change UX.\n\n"
        f"Write the briefing now with **{date_display}** as the date."
    )

    response = client.beta.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        betas=["web-search-2025-03-05"],
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": cached_context,
                    "cache_control": {"type": "ephemeral"},
                },
                {
                    "type": "text",
                    "text": daily_instruction,
                },
            ],
        }],
    )

    briefing = ""
    for block in response.content:
        if getattr(block, "type", None) == "text":
            briefing = block.text.strip()

    if not briefing:
        raise RuntimeError("Claude returned an empty briefing — check API key and web search access")

    # Strip any accidental preamble before the # header
    match = re.search(r"^# UX Briefing:", briefing, re.MULTILINE)
    if match:
        briefing = briefing[match.start():]

    title_match = re.search(r"^# UX Briefing: (.+)$", briefing, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Daily UX Update"

    return briefing, title


def determine_month_theme(date: datetime, briefing: str) -> tuple[str, str]:
    """Ask Claude to choose a monthly theme based on the first briefing of the month."""
    client = anthropic.Anthropic()
    month = date.strftime("%B %Y")

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": (
                f"Based on this first briefing for {month}, suggest a short monthly theme title "
                f"in the style of these past themes:\n"
                f"- \"The Operationalization of Agentic AI\" (Feb 2026)\n"
                f"- \"The Agent Becomes the OS\" (Mar 2026)\n"
                f"- \"Formalizing the Agentic Workspace\" (Apr 2026)\n\n"
                f"Briefing excerpt:\n{briefing[:1500]}\n\n"
                f"Reply with ONLY a JSON object, no markdown fences:\n"
                f'{{\"slug\": \"kebab-case-slug\", \"title\": \"Display Title\"}}'
            ),
        }],
    )

    try:
        raw = response.content[0].text.strip()
        # Remove possible markdown code fences
        raw = re.sub(r"```[a-z]*\n?", "", raw).strip()
        data = json.loads(raw)
        return data["slug"], data["title"]
    except Exception:
        month_slug = date.strftime("%B").lower()
        return f"agentic-evolution-{month_slug}", f"Agentic Evolution: {month}"


# ── README Update ──────────────────────────────────────────────────────────────

def update_readme(
    briefing_path: Path,
    title: str,
    date: datetime,
    monthly_folder: Path,
    theme_title: str,
) -> None:
    content = README_PATH.read_text()
    rel = str(briefing_path.relative_to(REPO_ROOT))
    date_str = date.strftime("%Y-%m-%d")
    month_name = date.strftime("%B %Y")
    folder_name = monthly_folder.name

    # Check if briefing is already listed
    if rel in content:
        return

    new_entry = f"*   [{date_str} - {title}]({rel})\n"
    month_header = f"### {month_name}"

    if month_header in content:
        month_pos = content.index(month_header)
        after = content[month_pos + len(month_header):]
        next_sec = re.search(r"\n###", after)
        section = after[: next_sec.start()] if next_sec else after
        bullets = list(re.finditer(r"\*   \[.+?\]\(.+?\)\n", section))
        if bullets:
            insert = month_pos + len(month_header) + bullets[-1].end()
        else:
            insert = month_pos + len(month_header) + 1
            new_entry = "\n" + new_entry
        content = content[:insert] + new_entry + content[insert:]
    else:
        anchor = "## Monthly Management Summaries"
        if anchor in content:
            pos = content.index(anchor)
            new_section = (
                f"### {month_name} — *{theme_title}* (`briefings/{folder_name}/`)\n"
                f"{new_entry}\n"
            )
            content = content[:pos] + new_section + content[pos:]

    README_PATH.write_text(content)


# ── Git Operations ─────────────────────────────────────────────────────────────

def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    )


def commit_and_push(files: list[Path], date: datetime) -> None:
    date_str = date.strftime("%Y-%m-%d")
    for f in files:
        git("add", str(f))

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT, capture_output=True, text=True
    )
    if not status.stdout.strip():
        print("No changes to commit.")
        return

    git("commit", "-m", f"Add UX briefing for {date_str}")

    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    # Retry push up to 4 times with exponential backoff
    import time
    for attempt, wait in enumerate([0, 2, 4, 8, 16]):
        if attempt > 0:
            print(f"Push failed, retrying in {wait}s...")
            time.sleep(wait)
        result = subprocess.run(
            ["git", "push", "-u", "origin", branch],
            cwd=REPO_ROOT, capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"Pushed to {branch}")
            return
        if attempt == 4:
            print(f"Push failed after 4 attempts:\n{result.stderr}", file=sys.stderr)
            sys.exit(1)


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[1] == "--date":
        date = datetime.strptime(sys.argv[2], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        date = datetime.now(timezone.utc)

    date_str = date.strftime("%Y-%m-%d")
    print(f"[research_agent] date={date_str}")

    if briefing_exists(date):
        print(f"Briefing for {date_str} already exists — skipping.")
        return

    themes = load_themes()
    monthly_folder, theme_slug, theme_title = get_monthly_folder(date, themes)

    examples = load_recent_examples()

    print("Researching and writing briefing via Claude API…")
    briefing, title = research_and_write(date, examples)
    print(f"  Title: {title}")

    if monthly_folder is None:
        print("New month — determining monthly theme…")
        theme_slug, theme_title = determine_month_theme(date, briefing)
        print(f"  Theme: {theme_title}")
        month_key = date.strftime("%Y-%m")
        save_theme(month_key, theme_slug, theme_title)
        monthly_folder = BRIEFINGS_DIR / f"{month_key}-{theme_slug}"
        monthly_folder.mkdir(parents=True, exist_ok=True)

    filename = f"{date_str}-{slugify(title)}.md"
    briefing_path = monthly_folder / filename
    briefing_path.write_text(briefing)
    print(f"  Saved: {briefing_path.relative_to(REPO_ROOT)}")

    print("Updating README…")
    update_readme(briefing_path, title, date, monthly_folder, theme_title)

    files_to_commit: list[Path] = [briefing_path, README_PATH]
    if THEMES_PATH.exists():
        files_to_commit.append(THEMES_PATH)

    print("Committing and pushing…")
    commit_and_push(files_to_commit, date)
    print("Done.")


if __name__ == "__main__":
    main()
