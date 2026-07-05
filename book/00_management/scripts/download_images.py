import os
import re
import urllib.request
import ssl
from urllib.parse import urlparse, parse_qs

# macOS 환경의 Python 인증서 오류(SSL: CERTIFICATE_VERIFY_FAILED)를 우회하기 위한 설정
ssl_context = ssl._create_unverified_context()

manuscript_dir = "/Users/jsbang/Developer/의공구/book_manuscript"
assets_dir = "/Users/jsbang/Developer/의공구/assets/images"

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

# Regex to match Markdown images
image_pattern = re.compile(r'!\[([^\]]*)\]\((https://img1\.daumcdn\.net[^)]+)\)')

def get_filename_from_url(url):
    # daumcdn URLs often have the real URL in fname parameter
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    if 'fname' in qs:
        real_url = qs['fname'][0]
        return os.path.basename(urlparse(real_url).path)
    # fallback
    return os.path.basename(parsed.path)

for root, dirs, files in os.walk(manuscript_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            matches = image_pattern.findall(content)
            if not matches:
                continue

            new_content = content
            for alt_text, url in matches:
                filename = get_filename_from_url(url)
                if not filename or filename == '':
                    import hashlib
                    filename = hashlib.md5(url.encode()).hexdigest() + ".png"
                
                # Make sure filename is safe
                filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
                
                download_path = os.path.join(assets_dir, filename)
                
                # Download if not exists
                if not os.path.exists(download_path):
                    print(f"Downloading {url} to {download_path}")
                    try:
                        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, context=ssl_context) as response, open(download_path, 'wb') as out_file:
                            data = response.read()
                            out_file.write(data)
                    except Exception as e:
                        print(f"Failed to download {url}: {e}")
                        continue
                
                # Replace in content
                # Calculate relative path from markdown file to assets dir
                rel_assets_dir = os.path.relpath(assets_dir, root)
                new_image_path = os.path.join(rel_assets_dir, filename)
                
                # Replace the exact url match
                # Use a specific replace to avoid messing up other links
                old_str = f"![{alt_text}]({url})"
                new_str = f"![{alt_text}]({new_image_path})"
                new_content = new_content.replace(old_str, new_str)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

print("Done.")
