#!/usr/bin/env python3
"""Generate a monthly management summary from that month's daily briefings.

The Feb/March/April summaries at the repo root (summary-2026-0X.md) were
written before this automation existed. Nothing has generated one since —
research_agent.py only writes daily briefings — which is why months can go
by with no summary even though the daily briefings exist. This script closes
that gap: it reads every daily briefing for a given month and asks Claude to
synthesize the same "Management Summary" format as the existing ones
(Executive Overview, Key Themes & Trends, Most Significant Developments
table), using the 3 existing summaries as style examples.

No web search needed — this is pure synthesis over already-written content.

Usage:
    python scripts/generate_summary.py                # previous calendar month
    python scripts/generate_summary.py --month 2026-06
    python scripts/generate_summary.py --month 2026-06 --force
"""

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

REPO_ROOT = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
README_PATH = REPO_ROOT / "README.md"

MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def previous_month(today: datetime) -> str:
    year, month = today.year, today.month - 1
    if month == 0:
        year, month = year - 1, 12
    return f"{year:04d}-{month:02d}"


def summary_exists(month_key: str) -> bool:
    return (REPO_ROOT / f"summary-{month_key}.md").exists()


def load_month_briefings(month_key: str) -> list[tuple[str, str, str]]:
    """Return [(date_str, title, content), ...] for every briefing in the month, sorted."""
    files = sorted(BRIEFINGS_DIR.glob(f"*/{month_key}-*.md"))
    out = []
    for path in files:
        content = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# UX Briefing: (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem
        out.append((path.stem[:10], title, content))
    return out


def load_example_summaries(n: int = 2) -> str:
    files = sorted(REPO_ROOT.glob("summary-*.md"))[-n:]
    return "\n\n---\n\n".join(
        f"=== EXAMPLE ({f.name}) ===\n\n{f.read_text(encoding='utf-8')}" for f in files
    )


def generate_summary(month_key: str, briefings: list[tuple[str, str, str]]) -> str:
    year, month = int(month_key[:4]), int(month_key[5:7])
    month_display = f"{MONTH_NAMES[month - 1]} {year}"

    examples = load_example_summaries()
    briefings_text = "\n\n".join(
        f"--- {date} : {title} ---\n{content}" for date, title, content in briefings
    )

    system_prompt = (
        "You are the editor of \"Ai-UX-Experience-News\", writing a monthly management "
        "summary that synthesizes a month of daily UX briefings into a 1-2 page executive "
        "overview for a UX leadership audience. Your lens is exclusively Agent2Agent2Human "
        "Experience Design: Interface Evolution, Interaction Patterns, Trust & Safety Design, "
        "Agentic Workflows, Temporal UX. You do NOT cover model benchmarks, pricing, or "
        "financial news unless it directly changes how users interact with the product."
    )

    instruction = (
        f"Here are 2 example management summaries showing the exact required format:\n\n"
        f"{examples}\n\n---\n\n"
        f"REQUIRED FORMAT (reproduce exactly):\n\n"
        f"# Management Summary: {month_display}\n\n"
        f"## Executive Overview\n"
        f"[2 paragraphs identifying the month's overarching theme(s) and why they matter.]\n\n"
        f"## Key Themes & Trends\n\n"
        f"### 1. [Theme title]\n"
        f"[One framing sentence.]\n"
        f"*   **[Bold sub-topic]:** [1-2 sentences with specifics from the briefings.]\n"
        f"*   **[Bold sub-topic]:** [1-2 sentences.]\n"
        f"*   **[Bold sub-topic]:** [1-2 sentences.]\n\n"
        f"### 2. [Theme title]\n[Same structure — 3-4 themes total, ranked by significance.]\n\n"
        f"## Most Significant Developments ({month_display})\n\n"
        f"| Briefing Theme & Date | Key Development | Strategic Impact |\n"
        f"| :--- | :--- | :--- |\n"
        f"| \"[Briefing title]\" — [Month] [Day] | [Development] | [Why it matters strategically] |\n"
        f"[One row per briefing day provided below — do not skip any.]\n\n"
        f"Rules:\n"
        f"- Synthesize across days into 3-4 named macro themes; do not just list days chronologically "
        f"in the prose sections.\n"
        f"- Every theme's bullets must cite specifics (product names, feature names) drawn only from "
        f"the briefings below — do not invent anything not present in them.\n"
        f"- The table must have exactly one row per briefing date provided.\n"
        f"- Output ONLY the markdown — no preamble, no commentary, no code fences.\n\n"
        f"Here are all {len(briefings)} daily briefings for {month_display}, oldest first:\n\n"
        f"{briefings_text}"
    )

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": instruction}],
    )
    summary = response.content[0].text.strip()

    match = re.search(r"^# Management Summary:", summary, re.MULTILINE)
    if match:
        summary = summary[match.start():].strip()

    required = ["## Executive Overview", "## Key Themes", "## Most Significant Developments"]
    missing = [r for r in required if r not in summary]
    if missing:
        raise RuntimeError(
            f"Generated summary is malformed — missing sections: {', '.join(missing)}. "
            f"stop_reason={response.stop_reason!r}\n\nFirst 500 chars:\n{summary[:500]}"
        )

    return summary


