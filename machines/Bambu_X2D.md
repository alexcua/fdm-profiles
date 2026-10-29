# Bambu X2D

**Machines:** includes **X2D-3** (0.6 HF main).  
**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** PMSM servo extruder — higher MVS than expected vs prior-gen toolheads. PA field not exposed in Bambu Studio; apply only in OrcaSlicer. Originally intended for ASA — currently running PCTG on 0.4mm and Polymaker PETG HF on 0.6mm.

---

## Filament Profiles — 0.4mm main nozzle

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C | 40°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ✅ | Session 2026-08-02 |

> Previously: PA 0.06 (OrcaSlicer manual pattern test, Session 2026-08-02). Replaced 2026-10-21 by Firmware (Bambu Flow Dynamics), per user and AGENT.md.
| ASA | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Deferred | — |

---

## Filament Profiles — 0.6mm main nozzle (High Flow)

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 250°C ✅ | ⚠ TBD | 70°C ✅ | 36 mm³/s ✅ (floor; glossy + strong to 45) | Firmware (auto flow cal) | ⚠ TBD | Firmware | ⚠ In progress (temp + MVS ✅) | Session 2026-10-21 |
| 3D Fuel PCTG | 265°C | 40°C (assumed) | 70°C (assumed) | 13 mm³/s ✅ (strength ceiling 16.5) | Firmware (auto flow cal) | ⚠ No stringing 0–1.6 mm (test 2026-10-28 at 265°C) | Firmware | ⚠ In progress (temp + MVS done; retraction value + real print TBD) | Imported 2026-10-29 / Session 2026-10-29 |

---

## Notes

- ~~PA = 0.06 confirmed via manual pattern test, range 0–0.08 in 0.005 steps.~~ Superseded 2026-10-21: PA is firmware-handled on the X2D (user). 0.06 kept here as history only.
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
  - **Curved/overhang part check (oval ring with overhanging ledge), 2026-10-26:**
    - MVS 28 with the overhang settings (threshold 10%, overhang fan 100%, overhang speeds 0/50/15/10, bridge 20 @ 0.85): curved walls clean; **center of the overhang droops** (symmetric). The P1S prints this part fine without support, so it's not the geometry. Session 2026-10-26
    - Quality preset (inherited MVS 12, about the P1S's 10): nearly identical droop, so MVS alone isn't the cause.
    - Preset comparison: filament cooling is identical to the P1S (fan 30–100, overhang 100 @ 10%, exhaust 70, chamber 0, aux 0, prestart 3s). The process presets differ: X2D has **smooth Z outer-wall speed ON** (P1S off), outer wall 200 vs 80 mm/s, outer-wall accel 5000 vs 3600. X2D `slow_down_min_speed` 20 vs P1S 10.
    - **Smoothing OFF → better, but the P1S is still better** (user).
    - Outer wall 80 + accel 3600 (MVS 28, smoothing off): **nearly the same** center droop (4-print comparison photo).
    - **Nozzle 245°C** (one change): **same droop.** Temp stays 250.
    - Full process diff P1S vs X2D: remaining differences are only prime tower, counterbore bridging and travel angle, so **slicing is effectively identical**. Cause is most likely **hardware**: X2D toolhead part-cooling airflow, or the HF nozzle vs the P1S's standard HS nozzle.
    - Options: rotate the part 90° (airflow diagnostic); aux fan 50% in a part-specific preset; painted support under the center; or print this part on the P1S. Session 2026-10-26
    - **Decision (user, 2026-10-26): modify the model** (e.g. a ≤45° chamfer or fillet under the center of the ledge) so it prints without support on the X2D. Profile unchanged: 250°C / bed 70 / Normal MVS 28; process keeps smoothing off and outer wall 80.
- **0.6 main nozzle is HF (High Flow)** (user, 2026-10-20). Select High Flow in the X2D printer preset. Values from standard nozzles don't transfer.
- **0.6 plan (user, 2026-10-20): full profiles for both Polymaker PETG HF and 3D Fuel PCTG.** Order: **Polymaker PETG HF first**, then PCTG. One filament at a time; label every test piece with the filament (after the 2026-10-20 mix-up); dry both spools first.
  - PCTG: tower 280→240 (bed 70, chamber 40, MVS cap 10) → MVS 10→30 → retraction 0→2.0 (extend to 3.0) → real print. PA and flow: firmware.
  - PETG HF: tower 270→230 (bed 70, fan 30–100%) → MVS 10→30 → Quality-tier check on curved parts → retraction. PA and flow: firmware.
  - **Flow ratio: Bambu auto flow calibration** (user, 2026-10-29), like PA. No manual flow test on the X2D 0.6. Applies to the X2D only; other machines unchanged unless the user says so.
    > Previously: manual flow test planned, start 0.952 (2026-10-20); replaced because the X2D auto-calibrates flow.
  - **X2D-3 0.6 HF, 3D Fuel PCTG retraction test 0→1.6 mm step 0.1 @ 40 mm/s, 2026-10-28** (photo reviewed; white): **clean at every length, no strings** (user). The test can't pick a value: even 0 mm didn't string. Run at 265°C (assumed; the PCTG temp was already done, user). Suggested production retraction ~0.8 mm @ 45 mm/s (mid-range margin; not measured). Session 2026-10-28
    > Previously: flagged out of order with temp TBD (2026-10-28); corrected 2026-10-29 because the temp had been done but not recorded.
  - **3D Fuel PCTG temp on X2D-3 0.6 HF: 265°C** (user, 2026-10-29: temp tower done earlier, not previously recorded; date and tower range unknown). Imported 2026-10-29
  - **X2D-3 0.6 HF, 3D Fuel PCTG MVS 10→30 at 265°C, 2026-10-29** (photo reviewed; white; bed 70 / chamber 40, step 1 mm³/s per mm: recommended settings, assumed): glossy all the way up, no sheen change or ripples, but **easy to separate at 10mm** (user). Strength ceiling 10 + 10 = **20 mm³/s**, so **production 16 mm³/s** (80%). Strength, not sheen, sets the limit; the photo can't show layer adhesion. Above X2D 0.4 PCTG (12). Session 2026-10-29
  > Previously: ceiling 20 / production 16 (2026-10-29, from 'easy to separate at 10mm'); replaced the same day because the user found it **durable only to 6.5mm**: ceiling 10 + 6.5 = 16.5, production 13 mm³/s (80%, rounded down). Session 2026-10-29
  - PA handling resolved (user, 2026-10-21): **firmware** for all X2D nozzles, per AGENT.md. The 0.4 PCTG's 0.06 is now a Previously note.
- ASA calibration deferred — needs full sequence (temp tower → MVS → PA → retraction) when needed.
- PCTG and ASA can share machine with separate profiles (different chamber/bed temps).
- AI defect detection may trigger false-positive stops during calibration — continue print.
- Auxiliary nozzle: AMS connected via single 6-pin daisy-chain port. Nozzle assignment in Bambu Studio software. Intended for support material (Bambu Support for PA/PET compatible with PCTG).

---

## ⚠ Pending

- Retraction distance and speed for PCTG
- ASA full calibration sequence
