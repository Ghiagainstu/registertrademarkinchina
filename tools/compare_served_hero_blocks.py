import urllib.request, re
for url in ['http://localhost:8081/blog/madrid-vs-direct-filing-china.html','http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html']:
    html = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    m = re.search(r'<main id=\"main-content\".*?</section>\s*<div class=\"section-divider', html, re.S)
    print(url)
    print(html[m.start():m.end()])
