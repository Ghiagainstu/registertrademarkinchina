from pathlib import Path
p = Path('dist/blog/ja/china-trademark-registration-complete-guide-2026.html')
text = p.read_text(encoding='utf-8')
text = text.replace('<link rel="stylesheet" href="/styles/tailwind.css">\n', '')
p.write_text(text, encoding='utf-8')
print('removed local tailwind.css link')
