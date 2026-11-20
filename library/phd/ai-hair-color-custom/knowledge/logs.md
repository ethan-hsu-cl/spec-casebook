# Logs (AI Hair Color Custom)

## KF-010 Every Custom generation logs the same Mixpanel style
- kind: fact · platform: android · use: analysis, run, ebug · tags: logs, mixpanel, custom, style
- source: run 2026-11-20-r3 O-7 (Pixel 8a, 12 Custom generations) · verified: 20.19.0 (90201901) (2026-11-20)

Whichever Custom style is generated (Ombre, Solid, Split-dye …), the Mixpanel style is
「Style_010_Custom_HairColor_gpt-image-2.5-sunburst」; a template logs its own (「Style_6001_Solid-Soft-Black_ChatGPT」,
is_customize FALSE). The event cannot tell which Custom pattern ran (KP-140 for the log tag).
