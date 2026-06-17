from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    ok1 = 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1"' in text
    ok2 = 'aria-label="Select language"' in text
    ok3 = 'data-lang="en" class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors"' not in text
    print(p.name, 'ok' if (ok1 and ok2 and ok3) else 'NO')
