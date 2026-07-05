# Print Image Priority

기준일: 2026-06-07

이 문서는 저해상도 후보를 **교체 우선순위** 기준으로 정리한 것이다.
기준은 해상도 자체, 페이지 내 중요도, 장 대표성, 대체 가능성이다.

## P1. 먼저 교체 검토

인쇄 품질에 가장 민감하거나, 장 대표 이미지인데 해상도가 낮은 경우다.

| figure_id | 파일 | 크기 | 이유 |
|---|---|---:|---|
| `fig_0019` | `assets/images/estroframe_01.png` | 914x472 | 장 대표 이미지 성격, 가로폭 사용 가능성 큼 |
| `fig_0020` | `assets/images/estroframe_02.png` | 716x368 | 해상도 낮음, 본문 설명과 결합될 가능성 큼 |
| `fig_0021` | `assets/images/estroframe_03.png` | 904x338 | 해상도 낮음, 대표 시각자료군 |
| `fig_0014` | `assets/images/voicegrape_01.png` | 906x328 | 대표 장 이미지, 인쇄 축소 여유 적음 |
| `fig_0015` | `assets/images/voicegrape_02.png` | 878x296 | 대표 장 이미지, 세부 텍스트 가독성 위험 |
| `fig_0053` | `assets/images/jlpt_01.png` | 400x231 | 매우 작음, 사실상 교체 우선 |

## P2. 조건부 교체 검토

레이아웃에서 작게 쓰면 버틸 수 있으나, 크게 쓰면 위험한 경우다.

| figure_id | 파일 | 크기 | 이유 |
|---|---|---:|---|
| `fig_0009` | `assets/images/openclaw_01.png` | 500x759 | 세로형이라 작게 쓰면 가능, 크게 쓰면 위험 |
| `fig_0012` | `assets/images/modeling_probabilistic_01.png` | 690x311 | 가로형 해상도 낮음 |
| `fig_0042` | `assets/images/surgery_cessation_02.png` | 870x892 | 1단/좁은 폭이면 가능, 전폭 사용은 위험 |

## P3. 레이아웃 축소 전제면 유지 가능

| figure_id | 파일 | 크기 | 이유 |
|---|---|---:|---|
| `fig_0008` | `assets/images/haos_02.png` | 294x636 | 매우 작지만 보조 컷이면 가능 |

## 우선 작업 제안

1. `EstroFrame` 3장
2. `VoiceGrape` 2장
3. `JLPT` 1장
4. `OpenClaw` 1장
5. `modeling_probabilistic_01` 1장
6. `surgery_cessation_02` 1장

## 실무 판단 기준

- 전폭 figure면 최소 교체 검토
- 1단 폭 축소 사용이면 유지 가능성 있음
- 스크린샷 내부 글자가 핵심이면 해상도보다 가독성을 우선 판단
- 같은 장에서 설명 보조용이면 작게 배치하는 쪽이 낫다
