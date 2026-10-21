# Polymaker ASA — All Machines

**Primary use:** ⚠ TBD (UV/heat-resistant outdoor parts)  
**⚠ ROOT CAUSE FOUND (2026-10-21): the black jams came from one bad spool** (H2C AMS slot 3), not the H2C. See "Spool finding" below.  
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
- ⚠ Snap test inconclusive. The tower broke at 255, but that was near the middle of the sample, where hand-bending leverage is highest. Other blocks could not be broken by hand. That doesn't show 255 is weaker. Controlled test pending: clamp each 250/255/260 boundary in a vise and load each block the same way. Session 2026-10-01
- Profile conditions: nozzle 255°C, bed 100°C, chamber 60°C. Session 2026-10-01
- Temp tower was printed at chamber 60°C, so the 255°C result holds at production chamber temp. Session 2026-10-01
- Slicer: Bambu Studio. Session 2026-10-01
- ⚠ Tower was printed in **white**. The heat creep problem is with **black**. Confirm 255°C on black before treating it as colorway-independent (carbon black changes flow behavior; see CALIBRATION_MASTER Key Learnings).

**Heat creep — black colorway (reason for this custom profile):**
- Symptom reported: heat creep printing black Polymaker ASA on 0.6mm HF. No custom profile existed; stock profile was in use (260°C).
- ⚠ Untested hypotheses, in order of likelihood:
  - (1) Chamber temp too high for the cold side of the heat break. Chamber is 60°C, which makes this the lead suspect. First variable to try: step chamber down (e.g. 50°C) on a black print.
  - (2) Low flow rate / long layer times leaving filament heat-soaking in the heat break.
  - ~~(3) Retraction too long~~ — unlikely: retraction was 0.4mm (short) when heat creep recurred. Session 2026-10-01
  - ~~(4) Nozzle temp~~ — ruled out: white completed starting at 270°C under the same chamber/bed. Session 2026-10-01
  - (5) Radiant heat from the 100°C bed into the toolhead during a long first layer. (6) Black absorbing more radiant heat than white. (7) Cumulative toolhead heat soak over the session. ⚠ Untested.
- Heat creep recurred on a black print at 255°C / chamber 60°C / bed 100°C / retraction 0.4mm. White printed clean at the same conditions (temp tower). Print was the MVS test (10–30 mm³/s). It failed before finishing layer 1. ❌ No MVS data from this run. Session 2026-10-01
- Failure point (photo): layer 1 perimeters printed clean. Under-extrusion began right after the first-layer solid fill started, strong at the start of the fill and fading to patchy within ~1/4 of one serpentine segment. The failure came when extrusion force rose (perimeter → fill), which fits filament too soft at the gear to take higher push force. Session 2026-10-01
- Failing in layer 1 points to a feed/hotend state problem before printing (leftover partial clog from the previous creep, or heat soak while the chamber preheated), not to the flow ceiling. ⚠ Diagnose before retrying MVS: inspect the unloaded filament tip, cold pull, then a manual extrude test.
- Unloaded filament was **squashed (soft-deformed, not chewed)** at the extruder gear. The filament softened at the gear itself. This is extruder-zone overheating, not classic heat-break creep. Session 2026-10-01
- White temp tower completed at the same chamber/bed, starting at 270°C (hottest block is printed first). So nozzle temp is not the cause. Session 2026-10-01
- Two variables differ between the passing and failing prints: **colour** (white vs black) and **object** (small tower vs larger MVS footprint, i.e. a longer layer 1 with the toolhead low over the 100°C bed). Toolhead heat-soak time also differed (the MVS run came after hours at 60°C chamber).
- **White MVS test (10–30 mm³/s) completed** at identical conditions (255 / 60 / 100, same AMS 3 slot). Object size and AMS ruled out. **The failure is black-specific.** ⚠ Toolhead heat soak still not fully excluded until confirmed whether the machine cooled between runs. Session 2026-10-01
- **White MVS (10→30 at 255°C / chamber 60 / bed 100):** clean all the way up, no sheen drop or ripples (user report 2026-10-18; photo to follow). Ceiling >30, so **white production MVS 24 mm³/s** (80% of 30, a floor). White-only; not ported to black. Session 2026-10-18
  - **Correction 2026-10-19:** surface glossy throughout, but the tower is **easier to break above 15mm** (user, snap check; photo reviewed). Strength-based ceiling = 10 + 15 × 1 = **25 mm³/s**, so **white production MVS 20 mm³/s**. Assumes the run used 10→30 step 1 like the other H2C runs. Session 2026-10-19
    > Previously: 24 mm³/s (2026-10-18), from the sheen reading alone. Replaced because strength drops at 15mm.
  > Previously: "⚠ White MVS ceiling not yet read" (2026-10-01).
- Validate each one on a black print before recording a fix.
- **Run A1 (protocol), 2026-10-17:** black, nozzle 255 / **chamber 50** / bed 100, Max flowrate 10→30, cold start. ⚠ **Marginal:** one stall needed a manual resume (reported after the first log). Otherwise: full tower completed, glossy to the top, no heat creep. Against the failed black MVS run (255 / 60 / 100) the only change was the chamber, so **chamber heat confirmed as the cause of the black failure**. Session 2026-10-17
  - Black flow limit at chamber 50 is **above 30 mm³/s** (glossy throughout). Second pass 28→45 planned in Stage D. Polymaker's preset leaves the HF MVS empty; Bambu's generic fallback is 12.
  - ⚠ **Adhesion trade-off:** middle prong(s) lifted at chamber 50; never needed glue at 60. Next: A2 at chamber 55 after a soap wipe of the plate.
  - Gear check not possible on the H2C (cutter cuts above the extruder).
  - A1 tower: ripples near the top on **all 3 prongs** (2 of 3 lifted), so they're not only from lifting. Likely the flow/speed limit approaching (~150 mm/s single wall at 30 mm³/s). Ripple onset height ⚠ TBD; it gives black's practical quality ceiling (10 + height mm³/s).
