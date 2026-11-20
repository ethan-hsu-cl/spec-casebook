# Swipe Collage quirks seen in runs

## KF-001 Tool bar and AI Enhance category tabs scroll sideways
- kind: quirk · platform: android · use: run, ebug · tags: toolbar, ai-enhance, scroll
- source: user, eBug review R1 2026-11-12 (F-15, F-23; inbox I-004); said of Swipe Collage only

The Swipe Collage image tool bar and the AI Enhance category tabs scroll horizontally: 「Delete」 (tool bar) and
「Concert」 (Enhance categories) sit at the far right and are reached by swiping the bar. Swipe a bar to its end
before calling an item missing or clipped.

## KF-002 After pm clear, switch back to the test server
- kind: howto · platform: android · use: run, ebug · tags: setup, server, pm-clear
- source: user, eBug review R1 2026-11-12 (F-46, not a bug; inbox I-005); said of Swipe Collage
- status: superseded by KP-137

`pm clear` puts the app back on its default server. Switch it back to the demo (test) server before going on;
otherwise every Swipe Collage template opens blank and Add Layer › Frame says No connection. On 20.19.0 the debug
dialog (KP-131) lists a 「Test server」 switch.
