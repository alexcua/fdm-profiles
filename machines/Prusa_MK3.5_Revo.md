# Prusa MK3.5 — 0.6mm E3D Revo (Swappable)

**Nozzle:** E3D Revo swappable system — available sizes: 0.4mm, 0.6mm, 0.8mm  
**Slicer:** OrcaSlicer / PrusaSlicer  
**Machines (Cherokee Makerspace ×2):** **CM05** has the 0.6 **brass** Revo nozzle; **CM04** has the 0.6 **ObXidian** Revo nozzle (E3D's coated hardened nozzle). Recorded 2026-10-16.  
**Notes:** Bed slinger. Brass and hardened are different nozzle types: separate calibrations, values don't transfer between them. Revo nozzle swaps tool-free. Each nozzle size requires independent calibration — do not port MVS between sizes. Do not port from CHT config even at same 0.6mm diameter.

---

## Filament Profiles — 0.4mm Revo

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Filament Profiles — 0.6mm Revo brass

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Filament Profiles — 0.6mm Revo ObXidian (CM04)

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 255°C ✅ | ⚠ TBD | 9 mm³/s ✅ (sheen ceiling 11) | ⚠ TBD | ⚠ TBD | 0.025 ✅ | ⚠ In progress (temp + MVS + PA ✅), Session 2026-10-16 / 2026-10-17 |

- **Temp tower 280→240°C step 5** (photos reviewed). Session 2026-10-16
  - 240–245: rough, beaded lines under the ledges; drooping layers at the top of the circle at 240; strings in the circle at 245. Too cold.
  - 250–255: better; one long string off the 255 overhang tip. Good, at the cold edge.
  - 260: clean overhang, crisp numerals, clean circle and cone. Best.
  - 265–270: strings in the circle, getting worse.
  - 275–280: lumpy, bubbly texture inside the window, drooping bridges, heavy strings. Too hot.
  - ✅ **255°C chosen by user** from the part in hand: cleaner bridge and less stringing than 260. Session 2026-10-16
    > Previously: 260°C proposed from photo review (2026-10-16). Replaced because the user's in-hand inspection showed 255 cleaner. The single long string off the 255 tip is likely from a travel move, not temperature.
  - Strings across the whole range, not just the hot end, point to retraction or moisture: dry the spool before MVS.
  - Filament: 3D Fuel PCTG, assumed from the 240–280 tower range; user didn't correct it.
  - ⚠ Pending: tower settings used (bed temp).
- **MVS at 255°C, 6→20 mm³/s step 1** (recommended settings, confirmed by user). Session 2026-10-17
  - Sheen change at **5mm**, faint but confirmed by user, so the ceiling is 6 + 5 × 1 = **11 mm³/s**. Strength held all the way to the top (≥20).
  - Production = 80% of the sheen ceiling, 8.8, rounded to **9 mm³/s** ✅.
  - Untested option: a strength-based Draft tier (≥16, i.e. 80% of ≥20) if finish doesn't matter. Needs an 18→30 pass to find the real strength limit.
  - Ceiling is about the same as CM03's 0.4 V6 (11.5) despite the larger 0.6 nozzle. Consistent with the Revo's short melt zone limiting flow. Not ported.
- **PA pattern test, 0→0.08 step 0.005, at 255°C** (photo reviewed). Session 2026-10-17
  - 0 to ~0.015: rounded, bulging tips (too low). No visible over-advance through 0.08 at photo resolution.
  - User's in-hand inspection: **0.02–0.03** most well formed.
  - **PA 0.025 ✅**, the middle of that range. Slightly below CM03 (0.03), as expected for the larger nozzle. Not ported.
  - Small wisps at several tips: stringing (matches the temp tower), not PA. Dry the spool and clean nozzle buildup before the retraction test. The booger on the left of the pattern was nozzle buildup, ignored.
  - Next: retraction.
- **Retraction test (0→2.0, step 0.1, @ 45 mm/s), 255°C, PA 0.025** (photo reviewed). ❌ Not readable. Session 2026-10-17
  - Both towers rough and bumpy, worse toward the top; hairy strings mid–upper; lower section cleanest.
  - CM04's spool is **different from CM03's** (CM03 printed clean at every retraction). CM04 strung on every test, so **moisture is the lead suspect**.
  - ⚠ **CM04 results may be moisture-affected:** MVS 9 (sheen ceiling 11) may be low, since moisture lowers the flow limit; the "Revo short melt zone" explanation is unconfirmed. Temp 255 and PA 0.025 are probably sound.
  - Plan: dry the spool (65–70°C, 6–8h), clean the nozzle, rerun retraction 0→2.0. If stringing clears, rerun MVS 6→20 to check whether the ceiling rises.

---

## Filament Profiles — 0.8mm Revo

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## ⚠ Pending

- All nozzle sizes and filament combinations need full calibration.
- CM04 (0.6 ObXidian): 3D Fuel PCTG temp 255°C ✅ (2026-10-16). CM05 (0.6 brass): Polymaker PETG HF loaded, not yet calibrated.
- Calibrate in this priority order based on usage frequency.
- Each nozzle size is a separate calibration — values do not transfer between sizes.
