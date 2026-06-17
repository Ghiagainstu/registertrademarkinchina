from pathlib import Path
p = Path('dist/blog/ja/who-can-register-trademark-in-china.html')
text = p.read_text(encoding='utf-8')
start = text.index('<div class="callout">\n<span class="callout-icon"><svg fill="none" height="20"')
end = text.index('<h2 id="section-663beb7e">', start)
print(repr(text[start:end]))
