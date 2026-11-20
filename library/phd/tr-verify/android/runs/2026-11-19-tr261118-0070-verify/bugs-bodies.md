=== PHA262026P0057 — PHD-A 20.19.0 - [AIAgent] Batch_Editing: AI Enhance does not pause in the background; remaining photos fail as Connection lost
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap AI Enhance
7. Tap Enhance
8. Tap Start
9. Wait until 「Enhancing 4 / 12」 shows
10. Press the Home key
11. Wait 30 seconds
12. Open PhotoDirector from Recents
13. Check the result

Result:
Not paused: the 7 remaining photos failed in the background; on return 「5 completed, 7 failed」 / Connection lost.
摘要：背景期間未暫停，剩餘 7 張立即以 Connection lost 失敗（兩次皆重現）。
{20.19.0_bea01_return_5done_7failed.jpg} {20.19.0_bea01_return2_4done_8failed.jpg} {20.19.0_bea01_log.txt}

Expect Result:
Processing pauses while the app is in the background and continues from where it was on return; it finishes normally.
摘要：App 在背景時暫停處理，回到前景後由中斷處繼續並正常完成。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Batch Edit PM spec (UI UX flow 2.pdf), Server task notes board (server-task-notes)
Related: PHA262026P0022 (AI_Removal: false Network Error after backgrounding during Generate)
<Claude Reviewed>

=== PHA262026P0058 — PHD-A 20.19.0 - [AIAgent] Batch_Editing: System Back does not close the AI Enhance confirm dialog 「Enhance 12 photos?」
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap AI Enhance
7. Tap Enhance
8. Press the system Back key
9. Press the system Back key
10. Check the result

Result:
The dialog stays open after each Back; only 「Cancel」 closes it. Nothing is processed.
摘要：按系統返回鍵兩次，確認對話框仍不關閉。
{20.19.0_bea04_confirm_after_back.jpg}

Expect Result:
Back acts like 「Cancel」: the dialog closes, the AI Enhance page shows and nothing is processed.
摘要：返回鍵等同 Cancel：關閉對話框且不開始處理。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Batch Edit PM spec (UI UX flow 2.pdf), AI Enhance Confirm Dialog · default board (confirm-dialog)
<Claude Reviewed>

=== PHA262026P0059 — PHD-A 20.19.0 - [AIAgent] Batch_Editing: System Back does not close the 「Discard changes?」 dialog opened from Home
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 12 photos
5. Tap Next
6. Tap Crop & Rotate
7. Tap Square
8. Tap ✓
9. Tap Home
10. Press the system Back key
11. Wait 2 seconds
12. Press the system Back key
13. Check the result

Result:
The 「Discard changes?」 dialog stays open after each Back.
摘要：按系統返回鍵兩次，放棄變更對話框仍不關閉。
{20.19.0_bea05_discard_after_back.jpg}

Expect Result:
Back acts like 「Keep Editing」: the dialog closes and Batch Edit Room stays with the edits.
摘要：返回鍵等同 Keep Editing：關閉對話框並保留編輯。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Batch Edit PM spec (UI UX flow 2.pdf), Discard Dialog · default board (discard-dialog)
<Claude Reviewed>

=== PHA262026P0060 — PHD-A 20.19.0 - [AIAgent] Batch_Editing: Square crop applied to all saves a 16:9 photo as 1434 x 1435, not square
Repro Steps:
1. Launch the APP
2. Tap Edit on the Launcher
3. Tap Batch
4. Select 4 photos, the 4th one 2730 x 1535 (16:9)
5. Tap Next
6. Tap Crop & Rotate
7. Tap the 4th thumbnail
8. Tap Square
9. Tap All
10. Tap ✓
11. Tap Save
12. Check the saved files' pixel sizes

Result:
The room labels the box 「1434 x 1435」 and the saved file is 1434 x 1435; the other three are square.
摘要：16:9 照片套用 Square 後輸出 1434 x 1435，並非正方形。
{20.19.0_bea06_square_label_1434x1435.jpg} {20.19.0_bea06_saved_4_photos.jpg}

Expect Result:
Square is a 1:1 crop: every saved photo's width equals its height.
摘要：Square 為 1:1，輸出寬高應相等。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Batch Edit PM spec (UI UX flow 2.pdf), Batch Edit Room · Crop & Rotate · default board (crop-default)
Spec Link: Batch Edit PM test (Section 3 · 美圖 Apply to all 實測.pdf), 結論 board (meitu-conclusion)
<Claude Reviewed>

