# Etsy's AI-tools disclosure cannot be set through the API

**Kind:** external fact, not ours to decide · **Recorded:** 2026-08-30 ·
**Re-checked:** quarterly, by a scheduled task that predates this repo

## The fact

Etsy asks "which tools did you use?" on a listing. As of this record the answer
cannot be supplied through the Etsy API. It is set by hand in the Etsy
dashboard.

This has been validated multiple times in `qhoto_printshop`, and a quarterly
re-check already exists there to catch the day the API allows it.

## What it forces

**The pipeline stops at the draft.** An automated run publishes an Etsy
*draft*; the owner ticks the AI-tools field and moves the listing to live.
Identical to the `qhoto_printshop` setup — not a new manual step invented for
this project, the same one, for the same reason.

This is a ceiling on automation imposed from outside. It is not a taste gate
and it does not substitute for one: the owner's judgement on whether a template
looks good (ADR-0001, D-4) happens before the draft exists.

## When this record dies

The quarterly re-check reports the API accepting the field. At that point the
draft-only stop becomes a choice rather than a constraint, and it moves into an
ADR or disappears.
