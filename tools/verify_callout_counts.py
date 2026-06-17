from pathlib import Path
for name in ['china-trademark-monitoring-protection.html','common-reasons-trademark-rejection-china.html','how-long-trademark-registration-china.html','how-much-trademark-registration-cost-china.html','china-first-to-file-trademark-guide.html','who-can-register-trademark-in-china.html']:
    p=Path('dist/blog/ja')/name
    text=p.read_text(encoding='utf-8')
    print(name, text.count('<div class="callout">'))
