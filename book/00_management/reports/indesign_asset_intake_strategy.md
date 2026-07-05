# InDesign 자산 반입 전략

기준일: 2026-06-07

이 문서는 handoff 직전 자산 처리 방침을 최종 확정하기 위한 운영 메모다.

## 1. 확정 결론

### case-mismatch 3건

다음 3건은 source manuscript 참조를 수정하지 않고, InDesign 반입 시 `image_manifest.csv`의 실제 디스크 경로를 기준으로 연결한다.

| manuscript ref | actual file |
|---|---|
| `assets/images/cleanemr_04.png` | `assets/images/cleanemr_04.PNG` |
| `assets/images/clinical_digital_twin_02.png` | `assets/images/clinical_digital_twin_02.PNG` |
| `assets/images/diaframe_02.png` | `assets/images/diaframe_02.PNG` |

이유:

- 현재 단계에서 원고 본문 참조까지 다시 수정할 필요가 없다.
- handoff 안정성만 확보하면 목적에 충분하다.
- `image_manifest.csv`에는 이미 actual path가 기록되어 있다.

### 저해상도 이미지

저해상도 이미지는 전면 교체가 아니라, 우선순위별 판단으로 처리한다.

- P1: 가능하면 원본 교체 또는 더 작은 배치 전제 검토
- P2: 레이아웃 축소 전제면 유지 가능
- P3: 보조 컷이면 유지 가능

## 2. 반입 작업 순서

1. `output/indesign_handoff/manuscript_indesign.md`를 기준 원고로 사용
2. `output/indesign_handoff/image_manifest.csv`에서 실제 파일 경로 확인
3. case-mismatch 3건은 raw ref를 무시하고 manifest의 `current_path`로 링크
4. P1 이미지부터 교체 가능성 검토
5. 교체가 어렵다면 전폭 사용을 피하고 축소 배치 기준으로 전환
6. 마지막으로 `raw_url_list.md`와 표지 처리 방식 점검

## 3. P1 이미지 처리 기준

우선순위:

1. `EstroFrame` 3장
2. `VoiceGrape` 2장
3. `JLPT` 1장

실무 방침:

- 대체 원본이 있으면 교체 검토
- 대체 원본이 없으면 본문 전폭 사용을 피함
- 스크린샷 내부 텍스트가 핵심이면 확대보다 축소 배치와 캡션 보완을 우선

## 4. P2 / P3 처리 기준

- `OpenClaw`, `modeling_probabilistic_01`, `surgery_cessation_02`는 레이아웃 시뮬레이션 후 판단
- `haos_02`는 보조 컷 유지 전제면 통과 가능

## 5. 표지와 파일명 정책

- `assets/앞표지.png`, `assets/뒷표지.png`는 현행 유지
- 표지 두 장은 interior 이미지가 아니라 exterior asset으로 분리 취급
- 한글 파일명 rename은 이번 단계에서 하지 않는다

## 6. handoff 담당자 전달 문구

- 링크 연결은 source manuscript의 raw ref가 아니라 `image_manifest.csv` actual path를 기준으로 진행합니다.
- `cleanemr_04`, `clinical_digital_twin_02`, `diaframe_02`는 확장자 case mismatch가 있으므로 manifest 기준으로만 연결합니다.
- 저해상도 이미지의 교체 여부는 `print_image_priority.md`의 P1부터 검토하고, 교체가 어렵다면 축소 배치로 대응합니다.
