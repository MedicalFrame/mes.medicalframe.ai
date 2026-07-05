import os
import glob
import re

MANUSCRIPT_DIR = "book_manuscript"

def analyze_headings():
    md_files = glob.glob(f"{MANUSCRIPT_DIR}/**/*.md", recursive=True)
    md_files.sort()
    
    results = []
    
    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        
        current_heading = "Start of Document"
        current_section_lines = 0
        current_section_chars = 0
        current_section_start_line = 0
        
        file_results = []
        
        for i, line in enumerate(lines):
            # Check for H2 or H3
            if line.startswith('## ') or line.startswith('### '):
                # Save previous section if it's long enough
                if current_section_lines > 30 or current_section_chars > 1500:
                    file_results.append({
                        'heading': current_heading,
                        'lines': current_section_lines,
                        'chars': current_section_chars,
                        'start_line': current_section_start_line
                    })
                
                # Start new section
                current_heading = line.strip()
                current_section_lines = 0
                current_section_chars = 0
                current_section_start_line = i + 1
            else:
                if line.strip(): # non-empty line
                    current_section_lines += 1
                    current_section_chars += len(line)
        
        # Add the last section
        if current_section_lines > 30 or current_section_chars > 1500:
            file_results.append({
                'heading': current_heading,
                'lines': current_section_lines,
                'chars': current_section_chars,
                'start_line': current_section_start_line
            })
            
        if file_results:
            results.append({
                'file': filepath,
                'sections': file_results
            })
            
    # Print results
    print("## Subheading Length Analysis\n")
    for res in results:
        print(f"### {res['file']}")
        for sec in res['sections']:
            print(f"- **{sec['heading']}** (Line {sec['start_line']}): {sec['lines']} lines, {sec['chars']} characters")
        print()

if __name__ == "__main__":
    analyze_headings()
