from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    grid = text.count('lg:grid-cols-4')
    toc = text.count('toc-sidebar hidden lg:block')
    article = text.count('article-body')
    sections = text.count('section-block')
    print(p.name, grid=grid, toc=toc, article=article, sections=sections)
