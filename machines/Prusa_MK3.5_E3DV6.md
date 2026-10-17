# Prusa MK3.5 — 0.4mm E3D V6 Nozzle

**Machine:** CM03  
**Nozzle:** 0.4mm E3D V6 brass (non-swappable)  
**Slicer:** OrcaSlicer / PrusaSlicer  
**Notes:** Bed slinger. Standard brass nozzle. Cherokee Makerspace only. No calibration data available — using generic profiles until filament is assigned and calibrated.

---

## Filament Profiles

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | ⚠ 260°C proposed (snap test + confirm pending) | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ In progress, Session 2026-10-16 |

---

## ⚠ Pending

- **3D Fuel PCTG temp tower 280→240°C step 5** (photos reviewed). Session 2026-10-16
  - 240–250: rough, jagged tops on the circle cutouts; numbers soft at 240/245. Slightly too cold.
  - 255–260: cleanest circles and cones, crisp numbers, no strings. Best.
  - 265: one small wisp in the circle. Good, at the hot edge.
  - 270–275: strings off the overhang tips and around the cone. Too hot.
  - 280: strings plus a tan/brown speck (darkened, overheated plastic, or baked-on residue from the nozzle exterior). Too hot.
  - **Proposed 260°C**, the middle of the clean 255–265 range. Slightly below the fleet's usual 265, which is plausible for a 0.4 brass V6 at low flow. Not ported from other machines.
  - ⚠ Pending: vise snap test of 255/260/265 (use 265 if it's clearly stronger), user confirmation of the pick, and confirmation of the tower settings used (recommended: bed 80°C, MVS cap 6 mm³/s, fan 10–30%).
  - Check the nozzle exterior for baked-on residue before the next test.
- Full calibration sequence needed once filament is decided: temp tower → MVS → PA → retraction.
- Do not port values from CHT or Revo configs — E3D V6 has different flow characteristics.
