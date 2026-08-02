# AGENT.md — Instructions for AI Agents

This file tells AI assistants (Claude or otherwise) how to read, update, and maintain this repository correctly. Read this before touching any file in this repo.

---

## Purpose of this repo

Calibration reference for two 3D printing operations:
- **Alexactly** — production printing business using Bambu Lab fleet + Farmloop automation
- **Cherokee Makerspace** — shared-use facility with mixed printer fleet

Profiles cover Bambu Studio, OrcaSlicer, and PrusaSlicer. The goal is minimal profile sprawl with accurate, machine-specific calibration data that can be handed off and reused across sessions.

---

## Repository structure

```
fdm-profiles/
  README.md                  # Human-readable overview
  AGENT.md                   # This file
  CALIBRATION_MASTER.md      # Narrative history, learnings, session log
  filaments/                 # One file per filament — all machines side by side
  machines/                  # One file per machine model — all filaments
```

---

## Critical naming rules — read carefully

| Term | Meaning |
|---|---|
| Polymaker PETG | HF (high flow) formula. Used on X1C, P1S 0.6mm. |
| Polylite PETG | Standard non-HF formula. Used on A1, Makerspace MK3.5s. |
| 3D Fuel PCTG | Primary structural filament for Alexactly production. |

**Polymaker PETG and Polylite PETG are different products.** Past AI sessions have repeatedly confused these. If you are unsure which is meant, ask before writing.

---

## How calibration data is structured

Every confirmed profile entry must include:

- **Machine** (model + nozzle size + nozzle type)
- **Filament** (brand + product name — be specific)
- **Slicer** used for calibration
- **Date** calibrated (approximate is fine)
- **Source** — see provenance rules below
- **Status** — ✅ Confirmed / ⚠ Pending / ❌ Invalid
- **Key values:** Temperature (first layer / other layers), Bed temp, MVS, Flow ratio, Retraction (distance + speed), Pressure Advance, Fan settings

---

## Data provenance — critical

Every entry must carry a source tag. There are exactly two types:

| Tag | Meaning |
|---|---|
| `Session YYYY-MM-DD` | Confirmed in a live calibration session. Physical tests were run (temp tower, MVS tower, PA test, retraction test) and results were observed directly. **Date is the actual chat conversation date — not the date the repo was updated.** |
| `Imported YYYY-MM-DD` | Added from memory summaries, past session notes, or AI recall without verifying against the original live conversation. Values have NOT been confirmed against actual test results. Treat as working hypothesis only. **Date is when the import was written — not when the original calibration happened.** |

**An `Imported` entry must never be treated as production-ready without reconciliation.**

### CRITICAL: How to determine the correct Session date

The date in `Session YYYY-MM-DD` is the date the calibration chat took place — **not today's date, not the date you are writing to the repo.**

**Right:** Prusa XL PCTG was calibrated in a conversation on 2026-07-18 → `Session 2026-07-18`  
**Wrong:** Writing to repo today on 2026-08-02 → `Session 2026-08-02` (this is lying about when the tests happened)

**How to find the correct date:**
1. Claude can search past conversations using `conversation_search` with keywords from the calibration (e.g. "Prusa XL MVS PCTG").
2. The `updated_at` timestamp on the returned chat is the conversation date.
3. Use that date in the source tag.
4. If no past conversation is found, the entry cannot be tagged `Session` — tag it `Imported` with today's date instead.

**Never assume all entries in a repo update share the same date.** Each entry carries the date of its own calibration conversation, which will differ across machines and filaments. A single repo commit may correctly contain `Session 2026-06-17`, `Session 2026-07-19`, and `Session 2026-08-02` in different rows — that is correct behavior, not an error.

### Reconciliation process

To promote an `Imported` entry to `Session`:
1. Search past chat history for the original calibration conversation (Claude has timestamp access via `conversation_search`).
2. Verify each value against the live test results described in that conversation — not the summary, the actual tower/test discussion.
3. Correct any discrepancies (mark old value ❌, add corrected value with explanation).
4. Update the source tag to `Session YYYY-MM-DD` using the actual conversation date from `updated_at`.
5. If the original conversation cannot be found or verified, the entry stays `Imported` until physically recalibrated.

### Why this matters

Memory-imported data carries the same risk as mid-session summaries: values may have been recorded before a calibration step was finalized, or may reflect a starting guess rather than a confirmed result. The Prusa XL MVS error (stored as 9mm³/s, actual 10mm³/s) is a documented example of this failure mode. The provenance tag makes that risk visible rather than hidden. Dating entries to the repo-commit date instead of the calibration date defeats the entire purpose — it makes everything look equally fresh when it is not.

