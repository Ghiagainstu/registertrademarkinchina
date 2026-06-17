from pathlib import Path
for name in ['china-first-to-file-trademark-guide.html','who-can-register-trademark-in-china.html']:
    p = Path('dist/blog/ja')/name
    text = p.read_text(encoding='utf-8')
    bad=[]
    idx=0
    while True:
        i=text.find('<p', idx)
        if i==-1: break
        j=text.find('</p>', i)
        if j==-1: break
        seg=text[i:j+4]
        if '?'*5 in seg:
            bad.append(seg[:120])
        idx=j+4
    print(name, len(bad))
