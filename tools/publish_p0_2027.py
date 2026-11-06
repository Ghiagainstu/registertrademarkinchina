# -*- coding: utf-8 -*-
"""Publish the P0 2027 Trademark Law articles (EN/JA/KO), update blog indexes and
sitemap, and correct the 3-month opposition wording in existing articles.

Usage:
    python tools/publish_p0_2027.py build     # generate 6 articles + index cards + sitemap
    python tools/publish_p0_2027.py fix       # correct opposition wording in 36 existing pages
    python tools/publish_p0_2027.py retitle    # remove the expiring "(2026)" from the guide title
    python tools/publish_p0_2027.py verify    # full validation
"""
import re
import sys
import html
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
BLOG = ROOT / 'dist' / 'blog'
SITEMAP = ROOT / 'dist' / 'sitemap.xml'
sys.path.insert(0, str(HERE))
from p0_2027_content import CONTENT  # noqa: E402

DOMAIN = 'https://registertrademarkchina.com'
SKELETON = 'muji-trademark-war-china.html'
LANG_DIR = {'en': '', 'ja': 'ja/', 'ko': 'ko/'}
LANG_PREFIX = {'en': '/blog', 'ja': '/blog/ja', 'ko': '/blog/ko'}
HOME = {'en': '/', 'ja': '/ja/', 'ko': '/ko/'}
SLUGS = {
    'act': 'china-trademark-law-2027-foreign-brands',
    'hub': 'china-trademark-law-2026-revision-changes',
}
OPPOSITION_SLUGS = [
    'amazon-tmall-trademark-requirement-china',
    'china-first-to-file-trademark-guide',
    'china-trademark-monitoring-protection',
    'china-trademark-registration-complete-guide-2026',
    'coca-cola-chinese-name-trademark-china',
    'disney-mickey-trademark-china',
    'how-long-trademark-registration-china',
    'huawei-trademark-uk-case',
    'japanese-anime-ip-trademark-china',
    'nike-chinese-name-trademark-china',
    'starbucks-xingbake-trademark-china',
    'trademark-registered-by-someone-else-china',
]
MARKER = 'data-law-update-2027'

CALLOUT = {
    'en': '''<strong>November 2026 regulatory update:</strong> China's revised Trademark Law takes effect on <strong>1 January 2027</strong>. The 3-month opposition period described on this page applies to applications <strong>published before that date</strong>; applications published on or after it have a <strong>2-month</strong> period (Article 36 of the 2026 law). See the <a href="/blog/china-trademark-law-2026-revision-changes.html">old vs new comparison</a> for the full change list.''',
    'ja': '''<strong>2026年11月 法改正のお知らせ：</strong>改正中国商標法は<strong>2027年1月1日</strong>に施行されます。本ページに記載された3ヶ月の異議申立期間は<strong>同日より前に公告された出願</strong>に適用され、同日以降に公告された出願は<strong>2ヶ月</strong>となります（2026年法第36条）。変更点の全覧は<a href="/blog/ja/china-trademark-law-2026-revision-changes.html">旧法・新法の条項対比</a>をご覧ください。''',
    'ko': '''<strong>2026년 11월 법 개정 안내:</strong> 중국 개정 상표법은 <strong>2027년 1월 1일</strong> 시행됩니다. 이 페이지에 기재된 3개월 이의신청 기간은 <strong>그날 이전에 공고된 출원</strong>에 적용되며, 그날 이후 공고된 출원은 <strong>2개월</strong>이 적용됩니다(2026년 법 제36조). 전체 변경 사항은 <a href="/blog/ko/china-trademark-law-2026-revision-changes.html">구법·신법 조항 대조</a>에서 확인하십시오.''',
}


def esc(s):
    return html.escape(str(s), quote=False)


def local(lang, slug):
    return f'{LANG_PREFIX[lang]}/{slug}.html'


