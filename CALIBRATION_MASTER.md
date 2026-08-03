# FDM Profiles — Master Calibration Reference
**Operations:** Alexactly (production) + Cherokee Makerspace  
**Last updated:** 2026-08-02  
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
| Bambu X2D | 0.4mm main nozzle | 3D Fuel PCTG | Alexactly |
| Bambu H2D/H2C | 0.4mm & 0.6mm | 3D Fuel PCTG | Alexactly |
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
- MVS tiers for demanding curved geometry (e.g. reducing elbow): Quality 10mm³/s / Normal 15mm³/s / Draft 20mm³/s.


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

**Calibrated:** June 2026 | **Slicer:** OrcaSlicer

### Filament Profile
| Setting | Value |
|---|---|
| Temperature | 265°C / 265°C |
| MVS | 8mm³/s |
| Flow ratio | 0.98 |
| Retraction distance | 0.6mm |
| Pressure advance | Firmware |

### Notes
- Lower MVS ceiling than 0.6mm nozzle — 0.4mm bore is the limiting factor, not the hotend.
- Retraction increased from stock 0.4mm to 0.6mm to address nozzle booger issue.


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
| Pressure advance | 0.06 (apply in OrcaSlicer; PA field not exposed in Bambu Studio) |

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
- 0.6mm temp tower must be rerun with chamber fully heat-soaked at 45°C before locking values.
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
| Bambu H2D/H2C | 3D Fuel PCTG 0.6mm | Temp tower rerun with chamber heat-soaked |
| Prusa MK3.5 (Alexactly) | 3D Fuel PCTG | PA, retraction |
| Prusa XL | 3D Fuel PCTG | Retraction speed, fan settings, print speeds |
| MK3.5 Makerspace | California Matte PETG | PA confirmation, retraction |
| Elegoo Giga | Atomic PLA | Full recalibration 190–230°C |
| Elegoo Giga | PCTG + Polylite PETG | Functional part validation |
| Bambu X2D | ASA | Full calibration sequence (deferred) |

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
| August 2, 2026 | Multi-machine PCTG/PETG | P1S PCTG, H2 PCTG, MK3.5 PCTG, overhang tuning |
| August 2, 2026 | Elegoo Giga — Full calibration PCTG + Polylite PETG + profile architecture | 3D Fuel PCTG full sequence: 265°C/MVS 36mm³/s cliff/PA 0.058/ret 0.55mm. Polylite PETG full sequence: 245°C/MVS 23mm³/s cliff/PA 0.05/ret 0.55mm. Fan correction: 100% max caused stringing, corrected to 60% max. Seam blobbing resolved: scarf contour+hole, staggered inner seams, gap 5%. Functional part validated (400×300mm frame). Profile architecture finalized: 1 filament profile per material, 2 shared process profiles (Normal 0.40mm + Draft 0.50mm), 200mm/s speeds, MVS governs. Atomic PLA temp tower flagged as invalid (265°C suspect) — full recal needed at 190–230°C. |
| August 2, 2026 | Bambu X2D — 3D Fuel PCTG full calibration confirmed | Temp tower 255–275°C → 265°C (270–275°C showed duller surface sheen). MVS 4–14mm³/s in 1mm³/s steps → 12mm³/s; exceptional result — strength held nearly full range, only failed in last ~2mm at 14mm³/s. Single-tier MVS (no Quality/Normal/Draft — range too flat). PA pattern test 0–0.08/0.005 → 0.06. PA field confirmed not exposed in Bambu Studio UI (firmware handles via Flow Dynamics Cal). Real print validation confirmed. Retraction deferred pending further observation. X2D confirmed for PCTG production (siding clips) with occasional ASA deferred. Discussed AMS support material workflow on auxiliary nozzle. |
| August 2, 2026 | MK3.5 CHT — California Matte + Polylite PETG (parallel dual-machine) | Two MK3.5 0.6 CHT machines run in parallel, one filament each, shared process profiles. **Polylite PETG:** temp tower 240–260°C → 255°C (clean all-sides; 245 stringy — stringing deferred to retraction, not solved by dropping temp). MVS cliff ~20mm³/s, tiers 15/17/19 Q/N/D. PA pattern clean → 0.044 (cross-validated vs Giga 0.05). Retraction still pending. **California Matte PETG:** temp tower 215–230°C → 220°C. MVS cooling-limited (not flow-limited) → conservative 10–12mm³/s; quality good to ~20mm, matte sheen holds to ~10mm before gloss transition from heat soak. PA UNCONFIRMED — pattern failed repeatedly on first-layer adhesion, Z-offset drop did NOT resolve, reprints lifted off bed and never completed. Retraction + finish tuning (fan/min-layer-time) pending. Corrected phantom July 12 entry (no matching conversation in history). Both spools dried + desiccant-stored. |
