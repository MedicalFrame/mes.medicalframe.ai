# MESbook

`MESbook`은 독립 출판 원고 프로젝트 **「의세계에 전생한 공학자는 자꾸 모델을 만든다」**를 관리하는 저장소입니다.

부제는 **의대생 엔지니어의 의료 구조화 노트**이며, Markdown 원고와 이미지 assets를 기반으로 책 원고를 편집하고 최종 산출물을 빌드합니다.

## 프로젝트 개요

- **원고 형식:** Markdown
- **이미지 자산:** `assets/`
- **원고 본체:** `book_manuscript/`
- **관리 문서:** `00_management/`
- **출력 산출물:** `output/`
- **빌드 결과:** `DOCX / PDF / EPUB`

## 폴더 구조

### `book_manuscript/`

- 실제 책 원고가 들어 있습니다.
- 파트별 챕터 원고, frontmatter, appendix, 합본용 `book.md`가 여기에 있습니다.
- 현재 합본 마크다운의 기준 파일은 `book_manuscript/book.md`입니다.

### `assets/`

- 본문에 들어가는 이미지 자산을 보관합니다.
- 현재는 주로 `assets/images/`를 사용합니다.

### `00_management/`

- 상태표, 매핑 문서, QA 리포트, 빌드 스크립트, 제작 노트 같은 운영 문서를 둡니다.
- 이미지 추가 아이디어와 프롬프트 정리는 `00_management/wiki_image_recommendations.md`에 있습니다.

### `output/`

- 최종 산출물 위치입니다.
- `MESbook.docx`, `MESbook.pdf`, `MESbook.epub`가 이 폴더에 생성됩니다.

### `legacy/`

- 이전 자료, 참고용 자원, 레거시 파일을 보관합니다.

## 책 구성

- 프롤로그
- Part 1. 왜 자꾸 모델을 만드는가
- Part 2. 구조로 공부하다
- Part 3. 사고를 구현하다
- Part 4. 기록은 곧바로 데이터가 되지 않는다
- Part 5. 약물은 점이 아니라 곡선이다
- Part 6. AI 시대에 살아남는 것
- 에필로그
- 부록
- 제작 노트

세부 목차와 원고 목록은 `book_manuscript/README.md`를 참고하면 됩니다.

## 빌드 방식

빌드는 두 단계로 구성됩니다.

1. `00_management/scripts/build_book.py`
   - 파트/챕터 원고를 모아 `book_manuscript/book.md`를 생성합니다.
2. `00_management/scripts/build_all.sh`
   - `book_manuscript/book.md`와 `assets`를 바탕으로 `Pandoc`으로 `DOCX / EPUB`를 생성한 뒤, `Microsoft Word`로 `PDF`를 내보냅니다.

## 빌드 명령

```bash
bash 00_management/scripts/build_all.sh
```

성공하면 아래 파일이 생성됩니다.

- `book_manuscript/book.md`
- `output/MESbook.docx`
- `output/MESbook.epub`
- `output/MESbook.pdf`

## 현재 빌드 파이프라인

`Markdown + assets -> Python build script -> Pandoc(DOCX/EPUB) -> Microsoft Word(PDF)`

## PDF 생성 메모

- `MESbook.pdf`는 `xelatex` 대신 `Microsoft Word`의 PDF 내보내기로 생성합니다.
- 스크립트 실행 시 macOS의 자동화 권한 요청이 뜰 수 있습니다.
- Word PDF 내보내기가 실패해도 `MESbook.docx`는 남으므로, 필요하면 Word에서 직접 PDF로 저장할 수 있습니다.

## 참고 문서

- 원고 목차: `book_manuscript/README.md`
- 이미지 추가 제안 및 프롬프트: `00_management/wiki_image_recommendations.md`
- 현재 빌드 기준 스크립트: `00_management/scripts/build_book.py`, `00_management/scripts/build_all.sh`
- 작업 TODO: `tasks/todo.md`
- 작업 교훈: `tasks/lessons.md`
