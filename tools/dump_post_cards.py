import re, pathlib
for rel in ['dist/blog/ja/index.html','dist/blog/index.html']:
    text = pathlib.Path(rel).read_text(encoding='utf-8')
    hrefs = re.findall(r'<a href="([^"]+)" class="post-card ', text)
    if not hrefs:
        hrefs = re.findall(r'class="post-card [^"]*"[^>]*href="([^"]+)"', text)
    print(rel)
    for h in hrefs:
        print(h)
