from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    checks = {
        'article-body': '.article-body' in text,
        'section-block': '.section-block' in text,
        'summary-tiles': 'summary-tiles' in text,
        'comparison-grid': 'comparison-grid' in text,
        'comparison-card': 'comparison-card' in text,
        'step-num': 'step-num' in text,
        'callout-icon': 'callout-icon' in text,
    }
    print(p.name, checks)
