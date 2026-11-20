# Logs

## KF-011 Image to Video log lines
- kind: fact · platform: android · use: run, ebug · tags: logs, credits, analytics, reuse
- source: i2v-reuse run 2026-11-19-r1 R1-c (TC-026, TC-037..040) · verified: 20.19.0.v202611181947 (2026-11-19)

Generate logs 「addNewPack credit_action_id <id>」 with 「credit_total_credit <price>」 (Kling 2.6 10s Pro Sound On:
「genvideo_1_sec_kling_custom_2.6pro_enable_single_1080p」, 80) and the prompt in an 「ImageToVideoPromptsHistory」 line;
the HTTP body is not logged. 「Reuse」 logs 「logEvent name=Artwork_Reuse_Click」 with no parameters and 「[setCurFrom]
from = artwork_reuse」; 「Create More」 sets from = 「Artwork」. Mixpanel tag: KP-140.
