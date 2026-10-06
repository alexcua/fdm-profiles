# Bambu P1S

**Nozzles:** 0.6mm hardened steel / 0.4mm hardened steel  
**Slicer:** OrcaSlicer (primary), Bambu Studio  
**Notes:** CoreXY enclosed. No Lidar (unlike X1C). PA handled by firmware. G-code from P1S profile can run on X1C.

---

## Filament Profiles — 0.6mm hardened steel

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Polymaker PETG HF | 250°C / 250°C | 70°C | 20mm³/s | 0.952 | 1.0mm | Firmware | ✅ | 2026-06-10 |
| 3D Fuel PCTG | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |

---

## Filament Profiles — 0.4mm hardened steel

| Filament | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| 3D Fuel PCTG | 265°C / 265°C | 80°C | 8mm³/s | 0.98 | 0.6mm @ 45mm/s | Firmware | ✅ | Session 2026-08-02 |

---

## Cooling Settings — Polymaker PETG HF (0.6mm)

| Setting | Value |
|---|---|
| Fan min | 30% @ 20s |
| Fan max | 100% @ 5s |
| Overhang fan | 100% |
| Overhang threshold | 10% |
| Fan prestart | 3s |
| Close fan first layers | 2 |
| Exhaust fan | 70% during + after print |

---

## Cooling Settings — 3D Fuel PCTG (0.4mm)

| Setting | Value |
|---|---|
| Fan min | 10% @ 30s |
| Fan max | 40% @ 12s |
| Overhang fan | 90% |
| Overhang threshold | 10% |
| Force cooling overhangs | on |

> Conservative fan settings are correct for PCTG on enclosed machines — do not apply PETG fan settings to PCTG.

---

## Machine G-code mods — purge coil and Z-home debris (PETG/PCTG)

**Problem:**
- **Debris on the bed after the wipe.** The nozzle touches the bed edge to home Z (X135 Y253) right after only one wipe, at first-layer temp −20. PETG/PCTG ooze at that temp, so it gets left at the touch point.
- **Purge coil thrown out instead of dropping into the chute.** The coil forms at the top of the chute and stays attached to the nozzle by a string. The stock sequence cools only to −20 before the shake, so a PETG/PCTG string bends instead of snapping. The fast passes over the wiper (just right of the chute) then drag the coil off the chute edge and throw it onto the bed. PLA's string snaps, so PLA is fine. Observed 2026-10-06.

**Mods** (`gcode/Bambu_P1S_0.6_start.gcode`, full file; all changes are non-PLA only, PLA runs stock):
- **1a:** after the purge, cool to first-layer temp −60 with the part fan on, then pause 5s so the string freezes before the shake.
- **1b:** every pass over the wiper at 6000 mm/min (stock uses 15000), plus extra passes and a slow exit to X165, so a coil that's still attached isn't flung.
- If the coil still comes out with 1a/1b: cool further before the shake, −60 → −80 (PCTG ≈185°C). It costs more time but freezes the string right at the nozzle.
- **2:** two extra wipes before moving to the Z-home touch point.
- ⚠ Not yet run on a printer (written 2026-10-06). Base: stock P1S-0.6 start G-code dated 20251031. Cost: roughly 30–60s more per start for PETG/PCTG.
- First-run checks:
  - Where the debris was: at the Z-home touch point (rear edge, X≈135) or at the scrub patch (rear centre, X124–131, Y≈260)? Mod 2 targets the touch point.
  - The coil drops into the chute during the shake.
  - Clean the exposed steel at the back of the bed once before testing, so old debris isn't mistaken for new.
- Applies to the 0.6 preset only. The 0.4 P1S needs its own stock file as the base.

---

## Notes

- 0.4mm PCTG: lower MVS ceiling than 0.6mm — bore size is the limiting factor.
- 0.4mm PCTG: retraction increased from stock 0.4mm to 0.6mm to address nozzle booger.
- Silicone sock must be intact — missing or degraded sock causes progressive external nozzle carbonization that accumulates between prints. PCTG contacts bare aluminum heater block, bakes on, and sheds onto next print. PCTG more aggressive than PETG at 265°C. Replace sock if any hardened material is embedded in its surface. ✅ Session 2026-08-02
- If external buildup persists with sock intact: re-seat nozzle at temp to eliminate heat-break gap as secondary accumulation point. ⚠ Session 2026-08-02
- If buildup still persists: try (in order) drop temp to 260°C → retraction to 0.8mm → MVS to 7mm³/s. ⚠ Session 2026-08-02
- PCTG nozzle drool: enable "Wipe before outside wall" and "Avoid crossing perimeters".
- Temp tower for P1S 0.4mm PCTG confirmed 265°C, range tested 240–280°C.
- See Bambu_X1C.md for shared overhang print profile settings.
