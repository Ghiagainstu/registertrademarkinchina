from pathlib import Path
p = Path('dist/blog/ja/who-can-register-trademark-in-china.html')
text = p.read_text(encoding='utf-8')
idx = text.index('<div class="lg:col-span-3 article-body">')
end = text.index('<h2 id="section-663beb7e">', idx)
print(repr(text[idx:end]))
