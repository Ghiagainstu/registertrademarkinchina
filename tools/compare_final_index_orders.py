import re, pathlib
ja = pathlib.Path('dist/blog/ja/index.html').read_text(encoding='utf-8')
en = pathlib.Path('dist/blog/index.html').read_text(encoding='utf-8')
ja_cards = re.findall(r'<a href="(/blog/ja/[^"]+)" class="post-card .*?</a>\s*', ja, re.S)
en_cards = re.findall(r'<a href="(/blog/[^"]+)" class="post-card .*?</a>\s*', en, re.S)
print('JA order')
for c in ja_cards:
    print(re.search(r'href="([^"]+)"', c).group(1))
print('EN order')
for c in en_cards:
    print(re.search(r'href="([^"]+)"', c).group(1))
