from pathlib import Path
p = Path('dist/blog/ja/madrid-vs-direct-filing-china.html')
lines = p.read_text(encoding='utf-8').splitlines()
updates = {
    179: '<a href="#two-paths-h2" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">\u4e2d\u56fd\u3078\u306e2\u3064\u306e\u4e3b\u8981\u30d1\u30b9</a>',
    180: '<a href="#madrid-h2" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">\u30de\u30c9\u30ea\u30c3\u30c9\u30eb\u30fc\u30c8\u306e\u4ed5\u7d44\u307f</a>',
    181: '<a href="#direct-h2" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">\u76f4\u63a5CNIPA\u51fa\u9858\u306e\u4ed5\u7d44\u307f</a>',
    182: '<a href="#compare-h2" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">\u4e3b\u8981\u306a\u6bd4\u8f03\u8ef8</a>',
    183: '<a href="#choose-h2" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">\u307e\u3068\u3081</a>'
}
for idx, val in updates.items():
    lines[idx] = val
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('updated toc labels')
