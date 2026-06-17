from pathlib import Path
ja = Path('dist/blog/ja/china-trademark-registration-complete-guide-2026.html').read_text(encoding='utf-8')
en = Path('dist/blog/madrid-vs-direct-filing-china.html').read_text(encoding='utf-8')
print('JA tailwind', ja.count('cdn.tailwindcss.com'), ja.count('/styles/tailwind.css'))
print('EN tailwind', en.count('cdn.tailwindcss.com'), en.count('/styles/tailwind.css'))
print('JA reading-progress script', 'reading-progress' in ja, ja.count('reading-progress'))
print('EN reading-progress script', 'reading-progress' in en, en.count('reading-progress'))
