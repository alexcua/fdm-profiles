# Prusa XL (5-head)

**Head configuration:**
- Heads 1 & 2: 0.4mm Obxidian HF
- Heads 3 & 4: 0.4mm stock brass
- Head 5: 0.4mm HF

**Slicer:** OrcaSlicer / PrusaSlicer  
**Notes:** CoreXY. Direct drive per head. PA set in slicer (not firmware). Each head independent — calibrate per nozzle type, not per head number.

---

## Filament Profiles — 0.4mm Obxidian HF (Heads 1, 2, 5)

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 255°C / 255°C | 80°C | 16mm³/s | 1.0 | 0.8mm | 0.050 | ✅ | Jun 2026 |
| 3D Fuel PCTG | 265°C / 270°C | 80°C | 10mm³/s | 0.98 | 1.0mm | 0.062 | ✅ | Jul 2026 |

---

## Filament Profiles — 0.4mm stock brass (Heads 3, 4)

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Notes

### Polymaker PETG HF — OBX HF
- Temp tower 250–260°C. 245°C fails on bridges. 255°C minimum.
- MVS ceiling ~20mm³/s. Production 16mm³/s.
- PA tower confirmed 0.050.
- Retraction carried from PrusaSlicer working value — no stringing observed.

### 3D Fuel PCTG — OBX HF
- ⚠ Earlier session summary incorrectly recorded temp as 265/265 and MVS as 9mm³/s. Corrected values above.
- Temp 265°C first layer / 270°C remaining layers.
- MVS ceiling ~11mm³/s (gloss only in bottom 2mm of 10–25mm³/s test). Production 10mm³/s.
- PA 0.062 — higher than PETG (0.050) due to PCTG viscosity.
- Retraction speed, fan settings, print speeds still pending.

## ⚠ Pending

- PCTG: retraction speed, fan settings, print speeds
- Heads 3 & 4 (stock brass): no calibration data — starting fresh when filament assigned
