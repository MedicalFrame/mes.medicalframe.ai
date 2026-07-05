# InDesign Handoff

## 1. First file to import

- Start from `output/indesign_handoff/manuscript_indesign.md`.

## 2. Source manuscript location

- Canonical combined manuscript: `book_manuscript/book.md`
- Chapter sources: `book_manuscript/`

## 3. Image asset location

- Primary assets: `assets/images/`
- Cover assets: `assets/앞표지.png`, `assets/뒷표지.png`

## 4. How to use `captions.csv`

- Use `figure_id` to match each placeholder in `manuscript_indesign.md`.
- `existing_caption` is conservative and may be blank.
- `proposed_caption` is a working label, not final editorial copy.
- `needs_manual_review=yes` means caption or asset handling should be checked before final layout.

## 5. Known unresolved issues

- Production note is currently placed after the back cover in `book.md`.
- Three source image refs rely on case-insensitive filesystem behavior.
- Several images are likely low-resolution for print.
- Some bridge chapters remain editorial review items.
- See `00_management/reports/case_mismatch_handoff_plan.md` for the recommended handling path.
- See `00_management/reports/print_image_priority.md` for replacement priority.
- Current working recommendation: keep source manuscript refs unchanged, and use `image_manifest.csv` actual disk paths for the three case-mismatch assets.

## 6. Suggested InDesign paragraph styles

- Book Title
- Subtitle
- Author
- Part Title
- Chapter Title
- Section Heading
- Body
- Body First Paragraph
- Bullet List
- Quote
- Figure Caption
- URL
- Production Note
- Meta Joke Box
- Code / Command

## 7. Suggested InDesign object styles

- Full-width Figure
- Inline Screenshot
- Webtoon Panel
- Cover Image
- Caption Box
- Production Note Box

## 8. Preflight checklist

- Confirm `image_manifest.csv` paths resolve on the handoff machine.
- Resolve case-mismatch image refs before packaging links.
- Review low-resolution candidates for print replacement or scaling limits.
- Decide whether production note stays after back cover or moves into appendix interior pages.
- Verify paragraph-style mapping for Part / Chapter / Section hierarchy.
- Verify front cover and back cover are handled as exterior assets, not interior body pages.
- Use `image_manifest.csv` actual paths, not raw manuscript refs, for the three case-mismatch assets.
- Prioritize P1 replacements first: `EstroFrame` 3, `VoiceGrape` 2, `JLPT` 1.
- Check malformed URLs in `raw_url_list.md` before styling URL blocks.
