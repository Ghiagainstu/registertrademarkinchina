import pathlib, re
ja = pathlib.Path('dist/blog/ja/index.html').read_text(encoding='utf-8')
start = ja.index('<a href="/blog/ja/china-trademark-registration-complete-guide-2026.html" class="post-card')
end_match = re.search(r'<a href="/blog/ja/madrid-vs-direct-filing-china.html" class="post-card .*?</a>\s*', ja, re.S)
print('start', start)
print('end', end_match.end())
print(ja[start:end_match.end()][:1200])
