#!/usr/bin/env python3
"""Sync Ai-UX-Experience-News briefings to an Obsidian vault.

Reads briefings from the local git clone, adds Obsidian-compatible YAML
frontmatter (date, tags, products, Dataview fields) and writes them into
the configured vault folder.  Already-synced notes are skipped.

Setup
-----
1.  Clone the repo once:
        git clone https://github.com/derscharni/Ai-UX-Experience-News
2.  Copy the config template:
        cp scripts/obsidian_config.example.json scripts/obsidian_config.json
3.  Edit obsidian_config.json — set vault_path and folders.
4.  Run once to do the initial full sync:
        python scripts/sync_to_obsidian.py
5.  Automate with cron (runs git pull first, then syncs):
        # Example crontab entry — runs every weekday at 08:00 local time
        0 8 * * 1-5 cd /path/to/repo && git pull -q && python scripts/sync_to_obsidian.py

Usage
-----
    python scripts/sync_to_obsidian.py                  # sync all new notes
    python scripts/sync_to_obsidian.py --since 2026-05-01  # only on/after date
    python scripts/sync_to_obsidian.py --dry-run        # preview without writing
    python scripts/sync_to_obsidian.py --force          # overwrite existing notes
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from generate_index import extract_excerpt

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT    = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
SUMMARIES    = sorted(REPO_ROOT.glob("summary-*.md"))
CONFIG_PATH  = Path(__file__).parent / "obsidian_config.json"
EXAMPLE_PATH = Path(__file__).parent / "obsidian_config.example.json"
RAW_BASE     = "https://raw.githubusercontent.com/derscharni/Ai-UX-Experience-News/main"

# ── Product detection ──────────────────────────────────────────────────────────

PRODUCT_KEYWORDS: dict[str, list[str]] = {
    "claude":      ["claude", "anthropic"],
    "chatgpt":     ["chatgpt", "openai", "codex", "sora", "operator"],
    "gemini":      ["gemini", "notebooklm", "google ai"],
    "copilot":     ["copilot", "microsoft", "github copilot", "bing ai"],
    "grok":        ["grok", "xai", "𝕏", "tesla"],
    "perplexity":  ["perplexity"],
}

PRODUCT_DISPLAY: dict[str, str] = {
    "claude":     "Claude (Anthropic)",
    "chatgpt":    "ChatGPT (OpenAI)",
    "gemini":     "Google Gemini",
    "copilot":    "Microsoft Copilot",
    "grok":       "Grok (xAI)",
    "perplexity": "Perplexity",
}


def detect_products(content: str) -> list[str]:
    found: list[str] = []
    lower = content.lower()
    for product, keywords in PRODUCT_KEYWORDS.items():
        if any(kw in lower for kw in keywords):
            found.append(product)
    return found


def yaml_escape(text: str) -> str:
    """Make text safe inside a double-quoted YAML scalar."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


# ── Monthly theme lookup ───────────────────────────────────────────────────────

def month_theme_from_folder(folder: Path) -> str:
    """'2026-04-formalizing-the-agentic-workspace' → 'Formalizing the Agentic Workspace'"""
    parts = folder.name.split("-", 2)
    if len(parts) > 2:
        return parts[2].replace("-", " ").title()
    return ""


def month_theme_title_from_folder(folder: Path) -> str:
    """Return the human-readable month theme, trying themes file first."""
    month_key = folder.name[:7]  # "2026-04"
    themes_file = Path(__file__).parent / "monthly_themes.json"
    if themes_file.exists():
        try:
            data = json.loads(themes_file.read_text())
            if month_key in data:
                return data[month_key][1]
        except Exception:
            pass
    return month_theme_from_folder(folder)


# ── Obsidian note conversion ───────────────────────────────────────────────────

