from pathlib import Path
for name in ['china-trademark-monitoring-protection.html','common-reasons-trademark-rejection-china.html','how-long-trademark-registration-china.html','how-much-trademark-registration-cost-china.html']:
    p = Path('dist/blog/ja')/name
    text = p.read_text(encoding='utf-8')
    idx=0; bad=[]
    while True:
        i=text.find('<p',idx)
        if i==-1: break
        j=text.find('</p>',i)
        if j==-1: break
        seg=text[i:j+4]
        if '?'*5 in seg:
            bad.append(seg[:200])
        idx=j+4
    print('\n###', name)
    for s in bad:
        print(s)
