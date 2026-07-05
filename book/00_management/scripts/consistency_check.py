import os
import re

manuscript_dir = "/Users/jsbang/Developer/의공구/book_manuscript"

replacements = {
    r"Clean Text": "CleanText",
    r"클린텍스트": "CleanText",
    r"클린 텍스트": "CleanText",
    r"Clean EMR": "CleanEMR",
    r"클린EMR": "CleanEMR",
    r"클린 EMR": "CleanEMR",
    r"다이아프레임": "DiaFrame",
    r"에스트로프레임": "EstroFrame",
    r"안드로프레임": "AndroFrame",
    r"파마프레임": "PharmaFrame",
    r"뉴로프레임": "NeuroFrame",
    r"보이스그레이프": "VoiceGrape",
    r"오픈클로": "OpenClaw",
    r"하오스": "HAOS",
    r"Jisong Cloud6\.0": "Jisong Cloud 6.0",
    r"(?i)\bhba1c\b": "HbA1c",
    r"(?i)\begfr\b": "eGFR",
    r"(?i)\buacr\b": "UACR",
    r"(?i)\bbmi\b": "BMI",
    r"(?i)\bfpg\b": "FPG",
    r"(?i)\bc-peptide\b": "C-peptide",
    r"(?i)\bsglt2\b": "SGLT2",
    r"(?i)\bglp-1\b": "GLP-1"
}

def fix_terminology():
    for root, dirs, files in os.walk(manuscript_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = content
                for pattern, repl in replacements.items():
                    # We don't want to replace inside URLs, so we'll use a hack or just accept that it might happen and revert if needed.
                    # Since medical abbreviations are unlikely to be in URLs, we can just do a regex sub.
                    new_content = re.sub(pattern, repl, new_content)

                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    fix_terminology()
    print("Terminology replacement completed.")
