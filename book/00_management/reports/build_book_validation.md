# Build Book Validation

기준일: 2026-06-07

대상 파일:

- `00_management/scripts/build_book.py`
- 생성 산출물 `book_manuscript/book.md`

## 1. Existence check for every file listed in `PARTS`

- `PARTS`에 나열된 장 파일: 40개
- frontmatter / 본문 / appendix 파일 모두 실존 확인
- 별도 참조 파일 `book_manuscript/99_appendix/99_제작_노트_의공구_Book_Pipeline.md` 실존 확인

결론: 누락된 참조 파일은 없다.

## 2. Inclusion check against `book_manuscript/README.md`

`book_manuscript/README.md`의 현재 목차 기준:

- 프롤로그 1
- 본문 33
- appendix 5
- 제작 노트 1
- 에필로그 1

`build_book.py` 기준 포함 방식:

- 프롤로그: 포함
- 본문 33장: 포함
- appendix 5장: 포함
- 에필로그: 포함
- 제작 노트: `PARTS` 내부가 아니라 마지막에 별도 append

결론:

- 의도된 장과 파일은 모두 결과물에 들어간다.
- 제작 노트만 포함 방식이 특수하다.

## 3. Part 6 title consistency

확인 결과:

- `README.md`: `AI 시대에 살아남는 것`
- `book_manuscript/README.md`: `AI 시대에 살아남는 것`
- `build_book.py`: `AI 시대에 살아남는 것`
- `book_manuscript/book.md`: `# Part 6. AI 시대에 살아남는 것`

결론: 현재 Part 6 표기는 일치한다.

## 4. Cover and production-note path validation

- 앞표지: `assets/앞표지.png` 존재
- 뒷표지: `assets/뒷표지.png` 존재
- 제작 노트: `book_manuscript/99_appendix/99_제작_노트_의공구_Book_Pipeline.md` 존재

결론: 정적 경로는 유효하다.

## 5. Production note placement / duplication

현재 동작:

- appendix 5개 파일을 먼저 포함
- 에필로그 뒤에 appendix가 끝남
- 뒷표지를 append
- 그 뒤에 제작 노트를 append

확인 결과:

- 제작 노트는 1회만 포함된다.
- 중복 append 문제는 없다.
- 다만 위치는 “appendix 내부 마지막 항목”이 아니라 “뒷표지 다음 별도 섹션”이다.

판단:

- 중복 버그는 아니다.
- 위치는 layout/production decision 성격이 있으므로, 자동 수정은 보류 가능하다.

## 6. Generated order check

생성된 `book_manuscript/book.md` 기준:

- 앞표지 1회
- 프롤로그 1회
- Part 1 -> Part 6 순서 정상
- 에필로그 포함
- appendix 5개 포함
- 뒷표지 1회
- 제작 노트 1회

결론: 장 순서는 현재 의도와 일치한다.

## 7. Validation finding: heading normalization bug

현재 산출물에서 다음 문제가 확인된다.

- `### # 1)` 형태의 잘못된 소제목 171개
- 예:
  - `### # 1) 불확실성을 구조로 바라보기`
  - `### # **1) 잘게 쪼개기**`

원인:

- `normalize_inner_headings()`가 기존 heading 앞의 추가 `#`와 `**`를 완전히 제거하지 못한다.

영향:

- `book_manuscript/book.md` heading 계층이 깨끗하지 않다.
- Pandoc TOC depth 2에는 직접 영향이 적지만, InDesign handoff용 구조화 Markdown 품질에는 악영향이 있다.

## 8. Safe mechanical fix assessment

안전하게 수정 가능한 항목:

- `normalize_inner_headings()`에서 잔여 `#` 및 wrapping `**` 제거

수정 보류 항목:

- 제작 노트의 최종 위치 변경
- 페이지 브레이크 정책 변경
- 표지/목차/본문 배치 재설계

## 9. Next action

1. 이 보고서 작성 후 `build_book.py`의 heading normalization만 수정
2. `book_manuscript/book.md` 재생성
3. 잘못된 `### # ...` heading이 사라졌는지 재검증

## 10. Remediation applied after report

- `build_book.py`의 `normalize_inner_headings()`를 수정해 잔여 `#`와 wrapping `**`를 제거했다.
- `python3 00_management/scripts/build_book.py` 재실행 완료
- 재검증 결과:
  - `BAD_HEADING_COUNT = 0`
  - Part 6 제목, 장 순서, 제작 노트 1회 포함 상태는 유지됨
