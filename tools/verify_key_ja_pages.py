import urllib.request
for url in [
    'http://localhost:8081/blog/ja/index.html',
    'http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html',
    'http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html',
    'http://localhost:8081/blog/ja/madrid-vs-direct-filing-china.html'
]:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(url.split('/')[-1], 'blogHighlight', html.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>'), 'switcher', html.count('aria-label="Select language"'))
