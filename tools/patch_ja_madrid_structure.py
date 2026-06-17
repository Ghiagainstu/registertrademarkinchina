from pathlib import Path
p = Path('dist/blog/ja/madrid-vs-direct-filing-china.html')
lines = p.read_text(encoding='utf-8').splitlines()
# patch hero lines
lines[113] = '          <a href="/blog/ja/" class="hover:text-white transition-colors">\u30d6\u30ed\u30b0</a>'
lines[115] = '          <span class="text-slate-300">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb vs \u4e2d\u56fd\u76f4\u63a5\u51fa\u9858\uff1a\u3069\u3061\u3089\u304c\u9069\u5207\u304b\uff1f</span>'
lines[116] = '        <h1 class="font-display text-3xl md:text-5xl font-bold text-white leading-tight mb-6">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb vs \u4e2d\u56fd\u76f4\u63a5\u51fa\u9858\uff1a\u3069\u3061\u3089\u304c\u9069\u5207\u304b\uff1f</h1>'
lines[117] = '        <p class="text-lg text-slate-400 max-w-3xl mx-auto">\u30de\u30c9\u30ea\u30c3\u30c9\u30d7\u30ed\u30c8\u30b3\u30eb\u3068CNIPA\u76f4\u63a5\u51fa\u9858\u3092\u6bd4\u8f03\u3057\u307e\u3059\u3002\u30bf\u30a4\u30e0\u30e9\u30a4\u30f3\u3001\u8cbb\u7528\u3001\u30ea\u30b9\u30af\u3001\u30d6\u30e9\u30f3\u30c9\u4fdd\u8b77\u6226\u7565\u306b\u5408\u308f\u305b\u305f\u9078\u629e\u80a2\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002</p>'
# structural fix around article wrapper
if lines[127].strip() != '<div class="lg:col-span-3">':
    print('unexpected wrapper line')
    raise SystemExit(1)
if lines[128].strip() != '<div class="lg:col-span-3 article-body">':
    print('unexpected article body line')
    raise SystemExit(1)
lines[127:129] = [
'<div class="lg:col-span-3">',
'<div class="lg:col-span-3 article-body">'
]
# need second closing div before aside
if '<aside class="toc-sidebar hidden lg:block">' not in lines[173]:
    print('aside not where expected')
    raise SystemExit(1)
# insert closing div for outer wrapper before aside if missing
insert_index = 173
if lines[insert_index-1].strip() != '</div>':
    lines.insert(insert_index, '        </div>')
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('patched structure and hero')
