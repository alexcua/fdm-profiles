# Prusa MK3.5 — 0.6mm E3D Revo (Swappable)

**Nozzle:** E3D Revo swappable system — available sizes: 0.4mm, 0.6mm, 0.8mm  
**Slicer:** OrcaSlicer / PrusaSlicer  
**Machines (Cherokee Makerspace ×2):** **CM05** has the 0.6 **brass** Revo nozzle; **CM04** has the 0.6 **ObXidian** Revo nozzle (E3D's coated hardened nozzle). Recorded 2026-10-16.  
**Notes:** Bed slinger. Brass and hardened are different nozzle types: separate calibrations, values don't transfer between them. Revo nozzle swaps tool-free. Each nozzle size requires independent calibration — do not port MVS between sizes. Do not port from CHT config even at same 0.6mm diameter.

---

## Filament Profiles — 0.4mm Revo

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Filament Profiles — 0.6mm Revo brass

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## Filament Profiles — 0.6mm Revo ObXidian (CM04)

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG (⚠ confirm) | ⚠ 260°C proposed (confirm pending) | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ In progress, Session 2026-10-16 |

- **Temp tower 280→240°C step 5** (photos reviewed). Session 2026-10-16
  - 240–245: rough, beaded lines under the ledges; drooping layers at the top of the circle at 240; strings in the circle at 245. Too cold.
  - 250–255: better; one long string off the 255 overhang tip. Good, at the cold edge.
  - 260: clean overhang, crisp numerals, clean circle and cone. Best.
  - 265–270: strings in the circle, getting worse.
  - 275–280: lumpy, bubbly texture inside the window, drooping bridges, heavy strings. Too hot.
  - **Proposed 260°C.** Same as CM03 (0.4 V6 brass). ObXidian conducts heat close to brass.
  - Strings across the whole range, not just the hot end, point to retraction or moisture: dry the spool before MVS.
  - ⚠ Pending: user confirmation of filament (assumed 3D Fuel PCTG from the 240–280 range) and of the 260 pick; tower settings used.

---

## Filament Profiles — 0.8mm Revo

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status |
|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated |

---

## ⚠ Pending

- All nozzle sizes and filament combinations need full calibration.
- CM04 (0.6 ObXidian): 3D Fuel PCTG temp tower done, 260°C proposed (2026-10-16). CM05 (0.6 brass): Polymaker PETG HF loaded, not yet calibrated.
- Calibrate in this priority order based on usage frequency.
- Each nozzle size is a separate calibration — values do not transfer between sizes.
