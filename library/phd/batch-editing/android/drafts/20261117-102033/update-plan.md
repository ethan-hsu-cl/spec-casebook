# Update plan — phd/batch-editing / android: approved v7 → draft 20261117-102033

Request: REQ-018 (user ruling, 2026-11-17). Rows: 171 (new 1, modified 2, unchanged 168, removed 0).
Same spec set; no Figma change read for this draft (a ruling, not a spec change).

## Why
「按 ✕ 或 Back 如果是已經有做過操作的話就應該要跳discard change dialog」 (user, 2026-11-17, REQ-018): once an edit has been made, ✕ or Back on the AI Enhance page asks 「Discard changes?」; with no edit it goes straight back.

## Rows
- Modified: TC-100 — REQ-018 ruling on Q-19: ✕ after edits opens the Discard Dialog (was: back with results kept, no dialog)
- Modified: TC-142 — REQ-018 ruling on Q-19: Back after edits opens the Discard Dialog, like ✕
- New: TC-171 after TC-100 — REQ-018 ruling: ✕ with no edit goes straight back (the other half of the rule TC-100 checks)