def absolute(lang, slug):
    return f'{DOMAIN}/blog/{LANG_DIR[lang]}{slug}.html'


def subs(text, lang):
    return (text.replace('{L}', LANG_PREFIX[lang])
                .replace('{HUB}', local(lang, SLUGS['hub']))
                .replace('{ACT}', local(lang, SLUGS['act']))
                .replace('{HOME}', HOME[lang]))


def read(path):
    return path.read_text(encoding='utf-8-sig')


def write(path, text, bom=False):
    body = ('\ufeff' if bom else '') + text
    path.write_text(body, encoding='utf-8', newline='\n')


# --------------------------------------------------------------------------
# HEAD
# --------------------------------------------------------------------------
EXTRA_CSS = '''
<style>
/* 2027 P0 articles: typography fallbacks */
.article-body .callout { border-left:4px solid #0FF0B3; padding:1rem 1.25rem; border-radius:0.5rem; background:rgba(15,240,179,0.05); margin:1.5rem 0; }
.article-body .callout-info { border-color:#00D4FF; background:rgba(0,212,255,0.05); }
.article-body .callout-warning { border-color:#FFB800; background:rgba(255,184,0,0.05); }
.article-body h2[id] { scroll-margin-top:100px; }
.article-body table { width:100%; border-collapse:collapse; margin:2rem 0; font-size:0.9rem; }
.article-body th, .article-body td { border-bottom:1px solid rgba(255,255,255,0.08); padding:0.75rem 1rem; text-align:left; vertical-align:top; }
.article-body th { color:#e2e8f0; font-weight:600; }
.article-body h3 { margin-top:2.25rem; margin-bottom:0.9rem; }
</style>
'''


def build_head(head, lang, cfg, art, key):
    for pattern in (
        r'<title\b[^>]*>.*?</title>',
        r'<meta\b[^>]*(?:name|property)\s*=\s*["\'](?:description|robots|og:[^"\']+|twitter:[^"\']+)["\'][^>]*>',
        r'<link\b[^>]*(?:hreflang|canonical|alternate)[^>]*>',
        r'<script\b[^>]*application/ld\+json[^>]*>.*?</script>',
    ):
        head = re.sub(pattern, '', head, flags=re.I | re.S)

    slug = art['slug']
    title = art['title']
    desc = art['desc']
    date = cfg['date_iso']
    canonical = absolute(lang, slug)
    alts = '\n'.join(
        f'  <link rel="alternate" hreflang="{code}" href="{absolute(code, slug)}" />'
        for code in ('en', 'ja', 'ko')
    )
    xdefault = f'  <link rel="alternate" hreflang="x-default" href="{absolute("en", slug)}" />'

    seo = f'''
  <title>{esc(title)} | RTMCN</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="robots" content="index, follow" />
{alts}
{xdefault}
  <link rel="canonical" href="{canonical}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{DOMAIN}/og-image.png" />
  <meta property="article:published_time" content="{date}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(desc)}" />
  <meta name="twitter:image" content="{DOMAIN}/og-image.png" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {json_str(title)},
    "description": {json_str(desc)},
    "datePublished": "{date}",
    "dateModified": "{date}",
    "author": {{"@type": "Organization", "name": "RTMCN"}},
    "publisher": {{"@type": "Organization", "name": "RTMCN"}},
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "{canonical}"}}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "{DOMAIN}/blog/"}},
      {{"@type": "ListItem", "position": 3, "name": {json_str(title)}}}
    ]
  }}
  </script>
''' + EXTRA_CSS
    return head.rstrip() + '\n' + seo


