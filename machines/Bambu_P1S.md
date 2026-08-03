# Bambu P1S

**Nozzles:** 0.6mm hardened steel / 0.4mm hardened steel  
**Slicer:** OrcaSlicer (primary), Bambu Studio  
**Notes:** CoreXY enclosed. No Lidar (unlike X1C). PA handled by firmware. G-code from P1S profile can run on X1C.

---

## Filament Profiles — 0.6mm hardened steel

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | 2026-06-10 |
| 3D Fuel PCTG | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |

---

## Filament Profiles — 0.4mm hardened steel

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C / 265°C | 70°C | 8mm³/s | 0.98 | 0.6mm | Firmware | ✅ | 2026-06-10 |

---

## Cooling Settings — Polymaker PETG HF (0.6mm)

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

## Notes

- 0.4mm PCTG: lower MVS ceiling than 0.6mm — bore size is the limiting factor.
- 0.4mm PCTG: retraction increased from stock 0.4mm to 0.6mm to address nozzle booger.
- Silicone sock must be intact — missing or degraded sock causes progressive external nozzle carbonization that accumulates between prints. PCTG contacts bare aluminum heater block, bakes on, and sheds onto next print. PCTG more aggressive than PETG at 265°C. Replace sock if any hardened material is embedded in its surface. ✅ Session 2026-08-02
- If external buildup persists with sock intact: re-seat nozzle at temp to eliminate heat-break gap as secondary accumulation point. ⚠ Session 2026-08-02
- If buildup still persists: try (in order) drop temp to 260°C → retraction to 0.8mm → MVS to 7mm³/s. ⚠ Session 2026-08-02
- PCTG nozzle drool: enable "Wipe before outside wall" and "Avoid crossing perimeters".
- Temp tower for P1S 0.4mm PCTG confirmed 265°C, range tested 240–280°C.
- See Bambu_X1C.md for shared overhang print profile settings.
