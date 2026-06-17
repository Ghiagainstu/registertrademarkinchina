import urllib.request, re
base = 'http://localhost:8081/blog/ja/'
pages = [
    'china-first-to-file-trademark-guide.html',
    'china-trademark-classes-complete-guide.html',
    'china-trademark-monitoring-protection.html',
    'china-trademark-registration-complete-guide-2026.html',
    'common-reasons-trademark-rejection-china.html',
    'how-long-trademark-registration-china.html',
    'how-much-trademark-registration-cost-china.html',
    'madrid-vs-direct-filing-china.html',
    'who-can-register-trademark-in-china.html'
]
for name in pages:
    html = urllib.request.urlopen(base+name).read().decode('utf-8','ignore')
    print(name, 'blog', html.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>'), 'switcher', html.count('aria-label="Select language"'))
