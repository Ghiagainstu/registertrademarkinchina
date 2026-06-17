from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    dup = text.count('data-lang="en" class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors"')
    print(p.name, dup)