def json_str(s):
    # minimal JSON string escaping for ld+json
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ') + '"'


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------
def build_main(lang, cfg, art, key):
    title = art['title']
    lede = art['lede']
    sections = art['sections']

    body = []
    for sid, heading, chunk in sections:
        body.append(f'<h2 id="{sid}">{esc(heading)}</h2>')
        body.append(subs(chunk.strip(), lang))
    body_html = '\n'.join(body)

    toc = '\n'.join(
        f'<a href="#{sid}" class="toc-link block text-sm text-slate-500 hover:text-brand pl-4 py-1 border-l-2 border-slate-800 hover:border-brand transition-all duration-200">{esc(h)}</a>'
        for sid, h, _ in sections
    )
    related = '\n'.join(
        f'<a href="{subs(href, lang)}" class="block text-sm text-slate-500 hover:text-brand py-1 pl-1 transition-colors">{esc(label)}</a>'
        for href, label in art['related']
    )

    return f'''<main id="main-content" class="pt-16">
    <nav class="max-w-5xl mx-auto px-6 pt-4 pb-2" aria-label="{esc(cfg['locale_label'])}">
      <ol class="flex items-center gap-2 text-sm text-slate-500">
        <li><a href="{HOME[lang]}" class="hover:text-brand transition-colors">{esc(cfg['home_label'])}</a></li><li class="text-slate-600">/</li>
        <li><a href="{LANG_PREFIX[lang]}/" class="hover:text-brand transition-colors">{esc(cfg['blog_label'])}</a></li><li class="text-slate-600">/</li>
        <li class="text-slate-300">{esc(title)}</li>
      </ol>
    </nav>

    <section class="hero-gradient py-16 px-6">
      <div class="max-w-4xl mx-auto text-center">
        <h1 class="font-display text-3xl md:text-5xl font-bold text-white leading-tight mb-6">{esc(title)}</h1>
        <p class="text-lg text-slate-400 max-w-3xl mx-auto">{esc(lede)}</p>
      </div>
    </section>

    <div class="section-divider max-w-4xl mx-auto"></div>
    <section class="py-12 px-6">
      <div class="max-w-7xl mx-auto grid lg:grid-cols-4 gap-12">
        <div class="lg:col-span-3">
          <div class="lg:col-span-3 article-body">
{body_html}
          </div>
        </div>
        <aside class="toc-sidebar hidden lg:block">
          <div class="sticky top-28 space-y-7">
            <div class="glass rounded-2xl p-6">
              <p class="text-xs text-slate-600 uppercase tracking-widest font-semibold mb-3 pl-1">{esc(cfg['in_this_article'])}</p>
{toc}
            </div>
            <div class="glass rounded-2xl p-6">
              <p class="text-xs text-slate-600 uppercase tracking-widest font-semibold mb-3 pl-1">{esc(cfg['related_label'])}</p>
{related}
            </div>
            <div class="glass rounded-2xl p-6 text-center">
              <p class="text-sm text-slate-400 mb-4">{esc(cfg['cta_help'])}</p>
              <a href="/contact.html" class="btn-glow inline-block w-full px-4 py-2.5 rounded-lg text-sm font-semibold text-center">{esc(cfg['cta_button'])}</a>
            </div>
          </div>
        </aside>
      </div>
    </section>
    <section class="py-16 px-6 text-center">
      <div class="max-w-3xl mx-auto">
        <h2 class="font-display text-2xl md:text-3xl font-bold mb-4">{esc(cfg['cta_title'])}</h2>
        <p class="text-slate-400 mb-8">{esc(cfg['cta_text'])}</p>
        <a href="/contact.html" class="btn-glow inline-block px-8 py-3 rounded-lg text-sm font-semibold">{esc(cfg['cta_button_big'])}</a>
      </div>
    </section>
  </main>'''


