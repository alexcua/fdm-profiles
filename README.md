# FDM Profiles Repository

Calibration reference for Alexactly and Cherokee Makerspace 3D printing fleets.

## What's in this repo

| File/Folder | Purpose |
|---|---|
| `CALIBRATION_MASTER.md` | Narrative history, key learnings, session log |
| `filaments/` | Per-filament profiles — all machines side by side for consistency checking |
| `machines/` | Per-machine profiles — all filaments for a given printer in one place |
| `AGENT.md` | Instructions for AI agents populating and maintaining this repo |

## How to use

**Checking consistency across machines** → use `filaments/` docs. See all machines running the same filament side by side.

**Setting up a specific printer** → use `machines/` docs. See all filament profiles for that machine in one place.

**Understanding calibration history and decisions** → use `CALIBRATION_MASTER.md`.

## Fleet Summary

### Alexactly
| Machine | Nozzle(s) | Primary Filament |
|---|---|---|
| Bambu A1 | 0.6mm | Polylite PETG |
| Bambu P1S | 0.6mm / 0.4mm | Polymaker PETG HF / 3D Fuel PCTG |
| Bambu X1C | 0.6mm | Polymaker PETG HF |
| Bambu X2D | 0.4mm | 3D Fuel PCTG |
| Bambu H2D | 0.6mm HF (both extruders) | 3D Fuel PCTG |
| Bambu H2C | 0.6mm HF (left) / Vortex TBD (right) | 3D Fuel PCTG |
| Prusa XL 5-head | 0.4mm OBX HF (1,2,5) / 0.4mm brass (3,4) | 3D Fuel PCTG |

### Cherokee Makerspace
| Machine | Nozzle(s) | Primary Filament |
|---|---|---|
| Bambu A1 ×2 | 0.4mm | TBD |
| Prusa MK3.5 ×2 | 0.6mm CHT | Polylite PETG / California Matte PETG |
| Prusa MK3.5 ×1 | 0.4mm E3D V6 | Generic |
| Prusa MK3.5 ×2 | 0.6mm Revo (swappable 0.4/0.6/0.8) | Polylite PETG |
| Elegoo Orangestorm Giga | 0.8mm brass | 3D Fuel PCTG / Polylite PETG / Atomic PLA |

## Filament Naming Rules

- **Polymaker PETG** = HF (high flow) formula. Used on X1C, P1S 0.6mm.
- **Polylite PETG** = standard non-HF formula. Used on A1, Makerspace MK3.5s.
- These are distinct products from the same brand. Never conflate them.
- **3D Fuel PCTG** = primary structural filament for Alexactly production parts.

## Calibration Sequence (OrcaSlicer)

1. Temperature tower
2. Max Volumetric Speed (MVS)
3. Pressure Advance (PA)
4. Retraction

## Status Legend used in docs

- ✅ Confirmed
- ⚠ Pending or needs retest
- ❌ Invalid / do not use
