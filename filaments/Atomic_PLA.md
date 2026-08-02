# Atomic PLA — All Machines

**Primary use:** Cherokee Makerspace (Elegoo Giga)  
**Material notes:** ❌ Current calibration data invalid — temp tower result of 265°C is suspect for PLA. Full recalibration required.

---

## Confirmed Profiles

| Machine | Nozzle | Temp | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Elegoo Giga | 0.8mm brass | ❌ 265°C INVALID | 60°C | ⚠ TBD | ⚠ TBD | ⚠ TBD | ⚠ TBD | ❌ Needs redo | Jul 2026 |

---

## Placeholder Tiers (DO NOT USE IN PRODUCTION)

| Tier | Layer Height | MVS | Speed |
|---|---|---|---|
| Quality | 0.30mm | 23mm³/s | 96mm/s |
| Normal | 0.40mm | 26mm³/s | 81mm/s |
| Draft | 0.50mm | 28mm³/s | 70mm/s |

These are placeholders only. Do not treat as production-ready until recalibration is complete.

---

## ❌ Required Action

Run full temp tower starting at **190–230°C**. Previous result of 265°C is unusually high for PLA and likely invalid. Then run full calibration sequence: MVS → PA → Retraction.

MVS cliff from preliminary test: ~28mm³/s. PA and retraction unknown.