def briefing_to_obsidian(path: Path) -> str:
    """Convert a briefing markdown file to an Obsidian note with YAML frontmatter."""
    content = path.read_text()

    date_str = path.stem[:10]  # "2026-04-30"
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return content  # fallback: return as-is

    title_match = re.search(r"^# UX Briefing: (.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem
    description = extract_excerpt(content)

    month_theme = month_theme_title_from_folder(path.parent)
    products     = detect_products(content)
    product_tags = [f"product/{p}" for p in products]
    resource     = f"{RAW_BASE}/{path.relative_to(REPO_ROOT).as_posix()}"

    # ── Build YAML frontmatter ──────────────────────────────────────────────────
    # Core fields follow Open Knowledge Format v0.1 (type/title/description/
    # resource/tags/timestamp — github.com/GoogleCloudPlatform/knowledge-catalog),
    # so any OKF-aware tool can read these notes too. Everything past `tags` is
    # a domain-specific extension — OKF explicitly allows and preserves those.
    lines = [
        "---",
        "type: Daily Briefing",
        f'title: "UX Briefing: {yaml_escape(title)}"',
        f'description: "{yaml_escape(description)}"',
        f"resource: {resource}",
    ]
    lines.append("tags:")
    lines += ["  - ai-ux", "  - briefing"]
    for t in product_tags:
        lines.append(f"  - {t}")
    lines.append(f"timestamp: {date_str}T00:00:00Z")
    lines.append(f"date: {date_str}")
    if month_theme:
        lines.append(f'month-theme: "{yaml_escape(month_theme)}"')
    if products:
        lines.append("products:")
        for p in products:
            lines.append(f"  - {PRODUCT_DISPLAY[p]}")
    lines += [
        "source: https://github.com/derscharni/Ai-UX-Experience-News",
        "---",
        "",
    ]

    return "\n".join(lines) + content


def summary_to_obsidian(path: Path) -> str:
    """Convert a monthly summary markdown to an Obsidian note."""
    content = path.read_text()

    # filename: summary-2026-04.md → date 2026-04-30 (end of month)
    m = re.search(r"summary-(\d{4}-\d{2})\.md", path.name)
    if not m:
        return content

    year_month = m.group(1)
    # last day of the month for sorting
    import calendar
    y, mo = int(year_month[:4]), int(year_month[5:])
    last_day = calendar.monthrange(y, mo)[1]
    date_str = f"{year_month}-{last_day:02d}"

    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem
    description = extract_excerpt(content)
    resource = f"{RAW_BASE}/{path.relative_to(REPO_ROOT).as_posix()}"

    lines = [
        "---",
        "type: Monthly Summary",
        f'title: "{yaml_escape(title)}"',
        f'description: "{yaml_escape(description)}"',
        f"resource: {resource}",
        "tags:",
        "  - ai-ux",
        "  - monthly-summary",
        f"timestamp: {date_str}T00:00:00Z",
        f"date: {date_str}",
        "source: https://github.com/derscharni/Ai-UX-Experience-News",
        "---",
        "",
    ]
    return "\n".join(lines) + content


# ── Config ─────────────────────────────────────────────────────────────────────

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(
            f"Config file not found.\n"
            f"Copy the example and edit it:\n"
            f"  cp {EXAMPLE_PATH} {CONFIG_PATH}\n"
            f"Falling back to dry-run mode."
        )
        return {
            "vault_path": None,
            "briefings_folder": "AI-UX-News/Daily Briefings",
            "summaries_folder": "AI-UX-News/Monthly Summaries",
            "dry_run": True,
        }
    return json.loads(CONFIG_PATH.read_text())


# ── Sync logic ─────────────────────────────────────────────────────────────────

def write_note(content: str, dest: Path, force: bool, dry_run: bool) -> str:
    """Write note to dest. Returns 'created', 'updated', 'skipped', or 'dry'."""
    if dry_run:
        return "dry"
    if dest.exists() and not force:
        return "skipped"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    return "updated" if dest.exists() else "created"


def sync(since: str | None = None, dry_run: bool = False, force: bool = False) -> None:
    config   = load_config()
    dry_run  = dry_run or config.get("dry_run", False)
    vault    = Path(config["vault_path"]) if config.get("vault_path") else None
    b_folder = config.get("briefings_folder", "AI-UX-News/Daily Briefings")
    s_folder = config.get("summaries_folder", "AI-UX-News/Monthly Summaries")

    if dry_run:
        print("[DRY RUN] no files will be written\n")

    counts = {"created": 0, "updated": 0, "skipped": 0, "dry": 0}

    # ── Daily briefings ────────────────────────────────────────────────────────
    briefing_files = sorted(BRIEFINGS_DIR.glob("*/*.md"))
    if since:
        briefing_files = [f for f in briefing_files if f.stem[:10] >= since]

    for src in briefing_files:
        date_str = src.stem[:10]
        if not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
            continue

        note = briefing_to_obsidian(src)
        if vault:
            dest = vault / b_folder / src.name
            status = write_note(note, dest, force, dry_run)
        else:
            status = "dry"
            print(f"\n{'─'*60}\nPREVIEW: {src.name}\n{'─'*60}")
            print(note[:600])
            print("  [... truncated ...]")

        counts[status] += 1
        if status != "skipped":
            print(f"  [{status:7s}] briefings/{src.parent.name}/{src.name}")

    # ── Monthly summaries ──────────────────────────────────────────────────────
    for src in SUMMARIES:
        note = summary_to_obsidian(src)
        if vault:
            dest = vault / s_folder / src.name
            status = write_note(note, dest, force, dry_run)
        else:
            status = "dry"

        counts[status] += 1
        if status != "skipped":
            print(f"  [{status:7s}] {src.name}")

    print(
        f"\n{'─'*40}\n"
        f"Briefings + summaries:\n"
        f"  created/updated : {counts['created'] + counts['updated'] + counts['dry']}\n"
        f"  skipped         : {counts['skipped']}\n"
    )
    if vault and not dry_run:
        print(f"Vault target: {vault / b_folder}")


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]
    since    = None
    dry_run  = False
    force    = False

    i = 0
    while i < len(args):
        if args[i] == "--since" and i + 1 < len(args):
            since = args[i + 1]
            i += 2
        elif args[i] == "--dry-run":
            dry_run = True
            i += 1
        elif args[i] == "--force":
            force = True
            i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    sync(since=since, dry_run=dry_run, force=force)


if __name__ == "__main__":
    main()
