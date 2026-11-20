# Logs

## KP-140 Mixpanel events are written to logcat
- kind: howto · platform: android · use: analysis, run, ebug · tags: logs, analytics, mixpanel, logcat
- source: i2v-reuse run 2026-11-19-r1 R1-c (TC-037..040; inbox I-008); seen in Image to Video only, filed product-wide because the tag is the app's · verified: 20.19.0.v202611181947 (2026-11-19)

PhotoDirector Android logs every Mixpanel event to logcat under the tag 「[PHD-A][Mixpanel]」: an event with
parameters as 「<Event>:{json}」 (e.g. 「ImageToVideo_Result_Generate:{…"model":"Model_Kling-2.6","from":"artwork_reuse",…}」),
one without as 「logEvent name=<Event>」, and the entry source as 「[setCurFrom] from = …」. A logcat capture
(`device-android.ts … logcat start` / `pull-logs`) is therefore the event log for tracking rows.
