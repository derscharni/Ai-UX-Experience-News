# OKF Alignment Log

Tracks how our Obsidian/vault frontmatter schema relates to Google's
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
(OKF) as that spec evolves. Newest entries first. Entries below the first are
generated automatically by `scripts/okf_watch.py`, which runs weekly, diffs
the upstream spec against the snapshot in `scripts/okf/`, and asks Claude to
summarize what changed and whether it's worth adopting — informational only,
it never edits code itself.

## 2026-08-24

### `okf/SPEC.md` changed

## OKF SPEC.md — patch notes

**What changed**

- All date-only values (`stale_after`, `last_modified`, `usage_window.from/to`) are now full ISO 8601 datetimes with explicit UTC offset (e.g. `2026-09-23T00:00:00Z`), not bare `YYYY-MM-DD` dates.
- `stale_after` semantics shifted from `today >= stale_after` (date comparison) to `now >= stale_after` (instant comparison).
- A new preamble in §5 explicitly requires every timestamp-valued key to carry an explicit UTC offset.
- `usage_window` values in the worked example updated from date strings to datetimes accordingly.

**Relevance to our schema**

- Our `date` field (kept as `YYYY-MM-DD` for Dataview) is unaffected — it is an Obsidian extension, not an OKF field.
- Our `timestamp` field is already ISO 8601 with offset, so it is compliant.
- Our `## References` citation convention is not touched by this diff; the old/new spec both deprecate `# Citations` identically.

**Recommendation**

No action needed — the change only tightens datetime formatting in OKF fields we do not currently emit, and our existing `timestamp` already satisfies the stricter requirement.

### `okf/README.md` changed

**What changed**

- A new `[!IMPORTANT]` callout at the top announces that OKF has migrated to a dedicated repository: `GoogleCloudPlatform/open-knowledge-format`.
- The copy under `okf/` in the original `knowledge-catalog` repo is now explicitly declared a **frozen snapshot**, no longer maintained.
- The word "repository" in the intro blurb was changed to "directory" — a minor editorial update reflecting the frozen status.
- No changes were made to the OKF specification itself, frontmatter fields, or citation conventions.

**Relevance to our schema**

None of our current frontmatter fields (`type`, `title`, `description`, `resource`, `tags`, `timestamp`, `date`, `month-theme`, `products`, `source`) are affected. The `resource` field pointing to raw GitHub URLs in `knowledge-catalog/okf/` will eventually point at a stale snapshot, but the spec content itself has not changed. Our `## References` citation convention is also untouched.

**Recommendation**

No action needed. This is a housekeeping/relocation announcement with zero spec changes; update the tracked upstream URL in documentation or monitoring scripts to `GoogleCloudPlatform/open-knowledge-format` at your convenience, but nothing in `sync_to_obsidian.py` requires modification today.

## 2026-07-27

### `okf/SPEC.md` changed

## What changed

- OKF bumped from v0.1 to v0.2; `timestamp` is superseded by `generated: { by, at }` and the body `# Citations` list is superseded by a `sources` frontmatter block with per-source credibility signals (`author`, `usage_count`, `last_modified`).
- New optional frontmatter families added: `sources`, `generated`, `verified`, `status`, `stale_after`, plus an actor convention (`human:`, `process:`, `agent/version`).
- A new concept type `Attested Computation` introduced with `runtime`, `parameters`, `executor`, and `attester` fields.
- Per-claim attribution moves from numbered body citations to markdown footnotes keyed to `sources[].id`.

## Relevance to our schema

- Our `timestamp` field maps directly to the now-deprecated `generated.at`; §13.1 explicitly names this as a breaking change.
- Our `## References` body section is structurally analogous to the retired `# Citations` list — both are now superseded by `sources` frontmatter. Our numbering convention differs from OKF's footnote-keyed approach.
- Our other fields (`type`, `title`, `description`, `resource`, `tags`, `date`, `month-theme`, `products`, `source`) are unaffected.

## Recommendation

**Adopt gradually** — the breaking changes touch `timestamp` and citations but OKF is still pre-1.0 with limited adoption signal.

### `okf/README.md` changed

## OKF README Update: v0.1 → v0.2

**What changed**
- Spec version bumped from **v0.1 to v0.2** (link now points to SPEC.md v0.2).
- A new **"Trust, provenance, and freshness"** bullet in Why OKF introduces three new frontmatter fields: `sources` (with credibility signals), `generated`/`verified` (producer/confirmer), and `status`/`stale_after` (currency).
- The "Mixes structured and unstructured data" bullet now lists `generated` and `status` as example queryable frontmatter keys, replacing the previous generic examples `resource` and `tags`.
- A fourth sample bundle, **`bundles/acme_retail/`**, was added to the intro and samples sections.

**Relevance to our schema**
- The new `generated`, `verified`, `status`, and `stale_after` fields don't conflict with our current frontmatter but overlap in intent with our `timestamp` and `date` fields — worth watching.
- Our citation convention (`## References` h2, numbered with full publisher detail) remains unaffected; OKF's `# Citations` h1 style was not changed.

**Recommendation**
No action needed — the README documents intent from SPEC.md v0.2, which we haven't reviewed; defer any schema changes until the spec diff is assessed.

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
