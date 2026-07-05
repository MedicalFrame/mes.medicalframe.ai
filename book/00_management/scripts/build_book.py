from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT_DIR = PROJECT_ROOT / "book_manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "book.md"
BUILD_NOTE_FILE = PROJECT_ROOT / "book_manuscript" / "99_appendix" / "99_제작_노트_의공구_Book_Pipeline.md"

# Pandoc treats a standalone form-feed character as a page break in DOCX/EPUB.
PAGE_BREAK = "\f"

PARTS = [
    {
        "title": "프롤로그",
        "is_part": False,
        "dir": "00_frontmatter",
        "files": [
            "00_프롤로그_의세계에_전생했다는_것_축약판.md",
        ],
    },
    {
        "title": "Part 1. 왜 자꾸 모델을 만드는가",
        "is_part": True,
        "dir": "01_왜_자꾸_모델을_만드는가",
        "files": [
            "01_의대생이_공학을_놓지_않는_이유.md",
            "02_공학적_사고란_무엇인가.md",
            "03_나는_왜_모델을_좋아하는가.md",
            "04_의료를_구조화한다는_것.md",
        ],
    },
    {
        "title": "Part 2. 구조로 공부하다",
        "is_part": True,
        "dir": "02_구조로_공부하다",
        "files": [
            "01_공부를_구조로_바라본다는_것.md",
            "02_암기와_이해는_다른_층위.md",
            "03_실습은_사고의_전환점.md",
            "04_구조화의_힘.md",
            "05_Anki는_구조_관리_도구.md",
            "06_AI를_도구로_쓰는_공부.md",
            "07_좋은_질문은_무엇일까.md",
            "08_가르친다는_것은_구조를_다시_짓는_일이다.md",
        ],
    },
    {
        "title": "Part 3. 사고를 구현하다",
        "is_part": True,
        "dir": "03_사고를_구현하다",
        "files": [
            "01_사고를_구현한다는_것.md",
            "02_구체화와_자동화.md",
            "03_집이_살아있다_HAOS.md",
            "04_작업용_개인_클라우드_Jisong_Cloud_6_0.md",
            "05_OpenClaw_그리고_춘식이.md",
            "06_모델링과_확률적_판단.md",
            "07_감각의_객관화_VoiceGrape.md",
            "08_상태를_모델로_NeuroFrame.md",
            "09_CDSS_prototype_EstroFrame.md",
        ],
    },
    {
        "title": "Part 4. 기록은 곧바로 데이터가 되지 않는다",
        "is_part": True,
        "dir": "04_기록은_곧바로_데이터가_되지_않는다",
        "files": [
            "01_감각에서_수치로_수치에서_예측으로.md",
            "02_의료_텍스트는_왜_바로_데이터가_되지_않는가.md",
            "03_로컬_기반_EMR_파싱_CleanText.md",
            "04_EMR_연구용_파싱_CleanEMR.md",
            "05_머신러닝_기반_당뇨_약물_추천_DiaFrame.md",
        ],
    },
    {
        "title": "Part 5. 약물은 점이 아니라 곡선이다",
        "is_part": True,
        "dir": "05_약물은_점이_아니라_곡선이다",
        "files": [
            "01_다학제_약제_PK_분석_PharmaFrame.md",
            "02_수술_전_약을_끊는다는_것.md",
            "03_모델은_처음부터_맞지_않는다.md",
        ],
    },
    {
        "title": "Part 6. AI 시대에 살아남는 것",
        "is_part": True,
        "dir": "06_AI_시대에도_남는_것",
        "files": [
            "01_AI에게 일을 맡긴다는 건, 좋은 상사가 되는 일이다.md",
            "02_판단은_설명될_때_완성된다.md",
            "03_어떤_의사가_될_것인가.md",
            "04_임상_디지털_트윈_설계자.md",
        ],
    },
    {
        "title": "에필로그",
        "is_part": False,
        "dir": "00_frontmatter",
        "files": [
            "99_에필로그_두_세계를_오가는_마법진.md",
        ],
    },
    {
        "title": "부록 (Appendix)",
        "is_part": True,
        "dir": "99_appendix",
        "files": [
            "01_하루_30분_1년_반_JLPT_N1까지.md",
            "02_Obsidian_PKM_연결을_관리하기.md",
            "03_도메인을_산다는_것.md",
            "04_사고_보조_장치_Antigravity_IDE.md",
            "05_사진도_구조를_보는_일이다.md",
        ],
    },
]

