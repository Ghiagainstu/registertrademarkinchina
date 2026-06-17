import urllib.request, re
for url in [
    'http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html',
    'http://localhost:8081/blog/ja/who-can-register-trademark-in-china.html',
    'http://localhost:8081/blog/ja/china-trademark-monitoring-protection.html',
    'http://localhost:8081/blog/ja/common-reasons-trademark-rejection-china.html',
    'http://localhost:8081/blog/ja/how-long-trademark-registration-china.html',
    'http://localhost:8081/blog/ja/how-much-trademark-registration-cost-china.html'
]:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    bad=[]
    idx=0
    while True:
        i=html.find('<p',idx)
        if i==-1: break
        j=html.find('</p>',i)
        if j==-1: break
        seg=html[i:j+4]
        if '?'*5 in seg:
            bad.append(seg[:120])
        idx=j+4
    print(url.split('/')[-1], len(bad))
