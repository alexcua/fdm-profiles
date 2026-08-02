# 3D Fuel PCTG — All Machines

**Primary use:** Alexactly production parts (camera mounts, siding clips, structural components)  
**Material notes:** Moisture sensitive — dry at 65–70°C for 6–8h before printing. Store in sealed container or AMS. Mildly abrasive — use hardened steel nozzles for extended runs.

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|---|
| Bambu X1C | 0.6mm HS | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |
| Bambu P1S | 0.6mm HS | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |
| Bambu P1S | 0.4mm HS | 265°C / 265°C | 70°C | 8mm³/s | 0.98 | 0.6mm | Firmware | ✅ | 2026-06-17 |
| Bambu X2D | 0.4mm main | 265°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | 0.06 (OrcaSlicer) | ✅ | 2026-07-19 |
| Bambu H2D | 0.6mm HF | 265°C (⚠ retest w/ chamber) | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ | 2026-08-02 |
| Bambu H2C | 0.6mm HF (left) | 265°C (⚠ retest w/ chamber) | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ | 2026-08-02 |
| Prusa XL | 0.4mm OBX HF | 265°C / 270°C | 80°C | 10mm³/s | 0.98 | 1.0mm | 0.062 | ✅ | 2026-07-18 |
| Prusa MK3.5 | 0.6mm CHT | 260–265°C | 80°C | 24mm³/s | 0.98 | ⚠ TBD | ⚠ TBD | ⚠ | 2026-08-02 |
| Elegoo Giga | 0.8mm brass | 265°C | 75°C | 32mm³/s (Normal) | 1.0 | 0.55mm @ 45mm/s | 0.058 | ✅ | 2026-08-02 |

---

## Consistency Notes

- **Temperature:** All machines confirmed at 265°C. H2D/H2C need retest with active chamber at 45°C — may require higher temp.
- **Flow ratio:** 0.98 across all machines except Giga (1.0). Consistent.
- **MVS:** Varies significantly by nozzle size and machine. Do not port between machines.
- **PA:** Bambu machines use firmware. Prusa/Giga use slicer values. Never apply a numeric PA value to a Bambu machine.
- **Retraction:** Higher than PETG due to PCTG viscosity. 1.4mm @ 45–50mm/s on 0.6mm Bambu. Lower on 0.4mm.

---

## Per-Machine Detail

### Bambu X1C / P1S — 0.6mm hardened steel
- Temp tower tested 240–280°C. Sweet spot 265°C.
- MVS ceiling ~15mm³/s. Production 12mm³/s.
- PA firmware-handled. OrcaSlicer PA checkbox must remain unchecked.
- Retraction speed 30mm/s was insufficient — caused stringing. Must be 45–50mm/s.
- Fan max 100% @ 5s, overhang threshold 10%.
- Nozzle booger/drool common with PCTG. Enable "Wipe before outside wall" and "Avoid crossing perimeters".
- Silicone sock must be intact on P1S — missing sock causes external carbonization.

### Bambu P1S — 0.4mm hardened steel
- Same hotend as 0.6mm but lower MVS ceiling due to bore size.
- Retraction increased from stock 0.4mm to 0.6mm to address nozzle booger.

### Bambu X2D — 0.4mm main nozzle
- Higher MVS than P1S 0.4mm due to PMSM servo extruder.
- MVS test (Aug 2026): 4–14mm³/s in 1mm³/s steps. Strength held full range — failed only in last ~2mm at 14mm³/s.
- Single-tier MVS profile — no Quality/Normal/Draft split. Range too flat to justify multiple profiles.
- Temp tower (Aug 2026): 255–275°C. Sweet spot 265°C confirmed. 270–275°C showed duller surface sheen.
- PA = 0.06 confirmed via manual pattern test (range 0–0.08, step 0.005).
- PA field not exposed in Bambu Studio — apply only in OrcaSlicer.
- Real print validation confirmed Aug 2026.
- Retraction pending real-world print test.

### Bambu H2D / H2C — 0.6mm HF (left extruder)
- 3D Fuel stock profile (0.4mm) uses 275°C, 12mm³/s, chamber 45°C, max fan 20%.
- Temp tower run at 265°C without active chamber — needs rerun with chamber heat-soaked.
- Conservative fan settings intentional for active chamber environment.

### Prusa XL — 0.4mm Obxidian HF
- ⚠ Earlier session summary incorrectly recorded temp as 265/265 and MVS as 9mm³/s.
- Corrected values: 265°C first layer / 270°C remaining, MVS 10mm³/s.
- Retraction speed, fan settings, print speeds still pending.

### Prusa MK3.5 — 0.6mm CHT
- MVS ceiling above 30mm³/s — CHT nozzle high-flow advantage confirmed.
- Layer shift during MVS test caused by bed slinger speed limits, not filament.
- PA and retraction pending.

### Elegoo Orangestorm Giga — 0.8mm brass
- MVS cliff ~36mm³/s.
- Tiers: Quality 0.30mm/28mm³/s | Normal 0.40mm/32mm³/s | Draft 0.50mm/35mm³/s.
- Nano Polymer adhesive required for large parts. 75°C bed maintained throughout.
- Functional part validation pending.
