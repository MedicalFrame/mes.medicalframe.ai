#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"
BOOK_MD="$BASE_DIR/book_manuscript/book.md"
DOCX_OUT="$OUTPUT_DIR/MESbook.docx"
EPUB_OUT="$OUTPUT_DIR/MESbook.epub"
PDF_OUT="$OUTPUT_DIR/MESbook.pdf"
REFERENCE_DOC="$BASE_DIR/user/의공모.docx"
COVER_IMAGE="$BASE_DIR/assets/앞표지.jpg"

mkdir -p "$OUTPUT_DIR"

echo "1. 마크다운 합본 (book.md) 생성 중..."
python3 "$BASE_DIR/00_management/scripts/build_book.py"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "오류: pandoc이 설치되어 있지 않아 빌드를 진행할 수 없습니다."
  exit 1
fi

PANDOC_COMMON_ARGS=(
  "$BOOK_MD"
  --standalone
  --from markdown
  --toc
  --toc-depth=2
  --metadata=title:"의세계에 전생한 공학자는 자꾸 모델을 만든다"
  --metadata=subtitle:"의대생 엔지니어의 의료 구조화 노트"
  --metadata=lang:ko
  --metadata=toc-title:목차
  --resource-path="$BASE_DIR:$BASE_DIR/book_manuscript:$BASE_DIR/assets"
)

echo "2. DOCX 생성 중..."
pandoc \
  "${PANDOC_COMMON_ARGS[@]}" \
  --reference-doc="$REFERENCE_DOC" \
  -o "$DOCX_OUT"

echo "3. EPUB 생성 중..."
pandoc \
  "${PANDOC_COMMON_ARGS[@]}" \
  --epub-cover-image="$COVER_IMAGE" \
  -o "$EPUB_OUT"

if ! command -v osascript >/dev/null 2>&1; then
  echo "오류: macOS osascript를 찾지 못해 Word PDF 내보내기를 진행할 수 없습니다."
  exit 1
fi

echo "4. Word로 PDF 생성 중..."
if ! osascript <<EOF
set docxPath to POSIX file "$DOCX_OUT"
set pdfPath to POSIX file "$PDF_OUT"

tell application "Microsoft Word"
  activate
  open docxPath
  set sourceDoc to active document
  save as sourceDoc file name pdfPath file format format PDF
  close sourceDoc saving no
end tell
EOF
then
  echo "오류: Microsoft Word PDF 내보내기에 실패했습니다."
  echo "DOCX는 생성되었으니 Word에서 직접 PDF로 저장할 수 있습니다: $DOCX_OUT"
  exit 1
fi

echo "모든 빌드 완료!"
echo "- DOCX: $DOCX_OUT"
echo "- EPUB: $EPUB_OUT"
echo "- PDF:  $PDF_OUT"