def build_pages():
    made = []
    for lang, cfg in CONTENT.items():
        sk_path = BLOG / LANG_DIR[lang] / SKELETON
        sk_raw = sk_path.read_bytes()
        bom = sk_raw.startswith(b'\xef\xbb\xbf')
        sk = read(sk_path)
        main_start = re.search(r'<main\b', sk).start()
        main_end = sk.index('</main>') + len('</main>')
        prefix, suffix = sk[:main_start], sk[main_end:]
        head_end = prefix.index('</head>')
        head, rest = prefix[:head_end], prefix[head_end:]

        for key, art in cfg['articles'].items():
            page = (build_head(head, lang, cfg, art, key) + rest
                    + build_main(lang, cfg, art, key) + suffix)
            if re.search(r'\{(?:L|HUB|ACT|HOME)\}', page):
                raise RuntimeError(f'unreplaced placeholder: {lang}/{key}')
            out = BLOG / LANG_DIR[lang] / f"{art['slug']}.html"
            write(out, page, bom=bom)
            made.append(str(out.relative_to(ROOT)))
    print(f'[build] wrote {len(made)} article pages')
    for m in made:
        print('   ', m)


# --------------------------------------------------------------------------
# INDEX CARDS
# --------------------------------------------------------------------------
def index_card(lang, cfg, key):
    art = cfg['articles'][key]
    category = cfg['category_a'] if key == 'act' else cfg['category_b']
    read_time = cfg['read_a'] if key == 'act' else cfg['read_b']
    tags = '\n'.join(
        f'<span class="px-2 py-0.5 rounded bg-white/5">{esc(t)}</span>' for t in art['tags']
    )
    return f'''<a href="{local(lang, art['slug'])}" class="post-card glass rounded-2xl p-8 block group">
          <div class="flex items-start justify-between gap-4">
            <div class="min-w-0 flex-1">
              <div class="flex items-center gap-3 mb-4">
                <span class="text-xs px-3 py-1 rounded-full bg-brand/10 text-brand font-semibold tracking-wide uppercase">{esc(category)}</span>
                <span class="text-xs text-slate-500">{esc(cfg['date_label'])}</span>
                <span class="text-xs text-slate-600">&middot;</span>
                <span class="text-xs text-slate-500">{esc(read_time)}</span>
              </div>
              <h2 class="font-display text-xl md:text-2xl font-bold mb-3 group-hover:text-brand transition-colors">{esc(art['title'])}</h2>
              <p class="text-slate-400 text-sm leading-relaxed mb-4">{esc(art['card_text'])}</p>
              <div class="flex items-center gap-2 text-xs text-slate-500">
{tags}
              </div>
            </div>
            <svg class="w-5 h-5 text-slate-600 group-hover:text-brand transition-colors flex-shrink-0 mt-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </div>
        </a>

'''


def build_indexes():
    for lang, cfg in CONTENT.items():
        path = BLOG / LANG_DIR[lang] / 'index.html'
        text = read(path)
        if local(lang, SLUGS['act']) in text:
            print(f'[index] {lang}: already present, skipped')
            continue
        m = re.search(r'<a href="[^"]+" class="post-card', text)
        if not m:
            raise RuntimeError(f'no post-card anchor in {path}')
        cards = index_card(lang, cfg, 'act') + index_card(lang, cfg, 'hub')
        text = text[:m.start()] + cards + text[m.start():]
        write(path, text, bom=path.read_bytes().startswith(b'\xef\xbb\xbf'))
        print(f'[index] {lang}: inserted 2 cards before first post-card')


