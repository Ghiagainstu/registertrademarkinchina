from pathlib import Path
for name in ['china-first-to-file-trademark-guide.html','who-can-register-trademark-in-china.html']:
    p = Path('dist/blog/ja')/name
    text = p.read_text(encoding='utf-8')
    text = text.replace('<div class="callout">\n<span class="callout-icon"><svg fill="none" height="20" viewbox="0 0 20 20" width="20"><circle cx="10" cy="10" fill="url(#cg1)" r="10"></circle><text fill="#0ff0b3" font-family="Space Grotesk,monospace" font-size="12" font-weight="700" text-anchor="middle" x="10" y="14.5">!</text><defs><lineargradient id="cg1" x1="0" x2="20" y1="0" y2="20"><stop stop-color="rgba(15,240,179,0.2)"></stop><stop offset="1" stop-color="rgba(0,212,255,0.2)"></stop></lineargradient></defs></svg></span>\n</div>\n', '')
    p.write_text(text, encoding='utf-8')
    print('removed leftover callout shell', name)
