from pathlib import Path
p = Path('dist/blog/ja/index.html')
text = p.read_text(encoding='utf-8')
text = text.replace('aria-label="\u8a00\u8a9e\u9078\u629e"', 'aria-label="Select language"')
text = text.replace('class="text-sm text-slate-400 hover:text-white transition-colors inline-flex items-center"', 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1"')
text = text.replace('class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors" data-lang="en" class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors"', 'class="block px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors" data-lang="en"')
text = text.replace('class="text-brand">\u30d6\u30ed\u30b0</a>', 'class="block text-sm text-brand">\u30d6\u30ed\u30b0</a>')
p.write_text(text, encoding='utf-8')
print('standardized ja index nav/switcher')
