#!/usr/bin/env python3
"""Enforce the AGENT.md / CLAUDE.md rules on profile data.

Default: checks only what is staged for commit (run by .githooks/pre-commit).
--all:   audits every profile table row in the repo (legacy issues included).

Exit code 1 if any error is found.
"""
import datetime
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date.today()

PROVENANCE = re.compile(r"\b(Session|Imported) (\d{4}-\d{2}-\d{2})\b")
ANY_DATE = re.compile(r"\b(Session|Imported) (\S+)")
MEASURED = re.compile(r"\d+(\.\d+)?\s*(°C|mm³/s|mm\b)|✅")
PA_OK = re.compile(r"^(Firmware|⚠.*|TBD|—|-)$", re.I)
STATUS_OK = re.compile(r"[✅⚠❌]")
IDENTITY_COLS = {"machine", "nozzle", "filament", "status", "source", "date"}
# Bambu machines whose PA is firmware-handled (AGENT.md "Pressure Advance" table).
BAMBU_FIRMWARE_PA = ("X1C", "P1S", "A1", "X2D", "H2D", "H2C")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_tables(text):
    """Yield (lineno, header_cells, row_cells, raw) for rows of tables with a Status column."""
    lines = text.splitlines()
    header = None
    for i, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            header = None
            continue
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
            continue
        if header is None:
            header = cells(line)
            continue
        if any(h.lower() == "status" for h in header):
            yield i, header, cells(line), line


def is_bambu_firmware(path, header, row):
    if path.startswith("machines/Bambu_"):
        model = path.split("_", 1)[1].removesuffix(".md")
        return model in BAMBU_FIRMWARE_PA
    if path.startswith("filaments/") and header and header[0].lower() == "machine":
        m = re.match(r"Bambu (\S+)", row[0])
        return bool(m) and m.group(1) in BAMBU_FIRMWARE_PA
    return False


def check_row(path, lineno, header, row, raw, errors):
    where = f"{path}:{lineno}"
    if len(row) != len(header):
        errors.append(f"{where}: row has {len(row)} cells, header has {len(header)}")
    if any(c == "" for c in row):
        errors.append(f"{where}: empty cell — use '⚠ TBD' (AGENT.md: never leave a field blank)")
    status = [c for h, c in zip(header, row) if h.lower() == "status"]
    if status and not STATUS_OK.search(status[0]):
        errors.append(f"{where}: Status must contain ✅, ⚠ or ❌")
    values = " | ".join(c for h, c in zip(header, row) if h.lower() not in IDENTITY_COLS)
    if MEASURED.search(values) and not PROVENANCE.search(raw):
        errors.append(f"{where}: row has values but no 'Session YYYY-MM-DD' / 'Imported YYYY-MM-DD' source tag")
    for kind, date in ANY_DATE.findall(raw):
        try:
            d = datetime.date.fromisoformat(date)
        except ValueError:
            errors.append(f"{where}: '{kind} {date}' is not a YYYY-MM-DD date")
            continue
        if d > TODAY:
            errors.append(f"{where}: '{kind} {date}' is in the future")
    if is_bambu_firmware(path, header, row):
        for h, c in zip(header, row):
            if h.upper() == "PA" and not PA_OK.match(c):
                errors.append(f"{where}: Bambu firmware handles PA — store 'Firmware', not '{c}'")


def check_naming(path, lineno, line, errors):
    if "Polylite PETG HF" in line:
        errors.append(f"{path}:{lineno}: 'Polylite PETG HF' does not exist — HF is Polymaker PETG")
    if re.search(r"Polymaker PETG(?! HF)", line):
        errors.append(f"{path}:{lineno}: write 'Polymaker PETG HF' in profile docs (distinct from Polylite PETG)")


def staged_changes():
    """Return {path: (added_linenos, removed_lines, added_lines)} for staged .md files."""
    out = git("diff", "--cached", "-U0", "--no-color", "--", "*.md")
    changes, path, new_no = {}, None, 0
    for line in out.splitlines():
        if line.startswith("+++ "):
            path = None if line.endswith("/dev/null") else line[6:]
            if path:
                changes[path] = (set(), [], [])
        elif line.startswith("@@"):
            new_no = int(re.search(r"\+(\d+)", line).group(1))
        elif path and line.startswith("+") and not line.startswith("+++"):
            changes[path][0].add(new_no)
            changes[path][2].append(line[1:])
            new_no += 1
        elif path and line.startswith("-") and not line.startswith("---"):
            changes[path][1].append(line[1:])
    return changes


def is_profile(path):
    return path.startswith(("machines/", "filaments/"))


def main():
    audit = "--all" in sys.argv
    errors = []

    if audit:
        files = [p for p in git("ls-files", "*.md").split() if is_profile(p)]
        for path in files:
            text = (ROOT / path).read_text()
            for lineno, header, row, raw in parse_tables(text):
                check_row(path, lineno, header, row, raw, errors)
            for lineno, line in enumerate(text.splitlines(), 1):
                check_naming(path, lineno, line, errors)
    else:
        changes = staged_changes()
        data_touched = {"machines": False, "filaments": False}
        for path, (added, removed, added_lines) in changes.items():
            if not is_profile(path):
                continue
            text = git("show", f":{path}")
            for lineno, header, row, raw in parse_tables(text):
                if lineno in added:
                    check_row(path, lineno, header, row, raw, errors)
                    data_touched[path.split("/")[0]] = True
            for lineno, line in enumerate(text.splitlines(), 1):
                if lineno in added:
                    check_naming(path, lineno, line, errors)
            if any(l.lstrip().startswith("|") for l in added_lines + removed):
                data_touched[path.split("/")[0]] = True
            # Never silently overwrite a confirmed value.
            if any(l.lstrip().startswith("|") and "✅" in l for l in removed):
                if not any("Previously:" in l or "❌" in l for l in added_lines):
                    errors.append(f"{path}: a ✅ row was changed/removed without a '> Previously: …' note or ❌ marker")

        # Machine and filament docs move together, with the master log.
        if any(data_touched.values()):
            staged = set(changes)
            if not any(p.startswith("machines/") for p in staged):
                errors.append("profile data changed but no machines/ doc is staged — update both sides")
            if not any(p.startswith("filaments/") for p in staged):
                errors.append("profile data changed but no filaments/ doc is staged — update both sides")
            if "CALIBRATION_MASTER.md" not in staged:
                errors.append("profile data changed but CALIBRATION_MASTER.md (session log / pending) is not staged")

    for e in errors:
        print(f"✗ {e}")
    if errors:
        print(f"\n{len(errors)} issue(s). See AGENT.md and CLAUDE.md.")
        return 1
    print("✓ fdm-profiles rules check passed" + (" (full audit)" if audit else " (staged changes)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
