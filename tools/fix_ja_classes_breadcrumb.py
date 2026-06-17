from pathlib import Path
p = Path('dist/blog/ja/china-trademark-classes-complete-guide.html')
lines = p.read_text(encoding='utf-8').splitlines()
for i,l in enumerate(lines):
    if 'href="/blog/ja/"' in l and 'hover:text-white transition-colors' in l and '</a>' not in l:
        lines[i] = '          <a href="/blog/ja/" class="hover:text-white transition-colors">\u30d6\u30ed\u30b0</a>'
        break
p.write_text('\n'.join(lines)+'\n', encoding='utf-8')
print('fixed breadcrumb link')
