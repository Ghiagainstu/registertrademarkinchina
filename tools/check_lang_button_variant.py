from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    print(p.name, 'button' if 'class="text-sm text-slate-400 hover:text-white transition-colors inline-flex items-center"' in text else 'gap1' if 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1"' in text else 'other')
