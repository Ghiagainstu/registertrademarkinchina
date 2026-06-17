from pathlib import Path
for p in sorted(Path('dist/blog/ja').glob('*.html')):
    if p.name=='index.html':
        continue
    text=p.read_text(encoding='utf-8')
    idx=0; bad=[]
    while True:
        i=text.find('<p',idx)
        if i==-1: break
        j=text.find('</p>',i)
        if j==-1: break
        seg=text[i:j+4]
        if '?'*5 in seg:
            bad.append(seg[:80])
        idx=j+4
    if bad:
        print(p.name, len(bad))
