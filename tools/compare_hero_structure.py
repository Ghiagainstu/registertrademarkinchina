import urllib.request, re
from collections import Counter
url1='http://localhost:8081/blog/madrid-vs-direct-filing-china.html'
url2='http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html'
html1=urllib.request.urlopen(url1).read().decode('utf-8','ignore')
html2=urllib.request.urlopen(url2).read().decode('utf-8','ignore')
def extract(html):
    s=html.index('<main id="main-content"')
    e=html.index('<div class="section-divider', s)
    return html[s:e]
tags1=[m.group() for m in re.finditer(r'<[^ >]+[^>]*>', extract(html1))]
tags2=[m.group() for m in re.finditer(r'<[^ >]+[^>]*>', extract(html2))]
print('tag_count', len(tags1), len(tags2))
print('tags_equal_by_class', [t.split()[0] for t in tags1]==[t.split()[0] for t in tags2])
print(Counter(tags1)==Counter(tags2))
