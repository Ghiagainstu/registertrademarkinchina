import urllib.request, re
urls = [
    'http://localhost:8081/blog/ja/index.html',
    'http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html',
    'http://localhost:8081/blog/ja/madrid-vs-direct-filing-china.html'
]
for url in urls:
    html = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    print(url)
    if 'index.html' in url:
        hrefs = re.findall(r'<a href="([^"]+)" class="post-card ', html)
        print('order', hrefs)
    print('blog highlight', html.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>'))
    print('select language', html.count('aria-label="Select language"'))
    print('duplicate class', html.count('data-lang="en" class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors"'))
