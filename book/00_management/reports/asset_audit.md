# Asset Audit

기준일: 2026-06-07

## Summary

- `book_manuscript/**/*.md` + `book_manuscript/book.md` 기준 이미지 참조 수: 106
- source manuscript 기준 고유 asset 수: 54
- `assets/` 전체 파일 수: 60
- missing physical asset 수: 0
- case-mismatch ref 수: 3
- unused asset 수: 6
- duplicate-looking stem group 수: 6

## Missing physical assets

- 없음

## Case-mismatch references

- ref `assets/images/cleanemr_04.png` -> actual `assets/images/cleanemr_04.PNG`
- ref `assets/images/clinical_digital_twin_02.png` -> actual `assets/images/clinical_digital_twin_02.PNG`
- ref `assets/images/diaframe_02.png` -> actual `assets/images/diaframe_02.PNG`

## Duplicate-looking files

- `cleantext_02`: `assets/images/cleantext_02.jpeg`, `assets/images/cleantext_02.png`
- `cleantext_03`: `assets/images/cleantext_03.jpeg`, `assets/images/cleantext_03.png`
- `clinical_digital_twin_03`: `assets/images/clinical_digital_twin_03.jpeg`, `assets/images/clinical_digital_twin_03.png`
- `haos_01`: `assets/images/haos_01.heic`, `assets/images/haos_01.png`
- `modeling_probabilistic_01`: `assets/images/modeling_probabilistic_01.heic`, `assets/images/modeling_probabilistic_01.png`
- `openclaw_01`: `assets/images/openclaw_01.jpeg`, `assets/images/openclaw_01.png`

## InDesign link risk notes

- 표지 파일은 `assets/앞표지.png`, `assets/뒷표지.png`로 한글 파일명이다.
- source manuscript에는 `.png`로 참조하지만 실제 파일이 `.PNG`인 case mismatch가 3건 있다.
- duplicate extension variant가 여러 개 있어 handoff 패키지에서는 actual disk path 기준 manifest 확인이 필요하다.

## Low-resolution candidates

- `assets/images/estroframe_01.png`: 914x472
- `assets/images/estroframe_02.png`: 716x368
- `assets/images/estroframe_03.png`: 904x338
- `assets/images/haos_02.png`: 294x636
- `assets/images/jlpt_01.png`: 400x231
- `assets/images/modeling_probabilistic_01.heic`: 690x311
- `assets/images/modeling_probabilistic_01.png`: 690x311
- `assets/images/openclaw_01.jpeg`: 500x759
- `assets/images/openclaw_01.png`: 500x759
- `assets/images/surgery_cessation_02.png`: 870x892
- `assets/images/voicegrape_01.png`: 906x328
- `assets/images/voicegrape_02.png`: 878x296

## Front / back cover

- `assets/앞표지.png`: exists=True size=1024x1536
- `assets/뒷표지.png`: exists=True size=1024x1536
