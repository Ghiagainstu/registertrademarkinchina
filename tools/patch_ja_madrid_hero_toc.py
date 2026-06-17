from pathlib import Path
p = Path('dist/blog/ja/madrid-vs-direct-filing-china.html')
lines = p.read_text(encoding='utf-8').splitlines()
# restore breadcrumb order and clean hero text
lines[111] = '          <a href="/" class="hover:text-white transition-colors">\u30db\u30fc\u30e0</a>'
lines[112] = '          <span class="mx-2">/</span>'
lines[113] = '          <a href="/blog/ja/" class="hover:text-white transition-colors">\u30d6\u30ed\u30b0</a>'
lines[114] = '          <span class="mx-2">/</span>'
lines[115] = '          <span class="text-slate-300">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb vs \u4e2d\u56fd\u76f4\u63a5\u51fa\u9858\uff1a\u3069\u3061\u3089\u304c\u9069\u5207\u304b\uff1f</span>'
lines[116] = '        <h1 class="font-display text-3xl md:text-5xl font-bold text-white leading-tight mb-6">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb vs \u4e2d\u56fd\u76f4\u63a5\u51fa\u9858\uff1a\u3069\u3061\u3089\u304c\u9069\u5207\u304b\uff1f</h1>'
lines[117] = '        <p class="text-lg text-slate-400 max-w-3xl mx-auto">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb\u3068CNIPA\u76f4\u63a5\u51fa\u9858\u3092\u6bd4\u8f03\u3057\u307e\u3059\u3002\u30bf\u30a4\u30e0\u30e9\u30a4\u30f3\u3001\u8cbb\u7528\u3001\u30ea\u30b9\u30af\u3001\u30d6\u30e9\u30f3\u30c9\u4fdd\u8b77\u6226\u7565\u306b\u5408\u308f\u305b\u305f\u9078\u629e\u80a2\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002</p>'
# translate toc labels to Japanese
toc_map = {
    '#two-paths-h2': '\u4e2d\u56fd\u3078\u306e2\u3064\u306e\u4e3b\u8981\u30d1\u30b9',
    '#madrid-h2': '\u30de\u30c9\u30ea\u30c3\u30c9\u30eb\u30fc\u30c8\u306e\u4ed5\u7d44\u307f',
    '#direct-h2': '\u76f4\u63a5CNIPA\u51fa\u9858\u306e\u4ed5\u7d44\u307f',
    '#compare-h2': '\u4e3b\u8981\u306a\u6bd4\u8f03\u8ef8',
    '#choose-h2': '\u307e\u3068\u3081'
}
for i,l in enumerate(lines):
    if 'class="toc-link block' in l and 'href="#' in l:
        for key,val in toc_map.items():
            if f'href="{key}"' in l:
                import re
                lines[i] = re.sub(r'>([^<]+)$', f'>{val}</a>', l)
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('restored hero and translated toc labels')
