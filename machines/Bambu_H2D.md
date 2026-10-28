# Bambu H2D

**Extruders:** Left 0.6mm HF / Right 0.6mm HF (both identical)  
**Slicer:** OrcaSlicer / Bambu Studio  
**Notes:** Large format enclosed. Active chamber heating at 45°C. Conservative fan settings intentional — chamber heat conflicts with aggressive cooling. PA handled by firmware.

---

## Filament Profiles — 0.6mm HF (both extruders)

| Filament | Temp | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | ⚠ 255°C (tower 2026-10-28; snap test pending) | 45°C | 70°C | 12mm³/s (stock, untested) | 0.98 | ⚠ TBD | Firmware | ⚠ | Session 2026-10-28 |

- **H2D temp tower 280→250, 2026-10-28** (photo reviewed; chamber 45 heat-soaked, bed 70: recommended settings, assumed; extruder L/R ⚠ TBD): 280 pitted/bubbly surface, numerals illegible; 275 bubbly surface, long strings off the overhang; 270–265 long strings off the overhang, webbing in the cutout; 260 a few strings, light webbing, good numerals; **255 and 250 cleanest** (crisp numerals, clean overhang, minimal webbing). Proposed **255°C** (hotter end of the clean window, for layer adhesion on structural parts). Cold edge not found (250 still clean). Fine webbing in the cutout at every temp and bubbling at 275–280 suggest moisture: dry the spool before MVS. ⚠ Pending: snap test 250/255/260 (photos can't show layer adhesion). H2D only; H2C left not yet retested. Session 2026-10-28
  > Previously: 265°C (2026-08-02), tower run without the chamber heater; replaced by the chamber-45 tower.

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

- Temp: snap test 250/255/260 to lock 255 (tower done 2026-10-28). Dry the spool.
- MVS 10→30 at the locked temp, chamber 45 (12 is 3D Fuel stock, untested).
  > Previously: "Temp tower rerun with chamber heat-soaked" and "265°C may need to be higher" (done 2026-10-28; came in lower, 255).
- Retraction distance and speed.
- Fan settings specific to 0.6mm nozzle config.
