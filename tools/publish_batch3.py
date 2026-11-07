# -*- coding: utf-8 -*-
"""Publish batch 3 (12 topics x EN/JA/KO), update indexes and sitemap.

Reuses the page builder from publish_p0_2027.py so all pages share the same
header/footer, hreflang, canonical, JSON-LD, TOC and CTA structure.

Usage:
    python tools/publish_batch3.py build
    python tools/publish_batch3.py verify
"""
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import publish_p0_2027 as p            # noqa: E402
import publish_batch2 as p2            # noqa: E402
from p0_2027_content import CONTENT as BASE_UI   # noqa: E402
import batch3_content_a as ca         # noqa: E402
import batch3_content_b as cb         # noqa: E402

BLOG = p.BLOG
ROOT = p.ROOT
SITEMAP = p.SITEMAP
LANG_DIR = p.LANG_DIR
ORDER = ['oem', 'naming', 'refusal', 'nice', 'dynamic', 'greaterchina', 'decision',
         'jp', 'kr', 'us', 'eu', 'kcase']
ARTICLES = {
    lang: dict(ca.CONTENT[lang]['articles'], **cb.CONTENT[lang]['articles'])
    for lang in ('en', 'ja', 'ko')
}
DATE_LABEL = {
    'en': 'November 7, 2026',
    'ja': '2026年11月7日',
    'ko': '2026년 11월 7일',
}
DATE_ISO = '2026-11-07'
UI_KEYS = (
    'locale_label', 'home_label', 'blog_label', 'in_this_article',
    'related_label', 'cta_help', 'cta_button', 'cta_title',
    'cta_text', 'cta_button_big',
)
PREVIOUS_SLUGS = set(p.SLUGS.values()) | {
    p2.ARTICLES['en'][k]['slug'] for k in p2.ORDER
}


def cfg_for(lang):
    cfg = {k: BASE_UI[lang][k] for k in UI_KEYS}
    cfg['date_iso'] = DATE_ISO
    cfg['date_label'] = DATE_LABEL[lang]
    return cfg


def build_pages():
    made = []
    for lang in ('en', 'ja', 'ko'):
        sk_path = BLOG / LANG_DIR[lang] / p.SKELETON
        bom = sk_path.read_bytes().startswith(b'\xef\xbb\xbf')
        sk = p.read(sk_path)
        main_start = re.search(r'<main\b', sk).start()
        main_end = sk.index('</main>') + len('</main>')
        prefix, suffix = sk[:main_start], sk[main_end:]
        head_end = prefix.index('</head>')
        head, rest = prefix[:head_end], prefix[head_end:]
        cfg = cfg_for(lang)
        for key in ORDER:
            art = ARTICLES[lang][key]
            page = (p.build_head(head, lang, cfg, art, key) + rest
                    + p.build_main(lang, cfg, art, key) + suffix)
            if re.search(r'\{(?:L|HUB|ACT|HOME)\}', page):
                raise RuntimeError(f'unreplaced placeholder: {lang}/{key}')
            out = BLOG / LANG_DIR[lang] / f"{art['slug']}.html"
            p.write(out, page, bom=bom)
            made.append(str(out.relative_to(ROOT)))
    print(f'[build] wrote {len(made)} article pages')
    for m in made:
        print('   ', m)


def index_card(lang, art):
    tags = '\n'.join(
        f'<span class="px-2 py-0.5 rounded bg-white/5">{p.esc(t)}</span>' for t in art['tags']
    )
    return f'''<a href="{p.local(lang, art['slug'])}" class="post-card glass rounded-2xl p-8 block group">
          <div class="flex items-start justify-between gap-4">
            <div class="min-w-0 flex-1">
              <div class="flex items-center gap-3 mb-4">
                <span class="text-xs px-3 py-1 rounded-full bg-brand/10 text-brand font-semibold tracking-wide uppercase">{p.esc(art['category'])}</span>
                <span class="text-xs text-slate-500">{p.esc(DATE_LABEL[lang])}</span>
                <span class="text-xs text-slate-600">&middot;</span>
                <span class="text-xs text-slate-500">{p.esc(art['read_time'])}</span>
              </div>
              <h2 class="font-display text-xl md:text-2xl font-bold mb-3 group-hover:text-brand transition-colors">{p.esc(art['title'])}</h2>
              <p class="text-slate-400 text-sm leading-relaxed mb-4">{p.esc(art['card_text'])}</p>
              <div class="flex items-center gap-2 text-xs text-slate-500">
{tags}
              </div>
            </div>
            <svg class="w-5 h-5 text-slate-600 group-hover:text-brand transition-colors flex-shrink-0 mt-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </div>
        </a>

'''


