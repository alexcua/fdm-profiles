# Protocol — Polymaker ASA on Bambu H2C 0.6mm HF (left): one profile for white and black

**Goal:** one Polymaker ASA profile that prints both white and black reliably. Split into separate white and black profiles **only** if the decision rules below say so.

**Why:** with vendor-default conditions (nozzle 255°C, chamber 60°C, bed 100°C), white prints and black does not. Black filament softens and gets squashed at the extruder gear in layer 1. See `filaments/Polymaker_ASA.md` for the evidence.

**Core idea:** black is the limiting colour. **Tune every step on black first, then confirm on white.** A setting is unified only once both colours pass.

---

## 0. Standard conditions — every run

Change **one variable per run**. Everything else stays fixed:

| Item | Standard |
|---|---|
| Slicer / base preset | Bambu Studio, `Polymaker ASA @BBL H2C`, with only the test variable changed |
| Softening temp field | 85°C (realistic value; see filament doc) |
| AMS | Same slot for both colours (AMS 3 slot used so far) |
| Spools | Both dried before the series, using the drying settings in Polymaker's preset |
| **Cold start** | Chamber at room temp and toolhead idle ≥ 30 min before each run. Removes heat soak as a variable. |
| Plate | Same plate, cleaned |
| After every run | Unload and inspect the filament at the extruder-gear position: **clean / flattened / chewed** |

A run **passes** only if:
- the print completes the stage target, **and**
- the filament is clean at the gear.

Slight flattening counts as **marginal** — treat it as a fail when choosing settings.

**H2C note (added after A1, 2026-10-17):** the gear check isn't possible on the H2C. On unload, the cutter cuts the filament above the extruder, so the gear-gripped section stays in the toolhead and is purged on the next load. On the H2C a run passes if it completes the stage target with no under-extrusion or heat creep.

---

## Stage A — Find black's working window (chamber, then bed)

**Test object:** Bambu Studio Max flowrate, 10–30 mm³/s, step 1. It reproduces the failure in layer 1, so pass/fail is fast.
**Target:** black completes ≥ 10mm of tower height with the filament clean at the gear.

| Run | Colour | Chamber | Bed | Nozzle | Next |
|---|---|---|---|---|---|
| A1 | Black | 50 | 100 | 255 | Pass → A2. Fail → A3 |
  > Previously logged as Pass (2026-10-17); changed after the user reported the stall.
| A2 | 2026-10-17 | Black | 55 | 100 | 255 | ⚠ TBD | **Fail**: filament jam error. Less severe than at 60 (didn't wrap the extruder). Extruder not physically jammed: white loaded and purged normally afterwards. **Threshold**: softening enough to trip the sensor, then recovering. Jam height/time ⚠ TBD. | Not checkable (H2C cutter) | Not logged |
| A3 | 2026-10-17 | Black | 45 | 100 | 255 | Yes | **Pass**: full tower, no errors or stalls. Glossy throughout; mild waviness near the top edges (flow/speed). Nano Polymer Adhesive on the plate. | Not checkable (H2C cutter) | Received |
| A2 | Black | 55 | 100 | 255 | Finds the upper edge (pass or fail) → Stage B |
| A3 | Black | 45 | 100 | 255 | Pass → Stage B. Fail → A4 |
| A4 | Black | 45 | 90 | 255 | Pass → Stage B. Fail → **stop**: check hardware (toolhead fan, extruder, nozzle seating) before more runs |

**Working point:** highest passing chamber temp with **one 5°C step of margin** below the first failing value. Example: 55 fails, 50 passes → use 45 if 45 passes Stage B.

---

## Stage B — Does white tolerate black's working point?

Lower chamber heat can cause ASA to warp and split layers. Check that the cooler settings don't break white.

| Run | Colour | Test | Pass if |
|---|---|---|---|
| B1 | White | Max flowrate 10–30 at working point | Completes ≥ 10mm, filament clean |
| B2 | White | Warp test: large flat part, ≥ 150mm long, sharp corners | No corner lift, no layer splits |
| B3 | Black | Same warp test | Same |

If B2 or B3 warps, try a single fix (brim **or** draft shield), then rerun **both** colours.

---

## Stage C — Temp tower at the working point

The 255°C result was found at chamber 60. A cooler chamber changes the thermal setup, so re-check it (AGENT.md: tower at production chamber temp).

| Run | Colour | Test |
|---|---|---|
| C1 | Black | Temp tower 230–270, step 5, at working point |
| C2 | White | Same |

**Unified temp:** one value clean on both towers. If both pick 250–255, choose 255. If neither tower has a clean block in common, see decision rules.

---

## Stage D — MVS at the unified temp

| Run | Colour | Test |
|---|---|---|
| D1 | Black | Max flowrate 10–30, step 1. If clean at the top, rerun 25–45. |
| D2 | White | Same |

**Unified MVS** = 80% of the **lower** of the two ceilings. Record both ceilings.

---

## Stage E — Retraction

- **E1:** retraction tower in black. Black strings worse in this fleet (see CALIBRATION_MASTER Key Learnings).
- **E2:** confirm the E1 value on white.
- Keep it short (current value is 0.4mm), since a long retraction worsens heat creep.

PA: firmware (Bambu). Nothing to test.

---

## Stage F — Real-world validation (heat-soak check)

| Run | Colour | Test | Pass if |
|---|---|---|---|
| F1 | Black | Production-like print, ≥ 2–3h, large footprint, at the unified profile | Completes; filament clean at gear on unload |
| F2 | White | Same | Same |

Stage F is the only test of long-run heat soak. The profile is ✅ only after F1 and F2 pass.

---

## Decision rules — when to split white and black

**Keep one profile** unless one of these happens:

1. **No shared chamber/bed:** no setting from Stage A that black passes also passes white's warp test in Stage B (after one brim/shield attempt).
2. **Temp mismatch:** the black and white towers' clean windows don't overlap, or they're > 5°C apart.
3. **MVS cost:** white's ceiling is > 20% above black's **and** white production parts actually need that speed.
4. **Retraction mismatch:** no single retraction value is clean on both colours.

**If you split:**
- Use the white settings as the base preset.
- Make the black preset inherit from it and override **only** the failing setting(s).
- Record the reason in the filament doc, per rule 9 (no porting between colourways).

---

## Optional diagnostic (doesn't affect the decision)

**Cantilever sag test:** a 2" piece of each colour, matched diameter (calipers), spool curl facing sideways, 5–10g weight on the end. Bend it once at room temp, then after 30 min a few mm above the 100°C bed. Photograph against a ruler at 0, 10 and 30 min.

This separates "black is softer" from "black gets hotter".

---

## Run log

> ⚠ **2026-10-21:** all black runs below used one bad spool (H2C AMS slot 3; also jams on the H2D; different sheen). The chamber results reflect that spool, not black Polymaker ASA in general. Next: rerun A at chamber 60 with a good spool.

Copy one row per run. Log each result in the three repo docs (filament, machine, CALIBRATION_MASTER) with `Session <date>`.

| Run | Date | Colour | Chamber | Bed | Nozzle | Cold start | Result (height / stage target) | Filament at gear | Photo |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 2026-10-17 | Black | 50 | 100 | 255 | Yes | **Pass**: full tower (10→30) completed, glossy to the top, no heat creep. Middle prong(s) lifted from the bed. | Not checkable (H2C cutter, see note) | Not logged |
