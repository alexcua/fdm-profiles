# FDM Profiles — Master Calibration Reference
**Operations:** Alexactly (production) + Cherokee Makerspace  
**Last updated:** 2026-10-30  
**Slicers:** OrcaSlicer (primary), Bambu Studio (retained for some overhangs), PrusaSlicer  
**Calibration sequence (OrcaSlicer):** Temperature → Max Volumetric Speed → Pressure Advance → Retraction

> **Critical naming rule:** Polymaker PETG = HF formula (used on X1C, P1S). Polylite PETG = standard non-HF (used on A1, Makerspace MK3.5s). These are distinct products — do not conflate them.

---

## Fleet Overview

| Machine | Nozzle | Primary Filament | Operation |
|---|---|---|---|
| Bambu X1C | 0.6mm hardened steel | Polymaker PETG HF | Alexactly |
| Bambu P1S | 0.4mm & 0.6mm hardened steel | Polymaker PETG HF (0.6) / 3D Fuel PCTG (0.4) | Alexactly |
| Bambu A1 | 0.6mm | Polylite PETG (standard) | Alexactly |
| Bambu X2D (0.4 profile machine, ID ⚠ TBD) | 0.4mm main nozzle | 3D Fuel PCTG | Alexactly |
| Bambu X2D-3 | Left 0.6 HF / Right 0.6 standard | Polymaker PETG HF / 3D Fuel PCTG (both on left 0.6 HF so far) | Alexactly |
| Bambu H2D | Left 0.6 HF / Right 0.6 HF | 3D Fuel PCTG | Alexactly |
| Bambu H2C | Left 0.6 HF / Right Vortex: 0.4, 0.6, 0.6 HF | Polymaker ASA (left) / 3D Fuel PCTG | Alexactly |

> Nozzle setup per user, 2026-10-29. When logging a test, name the machine, side and nozzle type so results land in the right table (AGENT.md rule).

| Machine | Nozzle | Primary Filament | Operation |
|---|---|---|---|
| Prusa XL | 0.4mm Obxidian HF | 3D Fuel PCTG | Alexactly |
| Prusa MK3.5 (×2, Makerspace) | 0.6mm CHT | Polylite PETG / California Matte PETG | Cherokee |
| Prusa MK3.5 (Alexactly) | 0.6mm CHT | 3D Fuel PCTG | Alexactly |
| Prusa MK3 (Makerspace) | 0.4mm E3D V6 | Generic profiles | Cherokee |
| Elegoo Orangestorm Giga | 0.8mm brass | 3D Fuel PCTG / Polylite PETG / Atomic PLA | Cherokee |


---

## Polymaker PETG HF — Bambu X1C & P1S (0.6mm hardened steel)

**Calibrated:** June 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature (first layer / other layers) | 250°C / 250°C |
| Bed temperature | 70°C |
| Max volumetric speed | 20mm³/s |
| Flow ratio | 0.952 |
| Retraction distance | 1.0mm |
| Pressure advance | Firmware (leave unchecked in OrcaSlicer) |
| Fan min | 30% @ 20s layer time |
| Fan max | 100% @ 5s layer time |
| Overhang fan speed | 100% |
| Overhang fan threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 2 |
| Exhaust fan during print | 70% |

### Notes
- Temp tower range tested: 220–270°C. Sweet spot confirmed at 250°C.
- MVS tested 10–25mm³/s. Caliper check 0.99–1.01mm across full range. No ceiling found below 25mm³/s.
- PA: X1C firmware handles pressure advance. OrcaSlicer PA checkbox must remain unchecked.
- P1S: same hotend/extruder as X1C, settings transfer directly.
- Black Polylite (not this filament) strings worse than white — increase retraction to 1.8–2.0mm for black.
- G-code sliced on P1S profile can run on X1C with flow cal disabled and purge line removed.
- MVS tiers for demanding curved geometry (e.g. reducing elbow): Quality 10mm³/s / Normal 15mm³/s (untested) / Draft 20mm³/s.
- Quality 10 confirmed on reducing elbow — MVS 12 showed artifacts, cliff is sharp between 10 and 12.
- Production MVS of 20mm³/s (from stock profile) confirmed causing artifacts on organic curved geometry — use Quality 10 for such parts.
- Overhang speeds corrected: 10%→0, 25%→50, 50%→15, 75%→10 mm/s (matched from Bambu Studio working profile — Orca defaults 60/40/12/9 were too fast at 25–50% range).


---

## 3D Fuel PCTG — Bambu X1C & P1S (0.6mm hardened steel)

**Calibrated:** June–August 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature (first layer / other layers) | 265°C / 265°C |
| Bed temperature | 70°C |
| Max volumetric speed | 12mm³/s |
| Flow ratio | 0.98 |
| Retraction distance | 1.4mm |
| Retraction speed | 45–50mm/s |
| Pressure advance | Firmware (leave unchecked in OrcaSlicer) |
| Fan max | 100% @ 5s layer time |
| Overhang fan threshold | 10–25% |

### Notes
- Temp tower range tested: 240–280°C. Sweet spot 260–265°C confirmed on P1S.
- MVS tested 10–20mm³/s on X1C. Sheen loss at ~15mm³/s. Production value 12mm³/s (80% of ceiling).
- PCTG is moisture sensitive — dry at 65–70°C for 6–8h before printing. Store in sealed AMS.
- Nozzle booger/drool during travel is a known PCTG behavior. Enable "Wipe before outside wall" and "Avoid crossing perimeters" in print profile.
- Retraction speed 30mm/s was insufficient — caused stringing. 45–50mm/s required.
- Silicone sock on P1S nozzle must be intact — missing sock causes external carbonization buildup.

---

## 3D Fuel PCTG — Bambu P1S (0.4mm hardened steel)

**Calibrated:** August 2026 | **Slicer:** Bambu Studio

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 265°C / 265°C |
| Bed temperature | 80°C |
| MVS | 8mm³/s |
| Flow ratio | 0.98 |
| Retraction distance | 0.6mm |
| Retraction speed | 45mm/s |
| Fan min | 10% @ 30s |
| Fan max | 40% @ 12s |
| Overhang fan | 90% |
| Overhang threshold | 10% |
| Force cooling overhangs | on |
| Pressure advance | Firmware |

