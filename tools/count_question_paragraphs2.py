import re, urllib.request
for url in ['http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html','http://localhost:8081/blog/ja/who-can-register-trademark-in-china.html']:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    bad=[]
    for m in re.finditer(r'<p[^>]*>.*?</p>', html, re.S):
        t=m.group(0)
        if '?'*5 in t:
            bad.append(t[:120])
    print(url.split('/')[-1], len(bad), bad[:3])
