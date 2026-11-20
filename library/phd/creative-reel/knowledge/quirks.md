# Reel Creator quirks seen in runs

## KF-003 Paging the template Preview needs a fast swipe
- kind: quirk · platform: android · use: run · tags: preview, swipe, adb
- source: run 2026-11-17-r1 O-4 (S23) · verified: 20.19.0 (90201901) (2026-11-18)

A slow multi-step `fingerdrag` does not page the template Preview; `adb shell input swipe <x> <y1> <x> <y2> 250`
does. Preview demos open muted; with the phone's media volume at 0, read mute from the player's state in
`dumpsys audio`, not by ear.

## KF-004 Picker gestures and scroll position
- kind: quirk · platform: android · use: run · tags: picker, drag, scroll
- source: run 2026-11-17-r1 O-7 (S23) · verified: 20.19.0 (90201901) (2026-11-18)

A `drag` on the picker grid is sometimes taken as a tap and ticks or unticks a photo, and a tap right after a fling
can miss: read the counter after every drag. The picker keeps its grid scroll position between openings and a drag
toward the top may not reach it; choose 「All」 again in the album list to go back to the top.
