# Polylite PETG (Standard) — All Machines

**Primary use:** Bambu A1 (Alexactly) + Makerspace MK3.5s  
**Material notes:** Standard non-HF formula. Different product from Polymaker PETG HF — do not conflate. ~50 rolls in Alexactly stock as of mid-2026. Makerspace sponsor material.

---

## Confirmed Profiles

| Machine | Nozzle | Temp (1st/Other) | Bed | MVS | Flow | Retraction | PA | Status | Date |
|---|---|---|---|---|---|---|---|---|---|
| Bambu A1 | 0.6mm | 255°C / 255°C | 70°C | 8mm³/s (Normal) / 6mm³/s (Quality) | 0.95 | 1.5mm @ 45mm/s | Firmware | ✅ | Jun 2026 |
| Prusa MK3.5 CHT | 0.6mm CHT | 255°C | 80°C | 15/17/19 mm³/s (Q/N/D) | ⚠ TBD | ⚠ TBD | 0.044–0.05 | ✅ | Jul 2026 |
| Elegoo Giga | 0.8mm brass | 245°C | 75°C | 18/20/22 mm³/s (Q/N/D) | 1.0 | 0.55mm @ 45mm/s | 0.05 | ✅ | Jul 2026 |

---

## Consistency Notes

- **Temperature:** A1 and MK3.5 CHT both at 255°C. Giga lower at 245°C — different nozzle diameter.
- **MVS:** Giga 0.8mm nozzle has higher ceiling than 0.6mm machines as expected.
- **Flow ratio:** 0.95 on A1. Giga 1.0. MK3.5 CHT pending.
- **PA:** Bambu firmware. Prusa/Giga slicer values. MK3.5 CHT confirmed ~0.05, cross-validated with Giga.

---

## Per-Machine Detail

### Bambu A1 — 0.6mm
- MVS 8mm³/s showed artifacts on reducing elbow. Use 6mm³/s for Quality tier on demanding geometry.
- Black colorway strings worse than white — increase retraction to 1.8–2.0mm for black.
- Z-hop 0.4mm Normal.
- Fan min 30% @ 20s, max 100% @ 5s, overhang 100% @ 10%, prestart 3s, close fan first 3 layers.
- A1 is open-frame — extra layer without fan vs P1S to compensate for faster heat loss.

### Prusa MK3.5 — 0.6mm CHT (Makerspace)
- MVS cliff ~20mm³/s. Tiers 15/17/19 mm³/s Quality/Normal/Draft.
- PA ~0.044–0.05, cross-validated against Giga result of 0.05.
- Retraction pending.
- Sponsor showcase material — not load-bearing production use.

### Elegoo Orangestorm Giga — 0.8mm brass
- MVS cliff ~23mm³/s.
- Tiers: Quality 0.30mm/18mm³/s/75mm/s | Normal 0.40mm/20mm³/s/63mm/s | Draft 0.50mm/22mm³/s/55mm/s.
- Uses same process profiles as PCTG — filament profile differs only.
- Functional part validation pending.
