from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    style = 'gap1' if 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1"' in text else 'button'
    print(p.name, style)
