# Build Result

기준일: 2026-06-07

## Command run

```bash
bash 00_management/scripts/build_all.sh
```

## Result

- success: yes
- exit_code: 0

## Output log

```text
1. 마크다운 합본 (book.md) 생성 중...
Book compiled successfully to /Users/jsbang/Developer/MESbook/book_manuscript/book.md
2. DOCX 생성 중...
3. EPUB 생성 중...
4. PDF 생성 중... (engine: xelatex)
모든 빌드 완료!
- DOCX: /Users/jsbang/Developer/MESbook/output/book.docx
- EPUB: /Users/jsbang/Developer/MESbook/output/book.epub
- PDF:  /Users/jsbang/Developer/MESbook/output/book.pdf
```

## Output artifacts

- `output/book.docx`: 42103310 bytes, modified `2026-06-07T13:38:55`
- `output/book.epub`: 23814953 bytes, modified `2026-06-07T13:38:55`
- `output/book.pdf`: 19448888 bytes, modified `2026-06-07T13:40:15`

## Likely cause if this later fails

- `user/의공모.docx` missing
- `pandoc` missing
- PDF engine or local font path unavailable
- case-sensitive filesystem exposing `.PNG` vs `.png` reference mismatches
