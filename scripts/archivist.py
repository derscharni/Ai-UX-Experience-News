#!/usr/bin/env python3
"""The Archivist — cross-links AI-UX notes inside an Obsidian vault.

It scans three kinds of notes living side by side in the vault:

  • Daily briefings      (written by research_agent.py → synced by sync_to_obsidian.py)
  • Monthly summaries     (synced by sync_to_obsidian.py)
  • On-demand research    (e.g. files produced by the /last30days skill)

For every note it computes a TF-IDF similarity against all other notes and
appends a "Related Notes" section with Obsidian `[[wikilinks]]` to the most
related ones, plus the shared products / keywords that connect them. This is
what turns a flat pile of notes into a navigable, interlinked knowledge base:
a /last30days deep-dive on "AI UX agent design" will automatically surface the
daily briefings that touched the same topic, and vice-versa.

The Related section is wrapped in marker comments and fully regenerated on each
run, so the Archivist is idempotent — run it as often as you like.

Setup
-----
Reuses scripts/obsidian_config.json (see obsidian_config.example.json).
Add an optional "research_folder" pointing at where /last30days saves notes
*inside the vault*, e.g. "AI-UX-News/Research".

Usage
-----
    python scripts/archivist.py                 # cross-link the whole vault
    python scripts/archivist.py --dry-run       # preview, write nothing
    python scripts/archivist.py --max-links 4   # links per note (default 5)
    python scripts/archivist.py --min-score 0.08

With no vault configured it previews against the repo's own briefings so you
can see the linking logic in action.
"""

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

# ── Paths & config ───────────────────────────────────────────────────────────

REPO_ROOT     = Path(__file__).parent.parent
BRIEFINGS_DIR = REPO_ROOT / "briefings"
CONFIG_PATH   = Path(__file__).parent / "obsidian_config.json"

MARK_START = "<!-- ARCHIVIST:START -->"
MARK_END   = "<!-- ARCHIVIST:END -->"

# Products we recognise — overlap is weighted heavily since it is a strong
# signal that two notes are about the same thing.
PRODUCT_KEYWORDS: dict[str, list[str]] = {
    "Claude":     ["claude", "anthropic"],
    "ChatGPT":    ["chatgpt", "openai", "codex", "sora", "operator", "gpt-"],
    "Gemini":     ["gemini", "notebooklm"],
    "Copilot":    ["copilot", "microsoft"],
    "Grok":       ["grok", "xai"],
    "Perplexity": ["perplexity", "comet"],
}

STOPWORDS = set("""
a about above after again against all am an and any are aren't as at be because been
before being below between both but by can cannot could couldn't did didn't do does
doesn't doing don't down during each few for from further had hadn't has hasn't have
haven't having he he'd he'll he's her here here's hers herself him himself his how
how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most
mustn't my myself no nor not of off on once only or other ought our ours ourselves
out over own same shan't she she'd she'll she's should shouldn't so some such than
that that's the their theirs them themselves then there there's these they they'd
they'll they're they've this those through to too under until up very was wasn't we
we'd we'll we're we've were weren't what what's when when's where where's which while
who who's whom why why's will with won't would wouldn't you you'd you'll you're you've
your yours yourself yourselves
also new now get gets getting one two via using used use uses make makes made like
just into across within their out way ways thing things lot lots day days week weeks
month months year years today user users
""".split())

TOKEN_RE = re.compile(r"[a-z][a-z0-9'+-]{2,}")


# ── Note model ───────────────────────────────────────────────────────────────

class Note:
    def __init__(self, path: Path, kind: str):
        self.path = path
        self.kind = kind                      # "briefing" | "summary" | "research"
        self.stem = path.stem                 # Obsidian wikilink target
        raw = path.read_text(encoding="utf-8")
        self.body = strip_frontmatter(raw)
        self.title = extract_title(raw, self.body, self.stem)
        self.products = detect_products(self.body)
        self.tf = Counter(tokenize(self.body))

    def wikilink(self) -> str:
        return f"[[{self.stem}|{self.title}]]"


def strip_frontmatter(raw: str) -> str:
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            raw = raw[end + 4:]
    # Drop any previously inserted Related section so it isn't fed back in.
    return re.sub(
        re.escape(MARK_START) + r".*?" + re.escape(MARK_END),
        "", raw, flags=re.DOTALL,
    )


def extract_title(raw: str, body: str, fallback: str) -> str:
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', raw, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


