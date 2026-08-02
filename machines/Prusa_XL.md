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
|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 255°C / 255°C | 80°C | 16mm³/s | 1.0 | 0.8mm | 0.050 | ✅ | 2026-06-10 |
| 3D Fuel PCTG | 265°C / 270°C | 80°C | 10mm³/s | 0.98 | 1.0mm | 0.062 | ✅ | 2026-07-18 |

---

## Filament Profiles — 0.4mm stock brass (Heads 3, 4)

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Notes

### Polymaker PETG HF — OBX HF
- Temp tower 250–260°C. 245°C fails on bridges. 255°C minimum.
- MVS ceiling ~20mm³/s. Production 16mm³/s (80%).
- PA tower confirmed 0.050 at 25mm of 50mm tower height.
- PA must be enabled in OrcaSlicer — default grayed-out value was 0.02 (incorrect).
- Retraction carried from PrusaSlicer working value — no stringing observed.

### 3D Fuel PCTG — OBX HF
- ⚠ Earlier session summary (Jul 18) incorrectly recorded temp as 265/265 and MVS as 9mm³/s. Corrected values above are from live test data.
- Temp tower 250–270°C tested. Acceptable range 260–270°C. 265°C first layer / 270°C remaining confirmed.
- MVS tower 10–25mm³/s. Gloss only in bottom 2mm = ceiling ~10–11mm³/s. Production 10mm³/s.
- PA 0.062 — higher than PETG HF (0.050) due to PCTG viscosity.
- Retraction speed, fan settings, and print speeds still pending.

---

## OrcaSlicer Setup Notes

- PA is set in slicer (not firmware). Confirm PA checkbox is enabled — grayed-out default of 0.02 is incorrect.
- OctoPrint on Raspberry Pi 4B handles print dispatch (USB connection, black USB 2.0 port — serial only, bandwidth irrelevant).

---

## ⚠ Pending

| Item | Notes |
|---|---|
| PCTG: retraction speed | Not confirmed |
| PCTG: fan settings | Not documented |
| PCTG: print speeds | Not confirmed |
| Heads 3 & 4 (stock brass) | Full calibration sequence needed when filament assigned |

---

## Calibration Session Log

| Date | Key outcomes |
|---|---|
| 2026-06-10 | Polymaker PETG HF full calibration — temp, MVS, PA, retraction confirmed |
| 2026-07-12 | 3D Fuel PCTG initial calibration — temp, MVS, PA, retraction confirmed |
| 2026-07-18 | Correction — MVS corrected from 9 to 10mm³/s; temp corrected from 265/265 to 265/270 |
| 2026-08-02 | OctoPrint/Pi USB setup documented; retraction speed, fan, print speeds flagged pending |
