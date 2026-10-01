# CLAUDE.md — fdm-profiles

Calibration reference for the Alexactly and Cherokee Makerspace 3D printer fleets. This is a data repo, not code: every edit is a claim about a real physical test.

**`AGENT.md` is the canonical rulebook. Read it before editing anything.** This file restates the rules that matter most, adds what is specific to Claude Code, and explains how the rules are enforced. If the two files ever disagree, follow `AGENT.md` and point out the conflict to the user.

---

## Hard rules

1. **Three-file sync.** A calibration change touches the `machines/` doc, the `filaments/` doc, *and* `CALIBRATION_MASTER.md` (session log row + pending table + "Last updated"). Never update one side only.
2. **Provenance tag on every row with values:** `Session YYYY-MM-DD` (physical test observed live) or `Imported YYYY-MM-DD` (from memory, notes or recall — unverified).
3. **Session date = the day the test happened, not the day of the commit.** Claude Code cannot search past chats (`conversation_search` is not available here), so:
   - Test results shared in *this* conversation → `Session <today>`.
   - Anything from an earlier day → ask the user for the date. If they don't know, use `Imported <today>`.
   - Never guess a Session date.
4. **Never overwrite silently.** Mark the old value ❌ or add `> Previously: [value] ([date]) — replaced because [reason]` under the row. Exception: a ⚠ pending value may be replaced by a ✅ confirmed one.
5. **Never leave a cell blank.** Use `⚠ TBD`.
6. **Status on every row:** ✅ Confirmed / ⚠ Pending / ❌ Invalid. A row with any ⚠ TBD calibration step is ⚠ overall, even if some values are confirmed.
7. **Bambu PA = `Firmware`.** Applies to X1C, P1S, A1, X2D, H2D and H2C. Store a numeric PA only for Prusa and Elegoo machines.
8. **Naming:**
   - **Polymaker PETG HF** (high flow) and **Polylite PETG** (standard) are different products. Always write "Polymaker PETG HF" in full.
   - **Polymaker ASA** and PolyLite ASA are the same product (unlike PETG). Always write "Polymaker ASA".
   - For any other Polymaker line, record the exact product name from the spool. If it's unclear, ask before writing.
9. **Values don't transfer.** Never port MVS, temp or retraction between nozzle sizes, nozzle types (CHT, Revo, HF, brass, Vortex), machine models or colorways. Write "may apply to X — unverified" instead.
10. **Calibration order:** Temp → MVS → PA → Retraction. Don't record a later step as ✅ while an earlier one is ⚠.
11. **Production MVS = 80% of the tested ceiling**, unless the user says otherwise. Record both the ceiling and the production value.

## Reviewing test photos

When the user shares a tower photo:
- Check the orientation from the printed labels. OrcaSlicer temp towers put the hottest block at the bottom.
- Give a per-block verdict (stringing, overhang curl, bridging, surface, numeral crispness) and say plainly whether the photos support the user's pick.
- Say what a photo *can't* show, e.g. layer adhesion and strength, and suggest the test that would show it (snap test).

## Enforcement — `scripts/check.py`

- **Pre-commit hook:** `.githooks/pre-commit` runs `python3 scripts/check.py` on staged changes and blocks the commit if a rule is broken. It checks rules 1, 2, 4, 5, 6 and 7, the naming rule, future dates, and column counts.
- **One-time setup in a fresh clone:** `git config core.hooksPath .githooks`. Clones made elsewhere (e.g. `/tmp` via Desktop Commander) don't have the hook, so run the script manually before every commit.
- **Full audit:** `python3 scripts/check.py --all`. It reports legacy issues too.
- **Legacy debt:** the audit currently reports untagged older rows and a few malformed rows. Don't "fix" these by inventing tags. Raise them with the user and reconcile them per `AGENT.md`.
- **Don't bypass the hook:** never use `git commit --no-verify` unless the user explicitly approves it for that commit.
- **When the checker is wrong:** if it gives a false positive, fix the checker in a separate commit and explain why.

## Git

- Commit when the user asks. **Never push without explicit approval.** A handoff request counts as approval.
- Commit message style follows the history: `<Machine> <nozzle> <Filament>: <what changed>`, e.g. `H2C 0.6HF Polymaker ASA: temp tower 255°C`.
- Remote: `github.com/alexcua/fdm-profiles`, branch `main`.
