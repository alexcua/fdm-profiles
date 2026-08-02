# Bambu X1C

**Nozzle:** 0.6mm hardened steel  
**Slicer:** OrcaSlicer (primary), Bambu Studio (retained for overhang fan prestart)  
**Notes:** CoreXY enclosed. Lidar-based flow calibration — disable for production. PA handled by firmware. G-code sliced on P1S profile can run on X1C with flow cal and purge line disabled.

---

## Filament Profiles

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | 2026-06-10 |
| 3D Fuel PCTG | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |

---

## Cooling Settings — Polymaker PETG HF

| Setting | Value |
|---|---|
| Fan min | 30% @ 20s |
| Fan max | 100% @ 5s |
| Overhang fan | 100% |
| Overhang threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 2 |
| Exhaust fan | 70% during + after print |

---

## Cooling Settings — 3D Fuel PCTG

| Setting | Value |
|---|---|
| Fan max | 100% @ 5s |
| Overhang threshold | 10–25% |
| Overhang fan | 100% |

---

## Print Profile — Overhang Settings (confirmed Aug 2026)

| Setting | Value |
|---|---|
| Bridge speed (ext + int) | 20mm/s |
| Bridge flow (ext + int) | 0.85 |
| Extra perimeters on overhangs | On |
| Make overhangs printable | Off (modifies geometry) |
| Reverse on even layers | On |
| Overhang speed 10% | 60mm/s |
| Overhang speed 25% | 40mm/s |
| Overhang speed 50% | 12mm/s |
| Overhang speed 75% | 9mm/s |
| Seam | Aligned back |
| Scarf joint | Contour, conditional |
| Staggered inner seams | On |

---

## Notes

- Overhang fan threshold at 95% (old setting) caused major overhang failures — must be 10%.
- PCTG nozzle drool: enable "Wipe before outside wall" and "Avoid crossing perimeters".
- For reducing elbow: scarf off, z-contouring off produces cleanest curved wall results.
- MVS Quality tier 10mm³/s for demanding curved geometry — stock 16mm³/s causes artifacts on elbows.
