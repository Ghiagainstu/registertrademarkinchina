from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    has_cdncdn = text.count('cdn.tailwindcss.com')
    has_localcss = '/styles/tailwind.css' in text
    print(p.name, 'cdn', has_cdncdn, 'local', has_localcss)