=== PHA262026P0084 — PHD-A 20.19.0 - [AIAgent] Swipe_Collage: 「Lock」 on the image tool bar does nothing; the photo can still be moved
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Tap the Year End 「7 photos · 3 pages」 card
5. Tap Use Template
6. Tap the 「+」 of a page-1 frame
7. Tap the 「+」 again
8. Select 3 photos
9. Tap Next
10. Tap a filled frame on page 1
11. Tap the same frame again
12. Tap Lock on the tool bar
13. Check the tool bar and floating icons
14. Drag the photo inside its frame

Result:
Nothing changes: still 「Lock」, no 「Image locked」, and the photo can still be dragged.
摘要：點 Lock 無反應，照片仍可拖動。
{20.19.0_swc19_image_lock_no_change.jpg} {20.19.0_swc19_log.txt}

Expect Result:
The image locks: 「Image locked」, a floating Unlock, and it cannot be dragged or zoomed.
摘要：圖片應鎖定，顯示 Image locked，不能拖動縮放。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: TC-086 – TC-088 (locked image cases) are blocked by this
Spec Link: Swipe Collage PhDM Spec.pdf (PM), states-locks board (D1-34: 「Image locked」, cannot be dragged or zoomed)
<Claude Reviewed>

=== PHA262026P0085 — PHD-A 20.19.0 - [AIAgent] Swipe_Collage: 「Removal」 on the image tool bar opens nothing
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Tap the Year End 「7 photos · 3 pages」 card
5. Tap Use Template
6. Tap the 「+」 of a page-1 frame
7. Tap the 「+」 again
8. Select 3 photos
9. Tap Next
10. Tap a filled frame on page 1
11. Tap the same frame again
12. Tap Removal on the tool bar
13. Check the screen

Result:
Nothing opens: no Object Removal room, no IAP page, no toast (Premium and Free).
摘要：點 Removal 沒反應（Premium 與 Free 都一樣）。
{20.19.0_swc20_premium_removal_tap_nothing.jpg} {20.19.0_swc20_free_removal_tap_nothing.jpg} {20.19.0_swc20_log.txt}

Expect Result:
Removal opens the Object Removal room; for a Free user, applying shows the IAP page.
摘要：應開啟物件移除；Free 套用時跳 IAP。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Related: TC-063, TC-066, TC-067, TC-167 (Removal result and IAP rows) are blocked by this
Spec Link: Swipe Collage Design Figma, GAI_removal board (Object Removal room from the image tool bar) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=61-4517
Spec Link: Swipe Collage PhDM Spec.pdf (PM), removal-flow board (D3-01 / D1-43: Removal opens the room; IAP on apply for Free)
<Claude Reviewed>

=== PHA262026P0089 — PHD-A 20.19.0 - [AIAgent] Swipe_Collage: System Back on the Custom color picker applies the colour instead of cancelling
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Tap the Year End 「7 photos · 3 pages」 card
5. Tap Use Template
6. Tap Background
7. Tap 「Custom color +」
8. Tap a light red in the colour square
9. Press the system Back key
10. Check the background

Result:
One Back closes the picker and the sheet, and the chosen light red stays on every page.
摘要：按返回鍵直接關閉並套用所選顏色。
{20.19.0_swc26_picker_light_red_chosen.jpg} {20.19.0_swc26_back_applied_colour.jpg}

Expect Result:
System Back acts as 「Cancel」 and does not apply the colour (team rule R-134; Q-14).
摘要：返回鍵應等同 Cancel，不套用顏色。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage PhDM Spec.pdf (PM), states-background board (D1-23: picker 「Cancel」 does not apply, 「Done」 applies)
Spec Link: Swipe Collage Design Figma, background_panel_solid board (Custom color picker Cancel / Done) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=72-1786
<Claude Reviewed>

=== PHA262026P0097 — PHD-A 20.19.0 - [AIAgent][UI] Swipe_Collage: Pages move button selects on a tap; dragging shows no enlarged page or hint
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Tap the Year End 「7 photos · 3 pages」 card
5. Tap Use Template
6. Tap Pages
7. Tap the ≡ pill under page 1
8. Check the pages
9. Long-press the ≡ pill under page 1
10. Drag it past page 3
11. Check the page while dragging

Result:
A plain tap on ≡ selects the page; dragged, the page keeps its size and opacity, with no hint.
摘要：單點 ≡ 會選頁；拖曳時不放大不透明，也無提示。
{20.19.0_swc36_tap_selects_page.jpg} {20.19.0_swc36_drag_not_enlarged_no_hint.jpg}

