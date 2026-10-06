;===== Bambu A1 END G-code — MOD 2026-10-06 (snippet, not the full file) =====
; Stock end G-code: machine A1, date 20260513.
; Insert this block between these two stock lines:
;     M621 S255
;     M104 S0 ; turn off hotend
; Purpose: stock turns the heater off right after the last wipe, so the nozzle oozes while cooling
; and the ooze hardens into a blob. Here it cools with the fan at the purge position (X-48.2, off the
; left edge of the bed), then wipes the ooze off while it's still soft.
; ⚠ Not yet run on a printer.

;===== MOD: cool at the purge position, then wipe the cooldown ooze off while still soft =====
G1 X-48.2 F3000            ; purge position, off the left edge of the bed
M106 S255                  ; part fan on to speed cooldown
{if filament_type[initial_no_support_extruder] == "PLA"}
M109 S170                  ; wait while cooling to wipe temp
{else}
M109 S200                  ; PETG/PCTG still soft enough to wipe here
{endif}
G1 X-28.5 F18000           ; wipe
G1 X-48.2 F3000
G1 X-28.5 F18000           ; wipe
G1 X-48.2 F3000
M106 S0
;===== MOD end =====
