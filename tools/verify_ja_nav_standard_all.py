from pathlib import Path
for p in [Path('dist/blog/ja/index.html')]+sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html' and str(p).endswith('index.html'):
        pass
    text=p.read_text(encoding='utf-8')
    print(p.name, text.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>'), text.count('aria-label="Select language"'))
