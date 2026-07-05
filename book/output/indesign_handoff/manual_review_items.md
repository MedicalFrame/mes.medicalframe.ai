# InDesign 반입 직전 최종 체크리스트

기준일: 2026-06-09

이 문서는 `output/indesign_handoff/` 패키지를 실제로 넘기기 직전에,
무엇을 먼저 확인하고 무엇을 최종 판단해야 하는지 순서대로 정리한 운영용 체크리스트다.

## 0. 기준 파일 확인

- [ ] 기준 원고는 `output/indesign_handoff/manuscript_indesign.md`로 고정한다.
- [ ] 합본 원본 확인이 필요하면 `book_manuscript/book.md`를 본다.
- [ ] 이미지 링크는 raw manuscript ref가 아니라 `output/indesign_handoff/image_manifest.csv`의 actual disk path를 기준으로 잡는다.
- [ ] 캡션 작업은 `output/indesign_handoff/captions.csv`를 기준으로 맞춘다.

## 1. 반입 전 즉시 확인할 것

- [ ] `image_manifest.csv` 경로가 반입 작업 머신에서 실제로 모두 열리는지 확인한다.
- [ ] 표지 파일 `assets/앞표지.png`, `assets/뒷표지.png`는 interior 본문이 아니라 exterior asset으로 분리 취급한다.
- [ ] `raw_url_list.md`에 모인 URL 문자열 중 깨진 항목을 수동으로 정리한다.
- [ ] paragraph style 매핑이 `Part / Chapter / Section / Body / Figure Caption / URL / Production Note`까지 커버되는지 확인한다.

## 2. 링크 안정성 리스크

- [ ] case-mismatch 3건은 source ref가 아니라 actual path 기준으로 링크한다.
- [ ] 대상 3건:
- [ ] `cleanemr_04`: `assets/images/cleanemr_04.PNG`
- [ ] `clinical_digital_twin_02`: `assets/images/clinical_digital_twin_02.PNG`
- [ ] `diaframe_02`: `assets/images/diaframe_02.PNG`
- [ ] 이 3건은 원고 파일명을 억지로 고치지 말고 handoff 패키지 기준으로 처리한다.
- [ ] duplicate extension variant가 있는 asset은 사람이 최종 선택한 실제 파일 하나로 링크를 고정한다.

## 3. 인쇄 품질 우선 점검

- [ ] `00_management/reports/print_image_priority.md`의 P1 이미지를 먼저 검토한다.
- [ ] P1 우선순위는 `EstroFrame` 3장 -> `VoiceGrape` 2장 -> `JLPT` 1장 순서로 본다.
- [ ] `EstroFrame` 이미지는 장 대표 컷 성격이 강하므로 전폭 배치 전 교체 여부를 먼저 판단한다.
- [ ] `VoiceGrape` 이미지는 내부 텍스트 가독성을 기준으로 유지/교체를 정한다.
- [ ] `JLPT` 이미지는 크기가 매우 작아서 사실상 교체 우선 대상으로 본다.
- [ ] P2 후보인 `OpenClaw`, `modeling_probabilistic_01`, `surgery_cessation_02`는 실제 배치 크기가 커질 때만 교체 우선순위를 올린다.

## 4. 편집 판단 항목

- [ ] 5장 `공부를 구조로 바라본다는 것`은 짧은 결함 장이 아니라 브리지 장으로 유지할지 최종 확인한다.
- [ ] 31장 `판단은 설명될 때 완성된다`는 Part 6 앵커 장으로 유지할지 최종 확인한다.
- [ ] 7장 `실습은 사고의 전환점`은 현행 유지로 충분한지, 마지막 절만 1단락 보강할지 판단한다.
- [ ] 13장 `사고를 구현한다는 것`은 파트 도입 장으로 현행 유지할지 확인한다.
- [ ] appendix와 production note의 paragraph style을 분리할지 결정한다.

## 5. 제작 노트와 위치 정책

- [ ] 제작 노트가 현재 `book.md`에서 뒷표지 뒤에 위치하는 상태를 그대로 둘지 결정한다.
- [ ] 대안 1: 현행 유지
- [ ] 대안 2: appendix 내부 마지막 항목으로 이동
- [ ] 대안 3: 별도 production page 성격으로 분리
- [ ] 이 결정은 자동 수정 전에 먼저 편집/디자인 정책으로 확정한다.

## 6. 최종 사인오프

- [ ] 본문, 표지, appendix, production note의 역할 구분이 모두 명확한지 확인한다.
- [ ] 링크 깨짐, 저해상도 대표 이미지, URL 깨짐, 제작 노트 위치 중 남은 보류 항목이 없는지 확인한다.
- [ ] 반입 담당자에게 “case-mismatch 3건은 `image_manifest.csv` actual path 기준 사용” 문구를 반드시 전달한다.
- [ ] 위 항목이 끝나면 이 패키지를 handoff 기준본으로 간주한다.

## 빠른 판정 기준

- 바로 반입 가능:
  - 링크 정상
  - P1 이미지 판단 완료
  - 제작 노트 위치 결정 완료
  - URL 정리 완료
- 조건부 반입:
  - 본문 구조는 확정됐지만 이미지/위치 정책 일부가 보류
- 반입 보류:
  - case-mismatch 처리 원칙이 공유되지 않았거나
  - P1 이미지 교체 판단이 전혀 안 된 상태
