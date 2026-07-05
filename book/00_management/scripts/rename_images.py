import os
import re
import shutil

manuscript_dir = "/Users/jsbang/Developer/의공구/book_manuscript"
assets_images_dir = "/Users/jsbang/Developer/의공구/assets/images"

# Mapping from part of Korean filename to English slug
slug_mapping = {
    "의료_텍스트는_왜_바로_데이터가_되지_않는가": "medical_text_data",
    "CleanText": "cleantext",
    "CleanEMR": "cleanemr",
    "DiaFrame": "diaframe",
    "PharmaFrame": "pharmaframe",
    "수술_전_약을_끊는다는_것": "surgery_cessation",
    "모델은_처음부터_맞지_않는다": "model_reality",
    "어떤_의사가_될_것인가": "future_doctor",
    "임상_디지털_트윈_설계자": "clinical_digital_twin",
    "HAOS": "haos",
    "OpenClaw_그리고_춘식이": "openclaw",
    "모델링과_확률적_판단": "modeling_probabilistic",
    "VoiceGrape": "voicegrape",
    "NeuroFrame": "neuroframe",
    "EstroFrame": "estroframe",
    "구조화의_힘": "structuring_power",
    "Anki": "anki",
    "JLPT": "jlpt",
    "사진도_구조를_보는_일이다": "photography"
}

def get_slug(filename):
    for key, slug in slug_mapping.items():
        if key in filename:
            return slug
    return "image"

def get_suffix(alt_text):
    if not alt_text:
        return ""
    alt = alt_text.lower()
    if "첫 화면" in alt or "대시보드" in alt or "메인" in alt or "ui" in alt:
        return "_main"
    if "결과" in alt or "리포트" in alt:
        return "_report"
    if "구조" in alt or "개념도" in alt:
        return "_architecture"
    if "비교" in alt:
        return "_comparison"
    return ""

# Pattern to find markdown images pointing to assets/images
# format: ![alt_text](../../assets/images/HASH.ext)
image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]*assets/images/([^)]+))\)')

for root, dirs, files in os.walk(manuscript_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            slug = get_slug(file)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            matches = image_pattern.findall(content)
            if not matches:
                continue

            new_content = content
            idx = 1
            for alt_text, full_url, filename in matches:
                # If filename is already sensible (not a long hash), skip
                # Daum CDN hashes are usually 20+ chars
                name, ext = os.path.splitext(filename)
                if len(name) < 15 and not name.startswith("IMG_"):
                    continue
                
                suffix = get_suffix(alt_text)
                
                new_filename = f"{slug}{suffix}_{idx:02d}{ext}"
                new_full_url = full_url.replace(filename, new_filename)
                
                old_image_path = os.path.join(assets_images_dir, filename)
                new_image_path = os.path.join(assets_images_dir, new_filename)
                
                # Rename the file if the old file exists
                if os.path.exists(old_image_path):
                    shutil.move(old_image_path, new_image_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                else:
                    if os.path.exists(new_image_path):
                        print(f"File already renamed: {new_filename}")
                    else:
                        print(f"Warning: could not find {old_image_path}")
                
                # Replace in markdown content
                old_str = f"![{alt_text}]({full_url})"
                new_str = f"![{alt_text}]({new_full_url})"
                new_content = new_content.replace(old_str, new_str)
                idx += 1
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated links in {filepath}")

print("Image renaming process completed.")
