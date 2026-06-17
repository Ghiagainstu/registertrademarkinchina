from pathlib import Path
for p in sorted(Path('dist/blog').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    print(p.name, 'og:title' in text, 'twitter:title' in text)
