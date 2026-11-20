# Reel Creator log lines

## KF-001 The picker's content check is online and logged
- kind: fact · platform: android · use: run, ebug · tags: picker, content-check, logs, nsfw, celebrity
- source: run 2026-11-17-r1 O-6 and addendum (TC-049, TC-050, TC-136) · verified: 20.19.0 (90201901) (2026-11-18)

Each photo ticked in the Reel Creator picker is checked online for NSFW and celebrity; a failure logs
`LibraryPickerActivity: [startReelCreatorContentCheck] <id> failed: NSFW|CELEBRITY`. A content failure and a size
failure get the same dimmed tile and yellow 「!」 with no message, so only this line tells them apart (size failures
log no content-check line). `<id>` is not the MediaStore id and changes between sessions: identify the photo by the
tap, not the id.

## KF-002 Photos upload while they are picked
- kind: fact · platform: android · use: run · tags: upload, picker, generate, logs, network
- source: run 2026-11-17-r1 O-11, TC-143 · verified: 20.19.0 (90201901) (2026-11-18)

Each ticked photo is uploaded at once (`uploadFile: true` lines as photos are picked); at 「Generate」 the job's
UploadFile step lasts about 1 s before Apply. To cut the network 「while the photos upload」, trigger on the device:
`adb shell "input tap …; logcat -T 1 | grep -m1 'column value: UploadFile'; svc wifi disable"`. Cutting Wi-Fi in
the same call as the tap is too early (「Network Error」 before the credit check, no job).
