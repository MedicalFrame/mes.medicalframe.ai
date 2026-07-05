# InDesign 반입 가능 여부 판정

기준일: 2026-06-09

## 한 줄 결론

현재 상태는 **조건부 반입 가능**이다.

즉:

- handoff 패키지는 이미 usable 하다.
- 본문/자산/manifest/캡션 scaffold는 갖춰져 있다.
- 다만 최종 반입 전에 사람이 반드시 결정해야 하는 항목이 아직 남아 있다.

## 이번 판정에서 다시 확인한 사실

### 1. handoff 패키지 기본 구성은 갖춰져 있다

- `output/indesign_handoff/manuscript_indesign.md` 존재
- `output/indesign_handoff/image_manifest.csv` 존재
- `output/indesign_handoff/captions.csv` 존재
- `output/indesign_handoff/raw_url_list.md` 존재
- `output/indesign_handoff/README_INDESIGN_HANDOFF.md` 존재

### 2. image manifest 기준 실제 경로는 현재 모두 살아 있다

- `image_manifest.csv`의 `current_path`를 기준으로 확인했을 때 missing file은 없다.
- 즉, 자산 누락 때문에 handoff가 즉시 막히는 상태는 아니다.

### 3. case-mismatch 3건은 handoff package에서 이미 actual path로 표현돼 있다

대상:

- `assets/images/cleanemr_04.PNG`
- `assets/images/diaframe_02.PNG`
- `assets/images/clinical_digital_twin_02.PNG`

판단:

- source manuscript ref와 실제 파일명 case는 다르다.
- 하지만 `image_manifest.csv`는 actual path를 기록하고 있으므로, 반입 담당자가 manifest 기준으로 링크하면 운영 가능하다.

### 4. 빌드 기준 원고와 handoff 기준 원고가 분리돼 있어 운영상 안전하다

- 합본 원본: `book_manuscript/book.md`
- 반입 기준본: `output/indesign_handoff/manuscript_indesign.md`

판단:

- source manuscript를 억지로 수정하지 않고 handoff 패키지에서만 대응하는 현재 전략이 맞다.

## 지금 당장 반입을 막는 하드 블로커는 아닌 것

- missing asset
- missing combined manuscript
- missing handoff manifest
- case-mismatch 자산의 물리적 부재
- 캡션 scaffold 부재

## 아직 남아 있는 실제 수동 판단 항목

### 1. 인쇄 품질

P1 이미지 교체 여부가 아직 확정되지 않았다.

우선순위:

- `EstroFrame` 3장
- `VoiceGrape` 2장
- `JLPT` 1장

의미:

- 레이아웃에 따라 그대로 써도 되는 컷이 있을 수는 있다.
- 하지만 전폭 사용이나 텍스트 가독성이 중요한 경우 교체 판단 없이 넘기면 인쇄 품질 리스크가 남는다.

### 2. 제작 노트 위치

현재 제작 노트는 `book.md`에서 뒷표지 뒤에 위치한다.

아직 결정이 필요한 선택지:

- 현행 유지
- appendix 내부 마지막으로 이동
- 별도 production page로 분리

의미:

- 구조 오류는 아니지만, layout 정책이 미정이면 반입 후 다시 손대게 될 가능성이 크다.

### 3. URL 문자열 정리

`raw_url_list.md` 기준으로 수동 정리가 필요한 항목이 보인다.

대표 예:

- `https://estroframe.streamlit.app/?utm_medium=social](http://estroframe.streamlit.app/`
- `https://github.com/MedicalFrame/DiaFrame`
- `https://nihongokanji.com](https://nihongokanji.com/`

의미:

- 본문 전체를 다시 고칠 단계는 아니지만, URL 스타일링이나 링크 표기 정리 직전에는 손봐야 한다.

### 4. 최종 출력본 눈검수

아직 실제 출력본 기준:

- 목차
- 페이지 브레이크
- 문단 스타일

의 최종 눈검수가 완료됐다고 볼 근거는 없다.

의미:

- 지금 단계는 “패키지 반입 가능”이지 “인쇄 직행 가능”은 아니다.

## 운영 판정

### 지금 바로 가능한 것

- InDesign 작업자에게 패키지를 넘기기
- `image_manifest.csv` actual path 기준으로 링크 연결하기
- P1 이미지 교체/유지 판단을 레이아웃 시안과 함께 병행하기
- 제작 노트 위치를 시안 보면서 결정하기

### 아직 보류해야 하는 것

- 최종 인쇄 확정
- URL 표기 확정본 고정
- P1 이미지 무판단 상태에서의 본문 시각 품질 확정

## 반입 담당자에게 전달할 핵심 문구

1. 기준 원고는 `output/indesign_handoff/manuscript_indesign.md`다.
2. 이미지 링크는 raw manuscript ref가 아니라 `image_manifest.csv`의 `current_path` 기준으로 연결한다.
3. case-mismatch 3건은 파일이 없는 게 아니라 extension case만 다르다.
4. P1 이미지와 제작 노트 위치는 반입 후 가장 먼저 판단해야 한다.

## 최종 결론

현재 MESbook은 **InDesign 반입은 진행 가능하지만, 최종 인쇄 사인오프 전 단계**다.

춘식이 판단으로는:

- 지금 넘겨도 된다.
- 다만 “완료”라고 부르면 안 되고,
- 가장 정확한 표현은 **조건부 반입 가능**이다.