def clean_markdown(content: str) -> str:
    content = content.replace("\r\n", "\n")
    content = content.replace("../../assets/images", "assets/images")
    content = re.sub(r'(?m)^\\newpage\s*$', PAGE_BREAK, content)
    content = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', r'![](\1)', content)
    content = re.sub(r'(\!\[\]\([^)]+\))(?=[^\s\n])', r"\1\n", content)
    content = re.sub(r'(\!\[\]\([^)]+\))([^\n]+)', r"\1\n\n\2", content)
    content = re.sub(r'([^\n])\n(!\[)', r'\1\n\n\2', content)
    content = re.sub(r'(\n!\[\]\([^)]+\))(\n[^\n])', r'\1\n\2', content)
    content = re.sub(r'(?m)^image\.(png|jpe?g|PNG|JPG|JPEG)\s*$', '', content)
    content = re.sub(r'(?m)^---\s*$', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def extract_first_heading(content: str) -> tuple[str | None, str]:
    lines = content.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^##?\s+(.+?)\s*$", line)
        if match:
            title = match.group(1).strip()
            remaining = "\n".join(lines[:index] + lines[index + 1:]).strip()
            return title, remaining
    return None, content.strip()


def extract_leading_plain_title(content: str) -> tuple[str | None, str]:
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if line.strip():
            title = line.strip()
            remaining = "\n".join(lines[:index] + lines[index + 1:]).strip()
            return title, remaining
    return None, content.strip()


def normalize_inner_headings(content: str) -> str:
    normalized_lines = []
    for line in content.splitlines():
        stripped = line.strip()
        if re.match(r"^#{2,}\s+", stripped):
            heading_text = re.sub(r"^#{2,}\s+", "", stripped).strip()
            heading_text = re.sub(r"^#+\s*", "", heading_text).strip()
            while True:
                bold_match = re.match(r"^\*\*(.+?)\*\*$", heading_text)
                if not bold_match:
                    break
                heading_text = bold_match.group(1).strip()
            heading_text = re.sub(r"^#+\s*", "", heading_text).strip()
            normalized_lines.append(f"### {heading_text}")
        else:
            normalized_lines.append(line)
    normalized = "\n".join(normalized_lines)
    normalized = re.sub(r'\n{3,}', '\n\n', normalized)
    return normalized.strip()


def add_subsection_page_breaks(content: str) -> str:
    lines = content.splitlines()
    sections: list[tuple[str | None, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if re.match(r"^###\s+", line.strip()):
            sections.append((current_heading, current_lines))
            current_heading = line
            current_lines = []
            continue
        current_lines.append(line)
    sections.append((current_heading, current_lines))

    rebuilt: list[str] = []
    if sections:
        intro_heading, intro_lines = sections[0]
        if intro_heading:
            rebuilt.append(intro_heading)
        if intro_lines:
            rebuilt.append("\n".join(intro_lines).strip())

    for index in range(1, len(sections)):
        heading, body_lines = sections[index]
        if heading is None:
            continue
        current_text = "\n".join(body_lines).strip()
        rebuilt.append(PAGE_BREAK)
        rebuilt.append(heading)
        if current_text:
            rebuilt.append(current_text)

    combined = "\n\n".join(
        block for block in rebuilt if block == PAGE_BREAK or block.strip()
    )
    combined = re.sub(r'\n{3,}', '\n\n', combined)
    return combined.strip()


def build_section(relative_path: str, fallback_title: str, heading_level: int) -> str:
    filepath = MANUSCRIPT_DIR / relative_path
    if not filepath.exists():
        raise FileNotFoundError(f"Missing manuscript file: {filepath}")

    content = filepath.read_text(encoding="utf-8")
    content = clean_markdown(content)
    title, body = extract_first_heading(content)
    if title is None and heading_level == 1:
        plain_title, plain_body = extract_leading_plain_title(content)
        if plain_title:
            title, body = plain_title, plain_body
    heading_text = title or fallback_title
    body = normalize_inner_headings(body)
    body = add_subsection_page_breaks(body)

    heading_prefix = "#" * heading_level
    if body:
        return f"{heading_prefix} {heading_text}\n\n{body}".strip()
    return f"{heading_prefix} {heading_text}"


def build_book() -> str:
    book_content = []

    def append_page_break() -> None:
        if not book_content or book_content[-1] != PAGE_BREAK:
            book_content.append(PAGE_BREAK)

    book_content.append("![](assets/앞표지.jpg)")
    append_page_break()
    book_content.append("의세계에 전생한 공학자는 자꾸 모델을 만든다")
    book_content.append("의대생 엔지니어의 의료 구조화 노트")
    append_page_break()

    for part in PARTS:
        if part["is_part"]:
            append_page_break()
            book_content.append(f"# {part['title']}")

        for filename in part["files"]:
            relative_path = f"{part['dir']}/{filename}"
            append_page_break()
            if part["is_part"]:
                book_content.append(build_section(relative_path, filename, 2))
            else:
                book_content.append(build_section(relative_path, part["title"], 1))

    if BUILD_NOTE_FILE.exists():
        append_page_break()
        book_content.append(clean_markdown(BUILD_NOTE_FILE.read_text(encoding="utf-8")))
    append_page_break()
    book_content.append("![뒷표지](assets/뒷표지.jpg)")
    return "\n\n".join(book_content).strip() + "\n"


def main() -> None:
    OUTPUT_FILE.write_text(build_book(), encoding="utf-8")
    print(f"Book compiled successfully to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
