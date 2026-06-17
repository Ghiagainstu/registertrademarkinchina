from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    canonical_count = text.count('link rel="canonical"')
    og_count = text.count('og:title')
    blog_count = text.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>')
    switcher = text.count('aria-label="Select language"')
    print(p.name, canonical=canonical_count, og=og_count, blog=blog_count, switcher=switcher)
