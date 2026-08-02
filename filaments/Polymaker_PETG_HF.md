# Polymaker PETG HF — All Machines

**Primary use:** Alexactly production parts (X1C, P1S 0.6mm)  
**Material notes:** HF = high flow formula. Different product from Polylite PETG — do not conflate. Flow ratio 0.952 is Polymaker's factory-calibrated value, confirmed accurate via caliper check.

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Bambu X1C | 0.6mm HS | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | 2026-06-10 |
| Bambu P1S | 0.6mm HS | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | 2026-06-10 |
| Prusa XL | 0.4mm OBX HF | 255°C / 255°C | 80°C | 16mm³/s | 1.0 | 0.8mm | 0.050 | ✅ | 2026-06-10 |

---

## Consistency Notes

- **Temperature:** X1C/P1S confirmed 250°C. XL needs 255°C minimum — 245°C shows bridge droops.
- **Flow ratio:** 0.952 on Bambu (Polymaker factory value, confirmed). 1.0 on XL.
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
- MVS tiers for demanding curved geometry: Quality 10 / Normal 15 / Draft 20 mm³/s.
- G-code sliced on P1S profile can run on X1C with flow cal disabled and purge line removed.

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
