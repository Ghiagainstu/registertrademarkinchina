from pathlib import Path
text = Path('dist/blog/ja/index.html').read_text(encoding='utf-8')
print(text.count('aria-label="Select language"'))
print(text.count('class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>'))
print(text.count('data-lang="en" class='))
