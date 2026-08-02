# Elegoo Orangestorm Giga

**Nozzle:** 0.8mm brass  
**Slicer:** OrcaSlicer 2.4  
**Notes:** Large format bed slinger. Cherokee Makerspace. No SD card slot — front USB occupied by camera, prints sent from OrcaSlicer each session. Powered USB hub or print server pending. Four independently heated bed zones. Nano Polymer adhesive required for large PETG parts.

---

## Filament Profiles

| Filament | Temp | Bed | MVS (Normal) | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C | 75°C | 32mm³/s | 1.0 | 0.55mm @ 45mm/s | 0.058 | ✅ | Jul 2026 |
| Polylite PETG | 245°C | 75°C | 20mm³/s | 1.0 | 0.55mm @ 45mm/s | 0.05 | ✅ | Jul 2026 |
| Atomic PLA | ❌ 265°C INVALID | 60°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ❌ Needs redo | Jul 2026 |

---

## MVS Tiers

### 3D Fuel PCTG
| Tier | Layer Height | MVS | Speed |
|---|---|---|---|
| Quality | 0.30mm | 28mm³/s | 117mm/s |
| Normal | 0.40mm | 32mm³/s | 100mm/s |
| Draft | 0.50mm | 35mm³/s | 88mm/s |
| MVS cliff | — | ~36mm³/s | — |

### Polylite PETG
| Tier | Layer Height | MVS | Speed |
|---|---|---|---|
| Quality | 0.30mm | 18mm³/s | 75mm/s |
| Normal | 0.40mm | 20mm³/s | 63mm/s |
| Draft | 0.50mm | 22mm³/s | 55mm/s |
| MVS cliff | — | ~23mm³/s | — |

---

## Profile Architecture

- One filament profile per brand/type: stores temp, MVS at Normal tier value, PA, retraction, fan.
- Two shared process profiles (Normal 0.40mm, Draft 0.50mm) with all speeds at 200mm/s so MVS always governs.
- Process profiles: 2 walls, 15% cubic infill, 1.5mm top/bottom fixed (by mm), first layer +0.05mm at 35mm/s.
- PA line test forces all four bed zones to heat (spawns at bed center).

---

## Fan Settings

| Filament | Max fan | Notes |
|---|---|---|
| 3D Fuel PCTG | 20–30% | Low fan to maintain layer adhesion |
| Polylite PETG | 50–60% | Standard PETG cooling |

---

## ⚠ Pending

- Atomic PLA: full recalibration starting 190–230°C temp tower.
- PCTG functional part validation.
- Polylite PETG functional part validation.
- Powered USB hub or print server for persistent connection.
