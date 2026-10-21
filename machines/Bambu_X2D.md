# Bambu X2D

**Machines:** includes **X2D-3** (0.6 HF main).  
**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** PMSM servo extruder — higher MVS than expected vs prior-gen toolheads. PA field not exposed in Bambu Studio; apply only in OrcaSlicer. Originally intended for ASA — currently running PCTG on 0.4mm and Polymaker PETG HF on 0.6mm.

---

## Filament Profiles — 0.4mm main nozzle

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C | 40°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | 0.06 | ✅ | Session 2026-08-02 |
| ASA | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Deferred | — |

---

## Filament Profiles — 0.6mm main nozzle (High Flow)

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 250°C ✅ | ⚠ TBD | ⚠ TBD (start 70°C) | 36 mm³/s ✅ (floor; glossy + strong to 45) | ⚠ TBD (start 0.952) | ⚠ TBD | Firmware | ⚠ In progress (temp + MVS ✅) | Session 2026-10-21 |
| 3D Fuel PCTG | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated (planned) | — |

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
- ❌ **INVALID: temp tower 270→230 step 5, white** (photos reviewed), 2026-10-20. Filament uncertain: likely 3D Fuel PCTG, not PETG HF, and the 230–270 range is too cold for PCTG. Retest planned. Notes below kept for reference only.
  > Previously: logged as the PETG HF tower with 245°C proposed (2026-10-20).
  - 230–235: soft, fuzzy numerals, wisps in the circles. A bit cold.
  - 240–250: crisper numerals, fairly clean circles (light wisps), clean overhangs. Cleanest range.
  - 255–260: strings across the window under the ledges, more wisps, overhang edges roughening.
  - 265–270: heavy strings, booger at 270, lumpy/wrinkled overhang edges. Too hot.
  - ~~Proposed 245°C~~ (void: tower invalid).
  - Stringing at every temperature, so it's a retraction or moisture issue, not temperature. Handle at the retraction step; dry the spool if it's been out.
- **X2D-3 Polymaker PETG HF temp tower 270→230 (0.6 HF), 2026-10-21** (photo reviewed): 230 fuzzy/cold; 235–240 OK; **245–255 crispest numerals, cleanest overhang edges**; 260–270 softer and rougher, heavier wisps. Strings across the windows at every temperature → retraction/moisture, not temp. **250°C ✅** (user). Matches X1C/P1S 0.6 (250). Session 2026-10-21
  - **MVS 10→30 step 1 at 250°C** (recommended settings, assumed): clean and strong all the way up (user). Ceiling >30, so **production 24 mm³/s ✅ (a floor)**, above X1C/P1S 20. Session 2026-10-21
  - **Second pass 28→45 step 1** (photo reviewed): glossy and strong all the way up (user). Ceiling **>45**, so **production 36 mm³/s ✅ (80% floor, repo convention)**. Session 2026-10-21
    > Previously: 24 mm³/s (2026-10-21), floor from the 10→30 pass. Replaced by the higher floor from the second pass.
  - No flow limit found. Above ~30, cooling, curved surfaces and motion limits govern quality more than flow. Suggested practical cap ~30 for general parts; set the Quality tier from a curved-part check (X1C/P1S curves needed 10). ⚠ Pending.
  - Next: curved-part Quality-tier check, then retraction → flow. **PA: firmware (Bambu Flow Dynamics)**, per user 2026-10-21; no PA test.
- **0.6 main nozzle is HF (High Flow)** (user, 2026-10-20). Select High Flow in the X2D printer preset. Values from standard nozzles don't transfer.
- **0.6 plan (user, 2026-10-20): full profiles for both Polymaker PETG HF and 3D Fuel PCTG.** Order: **Polymaker PETG HF first**, then PCTG. One filament at a time; label every test piece with the filament (after the 2026-10-20 mix-up); dry both spools first.
  - PCTG: tower 280→240 (bed 70, chamber 40, MVS cap 10) → MVS 10→30 → retraction 0→2.0 (extend to 3.0) → flow → real print. PA: firmware.
  - PETG HF: tower 270→230 (bed 70, fan 30–100%) → MVS 10→30 → Quality-tier check on curved parts → retraction → flow (start 0.952). PA: firmware.
  - PA handling resolved for the 0.6 (user, 2026-10-21): **firmware**, per AGENT.md. ⚠ Still open: what to do with the 0.4 PCTG's stored OrcaSlicer PA 0.06.
- ASA calibration deferred — needs full sequence (temp tower → MVS → PA → retraction) when needed.
- PCTG and ASA can share machine with separate profiles (different chamber/bed temps).
- AI defect detection may trigger false-positive stops during calibration — continue print.
- Auxiliary nozzle: AMS connected via single 6-pin daisy-chain port. Nozzle assignment in Bambu Studio software. Intended for support material (Bambu Support for PA/PET compatible with PCTG).

---

## ⚠ Pending

- Retraction distance and speed for PCTG
- ASA full calibration sequence
