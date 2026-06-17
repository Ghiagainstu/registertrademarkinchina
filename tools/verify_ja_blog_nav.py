from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    ok = 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>' in text
    print(p.name, 'ok' if ok else 'missing')