Expect Result:
A plain tap does nothing; dragged, the page is enlarged and translucent with 「Hold ≡ & drag to reorder」.
摘要：單點無反應；拖曳時放大半透明並顯示提示。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage PhDM Spec.pdf (PM), states-pages board (D1-25: tap does nothing; drag enlarged and translucent, hint)
Spec Link: Swipe Collage Design Figma, page board (move button) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=74-3076
<Claude Reviewed>

=== PHA262026P0098 — PHD-A 20.19.0 - [AIAgent][UI] Swipe_Collage: Pages controls overlap from 5 pages; at 10 only the last ••• can be reached
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Tap the Year End 「7 photos · 3 pages」 card
5. Tap Use Template
6. Tap Pages
7. Tap Add
8. Tap Add
9. Check the controls under the pages
10. Tap Add 5 times
11. Check the controls under the pages

Result:
From 5 pages the ••• sit under the next ≡; at 10 pages only the last page's ••• can be reached.
摘要：5 頁起 ••• 被蓋住，10 頁時只剩最後一頁可點。
{20.19.0_swc37_five_pages_controls_overlap.jpg} {20.19.0_swc37_ten_pages_one_row.jpg}

Expect Result:
Every page's ≡ and ••• stay reachable at any page count from 1 to 10.
摘要：1 到 10 頁時每頁的 ≡ 與 ••• 都能點。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage PhDM Spec.pdf (PM), states-pages board (D1-27 / D1-12: ••• per page, 1 to 10 pages)
Spec Link: Swipe Collage Design Figma, page board (page strip with ≡ and •••) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=74-3076
<Claude Reviewed>

=== PHA262026P0099 — PHD-A 20.19.0 - [AIAgent][UI] Swipe_Collage: Template cards read 「1 pages」 and Save & Share reads 「1 images」
Repro Steps:
1. Launch the APP
2. Tap Collage on the Launcher
3. Tap the 「Try Scrollable Collage!」 banner
4. Check the Year End card labels

Result:
Cards read 「2 photos · 1 pages」 and a one-page Save & Share reads 「1 images」.
摘要：顯示「1 pages」與「1 images」。
{20.19.0_swc38_card_1_pages.jpg} {20.19.0_swc38_save_share_1_images.jpg}

Expect Result:
Singular counts read 「1 page」 and 「1 image」.
摘要：單數應為「1 page」、「1 image」。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: Swipe Collage Design Figma, Template Page · default (NEW) board (「9 photos · 5 pages」 card label) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=3-336
Spec Link: Swipe Collage Design Figma, Save: Only 1 img board (one-page Save & Share) -
https://www.figma.com/design/iUy5kOrVNG7IjcyxGGnp9t/Swipe_collage?node-id=103-5778
<Claude Reviewed>

=== PHA262026P0112 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom panel: colour rows can be picked before any style is chosen
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap the dark brown swatch in Base Color
8. Check the result

Result:
The swatch gets the selection ring; the colour rows are not disabled before a style.
摘要：未選 style 時即可選色，顏色列未停用。
{20.19.0_hcc04_colour_selected_no_style.jpg}

