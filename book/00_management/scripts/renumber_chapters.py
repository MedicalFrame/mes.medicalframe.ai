import os
import re
import ast
import json

def format_parts(parts):
    lines = ["PARTS = ["]
    for part in parts:
        lines.append("    {")
        lines.append(f'        "title": "{part["title"]}",')
        lines.append(f'        "is_part": {str(part["is_part"])},')
        lines.append(f'        "dir": "{part["dir"]}",')
        lines.append('        "files": [')
        for f in part["files"]:
            lines.append(f'            "{f}",')
        lines.append('        ],')
        lines.append("    },")
    lines.append("]")
    return "\n".join(lines)

def process_book():
    base_dir = "/Users/jsbang/Developer/의공구"
    build_script = os.path.join(base_dir, "00_management/scripts/build_book.py")
    
    with open(build_script, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract PARTS
    match = re.search(r"PARTS\s*=\s*(\[.*?\])\n\ndef ", content, re.DOTALL)
    if not match:
        print("Could not find PARTS block")
        return
        
    parts_str = match.group(1)
    parts = ast.literal_eval(parts_str)
    
    new_parts = []
    
    for part in parts:
        new_part = dict(part)
        if part.get("is_part") and "appendix" not in part.get("dir"):
            new_files = []
            for i, old_filename in enumerate(part["files"], 1):
                name_without_prefix = re.sub(r'^\d+_', '', old_filename)
                new_filename = f"{i:02d}_{name_without_prefix}"
                new_files.append(new_filename)
                
                old_filepath = os.path.join(base_dir, "book_manuscript", part["dir"], old_filename)
                new_filepath = os.path.join(base_dir, "book_manuscript", part["dir"], new_filename)
                
                if not os.path.exists(old_filepath):
                    print(f"Warning: {old_filepath} does not exist.")
                    new_files[-1] = old_filename # revert if not found
                    continue
                
                with open(old_filepath, 'r', encoding='utf-8') as mf:
                    md_content = mf.read()
                
                lines = md_content.splitlines()
                replaced = False
                for j, line in enumerate(lines):
                    if line.startswith("## "):
                        title_match = re.match(r"^##\s+(?:\d+\.\s*)?(.*)$", line)
                        if title_match:
                            clean_title = title_match.group(1).strip()
                            lines[j] = f"## {i}. {clean_title}"
                            replaced = True
                        break
                        
                md_content = "\n".join(lines)
                
                if "AI에게 일을 맡긴다는 건" in name_without_prefix:
                    md_content = md_content.replace("프롬프트는 주문이 아니라 업무 지시서다", "### 1) 프롬프트는 주문이 아니라 업무 지시서다")
                    md_content = md_content.replace("AI는 자연어와 기계의 작업 언어 사이에 있는 번역기다", "### 2) AI는 자연어와 기계의 작업 언어 사이에 있는 번역기다")
                    md_content = md_content.replace("긴 작업은 한 번에 시키지 말고 파이프라인으로 나눈다", "### 3) 긴 작업은 한 번에 시키지 말고 파이프라인으로 나눈다")
                    md_content = md_content.replace("실제 작업 로그: 책 한 권을 AI와 같이 빌드하기", "### 4) 실제 작업 로그: 책 한 권을 AI와 같이 빌드하기")
                    md_content = md_content.replace("모델마다 다른 직원을 배치한다", "### 5) 모델마다 다른 직원을 배치한다")
                    md_content = md_content.replace("책임은 결국 사람에게 있다", "### 6) 책임은 결국 사람에게 있다")

                with open(old_filepath, 'w', encoding='utf-8') as mf:
                    mf.write(md_content)
                
                if old_filename != new_filename:
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed {old_filename} -> {new_filename}")
                    
            new_part["files"] = new_files
        new_parts.append(new_part)
        
    parts_py = format_parts(new_parts)
    new_build_content = content[:match.start()] + parts_py + "\n\ndef " + content[match.end():]
    
    with open(build_script, 'w', encoding='utf-8') as f:
        f.write(new_build_content)
        
    print("Updated build_book.py")

if __name__ == "__main__":
    process_book()
