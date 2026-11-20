# Update plan — phd/ai-hair-color-custom / android: approved v3 → draft 20261118-120459

## Spec files
- Unchanged: the spec set `specs/2026-11-17` (PM page 3287:89, Design page 616:9324).
- Standing inputs: the user's rulings on the R2 eBug review (requests.md REQ-009, `ebugs/2026-11-18-r2/decisions.md`).

## Requirement changes
| Requirement | Change | Before | After |
|---|---|---|---|
| R-010 | modified | 「No face detected. Face is required for this feature.」 | Either wording; the app's 「A face is required」 is accepted |
| R-027 | modified | Solid greys the Highlight row (Design) | Solid hides the Highlight row (PM D6-04; Q-18 answered) |
| R-029 | modified | Base alone enables Generate (REQ-003 / REQ-007) | Both colours required; one alone keeps Generate disabled (REQ-003 / REQ-007 superseded) |
| R-085 | modified | Missing colour → toast 「Select both a base and highlight color.」 | No toast required; the disabled Generate is enough |
| R-068, R-076 | modified | ✕ / Back return to the screen before entry, no confirmation | They land in the Edit Room; a 「Discard changes?」 confirmation is Q-22 |
| R-088 | modified | Design's exact guide strings | App-wide 「Recommendation」 heading, items per feature, album-name tab (Q-20 answered) |
| R-089 | not testable | Quick Action holds 「Hair Color」 | Quick Action has no 「Hair Color」 (ruling) |
| Q-18, Q-20 | answered | — | By REQ-009 |
| Q-19 | superseded | — | By REQ-009 |
| Q-22 | new | — | The 「Discard changes?」 confirmation before landing in the Edit Room |

## Case changes
- New (0) · Removed (0) · Unchanged: 78
- Modified (9):
  - TC-009: either no-face wording passes.
  - TC-015: back to Portrait › Hair › AI Hair Color (no Quick Action tool).
  - TC-024, TC-029: Solid hides the Highlight row.
  - TC-026: Base only keeps Generate disabled (both required).
  - TC-027: Highlight only keeps Generate disabled; no toast required.
  - TC-079, TC-088: land in the Edit Room; the confirmation is recorded (Q-22).
  - TC-092: app-wide 「Recommendation」 heading, items per feature, album-name tab.

## Found by the analysis
- With these rulings, R2's Fails of TC-009, TC-015, TC-024, TC-026, TC-027, TC-029 and TC-092 match the new
  expectations on 90201901; TC-079 / TC-088 match apart from the recorded confirmation (Q-22). They are re-run in
  the next round.
- Control trace: the Edit Room's Quick Action tab and its tool row are now n/a (other feature, REQ-009).

## Not added (value check)
- None.
