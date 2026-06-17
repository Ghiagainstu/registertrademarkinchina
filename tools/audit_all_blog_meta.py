from pathlib import Path
for lang, base in [('en', Path('dist/blog')), ('ja', Path('dist/blog/ja'))]:
    print(lang)
    for p in sorted(base.glob('*.html')):
        if p.name=='index.html':
            continue
        text=p.read_text(encoding='utf-8')
        print(p.name, 'og:title' in text, 'twitter:title' in text)
