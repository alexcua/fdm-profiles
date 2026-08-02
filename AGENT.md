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
- **Status** — ✅ Confirmed / ⚠ Pending / ❌ Invalid
- **Key values:** Temperature (first layer / other layers), Bed temp, MVS, Flow ratio, Retraction (distance + speed), Pressure Advance, Fan settings

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

## Session log

When migrating data from a past chat session, add an entry to the session log in `CALIBRATION_MASTER.md`:

```
| Date | Session title | Key outcomes |
```

Include the approximate date, what machine/filament was calibrated, and any important corrections or decisions made.