def tokenize(text: str) -> list[str]:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[*_`#>|\[\]()]", " ", text)
    return [t for t in TOKEN_RE.findall(text.lower())
            if t not in STOPWORDS and not t.isdigit()]


def detect_products(text: str) -> list[str]:
    lower = text.lower()
    return [name for name, kws in PRODUCT_KEYWORDS.items()
            if any(kw in lower for kw in kws)]


# ── Similarity ───────────────────────────────────────────────────────────────

def build_idf(notes: list[Note]) -> dict[str, float]:
    n = len(notes)
    df: Counter = Counter()
    for note in notes:
        df.update(note.tf.keys())
    return {term: math.log((n + 1) / (count + 1)) + 1.0 for term, count in df.items()}


def tfidf_vector(note: Note, idf: dict[str, float]) -> dict[str, float]:
    vec = {t: (1 + math.log(c)) * idf.get(t, 0.0) for t, c in note.tf.items()}
    norm = math.sqrt(sum(w * w for w in vec.values())) or 1.0
    return {t: w / norm for t, w in vec.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    # Iterate over the smaller vector for speed.
    if len(a) > len(b):
        a, b = b, a
    return sum(w * b.get(t, 0.0) for t, w in a.items())


def shared_terms(a: Note, b: Note, idf: dict[str, float], top: int = 3) -> list[str]:
    common = set(a.tf) & set(b.tf)
    ranked = sorted(common, key=lambda t: idf.get(t, 0.0) * min(a.tf[t], b.tf[t]),
                    reverse=True)
    return ranked[:top]


# ── Related section ──────────────────────────────────────────────────────────

def build_related_section(note: Note, ranked: list[tuple[Note, float]],
                          idf: dict[str, float]) -> str:
    lines = [MARK_START, "", "## Related Notes", ""]
    for other, score in ranked:
        bits: list[str] = []
        prods = [p for p in note.products if p in other.products]
        if prods:
            bits.append(", ".join(prods))
        kws = [k for k in shared_terms(note, other, idf) if k.lower() not in
               {p.lower() for p in prods}]
        if kws:
            bits.append(", ".join(kws))
        hint = f" — _{' · '.join(bits)}_" if bits else ""
        lines.append(f"- {other.wikilink()}{hint}")
    lines += ["", MARK_END, ""]
    return "\n".join(lines)


def apply_related(path: Path, section: str, dry_run: bool) -> str:
    raw = path.read_text(encoding="utf-8")
    if MARK_START in raw and MARK_END in raw:
        new = re.sub(
            re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n?",
            section, raw, flags=re.DOTALL,
        )
        status = "updated"
    else:
        new = raw.rstrip() + "\n\n" + section
        status = "linked"
    if not dry_run:
        path.write_text(new, encoding="utf-8")
    return status


# ── Collection ───────────────────────────────────────────────────────────────

def collect_notes(roots: list[tuple[Path, str]]) -> list[Note]:
    notes: list[Note] = []
    for root, kind in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            try:
                notes.append(Note(path, kind))
            except Exception as exc:                       # pragma: no cover
                print(f"  ! skipped {path.name}: {exc}", file=sys.stderr)
    return notes


def resolve_roots(config: dict) -> tuple[list[tuple[Path, str]], bool]:
    """Return (roots, preview). Preview mode runs against the repo itself."""
    vault = config.get("vault_path")
    if vault:
        v = Path(vault)
        roots = [
            (v / config.get("briefings_folder", "AI-UX-News/Daily Briefings"), "briefing"),
            (v / config.get("summaries_folder", "AI-UX-News/Monthly Summaries"), "summary"),
            (v / config.get("research_folder",  "AI-UX-News/Research"),         "research"),
        ]
        return roots, False
    return [(BRIEFINGS_DIR, "briefing")], True


def load_config() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text())
        except Exception:
            pass
    return {}


# ── Main ─────────────────────────────────────────────────────────────────────

def run(dry_run: bool, max_links: int, min_score: float) -> None:
    config = load_config()
    roots, preview = resolve_roots(config)
    if preview:
        dry_run = True
        print("No vault configured — previewing against the repo's briefings.\n")

    notes = collect_notes(roots)
    if len(notes) < 2:
        print(f"Need at least 2 notes to cross-link (found {len(notes)}).")
        return

    idf = build_idf(notes)
    vectors = [tfidf_vector(n, idf) for n in notes]

    if dry_run:
        print("[DRY RUN] no files will be written\n")

    counts = {"linked": 0, "updated": 0, "dry": 0, "none": 0}
    by_kind = Counter(n.kind for n in notes)
    print(f"Scanned {len(notes)} notes "
          f"({', '.join(f'{v} {k}' for k, v in by_kind.items())})\n")

    for i, note in enumerate(notes):
        scored = sorted(
            ((notes[j], cosine(vectors[i], vectors[j]))
             for j in range(len(notes)) if j != i),
            key=lambda t: t[1], reverse=True,
        )
        ranked = [(o, s) for o, s in scored if s >= min_score][:max_links]
        if not ranked:
            counts["none"] += 1
            continue

        section = build_related_section(note, ranked, idf)
        if dry_run:
            counts["dry"] += 1
            print(f"── {note.path.name}  ({note.kind})")
            for other, score in ranked:
                print(f"     → {other.title}  [{score:.2f}]")
        else:
            status = apply_related(note.path, section, dry_run)
            counts[status] += 1
            print(f"  [{status:7s}] {note.path.name}  (+{len(ranked)} links)")

    print(
        f"\n{'─'*48}\n"
        f"  cross-linked : {counts['linked'] + counts['updated'] + counts['dry']}\n"
        f"  no matches   : {counts['none']}"
    )


def main() -> None:
    args = sys.argv[1:]
    dry_run   = "--dry-run" in args
    max_links = 5
    min_score = 0.06
    if "--max-links" in args:
        max_links = int(args[args.index("--max-links") + 1])
    if "--min-score" in args:
        min_score = float(args[args.index("--min-score") + 1])
    run(dry_run=dry_run, max_links=max_links, min_score=min_score)


if __name__ == "__main__":
    main()
