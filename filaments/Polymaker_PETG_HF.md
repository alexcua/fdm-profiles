# Polymaker PETG HF — All Machines

**Primary use:** Alexactly production parts (X1C, P1S 0.6mm)  
**Material notes:** HF = high flow formula. Different product from Polylite PETG — do not conflate. Flow ratio 0.952 is Polymaker's factory-calibrated value, confirmed accurate via caliper check.

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Bambu X1C | 0.6mm HS | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | Imported 2026-06-10 |
| Bambu P1S | 0.6mm HS | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | Imported 2026-06-10 |
| Bambu X2D (X2D-3) | 0.6mm HF (left) | 250°C ✅ | 70°C | 0.6 HF: Normal 28 ✅ / Draft ⚠ TBD / Quality ⚠ TBD (ceiling >45) | Firmware (auto flow cal) | ⚠ TBD | Firmware | ⚠ In progress (temp + MVS ✅) | Session 2026-10-21 |
| Prusa MK3.5 (CM01) | 0.6mm CHT | 245°C ✅ | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ In progress | Session 2026-10-17 |
| Prusa XL | 0.4mm OBX HF | 255°C / 255°C | 80°C | 16mm³/s | 1.0 | 0.8mm | 0.050 | ✅ | Imported 2026-06-10 |

---

## Consistency Notes

- **Temperature:** X1C/P1S confirmed 250°C. XL needs 255°C minimum — 245°C shows bridge droops.
- **Flow ratio:** 0.952 on Bambu (Polymaker factory value, confirmed). 1.0 on XL. X2D: Bambu auto flow calibration (user, 2026-10-29).
  > Previously: X2D-3 row showed 0.952 (Polymaker preset starting value, untested on X2D); replaced because the X2D auto-calibrates flow.
- **MVS:** X1C/P1S ceiling above 25mm³/s. XL ceiling ~20mm³/s at 0.4mm nozzle. Do not port.
- **PA:** Bambu machines firmware only. XL slicer value 0.050 confirmed.

---

## Per-Machine Detail

### Bambu X1C / P1S — 0.6mm hardened steel
- Temp tower tested 220–270°C. Sweet spot confirmed 250°C.
- MVS tested 10–25mm³/s. Caliper check 0.99–1.01mm across full range — no ceiling found.
- Production MVS 20mm³/s is conservative — actual ceiling likely higher.
- PA firmware-handled. OrcaSlicer PA checkbox must remain unchecked.
- Fan min 30% @ 20s, max 100% @ 5s, overhang 100% @ 10% threshold, prestart 3s.
- MVS tiers for demanding curved geometry: Quality 10 / Normal 15 (untested) / Draft 20 mm³/s. Quality 10 confirmed on reducing elbow. MVS 12 showed artifacts. Normal 15 pending test on simple geometry.
- Production MVS 20mm³/s (Draft tier) confirmed causing artifacts on demanding geometry — use Quality 10 for curved/organic production parts.
- Overhang speeds (corrected from Bambu Studio reference profile): 10% → 0mm/s, 25% → 50mm/s, 50% → 15mm/s, 75% → 10mm/s. Previous Orca defaults (60/40/12/9) were too fast at 25–50% range.
- G-code sliced on P1S profile can run on X1C with flow cal disabled and purge line removed.

### Bambu X2D — 0.6mm HF main
- ❌ Temp tower 270→230 (2026-10-20) **invalid**: filament likely PCTG, not PETG HF. Retest planned.
  > Previously: logged as PETG HF with 245°C proposed.
- **X2D-3 tower 270→230 (2026-10-21):** 245–255 cleanest; strings at every temperature (retraction/moisture). **250°C ✅** (user). Dry before MVS. Session 2026-10-21
- MVS 10→30 at 250°C: clean and strong to the top. Ceiling >30, production 24 mm³/s (floor). Next: 28→45 pass, curved-part Quality-tier check. Session 2026-10-21
- **Tiers (X2D-3 left 0.6 HF, 2026-10-29):** Normal 28 (production value per the 2026-10-26 notes); Draft and Quality not set. 36 is the 80% floor of the >45 ceiling, not a tier.
  > Previously: table showed 36 mm³/s (floor) as the single MVS.
- Second pass 28→45: glossy and strong throughout. Ceiling >45, production 36 mm³/s (floor). Practical cap ~30 suggested; Quality tier from curved-part check pending. Session 2026-10-21
  > Previously: 24 mm³/s floor from the first pass.

### Prusa MK3.5 (CM01) — 0.6mm CHT
- Temp tower 270→230°C (gray): 240–250 clean, ≤235 drooping bridges, ≥255 stringing, 265–270 bubbly. **245°C confirmed by user.** Dry before MVS. Session 2026-10-17

### Prusa XL — 0.4mm Obxidian HF
- Temp tower range 250–260°C. 245°C fails on bridges. 255°C provides safe buffer.
- MVS ceiling ~20mm³/s. Production 16mm³/s.
- PA tower confirmed 0.050 at midpoint of tower.
- Retraction carried over from PrusaSlicer working value — no stringing observed.

---

## Fan Settings (X1C / P1S)

| Setting | Value |
|---|---|
| Fan min | 30% @ 20s layer time |
| Fan max | 100% @ 5s layer time |
| Overhang fan | 100% |
| Overhang threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 2 |
| Exhaust fan during print | 70% |
