import urllib.request, re
url1='http://localhost:8081/blog/madrid-vs-direct-filing-china.html'
url2='http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html'
html1=urllib.request.urlopen(url1).read().decode('utf-8','ignore')
html2=urllib.request.urlopen(url2).read().decode('utf-8','ignore')
def extract(html):
    s=html.index('<main id="main-content"')
    e=html.index('<div class="section-divider', s)
    return html[s:e]
print(extract(html1)==extract(html2))
print(extract(html1))
print(extract(html2))
