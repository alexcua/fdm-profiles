# Polymaker ASA — All Machines

**Primary use:** ⚠ TBD (UV/heat-resistant outdoor parts)  
**Material notes:** Needs an enclosure. Heated-chamber machines (H2 series) are the target. Black colorway has shown heat creep on H2C 0.6mm HF; see notes. Polymaker ASA and PolyLite ASA are the same product (branding only). All stock is labeled Polymaker ASA, so use that name.

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Chamber | Bed | MVS | Flow | Retraction | PA | Status | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Bambu H2C | 0.6mm HF (left) | ⚠ TBD / 255°C | 60°C | 100°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | Firmware | ⚠ In progress (temp done) | Session 2026-10-01 |

---

## Consistency Notes

- Only one machine so far. H2D uses the same left 0.6mm HF hotend, so the H2C result may apply to H2D. Unverified.
- Stock profile temp 260°C. Calibrated 255°C.

---

## Per-Machine Detail

### Bambu H2C — 0.6mm HF (left extruder)

**Temp tower (white colorway), 230–270°C in 5° steps, chamber 60°C, bed 100°C, Bambu Studio:**
- 230–240: Too cold. Overhang edges lumpy and curling at the tips, loose layer lines on overhang faces, strings across the circle cutouts at 230/235.
- 245: Usable, but at the cold edge (slightly rough overhang edge).
- 250–255: Cleanest blocks. Clean overhangs, crisp numerals, minimal stringing.
- 260: Surfaces start degrading. Ledge tops show infill texture, numerals rougher.
- 265–270: Most stringing. Textured/scarred ledge surfaces.
- **Result: 255°C**, the hot end of the clean 250–255 window. Photos reviewed in session. Session 2026-10-01

**Open items:**
- ⚠ Snap test of 250 / 255 / 260 blocks pending. A tower can't show layer adhesion, which is ASA's main reason to run hotter. If 255 breaks noticeably easier than 260, reconsider 260 for functional parts.
- Profile conditions: nozzle 255°C, bed 100°C, chamber 60°C. Session 2026-10-01
- Temp tower was printed at chamber 60°C, so the 255°C result holds at production chamber temp. Session 2026-10-01
- Slicer: Bambu Studio. Session 2026-10-01
- ⚠ Tower was printed in **white**. The heat creep problem is with **black**. Confirm 255°C on black before treating it as colorway-independent (carbon black changes flow behavior; see CALIBRATION_MASTER Key Learnings).

**Heat creep — black colorway (reason for this custom profile):**
- Symptom reported: heat creep printing black Polymaker ASA on 0.6mm HF. No custom profile existed; stock profile was in use (260°C).
- ⚠ Untested hypotheses, in order of likelihood:
  - (1) Chamber temp too high for the cold side of the heat break. Chamber is 60°C, which makes this the lead suspect. First variable to try: step chamber down (e.g. 50°C) on a black print.
  - (2) Low flow rate / long layer times leaving filament heat-soaking in the heat break.
  - (3) Retraction too long, pulling softened filament up into the cold zone.
  - (4) 260°C stock temp. The drop to 255°C may help on its own.
- Validate each one on a black print before recording a fix.
