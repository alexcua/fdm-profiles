# Elegoo Orangestorm Giga

**Nozzle:** 0.8mm brass  
**Slicer:** OrcaSlicer 2.4  
**Notes:** Large format bed slinger. Cherokee Makerspace. No SD card slot — front USB occupied by camera, prints sent from OrcaSlicer each session. Powered USB hub or print server pending. Four independently heated bed zones. Nano Polymer adhesive required for large PETG parts.

---

## Filament Profiles

| Filament | Temp | Bed | MVS (Normal) | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C | 75°C | 32mm³/s | 1.0 | 0.55mm @ 45mm/s | 0.058 | ✅ | Session 2026-07-30 |
| Polylite PETG | 245°C | 75°C | 20mm³/s | 1.0 | 0.55mm @ 45mm/s | 0.05 | ✅ Functional part validated | Session 2026-07-30 |
| Atomic PLA | ❌ 265°C INVALID | 60°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ❌ Needs redo | Session 2026-07-30 |

---

## MVS Tiers

### 3D Fuel PCTG — Session 2026-07-30
| Tier | Layer Height | MVS | Speed |
|---|---|---|---|
| Quality | 0.30mm | 28mm³/s | 117mm/s |
| Normal | 0.40mm | 32mm³/s | 100mm/s |
| Draft | 0.50mm | 35mm³/s | 88mm/s |
| MVS cliff | — | ~36mm³/s | — |


### Polylite PETG — Session 2026-07-30
| Tier | Layer Height | MVS | Speed |
|---|---|---|---|
| Quality | 0.30mm | 18mm³/s | 75mm/s |
| Normal | 0.40mm | 20mm³/s | 63mm/s |
| Draft | 0.50mm | 22mm³/s | 55mm/s |
| MVS cliff | — | ~23mm³/s | — |

---

## Profile Architecture — Session 2026-07-30

- One filament profile per brand/type: stores temp, MVS at Normal tier value, PA, retraction, fan.
- Two shared process profiles (Normal 0.40mm, Draft 0.50mm) with all speeds at 200mm/s so MVS always governs.
- Process profiles: 2 walls, 15% cubic infill, 1.5mm top/bottom fixed (by mm), first layer +0.05mm at 35mm/s.
- PA line test forces all four bed zones to heat (spawns at bed center).

---

## Fan Settings — Session 2026-07-30

| Filament | Fan thresholds | Notes |
|---|---|---|
| 3D Fuel PCTG | 20–30% max | Low fan to maintain layer adhesion. Do not exceed 30%. |
| Polylite PETG | 40% @ 30s / 60% @ 12s max | Standard PETG cooling. 100% max caused stringing — confirmed this session. |

---

## Seam Settings — Session 2026-07-30

| Setting | Value |
|---|---|
| Seam position | Back |
| Scarf seam | Contour ✅, Hole ✅, Conditional ✅ |
| Seam gap | 5% |
| Staggered inner seams | On |

- Corner seam blobbing resolved by enabling scarf on both contour AND hole plus staggered inner seams.
- Seam gap reduced from 10% to 5% to close missing extrusion at seam start point.
- Scarf on hole critical for parts with rectangular cutouts — inner perimeter seam stacks at corners without it.

---

## ⚠ Pending

- Atomic PLA: full recalibration starting 190–230°C temp tower.
- PCTG functional part validation.
- Powered USB hub or print server for persistent connection.
