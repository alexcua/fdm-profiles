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
- Snap test inconclusive: broke at 255, but at the max-leverage point (mid-tower). Other blocks unbreakable by hand. Controlled vise test pending. Black colorway not yet tower-tested. See filaments/Polymaker_ASA.md.
- Run A1 2026-10-17: black at chamber 50 (else 255/100) completed the MVS tower 10→30, glossy throughout, no heat creep. Chamber heat confirmed as the cause. Prongs lifted (adhesion cost of the cooler chamber). Next: A2 at chamber 55.
- Run A2 2026-10-17: black at chamber 55 tripped the filament jam error (milder than at 60; extruder recovered, white loaded and purged fine, so 55 is at the threshold). Black limit between 50 and 55. Next: A3 at chamber 45 (protocol margin rule).
- A1 corrected: chamber 50 had one stall needing a resume, so it's marginal.
- Run A3 2026-10-17: black at chamber 45 (Nano Polymer Adhesive) clean pass. **Black working chamber 45°C** for now. Provisional black MVS: ripple ceiling 21, so production ~17 mm³/s (⚠ until Stage C/D).
- White (stock preset, chamber 60): MVS glossy to 30 but easier to break above 15mm, so strength ceiling 25 and **production 20 mm³/s**.
  > Previously: 24 mm³/s (2026-10-18), sheen-only. Corrected 2026-10-19. Black (NoJam, chamber 45): ~17 provisional.
- Bambu Studio user filament preset for these settings (chamber 45, nozzle 255, bed 100, softening 85): **NoJam** (named 2026-10-17). Use with Nano Polymer Adhesive.
- ⚠ The H2D prints black ASA at chamber 60 (same HF nozzle type) without issues, which points to an H2C-specific cause. Check the left hotend fan and heatsink; swap spools H2D↔H2C.
- **Standard 0.6 nozzle trial (2026-10-19):** white ASA at chamber 60: faint sheen change at 8mm (ceiling 14, so ~11), unbreakable through 20 (≥16). Production choice pending. Black test pending: does it jam at chamber 60 on a standard nozzle? Values don't transfer between HF and standard.
- Purpose: black ASA heat creep on this nozzle with the stock profile. Causes not yet isolated. Chamber 60°C is the lead suspect. Recurred on black at 255/60/100 with 0.4mm retraction (rules out long retraction). White clean at same conditions. Black MVS test failed in layer 1. ❌ No MVS data. Feed/hotend diagnosis pending. Filament squashed (softened) at the extruder gear, so the extruder zone is overheating. Nozzle temp ruled out (white tower completed starting at 270°C). Colour vs object size not yet separated. Next: white MVS at the same conditions. Black failed at the layer-1 perimeter → fill transition (when extrusion force rose). White MVS test completed at identical conditions in the same AMS slot, so the failure is black-specific. Next black test: chamber 50°C. White MVS ceiling reading pending. Session 2026-10-01

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
- Polymaker ASA (left 0.6mm HF): controlled (vise) snap test 250/255/260, temp check on black, then MVS → retraction (PA firmware). Isolate the black heat creep cause. Follow `protocols/Polymaker_ASA_H2C_unified.md` (aim: one profile for white and black).
