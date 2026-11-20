# TR261118-0070 verify plan — PHD-A 20.19.0.v202611181947 (R5), 2026-11-19

Scope: all 21 bugs on the TR's verify list (PHD-A rule: every bug, whoever created it; all 21 are WILLY_WU's).
Testers on the TR: WILLY_WU, BIAGGI_LI. No QA Report on the TR yet (Pass 0 / Fail 0 / Not yet verified 21 at 14:45).

Device: Samsung Galaxy S23 (SM-S9110, adb RFCW2198L7B), Android 16. App 20.19.0 versionCode 90201901, installed
2026-11-19 10:30 from the TR's APK (creative-reel REQ-013); About: Version 20.19.0, SR PHA261029-01. Test Server.
Start state: not signed in, Free, 215 credits (Mine, 14:48).

Bug bodies: `bugs-raw.txt` (old-ASP bodies + headers), `bugs-bodies.md` (IF3 bodies from the filing ledgers),
`rd-notes.json` (RD resolve notes).

## What each bug needs (today's spec)

| Bug | Area | RD says | Check | Cost |
| --- | --- | --- | --- | --- |
| PHA252025-0128 | Artistic Avatar result page | added credit number on result page | result page shows remaining credits | 1 generation |
| PHA262026-0361 | AI Replace › My AI Artwork › Create More | deep link now resets the source image | after picking another AI Replace artwork, Create More / Replace More opens AI Replace with THAT image | 1 generation if fewer than 2 AI Replace artworks |
| PHA262026-0362 | My AI Artwork › AI Replace tab | ux modify | button reads 「Replace More」 | none |
| P0057 | Batch AI Enhance, Home mid-run | pauses in background, resumes | 12 photos, Home at ~4/12, 30 s, back: continues, all complete | free (R-004) |
| P0058 | Batch AI Enhance confirm dialog | Back = Cancel | Back closes 「Enhance 12 photos?」, nothing processed | none |
| P0059 | Batch Discard dialog from Home | Back = Cancel (Keep Editing) | Back closes 「Discard changes?」, edits kept | none |
| P0060 | Batch Square crop All | rounding fixed | saved 16:9 photo is square (also single-photo Crop tab per RD) | none |
| P0084 | Swipe Collage image Lock | "test build not implemented yet" | Lock → 「Image locked」, floating Unlock, cannot drag | none |
| P0085 | Swipe Collage image Removal | "test build not implemented yet" | Removal opens Object Removal room (Premium and Free) | none to open |
| P0089 | Swipe Collage Custom color picker Back | Back = Cancel | Back closes only the picker, colour not applied | none |
| P0097 | Swipe Collage Pages ≡ | drag: 1.1x, 4°, 0.7 alpha | tap ≡ does nothing; drag enlarged + translucent (+ hint per spec) | none |
| P0098 | Swipe Collage Pages controls 5–10 pages | RD note is about another bug (pasted wrong) | every ≡ and ••• reachable at 5 and 10 pages | none |
| P0099 | Swipe Collage 1 page / 1 image | plurals | 「1 page」 on cards, 「1 image」 on one-page Save & Share | none |
| P0112 | Hair Color Custom, no style | already solved | colour rows disabled before a style | none |
| P0113 | Hair Color palette eyedropper | already solved | eyedropper right of hue slider, picks a photo colour | none |
| P0114 | Hair Color palette Back | already fixed | Back closes only the palette like Cancel | none |
| P0115 | Hair Color collapse | already solved | collapse selects Custom with the colours; outer Generate makes Custom | 1 generation (6) |
| P0117 | Hair Color Custom Intensity | already fixed | Intensity bar at 100 above Retry, panel open and collapsed | shares P0115/P0119 generations |
| P0118 | Hair Color one-time 100% dialog | PM comment: Custom shows the panel first → close → Intensity | dialog appears (after collapsing, per RD) on the first Custom result | shares; one-time state |
| P0119 | Hair Color Custom recall | already solved | after a template result, Custom brings back the Custom result, no charge | 1 template generation (6) |
| P0129 | Reel Creator Preview mask | applied design guideline | mask covers the preview below 「Use Template」 | none |

## Order (one journey per feature segment, one subagent each)

- A. Reel Creator P0129 → AI Replace 0362 / 0361 → Artistic Avatar 0128 (Free; credits 215).
- B. Batch Editing P0058 → P0059 → P0060 → P0057 (Premium by backdoor if AI Enhance needs it; restore Free).
- C. Swipe Collage P0099 → P0098 → P0097 → P0089 → P0084 → P0085 (Free and Premium for Removal).
- D. AI Hair Color P0112 → P0113 → P0114 → Custom generate (P0117 open, P0118 dialog) → collapse (P0117 collapsed,
  P0115 outer Generate) → template result → Custom (P0119). P0118 is one-time state: check it on the first result;
  if the dialog was already dismissed on this install, report it (Hold) instead of clearing app data.

End state to restore: Free (Set to subscriber OFF), Wi-Fi on.
