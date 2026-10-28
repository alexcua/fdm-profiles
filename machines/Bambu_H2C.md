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
| Polymaker ASA | 255°C (stock 260°C) | 60°C | 100°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | Firmware | ⚠ In progress (temp 255 white + black; black OK at chamber 60) | Session 2026-10-01 / 2026-10-28 |

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
- **Standard 0.6 nozzle trial (2026-10-19):** white ASA at chamber 60: faint sheen change at 8mm (ceiling 14, so ~11), unbreakable through 20 (≥16). **White production 14** (user). Revisit if black is lower. Black on standard at chamber 60: ❌ motor overloaded (feed failure). Nozzle type ruled out. Suspect the H2C toolhead (cooling/extruder) or the spool. Next: H2C black spool on the H2D; Bambu support.
- **2026-10-21: the black jams were the spool** (AMS slot 3), not the H2C. It also jammed on the H2D, which prints its own black ASA fine, and it has a different sheen from the other spools. H2C hardware suspicion withdrawn; black chamber results above are spool-confounded. ⚠ Confirm with a good black spool at chamber 60, no adhesive.
  > Previously: H2C toolhead (cooling/extruder) suspected (2026-10-17/19).
- **2026-10-28: the slot-3 spool was mislabeled PolyLite ASA.** Good black **Polymaker ASA** spool, nozzle 255 / chamber 60 / bed 100, no adhesive, MVS tower 10→30 (recommended settings, assumed): **completed, no jam** (user). Nozzle: left 0.6 HF (user). MVS ceiling reading ⚠ TBD. Session 2026-10-28
  - ❌ Black chamber 45 working point, provisional black MVS ~17 and the NoJam preset came from the PolyLite spool. Invalid for Polymaker ASA. **Black chamber = stock 60, no adhesive.**
- **Black temp tower 270→240 (Stage C), 2026-10-28** (photo reviewed; black Polymaker ASA, chamber 60 / bed 100, no adhesive: recommended settings, assumed). Completed with no jam. 270 glossy but soft numerals, fine strings in the cutout; 265–260 mushy/blobby numerals, wisps; **255 cleanest** (crisp numerals, clean cutout and overhang); 250 crisp, a few strings in the cutout; 245–240 webbing in the cutout, rougher numerals. Curved overhang edge similar at all temps. **Black = 255°C, same as white**, so one temp for both colours. ⚠ Snap test 250/255/260 still pending (white and black towers now both on hand). Session 2026-10-28
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
- Polymaker ASA (left 0.6mm HF): black runs at chamber 60 (2026-10-28). Black temp 255 ✅ by tower (2026-10-28). Next: vise snap test 250/255/260, black MVS 10→30 at 255 (earlier tower not on hand), then retraction (PA firmware), then Stage F real prints. Follow `protocols/Polymaker_ASA_H2C_unified.md`.
  > Previously: "Isolate the black heat creep cause" (resolved 2026-10-28: mislabeled PolyLite ASA spool).
