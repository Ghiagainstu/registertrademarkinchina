import pathlib, re, collections
en_text = pathlib.Path('dist/blog/index.html').read_text(encoding='utf-8')
ja_path = pathlib.Path('dist/blog/ja/index.html')
ja_text = ja_path.read_text(encoding='utf-8')
en_slugs = [m.split('/')[-1] for m in re.findall(r'<a href="/blog/([^"]+)" class="post-card ', en_text)]
ja_start = ja_text.index('<a href="/blog/ja/china-trademark-registration-complete-guide-2026.html" class="post-card')
pat = re.compile(r'<a href="/blog/ja/([^"]+)" class="post-card .*?</a>\s*', re.S)
matches = list(pat.finditer(ja_text, ja_start))
blocks = {m.group(1): m.group(0) for m in matches}
ja_end = matches[-1].end()
new_order = [slug for slug in en_slugs if slug in blocks]
if len(new_order) != len(blocks):
    missing = [s for s in blocks if s not in new_order]
    new_order.extend(missing)
new_text = ja_text[:ja_start] + ''.join(blocks[s] for s in new_order) + ja_text[ja_end:]
ja_path.write_text(new_text, encoding='utf-8')
print('reordered ja index to', new_order)
