# Bambu A1

**Nozzles:** 0.6mm (Alexactly) / 0.4mm (Cherokee Makerspace ×2)  
**Slicer:** Bambu Studio / OrcaSlicer  
**Notes:** Open-frame bed slinger. Different thermal behavior than enclosed P1S/X1C — requires more layers without fan and higher min fan baseline.

---

## Filament Profiles — 0.6mm (Alexactly)

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|
| Polylite PETG | 255°C / 255°C | 70°C | 8mm³/s (Normal) / 6mm³/s (Quality) | 0.95 | 1.5mm @ 45mm/s | Firmware | ✅ | 2026-06-10 |
| 3D Fuel PCTG | 265°C / 265°C | 70°C | 28/32/36 mm³/s (Q/N/D) | ⚠ TBD | 4.0mm @ 45mm/s | Firmware | ✅ | Session 2026-08-05 |

---

## Filament Profiles — 0.4mm (Cherokee Makerspace)

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|
| ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Not calibrated | — |

---

## Cooling Settings — Polylite PETG 0.6mm

| Setting | Value |
|---|---|
| Fan min | 30% @ 20s |
| Fan max | 100% @ 5s |
| Overhang fan | 100% |
| Overhang threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 3 (one more than P1S — open frame) |
| Z-hop | 0.4mm Normal |

---

## Cooling Settings — 3D Fuel PCTG 0.6mm

| Setting | Value |
|---|---|
| Z-hop | 0.4mm |
| Fan settings | ⚠ TBD — pending fan calibration |

---

## MVS Detail — 3D Fuel PCTG 0.6mm

| Tier | MVS |
|---|---|
| Quality | 28 mm³/s |
| Normal | 32 mm³/s |
| Draft | 36 mm³/s |

MVS cliff confirmed ~40 mm³/s. Production ceiling = 80% of cliff.

---

## Notes

- MVS 8mm³/s showed artifacts on reducing elbow for Polylite PETG. Use 6mm³/s Quality tier for demanding geometry.
- Black Polylite PETG strings worse than white — increase retraction to 1.8–2.0mm for black colorway.
- 3D Fuel PCTG retraction (4.0mm) is significantly higher than Polylite PETG (1.5mm) — PCTG oozes considerably more on this open-frame machine. Do not cross-apply retraction values.
- Flow ratio for PCTG not yet calibrated — use 0.98 as starting point (consistent with other Bambu machines).
- ~50 rolls Polylite in Alexactly stock as of mid-2026. Transition to Polymaker PETG HF planned when depleted.
- Makerspace A1s (0.4mm) have no calibration data — starting fresh when filament is assigned.
- A1 being evaluated for phase-out at Alexactly — borderline performance on production parts.