### Notes
- Temp tower range 240–280°C. 265°C and 270°C both clean — 265°C chosen as lower of the two clean temps.
- MVS skinny line test: sheen dropped at 5mm height (start 4mm³/s, 1mm³/s increments) = ~9mm³/s ceiling. Production 8mm³/s. Stock profile value 12mm³/s — not adopted, actual calibrated ceiling lower.
- Flow calibration: coarse patches -20 to +20. 0 patch (0.98) cleanest edge to center. Matches X1C flow ratio.
- Retraction tower 0–2mm in 0.1mm increments. Blob at 0.4mm (stock value). Clean from 0.5mm up. Production 0.6mm. Booger fix validation pending on full production plate of siding clips.
- Lower MVS ceiling than 0.6mm nozzle — 0.4mm bore + stainless/hardened steel nozzle is the limiting factor.
- PA firmware-handled. Confirmed via P1S firmware behavior.
- Conservative fan settings (40% max) are correct for PCTG on enclosed machine — do not apply PETG fan settings.


---

## 3D Fuel PCTG — Bambu X2D (0.4mm main nozzle)

**Calibrated:** July 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 265°C |
| Chamber temperature | 40°C |
| MVS | 12mm³/s |
| Flow ratio | 0.98 |
| Pressure advance | Firmware (Bambu Flow Dynamics). Previously 0.06 via OrcaSlicer; superseded 2026-10-21 per user |

### Notes
- Higher MVS ceiling than P1S 0.4mm — attributed to X2D's PMSM servo extruder.
- PA confirmed via manual pattern test, range 0–0.08 in 0.005 steps.
- X2D originally intended for ASA — ASA calibration deferred, needs full sequence when needed.
- X2D AI defect detection may trigger false-positive stops during calibration prints; continue print.
- ASA and PCTG can share machine with separate profiles (different chamber/bed temps).

---

## 3D Fuel PCTG — Bambu H2D/H2C (0.6mm HF nozzle)

**Calibrated:** August 2026 | **Slicer:** OrcaSlicer / Bambu Studio

### Filament Profile (0.6mm nozzle)
| Setting | Value |
|---|---|
| Temperature | 265°C (retest with chamber heat-soaked — initial tower run without active chamber) |
| Chamber temperature | 45°C |
| MVS | 12mm³/s (from 3D Fuel stock profile) |
| Flow ratio | 0.98 |
| Pressure advance | Firmware |

### 3D Fuel Stock Profile Notes (0.4mm nozzle, for reference)
- Temp: 275°C, MVS: 12mm³/s, Chamber: 45°C
- Fan max: 20%, Overhang fan: 50%, Overhang threshold: 95%
- These conservative fan settings are intentional — active chamber heating at 45°C conflicts with aggressive cooling.

### ⚠ Pending
- 0.6mm temp tower must be rerun with chamber fully heat-soaked at 45°C before locking values. **H2D (right extruder) done 2026-10-28:** 250–255 cleanest, 255°C proposed (snap test pending); 260+ stringing, 275–280 bubbling. H2C still 265 ⚠. Session 2026-10-28
- H2 is large format enclosed — chamber heat buildup affects thermal behavior differently than X1C/P1S.


---

## Polymaker PETG HF — Prusa XL (0.4mm Obxidian HF nozzle)

**Calibrated:** June–July 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature (first layer / other layers) | 255°C / 255°C |
| Bed temperature | 80°C |
| MVS | 16mm³/s |
| Flow ratio | 1.0 |
| Retraction distance | 0.8mm |
| Pressure advance | 0.050 |

### Notes
- Temp tower range 250–260°C. 245°C shows bridge droops. Sweet spot 250°C minimum; 255°C used for buffer.
- MVS tested 10–25mm³/s. Ceiling confirmed around 20mm³/s. Production 16mm³/s (80%).
- PA tower confirmed 0.050 at 25mm of 50mm tower height.
- PA must be enabled in OrcaSlicer (grayed out default was 0.02 — incorrect).
- Retraction carried over from PrusaSlicer working value. OrcaSlicer default 0.8mm used.

---

## 3D Fuel PCTG — Prusa XL (0.4mm Obxidian HF nozzle)

**Calibrated:** June–August 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature (first layer / other layers) | 265°C / 270°C |
| Bed temperature | 80°C |
| MVS | 10mm³/s |
| Flow ratio | 0.98 |
| Retraction distance | 1.0mm |
| Pressure advance | 0.062 |
| Layer height | 0.20mm |

### Notes
- Temp tower range 250–260°C. Sweet spot 265°C first layer / 270°C remaining.
- MVS tested 10–25mm³/s. Gloss only in bottom 2mm = ceiling ~10–11mm³/s. Production 10mm³/s.
- PA tower: best at 25mm of 50mm = 0.062. Higher PA value than PETG (0.050) due to PCTG viscosity.
- Retraction speed, fan settings, and print speeds still pending confirmation.
- ⚠ Earlier session summary incorrectly recorded MVS as 9mm³/s and temp as 265/265 — actual values above are corrected from live test data.


---

## Polylite PETG (standard) — Bambu A1 (0.6mm)

**Calibrated:** June 2026 | **Slicer:** Bambu Studio / OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 255°C / 255°C |
| Bed temperature | 70°C |
| MVS (Normal) | 8mm³/s |
| MVS (Quality) | 6mm³/s |
| Flow ratio | 0.95 |
| Retraction distance | 1.5mm |
| Retraction speed | 45mm/s |
| Z-hop | 0.4mm (Normal) |
| Fan min | 30% @ 20s |
| Fan max | 100% @ 5s |
| Overhang fan | 100% |
| Overhang threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 3 |

### Notes
- MVS 8mm³/s showed artifacts on reducing elbow. Use 6mm³/s for Quality tier on demanding geometry.
- A1 is open-frame — close fan first layers set to 3 (vs 2 on P1S) to compensate for faster heat loss.
- Black Polylite PETG strings worse than white — increase retraction to 1.8–2.0mm for black colorway.
- ~50 rolls of Polylite in stock as of mid-2026. Transition to Polymaker PETG HF planned when stock depletes.
- A1 being considered for phase-out — borderline performance, mainly running out Polylite stock.