---

## Calibration sequence (OrcaSlicer standard)

1. Temperature tower
2. Max Volumetric Speed (MVS)
3. Pressure Advance (PA)
4. Retraction

**Do not reorder.** Each step depends on the previous being locked.

---

## Rules for updating this repo

### When adding new calibration data
1. Update the relevant `filaments/` doc — add a row or section for the new machine.
2. Update the relevant `machines/` doc — add a row or section for the new filament.
3. Update `CALIBRATION_MASTER.md` — add to the session log and pending items.
4. Do NOT update values in one place without updating the other. Both filament and machine docs must stay in sync.

### When correcting existing values
- Mark the old value as ❌ with a note explaining why it was wrong.
- Add the corrected value with ✅ and the date corrected.
- Do not silently overwrite — the history matters.
- Common error pattern: session summaries written mid-calibration contain incorrect values that get stored as final. Always verify against live test results described in the conversation, not summary notes.

### When data is pending
- Use ⚠ and describe what test still needs to be run.
- Never leave a field blank — use ⚠ TBD so it's clear it's intentionally empty.

---

## Pressure Advance — machine-specific rules

| Machine type | PA handling |
|---|---|
| Bambu X1C, P1S, A1, X2D, H2D, H2C | Firmware handles PA. Leave PA unchecked in OrcaSlicer. Do not store a PA value. |
| Prusa XL, MK3.5 | PA set in slicer. Store confirmed value. |
| Elegoo Giga | PA set in slicer. Store confirmed value. |

---

## MVS architecture

- **Production MVS = 80% of tested ceiling** unless otherwise noted.
- Process profile speeds should be set high (e.g. 200mm/s) so MVS always governs — this is the architectural convention for Giga and Makerspace profiles.
- MVS values are nozzle-size and machine-specific. Never port MVS between different nozzle diameters or different machine types.
- For demanding curved geometry (e.g. reducing elbow), use Quality MVS tier which may be significantly lower than Normal tier.

---

## Fan settings — key gotchas

- Overhang cooling threshold defaults in Bambu Studio/OrcaSlicer are often 95% — this is too late. Production profiles use 10%.
- Bambu H2 with active chamber heating (45°C) uses conservative fan settings intentionally — do not apply standard fan settings to H2.
- Fan prestart (3s) exists in Bambu Studio but not in OrcaSlicer. Account for this when comparing overhang results between slicers.

---

## What NOT to do

- Do not assume calibration values transfer between nozzle sizes.
- Do not assume values transfer between CHT, Revo, HF, and standard brass nozzles even at the same diameter.
- Do not use manufacturer MVS profiles as production values without testing — they are often too high.
- Do not store values from mid-session summaries without verifying against the actual test results described in the conversation.
- Do not conflate Polymaker PETG (HF) with Polylite PETG (standard).

---

## Location vs machine

Profiles are organized by **machine model + nozzle**, not by physical location. The same machine model with the same nozzle should have the same profile whether it's at Alexactly or Cherokee Makerspace. Location is tracked in README.md for inventory purposes only.

---

## Timestamp rules

Every confirmed profile entry must have a date. Format: `YYYY-MM-DD` (e.g. `2026-08-02`). Use the actual chat session date, not today's date. If only month/year is known, use the first of the month as a placeholder and note it as approximate (e.g. `2026-08-01 (approx)`).

### When migrating from a past chat session
- Use the chat session date as the calibration date, not today's date.
- If a value was written without a timestamp, add the session date when migrating.
- If a newer confirmed value already exists in the repo for the same machine/filament/setting, do not overwrite it. Add a note referencing the older session date instead.
- If the repo has a value marked ⚠ and the migrated session has a confirmed ✅ value for the same field, replace it and update the date.

### Conflict resolution
- **Newer confirmed value wins** over older confirmed value.
- **Confirmed value wins** over pending (⚠) regardless of date.
- **Never silently overwrite** — if replacing a value, note the previous value and date in a comment below the table row using the format: `> Previously: [value] ([date]) — replaced because [reason]`

---

## Session log

When migrating data from a past chat session, add an entry to the session log in `CALIBRATION_MASTER.md`:

```
| Date | Session title | Key outcomes |
```

Use the actual conversation timestamp as the date — Claude can retrieve this from chat history. Do not use estimated or approximate dates when the real date is retrievable. Include what machine/filament was calibrated and any important corrections or decisions made.

Entries imported from memory without live chat verification should be noted as `Imported` in the session log row, not as confirmed calibration sessions.
