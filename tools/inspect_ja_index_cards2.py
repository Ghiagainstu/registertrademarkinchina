import pathlib, re
ja = pathlib.Path('dist/blog/ja/index.html').read_text(encoding='utf-8')
start = ja.index('<a href="/blog/ja/china-trademark-registration-complete-guide-2026.html" class="post-card')
pat = re.compile(r'<a href="/blog/ja/[^"]+" class="post-card .*?</a>\s*', re.S)
matches = [(m.group(), m.start(), m.end()) for m in pat.finditer(ja, start)]
print('count', len(matches))
for i,(g,s,e) in enumerate(matches[:3],1):
    href = re.search(r'href="([^"]+)"', g).group(1)
    print(i, s, e, href)
print('last', matches[-1][1], matches[-1][2], re.search(r'href="([^"]+)"', matches[-1][0]).group(1))
