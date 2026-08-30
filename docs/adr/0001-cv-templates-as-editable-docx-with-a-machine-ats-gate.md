---
status: accepted
revisit-after: 2026-11-30
---

# CV templates are editable `.docx` behind a machine ATS gate, and the store's premise is two parallel epics

**Date:** 2026-08-30 · **Session:** onboarding interview · **Supersedes:** the
Notion PRD threshold on *Etsy digital CVs — European / industry niches*.

## Context

`docs/initial_plan.md` describes this store as "similar process as the
qhoto_printshop": research a niche, generate, review, mock up, list, publish a
draft. It never names what the buyer downloads.

The owner's own catalogued research says the analogy breaks at exactly that
point. A CV template's value is layout, typography and machine-parseability
delivered as an **editable** artifact. No diffusion model produces one, so the
generation stage does not transfer from the print shop; what transfers is the
harness — state machine, scheduled stages, Telegram approval, dry-run
discipline.

The market numbers behind the premise exist and are the owner's, from a July
2026 research pass: ~125K monthly Etsy searches for resume templates, rising,
at $5–20; niche-specific templates see ~40% less competition at ~20% higher
prices; "ATS-optimized" messaging converts ~35% better. Country conventions are
documented and real — DE/AT/CH expect a photo'd tabular Lebenslauf, FR a
stricter one-page form with `Formation` / `Expérience professionnelle`,
Southern Europe photos, the Nordics none — and private-sector EU employers
prefer a locally-formatted CV over generic Europass. Competitors sell either
one generic Europass layout or a single country. **None of those figures
carries a source URL.**

Three documents claimed to be the source of truth: `docs/initial_plan.md`, a
Notion PRD, and the tracker. `CLAUDE.md` already settles it — the issue wins.

## Decision

**D-1 — The sold artifact is an editable `.docx`.** The format itself is a
research question (what comparable digital-download shops actually ship; the
owner's prior is that text-based templates sell as `.docx` the way financial
dashboards sell as `.xlsx`), but `.docx` is the working assumption every other
decision here is built on. A change of format reopens this ADR.

**D-2 — The ATS gate is two-tier, and the tiers are not equivalent.** Primary:
an open-source resume parser. Backup: `python-docx` text extraction. Extraction
proves the fields survive; it does **not** prove a real applicant tracking
system reads them in the right order. Whichever tier ran is named in the
sortie's acceptance criteria, because a green backup tier is weaker evidence
than a green primary one and the record must not blur them.

**D-3 — Editability is checked by persona injection, not by opening the file.**
A fixed set of test personas is generated once and injected into every
template; a template that shatters when values change fails. This is what
catches the failure text extraction cannot see — text boxes, nested tables,
manual line breaks.

**D-4 — Taste is reserved for "does it look nice to a human".** Same class of
judgement as image generation in `qhoto_printshop`, and it is not scriptable.
Everything else on a CV — fields survive, personas inject, sections present —
is machine-gated. A gate that is neither class is not a gate.

**D-5 — Every quantitative claim carries a source URL and a retrieval date.**
The July figures above do not, which is why they appear here as provenance
rather than as findings. Research output that restates a number without a
source does not land.

**D-6 — The kill threshold is €175/month revenue.** It covers €5/day of Etsy
advertising (~€150), roughly one month of Claude subscription, and mockup
generation calls. At $5–20 a template that is roughly 12–35 sales a month.
Below it, counting setup and generation cost, the store stops. **The margin
above cost is thin by construction** — advertising alone is ~86% of the floor —
so the price-point research is what makes this reachable, not the volume.

**D-7 — Reuse from `qhoto_printshop` is copy-on-demand.** A component is copied
when a sortie needs it, not ported up front. Extraction into a shared substrate
is deferred until the overlap proves large enough to be worth it; the current
read is that the architectures rhyme but few parts transfer verbatim.

**D-8 — The epic supersedes the Notion PRD.** The Notion note's "nothing gets
built until the PRD is signed" predates qops in this project. There is no PRD
in this repo and none is owed.

**D-9 — Two root epics, run in parallel.** Market-and-mechanics research is
slow and gated on owner review; proving one CV trio end to end is near-fully
autonomous until its final taste gate. Neither blocks the other. This
contradicts `docs/initial_plan.md`, which orders all research before any
generation, and the contradiction is deliberate.

**D-10 — Publishing stops at the Etsy draft.** Recorded as a constraint, not a
decision: see `docs/constraints/etsy-ai-disclosure.md`.

## Consequences

**`docs/initial_plan.md` is demoted to provenance.** It stays as the record of
what was originally imagined. Where it disagrees with this ADR — on ordering
(D-9), on what transfers from the print shop (D-7), on the artifact (D-1) —
this ADR wins, and the tracker wins over both.

**Five of the plan's review gates are not gates.** The plan places owner review
after nearly every stage, described as flow control rather than as a pass/fail.
D-4 keeps exactly one class of those — taste on appearance — and D-2, D-3 and
D-5 replace the rest with checks. Owner control over sequencing survives as the
`gate:taste` label on an epic, which is where sequencing belongs.

**Font licensing is unresolved and blocks no sortie yet.** A `.docx` sold
commercially depends on fonts the buyer may not have and that may not be
licensed for the use. The owner's prior is to use generally-available fonts
licensed for commercial use. It is a research item in the research epic, not a
constraint record, because nothing about it has been established.

**If the ATS parser choice turns out to be theatre, D-2 is what gets amended.**
The named parser defines what "passes ATS" means in this repo. That is a real
risk of the two-tier design and the reason the tier is recorded per sortie.
