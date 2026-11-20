# Image to Video models (Custom tab)

## KF-001 Default model is Kling 3.0, and the room keeps its last state
- kind: fact · platform: android · use: analysis, run, ebug · tags: model, default, custom, create-more
- source: i2v-reuse run 2026-11-19-r1 R1-setup, TC-022, TC-028 (Pixel 8a, Test Server) · verified: 20.19.0.v202611181947 (2026-11-19)

The Custom tab's default model on 20.19.0 is 「Kling 3.0」 (5s, Standard, Generate Background Sound Off: 30 credits).
「Create More」 opens on Kling 3.0 every time, also after a Reuse room (R-032). AI Videos › Image to Video, by
contrast, keeps the last model, photo and prompt after Generate → ‹.

## KF-002 Prompt limits per model on 20.19.0
- kind: decision · platform: android · use: analysis, run, ebug · tags: prompt, limits, model
- source: i2v-reuse run 2026-11-19-r1 R1-setup (each model's counter), TC-032 · verified: 20.19.0.v202611181947 (2026-11-19)

Kling 4.0 3000; Kling 3.0 / 2.6 / 2.5 Turbo / O1 / O3 and Happy Horse 1.1 2500; Pixverse V6, Vidu Q3, Vidu Q2 2000;
Veo 3.1 4000; Vidu Q4, Wan 2.7 5000; Seedance 2.0 / 2.5, Gemini Omni Flash 1.2, Wan 3.0 20000. No model has the PM's
「Android 上限 500」 (Q-7). Over a limit: counter 「2129/2000」 with the number red, 「Description exceeds 2000 character
limit.」 in red under the box, no red outline, 「Generate」 disabled. Version-bound (KP-064).

## KF-003 Start / End is off for Vidu Q4 and Happy Horse 1.1
- kind: fact · platform: android · use: analysis, run · tags: model, start-end
- source: i2v-reuse run 2026-11-19-r1 R1-setup · verified: 20.19.0.v202611181947 (2026-11-19)

「Specify Video Start / End」 is disabled for Vidu Q4 and Happy Horse 1.1; the other models on 20.19.0 offer it.

## KF-004 Settings each model offers
- kind: fact · platform: android · use: analysis, run · tags: model, duration, quality, sound
- source: i2v-reuse run 2026-11-19-r1 R1-setup, TC-021 · verified: 20.19.0.v202611181947 (2026-11-19)

Duration: Veo 3.1 4/6/8; Vidu Q3 4/8/16; Vidu Q2, Wan 2.7 5/8; Kling 3.0 / O3 / 4.0, Seedance, Pixverse V6, Happy
Horse 1.1, Vidu Q4 5/10/15; Kling 2.6 / 2.5 Turbo / O1, Gemini Omni Flash 1.2 5/10. Kling 2.6 offers only 「Pro」,
Gemini only 「Standard」. The sound row is 「Generate Background Sound」 (Off / On, ⓘ). Switching models keeps what the
new model supports and takes its defaults for the rest.

## KF-005 No model refuses a real-person photo on 20.19.0 Test Server
- kind: quirk · platform: android · use: analysis, run · tags: model, real-person, test-data
- source: i2v-reuse run 2026-11-19-r1 R1-setup (all 18 models given a face photo, Premium), TC-034 Blocked · verified: 20.19.0.v202611181947 (2026-11-19)

None shows 「The photo you uploaded includes a real person, which isn't supported by the selected model.」 at Generate,
though the string is in the APK. Rows that need the message are Blocked test-data until a model refuses one (Q-12).

## KF-006 Test Server jobs can fail with External Error 4000 / 4001
- kind: quirk · platform: android · use: run, ebug · tags: failure, server, refund
- source: i2v-reuse run 2026-11-19-r1 R1-setup (Kling 2.5 Turbo with Start / End; Kling 4.0 probe) · verified: 20.19.0.v202611181947 (2026-11-19)

Such a job fails after about 13 min with a 「View Detail」 tile; the log shows 「status=Error … desc=External Error,
errorCode=4000 … errorCode=4001 general error」 and the credits are refunded. Not injected; a ready failed tile for
rows that need one.
