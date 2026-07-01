#!/usr/bin/env python3
"""Generate docs/feed.xml — an RSS 2.0 feed of the briefings index.

Lets any feed reader or "second brain" RSS-ingestion plugin (Obsidian's RSS
Reader community plugin, Logseq, Readwise Reader, Zapier/IFTTT, etc.) pick up
new briefings automatically without polling the GitHub API or scraping HTML.

Runs after generate_index.py — it just reprojects docs/briefings.json as XML,
so the two files are always in sync.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
SITE_URL = "https://derscharni.github.io/Ai-UX-Experience-News/"
FEED_TITLE = "AI·UX Experience News"
FEED_DESC = "Daily briefings tracking UX and interaction design across the leading AI agents."
MAX_ITEMS = 60


def rfc822(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return dt.strftime("%a, %d %b %Y %H:%M:%S GMT")


def item_xml(b: dict) -> str:
    link = f"{SITE_URL}#{quote(b['path'], safe='')}"
    # One <category> per tag (products + themes) — the RSS-correct way to
    # emit multiple discrete tags, rather than one comma-joined string.
    categories = list(b.get("products", [])) + list(b.get("themes", []))
    category_xml = "".join(f"    <category>{escape(c)}</category>\n" for c in categories)
    return (
        "  <item>\n"
        f"    <title>{escape(b['title'])}</title>\n"
        f"    <link>{escape(link)}</link>\n"
        f"    <guid isPermaLink=\"true\">{escape(link)}</guid>\n"
        f"    <pubDate>{rfc822(b['date'])}</pubDate>\n"
        f"    <description>{escape(b.get('excerpt', ''))}</description>\n"
        + category_xml
        + "  </item>"
    )


def main() -> None:
    index_path = DOCS_DIR / "briefings.json"
    index = json.loads(index_path.read_text())
    briefings = index["briefings"][:MAX_ITEMS]

    items = "\n".join(item_xml(b) for b in briefings)
    build_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    last_pub = rfc822(briefings[0]["date"]) if briefings else build_date

    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n'
        "<channel>\n"
        f"  <title>{escape(FEED_TITLE)}</title>\n"
        f"  <link>{escape(SITE_URL)}</link>\n"
        f"  <description>{escape(FEED_DESC)}</description>\n"
        "  <language>en</language>\n"
        f"  <lastBuildDate>{build_date}</lastBuildDate>\n"
        f"  <pubDate>{last_pub}</pubDate>\n"
        f"{items}\n"
        "</channel>\n"
        "</rss>\n"
    )

    out = DOCS_DIR / "feed.xml"
    out.write_text(feed)
    print(f"Generated {out} — {len(briefings)} items")


if __name__ == "__main__":
    main()
