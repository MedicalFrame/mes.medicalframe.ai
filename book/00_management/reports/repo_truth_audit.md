# Repo Truth Audit

기준일: 2026-06-07

## 1. Actual current folder structure

- 원고 소스: `book_manuscript/`
- 이미지 자산: `assets/`
- 관리 문서: `00_management/`
- 출력 산출물: `output/`
- 폰트: `fonts/`
- 레거시 자료: `legacy/`
- 사용자 참조 DOCX: `user/의공모.docx`

## 2. Actual manuscript source files under `book_manuscript/`

- frontmatter 2개
  - `book_manuscript/00_frontmatter/00_프롤로그_의세계에_전생했다는_것.md`
  - `book_manuscript/00_frontmatter/99_에필로그_두_세계를_오가는_마법진.md`
- Part 1 원고 4개
- Part 2 원고 8개
- Part 3 원고 9개
- Part 4 원고 5개
- Part 5 원고 3개
- Part 6 원고 4개
- appendix 원고 6개
  - 이 중 `book_manuscript/99_appendix/99_제작_노트_의공구_Book_Pipeline.md`는 실파일로 존재한다.
- 추가 관리 파일
  - `book_manuscript/README.md`
  - `book_manuscript/book.md`

총 Markdown 파일 기준:
- 장/부록 원고: 41개
- 원고 폴더 내부 관리/합본 파일 포함: 43개

## 3. Actual build scripts

- 합본 생성: `00_management/scripts/build_book.py`
- 최종 빌드: `00_management/scripts/build_all.sh`

현재 파이프라인:

`Markdown + assets -> 00_management/scripts/build_book.py -> book_manuscript/book.md -> Pandoc -> DOCX/PDF/EPUB`

## 4. Actual output artifacts under `output/`

- `output/book.docx`
- `output/book.epub`
- `output/book.pdf`
- 보조 테스트 파일: `output/test_toc.md`

현재 확인된 산출물 크기:

| 파일 | 크기 |
|---|---:|
| `output/book.docx` | 40M |
| `output/book.epub` | 23M |
| `output/book.pdf` | 19M |
| `output/test_toc.md` | 304K |

## 5. Mismatches among `README.md`, `book_manuscript/README.md`, `chapter_status.md`, `file_mapping.md`, and `build_book.py`

### 현재 일치하는 항목

- Part 6 제목은 모두 `AI 시대에 살아남는 것`으로 맞춰져 있다.
- `build_book.py`의 장 순서와 `book_manuscript/README.md`의 목차는 현재 동일하다.
- `chapter_status.md`와 `file_mapping.md`는 현재 `build_book.py` 기준 장 순서를 반영한다.

### 현재 남아 있는 불일치 또는 주의점

- `book_manuscript/README.md`의 메모 섹션은 일부가 역사적 설명이다.
  - `chapter_status.md`를 기준으로 복제했다는 표현은 현재 운영 기준이라기보다 이전 이관 과정을 설명하는 기록에 가깝다.
- `file_mapping.md`는 현재는 “실제 빌드 기준 파일명 대응표” 역할을 한다.
  - 파일명만 보면 “원본 -> 복사본 매핑” 문서처럼 읽히지만, 현재 문서 내용은 역사적 raw source 매핑이 아니라 현재 책 원고 매핑에 가깝다.
- `build_book.py`는 `99_제작_노트_의공구_Book_Pipeline.md`를 `PARTS` 안에 넣지 않고 마지막에 별도 append 한다.
  - 결과물에는 1회만 포함되며 중복은 아니다.
  - 다만 Appendix 내부 항목인지, 뒷표지 이후 별도 항목인지 해석이 필요한 상태다.
- 생성된 `book_manuscript/book.md`에는 소제목 정규화가 완전하지 않아 `### # 1)` 형태의 잘못된 heading이 다수 남아 있다.

## 6. Missing manuscript files referenced by `build_book.py`

없다.

`build_book.py`의 `PARTS` 및 별도 `BUILD_NOTE_FILE`에서 참조하는 Markdown 파일은 현재 모두 실존한다.

## 7. Manuscript files that exist but are not included in `build_book.py`

- `book_manuscript/99_appendix/99_제작_노트_의공구_Book_Pipeline.md`
  - `PARTS` 목록에는 없지만, 스크립트 말미에서 별도 append 된다.
- `book_manuscript/README.md`
  - 관리 문서이므로 합본 대상이 아니다.
- `book_manuscript/book.md`
  - 합본 산출물이므로 입력 장 목록에는 포함되지 않는다.

## 8. Stale management notes

- `book_manuscript/README.md` 메모 섹션의 “복제했다” 설명은 현재 source-of-truth 설명으로는 약하다.
- `tasks/todo.md`는 2026-06-06 기준 점검 상태를 유지하고 있어, InDesign handoff 단계 기준으로는 다음 단계 분리가 더 필요하다.
- 루트 `todo.md`는 기록용으로 남아 있으며, 현재 운영 기준 문서는 `tasks/todo.md`다.

## 9. Likely title inconsistencies, especially Part 6 naming

- Part 6 이름은 현재 문서 간 일치한다: `AI 시대에 살아남는 것`
- 디렉터리명은 `book_manuscript/06_AI_시대에도_남는_것/`이다.
  - 표시 제목과 폴더명은 다르지만, 파일 rename 없이 유지하는 쪽이 현재 규칙에 맞다.
- `build_book.py`의 appendix 표시는 `부록 (Appendix)`이고, `book_manuscript/README.md`는 `Appendix`, `README.md`는 `부록`으로 표기한다.
  - 의미상 문제는 없지만 표기 일관성은 완전하지 않다.

## 10. Recommended next actions

1. `build_book.py`의 소제목 정규화 로직을 기계적으로 수정한다.
2. 수정 후 `book_manuscript/book.md`를 다시 생성하고 heading 오염이 해소됐는지 확인한다.
3. `tasks/todo.md`를 InDesign handoff 단계 기준으로 다시 구분한다.
4. 자산 참조 감사 후 missing/unused/rename suggestion을 별도 보고서로 분리한다.
5. 최종 빌드를 다시 실행해 build status를 현재 시점 기준으로 재기록한다.
