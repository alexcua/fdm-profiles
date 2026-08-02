# Prusa MK3.5 — 0.6mm CHT Nozzle

**Nozzle:** 0.6mm CHT (non-swappable)  
**Slicer:** OrcaSlicer / PrusaSlicer  
**Notes:** Bed slinger. CHT nozzle has high MVS ceiling but machine motion limits print speeds. PA set in slicer. Independent calibration required — do not port MVS from Revo or E3D V6 configs.

---

## Filament Profiles

| Filament | Temp | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 260–265°C | 80°C | 24mm³/s | 0.98 | ⚠ TBD | ⚠ TBD | ⚠ Partial | 2026-08-02 |
| Polylite PETG | 255°C | 80°C | 15/17/19 mm³/s (Q/N/D) | ⚠ TBD | ⚠ TBD | 0.044–0.05 | ⚠ Partial | 2026-07-12 |
| California Matte PETG | 220°C | 80°C | 10–12mm³/s | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Partial | 2026-07-12 |

---

## Notes

### 3D Fuel PCTG
- First temp tower invalid (wet filament — 1 week out of bag). Retest with dry filament confirmed 260–265°C.
- MVS ceiling above 30mm³/s. Production 24mm³/s (80% of 30).
- Layer shift during MVS test caused by bed slinger speed limits — not a filament issue. Does not affect production at 45mm/s.
- PA and retraction pending.
- Dry at 65–70°C for 6–8h before printing.

### Polylite PETG
- MVS cliff ~20mm³/s. Tiers 15/17/19 mm³/s Quality/Normal/Draft.
- PA ~0.044–0.05, cross-validated against Giga result of 0.05.
- Retraction pending.
- Sponsor showcase material at Cherokee Makerspace.

### California Matte PETG
- MVS cooling-limited, not flow-limited. Conservative 10–12mm³/s.
- PA test required Z offset drop to get first-layer adhesion. Final PA value not confirmed.
- Retraction pending.
- Sponsor showcase material at Cherokee Makerspace.

## ⚠ Pending

- PCTG: PA, retraction
- Polylite: retraction, flow ratio
- California Matte: PA confirmation, retraction, flow ratio