def build_indexes():
    for lang in ('en', 'ja', 'ko'):
        path = BLOG / LANG_DIR[lang] / 'index.html'
        text = p.read(path)
        first_new = p.local(lang, ARTICLES[lang][ORDER[0]]['slug'])
        if first_new in text:
            print(f'[index] {lang}: already present, skipped')
            continue
        cards = list(re.finditer(r'<a href="([^"]+)" class="post-card', text))
        pos = None
        for m in cards:
            if not any(s in m.group(1) for s in PREVIOUS_SLUGS):
                pos = m.start()
                break
        if pos is None:
            pos = cards[0].start()
        insert = ''.join(index_card(lang, ARTICLES[lang][k]) for k in ORDER)
        text = text[:pos] + insert + text[pos:]
        p.write(path, text, bom=path.read_bytes().startswith(b'\xef\xbb\xbf'))
        print(f'[index] {lang}: inserted 12 cards at position {pos}')


def build_sitemap():
    text = p.read(SITEMAP)
    blocks = []
    for key in ORDER:
        slug = ARTICLES['en'][key]['slug']
        for lang in ('en', 'ja', 'ko'):
            if p.absolute(lang, slug) in text:
                continue
            blocks.append(p.sitemap_block(lang, slug))
    if not blocks:
        print('[sitemap] already up to date')
        return
    text = text.replace('</urlset>', ''.join(blocks) + '</urlset>')
    p.write(SITEMAP, text, bom=SITEMAP.read_bytes().startswith(b'\xef\xbb\xbf'))
    print(f'[sitemap] added {len(blocks)} URLs')


def verify():
    errors = []
    checks = []

    for lang in ('en', 'ja', 'ko'):
        for key in ORDER:
            art = ARTICLES[lang][key]
            path = BLOG / LANG_DIR[lang] / f"{art['slug']}.html"
            if not path.exists():
                errors.append(f'missing page: {path}')
                continue
            t = p.read(path)
            for token in (f'<html lang="{lang}"', '</html>', '<main', '</main>',
                          'rel="canonical"', 'application/ld+json',
                          'article-body', 'toc-sidebar', 'lang-btn'):
                if token not in t:
                    errors.append(f'{lang}/{key}: missing {token}')
            if t.count('hreflang=') < 4:
                errors.append(f'{lang}/{key}: hreflang count {t.count("hreflang=")}')
            if art['title'] not in t:
                errors.append(f'{lang}/{key}: title missing')
            if re.search(r'\{(?:L|HUB|ACT|HOME)\}', t):
                errors.append(f'{lang}/{key}: unreplaced placeholder')
            if t.count('<h2 id=') < len(art['sections']):
                errors.append(f'{lang}/{key}: section headings missing')
            for href in re.findall(r'href="(/blog/[^"#]+\.html)"', t):
                if not (ROOT / 'dist' / href.lstrip('/')).exists():
                    errors.append(f'{lang}/{key}: broken link {href}')
    checks.append('36 article pages: structure, meta, hreflang, local links')

    for lang in ('en', 'ja', 'ko'):
        t = p.read(BLOG / LANG_DIR[lang] / 'index.html')
        cards = re.findall(r'<a href="([^"]+)" class="post-card', t)
        if len(cards) != 46:
            errors.append(f'{lang} index: {len(cards)} cards, expected 46')
        for key in ORDER:
            if p.local(lang, ARTICLES[lang][key]['slug']) not in t:
                errors.append(f'{lang} index: missing card for {key}')
    checks.append('3 blog indexes: 46 cards each, 12 new cards each')

    sm = p.read(SITEMAP)
    locs = re.findall(r'<loc>([^<]+)</loc>', sm)
    if len(locs) != 184 or len(set(locs)) != 184:
        errors.append(f'sitemap: {len(locs)} URLs, {len(set(locs))} unique, expected 184')
    for key in ORDER:
        slug = ARTICLES['en'][key]['slug']
        for lang in ('en', 'ja', 'ko'):
            if p.absolute(lang, slug) not in locs:
                errors.append(f'sitemap: missing {p.absolute(lang, slug)}')
    checks.append(f'sitemap: {len(locs)} unique URLs, 36 new URLs present')

    for lang in ('en', 'ja', 'ko'):
        for slug in PREVIOUS_SLUGS:
            if not (BLOG / LANG_DIR[lang] / f'{slug}.html').exists():
                errors.append(f'earlier page missing: {lang}/{slug}')
    checks.append('batch-1 and batch-2 pages still present')

    print('\n=== VERIFY (batch 3) ===')
    for c in checks:
        print('  checked:', c)
    if errors:
        print(f'\n  {len(errors)} ERROR(S):')
        for e in errors[:60]:
            print('   -', e)
        return 1
    print('\n  ALL CHECKS PASSED')
    return 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'verify'
    if cmd == 'build':
        build_pages()
        build_indexes()
        build_sitemap()
        return 0
    if cmd == 'verify':
        return verify()
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
