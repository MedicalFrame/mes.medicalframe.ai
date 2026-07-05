# Management Sync Report

기준일: 2026-06-07

## Documents updated

- `00_management/chapter_status.md`
- `00_management/file_mapping.md`
- `tasks/todo.md`

## Stale items fixed

- `chapter_status.md`
  - 현재 `build_book.py` 순서를 기준으로 장 목록을 유지했다.
  - short chapter 관련 표현을 `브리지 장 후보`, `편집 검토 필요`로 정리했다.
  - 과거의 “30장 누락” 관성 메모를 현재 구조 기준으로 정리했다.
- `file_mapping.md`
  - 문서 역할을 “historical raw-source migration map”이 아니라 “현재 운영용 대응표”로 명시했다.
  - 제작 노트 파일이 `PARTS` 내부가 아니라 스크립트 말미에 별도 append 된다는 점을 추가했다.
- `tasks/todo.md`
  - repo inspection / management sync / content review / asset review / handoff prep / proofing 단계로 다시 분리했다.
  - short review 대상이 현재 번호 기준으로 5, 7, 13, 31장 쪽이라는 점을 반영했다.
  - `build_book.py` heading normalization fix 완료 상태를 반영했다.

## Unresolved ambiguities

- 제작 노트를 appendix 내부 마지막 항목으로 볼지, 뒷표지 뒤 별도 production note로 볼지는 아직 운영 판단이 필요하다.
- 폴더명 `06_AI_시대에도_남는_것`과 표시 제목 `AI 시대에 살아남는 것`은 공존 상태다.
  - 현재 규칙상 source file rename은 하지 않았다.
- short chapter 분류는 정리했지만, 실제 확장 여부는 편집 판단이 남아 있다.

## Manual decisions still needed

1. 5장과 31장을 브리지 장으로 유지할지 확장할지 결정
2. 7장과 13장을 추가 보강 대상으로 볼지 결정
3. 제작 노트의 최종 위치를 현행 유지할지 조정할지 결정
4. InDesign 반입 시 appendix / production note 스타일 분리를 어떻게 할지 결정
