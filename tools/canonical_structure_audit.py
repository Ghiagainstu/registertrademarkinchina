from pathlib import Path
text = Path('dist/blog/madrid-vs-direct-filing-china.html').read_text(encoding='utf-8')
print('EN', text.count('lg:grid-cols-4'), text.count('toc-sidebar hidden lg:block'), text.count('article-body'), text.count('section-block'))
