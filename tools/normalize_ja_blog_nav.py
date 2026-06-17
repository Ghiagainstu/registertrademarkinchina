from pathlib import Path
changed=[]
for p in Path('dist/blog/ja').glob('*.html'):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    new=text.replace('class="text-brand">\u30d6\u30ed\u30b0</a>', 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>')
    if new!=text:
        p.write_text(new,encoding='utf-8')
        changed.append(p.name)
print('changed', len(changed))
for n in changed:
    print(n)