---

## 3D Fuel PCTG — Prusa MK3.5 (0.6mm CHT nozzle) — Alexactly

**Calibrated:** August 2026 | **Slicer:** OrcaSlicer / PrusaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 260–265°C |
| Flow ratio | 0.98 |
| MVS | 24mm³/s |
| Print speed | 45mm/s |

### Notes
- Temp tower range 240–280°C (first run wet — invalid). Retest with dry filament confirmed 260–265°C sweet spot.
- MVS tested 10–30mm³/s. Glossy all the way to 30mm³/s — ceiling above 30mm³/s. Production 24mm³/s (80% of 30).
- Layer shift and ringing at 20mm height during MVS test caused by bed slinger speed limits, not filament. Does not affect production prints at 45mm/s.
- CHT nozzle does not require higher temp than standard 0.6mm at these flow rates.
- Dry filament before printing — 1 week out of bag caused significant stringing artifacts.
- PA and retraction pending.


---

## Polylite PETG — Prusa MK3.5 ×2 (0.6mm CHT) — Cherokee Makerspace

**Calibrated:** July 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 255°C |
| MVS cliff | ~20mm³/s |
| MVS tiers | Quality 15 / Normal 17 / Draft 19 mm³/s |
| Pressure advance | 0.044–0.05 (cross-validated against Giga result of 0.05) |

### Notes
- CHT and Revo hotends require independent profiles even at same nozzle diameter — never port MVS values between them.
- MVS tiers set with process speeds at 200mm/s so MVS always governs (architectural convention).

---

## California Filament PETG Matte — Prusa MK3.5 (0.6mm CHT) — Cherokee Makerspace

**Calibrated:** July 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 220°C |
| MVS | 10–12mm³/s (cooling-limited, not flow-limited) |
| PA | Pending confirmation |
| Retraction | Pending |

### Notes
- Matte texture is cooling-limited — sheen transition at ~10mm height regardless of flow rate.
- MVS not a meaningful ceiling for this filament — use conservative 10mm³/s.
- Sponsor material for Cherokee Makerspace — showcase/demo use, not load-bearing production.

---

## Elegoo Orangestorm Giga — 0.8mm brass — Cherokee Makerspace

**Calibrated:** July 2026 | **Slicer:** OrcaSlicer 2.4

### 3D Fuel PCTG
| Setting | Value |
|---|---|
| Temperature | 265°C |
| MVS cliff | ~36mm³/s |
| PA | 0.058 |
| Retraction | 0.55mm @ 45mm/s |
| Z-hop | 0 |
| Max fan | 20–30% |
| Quality tier | 0.30mm / 28mm³/s / 117mm/s |
| Normal tier | 0.40mm / 32mm³/s / 100mm/s |
| Draft tier | 0.50mm / 35mm³/s / 88mm/s |

### Polylite PETG (standard)
| Setting | Value |
|---|---|
| Temperature | 245°C |
| MVS cliff | ~23mm³/s |
| PA | 0.05 |
| Retraction | 0.55mm @ 45mm/s |
| Z-hop | 0 |
| Max fan | 50–60% |
| Quality tier | 0.30mm / 18mm³/s / 75mm/s |
| Normal tier | 0.40mm / 20mm³/s / 63mm/s |
| Draft tier | 0.50mm / 22mm³/s / 55mm/s |

### Atomic PLA — ⚠ REQUIRES RECALIBRATION
| Setting | Value |
|---|---|
| Temp tower result | 265°C — FLAGGED AS SUSPECT (too high for PLA) |
| Action required | Full recalibration starting 190–230°C |


### Giga Profile Architecture
- One filament profile per brand/type storing: temp, MVS at Normal tier value, PA, retraction, fan.
- Two shared process profiles (Normal 0.40mm, Draft 0.50mm) with speeds at 200mm/s so MVS always governs.
- Both process profiles: 2 walls, 15% cubic infill, 1.5mm top/bottom fixed (by mm), first layer +0.05mm, 35mm/s.
- Large PETG parts require Nano Polymer adhesive and 75°C bed maintained for full print duration.
- No SD card slot — front USB occupied by camera. All prints sent from OrcaSlicer. Powered USB hub pending.
- PA line test forces all four bed zones to heat (test spawns at bed center).

---

## Polymaker ASA — Bambu H2C (0.6mm HF, left extruder)

**Calibrated:** In progress — Session 2026-10-01 | **Slicer:** Bambu Studio

### Filament Profile
| Setting | Value |
|---|---|
| Temperature (first layer / other layers) | ⚠ TBD / 255°C (stock 260°C) |
| Chamber temperature | 60°C |
| Bed temperature | 100°C |
| MVS (Standard / High Flow) | ⚠ 14 / 20 (white; black unverified) |
| Flow ratio | ⚠ TBD |
| Retraction | ⚠ TBD |
| Pressure advance | Firmware |

### Notes
- Reason for custom profile: heat creep printing black Polymaker ASA on 0.6mm HF with the stock profile.
- ✅ **Resolved 2026-10-28:** the black "Polymaker ASA" spool was mislabeled PolyLite ASA (a different product, per Polymaker). Good black Polymaker ASA at 255 / chamber 60 / bed 100, no adhesive, completed the MVS tower with no jam. ❌ Earlier black results (chamber 45/50/55, NoJam, provisional MVS ~17) are invalid for Polymaker ASA. MVS reading ⚠ TBD. Session 2026-10-28
- Temp tower 230–270°C (white, chamber 60°C): ≤240 too cold (overhang curl, stringing), 250–255 cleanest, 260+ surfaces degrade, 265–270 heavy stringing. 255°C chosen.
- ⚠ Snap test inconclusive: broke at 255 at the mid-tower max-leverage point. Other blocks unbreakable by hand. Controlled vise test pending.
- ⚠ Tower was white. Black heat creep recurred at 255°C / chamber 60°C / bed 100°C / retraction 0.4mm. White was clean at the same conditions. Short retraction rules out retraction as the cause. Chamber 60°C is the lead suspect.
- ❌ Black MVS test (10–30) failed in layer 1. No MVS data. Suspect a leftover clog or preheat heat soak. Filament squashed (softened) at the extruder gear: extruder-zone overheating. Nozzle temp ruled out (white tower completed from 270°C). Colour vs object size/layer-1 dwell not yet separated. Black failed at the layer-1 perimeter → fill transition. White MVS test completed at identical conditions in the same AMS slot, so the failure is black-specific (object size and AMS ruled out). Next black test: chamber 50°C. White MVS ceiling reading pending.

