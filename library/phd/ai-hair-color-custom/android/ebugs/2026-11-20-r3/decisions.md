# Review decisions (user, 2026-11-20)

Account WILLY_WU · TR261111-0042 · [AIAgent] · API (new way) · PhotoDirector Mobile for Android. The user chose
TR261111-0042 (confirmed for build 90201901 in R2, REQ-010) over TR261118-0070.

Pasted verbatim:

| # | Sev | Belong | Type | UX check | Action | Short Description | Note |
|---|---|---|---|---|---|---|---|
| 1 | 4 | RD | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Intro Demo button reads 「Try now」, not 「Try Now」 |  |
| 2 | 3 | RD | Functional | — | hold | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel: Solid leaves the Highlight Color row greyed out instead of hiding it |  |
| 3 | 3 | PM | UX | — | hold | PHD-A 20.19.0 - [AIAgent][UX] AI_Hair_Color: Custom cell keeps its unset look after applying, not the chosen colours — PM to decide |  |
| 4 | 3 | RD | Functional | — | file | PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Solid template 「Soft Black」 takes about 35 s to generate, not about 15 s |  |
| 5 | 3 | PM | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Colour page: first Solid template is 「Soft Black」, no 「Platinum」 — PM to confirm |  |
| 6 | 3 | PM | UI | — | hold | PHD-A 20.19.0 - [AIAgent][UI] AI_Hair_Color: Custom panel: split-dye styles show photo thumbnails, not plain-colour ones — PM to confirm |  |

- File: 04 = ISS-HCC-34 (Soft Black template wait about 35 s; Sev 3, RD, Functional).
- Hold, no reason given: 01 ISS-HCC-31, 02 ISS-HCC-32, 03 ISS-HCC-33, 05 ISS-HCC-35, 06 ISS-HCC-36.
