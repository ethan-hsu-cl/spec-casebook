# Swipe Collage decisions: what not to assert

## KF-003 No translations yet on 20.19.0
- kind: decision · platform: android · use: analysis, run, ebug · tags: locale, translation, version
- source: user, eBug review R1 2026-11-12 (F-47; inbox I-006)

On 20.19.0 the Swipe Collage translations are not in: English strings in other app languages are expected, not a
bug. A separate test runs once they land.

## KF-004 Test Server template set is temporary
- kind: decision · platform: android · use: analysis, run, ebug · tags: templates, server, version
- source: user, eBug review R1 2026-11-12 (F-48; inbox I-006)

The Test Server's Swipe Collage template set is temporary: fewer templates than the spec's 20 is expected on
20.19.0, not a bug.
