from pathlib import Path
p = Path('dist/blog/ja/china-trademark-registration-complete-guide-2026.html')
text = p.read_text(encoding='utf-8')
marker = '        <h1 class="font-display text-3xl md:text-5xl font-bold text-white leading-tight mb-6">'
idx = text.find(marker)
print(idx)
print(text[idx:idx+250])
