#!/usr/bin/env python3
"""Generate docs/briefings.json — the index used by the HTML news reader."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
DOCS_DIR = REPO_ROOT / "docs"


def main() -> None:
    DOCS_DIR.mkdir(exist_ok=True)

    briefings = []
    for path in sorted(BRIEFINGS_DIR.glob("*/*.md"), reverse=True):
        date_str = path.stem[:10]
        if not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
            continue

        content = path.read_text()
        title_match = re.search(r"^# UX Briefing: (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem

        folder = path.parent.name          # "2026-04-formalizing-the-agentic-workspace"
        parts = folder.split("-", 2)
        month_theme = parts[2].replace("-", " ").title() if len(parts) > 2 else ""

        briefings.append({
            "date": date_str,
            "title": title,
            "path": str(path.relative_to(REPO_ROOT)),
            "month_theme": month_theme,
            "month_key": date_str[:7],     # "2026-04"
        })

    summaries = []
    for path in sorted(REPO_ROOT.glob("summary-*.md"), reverse=True):
        m = re.search(r"summary-(\d{4}-\d{2})\.md", path.name)
        if m:
            summaries.append({"month": m.group(1), "path": path.name})

    index = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "briefings": briefings,
        "summaries": summaries,
    }

    out = DOCS_DIR / "briefings.json"
    out.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    print(f"Generated {out} — {len(briefings)} briefings, {len(summaries)} summaries")


if __name__ == "__main__":
    main()
