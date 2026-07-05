import os
import re

book_path = "/Users/jsbang/Developer/의공구/book_manuscript/book.md"
report_path = "/Users/jsbang/Developer/의공구/00_management/qa_report.md"

if not os.path.exists(book_path):
    print("book.md not found.")
    exit(1)

with open(book_path, "r", encoding="utf-8") as f:
    content = f.read()

report_lines = ["# 최종 교정용 내비게이터 (QA Report)", ""]
report_lines.append("이 리포트는 기계적으로 탐지된 잠재적 오류 위치를 안내합니다. (원고 내용을 수정하지 않았습니다)")
report_lines.append("")

# 1. 괄호 짝 점검
report_lines.append("## 1. 괄호 짝 불일치 의심")
brackets = {'(': ')', '{': '}', '[': ']'}
lines = content.split('\n')
for i, line in enumerate(lines):
    for open_b, close_b in brackets.items():
        if line.count(open_b) != line.count(close_b):
            report_lines.append(f"- Line {i+1}: `{open_b}`와 `{close_b}` 개수 불일치 의심")
            report_lines.append(f"  > {line[:50]}...")
            
report_lines.append("")

# 2. 1줄 단락 연속 발생 점검 (책 호흡 점검)
report_lines.append("## 2. 1줄 단락 연속 발생 의심 (3회 이상 연속)")
paragraphs = re.split(r'\n\n+', content)
consecutive_short = 0
for p in paragraphs:
    if p.strip() == '' or p.startswith('#') or p.startswith('!') or p.startswith('<') or p.startswith('<!--') or p.startswith('-'):
        consecutive_short = 0
        continue
    if len(p.split('\n')) == 1:
        consecutive_short += 1
        if consecutive_short >= 3:
            report_lines.append(f"- 연속 1줄 단락 발생 의심: `{p[:50]}...`")
    else:
        consecutive_short = 0

with open(report_path, "w", encoding="utf-8") as f:
    f.write('\n'.join(report_lines))

print("QA Report generated.")
