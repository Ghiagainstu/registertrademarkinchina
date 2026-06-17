from pathlib import Path
p = Path('dist/blog/ja/china-trademark-classes-complete-guide.html')
text = p.read_text(encoding='utf-8')
if 'class="text-brand">\u30d6\u30ed\u30b0</a>' in text:
    text = text.replace('class="text-brand">\u30d6\u30ed\u30b0</a>', 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>')
    p.write_text(text, encoding='utf-8')
    print('updated nav highlight')
else:
    print('no legacy nav highlight found')
