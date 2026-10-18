# 3D Fuel PCTG — All Machines

**Primary use:** Alexactly production parts (camera mounts, siding clips, structural components)  
**Material notes:** Moisture sensitive — dry at 65–70°C for 6–8h before printing. Picks up enough moisture in about a day out to string badly (CM03→CM04, 2026-10-17/18). Store in sealed container or AMS. Not abrasive: unfilled PCTG has no fibre or mineral filler, so brass nozzles are fine. Exception: sparkle/glitter colourways (e.g. Galaxy Black) carry particles that can wear brass over long runs.
> Previously: "Mildly abrasive — use hardened steel nozzles for extended runs" — corrected 2026-10-16: unfilled PCTG isn't abrasive (per user).

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|---|
| Bambu X1C | 0.6mm HS | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |
| Bambu P1S | 0.6mm HS | 265°C / 265°C | 70°C | 12mm³/s | 0.98 | 1.4mm @ 45mm/s | Firmware | ✅ | 2026-08-02 |
| Bambu P1S | 0.4mm HS | 265°C / 265°C | 80°C | 8mm³/s | 0.98 | 0.6mm @ 45mm/s | Firmware | ✅ | Session 2026-08-02 |
| Bambu X2D | 0.4mm main | 265°C | 70°C | 12mm³/s | 0.98 | ⚠ TBD | 0.06 (OrcaSlicer) | ✅ | 2026-07-19 |
| Bambu H2D | 0.6mm HF | 265°C (⚠ retest w/ chamber) | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ | 2026-08-02 |
| Bambu H2C | 0.6mm HF (left) | 265°C (⚠ retest w/ chamber) | 70°C | 12mm³/s | 0.98 | ⚠ TBD | Firmware | ⚠ | 2026-08-02 |
| Prusa XL | 0.4mm OBX HF | 265°C / 270°C | 80°C | 10mm³/s | 0.98 | 1.0mm | 0.062 | ✅ | 2026-07-18 |
| Prusa MK3.5 | 0.6mm CHT | 260–265°C | 80°C | 24mm³/s | 0.98 | ⚠ TBD | ⚠ TBD | ⚠ | 2026-08-02 |
| Bambu A1 | 0.6mm | 265°C / 265°C | 70°C | 28/32/36 mm³/s (Q/N/D) | ⚠ TBD | 4.0mm @ 45mm/s | Firmware | ✅ | Session 2026-08-05 |
| Prusa MK3.5 (CM03) | 0.4mm E3D V6 brass | 260°C ✅ | 80°C | 9mm³/s | ⚠ TBD | 0.6mm @ 45mm/s | 0.03 | ⚠ In progress | Session 2026-10-16 |
| Prusa MK3.5 (CM04) | 0.6mm Revo ObXidian | 255°C ✅ | ⚠ TBD | 9mm³/s | ⚠ TBD | ⚠ TBD | 0.025 | ⚠ In progress | Session 2026-10-16 |
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
- External nozzle carbonization (inter-print buildup): root cause is missing or degraded silicone sock. PCTG contacts bare heater block, bakes on, accumulates between prints, sheds onto next print. Inspect and replace sock first. If buildup persists with sock intact: re-seat nozzle at temp, then try temp 260°C → retraction 0.8mm → MVS 7mm³/s in that order. Session 2026-08-02

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

### Prusa MK3.5 (CM03) — 0.4mm E3D V6 brass
- Temp tower 280→240°C: 255–265 clean, ≤250 rough circle tops, ≥270 stringing, 280 brown speck. **260°C confirmed by user** (snap test not run). Session 2026-10-16
- MVS 4→14 step 1 at 260°C: sheen drop and easy layer split at 7.5mm, so the ceiling is 11.5 mm³/s. Production 9 mm³/s (80%). Session 2026-10-16
- PA pattern 0→0.08 at 260°C: tips smooth 0.03–0.05 (user, in hand), nearly identical. PA 0.03 (user's choice, low end of range; 0.04 proposed first). Session 2026-10-17
  > Previously: PA 0.04 (2026-10-17), replaced by the user's choice of 0.03 within the same clean range.
- Retraction test 0→2.0 at 260°C: no stringing at any height. 0.6mm @ 45 mm/s (low value with margin for ooze). Session 2026-10-17

### Prusa MK3.5 (CM04) — 0.6mm Revo ObXidian
- Temp tower 280→240°C: 260 cleanest, ≤245 too cold, ≥265 stringing, 275–280 bubbling. **255°C chosen by user** (cleaner bridge, less stringing in hand). My photo read was 260, replaced.
- MVS 6→20 step 1 at 255°C: faint sheen change at 5mm, so the ceiling is 11 mm³/s; strength held to 20. Production 9 mm³/s. About the same ceiling as CM03's 0.4 (Revo short melt zone). Session 2026-10-17
- PA pattern 0→0.08 at 255°C: 0.02–0.03 most well formed (user, in hand). PA 0.025. Session 2026-10-17
- Retraction test unreadable (rough towers, strings). Different spool from CM03, which printed clean. Moisture suspected, so MVS 9 may be low. Dry the spool, rerun retraction, then recheck MVS. Session 2026-10-17
- Rerun with CM03's clean spool: still rough + stringy, so **moisture is ruled out and the cause is CM04 hardware** (suspect partial clog, nozzle buildup, extruder tension, Revo seating). Cold pull, then retraction 0→1.0 step 0.05, then recheck MVS. Session 2026-10-17
  > Previously: moisture suspected (2026-10-17). Ruled out by the spool swap.
- **Correction 2026-10-18:** after drying that same spool 3h (nothing else changed), CM04's retraction towers came out clean. **Moisture was the cause.** The spool picked up moisture between CM03 and CM04. Hardware suspicion withdrawn. Rerun CM04 MVS dry. Session 2026-10-18
  > Previously: "moisture ruled out, CM04 hardware" (2026-10-17). Wrong. Strings across the whole range, so dry before MVS. Session 2026-10-16

### Prusa MK3.5 — 0.6mm CHT
- MVS ceiling above 30mm³/s — CHT nozzle high-flow advantage confirmed.
- Layer shift during MVS test caused by bed slinger speed limits, not filament.
- PA and retraction pending.

### Elegoo Orangestorm Giga — 0.8mm brass
- MVS cliff ~36mm³/s.
- Tiers: Quality 0.30mm/28mm³/s | Normal 0.40mm/32mm³/s | Draft 0.50mm/35mm³/s.
- Nano Polymer adhesive required for large parts. 75°C bed maintained throughout.
- Functional part validation pending.

### Bambu A1 — 0.6mm (Alexactly)
- Temp tower 245–275°C confirmed 265°C — consistent with all other machines running 3D Fuel PCTG.
- MVS tested in three passes (5–25, 25–40, 40–55 mm³/s). Clean through 40mm³/s, hard cliff 40–55. Cliff ~40mm³/s.
- Production MVS tiers: Quality 28 mm³/s / Normal 32 mm³/s / Draft 36 mm³/s.
- Retraction required four test passes (0.5–2.0, 1.5–3.0, 2.5–4.0, 3.5–5.0mm). Clean zone at 3.5–4.0mm; over-retraction artifacts above 4.0mm. Confirmed 4.0mm @ 45mm/s.
- Retraction is dramatically higher than Polylite PETG on same machine (1.5mm) — PCTG ooze characteristics are substantially different on open-frame machine.
- Z-hop 0.4mm. PA firmware-handled. Flow ratio and fan settings pending.
- Session 2026-08-05
