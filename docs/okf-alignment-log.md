# OKF Alignment Log

Tracks how our Obsidian/vault frontmatter schema relates to Google's
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
(OKF) as that spec evolves. Newest entries first. Entries below the first are
generated automatically by `scripts/okf_watch.py`, which runs weekly, diffs
the upstream spec against the snapshot in `scripts/okf/`, and asks Claude to
summarize what changed and whether it's worth adopting — informational only,
it never edits code itself.

## 2026-07-01 — Baseline: adopted OKF v0.1 core fields

Read OKF v0.1 in full and aligned `scripts/sync_to_obsidian.py`'s frontmatter
to it. What we did and what's still open:

**Adopted now** (low risk, clear win):
- `type`, `title`, `description`, `resource`, `tags`, `timestamp` — all six
  OKF v0.1 frontmatter fields are now emitted for both daily briefings and
  monthly summaries. `resource` points at the raw GitHub URL of the source
  markdown file (agent-fetchable without JS, matching OKF's "readable
  without tooling" design goal).
- Our existing richer fields (`date`, `month-theme`, `products`, `source`)
  are kept as-is — OKF explicitly permits and requires consumers to
  preserve unknown extension keys, so nothing was lost by adding OKF's
  fields alongside them.

**Deliberately not adopted yet** (tracked here, revisit as OKF adoption grows):
- **Citations convention** — OKF recommends a `# Citations` (h1) section
  with `[N] [Title](url)` entries. Our briefings already use an equivalent
  `## References` (h2) section with richer `[N] Publisher. (Year).
  *Title*. [url](url)` entries. Functionally aligned, naming/heading-level
  differs. Not renaming yet since our format carries more citation
  metadata (publisher, year) than OKF's convention captures — would be a
  lossy conversion in the wrong direction.
- **`index.md` per directory** — OKF's progressive-disclosure convention
  for bundle navigation. We use `README.md` at the repo root instead. Our
  monthly folders (`briefings/2026-06-.../`) don't have per-folder
  `index.md` files; low priority unless an OKF-aware consumer tool
  actually needs them for traversal.
- **`okf_version: "0.1"` declaration** — OKF lets a bundle declare its
  target spec version in a root `index.md`. Skipped since we don't have a
  root `index.md` yet (see above).

**Recommendation**: treat this as a living baseline. As OKF sees more
real-world adoption (more producers/consumers beyond this Google Cloud
Platform repo), gradually close the two gaps above — starting with an
`index.md` synthesized from `docs/briefings.json`, since that's the
cheapest of the two and immediately useful for any OKF-aware crawler.
