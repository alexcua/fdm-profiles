# Bambu H2C

**Extruders:** Left 0.6mm HF (same as H2D) / Right Vortex inductive (machine-changeable)  
**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** Large format enclosed. Active chamber heating at 45°C. Left extruder profile identical to H2D. Right extruder Vortex nozzle sizes TBD — 0.25mm being considered for removal.

---

## Left Extruder — 0.6mm HF

Same profile as H2D. See Bambu_H2D.md.

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | ⚠ 265°C (retest needed) | 45°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ |

### Polymaker ASA — H2C-specific (not yet run on H2D)

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker ASA | 255°C (stock 260°C) | 60°C | 100°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | Firmware | ⚠ In progress (temp done) | Session 2026-10-01 |

- Temp tower 230–270°C (white, chamber 60°C, Bambu Studio): 250–255 clean, 260+ surfaces degrade and stringing increases, ≤245 overhang curl. 255°C chosen. Session 2026-10-01
- Snap test pending. Black colorway not yet tower-tested. See filaments/Polymaker_ASA.md.
- Purpose: black ASA heat creep on this nozzle with the stock profile. Causes not yet isolated. Chamber 60°C is the lead suspect.

---

## Right Extruder — Vortex Inductive (machine-changeable)

| Nozzle | Filament | Temp | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| 0.4mm | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |
| 0.6mm | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |
| 0.6mm HF | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

Note: 0.25mm being considered for removal. Larger sizes TBD.

---

## ⚠ Pending

- Same as H2D: temp rerun with chamber heat-soaked.
- Right extruder Vortex nozzle sizes to be decided before calibration.
- All right extruder profiles starting fresh.
- Polymaker ASA (left 0.6mm HF): snap test 250/255/260, temp check on black, then MVS → retraction (PA firmware). Isolate the black heat creep cause.
