from pathlib import Path
p = Path('dist/blog/ja/china-trademark-classes-complete-guide.html')
text = p.read_text(encoding='utf-8')
repls = {
    'class="text-brand">\u30d6\u30ed\u30b0</a>': 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>',
    'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>': 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>',
    '>\u30d6\u30ed\u30b0<': '\u30d6\u30ed\u30b0',
}
for old,new in repls.items():
    text=text.replace(old,new)
p.write_text(text,encoding='utf-8')
print('patched classes nav/blog text')