# --------------------------------------------------------------------------
# SITEMAP
# --------------------------------------------------------------------------
def sitemap_block(lang, slug):
    loc = absolute(lang, slug)
    alts = '\n'.join(
        f'    <xhtml:link rel="alternate" hreflang="{code}" href="{absolute(code, slug)}"/>'
        for code in ('en', 'ja', 'ko')
    )
    return f'''  <url>
    <loc>{loc}</loc>
{alts}
    <xhtml:link rel="alternate" hreflang="x-default" href="{absolute('en', slug)}"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''


def build_sitemap():
    text = read(SITEMAP)
    blocks = []
    for slug in (SLUGS['act'], SLUGS['hub']):
        for lang in ('en', 'ja', 'ko'):
            if absolute(lang, slug) in text:
                continue
            blocks.append(sitemap_block(lang, slug))
    if not blocks:
        print('[sitemap] already up to date')
        return
    text = text.replace('</urlset>', ''.join(blocks) + '</urlset>')
    write(SITEMAP, text, bom=SITEMAP.read_bytes().startswith(b'\xef\xbb\xbf'))
    print(f'[sitemap] added {len(blocks)} URLs')


# --------------------------------------------------------------------------
# EXISTING ARTICLE CORRECTIONS
# --------------------------------------------------------------------------
NUMBER_MAP = {
    'en': lambda s: s + (' (2-month from 1 January 2027)' if '-' in s else ' (2 months from 1 January 2027)'),
    'ja': lambda s: s + '（2027年1月1日以降は2ヶ月）',
    'ko': lambda s: s + '(2027년 1월 1일부터 2개월)',
}
NUMBER_RE = re.compile(r'3[- ]months?|3ヶ月|3개월', re.I)
CTX_RE = {
    'en': re.compile(r'oppos|publication|gazette|window', re.I),
    'ja': re.compile(r'異議|公告|公報'),
    'ko': re.compile(r'이의|공고|공보'),
}
# Words that identify an *examination* duration rather than an opposition window.
# A 3-month figure right after these must not be touched.
EXCLUDE_RE = {
    'en': re.compile(r'Substantive|Core review|Formal exam|Exam:', re.I),
    'ja': re.compile(r'実体審査|方式審査|審査:'),
    'ko': re.compile(r'실체 심사|실질 심사|형식 심사|심사:'),
}
# Clean up nested parentheses produced when the figure sits inside a bracket.
NESTED = {
    'en': ('(3 months (2 months from 1 January 2027))', '(3 months; 2 months from 1 January 2027)'),
    'ja': ('（3ヶ月（2027年1月1日以降は2ヶ月））', '（3ヶ月／2027年1月1日以降は2ヶ月）'),
    'ko': ('(3개월(2027년 1월 1일부터 2개월))', '(3개월 / 2027년 1월 1일부터 2개월)'),
}


def plain(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))


def correction_callout(lang):
    hub = local(lang, SLUGS['hub'])
    body = CALLOUT[lang].replace(
        local('en', SLUGS['hub']), hub
    ).replace(
        '/blog/ja/' + SLUGS['hub'] + '.html', hub
    ).replace(
        '/blog/ko/' + SLUGS['hub'] + '.html', hub
    )
    return (f'<div class="callout callout-info" {MARKER}="1" '
            f'style="margin:0 0 2rem 0;border-left:4px solid #00D4FF;'
            f'background:rgba(0,212,255,0.05);padding:1rem 1.25rem;border-radius:0.5rem;">'
            f'<p class="leading-relaxed text-slate-300" style="margin:0;font-size:0.95rem;line-height:1.75;">'
            f'{body}</p></div>\n')


def fix_opposition():
    changed = 0
    repl_total = 0
    for lang in ('en', 'ja', 'ko'):
        for slug in OPPOSITION_SLUGS:
            path = BLOG / LANG_DIR[lang] / f'{slug}.html'
            text = read(path)
            if MARKER in text:
                print(f'[fix] {lang}/{slug}: already updated, skipped')
                continue

            # 1) replace the 3-month figure, but only in opposition contexts and
            #    never inside a numeric range such as "1-3 months" / "1〜3ヶ月".
            hits = [0]

            def repl(m):
                prev = text[max(0, m.start() - 3):m.start()]
                if re.search(r'[〜~～\-–/0-9]\s*$', prev):
                    return m.group(0)                      # inside a range: 1-3 months
                near_before = plain(text[max(0, m.start() - 120):m.start()])
                near_after = plain(text[m.end():m.end() + 120])
                if not CTX_RE[lang].search(near_before + near_after):
                    return m.group(0)
                # Reject examination durations, unless the same short prefix
                # already contains an opposition/publication word.
                tight = near_before[-40:]
                if EXCLUDE_RE[lang].search(tight) and not CTX_RE[lang].search(tight):
                    return m.group(0)
                hits[0] += 1
                return NUMBER_MAP[lang](m.group(0))

            text = NUMBER_RE.sub(repl, text)
            old, new = NESTED[lang]
            text = text.replace(old, new)

            # 2) insert the update callout just before the first body heading
            anchor = re.search(r'<div class="lg:col-span-3 article-body">', text)
            if anchor:
                pos = anchor.end()
            else:
                h2 = re.search(r'<h2\b', text)
                pos = h2.start() if h2 else text.index('</main>')
            text = text[:pos] + '\n' + correction_callout(lang) + text[pos:]

            write(path, text, bom=path.read_bytes().startswith(b'\xef\xbb\xbf'))
            repl_total += hits[0]
            changed += 1
            print(f'[fix] {lang}/{slug}: {hits[0]} figure(s) updated + callout')
    print(f'[fix] {changed} pages changed, {repl_total} figure replacements')


# --------------------------------------------------------------------------
# RETITLE THE 2026 GUIDE (drop the expiring year from display text only)
# --------------------------------------------------------------------------
RETITLE_SLUG = 'china-trademark-registration-complete-guide-2026'


RETITLE_RULES = {
    'en': [
        (re.compile(r'\s*\(2026\)'), ''),
        (' in 2026. Covers', '. Covers'),
        (' in 2026.', '.'),
    ],
    'ja': [
        (re.compile(r'\s*[(（]2026年版[)）]'), ''),
    ],
    'ko': [
        ('중국 상표 등록 완전 가이드 2026', '중국 상표 등록 완전 가이드'),
        (re.compile(r'\s*[(（]2026년판[)）]'), ''),
        (re.compile(r'\s*[(（]2026[)）]'), ''),
    ],
}
RETITLE_RESIDUE = {
    'en': re.compile(r'\(2026\)'),
    'ja': re.compile(r'2026年版'),
    'ko': re.compile(r'등록 완전 가이드 2026|2026년판|가이드 \(2026\)'),
}


def apply_retitle(text, lang):
    for pattern, replacement in RETITLE_RULES[lang]:
        text = (pattern.sub(replacement, text) if hasattr(pattern, 'sub')
                else text.replace(pattern, replacement))
    return text


def retitle_guide():
    changed = 0
    for lang in ('en', 'ja', 'ko'):
        targets = [
            BLOG / LANG_DIR[lang] / f'{RETITLE_SLUG}.html',
            BLOG / LANG_DIR[lang] / 'index.html',
        ]
        for path in targets:
            raw = path.read_bytes().decode('utf-8-sig')
            updated = apply_retitle(raw, lang)
            if updated != raw:
                write(path, updated, bom=path.read_bytes().startswith(b'\xef\xbb\xbf'))
                changed += 1
                print(f'[retitle] {lang} {path.name} updated')
    print(f'[retitle] {changed} files updated (URLs/slugs untouched)')


# --------------------------------------------------------------------------
# VERIFY
# --------------------------------------------------------------------------
def verify():
    errors = []
    checks = []

    # 1) six new pages
    for lang, cfg in CONTENT.items():
        for key, art in cfg['articles'].items():
            p = BLOG / LANG_DIR[lang] / f"{art['slug']}.html"
            if not p.exists():
                errors.append(f'missing page: {p}')
                continue
            t = read(p)
            expect = (f'<html lang="{lang}"', '</html>', '<main', '</main>',
                      'rel="canonical"', f'hreflang="{lang}"',
                      'application/ld+json', 'article-body', 'toc-sidebar',
                      'lang-btn', 'lang-dropdown')
            for token in expect:
                if token not in t:
                    errors.append(f'{lang}/{key}: missing {token}')
            if t.count('hreflang=') < 4:
                errors.append(f'{lang}/{key}: hreflang count {t.count("hreflang=")} < 4')
            if art['title'] not in t:
                errors.append(f'{lang}/{key}: title missing from body')
            if re.search(r'\{(?:L|HUB|ACT|HOME)\}', t):
                errors.append(f'{lang}/{key}: unreplaced placeholder')
            if t.count('<h2 id=') < len(art['sections']) - 1:
                errors.append(f'{lang}/{key}: section headings missing')
            # all local article links resolve
            for href in re.findall(r'href="(/blog/[^"#]+\.html)"', t):
                rel = href.lstrip('/')
                if not (ROOT / 'dist' / rel).exists():
                    errors.append(f'{lang}/{key}: broken link {href}')
    checks.append('6 article pages: structure, meta, hreflang, local links')

    # 2) indexes
    for lang in ('en', 'ja', 'ko'):
        p = BLOG / LANG_DIR[lang] / 'index.html'
        t = read(p)
        cards = re.findall(r'<a href="([^"]+)" class="post-card', t)
        if len(cards) != 29:
            errors.append(f'{lang} index: {len(cards)} cards, expected 29')
        for slug in SLUGS.values():
            if local(lang, slug) not in t:
                errors.append(f'{lang} index: missing card for {slug}')
    checks.append('3 blog indexes: 29 cards each, 2 new cards each')

    # 3) sitemap
    sm = read(SITEMAP)
    locs = re.findall(r'<loc>([^<]+)</loc>', sm)
    for slug in SLUGS.values():
        for lang in ('en', 'ja', 'ko'):
            if absolute(lang, slug) not in locs:
                errors.append(f'sitemap: missing {absolute(lang, slug)}')
    if len(locs) != len(set(locs)):
        errors.append('sitemap: duplicate URLs')
    for loc in locs:
        if f'{loc}</loc>' in sm and '2027' in loc:
            pass
    checks.append(f'sitemap: {len(locs)} unique URLs, 6 new URLs present')

    # 4) corrected pages
    for lang in ('en', 'ja', 'ko'):
        marker_text = {'en': '1 January 2027', 'ja': '2027年1月1日', 'ko': '2027년 1월 1일'}[lang]
        new_figure = {'en': '2 months from 1 January 2027', 'ja': '2027年1月1日以降は2ヶ月',
                      'ko': '2027년 1월 1일부터 2개월'}[lang]
        for slug in OPPOSITION_SLUGS:
            p = BLOG / LANG_DIR[lang] / f'{slug}.html'
            t = read(p)
            if MARKER not in t:
                errors.append(f'{lang}/{slug}: update callout missing')
            if marker_text not in t:
                errors.append(f'{lang}/{slug}: effective date missing')
            if t.count('<main') != 1 or t.count('</main>') != 1:
                errors.append(f'{lang}/{slug}: main tag count changed')
        # at least some figure replacements exist
        joined = '\n'.join(read(BLOG / LANG_DIR[lang] / f'{s}.html') for s in OPPOSITION_SLUGS)
        if new_figure not in joined:
            errors.append(f'{lang}: no figure replacements found')
    checks.append('36 existing pages: callout + effective date + figure updates')

    # 5) retitle
    for lang in ('en', 'ja', 'ko'):
        for path in (BLOG / LANG_DIR[lang] / f'{RETITLE_SLUG}.html',
                     BLOG / LANG_DIR[lang] / 'index.html'):
            t = read(path)
            if RETITLE_RESIDUE[lang].search(t):
                errors.append(f'{lang} {path.name}: expiring year still in display text')
            if not path.exists():
                errors.append(f'{lang} guide page missing: {path}')
    checks.append('guide display titles: expiring year removed, slug preserved')

    print('\n=== VERIFY ===')
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
    elif cmd == 'fix':
        fix_opposition()
    elif cmd == 'retitle':
        retitle_guide()
    elif cmd == 'verify':
        return verify()
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
