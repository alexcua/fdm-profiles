# Bambu H2D

**Extruders:** Left 0.6mm HF / Right 0.6mm HF (both identical)  
**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** Large format enclosed. Active chamber heating at 45°C. Conservative fan settings intentional — chamber heat conflicts with aggressive cooling. PA handled by firmware.

---

## Filament Profiles — 0.6mm HF (both extruders)

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | ⚠ 265°C (retest needed) | 45°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ | 2026-08-02 |

---

## 3D Fuel Stock Profile Reference (0.4mm — for comparison)

| Setting | Value |
|---|---|
| Temperature | 275°C |
| MVS | 12mm³/s |
| Chamber | 45°C |
| Fan max | 20% |
| Overhang fan | 50% |
| Overhang threshold | 95% |

These conservative fan values are intentional for active chamber environment. Do not apply standard PETG/PCTG fan settings to H2.

---

## ⚠ Pending

- Temp tower rerun with chamber fully heat-soaked at 45°C before locking temperature value.
- Initial temp tower run at 265°C without active chamber — may need to be higher (stock profile uses 275°C).
- Retraction distance and speed.
- Fan settings specific to 0.6mm nozzle config.