Expect Result:
Both colour rows are disabled until a style is chosen.
摘要：選 style 前兩列顏色應為停用。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_open_no_style (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-824
<Claude Reviewed>

=== PHA262026P0113 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom colour palette has no eyedropper key next to the hue slider
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the colour wheel in Base Color
9. Check the result

Result:
The palette shows Cancel / Done, the colour square and the hue slider, but no eyedropper key.
摘要：調色盤沒有滴管鍵。
{20.19.0_hcc06_palette_no_eyedropper.jpg}

Expect Result:
An eyedropper key sits right of the hue slider and picks a colour from the photo.
摘要：hue slider 右側應有滴管鍵，可從照片取色。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_palette (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-1204
<Claude Reviewed>

=== PHA262026P0114 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: System Back in the colour palette leaves AI Hair Color, not just the palette
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap a portrait photo with one clear, front-facing face
6. Tap Custom in the swatch row
7. Tap Ombre in Style
8. Tap the colour wheel in Base Color
9. Drag the hue slider to green
10. Press the system Back key
11. Check the result

Result:
AI Hair Color closes into the Edit Room; the palette and Custom settings are gone.
摘要：按系統返回鍵直接離開 AI Hair Color 進入 Edit Room，設定遺失。
{20.19.0_hcc07_palette_before_back.jpg} {20.19.0_hcc07_back_lands_edit_room.jpg}

Expect Result:
Back closes only the palette like Cancel; the room and the Custom settings stay.
摘要：返回鍵應只關閉調色盤（同 Cancel）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), panel_palette (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3327-1204
<Claude Reviewed>

=== PHA262026P0115 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Collapsing Custom panel keeps Soft Black selected; Generate makes a template
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Ombre in Style
10. Tap the dark brown swatch in Base Color
11. Tap the purple swatch in Highlight Color
12. Tap the collapse key at the top right of the panel
13. Tap Generate
14. Check the result

Result:
Soft Black stays selected after collapsing and Generate makes a Soft Black template result (6 credits).
摘要：收合後仍選 Soft Black，外部 Generate 產生的是 Soft Black 模板結果。
{20.19.0_hcc08_collapse_soft_black_selected.jpg} {20.19.0_hcc08_outer_generate_template_result.jpg} {20.19.0_hcc08_log.txt}

Expect Result:
Collapsing selects the Custom cell with the chosen colours and Generate makes the Custom result.
摘要：收合應選中 Custom 並顯示所選顏色，Generate 產生 Custom 結果。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), collapsed_applied (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-512
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), flow arrow panel_ready ⌄ → collapsed_applied - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3337-1879
<Claude Reviewed>

=== PHA262026P0117 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Custom result has no Intensity bar, panel open or collapsed
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Ombre in Style
10. Tap the dark brown swatch in Base Color
11. Tap the purple swatch in Highlight Color
12. Tap Generate in the panel
13. Wait for the result
14. Check the result

Result:
The result shows and the button reads Retry, but there is no Intensity bar.
摘要：結果出現、按鈕變 Retry，但沒有 Intensity 調整條。
{20.19.0_hcc11_result_no_intensity.jpg} {20.19.0_hcc11_collapsed_result_no_intensity.jpg}

Expect Result:
An Intensity bar at 100 % appears above Retry and adjusts the result's strength.
摘要：Retry 上方應出現 Intensity 條（預設 100%）。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), result_custom (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-718
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Spec - UI rules D1-15 / D1-16 / D1-19 (Artwork save, Intensity) - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3030-302
<Claude Reviewed>

=== PHA262026P0118 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: First Custom result shows no one-time My AI Artwork 100% dialog
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Ombre in Style
10. Tap the dark brown swatch in Base Color
11. Tap the purple swatch in Highlight Color
12. Tap Generate in the panel
13. Wait for the first result
14. Check the result

Result:
The result shows with no one-time dialog.
摘要：第一次結果出現時沒有一次性說明對話框。
{20.19.0_hcc12_first_result_no_dialog.jpg}

Expect Result:
A one-time dialog says My AI Artwork keeps only the 100% version, with Don't show again.
摘要：應出現一次性對話框說明 My AI Artwork 只保存 100% 版本。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Spec - UI rules D1-15 / D1-16 / D1-19 (Artwork save, Intensity) - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3030-302
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), result_custom (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-718
<Claude Reviewed>

=== PHA262026P0119 — PHD-A 20.19.0 - [AIAgent] AI_Hair_Color: Tapping Custom after a template result does not bring back the Custom result
Repro Steps:
1. Launch the APP
2. Tap AI Photos on the Launcher
3. Tap AI Hair Color
4. Tap Continue on the photo tips sheet
5. Tap Stock
6. Search 「woman portrait」 in Pexels
7. Tap the portrait of a woman in a knitted hat
8. Tap Custom in the swatch row
9. Tap Ombre in Style
10. Tap the dark brown swatch in Base Color
11. Tap the purple swatch in Highlight Color
12. Tap Generate in the panel
13. Wait for the result
14. Tap the collapse key
15. Tap Generate
16. Wait for the Soft Black result
17. Tap Custom in the swatch row
18. Check the result

Result:
The panel opens with the Custom settings, but the photo still shows the Soft Black result.
摘要：切回 Custom 後照片仍顯示 Soft Black 結果，未叫回 Custom 結果。
{20.19.0_hcc13_custom_tap_shows_template_result.jpg}

Expect Result:
The Custom result is shown again with no new generation and no charge.
摘要：應叫回 Custom 結果，不重新生成、不扣點。

Note:
Device: Samsung Galaxy S23 (SM-S9110) / Android 16
Spec Link: AI Hair Color Custom PM Figma (26 11E AI Hair Color Custom), result_custom (NEW) frame, Spec - UI - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3330-718
Spec Link: AI Hair Color PM Figma (26 10E AI Hair Color v2, cited by the Custom page), Spec - UI rules D1-15 / D1-16 / D1-19 (Artwork save, Intensity) - https://www.figma.com/design/vhIp15PMJcwOcWJ6E9Q4JE/AI-Hair?node-id=3030-302
Related: PHA262026P0047 (20.18.0, Assigned: preview resets to the original after switching to a template not used in generation)
<Claude Reviewed>

