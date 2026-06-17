import urllib.request
for url in ['http://localhost:8081/blog/madrid-vs-direct-filing-china.html','http://localhost:8081/blog/ja/madrid-vs-direct-filing-china.html']:
    html = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(url)
    print('tailwind.css', '/styles/tailwind.css' in html)
    print('cdn', 'cdn.tailwindcss.com' in html)
    print('reading-progress', 'id="reading-progress"' in html)
    print('lang-switcher', 'id="lang-switcher"' in html)