def generate_readme_blurb(month_key: str, summary: str) -> str:
    """One sentence for the README bullet, in the style of the existing ones."""
    client = anthropic.Anthropic()
    year, month = int(month_key[:4]), int(month_key[5:7])
    month_display = f"{MONTH_NAMES[month - 1]} {year}"
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=150,
        messages=[{
            "role": "user",
            "content": (
                f"Write ONE sentence (no more) summarizing this {month_display} UX briefing "
                f"summary's main themes, in the style of: \"Details the formalization of Agentic "
                f"UX patterns, the fragmentation of generic chat windows into specialized "
                f"workspaces, and the expansion of multimodal, multi-agent workflows.\"\n\n"
                f"Reply with ONLY the sentence, no quotes, no preamble.\n\n{summary[:3000]}"
            ),
        }],
    )
    return response.content[0].text.strip()


def update_readme(month_key: str, blurb: str) -> None:
    year, month = int(month_key[:4]), int(month_key[5:7])
    month_display = f"{MONTH_NAMES[month - 1]} {year}"
    content = README_PATH.read_text()
    rel = f"summary-{month_key}.md"
    if rel in content:
        return

    new_entry = f"*   [**{month_display} Summary**]({rel}): {blurb}\n"
    anchor = "## Monthly Management Summaries"
    if anchor not in content:
        return
    pos = content.index(anchor)
    section_end = content.index("\n\n## ", pos + len(anchor))
    insert_at = section_end
    content = content[:insert_at] + "\n" + new_entry + content[insert_at:]
    README_PATH.write_text(content)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO_ROOT, check=True, capture_output=True, text=True)


def commit_and_push(files: list[Path], month_key: str) -> None:
    for f in files:
        git("add", str(f))
    status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True)
    if not status.stdout.strip():
        print("No changes to commit.")
        return
    git("commit", "-m", f"Add management summary for {month_key}")
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    git("push", "-u", "origin", branch)
    print(f"Pushed to {branch}")


def run_for_month(month_key: str, force: bool) -> None:
    print(f"\n[generate_summary] month={month_key}")
    if summary_exists(month_key) and not force:
        print(f"summary-{month_key}.md already exists — skipping (use --force to overwrite).")
        return

    briefings = load_month_briefings(month_key)
    if not briefings:
        print(f"No daily briefings found for {month_key} — nothing to summarize.")
        return
    print(f"Found {len(briefings)} daily briefings for {month_key}.")

    print("Synthesizing summary via Claude API…")
    summary = generate_summary(month_key, briefings)

    out_path = REPO_ROOT / f"summary-{month_key}.md"
    out_path.write_text(summary + "\n")
    print(f"  Saved: {out_path.name}")

    print("Generating README blurb…")
    blurb = generate_readme_blurb(month_key, summary)
    update_readme(month_key, blurb)

    print("Committing and pushing…")
    commit_and_push([out_path, README_PATH], month_key)
    print("Done.")


def main() -> None:
    args = sys.argv[1:]
    force = "--force" in args
    args = [a for a in args if a != "--force"]

    if len(args) == 2 and args[0] == "--month":
        month_key = args[1]
    elif not args:
        month_key = previous_month(datetime.now(timezone.utc))
    else:
        print("Usage: python scripts/generate_summary.py [--month YYYY-MM] [--force]", file=sys.stderr)
        sys.exit(1)

    run_for_month(month_key, force)


if __name__ == "__main__":
    main()
