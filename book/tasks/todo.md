# MESbook 작업 TODO

기준일: 2026-06-09 (InDesign handoff 준비)

## 현재 상태 요약

- 원고 본체는 `book_manuscript/` 아래에 정리되어 있다.
- 합본 기준 파일은 `book_manuscript/book.md`다.
- 최신 빌드 스크립트 기준 Part 6 제목은 `AI 시대에 살아남는 것`이며, 장 수는 4개다.
- 관리 문서와 빌드 스크립트 기준 구조를 다시 동기화했다.
- `user/의공모.docx`는 복구되어 현재 빌드에 다시 연결된다.
- `build_all.sh` 기준 `DOCX / EPUB / PDF` 빌드를 다시 통과했다.
- `build_book.py`의 소제목 정규화 버그를 수정해 합본 `book.md`의 `### # ...` 오염을 제거했다.
- 운영 체크리스트의 기준 문서는 `tasks/todo.md`로 둔다.
- 2026-07-05 기준 원본 소스는 `mes.medicalframe.ai/book/` 아래로 흡수했고, 공개 PDF는 `downloads/MESbook.pdf`와 `book/output/MESbook.pdf`를 같은 파일로 유지한다.
- GitHub 이전 후 본문 내 제품 레포 링크는 새 조직 주소 기준으로 정리했다.

## 1) Repo inspection

- [X] 루트 폴더 구조 확인
- [X] `book_manuscript/`, `assets/`, `00_management/`, `output/` 실파일 재점검
- [X] `README.md`, `book_manuscript/README.md`, `chapter_status.md`, `file_mapping.md`, `build_book.py`, `build_all.sh` 대조
- [X] `00_management/reports/repo_truth_audit.md` 작성
- [X] `00_management/reports/build_book_validation.md` 작성

## 2) Management document sync

- [X] `00_management/chapter_status.md` 최신 상태로 재동기화
- [X] `00_management/file_mapping.md` 운영용 대응표 기준으로 재정리
- [X] `tasks/todo.md`를 현재 운영 기준 문서로 유지
- [X] `00_management/reports/management_sync_report.md` 작성

## 3) Manuscript / content review

- [X] 짧은 장 후보 재확인
- [X] 30장 누락 이슈 해소 확인
- [X] 현재 short review 대상이 실제로는 5, 7, 13, 31장 쪽에 가깝다는 점 반영
- [X] 브리지 장 후보(5, 31장)와 편집 검토 필요 장(7, 13장) 최종 판단

## 4) Asset review

- [X] 이미지 참조 경로 스캔
- [X] missing / unused / rename suggestion 보고서 작성
- [X] InDesign 링크 리스크(한글 파일명, 공백, 중복 확장자) 정리
- [X] case-mismatch 3건과 저해상도 P1 이미지의 실제 반입 전략 최종 확정

## 5) InDesign handoff preparation

- [X] handoff용 `manuscript_indesign.md` 생성
- [X] `image_manifest.csv`, `captions.csv`, `raw_url_list.md` 생성
- [X] `README_INDESIGN_HANDOFF.md`와 `book_metadata.yaml` 생성
- [X] handoff 문서의 최종 운영 문구와 체크리스트 확정
- [X] handoff readiness 판정 문서 작성

## 6) Final print / PDF proofing

- [X] `DOCX / EPUB / PDF` 빌드 재통과
- [X] `user/의공모.docx`를 Word 호환 reference-doc로 복구 및 재연결
- [X] 고용량 삽화의 `jpg` 복사본 생성 및 본문/빌드 경로 반영
- [ ] 실제 출력본 기준으로 목차 / 페이지 브레이크 / 스타일 최종 눈검수
- [X] InDesign 반입 전 수동 검토 항목 확정
- [ ] P1 이미지 교체 여부 / 제작 노트 위치 / URL 문자열 정리까지 포함한 최종 사인오프

## 이번 점검에서 확인한 핵심 메모

- 폴더 구조는 `00_management / book_manuscript / assets / output / legacy`로 명확하다.
- 실제 원고는 파트별 폴더와 appendix까지 일관되게 배치되어 있다.
- 최신 레포에서는 Part 6 제목과 장 구성이 과거 메모와 달랐고, 상태표/매핑표/README를 모두 현재 구조 기준으로 재정렬했다.
- 소제목 정규화 문제는 스크립트 수정으로 해결했고, 이제 남은 일은 자산 감사와 handoff 패키지 정리다.
- 이제 핵심 잔여 작업은 원고 대수정보다도 handoff 운영 판단과 최종 출력 검수 쪽에 가깝다.
- 프롤로그는 원본 보존 상태에서 빌드용 축약판으로 분기했고, 브리지 장/자산 반입 전략 판단도 운영 문서에 반영했다.
- 현재 handoff는 패키지 구조상 가능하지만, 최종 판정은 여전히 `조건부 반입 가능` 상태다.
- 사이트 레포가 이제 원본과 공개 산출물을 함께 관리하므로, 이후에는 `mes.medicalframe.ai/book/`에서 빌드하고 필요한 산출물만 `downloads/`로 복사한다.
