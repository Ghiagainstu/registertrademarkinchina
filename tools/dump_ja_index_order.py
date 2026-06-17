import re, pathlib
text = pathlib.Path('dist/blog/ja/index.html').read_text(encoding='utf-8')
print('\n'.join(re.findall(r'<a href="(/blog/ja/[^"]+)" class="post-card ', text)))
