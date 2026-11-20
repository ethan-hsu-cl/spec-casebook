# Flows and quirks

## KF-007 The intro shows at every entry until 「Don't show again」
- kind: fact · platform: android · use: run · tags: intro, entry
- source: i2v-reuse run 2026-11-19-r1 R1-setup, TC-015, TC-028, O-4 · verified: 20.19.0.v202611181947 (2026-11-19)

AI Videos › Image to Video and a fresh 「Create More」 show the 「Image To Video」 intro (「Try now」) and a 「Steps」 page
(「Continue」) at every entry while 「Don't show again」 is not tapped. A Create More reached from the room's history
button skipped it (activity reuse), and Reuse never shows it. 「Don't show again」 is one-way state.

## KF-008 Back from a Custom room follows the activity stack
- kind: quirk · platform: android · use: analysis, run, ebug · tags: back, navigation, reuse, create-more
- source: i2v-reuse run 2026-11-19-r1 O-3 (TC-010, TC-020, TC-043), O-4 (TC-028) · verified: 20.19.0.v202611181947 (2026-11-19)

‹ or system Back in a room opened by Save & Share 「Reuse」 returns to My AI Artwork › Image to Video, not to Save &
Share. A room opened by 「Create More」 after AI Videos › Image to Video › history button › Reuse › ‹ went back to the
Launcher's AI Videos tab. Note the path that led to a room before judging its Back.

## KF-009 First tap in a reused prompt selects all of it
- kind: quirk · platform: android · use: run · tags: prompt, keyboard, reuse
- source: i2v-reuse run 2026-11-19-r1 O-5 (TC-032, TC-045) · verified: 20.19.0.v202611181947 (2026-11-19)

The first tap into the prompt box of a reused room selects the whole prompt; a Backspace then deletes all of it. Tap
again to place the cursor before editing.

## KF-010 Reuse draws the room rotated for a frame or two
- kind: quirk · platform: android · use: run, ebug · tags: reuse, transition, layout
- source: i2v-reuse run 2026-11-19-r1 O-2 (TC-010, recording frames 3–4) · verified: 20.19.0.v202611181947 (2026-11-19)

On 「Reuse」 the Custom room is drawn landscape (rotated 90°) for one or two frames before it settles portrait. Only
a screen recording shows it.
