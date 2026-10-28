# California Filament PETG Matte — All Machines

**Primary use:** Cherokee Makerspace (sponsor material — showcase/demo only, not load-bearing production)  
**Material notes:** Matte texture is cooling-limited, not flow-limited. MVS ceiling is determined by when the matte surface transitions to gloss from heat soak, not by extrusion failure.

---

## Confirmed Profiles

| Machine | Nozzle | Temp | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Prusa MK3.5 CHT | 0.6mm CHT | 220°C | 80°C | 10–12mm³/s | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ Partial | 2026-08-02 |
| Bambu A1 (Makerspace) | 0.4mm | 225°C (black) | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | Firmware | ⚠ In progress (temp done) | Session 2026-10-28 |

---

## Notes

- Temp tower confirmed 220°C. Lower than standard PETG due to matte additive formulation.
- MVS conservative at 10–12mm³/s — cooling-limited, not flow-limited. Quality good to ~20mm height; matte surface holds to ~10mm before transitioning to gloss from heat soak. Gloss/rough-top/blobbing at height are all one cooling story, not a flow problem.
- PA UNCONFIRMED. PA pattern failed repeatedly on first-layer adhesion. Dropping Z offset did NOT resolve it — subsequent reprints lifted off the bed and never completed. Bed adhesion on the single-layer pattern is the open blocker. Note: PETG on MK3.5 direct drive lands ~0.04 if a working placeholder is needed; material is non-critical so PA precision is low priority.
- Retraction pending.
- **California Filament PETG Matte (black), A1 0.4 (Makerspace; machine ID ⚠ TBD), temp tower 240→210, 2026-10-28** (photos reviewed; run while fixing the 0.4 nozzle): 240 drooping ledge, layer separation on the overhang, soft numerals; 235 blobby numerals, fine strings; 230 clean cutout, a few hair strings; **225 cleanest** (clean cutout and spike, crisp numerals, clean overhang); 220 minor wisps, slight edge curl; 215–210 heavy strings/blobs in the cutout. **225°C** (user: 220–225 is normal for this matte PETG). Overhang outer edge curls a little at every temp (cooling, not temp). ⚠ Layer adhesion not visible in photos; hand snap test 220/225/230 suggested. Session 2026-10-28
- Finish tuning pending: fan + minimum layer time to push the ~10mm gloss transition higher. Now that parts are non-load-bearing, fan can be used freely (no adhesion-gate needed).
- Sponsor material for Cherokee Makerspace — calibration goal is clean showcase prints, not production performance.

---

## ⚠ Pending

- Confirm PA value
- Confirm retraction distance and speed
- Confirm flow ratio
