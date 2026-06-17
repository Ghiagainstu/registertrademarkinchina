from pathlib import Path
changed=[]
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    new = text.replace('aria-label="\u8a00\u8a9e\u9078\u629e"', 'aria-label="Select language"')
    new = new.replace('class="text-sm text-slate-400 hover:text-white transition-colors inline-flex items-center"', 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1"')
    new = new.replace('class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors" data-lang="en" class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors"', 'class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors" data-lang="en"')
    if new != text:
        p.write_text(new, encoding='utf-8')
        changed.append(p.name)
print('changed', len(changed))
for n in changed:
    print(n)
