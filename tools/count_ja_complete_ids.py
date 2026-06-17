import pathlib
text = pathlib.Path('dist/blog/ja/china-trademark-registration-complete-guide-2026.html').read_text(encoding='utf-8')
print(text.count('id="reading-progress"'))
print(text.count('id="mobile-menu-btn"'))
print(text.count('id="lang-switcher"'))