---

## Print Profile — Overhang Settings (X1C / P1S)

These settings resolved overhang curl on curved geometry (confirmed August 2026):

| Setting | Value | Location in OrcaSlicer |
|---|---|---|
| Bridge speed (external & internal) | 20mm/s | Quality → Speed |
| Bridge flow ratio (external & internal) | 0.85 | Quality → Advanced |
| Extra perimeters on overhangs | On | Quality |
| Make overhangs printable | Off for dimensionally critical parts | Quality |
| Reverse on even layers | On | Quality |
| Overhang fan threshold | 10% | Filament → Cooling |
| Fan max | 100% @ 5s | Filament → Cooling |
| Overhang speed 10% | 60mm/s | Quality → Speed |
| Overhang speed 25% | 40mm/s | Quality → Speed |
| Overhang speed 50% | 12mm/s | Quality → Speed |
| Overhang speed 75% | 9mm/s | Quality → Speed |
| Seam position | Aligned back | Quality → Seam |
| Scarf joint seam | Contour (conditional) | Quality → Seam |
| Staggered inner seams | On | Quality → Seam |

### Notes
- "Make overhangs printable" modifies geometry — disable for production parts where dimensional accuracy matters.
- Bambu Studio produces cleaner overhangs due to fan prestart (absent in OrcaSlicer). OrcaSlicer produces better seams.
- For reducing elbow geometry: scarf seam off, z-contouring off produces cleanest results on curved walls.
- Overhang threshold at 95% (old setting) was a major cause of overhang failures — must be 10%.


---

## Key Learnings & Principles

- **MVS governs, process speeds are ceilings.** Set all process speeds high so filament profile MVS is the actual limit.
- **Profile sprawl is a maintenance liability.** One filament profile per material + shared process profiles.
- **Nozzle diameter creates hard MVS walls.** CHT, Revo, HF nozzles, and different bore sizes require independent MVS calibration. Never port values between machines.
- **Calibration summaries written mid-session are unreliable.** Confirm stored values against live test results, not interim notes. (Prusa XL MVS was incorrectly stored as 9mm³/s — actual value 10mm³/s per live test.)
- **Carbon black pigment changes flow behavior.** Black variants need tighter retraction than white/light variants of same filament.
- **PCTG requires aggressive retraction speed.** 30mm/s insufficient — 45–50mm/s required to cut string cleanly.
- **Wet PCTG causes severe stringing** that mimics retraction problems. Always dry before calibration.
- **Manufacturer profiles are often conservative** and tuned for 0.4mm nozzles. Override with your calibrated values.
- **Scarf seam on curved interior surfaces** can cause roughness artifacts. Apply to outer wall only or disable.
- **Overhang fan threshold at 95%** (Bambu Studio default for some profiles) is too late — set to 10%.
- **Chamber temperature (H2) changes entire thermal profile.** Calibration must be run with chamber active.

---

## Pending Calibration Items

| Machine | Filament | Pending |
|---|---|---|
| Bambu A1 | 3D Fuel PCTG 0.6mm | Flow ratio, fan settings |
| Bambu H2D (right) | 3D Fuel PCTG 0.6mm | Tower at chamber 45 done on the right extruder (2026-10-28; left may apply — unverified): 255°C proposed. Next: dry spool, snap test 250/255/260, MVS 10→30, retraction. |
| Bambu H2C (left) | 3D Fuel PCTG 0.6mm | Temp tower rerun with chamber heat-soaked (H2D result may apply — unverified) |
| Prusa MK3.5 (Alexactly) | 3D Fuel PCTG | PA, retraction |
| Prusa MK3.5 CHT (CM01/CM02) | 3D Fuel PCTG | Seam wisps on CM02: dry spool, one retraction test, wipe/seam settings |
| Prusa XL | 3D Fuel PCTG | Retraction speed, fan settings, print speeds |
| MK3.5 Makerspace | California Matte PETG | PA confirmation, retraction |
| Bambu A1 0.4 (Makerspace, ID ⚠ TBD) | California Filament PETG Matte (black) | Temp 225°C (2026-10-28). Next: hand snap 220/225/230, one MVS pass at 225, one retraction test. Bed TBD. |
| Elegoo Giga | Atomic PLA | Full recalibration 190–230°C |
| Elegoo Giga | PCTG + Polylite PETG | Functional part validation |
| Bambu X2D | ASA | Full calibration sequence (deferred) |
| Bambu X2D 0.6 HF | 3D Fuel PCTG | Temp 265°C (Imported 2026-10-29: done earlier, not recorded). Retraction test 0→1.6 at 265 clean throughout (2026-10-28). MVS 2026-10-29: glossy to 30, durable only to 6.5mm (easy to separate at 10), so ceiling 16.5. Tiers (user): Normal 13 / Draft 15. Shared with robotics. Next: set retraction (suggest 0.8 @ 45), real print. PA and flow firmware (auto cal). |
| Bambu X2D-3 left 0.6 HF | Polymaker PETG HF | Temp 250 ✅, bed 70 ✅, MVS Normal 28 / Draft 36 ✅ (0.6 HF). PA and flow firmware. Retraction set to 1.0 mm @ 45 mm/s in the preset (not tested). Next: retraction test on a dried spool to confirm. |
| Bambu X2D-3 right 0.6 standard | Polymaker PETG HF | Starting values only: 250°C / Normal 12 / Draft 16 (untested). Next: MVS 10→30 on the right nozzle. |
| Bambu A1 0.6 | — | First-run validation of start/end G-code blob mods (preset `Bambu Lab A1 0.6 (Nozzle Clear)`; see machines/Bambu_A1.md) |
| Prusa MK3.5 0.4 E3D V6 brass (CM03) | 3D Fuel PCTG | Sequence complete: 260°C / MVS 9 / PA 0.03 / retraction 0.6 @ 45. Bed 80°C ✅. Remaining: flow ratio (0.98 working), fan, real-print validation. |
| Prusa MK3.5 0.6 Revo ObXidian (CM04) | 3D Fuel PCTG | Done to the Makerspace standard: 255°C / MVS 10 / PA 0.025 / retraction 0.6 @ 45. Bed temp + flow TBD. |
| Prusa MK3.5 0.6 Revo brass (CM05) | 3D Fuel PCTG | Starting values from CM04 (255 / MVS 10 / PA 0.025 / ret 0.6, untested). Makerspace standard: temp tower, one MVS pass, one retraction test. |
| Prusa MK3.5 0.6 CHT (CM01) | Polymaker PETG HF | Temp 245°C ✅. Dry spool, then MVS at 245 → PA → retraction |
| Bambu P1S 0.6 | — | First-run validation of start G-code purge-coil/debris mods (`gcode/Bambu_P1S_0.6_start.gcode`, see machines/Bambu_P1S.md) |
| Bambu H2C (0.6 HF left) | Polymaker ASA | Black OK at stock chamber 60, no adhesive (2026-10-28; earlier jams were a mislabeled PolyLite ASA spool). Black temp tower 2026-10-28: 255, same as white. Preset MVS (Standard/HF): 14 / 20, white-based. Next: black MVS 10→30 at 255 / chamber 60 to confirm, vise snap test 250/255/260, black MVS 10→30 at 255, retraction, Stage F real prints. |

