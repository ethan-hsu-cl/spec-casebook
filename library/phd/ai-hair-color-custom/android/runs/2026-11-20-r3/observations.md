# Observations — R3 (Pixel 8a, 20.19.0 / 90201901)

- **O-1 (R3-c, closest TC-019 / TC-024 / TC-032).** Same build 90201901 as R2 on the S23, but the Custom panel behaves
  differently on the Pixel 8a (CMS / remote config or device?): colour rows are drawn dimmed/disabled before a style
  (R2: hidden); Solid greys the Highlight row (R2: hid it — now fails REQ-009 / KF-003); no ⌄ collapse key (R2 had
  `custom_collapse_btn`); no 「Both Base Color and Highlight Color are required.」 hint (R2 showed it); a palette pick
  adds a ringed custom circle after the wheel (R2: none; one custom slot, a second pick replaces it). Evidence
  screenshots/TC-019_panel.png, TC-024_solid.png, TC-032_after.png, TC-035_after.png.
- **O-2 (R3-c, closest TC-035).** First eyedropper sample on the hair edge (276,780, screen #3B312F) set the palette to
  near-white (top-left, hue 16); the second sample (312,840) read the hair correctly (hue 3, dark). R2 saw a similar
  odd first reading. screenshots/TC-035_sampled.png, TC-035_hair.png.
- **O-3 (R3-d, closest TC-078).** The Soft Black template generation took 34.4 s and 36.0 s on the Pixel 8a (Test
  Server, 10:54–10:56), against 16.2 s for the same template on the S23 in R2; Custom generations stayed 41.8–54.9 s.
  Server timing (KP-070) or a changed template model; TC-078 is queued as a question. screenshots/TC-078_result*.png.
- **O-4 (R3-d, closest TC-056).** After ✓ (TC-056) the new Edit Room's Home button asks 「Discard changes?」 /
  「All your existing changes will be lost.」; 「Discard」 went to the Launcher (the result stays in My AI Artwork).
  The Edit Room opened from ✕ / Back (TC-079 / TC-088) left by Home with no dialog. screenshots/r3d_editroom_home_discard.png.
- **O-5 (R3-d, script).** During a regeneration the button keeps the text 「Retry」 (disabled), so `waitfor Retry`
  returns at once; R3-d waited on the log's `AIHairColor_Generate_Status` line instead (poll the live logcat).
- **O-6 (R3-e, closest TC-064, script).** A `lbl Dip-dye` in a `do` failed because the style was scrolled off the
  left edge of the Style row, and the next Generate re-ran the still-selected Bangs (11:15:19, chip 1910 -> 1904,
  log succeed 11:16:08): one extra generation, not a case. Afterwards each style was selected after dragging the Style
  row into view and checked with `els color_name` (selected) before Generate. screenshots/O-6_bangs_retry.png.
- **O-7 (R3-e, closest TC-062 … TC-068).** Every Custom generation logs the same Mixpanel style
  `Style_010_Custom_HairColor_gpt-image-2.5-sunburst`, whichever Custom style (Ombre, Solid, Split-dye …) was chosen;
  the event does not say which pattern was generated. Waits 45.0–69.2 s (Babylights 69.2 s).
