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

## Machine G-code mods — nozzle blob (PETG/PCTG)

**Problem:** stock start G-code crosses the nozzle wiper at ~140°C (it sets print temp with `M104` and doesn't wait). A leftover PETG/PCTG blob is still hard at 140°C. It bends the wiper, stays on the nozzle, and makes bed probing read high. The blob comes from the stock end G-code: it turns the heater off right after the last wipe, so the nozzle oozes while cooling and nothing wipes it.

- **Start G-code** (`gcode/Bambu_A1_start.gcode`, full file): non-PLA only. Park at X-28.5, `M109` to first-layer temp, then cross the wiper. ⚠ Not yet run on a printer (written 2026-10-06).
- **End G-code** (`gcode/Bambu_A1_end.gcode`, full file; the change sits between `M621 S255` and `M104 S0`): part fan on, cool at the purge position (X-48.2) to 200°C (PETG/PCTG) or 170°C (PLA), wipe twice, then heater off. ⚠ Not yet run on a printer (written 2026-10-06).

- Base: stock Bambu A1 G-code dated 20260513.
- **Bambu Studio user printer preset: `Bambu Lab A1 0.6 (Nozzle Clear)`** holds both modified start and end G-code (Alexactly 0.6mm). Created 2026-10-06.
- Makerspace A1s (0.4mm): not applied. To apply, make a matching 0.4 user preset with the same two files.
- Straighten or replace a bent wiper before testing.
- First-run checks:
  - **Start:** for non-PLA, the head pauses at X-28.5 until it reaches temp before crossing the wiper. If the wiper still bends during the very first `G28 X` (before any heating), that's a different move and needs a different fix.
  - **End:** the cooldown ooze drops where purge waste normally goes, not on the frame or the Y-axis path. Check the nozzle tip is clean before the next start.
- No end-of-print retraction added. Pulling molten PETG/PCTG up into the cool zone risks a jam on the next load.

---

## Notes

- MVS 8mm³/s showed artifacts on reducing elbow for Polylite PETG. Use 6mm³/s Quality tier for demanding geometry.
- Black Polylite PETG strings worse than white — increase retraction to 1.8–2.0mm for black colorway.
- 3D Fuel PCTG retraction (4.0mm) is significantly higher than Polylite PETG (1.5mm) — PCTG oozes considerably more on this open-frame machine. Do not cross-apply retraction values.
- Flow ratio for PCTG not yet calibrated — use 0.98 as starting point (consistent with other Bambu machines).
- ~50 rolls Polylite in Alexactly stock as of mid-2026. Transition to Polymaker PETG HF planned when depleted.
- Makerspace A1s (0.4mm) have no calibration data — starting fresh when filament is assigned.
- A1 being evaluated for phase-out at Alexactly — borderline performance on production parts.
