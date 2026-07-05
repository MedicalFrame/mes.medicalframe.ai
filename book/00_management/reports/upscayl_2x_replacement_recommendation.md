# Upscayl 2X 교체 추천

기준일: 2026-06-07

## 요약

- `assets/upscayl_png_upscayl-standard-4x_2x/` 안의 업스케일 결과물 이름을 모두 `_2X` 규칙으로 정리했다.
- `openclaw_01`은 동일 파일이 2개라서 하나는 `openclaw_01_2X.png`, 다른 하나는 `openclaw_01_dup_2X.png`로 분리해 두었다.
- 모든 업스케일본을 본문에 반영할 필요는 없다.
- 현재 기준으로는 **저해상도 후보군 위주로 선별 교체**하는 편이 가장 실용적이다.

## 1차 즉시 대체 추천

인쇄 품질 개선 효과가 크고, 기존 보고서의 P1 / P2 / P3 우선순위와도 일치하는 파일들이다.

| 기존 파일 | 대체 업스케일본 | 이유 |
|---|---|---|
| `assets/images/estroframe_01.png` | `assets/upscayl_png_upscayl-standard-4x_2x/estroframe_01_2X.png` | 914x472 -> 1828x944 |
| `assets/images/estroframe_02.png` | `assets/upscayl_png_upscayl-standard-4x_2x/estroframe_02_2X.png` | 716x368 -> 1432x736 |
| `assets/images/estroframe_03.png` | `assets/upscayl_png_upscayl-standard-4x_2x/estroframe_03_2X.png` | 904x338 -> 1808x676 |
| `assets/images/voicegrape_01.png` | `assets/upscayl_png_upscayl-standard-4x_2x/voicegrape_01_2X.png` | 906x328 -> 1812x656 |
| `assets/images/voicegrape_02.png` | `assets/upscayl_png_upscayl-standard-4x_2x/voicegrape_02_2X.png` | 878x296 -> 1756x592 |
| `assets/images/jlpt_01.png` | `assets/upscayl_png_upscayl-standard-4x_2x/jlpt_01_2X.png` | 400x231 -> 800x462 |
| `assets/images/openclaw_01.png` | `assets/upscayl_png_upscayl-standard-4x_2x/openclaw_01_2X.png` | 500x759 -> 1000x1518 |
| `assets/images/modeling_probabilistic_01.png` | `assets/upscayl_png_upscayl-standard-4x_2x/modeling_probabilistic_01_2X.png` | 690x311 -> 1380x622 |
| `assets/images/surgery_cessation_02.png` | `assets/upscayl_png_upscayl-standard-4x_2x/surgery_cessation_02_2X.png` | 870x892 -> 1740x1784 |
| `assets/images/haos_02.png` | `assets/upscayl_png_upscayl-standard-4x_2x/haos_02_2X.png` | 294x636 -> 588x1272 |

## 2차 조건부 대체 추천

기존 해상도도 이미 1200px 안팎이라 급한 교체는 아니지만, print나 확대 배치에서 여유가 생길 수 있는 파일들이다.

- `assets/images/anki_01.png` -> `anki_01_2X.png`
- `assets/images/anki_02.png` -> `anki_02_2X.png`
- `assets/images/openclaw_02.png` -> `openclaw_02_2X.png`
- `assets/images/openclaw_03.png` -> `openclaw_03_2X.png`
- `assets/images/structuring_power_01.png` -> `structuring_power_01_2X.png`
- `assets/images/structuring_power_02.png` -> `structuring_power_02_2X.png`
- `assets/images/structuring_power_03.png` -> `structuring_power_03_2X.png`

## 이번에는 굳이 안 바꿔도 되는 파일

아래 계열은 이미 원본이 1280px 전후이거나 충분히 크고, 현재 보고서 기준 저해상도 리스크도 낮다.

- `cleantext_*`
- `cleanemr_*`
- `diaframe_*`
- `pharmaframe_*`
- `neuroframe_*`
- `future_doctor_*`
- `model_reality_*`
- `clinical_digital_twin_*`

이 파일들까지 전부 업스케일본으로 교체하면:

- 경로 관리가 복잡해지고
- 파일 크기만 커지고
- 실제 인쇄 이득은 상대적으로 작을 수 있다

## 운영 권장

1. 본문/원고 경로를 한 번에 전부 바꾸지 않는다.
2. InDesign 또는 Word 최종 편집 단계에서 **1차 즉시 대체 추천 파일만 우선 교체**한다.
3. 실제 출력 시 크게 쓰는 이미지가 있으면 그때 2차 조건부 대체 추천 파일을 추가 반영한다.
