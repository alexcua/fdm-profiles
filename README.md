# FDM Profiles Repository

Calibration reference for Alexactly and Cherokee Makerspace 3D printing fleets.

## What's in this repo

| File/Folder | Purpose |
|---|---|
| `CALIBRATION_MASTER.md` | Narrative history, key learnings, session log |
| `filaments/` | Per-filament profiles — all machines side by side for consistency checking |
| `machines/` | Per-machine profiles — all filaments for a given printer in one place |
| `AGENT.md` | Instructions for AI agents populating and maintaining this repo |

## How to use

**Checking consistency across machines** → use `filaments/` docs. See all machines running the same filament side by side.

**Setting up a specific printer** → use `machines/` docs. See all filament profiles for that machine in one place.

**Understanding calibration history and decisions** → use `CALIBRATION_MASTER.md`.

## Fleet Summary

### Alexactly
| Machine | Nozzle(s) | Primary Filament |
|---|---|---|
| Bambu A1 | 0.6mm | Polylite PETG |
| Bambu P1S | 0.6mm / 0.4mm | Polymaker PETG HF / 3D Fuel PCTG |
| Bambu X1C | 0.6mm | Polymaker PETG HF |
| Bambu X2D | 0.4mm | 3D Fuel PCTG |
| Bambu H2D | 0.6mm HF (both extruders) | 3D Fuel PCTG |
| Bambu H2C | 0.6mm HF (left) / Vortex TBD (right) | 3D Fuel PCTG |
| Prusa XL 5-head | 0.4mm OBX HF (1,2,5) / 0.4mm brass (3,4) | 3D Fuel PCTG |

### Cherokee Makerspace
| Machine | Nozzle(s) | Primary Filament |
|---|---|---|
| Bambu A1 ×2 | 0.4mm | TBD |
| Prusa MK3.5 ×2 | 0.6mm CHT | Polylite PETG / California Matte PETG |
| Prusa MK3.5 ×1 | 0.4mm E3D V6 | Generic |
| Prusa MK3.5 ×2 | 0.6mm Revo (swappable 0.4/0.6/0.8) | Polylite PETG |
| Elegoo Orangestorm Giga | 0.8mm brass | 3D Fuel PCTG / Polylite PETG / Atomic PLA |

## Filament Naming Rules

- **Polymaker PETG** = HF (high flow) formula. Used on X1C, P1S 0.6mm.
- **Polylite PETG** = standard non-HF formula. Used on A1, Makerspace MK3.5s.
- These are distinct products from the same brand. Never conflate them.
- **3D Fuel PCTG** = primary structural filament for Alexactly production parts.

## Calibration Sequence

The sequence is the same regardless of slicer:

1. Temperature tower
2. Max Volumetric Speed (MVS)
3. Pressure Advance (PA)
4. Retraction

**Slicer support:**
- **Bambu Studio** — built-in calibration tools for Bambu machines
- **OrcaSlicer** — built-in calibration tools, works on all machines including Prusa
- **PrusaSlicer** — no built-in calibration features; use OrcaSlicer for Prusa machines

## Status Legend used in docs

- ✅ Confirmed
- ⚠ Pending or needs retest
- ❌ Invalid / do not use

---

## AI Session Startup Prompt

Use this at the start of any new Claude session:

---

> Please read https://github.com/alexcua/fdm-profiles — start with AGENT.md and README.md, then any relevant machine or filament docs. Today I'm working on: [machine, filament, task]

---

All rules and context are in the repo. Just update the last line with what you're doing.

## Updating this Repo with Desktop Commander

Claude can write directly to this repo using Desktop Commander (no local clone needed). At the end of a calibration session, ask Claude to push updates.

**How it works:**
1. Claude clones the repo to `/tmp/fdm-profiles` using `git clone`
2. Reads existing files to understand current state
3. Updates relevant machine and filament docs
4. Commits and pushes back to GitHub

**What Claude needs to push:**
- Your GitHub personal access token must be stored in your Mac keychain, OR
- Run this once in Terminal to cache credentials:
  ```
  git config --global credential.helper osxkeychain
  cd /tmp && git clone https://github.com/alexcua/fdm-profiles.git
  ```
  Enter your GitHub username and a Personal Access Token (PAT) when prompted. macOS will cache it going forward.

**To generate a PAT:**
1. GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Create token with `repo` scope
3. Use as your password when git prompts

**Session end prompt:**
> Please update the fdm-profiles repo with everything we calibrated today. Push to GitHub.

Claude will update machine docs, filament docs, CALIBRATION_MASTER session log, and pending items automatically.
