# Bambu X2D

**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** PMSM servo extruder — higher MVS than expected vs prior-gen toolheads. PA field not exposed in Bambu Studio; apply only in OrcaSlicer. Originally intended for ASA — currently running PCTG on 0.4mm and Polymaker PETG HF on 0.6mm.

---

## Filament Profiles — 0.4mm main nozzle

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C | 40°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | 0.06 | ✅ | Session 2026-08-02 |
| ASA | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Deferred | — |

---

## Filament Profiles — 0.6mm main nozzle

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | ⚠ TBD (start 240°C, Polymaker) | ⚠ TBD | ⚠ TBD (start 70°C) | ⚠ 12 mm³/s starting value (Polymaker X2D preset, untested) | ⚠ TBD (start 0.952) | ⚠ TBD | Firmware | ⚠ Starting values only; testing started | Imported 2026-10-19 |

---

## Notes

- PA = 0.06 confirmed via manual pattern test, range 0–0.08 in 0.005 steps.
- PA field not in Bambu Studio UI — apply when setting up OrcaSlicer profile only.
- Higher MVS than P1S 0.4mm (12 vs 8mm³/s) attributed to PMSM servo extruder.
- MVS test (Aug 2026): range 4–14mm³/s in 1mm³/s steps. Structural strength held across full range — only failed in last ~2mm at 14mm³/s. Exceptional result vs P1S 0.4mm ceiling of 8mm³/s.
- Single-tier MVS profile (no Quality/Normal/Draft split). Differences across range too small to justify profile sprawl. 12mm³/s used as single production value.
- Real print validation confirmed Aug 2026 — profile quality described as "really good."
- Retraction pending real-world print test (deferred after initial validation print).
- Polymaker PETG HF 0.6 starting values from Polymaker's X2D preset for this filament (Polymaker preset repo, updated 2026-08-14): 240°C, MVS 12 (same for all nozzle variants), flow 0.95, bed 70. It inherits Bambu's **0.4** nozzle preset, so it isn't 0.6-specific. X1C/P1S 0.6 reference (Imported): 250°C, MVS 20, Quality tier 10 for curved geometry. Full sequence (production machine): temp tower 270→230, MVS 10→30 step 1 (note sheen and break point), Quality-tier check on curved parts. Testing started 2026-10-19.
- ASA calibration deferred — needs full sequence (temp tower → MVS → PA → retraction) when needed.
- PCTG and ASA can share machine with separate profiles (different chamber/bed temps).
- AI defect detection may trigger false-positive stops during calibration — continue print.
- Auxiliary nozzle: AMS connected via single 6-pin daisy-chain port. Nozzle assignment in Bambu Studio software. Intended for support material (Bambu Support for PA/PET compatible with PCTG).

---

## ⚠ Pending

- Retraction distance and speed for PCTG
- ASA full calibration sequence
