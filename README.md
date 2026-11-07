# English–Korean Scout Terminology

**Version:** 1.0.1 · **Snapshot:** 7 November 2026
**DOI:** [10.5281/zenodo.24032806](https://doi.org/10.5281/zenodo.24032806) (all versions) · v1.0.0: [10.5281/zenodo.24032807](https://doi.org/10.5281/zenodo.24032807)
**Author:** Jimin Park (박지민), Independent Researcher · ORCID [0009-0000-5227-620X](https://orcid.org/0009-0000-5227-620X)
**Sources:** BP Media Scout Glossary (bpmedia.net/glossary); Korea Scout Association regulations, policy documents, official history and a previously distributed glossary; WOSM and World Scout Bureau publications; Korean press usage

## What this is

A reference glossary of 191 Scouting terms with their English source form, a Korean rendering
and a Korean definition. It covers the elements of the Scout Method, age sections, ranks and
awards, roles and qualifications, WOSM governance bodies and positions, World Scout Bureau
support centres, events and camp operations, international organisations, Korea Scout Association
councils and bodies, laws and documents, uniform items and pioneering skills.

It also records cross-national equivalences: for example, Malaysia's *Pengakap Kanak-kanak*
and Indonesia's *Siaga* are mapped to the Korean Cub Scout section. Such mappings are rarely
documented in one place and are a common source of translation error.

Names of national Scout organisations and faith-based international Scout bodies are deliberately excluded from this release. The regional and special councils of the Korea Scout Association are included, because their English names are fixed by a glossary the Association distributed.

## Why it exists

International Scouting documents use terms whose meaning depends on organisational context.
Literal or machine translation often produces Korean that is grammatical but wrong for Korean
Scouting (for example, rendering a WOSM governance body with an everyday word for "committee").
This glossary provides a reviewed reference for human translators, editors and AI-assisted
translation workflows.

## How it was made

- Terms were collected and defined during editorial work at BP Media, an independent
  Korean-language Scout news service founded and edited by the author.
- No official English–Korean Scout terminology standard has been published by the Korea Scout
  Association. This glossary is an attempt to establish one as a reference.
- Where Korean usage is documented, the rendering follows that usage and the source is recorded.
  Primary usage sources are Korea Scout Association regulations: 지도자 규정 (2022), 포상규정
  (amended 2025), 진보과정 규정 (2015), 제복장구 규정 (2020) and Youth Hero상 운영규정 (2023).
  A Scout glossary previously distributed by the Korea Scout Association (supplied by the compiler) is also used. These regulations govern qualifications, awards, advancement and uniform; they are not a
  terminology standard, but they fix the official Korean names they use.
- Otherwise the compiler chose the rendering (`verify_status = editorial_choice`). The reasoning is
  recorded in `rationale_ko`. The compiler applies these criteria, in order:
  1. A name fixed by a Korean law, KSA regulation, policy or the KSA official history.
  2. The form most commonly used inside Korean Scouting and in KSA press releases or Korean press.
  3. Consistency with related entries (e.g. 세계사무국 / 세계사무국 본부 / 지역사무처 / 지역 사무처장;
     이사회 → 의장·부의장; 총회 → 결의).
  4. Where Korean Scouting uses the English name as is, the English name is kept (see below).
  5. Only where none of the above applies, a new rendering that keeps the meaning of the English term.
  A rendering chosen under criterion 2 reflects the compiler's knowledge of current practice and should
  be checked against new documents as they appear.
- Where Korean Scouting uses an English name as is, `term_ko` repeats the English name.
- Each definition was written and reviewed by the compiler.

## Limitations

- Known overlaps: Contingent and Delegation are both 대표단, and Head of Contingent and Head of
  Delegation are both 대표단장; the context distinguishes them.

- **This is a proposed reference, not an official Korea Scout Association or WOSM standard.**
  If an official body later publishes different terminology, the official source prevails and
  this glossary will record the difference in a new version.
- `source_status`: `cited` = the definition is linked to a published source; `not_required` = a general
  definition with no specific factual claim; `compiler` = based on the compiler's knowledge of Korean
  Scouting practice, with no published source yet.
- National programmes change. Age ranges and rank names are valid as of `bp_updated_at`.
- Korean definitions only. English definitions are planned for a later version.

## Columns (`terms.csv`, UTF-8 with BOM)

| Column | Meaning |
|---|---|
| `term_id` | Permanent dataset identifier (SKT-0001…). Assigned once and never reused or renumbered; new terms get the next free number. Numbers in this first release follow English alphabetical order; later additions take the next free number, and a removed term leaves its number unused |
| `bp_id` | Row identifier in the BP Media glossary database, used for synchronisation only. Gaps are expected |
| `term_en` | Source term (English, or the original language for national terms) |
| `term_en_variant` | Alternative or former English name, and abbreviations (e.g. WOSM, WSB); several values are separated by `; ` |
| `term_ko` | Korean rendering |
| `term_ko_variant` | Alternative or legacy Korean name, or an abbreviation used in Korean |
| `type` | method · section · rank · award · role · training · governance · event · organization · initiative · observance · document · uniform-symbol · skill |
| `scope` | `international`, or ISO country code(s) where the term is national |
| `equivalent_ksa_term` | Corresponding Korea Scout Association section or rank, for national terms |
| `term_fr` | French form, where recorded |
| `definition_ko` | Korean definition |
| `source` | Cited source, where recorded |
| `source_status` | `cited` · `not_required` (general definition) · `compiler` (compiler's knowledge of practice) |
| `bp_updated_at` | Last update of the entry in the source database (UTC) |
| `verify_status` | verified · partly_verified · corrected · edited · generic_definition (no specific factual claim) · editorial_choice (rendering chosen by the compiler, usually the most common usage in Korean Scouting; see `rationale_ko`) |
| `verify_note` | What was checked or changed (Korean) |
| `verify_source` | URL of the source used for verification |
| `rationale_ko` | Why this Korean rendering was chosen, for editorial choices (Korean) |

## Using this glossary with AI translation

Language models do not consult this glossary on their own. Supply it explicitly, for example:

> Translate the following Scouting text from English to Korean. Use the attached glossary
> (`terms.csv`) as binding terminology: when a source term matches `term_en` or `term_en_variant`, use `term_ko`.
> For national terms, keep the original name and add `equivalent_ksa_term` in parentheses on
> first use. Flag any Scouting term not in the glossary instead of inventing a rendering.

## Licence

Proposed: CC BY 4.0, subject to confirming that no definition reproduces third-party text verbatim.

## Maintaining this dataset

Rules for editors and AI assistants are in [AGENTS.md](AGENTS.md); the history of naming and
scope decisions is in [docs/DECISIONS.md](docs/DECISIONS.md). Run `python3 tools/validate.py`
(Python 3, standard library only) before every commit. `term_id` values are permanent from v1.0.0.

## How to cite

Park, J. (2026). *English–Korean Scout Terminology* (Version 1.0.1) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.XXXXXXX
