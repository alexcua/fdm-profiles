# Prusa MK3.5 — 0.4mm E3D V6 Nozzle

**Machine:** CM03  
**Nozzle:** 0.4mm E3D V6 brass (non-swappable)  
**Slicer:** OrcaSlicer / PrusaSlicer  
**Notes:** Bed slinger. Standard brass nozzle. Cherokee Makerspace only. No calibration data available — using generic profiles until filament is assigned and calibrated.

---

## Filament Profiles

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 260°C ✅ | ⚠ TBD | 9 mm³/s ✅ (ceiling 11.5) | ⚠ TBD (0.98 working) | 0.6mm @ 45mm/s ✅ | 0.03 ✅ | ⚠ Sequence complete; bed + flow TBD, Session 2026-10-16 / 2026-10-17 |

---

## ⚠ Pending

- **3D Fuel PCTG temp tower 280→240°C step 5** (photos reviewed). Session 2026-10-16
  - 240–250: rough, jagged tops on the circle cutouts; numbers soft at 240/245. Slightly too cold.
  - 255–260: cleanest circles and cones, crisp numbers, no strings. Best.
  - 265: one small wisp in the circle. Good, at the hot edge.
  - 270–275: strings off the overhang tips and around the cone. Too hot.
  - 280: strings plus a tan/brown speck (darkened, overheated plastic, or baked-on residue from the nozzle exterior). Too hot.
  - **Proposed 260°C**, the middle of the clean 255–265 range. Slightly below the fleet's usual 265, which is plausible for a 0.4 brass V6 at low flow. Not ported from other machines.
  - ✅ **260°C confirmed by user.** Session 2026-10-16. Vise snap test not run; user accepted 260 on visual result.
  - ⚠ Pending: confirm the tower settings used (recommended: bed 80°C, MVS cap 6 mm³/s, fan 10–30%).
- **MVS test at 260°C, 4→14 mm³/s step 1** (photo reviewed). Sheen dropped and the layers split easily at **7.5mm**, so the ceiling is 4 + 7.5 × 1 = **11.5 mm³/s**. Production = 80% = 9.2, rounded to **9 mm³/s** ✅. Strength-based reading: sheen drop and layer split at the same height. Session 2026-10-16
  - In line with the other 0.4 setups (P1S 0.4 hardened steel ceiling ~9, XL 0.4 ObXidian HF ~10–11). Not ported.
- **PA pattern test, 0→0.08 step 0.005, at 260°C** (photo reviewed). Session 2026-10-17
  - 0–0.01: rounded, blobby tips (too low). No visible over-advance by 0.08 at photo resolution.
  - User's in-hand inspection: tips smooth from **0.03 to 0.05**, nearly identical.
  - **PA 0.03 ✅, chosen by user** (low end of the flat clean range). A flat pattern means PA isn't sensitive here. Not ported.
    > Previously: 0.04 (2026-10-17), the middle of the clean range. Replaced by the user's choice of 0.03 within the same range.
- **Retraction test (0→2.0, step 0.1, @ 45 mm/s), 260°C, PA 0.03** (photo reviewed + user). Session 2026-10-17
  - Towers smooth and even with **no stringing at any height**, including the bottom (user: "super clean"). One string off the final travel, small blob at the base.
  - **0.6mm @ 45 mm/s ✅**: a low value with margin to stop ooze blobs, since strings aren't the issue at any length. Close to the P1S 0.4 (0.6mm). Not ported.
- ⚠ Remaining: bed temp used (80°C if the recommended settings were used), flow ratio not tested (0.98 working value), fan not tuned.
  - Check the nozzle exterior for baked-on residue before the next test.
- Full calibration sequence needed once filament is decided: temp tower → MVS → PA → retraction.
- Do not port values from CHT or Revo configs — E3D V6 has different flow characteristics.