---

## Calibration Session Log

| Date | Session | Key Outcomes |
|---|---|---|
| June 10–17, 2026 | Polymaker PETG P1S artifacts | Elbow CAD fix (Loft Thin), OrcaSlicer migration, fleet baseline |
| June 29, 2026 | A1 black Polylite stringing | Retraction 1.5–2.0mm for black colorway |
| June 29, 2026 | P1S nozzle buildup | Silicone sock inspection, start G-code wipe |
| July 12, 2026 | MK3.5 Makerspace | California Matte + Polylite PETG calibration — ⚠ date unverified; no matching conversation found in chat history. Superseded by Aug 2 2026 entry below (per-value live results). |
| July 18, 2026 | Prusa XL correction | MVS and temp values corrected from mid-session summary errors |
| July 19, 2026 | Bambu X2D | 3D Fuel PCTG full calibration |
| July 28, 2026 | Dental adapters (SLA) | DrySHIELD Tough 1500 production settings |
| July 29, 2026 | Farmloop/fswap | G-code post-processing automation |
| August 5, 2026 | Bambu A1 0.6mm — 3D Fuel PCTG full calibration | Temp tower 245–275°C → 265°C (consistent with all other PCTG machines). MVS tested in three passes (5–25, 25–40, 40–55 mm³/s) — clean through 40, hard cliff 40–55. Cliff ~40mm³/s. Tiers: Q 28 / N 32 / D 36 mm³/s. Retraction required four test passes — clean zone confirmed at 3.5–4.0mm, over-retraction above 4.0mm. Confirmed 4.0mm @ 45mm/s. Significantly higher than Polylite PETG on same machine (1.5mm). Flow ratio and fan settings pending. PA firmware. |
| August 2, 2026 | Multi-machine PCTG/PETG | P1S PCTG, H2 PCTG, MK3.5 PCTG, overhang tuning |
| August 2, 2026 | Elegoo Giga — Full calibration PCTG + Polylite PETG + profile architecture | 3D Fuel PCTG full sequence: 265°C/MVS 36mm³/s cliff/PA 0.058/ret 0.55mm. Polylite PETG full sequence: 245°C/MVS 23mm³/s cliff/PA 0.05/ret 0.55mm. Fan correction: 100% max caused stringing, corrected to 60% max. Seam blobbing resolved: scarf contour+hole, staggered inner seams, gap 5%. Functional part validated (400×300mm frame). Profile architecture finalized: 1 filament profile per material, 2 shared process profiles (Normal 0.40mm + Draft 0.50mm), 200mm/s speeds, MVS governs. Atomic PLA temp tower flagged as invalid (265°C suspect) — full recal needed at 190–230°C. |
| August 2, 2026 | Bambu X2D — 3D Fuel PCTG full calibration confirmed | Temp tower 255–275°C → 265°C (270–275°C showed duller surface sheen). MVS 4–14mm³/s in 1mm³/s steps → 12mm³/s; exceptional result — strength held nearly full range, only failed in last ~2mm at 14mm³/s. Single-tier MVS (no Quality/Normal/Draft — range too flat). PA pattern test 0–0.08/0.005 → 0.06. PA field confirmed not exposed in Bambu Studio UI (firmware handles via Flow Dynamics Cal). Real print validation confirmed. Retraction deferred pending further observation. X2D confirmed for PCTG production (siding clips) with occasional ASA deferred. Discussed AMS support material workflow on auxiliary nozzle. |
| August 2, 2026 | P1S 0.4mm PCTG — nozzle carbonization troubleshooting | Inter-print nozzle buildup diagnosed as external carbonization from missing/degraded silicone sock (not mid-print ooze). Root cause: PCTG contacts bare heater block, bakes on, sheds onto next print. Primary fix: inspect/replace sock. Secondary: re-seat nozzle at temp. Tertiary escalation: drop temp to 260°C → retraction to 0.8mm → MVS to 7mm³/s. Notes added to machines/Bambu_P1S.md and filaments/3DFuel_PCTG.md. |
| August 2, 2026 | P1S 0.4mm PCTG — full calibration sequence | Temp tower 240–280°C → 265°C confirmed. Retraction tower 0–2mm → blob at 0.4mm (stock), clean from 0.5mm, production 0.6mm @ 45mm/s. Flow coarse calibration → 0.98 confirmed (matches X1C). MVS skinny line 4–16mm³/s → sheen drops at ~9mm³/s, production 8mm³/s (stock 12 not adopted). PA firmware. Fan: 10%/40% conservative correct for PCTG on enclosed machine. Bed 80°C on textured PEI. Booger fix pending validation on siding clip production plate. |
| August 2, 2026 | Polymaker PETG HF MVS tier correction | MVS 12 tested on P1S — artifacts confirmed. MVS 10 clean. Quality tier = 10mm³/s confirmed. Normal 15 untested. Draft 20 = artifacts on demanding geometry. Overhang speeds corrected from Orca defaults (60/40/12/9) to Bambu-matched values (0/50/15/10). |
| August 2, 2026 | MK3.5 CHT — California Matte + Polylite PETG (parallel dual-machine) | Two MK3.5 0.6 CHT machines run in parallel, one filament each, shared process profiles. **Polylite PETG:** temp tower 240–260°C → 255°C (clean all-sides; 245 stringy — stringing deferred to retraction, not solved by dropping temp). MVS cliff ~20mm³/s, tiers 15/17/19 Q/N/D. PA pattern clean → 0.044 (cross-validated vs Giga 0.05). Retraction still pending. **California Matte PETG:** temp tower 215–230°C → 220°C. MVS cooling-limited (not flow-limited) → conservative 10–12mm³/s; quality good to ~20mm, matte sheen holds to ~10mm before gloss transition from heat soak. PA UNCONFIRMED — pattern failed repeatedly on first-layer adhesion, Z-offset drop did NOT resolve, reprints lifted off bed and never completed. Retraction + finish tuning (fan/min-layer-time) pending. Corrected phantom July 12 entry (no matching conversation in history). Both spools dried + desiccant-stored. |
| October 1, 2026 | Bambu H2C 0.6mm HF — Polymaker ASA temp tower | Custom profile started because of black ASA heat creep on the stock profile (260°C). Temp tower 230–270°C (white) photo-reviewed: 250–255 clean, 260+ degrading, ≤240 overhang curl. 255°C selected. Profile conditions: bed 100°C, chamber 60°C (chamber is lead heat creep suspect). Tower run at 60°C chamber in Bambu Studio. Hand snap test inconclusive (broke at 255, mid-tower leverage point). Black-colorway check pending. Added CLAUDE.md + scripts/check.py pre-commit enforcement of AGENT.md rules. |
| October 6, 2026 | Bambu A1 — start/end G-code nozzle blob fix | Stock start G-code crosses the wiper at ~140°C (M104 without wait), so a hard PETG/PCTG blob bends the wiper and stays on for bed probing. The stock end G-code lets the nozzle ooze during cooldown with no wipe afterwards. Mods: start waits for first-layer temp at X-28.5 before the wiper (non-PLA); end cools with the fan at the purge position to 200°C (PETG/PCTG) or 170°C (PLA), wipes twice, then turns the heater off. Files in `gcode/`. ⚠ Not yet run on a printer. |
| October 6, 2026 | Bambu P1S 0.6 — start G-code purge coil + bed debris | Stock homes Z on the bed edge after one wipe at first-layer temp −20 (PETG/PCTG ooze left at the touch point), and flings the purge coil with a 15000 mm/min move before the PETG/PCTG string has frozen. Mods (non-PLA only): cool to −60 plus a 5s pause before the shake, slow wiper passes and a slow exit, two extra wipes before the Z-home touch. ⚠ Not yet run on a printer. A1 user preset named `Bambu Lab A1 0.6 (Nozzle Clear)`. |
| October 16, 2026 | Prusa MK3.5 CM03 (0.4 E3D V6 brass) — 3D Fuel PCTG temp tower | Tower 280→240 photo-reviewed: 255–265 clean, ≤250 rough circle tops, ≥270 stringing, 280 brown speck. 260°C confirmed by user (snap test not run). Also recorded: CM05 = MK3.5 0.6 Revo brass (Polymaker PETG HF loaded); one MK3.5 has a 0.6 Revo hardened. Corrected PCTG note: not abrasive. |
| October 16, 2026 | Prusa MK3.5 CM04 (0.6 Revo ObXidian) — 3D Fuel PCTG temp tower | Tower 280→240 photo-reviewed: 260 cleanest, ≤245 cold, ≥265 stringing, 275–280 bubbling. User chose 255°C from the part in hand (cleaner bridge, less stringing); my photo read was 260. Strings across the whole range, so check retraction/moisture. CM04 recorded as the ObXidian Revo machine. |
| October 16, 2026 | Prusa MK3.5 CM03 (0.4 E3D V6 brass) — 3D Fuel PCTG MVS | MVS 4→14 step 1 at 260°C: sheen drop and easy layer split at 7.5mm, so the ceiling is 11.5 mm³/s. Production 9 mm³/s (80%). |
| October 17, 2026 | Prusa MK3.5 CM01 (0.6 CHT) — Polymaker PETG HF temp tower | Tower 270→230 (gray) photo-reviewed: 240–250 clean, ≥255 stringing, 265–270 bubbly. 245°C confirmed by user. |
| October 17, 2026 | Prusa MK3.5 CM04 (0.6 Revo ObXidian) — 3D Fuel PCTG MVS | 6→20 step 1 at 255°C: faint sheen change at 5mm, so the ceiling is 11; strength held to 20. Production 9 mm³/s. Same ceiling as CM03's 0.4, consistent with the Revo's short melt zone. |
| October 17, 2026 | Prusa MK3.5 CM03 (0.4 E3D V6 brass) — 3D Fuel PCTG PA | Pattern 0→0.08 at 260°C: 0–0.01 blobby tips, 0.03–0.05 smooth and nearly identical (user, in hand). PA 0.03 (user's choice; 0.04 proposed first). |
| October 17, 2026 | Prusa MK3.5 CM04 (0.6 Revo ObXidian) — 3D Fuel PCTG PA | Pattern 0→0.08 at 255°C: tips rounded below ~0.015, 0.02–0.03 most well formed (user, in hand). PA 0.025. Wisps at tips = stringing, not PA. |
| October 17, 2026 | Prusa MK3.5 CM03 (0.4 E3D V6 brass) — 3D Fuel PCTG retraction | Retraction test 0→2.0 at 260°C: no stringing at any height. 0.6mm @ 45 mm/s. Calibration sequence complete. |
| October 17, 2026 | Prusa MK3.5 CM04 (0.6 Revo ObXidian) — 3D Fuel PCTG retraction | Retraction towers rough with strings, unreadable. Spool differs from CM03 (clean), so moisture is suspected; MVS 9 flagged as possibly low. Dry, clean nozzle, rerun retraction, recheck MVS. |
| October 17, 2026 | Bambu H2C 0.6 HF — Polymaker ASA run A1 (black, chamber 50) | Black at 255 / chamber 50 / bed 100 completed the full MVS tower 10→30, glossy throughout, no heat creep. Only change from the failed run was chamber 60 → 50, so chamber heat is confirmed as the cause. Black MVS ceiling >30 at chamber 50. Middle prongs lifted (adhesion cost). Gear check not possible on the H2C (cutter). Next: A2 at 55. |
| October 17, 2026 | Bambu H2C 0.6 HF — Polymaker ASA run A2 (black, chamber 55) | Filament jam error at chamber 55 (milder than at 60, no wrap around the extruder; white loaded and purged fine afterwards, so 55 is the threshold). Black chamber limit is between 50 and 55. A1 tower ripples on all 3 prongs point to the flow/speed limit near the top, not only to lifting. Next: A3 at 45. |
| October 17, 2026 | Bambu H2C 0.6 HF — Polymaker ASA run A3 (black, chamber 45) | Clean pass, no errors, Nano Polymer Adhesive. Ripple onset at 11mm gives a provisional black MVS of 21, production ~17 (sheen >30). A1 (chamber 50) corrected to marginal: one stall needed a resume. Black working chamber on this H2C is 45. The H2D prints black at 60 with the same HF nozzle type, so an H2C hardware cause (hotend cooling) is suspected. |
| October 17, 2026 | Prusa MK3.5 CM04 (0.6 Revo ObXidian) — PCTG retraction rerun with CM03's spool | Still rough at every height with strings, using the spool that printed clean on CM03. Moisture ruled out; the cause is CM04 hardware. Next: cold pull, inspect the Revo, retraction 0→1.0 step 0.05, recheck MVS. |
| October 18, 2026 | Prusa MK3.5 CM04 — PCTG retraction after drying + cold pulls | Same spool dried 3h (near empty) plus two cold pulls: clean towers. Cause not isolated (moisture and/or partial clog). Retraction 0.6 @ 45, same as CM03. Rerun CM04 MVS. |
| October 18, 2026 | Calibration depth policy | User: Makerspace machines (robotics, older MK3.5s, not production) get a reliable middle ground: temp tower, one MVS pass, one retraction test; PA/flow only if needed. Recorded in AGENT.md and CLAUDE.md. CM04 closed with MVS 10 (user; was 9). |
| October 18, 2026 | MK3.5 CM05 (0.6 Revo brass) — assigned 3D Fuel PCTG | CM05 will run PCTG. Starting values copied from CM04 (ObXidian), untested: 255°C, MVS 10, PA 0.025, retraction 0.6 @ 45. CM03 MVS stays 9 (its 11.5 ceiling was a layer split). |
| October 18, 2026 | Bambu H2C 0.6 HF — Polymaker ASA white MVS | White 10→30 at 255 / chamber 60 / bed 100: clean throughout (user). Ceiling >30, production 24 mm³/s (floor). Black NoJam ~17 provisional. Photo to follow. |
| October 18, 2026 | Prusa MK3.5 CM02 (0.6 CHT) — black PCTG seam wisps | CM02 recorded as the second CHT machine (same as CM01). Seam wisps, a blob line at the seam, speckled walls. Suspect a damp spool plus untuned retraction. Plan: dry, one retraction test, wipe/seam settings. |
| October 19, 2026 | Bambu H2C 0.6 HF — Polymaker ASA white MVS correction | White tower glossy to the top but easier to break above 15mm: strength ceiling 25, production 20 mm³/s (was 24, sheen-only). |
| October 19, 2026 | Bambu H2C — standard 0.6 nozzle trial, Polymaker ASA white | White at 255 / chamber 60 / bed 100, MVS 6→20: unbreakable through 20; on a re-look, a faint sheen change at 8mm (ceiling 14). White production 14 (user's choice; matches Polymaker's 14; ≤70% of the strength limit). Nozzle install confirmed good. Next: black at chamber 60, does it jam? |
| October 19, 2026 | Bambu H2C — standard 0.6 nozzle trial, Polymaker ASA black | Black at 255 / chamber 60 / bed 100 on the standard nozzle: motor-overloaded error, the same feed failure as on HF. Nozzle type ruled out. Remaining: H2C toolhead (cooling/extruder) or spool. Next: H2C's black spool on the H2D at 60; Bambu support with HMS codes. |
| October 20, 2026 | Bambu X2D 0.6 — Polymaker PETG HF temp tower | 270→230 (white) photo-reviewed: 240–250 clean, ≥255 stringing/roughness, 265–270 lumpy. Proposed 245°C (Polymaker 240, X1C/P1S 250). Stringing at every temperature, so address via retraction/drying. ❌ **Invalidated same day:** filament likely 3D Fuel PCTG, and the range was too cold for PCTG. Retest. |
| October 21, 2026 | Bambu X2D-3 (0.6 HF) — Polymaker PETG HF temp tower | 270→230 photo-reviewed: 245–255 cleanest, 230 cold, 260–270 rougher. Strings at every temperature (retraction/moisture). 250°C chosen (matches X1C/P1S 0.6). Machine ID X2D-3 recorded. |
| October 21, 2026 | Bambu X2D-3 (0.6 HF) — Polymaker PETG HF MVS | 10→30 at 250°C clean and strong to the top. Ceiling >30, production 24 mm³/s (floor), above X1C/P1S 20. Next: 28→45 pass, curved-part check. |
| October 21, 2026 | Bambu X2D-3 (0.6 HF) — Polymaker PETG HF MVS second pass | 28→45 glossy and strong throughout. Ceiling >45, production 36 mm³/s (floor), replacing 24. No flow limit found; cooling/curves/motion govern above ~30. |
| October 21, 2026 | Polymaker ASA black — root cause found | The black spool from H2C AMS slot 3 also jammed on the H2D, which prints its own black ASA fine; the spool has a different sheen. Root cause is the spool (batch/formulation/product), not the H2C. All black chamber results (A1–A3, NoJam, standard-nozzle trial) are spool-confounded. Next: good black spool on the H2C at stock chamber 60, no adhesive; check the bad spool's lot number. |
| October 21, 2026 | Bambu X2D — PA policy | User: PA is maintained by Bambu firmware. X2D 0.4 PCTG PA 0.06 (OrcaSlicer) replaced by Firmware, kept as a Previously note. Resolves the AGENT.md conflict. |
| October 26, 2026 | Bambu X2D-3 (0.6 HF) — PETG HF overhang droop vs P1S | Curved walls clean at MVS 28; center overhang droops; the P1S prints the same part fine. Not MVS (same at 12). Filament cooling identical; X2D process has smooth Z outer-wall speed on (off on P1S), outer wall 200 vs 80, accel 5000 vs 3600. Smoothing off improved it. Next: outer wall 80 / accel 3600, then aux fan. |
| October 26, 2026 | Bambu X2D-3 — PETG HF overhang droop, continued | Outer wall 80 / accel 3600 and nozzle 245 gave the same center droop. Full process diff vs P1S shows effectively identical slicing, so the cause is X2D hardware (part-cooling airflow or HF nozzle). Production: painted support or print on the P1S; diagnostic: rotate 90°; aux fan as compensation. **Decision: modify the model** (chamfer/fillet under the ledge center). |
| October 28, 2026 | Bambu H2C — Polymaker ASA black, good spool | The slot-3 spool was mislabeled PolyLite ASA (Polymaker: a different product from Polymaker ASA). Good black Polymaker ASA at 255 / chamber 60 / bed 100, no adhesive: MVS tower completed, no jam. Black chamber = stock 60; NoJam superseded; earlier black results invalid. Naming rule updated in AGENT.md/CLAUDE.md. No PolyLite ASA left in stock. Next: MVS reading, vise snap test, retraction. |
| October 28, 2026 | Bambu A1 0.4 (Makerspace) — California Filament PETG Matte black temp tower | 240→210 photo-reviewed: 225 cleanest (clean cutout, crisp numerals, clean overhang), 220–230 usable, 235–240 droop/blobs, 210–215 strings in cutout. 225°C chosen. Overhang edge curl at all temps (cooling). Snap test suggested. Run while fixing the A1 0.4 nozzle. |
| October 28, 2026 | Bambu H2D 0.6 HF — 3D Fuel PCTG temp tower, chamber 45 | 280→250 photo-reviewed: 250–255 cleanest, 260 light strings, 265–270 long strings, 275–280 bubbly/pitted. 255°C proposed (was 265 from a no-chamber run). Webbing at all temps: dry spool. Next: snap test 250/255/260, MVS. |
| October 28, 2026 | Bambu H2C — Polymaker ASA black temp tower (Stage C) | 270→240 at chamber 60 / bed 100, no adhesive, no jam. Photo-reviewed: 255 cleanest, 250 close, 260–265 mushy numerals, 240–245 webbing. Black 255 = white 255: one temp for both. Next: snap test 250/255/260, black MVS. |
| October 28, 2026 | Bambu X2D-3 0.6 HF — 3D Fuel PCTG retraction test | 0→1.6 mm @ 40 mm/s, white: no strings at any length (user, photo). Can't pick a value; run before the temp tower and nozzle temp unconfirmed, so ⚠. Suggested ~0.8 mm @ 45 mm/s. Next: PCTG temp tower 280→240. |
| October 29, 2026 | Bambu X2D — flow policy | User: the X2D auto-calibrates flow ratio. X2D 0.6 flow = Firmware (auto flow cal) for PETG HF and PCTG; manual flow tests dropped. X2D 0.4 PCTG 0.98 and other machines unchanged. |
| October 29, 2026 | Bambu X2D-3 0.6 HF — 3D Fuel PCTG temp (imported) | User: PCTG temp was done earlier, 265°C; date/range unknown, so Imported. The 10-28 retraction test ran at 265, so it's no longer out of order. Next: MVS 10→30. |
| October 29, 2026 | Bambu X2D-3 0.6 HF — 3D Fuel PCTG MVS | 10→30 at 265: glossy throughout, easy to separate at 10mm, durable only to 6.5mm. Strength ceiling 16.5, production 13 mm³/s (first logged as 20/16, corrected same day). Next: retraction value, real print. |
| October 29, 2026 | Fleet nozzle setup + PETG HF X2D tiers | User: X2D-3 left 0.6 HF / right 0.6 standard; H2D both 0.6 HF; H2C left 0.6 HF, right Vortex 0.4 / 0.6 / 0.6 HF. New rule: every result names machine, side and nozzle type. X2D-3 PETG HF: Normal 28 (0.6 HF) moved into the table; Draft/Quality not set; no chamber for PETG. |
| October 29, 2026 | Bambu X2D-3 0.6 HF — tier decision | Two profiles only: Normal = quality, Draft = speed. 3D Fuel PCTG (0.6 HF): Normal 13 / Draft 15 (user; 91% of the 16.5 strength ceiling). Polymaker PETG HF: Normal 28, Draft TBD (36 suggested). Profiles shared with the robotics team. |
| October 29, 2026 | Bambu X2D-3 — PETG HF Draft + right-nozzle start values | Left 0.6 HF Draft 36 confirmed (user). Bed 70 is the standing value. Right 0.6 standard: conservative start Normal 12 / Draft 16, untested. |
| October 29, 2026 | Bambu X2D-3 — PETG HF retraction set | User set retraction 1.0 mm @ 45 mm/s in the Normal/Draft presets (matches X1C/P1S 0.6 PETG HF; untested on X2D). |
| October 30, 2026 | Bambu H2C left — Polymaker ASA preset MVS | User's current preset: MVS 14 (0.6 standard) / 20 (0.6 HF). Matches the white results (standard 2026-10-19, HF 2026-10-19). Black not yet MVS-tested on a good spool. |
