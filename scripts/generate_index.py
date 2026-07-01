#!/usr/bin/env python3
"""Generate docs/briefings.json — the index used by the HTML news reader.

Extracts per-briefing metadata used by the magazine homepage:
  date, title, path, month theme/key, an excerpt (intro paragraph),
  and the list of products covered (from the "At a Glance" table).
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
DOCS_DIR = REPO_ROOT / "docs"

# Canonical product names we track, with detection keywords.
PRODUCTS = {
    "Claude": ["claude", "anthropic"],
    "ChatGPT": ["chatgpt", "openai", "gpt-", "codex", "sora", "operator"],
    "Gemini": ["gemini", "notebooklm", "google"],
    "Copilot": ["copilot", "microsoft"],
    "Grok": ["grok", "xai"],
    "Perplexity": ["perplexity", "comet"],
}

# UX themes, with detection keywords. Every briefing mentions nearly every
# product (it's a daily roundup), so the product chips above barely narrow
# anything down — see docs/index.html's second filter row. Themes are meant
# to actually differentiate: instead of "any keyword present" (which suffers
# the same problem once a corpus is even lightly topical — everything ends up
# tagged with everything), we rank themes by keyword *hit count* per article
# and keep only the top 2 that clear a minimum count, so tags reflect an
# article's dominant focus rather than everything it briefly touches.
THEMES = {
    "Trust & Safety": ["trust", "safety", "guardrail", "permission", "governance", "audit",
                        "transparen", "refusal", "consent", "safeguard", "oversight", "verif",
                        "confidence signal", "accountab"],
    "Generative UI": ["generative ui", "canvas", "visual layout", "dynamic view", "interactive",
                       "rendered interface", "design system", "custom-coded", "bespoke"],
    "Agentic Workflows": ["workflow", "orchestrat", "subagent", "sub-agent", "background agent",
                           "multi-step", "parallel", "autonomous task", "delegat", "task queue"],
    "Memory & Context": ["memory", "personalizat", "context window", "recall", "carry-forward",
                          "compaction", "long-horizon"],
    "Browser & Computer Use": ["browser", "browsing agent", "computer use", "navigate websit",
                                "agentic browsing", "auto browse"],
    "Multimodal": ["multimodal", "voice mode", "voice input", "voice assistant", "voice command",
                    "voice cloning", "voice chat", "voice interface", "image generat", "video generat",
                    "vision model", "speech-to-text", "text-to-speech"],
    "Enterprise & Governance": ["enterprise", "admin console", "workspace admin", "compliance",
                                 "deployment", "business tier", "edu admin"],
    "Identity & Security": ["identity", "authenticat", "session securit", "credential", "password",
                             "sso", "oauth"],
}
THEME_TOP_N = 2
THEME_MIN_HITS = 2


def strip_md(text: str) -> str:
    """Remove markdown emphasis/links/comments for a clean excerpt."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\[(\d+)\]", "", text)                 # citation markers [1]
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"[*_`#]", "", text)                    # emphasis chars
    return re.sub(r"\s+", " ", text).strip()


def extract_excerpt(content: str) -> str:
    """First real paragraph after the title/date line."""
    for line in content.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        # Skip the bold date line like "**April 30, 2026**"
        if re.fullmatch(r"\*\*.+\*\*", s):
            continue
        excerpt = strip_md(s)
        # Drop a leading "Good morning." greeting for a punchier card.
        excerpt = re.sub(r"^Good morning[.,]?\s*", "", excerpt)
        if len(excerpt) > 20:
            return excerpt[:240]
    return ""


def detect_products(content: str) -> list[str]:
    """Products covered, ordered by the canonical PRODUCTS order."""
    # Restrict to the At a Glance table if present for precision.
    glance = re.search(r"## At a Glance(.+?)(?:\n## |\Z)", content, re.DOTALL)
    scope = glance.group(1).lower() if glance else content.lower()
    found = []
    for name, kws in PRODUCTS.items():
        if any(kw in scope for kw in kws):
            found.append(name)
    return found


def detect_themes(content: str) -> list[str]:
    """The 1-2 UX themes this briefing is actually about, ranked by keyword
    hit count so tags stay differentiating instead of "present in everything"."""
    lower = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL).lower()
    scores = {}
    for theme, kws in THEMES.items():
        c = sum(lower.count(kw) for kw in kws)
        if c > 0:
            scores[theme] = c
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])[:THEME_TOP_N]
    return [t for t, c in ranked if c >= THEME_MIN_HITS]


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
            "excerpt": extract_excerpt(content),
            "products": detect_products(content),
            "themes": detect_themes(content),
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
