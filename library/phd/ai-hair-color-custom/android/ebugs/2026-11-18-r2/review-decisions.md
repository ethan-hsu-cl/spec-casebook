Account: WILLY_WU
TRCode: TR261111-0042
Source tag: [AIAgent]
Method: API (new way)
ECL product: PhotoDirector Mobile for Android

| # | Sev | Belong | Type | UX check | Action | Short Description | Note |
|---|---|---|---|---|---|---|---|
| 1 | 3 | RD | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Photo guide reads 「Recommendation」, 「Face Too Small」, adds 「Accessories」 vs the Design | 其他feature都是Recommendation, 底下的三個會隨著feature改變, photo tab的話那個是相簿名稱本來就會變 |
| 2 | 4 | RD | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: No-face dialog reads 「A face is required」, not 「Face is required」 | 用字不同沒關係 |
| 3 | 3 | RD | Functional | — | hold | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Edit Room Quick Action row has no 「Hair Color」 tool | quick action本來就沒有要加hair color |
| 4 | 3 | PM | UX | — | hold | PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: Solid hides the Highlight Color row; Design greys it, PM hides it — which? | 隱藏就好 |
| 5 | 2 | PM | UX | — | hold | PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: two-colour style with only Base Color keeps Generate disabled — PM to decide | 更新知識, 都要選才能生成 |
| 6 | 3 | RD | Functional | — | hold | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel: tapping grey Generate with Highlight only shows no 「Select both…」 toast | 不用toast, generate沒有亮起來user就該知道不能generate |
| 7 | 3 | RD | Functional | — | file | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom palette: colour picked with Done is not added to the row as a new circle |  |
| 8 | 3 | PM | UX | confirmed | file | PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom panel: tapping the photo closes the panel and applies — PM to decide |  |
| 9 | 3 | RD | Functional | — | hold | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel collapses as soon as Generate is tapped in it; it should stay open |  |
| 10 | 3 | RD | Functional | — | hold | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: ✕ on a result asks 「Discard changes?」, then opens Edit Room, not the Launcher | 回到edit room是正常的 |
| 11 | 3 | RD | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Subscriber out of credits sees 「Get Credit Refilled!」, not 「More Credits Required!」 |  |
| 12 | 3 | PM | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Colour page: first Solid template is 「Soft Black」, no 「Platinum」 — PM to confirm |  |
| 13 | 3 | PM | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Custom panel: split-dye styles show photo thumbnails, not plain-colour ones — PM to confirm |  |
