# Quirks (AI Hair Color Custom)

## KF-007 The Custom panel differs by device on the same build
- kind: quirk · platform: android · use: analysis, run, ebug · tags: custom, panel, device, remote-config
- source: run 2026-11-20-r3 O-1 (Pixel 8a) against run 2026-11-17-r2 O-9, O-11 (S23) · verified: 20.19.0 (90201901) (2026-11-20)

Build 90201901 draws the Custom panel differently on the two phones (remote config or device, not known). Pixel 8a:
colour rows dimmed and disabled before a style, Solid greys the Highlight row, no ⌄ collapse key, no hint 「Both Base
Color and Highlight Color are required.」, a palette pick adds a ringed custom circle after the wheel. S23 (R2): rows
hidden before a style, Solid hides the Highlight row, ⌄ (`custom_collapse_btn`) and the hint shown, no added circle.
Record the phone with every panel result; rulings (KF-003) stay the expected behaviour on both.

## KF-008 During a regeneration the button still reads 「Retry」
- kind: quirk · platform: android · use: run · tags: generate, retry, wait, script
- source: run 2026-11-20-r3 O-5 (Pixel 8a) · verified: 20.19.0 (90201901) (2026-11-20)

While a regeneration runs the button keeps the text 「Retry」 (disabled), so a wait for 「Retry」 returns at once. Wait on
the live logcat line `AIHairColor_Generate_Status` instead.

## KF-009 The first eyedropper sample can read the wrong colour
- kind: quirk · platform: android · use: run · tags: eyedropper, palette, custom
- source: run 2026-11-20-r3 O-2 (Pixel 8a); a similar first reading in run 2026-11-17-r2 (S23) · verified: 20.19.0 (90201901) (2026-11-20)

The first eyedropper sample on the hair edge set the palette near-white although the screen showed dark hair; a second
sample inside the hair read it correctly. Not filed; sample well inside the hair and check the palette before Done.
