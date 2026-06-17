import urllib.request, re
pages = [
    'http://localhost:8081/blog/ja/china-first-to-file-trademark-guide.html',
    'http://localhost:8081/blog/ja/china-trademark-classes-complete-guide.html',
    'http://localhost:8081/blog/ja/china-trademark-monitoring-protection.html',
    'http://localhost:8081/blog/ja/china-trademark-registration-complete-guide-2026.html',
    'http://localhost:8081/blog/ja/common-reasons-trademark-rejection-china.html',
    'http://localhost:8081/blog/ja/how-long-trademark-registration-china.html',
    'http://localhost:8081/blog/ja/how-much-trademark-registration-cost-china.html',
    'http://localhost:8081/blog/ja/madrid-vs-direct-filing-china.html',
    'http://localhost:8081/blog/ja/who-can-register-trademark-in-china.html'
]
for url in pages:
    html=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(url.split('/')[-1], len(re.findall(r'<section class="section-block', html)), len(re.findall(r'id="key-takeaway"', html)))
