from pathlib import Path
p = Path('dist/blog/ja/china-trademark-registration-complete-guide-2026.html')
text = p.read_text(encoding='utf-8')
marker = '<link rel="stylesheet" href="/styles/tailwind.css">'
idx = text.find(marker)
print('idx', idx)
print(text[idx-300:idx+300])