- **Run A2, 2026-10-17:** black, 255 / **chamber 55** / 100. ❌ **Fail: filament jam error**, less severe than at 60 (filament didn't wrap the extruder). **Black's limit is between 50 (pass) and 55 (fail).** Extruder not physically jammed: white loaded and purged normally afterwards, so 55 is right at the threshold (trips the jam sensor, recovers once cool). Still a fail for unattended prints. Jam timing ⚠ TBD. Session 2026-10-17
  - Protocol margin rule gives a working chamber of **45** (one 5°C step below the first fail). Next: A3 at chamber 45 with glue stick for adhesion, then Stage F long print.
  > Previously: A1 recorded as a clean Pass. Corrected to marginal after the user reported a stall that needed a resume.
- **Run A3, 2026-10-17:** black, 255 / **chamber 45** / 100, Nano Polymer Adhesive. ✅ **Clean pass**, no errors or stalls, glossy throughout; mild waviness near the top edges (flow/speed). Session 2026-10-17
  - **Black working chamber on this H2C: 45°C** (protocol margin rule: one step below the first failure, 50). Chamber results: 60 hard jam / 55 jam error / 50 stall / 45 clean.
  - Adhesive needed at 45 (at 60 none was needed). User wants to avoid adhesive.
  - Bambu Studio user filament preset holding the chamber-45 settings: **NoJam** (named 2026-10-17).
  - **Provisional black MVS at chamber 45:** ripples start at **11mm**, so the quality ceiling is 10 + 11 = **21 mm³/s** and production ~**17 mm³/s** (80%). Sheen never dropped (>30). ⚠ Provisional until Stage C (temp towers at chamber 45) and Stage D (28→45). Some rippling may be thin-wall flex at ~100+ mm/s rather than a true flow limit; multi-wall parts may hold higher. Session 2026-10-17
  - ⚠ **Strong hint of an H2C-specific cause:** the H2D prints black ASA at chamber 60 with the same HF nozzle type and no issues, and both Polymaker presets use chamber 60. Next: check the H2C left hotend fan and heatsink, and swap spools between H2D and H2C. If it's H2C hardware, fix it and rerun at 60, which would remove the adhesive need.
- **Standard 0.6 nozzle trial (H2C left), 2026-10-19:** testing whether a non-HF nozzle stops black jamming at chamber 60.
  - **White**, 255 / chamber 60 / bed 100, Max flowrate 6→20 step 1 (recommended settings, assumed): clean to the top, no sheen change, couldn't be broken. Ceiling **>20**, so production **≥16 mm³/s** (floor); already above Polymaker's 14. Also confirms the nozzle install is good. Session 2026-10-19
  - White re-look (user): **very faint sheen change at 8mm**, glossy otherwise. Sheen ceiling 6 + 8 = **14** (production ~11); strength held through 20 (production ≥16). **White production MVS 14 mm³/s** (user's choice): at most 70% of the strength limit (unbreakable through 20); at the faint sheen change, so slight gloss loss at full speed is possible (cosmetic). Matches Polymaker's preset value. Revisit if black comes in lower (unified profile uses the lower). Session 2026-10-19
  - **Black** on the same settings (standard 0.6, 255 / chamber 60 / bed 100): ❌ **"motor overloaded" error** (assumed extruder; ⚠ confirm). Same feed failure as on HF. **Nozzle type (HF vs standard) ruled out.** Session 2026-10-19
  - Remaining suspects: the H2C toolhead (cooling or extruder) or the black spool/batch. The H2D prints black ASA at chamber 60 fine. Deciding test: print the H2C's black spool on the H2D at chamber 60. Then Bambu support with HMS codes if it's the H2C.
- **Spool finding, 2026-10-21:** the black spool from H2C AMS slot 3 **also jammed on the H2D**, which prints black ASA fine with its own spool. The spool has a **visibly different sheen** from the other spools. **Root cause: that spool (different batch, formulation or product), not the H2C.** Session 2026-10-21
  > Previously: "H2C-specific cause suspected (hotend cooling)" (2026-10-17/19). Withdrawn: the spool fails on both machines.
  - Every black H2C result above (60 hard jam, 55 jam error, 50 stall, 45 pass, NoJam's long-print failure, the standard-nozzle motor overload) was **run on this spool**. Treat them as spool-confounded, not as limits of black Polymaker ASA.
  - NoJam (chamber 45 + adhesive) is **likely unnecessary** with a good spool. ⚠ Confirm: print black from a good spool on the H2C at the stock 60°C chamber, no adhesive.
  - Actions: compare label and lot number with the H2D's good black spool; set the spool aside; if it's Polymaker ASA, report the lot to Polymaker. Drying (70°C, 7h) is optional; the sheen difference points to batch/product, not moisture.
- **Test plan:** `protocols/Polymaker_ASA_H2C_unified.md`. ⚠ Black chamber results were spool-confounded (2026-10-21). Aim is one profile for white and black; split only per that doc's decision rules.
