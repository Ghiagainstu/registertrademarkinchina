import re, pathlib
for rel in ['dist/blog/ja/index.html','dist/blog/index.html']:
    text = pathlib.Path(rel).read_text(encoding='utf-8')
    hrefs = re.findall(r'<a href="(/blog/ja/[^"]+)" class="post-card ', text)
    if not hrefs:
        hrefs = re.findall(r'<a href="(/blog/[^"]+)" class="post-card ', text)
    print(rel)
    print('\n'.join(hrefs))
