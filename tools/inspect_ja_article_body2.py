import urllib.request, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
for url in [
    'http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html',
    'http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html',
    'http://localhost:8081/blog/ja/who-can-register-trademark-in-china.html'
]:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    m=re.search(r'<div class="lg:col-span-3 article-body">(.*?)<aside class="toc-sidebar', html, re.S)
    print(url.split('/')[-1])
    snippet=m.group(1)[:1200]
    print(snippet)
