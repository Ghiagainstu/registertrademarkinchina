import urllib.request, re
for url in ['http://localhost:8081/blog/madrid-vs-direct-filing-china.html','http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html']:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(url.split('/')[-1], re.findall(r'<section class="section-block[^"]*"', html))
