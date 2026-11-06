# -*- coding: utf-8 -*-
"""Content data for the two P0 articles on China's 2026 Trademark Law revision.

Placeholders replaced by the publisher:
  {L}    -> /blog | /blog/ja | /blog/ko
  {HUB}  -> comparison article URL (localised)
  {ACT}  -> action-guide article URL (localised)
  {HOME} -> / | /ja/ | /ko/
"""

CONTENT = {}

CONTENT['en'] = {
    'lang': 'en',
    'locale_label': 'Breadcrumb',
    'home_label': 'Home',
    'blog_label': 'Blog',
    'in_this_article': 'In This Article',
    'related_label': 'Related Articles',
    'cta_help': 'Need help with China trademark registration?',
    'cta_button': 'Free Consultation',
    'cta_title': 'Need Help With Your China Trademark?',
    'cta_text': 'Our experts will guide you through the entire process.',
    'cta_button_big': 'Get a Free Consultation',
    'date_label': 'November 6, 2026',
    'date_iso': '2026-11-06',
    'category_a': 'Policy Update',
    'category_b': 'Policy Update',
    'read_a': '9 min read',
    'read_b': '10 min read',
    'articles': {
        'act': {
            'slug': 'china-trademark-law-2027-foreign-brands',
            'title': "China's New Trademark Law Takes Effect 1 January 2027: What Foreign Brands Should Do Now",
            'desc': "China's revised Trademark Law takes effect on 1 January 2027. A practical guide for foreign brand owners: what changes, whether filing before year-end helps, and the five actions to take now.",
            'lede': "China's first full rewrite of its Trademark Law since 1983 takes effect on 1 January 2027. Here is what actually changes for foreign brand owners — and what to do in the remaining weeks.",
            'card_text': "The 2027 law shortens the opposition window, adds CNIPA-initiated cancellation and tightens bad-faith filing rules. Here is what foreign brands should do before 1 January.",
            'tags': ['2027 trademark law', 'opposition', 'CNIPA'],
            'related': [
                ('{L}/china-trademark-law-2026-revision-changes.html', 'Old vs New: 2026 Trademark Law Comparison'),
                ('{L}/china-trademark-monitoring-protection.html', 'Trademark Monitoring and Protection'),
                ('{L}/trademark-registered-by-someone-else-china.html', 'If Someone Registered Your Mark First'),
            ],
            'sections': [
                ('the-short-answer', 'The Short Answer: Keep Filing Early — But Not to "Lock In" the Old Law', """
<p class="leading-relaxed text-slate-300 mb-6">On 26 June 2026, China adopted a completely revised Trademark Law. It takes effect on <strong>1 January 2027</strong>. This is the first full rewrite since 1983: the statute grows from 8 chapters and 73 articles to <strong>9 chapters and 87 articles</strong>, with a new chapter devoted to registrability conditions.</p>
<p class="leading-relaxed text-slate-300 mb-6">If you own a foreign brand with Chinese trademark rights, or are about to file, the practical answer is: <strong>keep filing early, but do not file purely to "lock in" the old rules.</strong> Under the CNIPA's draft transition measures published on 28 September 2026, an application filed before 1 January 2027 but decided on or after that date is handled under the new law.</p>
<p class="leading-relaxed text-slate-300 mb-6">What early filing still buys you is the one thing that has always mattered most in China: <strong>the earliest filing date</strong>. China remains a first-to-file jurisdiction. The 2027 law changes examination standards, procedural deadlines and enforcement powers — it does not change who wins when two parties claim the same mark.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Status note:</strong> The revised law is enacted and its effective date is fixed. The CNIPA's <em>Measures for Handling Business Matters Following the Revised Trademark Law</em> are still a <strong>draft</strong> (public comment closed 12 November 2026) and may change before the final text is issued. We flag draft-based statements below.</p></div>
"""),
                ('key-dates', 'Four Dates That Matter', """
<table>
<thead><tr><th>Date</th><th>What happens</th><th>Why it matters to you</th></tr></thead>
<tbody>
<tr><td>26 June 2026</td><td>NPC Standing Committee adopts the revised Trademark Law</td><td>The text is final; the 9-chapter / 87-article structure is fixed</td></tr>
<tr><td>28 September 2026</td><td>CNIPA publishes draft transition measures and a draft Examination and Review Guidelines</td><td>Shows how pending cases and new filing types are intended to be handled</td></tr>
<tr><td>12 November 2026</td><td>Public comment on the draft measures closes</td><td>Final measures may differ; re-check before relying on transition detail</td></tr>
<tr><td><strong>1 January 2027</strong></td><td>Revised Trademark Law (and, if adopted, the transition measures) take effect</td><td>New opposition window, new registrable signs, new cancellation powers</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Source: CNIPA, <em>Main Contents of the Revision to the PRC Trademark Law</em> (10 July 2026) and the CNIPA notice of 28 September 2026.</p>
"""),
                ('what-changes', 'What Changes for Foreign Applicants', """
<table>
<thead><tr><th>Change</th><th>2026 law article</th><th>Practical effect</th></tr></thead>
<tbody>
<tr><td>Opposition window</td><td>Art. 36</td><td><strong>3 months &rarr; 2 months</strong> after preliminary publication</td></tr>
<tr><td>Refusal review</td><td>Art. 37</td><td>15 days to request review; CNIPA decides within 9 months (extendable by 3)</td></tr>
<tr><td>Registrable signs</td><td>Art. 14</td><td><strong>Dynamic (motion) marks</strong> added alongside words, devices, colours and sounds</td></tr>
<tr><td>Bad-faith / speculative filings</td><td>Arts. 19, 54</td><td>Applications with no intent to use that clearly exceed normal business needs are refused; warning plus fine up to RMB 100,000</td></tr>
<tr><td>Misleading use</td><td>Art. 56</td><td>Fines up to 5&times; illegal turnover (or RMB 250,000); CNIPA may revoke the registration if not corrected</td></tr>
<tr><td>Idle marks</td><td>Art. 57</td><td><strong>CNIPA may cancel a mark on its own initiative</strong> after 3 consecutive years of non-use</td></tr>
<tr><td>Well-known marks</td><td>Art. 21</td><td>Cross-class protection no longer requires the mark to be registered in China</td></tr>
<tr><td>Online use</td><td>Art. 2</td><td>Use through the internet and information networks expressly counts as trademark use</td></tr>
<tr><td>Trademark agents</td><td>Arts. 65&ndash;68</td><td>Filing/recordal duties and penalties tightened; unrecorded agencies face fines</td></tr>
<tr><td>Damages</td><td>Art. 77</td><td>Reasonable costs of stopping infringement expressly included in damages</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">For the full old-versus-new comparison with article numbers, see <a href="{HUB}">China Trademark Law 2026 Revision: Old Rules vs New Rules</a>.</p>
"""),
                ('should-you-file-before-2027', 'Should You Rush to File Before 31 December 2026?', """
<p class="leading-relaxed text-slate-300 mb-6">This is the question most brand owners are asking in November 2026. The honest answer has two parts.</p>
<h3>No — a pre-2027 filing date does not freeze the old examination rules</h3>
<p class="leading-relaxed text-slate-300 mb-6">The draft transition measures follow a general principle of <strong>"substantive issues under the old law, procedural issues under the new law"</strong>. For registration, opposition, refusal review and other applications filed before 1 January 2027 where CNIPA issues its decision on or after that date, the draft provides that the new law applies. For invalidation or cancellation actions against marks already registered before 2027, procedural questions follow the new law while substantive questions follow the law in force when the mark was registered.</p>
<h3>Yes — an earlier filing date still protects you under first-to-file</h3>
<p class="leading-relaxed text-slate-300 mb-6">Priority between competing claimants is decided by who filed first, not by which statute was in force. Filing now still secures your position against a squatter, a distributor or a factory that files tomorrow. The new law's stronger bad-faith provisions are a useful additional remedy, but they are not a substitute for being first.</p>
<h3>One date is genuinely decisive: the publication date</h3>
<p class="leading-relaxed text-slate-300 mb-6">Under Article 4 of the draft measures, the length of the opposition window is determined by the <strong>publication date</strong>, not the filing date: for domestic applications, the date of preliminary publication in the Trademark Gazette; for international registrations designating China, the WIPO publication date. Applications published before 1 January 2027 keep the 3-month window; those published on or after that date get 2 months. A window that straddles the year boundary is <strong>not restarted</strong>. This is the single most operationally important transition rule for any brand running a watch service.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Do not rely on the draft as final.</strong> The measures were still open for comment until 12 November 2026. Confirm the final text before setting internal deadlines or advising a client on a live opposition.</p></div>
"""),
                ('action-checklist', 'Five Things to Do Before 1 January 2027', """
<ol>
<li><strong>Audit your portfolio for "no intent to use" exposure.</strong> Article 19 refuses applications that lack intent to use and clearly exceed normal business needs. Broad defensive portfolios remain permissible in principle, but every class should have a documented business rationale, expansion plan, anti-counterfeit purpose or sub-class logic behind it.</li>
<li><strong>Upgrade your watch service to a 2-month response cycle.</strong> A monthly gazette review plus slow internal approval is no longer safe. Move to weekly monitoring of your key classes and Chinese-character variants, pre-authorise local counsel, and keep an evidence package ready so an opposition can be filed within days of publication. See our <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a>.</li>
<li><strong>Build a use-evidence file now.</strong> Because CNIPA can cancel idle marks on its own initiative, dated invoices, platform listings with capture dates, packaging, customs records, distributor agreements and exhibition materials should be archived by mark and by class from day one.</li>
<li><strong>Check your Chinese-character coverage.</strong> English and Chinese marks are separate rights in China. Confirm that your official Chinese name, common transliterations and consumer-coined nicknames are registered in the classes that matter. Our <a href="{L}/china-trademark-classes-complete-guide.html">classification guide</a> explains how sub-classes affect scope.</li>
<li><strong>Re-vet your agent.</strong> Articles 65&ndash;68 require agencies and their practitioners to be recorded with CNIPA and add penalties for conflicts of interest and knowingly assisting bad-faith filings. Ask your agent for its recordal status and who is personally signing your filings.</li>
</ol>
"""),
                ('what-does-not-change', 'What Does Not Change', """
<ul>
<li><strong>First-to-file.</strong> China does not award rights to the first user. A foreign registration has no effect in China.</li>
<li><strong>Territorial scope.</strong> A CNIPA registration covers mainland China. Separate filings are needed for Hong Kong, China; Macao, China; and Taiwan, China.</li>
<li><strong>The local-agent requirement.</strong> Foreign applicants without a domicile or place of business in China still file through a Chinese trademark agency.</li>
<li><strong>10-year terms and renewals.</strong> Registrations remain valid for 10 years and are renewable; see our <a href="{L}/china-trademark-renewal-guide.html">renewal guide</a>.</li>
<li><strong>The Madrid route.</strong> You can still designate China through WIPO, though CNIPA examines under Chinese law. Compare both paths in <a href="{L}/madrid-vs-direct-filing-china.html">Madrid vs direct filing</a>.</li>
</ul>
"""),
                ('faq', 'Frequently Asked Questions', """
<h3>Will my pending application be examined under the old law?</h3>
<p class="leading-relaxed text-slate-300 mb-6">Under the September 2026 draft, if CNIPA decides the case on or after 1 January 2027, the new law generally applies to a pre-2027 application. Treat this as the planning assumption, then confirm against the final measures.</p>
<h3>Can I still oppose a mark published in December 2026?</h3>
<p class="leading-relaxed text-slate-300 mb-6">Under the draft, a mark published before 1 January 2027 keeps the 3-month opposition window and the clock is not restarted by the new law. Do not, however, wait until the last week — evidence preparation and translation take time.</p>
<h3>Does the new law remove squatters automatically?</h3>
<p class="leading-relaxed text-slate-300 mb-6">No. The bad-faith provisions, the active cancellation power and the wider well-known mark protection are stronger tools, but they are invoked in proceedings. Monitoring and early filing remain the cheapest protection. If a squatter already holds a registration, see <a href="{L}/trademark-registered-by-someone-else-china.html">your four recovery options</a>.</p>
"""),
                ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: the full text of the <em>Trademark Law of the PRC (2026 Revision)</em> published by CNIPA (26 June 2026); CNIPA's <em>Main Contents of the Revision</em> (10 July 2026); and the CNIPA notice of 28 September 2026 on the draft transition measures and draft Examination and Review Guidelines. Article numbers in this article refer to the 2026 law. This article is general information, not legal advice; outcomes depend on the specific facts and on the final implementing rules.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Need a portfolio review before the 1 January deadline?</strong> <a href="/contact.html">Talk to our team</a> about a pre-2027 audit and a 2-month watch configuration.</p></div>
"""),
            ],
        },
        'hub': {
            'slug': 'china-trademark-law-2026-revision-changes',
            'title': 'China Trademark Law 2026 Revision: Old Rules vs New Rules Side by Side',
            'desc': "A side-by-side comparison of China's 2019 and 2026 Trademark Laws for foreign brand owners, with article numbers, the draft transition rules and an action list before 1 January 2027.",
            'lede': "China's 2026 Trademark Law takes effect on 1 January 2027. This hub page maps every change that affects foreign brand owners to its article number and to the action it requires.",
            'card_text': "9 chapters, 87 articles, a 2-month opposition window and CNIPA-initiated cancellation. A clause-by-clause comparison of the 2019 and 2026 laws.",
            'tags': ['trademark law', '2027', 'article comparison'],
            'related': [
                ('{L}/china-trademark-law-2027-foreign-brands.html', 'What Foreign Brands Should Do Before 2027'),
                ('{L}/china-trademark-registration-complete-guide-2026.html', 'China Trademark Registration: Complete Guide'),
                ('{L}/common-reasons-trademark-rejection-china.html', 'Common Reasons for Trademark Rejection'),
            ],
            'sections': [
                ('at-a-glance', 'At a Glance', """
<p class="leading-relaxed text-slate-300 mb-6">Adopted on <strong>26 June 2026</strong> and effective <strong>1 January 2027</strong>, the revised PRC Trademark Law is the first comprehensive rewrite since 1983. It expands from 8 chapters / 73 articles to <strong>9 chapters / 87 articles</strong>, adds a dedicated chapter on conditions for registration, and shifts the system's centre of gravity from "who registered first" toward "who actually uses the mark in good faith".</p>
<p class="leading-relaxed text-slate-300 mb-6">For foreign brand owners, the revision is net positive on enforcement but raises the compliance bar on portfolio maintenance. Below is the clause-by-clause comparison; for the decision-oriented version, see <a href="{ACT}">What Foreign Brands Should Do Before 1 January 2027</a>.</p>
"""),
                ('side-by-side', 'Old vs New: Side-by-Side Comparison', """
<table>
<thead><tr><th>Topic</th><th>Until 31 Dec 2026 (2019 law)</th><th>From 1 Jan 2027 (2026 law)</th></tr></thead>
<tbody>
<tr><td>Opposition after publication</td><td>3 months (Art. 33)</td><td><strong>2 months (Art. 36)</strong></td></tr>
<tr><td>Refusal review</td><td>15 days to request review (Art. 34)</td><td>15 days; decision in 9 months, +3 extension (Art. 37)</td></tr>
<tr><td>Registrable signs</td><td>Words, devices, letters, numerals, 3D, colour combinations, sounds (Art. 8)</td><td>Same plus <strong>dynamic / motion marks</strong> (Art. 14)</td></tr>
<tr><td>Applications without intent to use</td><td>Bad-faith applications not intended for use rejected (Art. 4)</td><td>Refusal where there is no intent to use <em>and</em> the filing clearly exceeds normal business needs; deception or other improper means prohibited (Art. 19)</td></tr>
<tr><td>Penalty for the applicant</td><td>No fine on the applicant in the statute</td><td>Warning + fine up to <strong>RMB 100,000</strong> for bad-faith filing causing adverse effects (Art. 54)</td></tr>
<tr><td>Misleading use of a registered mark</td><td>No dedicated penalty</td><td>Up to 5&times; illegal turnover / RMB 250,000; possible revocation (Art. 56)</td></tr>
<tr><td>Non-use cancellation</td><td>Any party may apply after 3 consecutive years (Art. 49)</td><td>Any party may apply <strong>and CNIPA may cancel on its own initiative</strong> (Art. 57)</td></tr>
<tr><td>Well-known marks</td><td>Cross-class protection for marks registered in China (Art. 13)</td><td>Cross-class protection <strong>regardless of Chinese registration</strong> (Art. 21)</td></tr>
<tr><td>Recognition vs confirmation</td><td>"Recognition" of well-known status</td><td>"Confirmation", also available in unfair-competition proceedings (Art. 63)</td></tr>
<tr><td>Internet use</td><td>Not expressly stated</td><td>Use via information networks expressly covered (Art. 2)</td></tr>
<tr><td>One-year re-filing block</td><td>Applied after cancellation, invalidation or non-renewal (Art. 50)</td><td>Narrowed to voluntary cancellation by the owner (Art. 49)</td></tr>
<tr><td>Trademark agencies</td><td>General duties (Art. 68)</td><td>Recordal, practitioner sign-off, conflict-of-interest and penalty rules (Arts. 65&ndash;68)</td></tr>
<tr><td>Damages</td><td>Statutory calculation rules</td><td>Reasonable enforcement costs expressly included (Art. 77)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The 2026 law renumbers the entire statute, so older commentary citing 2019 article numbers is easy to misread. Always check which version an article number refers to.</p>
"""),
                ('six-changes', 'Six Changes That Matter Most for Foreign Brands', """
<h3>1. A two-month opposition window compresses the whole response chain</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 36 cuts the publication-based opposition period from three months to two. Detection, internal go/no-go approval, evidence collection, translation and local counsel instruction all have to fit into a shorter window. Brands that check the register occasionally will miss deadlines; a <a href="{L}/china-trademark-monitoring-protection.html">continuous watch programme</a> becomes a requirement rather than a nice-to-have.</p>
<h3>2. CNIPA can now cancel idle marks without a third-party request</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 57 adds ex officio cancellation for marks unused for three consecutive years without justification. This is a double-edged sword: it is an effective weapon against squatters who never use their registrations, but it also exposes dormant defensive registrations held by legitimate foreign brands. Article 2's express recognition of internet use helps — dated e-commerce listings, social accounts and online advertising can form part of a use-evidence file.</p>
<h3>3. Bad-faith filing is attacked at three levels</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 19 refuses speculative applications, Article 54 adds a fine of up to RMB 100,000, and Articles 65&ndash;68 impose duties and penalties on the agencies that assist them. Article 36 also makes "filing by deception or other improper means" an independent ground for opposition at the publication stage, rather than something that could only be raised later in invalidation.</p>
<h3>4. Dynamic marks become registrable</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 14 adds dynamic signs and their combinations to the list of registrable marks. Animated logos, app loading sequences and UI transitions that previously relied on copyright or unfair-competition arguments can now be protected as trademarks. The draft Examination Guidelines specify an MP4 video (up to 20 MB) plus 3&ndash;9 JPEG still frames and a description of how the mark is used.</p>
<h3>5. Unregistered well-known marks gain cross-class protection</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 21 removes the requirement that a well-known mark be registered in China before it can block dissimilar goods or services. Article 63 also allows well-known status to be confirmed in unfair-competition proceedings. This is directly relevant to foreign brands whose reputation in China precedes their filing — though strong evidence of that reputation remains essential.</p>
<h3>6. Misleading use and "心机商标" become a registrant's own risk</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 56 targets marks used in ways that mislead the public about quality, origin, ingredients or process, with fines and possible revocation. International brands using claims such as "Swiss Made", "medical grade" or "eco-friendly" in Chinese packaging, listings and advertising should be able to substantiate them — including when a licensee or OEM partner applies the mark.</p>
"""),
                ('transition-measures', 'What the Draft Transition Measures Add', """
<table>
<thead><tr><th>Draft article</th><th>Rule</th><th>Practical reading</th></tr></thead>
<tbody>
<tr><td>Art. 1&ndash;2</td><td>No retroactivity; substantive issues under the old law, procedural issues under the new</td><td>Pre-2027 applications decided on or after 1 Jan 2027 are handled under the new law; invalidation/cancellation of pre-2027 registrations keeps old substantive law</td></tr>
<tr><td>Art. 3</td><td>Dynamic mark filing materials</td><td>MP4 &le;20 MB, 3&ndash;9 JPEG frames, evidence of acquired distinctiveness within 15 days if requested</td></tr>
<tr><td>Art. 4</td><td>Opposition period determined by publication date</td><td>Domestic: Gazette publication date. International registration: WIPO publication date. Pre-2027 = 3 months; from 2027 = 2 months; no restart of a running clock</td></tr>
<tr><td>Art. 6&ndash;7</td><td>Isolation period and ex officio cancellation</td><td>Local trademark authorities investigate idle marks and report upward through CNIPA</td></tr>
<tr><td>Art. 9&ndash;10</td><td>New law prevails over the old Implementing Regulations; measures effective 1 Jan 2027</td><td>Do not assume the current Regulations override the revised statute during the transition</td></tr>
</tbody>
</table>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Draft status.</strong> These measures were published for comment on 28 September 2026 with a 12 November 2026 deadline, together with a draft Examination and Review Guidelines. Verify the final text before relying on any transition rule in a live matter.</p></div>
"""),
                ('your-action-list', 'Your Action List', """
<ul>
<li>Before 1 January 2027: <a href="{ACT}">run the five-step pre-2027 portfolio audit</a> and reconfigure your watch service for a 2-month window.</li>
<li>Check eligibility, documents and the local-agent requirement in <a href="{L}/who-can-register-trademark-in-china.html">Who Can Register a Trademark in China</a>.</li>
<li>Review the current process and timeline in the <a href="{L}/china-trademark-registration-complete-guide-2026.html">Complete Guide</a> and <a href="{L}/how-long-trademark-registration-china.html">How Long It Takes</a>.</li>
<li>Refresh rejection-risk assumptions against <a href="{L}/common-reasons-trademark-rejection-china.html">Common Reasons for Rejection</a> — Article 19 adds a new refusal ground.</li>
<li>If a squatter is already registered, compare opposition, invalidation, negotiation and rebranding in <a href="{L}/trademark-registered-by-someone-else-china.html">What Happens If Someone Registers Your Trademark First</a>.</li>
</ul>
"""),
                ('sources-and-caveats', 'Sources, Status and Caveats', """
<ul>
<li>Full text: <em>Trademark Law of the People's Republic of China (2026 Revision)</em>, CNIPA, 26 June 2026.</li>
<li>Official summary: CNIPA, <em>Main Contents of the Revision to the PRC Trademark Law</em>, 10 July 2026.</li>
<li>Transition: CNIPA notice on the draft <em>Measures for Handling Business Matters Following the Revised Trademark Law</em> and draft <em>Trademark Examination and Review Guidelines</em>, 28 September 2026.</li>
<li>Effective date and chapter structure also confirmed by the National People's Congress and the Supreme People's Court's public reporting, July&ndash;August 2026.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">Article numbers refer to the 2026 law unless marked otherwise. This page is general information, not legal advice. Last reviewed: 6 November 2026.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Want this reviewed against your own portfolio?</strong> <a href="/contact.html">Request a free consultation</a> with our China trademark team.</p></div>
"""),
            ],
        },
    },
}

CONTENT['ja'] = {
    'lang': 'ja',
    'locale_label': 'パンくずリスト',
    'home_label': 'ホーム',
    'blog_label': 'ブログ',
    'in_this_article': 'この記事の内容',
    'related_label': '関連記事',
    'cta_help': '中国での商標登録についてご相談ですか？',
    'cta_button': '無料相談',
    'cta_title': '中国商標のご相談はこちら',
    'cta_text': '専門スタッフが手続き全体をサポートします。',
    'cta_button_big': '無料相談を申し込む',
    'date_label': '2026年11月6日',
    'date_iso': '2026-11-06',
    'category_a': '法改正アップデート',
    'category_b': '法改正アップデート',
    'read_a': '約9分',
    'read_b': '約10分',
    'articles': {
        'act': {
            'slug': 'china-trademark-law-2027-foreign-brands',
            'title': '2027年1月1日施行・中国新商標法：外国ブランドが今やるべきこと',
            'desc': '改正中国商標法は2027年1月1日に施行されます。外国ブランド向けに、何が変わるのか、年内の出願に意味はあるのか、そして今取るべき5つの対応を解説します。',
            'lede': '1983年以来初の全面改正となる中国商標法が、2027年1月1日に施行されます。外国ブランドに影響する変更点と、残り期間で対応すべきことを整理しました。',
            'card_text': '異議申立期間は2ヶ月に短縮され、CNIPAによる職権取消や悪意出願への罰則が加わります。2027年1月1日までに外国ブランドが取るべき対応とは。',
            'tags': ['2027年商標法', '異議申立', 'CNIPA'],
            'related': [
                ('{L}/china-trademark-law-2026-revision-changes.html', '旧法・新法の条項対比'),
                ('{L}/china-trademark-monitoring-protection.html', '商標モニタリングと保護戦略'),
                ('{L}/trademark-registered-by-someone-else-china.html', '商標を先に登録された場合の対処'),
            ],
            'sections': [
                ('the-short-answer', '結論：早期出願は続けるべきだが、「旧法を確定させる」ためではない', """
<p class="leading-relaxed text-slate-300 mb-6">2026年6月26日、中国は商標法の全面改正を可決しました。施行日は<strong>2027年1月1日</strong>。1983年の制定以来初の全面改正であり、8章73条から<strong>9章87条</strong>へと拡張され、登録条件を定める独立の章が新設されています。</p>
<p class="leading-relaxed text-slate-300 mb-6">中国で商標権を持つ外国ブランド、あるいは出願を予定している企業への答えは明確です。<strong>早期出願は続けるべきですが、「旧法の適用を確定させる」ためだけに急ぐ意味はありません。</strong>2026年9月28日に公表されたCNIPAの移行措置（草案）によれば、2027年1月1日より前に出願され、同日以降に判断される案件は新法で処理されます。</p>
<p class="leading-relaxed text-slate-300 mb-6">それでも早期出願に価値があるのは、中国で一貫して最も重要だった<strong>「最初の出願日」</strong>を確保できるからです。中国は先願主義のままです。2027年法が変えるのは審査基準、手続期限、権利行使の手段であり、同一商標をめぐって誰が優先するかという原則ではありません。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>ステータス注記：</strong>改正法は成立済みで施行日も確定しています。一方、CNIPAの『改正後の商標法施行に伴う業務処理弁法』は<strong>草案</strong>です（意見募集は2026年11月12日まで）。最終条文が出るまで内容が変わり得るため、草案に基づく記述は以下で明示しています。</p></div>
"""),
                ('key-dates', '押さえるべき4つの日付', """
<table>
<thead><tr><th>日付</th><th>出来事</th><th>実務上の意味</th></tr></thead>
<tbody>
<tr><td>2026年6月26日</td><td>全国人大常委会が改正商標法を可決</td><td>条文が確定。9章87条の構成も確定</td></tr>
<tr><td>2026年9月28日</td><td>CNIPAが移行措置（草案）と審査審理指南（草案）を公表</td><td>係属案件と新しい商標類型の取扱い方針が判明</td></tr>
<tr><td>2026年11月12日</td><td>草案への意見募集期限</td><td>最終版は変更され得る。依拠する前に再確認が必要</td></tr>
<tr><td><strong>2027年1月1日</strong></td><td>改正商標法（および採択されれば移行措置）が施行</td><td>異議期間の短縮、新しい登録要素、職権取消が開始</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">出典：CNIPA『中華人民共和国商標法改正の主要内容』（2026年7月10日）、CNIPA通知（2026年9月28日）。</p>
"""),
                ('what-changes', '外国出願人に影響する変更点', """
<table>
<thead><tr><th>変更点</th><th>2026年法の条文</th><th>実務への影響</th></tr></thead>
<tbody>
<tr><td>異議申立期間</td><td>第36条</td><td>初步審定公告後<strong>3ヶ月 &rarr; 2ヶ月</strong></td></tr>
<tr><td>拒絶査定不服審判</td><td>第37条</td><td>收到から15日以内に請求。CNIPAは9ヶ月以内に決定（3ヶ月延長可）</td></tr>
<tr><td>登録可能な標識</td><td>第14条</td><td>文字・図形・色彩・音に加え<strong>動的標識（モーションマーク）</strong>を追加</td></tr>
<tr><td>悪意・大量出願</td><td>第19条・第54条</td><td>使用意思がなく、かつ正常な経営需要を明らかに超える出願は登録拒絶。警告および最高10万元の過料</td></tr>
<tr><td>誤認を招く使用</td><td>第56条</td><td>違法売上高の5倍以下または25万元以下の過料。是正されなければ登録抹消も</td></tr>
<tr><td>不使用商標</td><td>第57条</td><td>3年連続不使用の場合、<strong>CNIPAが職権で取り消すことが可能</strong>に</td></tr>
<tr><td>馳名商標</td><td>第21条</td><td>中国での登録の有無を問わず、跨類保護が可能に</td></tr>
<tr><td>ネットワーク上の使用</td><td>第2条</td><td>インターネット等を通じた使用が商標使用に明示的に含まれる</td></tr>
<tr><td>商標代理機構</td><td>第65〜68条</td><td>届出義務・担当者責任・利益相反への罰則を強化</td></tr>
<tr><td>損害賠償</td><td>第77条</td><td>権利侵害停止に要した合理的費用が賠償額に明示的に含まれる</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">条文番号付きの全対比表は<a href="{HUB}">「中国商標法2026年改正：旧法・新法の条項対比」</a>をご覧ください。</p>
"""),
                ('should-you-file-before-2027', '2026年12月31日までに急いで出願すべきか', """
<p class="leading-relaxed text-slate-300 mb-6">2026年11月の時点で最も多く寄せられる質問です。答えは二段階で整理する必要があります。</p>
<h3>旧法の審査基準を固定することはできない</h3>
<p class="leading-relaxed text-slate-300 mb-6">移行措置（草案）は<strong>「実体は旧法、手続は新法」</strong>を基本原則としています。2027年1月1日より前に出願された登録・異議申立・拒絶査定不服審判等の案件で、CNIPAが同日以降に決定を下す場合、草案は新法を適用すると定めています。一方、2027年より前に登録された商標に対する無効審判・取消については、手続は新法、実体は登録時に施行されていた法が適用されます。</p>
<h3>ただし、先願主義の下で早い出願日は今も最大の防御</h3>
<p class="leading-relaxed text-slate-300 mb-6">競合する出願人の優先順位は、どの法律が施行されていたかではなく、誰が先に出願したかで決まります。今出願すれば、明日出願するかもしれないハイジャッカー、販売代理店、OEM工場に対して地位を確保できます。新法の悪意出願対策は追加の救済手段として有効ですが、先に出願することの代わりにはなりません。</p>
<h3>本当に決め手になるのは「公告日」</h3>
<p class="leading-relaxed text-slate-300 mb-6">草案第4条は、異議申立期間の長さを出願日ではなく<strong>公告日</strong>で判断すると定めています。国内出願は商標公報への初步審定公告日、中国を指定する国際登録はWIPOの公告日が基準です。2027年1月1日より前に公告された案件は3ヶ月、同日以降に公告された案件は2ヶ月となり、年をまたいで進行中の期間が<strong>リセットされることはありません</strong>。ウォッチングサービスを運用するブランドにとって、最も実務的に重要な移行ルールです。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>草案を最終版として扱わないでください。</strong>意見募集は2026年11月12日までです。社内期限の設定や係属中の異議案件の助言にあたっては、最終条文を必ず確認してください。</p></div>
"""),
                ('action-checklist', '2027年1月1日までに実施すべき5項目', """
<ol>
<li><strong>「使用意思なし」のリスクをポートフォリオ全体で監査する。</strong>第19条は、使用意思がなく正常な経営需要を明らかに超える出願を拒絶します。広範な防御登録自体は原則として適法ですが、各区分に事業根拠・拡張計画・模倣品対策・サブクラス上の理由を文書で残してください。</li>
<li><strong>ウォッチングを2ヶ月対応に引き上げる。</strong>月次の公報チェックと緩やかな社内承認では間に合わなくなります。重点区分と中国語表記のバリエーションを週次で監視し、現地代理人を事前授権し、証拠パッケージを常備して公告後数日で異議を出せる体制を作ります。<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>もご参照ください。</li>
<li><strong>使用証拠ファイルを今から構築する。</strong>CNIPAが職権で不使用商標を取り消し得るため、日付入りの請求書・キャプチャ日付付きEC画面・包装・通関記録・販売店契約・展示会資料を、商標および区分ごとに初日から保管します。</li>
<li><strong>中国語表記のカバレッジを確認する。</strong>中国では英語表記と中国語表記は別個の権利です。公式中国語名、一般的な音写、消費者が自然に付けた通称が、必要な区分で登録されているか確認してください。<a href="{L}/china-trademark-classes-complete-guide.html">区分ガイド</a>ではサブクラスが保護範囲に与える影響を解説しています。</li>
<li><strong>代理人を再点検する。</strong>第65〜68条は代理機構と従業者のCNIPA届出、利益相反、悪意出願への加担に対する罰則を定めています。届出状況と、自社案件に誰が署名しているかを確認してください。</li>
</ol>
"""),
                ('what-does-not-change', '変わらないこと', """
<ul>
<li><strong>先願主義。</strong>最初に使用した者に権利が与えられるわけではありません。外国での登録は中国では効力を持ちません。</li>
<li><strong>権利の地域性。</strong>CNIPA登録は中国大陸を対象とします。中国香港・中国マカオ・中国台湾にはそれぞれ別途の出願が必要です。</li>
<li><strong>現地代理人の必要性。</strong>中国国内に住所または営業所を持たない外国出願人は、引き続き中国の商標代理機構を通じて出願します。</li>
<li><strong>10年の存続期間と更新。</strong>登録は10年間有効で更新可能です。<a href="{L}/china-trademark-renewal-guide.html">更新ガイド</a>をご覧ください。</li>
<li><strong>マドリッドルート。</strong>WIPO経由で中国を指定できますが、審査は中国法に基づきます。<a href="{L}/madrid-vs-direct-filing-china.html">マドリッドと直接出願の比較</a>もご参照ください。</li>
</ul>
"""),
                ('faq', 'よくある質問', """
<h3>係属中の出願は旧法で審査されますか？</h3>
<p class="leading-relaxed text-slate-300 mb-6">2026年9月の草案では、CNIPAが2027年1月1日以降に判断する場合、原則として新法が適用されます。計画上はその前提で進め、最終版で確認してください。</p>
<h3>2026年12月に公告された商標にも異議を申し立てられますか？</h3>
<p class="leading-relaxed text-slate-300 mb-6">草案によれば、2027年1月1日より前に公告された案件は3ヶ月の異議期間が維持され、新法によって時計が振り戻されることはありません。ただし証拠収集と翻訳には時間がかかるため、最終週まで待つべきではありません。</p>
<h3>新法でハイジャッカーは自動的に排除されますか？</h3>
<p class="leading-relaxed text-slate-300 mb-6">いいえ。悪意出願規制、職権取消、馳名商標保護の拡張はいずれも手続の中で主張・行使する道具です。監視と早期出願が依然として最も安価な防御です。すでに登録されている場合は<a href="{L}/trademark-registered-by-someone-else-china.html">4つの回復オプション</a>をご覧ください。</p>
"""),
                ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：CNIPA公表『中華人民共和国商標法（2026年改正）』全文（2026年6月26日）、CNIPA『商標法改正の主要内容』（2026年7月10日）、CNIPA通知（2026年9月28日、移行措置草案および審査審理指南草案）。本記事の条番号は特に断りのない限り2026年法のものです。本記事は一般情報であり法的助言ではありません。結論は個別の事実関係と最終的な実施規則に左右されます。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>1月1日までにポートフォリオを点検しますか？</strong> <a href="/contact.html">2027年対応監査と2ヶ月ウォッチ設定についてご相談ください</a>。</p></div>
"""),
            ],
        },
        'hub': {
            'slug': 'china-trademark-law-2026-revision-changes',
            'title': '中国商標法2026年改正：旧法・新法の条項対比と実務インパクト',
            'desc': '2027年1月1日施行の中国改正商標法について、2019年法との条項対比、条文番号、移行措置草案、外国ブランドの対応リストを一覧で解説します。',
            'lede': '中国商標法2026年改正は2027年1月1日に施行されます。外国ブランドに影響する全変更点を条文番号と必要なアクションに対応付けたハブページです。',
            'card_text': '9章87条、2ヶ月の異議期間、CNIPAの職権取消。2019年法と2026年法を条項単位で比較しました。',
            'tags': ['商標法改正', '2027年', '条項対比'],
            'related': [
                ('{L}/china-trademark-law-2027-foreign-brands.html', '2027年までに外国ブランドがやるべきこと'),
                ('{L}/china-trademark-registration-complete-guide-2026.html', '中国商標登録 完全ガイド'),
                ('{L}/common-reasons-trademark-rejection-china.html', '商標登録が拒絶される主な理由'),
            ],
            'sections': [
                ('at-a-glance', '全体像', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2026年6月26日</strong>に採択され、<strong>2027年1月1日</strong>に施行される改正中国商標法は、1983年以来初の全面改正です。8章73条から<strong>9章87条</strong>へ拡張され、登録条件を扱う独立の章が設けられました。制度の重心は「誰が最初に登録したか」から「誰が誠実に実際に使用しているか」へと大きく動きます。</p>
<p class="leading-relaxed text-slate-300 mb-6">外国ブランドにとって権利行使面では総じて追い風ですが、ポートフォリオ管理のコンプライアンス水準は上がります。以下に条項単位の対比を示します。意思決定向けの解説は<a href="{ACT}">「2027年1月1日までに外国ブランドがやるべきこと」</a>をご覧ください。</p>
"""),
                ('side-by-side', '旧法・新法 対比表', """
<table>
<thead><tr><th>項目</th><th>2026年12月31日まで（2019年法）</th><th>2027年1月1日から（2026年法）</th></tr></thead>
<tbody>
<tr><td>公告後の異議申立</td><td>3ヶ月（第33条）</td><td><strong>2ヶ月（第36条）</strong></td></tr>
<tr><td>拒絶査定不服審判</td><td>收到から15日以内に請求（第34条）</td><td>15日。9ヶ月以内に決定、3ヶ月延長可（第37条）</td></tr>
<tr><td>登録可能な標識</td><td>文字・図形・記号・数字・立体・色彩の組合せ・音（第8条）</td><td>これらに加え<strong>動的標識</strong>（第14条）</td></tr>
<tr><td>使用意思のない出願</td><td>使用を目的としない悪意の出願を拒絶（第4条）</td><td>使用意思がなく、かつ正常な経営需要を明らかに超える場合に拒絶。欺罔その他不正の手段も禁止（第19条）</td></tr>
<tr><td>出願人への罰則</td><td>法律上の過料なし</td><td>悪意出願で不良な影響を生じた場合、警告＋最高<strong>10万元</strong>（第54条）</td></tr>
<tr><td>登録商標の誤認使用</td><td>専用の罰則なし</td><td>違法売上高の5倍以下／25万元以下、是正なき場合は登録抹消（第56条）</td></tr>
<tr><td>不使用取消</td><td>3年連続不使用で誰でも請求可（第49条）</td><td>第三者請求に加え<strong>CNIPAが職権で取消可能</strong>（第57条）</td></tr>
<tr><td>馳名商標</td><td>中国で登録された馳名商標に跨類保護（第13条）</td><td><strong>中国登録の有無を問わず</strong>跨類保護（第21条）</td></tr>
<tr><td>認定か確認か</td><td>馳名商標の「認定」</td><td>「確認」に変更。不正競争案件でも確認可能（第63条）</td></tr>
<tr><td>ネットワーク上の使用</td><td>明示規定なし</td><td>情報ネットワークを通じた使用を明記（第2条）</td></tr>
<tr><td>1年間の再出願制限</td><td>取消・無効・更新懈怠の後に適用（第50条）</td><td>権利者が自発的に抹消した場合に限定（第49条）</td></tr>
<tr><td>商標代理機構</td><td>一般的な義務規定（第68条）</td><td>届出・担当者署名・利益相反・罰則を整備（第65〜68条）</td></tr>
<tr><td>損害賠償</td><td>法定の算定ルール</td><td>権利行使に要した合理的費用を明記（第77条）</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">2026年法は条番号が全面的に振り直されているため、2019年法の条番号を引用した旧い解説は誤読の原因になります。必ずどちらの版の条番号かを確認してください。</p>
"""),
                ('six-changes', '外国ブランドに効く6つの変更', """
<h3>1. 異議申立期間の2ヶ月短縮は、対応チェーン全体を圧縮する</h3>
<p class="leading-relaxed text-slate-300 mb-6">第36条は公告後の異議期間を3ヶ月から2ヶ月に短縮します。検知、社内の可否判断、証拠収集、翻訳、現地代理人への指示を、より短い期間に収める必要があります。登録簿を時々確認する程度では期限を逃します。<a href="{L}/china-trademark-monitoring-protection.html">継続的なウォッチング体制</a>が「あれば望ましい」から「必須」になります。</p>
<h3>2. CNIPAが第三者請求なしに不使用商標を取り消せるように</h3>
<p class="leading-relaxed text-slate-300 mb-6">第57条は、正当な理由なく3年連続で使用されなかった商標の職権取消を追加しました。登録を使わないハイジャッカーへの有効な武器である一方、正当な外国ブランドが持つ休眠的な防御登録もリスクにさらします。第2条がネットワーク上の使用を明示したことで、日付入りのEC画面、ソーシャルアカウント、オンライン広告を使用証拠の一部として組み込めます。</p>
<h3>3. 悪意出願を三層で叩く</h3>
<p class="leading-relaxed text-slate-300 mb-6">第19条が投機的出願を拒絶し、第54条が最高10万元の過料を加え、第65〜68条が関与した代理機構に義務と罰則を課します。さらに第36条は「欺罔その他不正の手段による出願」を公告段階の異議理由として独立させ、登録後の無効審判を待たずに主張できるようにしました。</p>
<h3>4. 動的標識が登録可能に</h3>
<p class="leading-relaxed text-slate-300 mb-6">第14条は動的標識およびその組合せを登録可能な標識に加えます。従来は著作権や不正競争法に頼っていたアニメーションロゴ、アプリの起動シーケンス、UI遷移を商標として保護できます。審査指南草案では、20MB以下のMP4動画、3〜9枚のJPEG静止画、使用態様の説明が求められています。</p>
<h3>5. 未登録の馳名商標にも跨類保護</h3>
<p class="leading-relaxed text-slate-300 mb-6">第21条は、非類似の商品・役務を差し止める前提だった「中国での登録」要件を撤廃しました。第63条は不正競争手続における馳名性の確認も可能にしています。中国での知名度が出願に先行する外国ブランドに直結する変更ですが、知名度を立証する強い証拠は依然として不可欠です。</p>
<h3>6. 誤認を招く使用は、権利者自身のリスクになる</h3>
<p class="leading-relaxed text-slate-300 mb-6">第56条は、品質・産地・原料・製法について公衆を誤認させる商標使用を罰し、過料および登録抹消の対象とします。「Swiss Made」「医療グレード」「エコ」等の表示を中国向け包装・EC画面・広告で使う場合、ライセンシーやOEM先が標識を付する場合も含め、裏付けを用意しておく必要があります。</p>
"""),
                ('transition-measures', '移行措置草案が追加するルール', """
<table>
<thead><tr><th>草案条文</th><th>規則</th><th>実務的な読み方</th></tr></thead>
<tbody>
<tr><td>第1〜2条</td><td>遡及不適用、実体は旧法・手続は新法</td><td>2027年より前の出願で同日以降に決定される案件は新法。2027年より前の登録に対する無効・取消は実体が旧法</td></tr>
<tr><td>第3条</td><td>動的標識の出願書類</td><td>20MB以下のMP4、3〜9枚のJPEG、使用により識別力を得た証拠は通知から15日以内</td></tr>
<tr><td>第4条</td><td>異議期間は公告日で判断</td><td>国内は商標公報の公告日、国際登録はWIPO公告日。2027年より前は3ヶ月、以降は2ヶ月。進行中の期間はリセットしない</td></tr>
<tr><td>第6〜7条</td><td>隔離期間と職権取消</td><td>地方の商標管理部門が不使用商標を調査し、CNIPAへ逐次報告</td></tr>
<tr><td>第9〜10条</td><td>旧実施条例より新法が優先、措置は2027年1月1日施行</td><td>移行期に現行実施条例が改正法に優先するという前提は置けない</td></tr>
</tbody>
</table>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>草案の扱いに注意。</strong>本措置は2026年9月28日に意見募集が開始され、期限は2026年11月12日です。審査審理指南草案も同時に公表されています。係属案件で移行ルールに依拠する前に、最終版を必ず確認してください。</p></div>
"""),
                ('your-action-list', '対応チェックリスト', """
<ul>
<li>2027年1月1日までに：<a href="{ACT}">5項目の事前監査</a>を実施し、ウォッチングを2ヶ月対応に再設定する。</li>
<li>出願資格・必要書類・現地代理人の要件は<a href="{L}/who-can-register-trademark-in-china.html">「中国で商標登録できるのは誰か」</a>で確認する。</li>
<li>現行手続と期間は<a href="{L}/china-trademark-registration-complete-guide-2026.html">完全ガイド</a>および<a href="{L}/how-long-trademark-registration-china.html">所要期間ガイド</a>で確認する。</li>
<li>第19条で拒絶理由が増えたことを踏まえ、<a href="{L}/common-reasons-trademark-rejection-china.html">拒絶の主な理由</a>の前提を更新する。</li>
<li>すでにハイジャッカーが登録済みの場合は、<a href="{L}/trademark-registered-by-someone-else-china.html">異議・無効・交渉・リブランディングの比較</a>を参照する。</li>
</ul>
"""),
                ('sources-and-caveats', '出典・ステータス・注意書き', """
<ul>
<li>全文：『中華人民共和国商標法（2026年改正）』CNIPA、2026年6月26日。</li>
<li>公式解説：CNIPA『中華人民共和国商標法改正の主要内容』、2026年7月10日。</li>
<li>移行：CNIPA『改正後の商標法施行に伴う業務処理弁法（意見募集稿）』および『商標審査審理指南（意見募集稿）』に関する通知、2026年9月28日。</li>
<li>施行日・章構成は全国人大および最高人民法院の2026年7〜8月の公表資料でも確認済み。</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">条番号は特に断りのない限り2026年法のものです。本ページは一般情報であり法的助言ではありません。最終確認日：2026年11月6日。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>自社ポートフォリオに照らして確認しますか？</strong> <a href="/contact.html">中国商標チームに無料でご相談ください</a>。</p></div>
"""),
            ],
        },
    },
}

CONTENT['ko'] = {
    'lang': 'ko',
    'locale_label': '브레드크럼',
    'home_label': '홈',
    'blog_label': '블로그',
    'in_this_article': '이 글의 내용',
    'related_label': '관련 글',
    'cta_help': '중국 상표 등록에 도움이 필요하신가요?',
    'cta_button': '무료 상담',
    'cta_title': '중국 상표, 전문가와 상담하세요',
    'cta_text': '전체 절차를 전문가가 안내해 드립니다.',
    'cta_button_big': '무료 상담 신청',
    'date_label': '2026년 11월 6일',
    'date_iso': '2026-11-06',
    'category_a': '법 개정 업데이트',
    'category_b': '법 개정 업데이트',
    'read_a': '약 9분',
    'read_b': '약 10분',
    'articles': {
        'act': {
            'slug': 'china-trademark-law-2027-foreign-brands',
            'title': '2027년 1월 1일 시행 중국 신(新) 상표법: 외국 브랜드가 지금 해야 할 일',
            'desc': '중국 개정 상표법이 2027년 1월 1일 시행됩니다. 무엇이 바뀌는지, 연내 출원이 의미가 있는지, 지금 취해야 할 다섯 가지 조치를 외국 브랜드 관점에서 정리했습니다.',
            'lede': '1983년 이후 첫 전면 개정인 중국 상표법이 2027년 1월 1일 시행됩니다. 외국 브랜드에 영향을 주는 변경 사항과 남은 기간의 대응 과제를 정리했습니다.',
            'card_text': '이의신청 기간은 2개월로 짧아지고 CNIPA의 직권 취소와 악의적 출원 제재가 추가됩니다. 2027년 1월 1일 전에 무엇을 해야 할까요?',
            'tags': ['2027년 상표법', '이의신청', 'CNIPA'],
            'related': [
                ('{L}/china-trademark-law-2026-revision-changes.html', '구법·신법 조항 대조'),
                ('{L}/china-trademark-monitoring-protection.html', '상표 모니터링과 보호 전략'),
                ('{L}/trademark-registered-by-someone-else-china.html', '상표를 먼저 등록당했을 때의 대응'),
            ],
            'sections': [
                ('the-short-answer', '결론: 조기 출원은 계속하되, "구법 확정"을 목적으로 서두르지는 마십시오', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 6월 26일 중국은 상표법 전면 개정안을 통과시켰습니다. 시행일은 <strong>2027년 1월 1일</strong>입니다. 1983년 제정 이후 첫 전면 개정으로, 8장 73조에서 <strong>9장 87조</strong>로 확대되었고 등록 요건을 다루는 독립된 장이 신설되었습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">중국에 상표권을 보유한 외국 브랜드나 출원을 준비 중인 기업에 대한 답은 명확합니다. <strong>조기 출원은 계속해야 하지만, "구법의 적용을 확정"하기 위해서만 서두를 이유는 없습니다.</strong> 2026년 9월 28일 공개된 CNIPA의 경과 조치(초안)에 따르면, 2027년 1월 1일 이전에 출원되었으나 그날 이후 결정되는 사건은 신법으로 처리됩니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">그럼에도 조기 출원이 여전히 가치 있는 이유는, 중국에서 줄곧 가장 중요했던 <strong>"가장 이른 출원일"</strong>을 확보할 수 있기 때문입니다. 중국은 여전히 선출원주의입니다. 2027년 법이 바꾸는 것은 심사 기준, 절차 기한, 권리 행사 수단이며 동일 상표를 두고 누가 우선하는지라는 원칙은 아닙니다.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>상태 안내:</strong> 개정법은 이미 통과되었고 시행일도 확정되었습니다. 반면 CNIPA의 『개정 후 상표법 시행에 따른 업무 처리 방안』은 아직 <strong>초안</strong>입니다(의견 수렴 마감 2026년 11월 12일). 최종 문구가 확정되기 전까지 내용이 바뀔 수 있으므로, 초안에 근거한 서술은 아래에서 명시했습니다.</p></div>
"""),
                ('key-dates', '반드시 확인할 네 가지 날짜', """
<table>
<thead><tr><th>날짜</th><th>내용</th><th>실무상 의미</th></tr></thead>
<tbody>
<tr><td>2026년 6월 26일</td><td>전국인대 상무위원회, 개정 상표법 통과</td><td>조문 확정. 9장 87조 구성도 확정</td></tr>
<tr><td>2026년 9월 28일</td><td>CNIPA, 경과 조치(초안)와 심사심리 지침(초안) 공개</td><td>계류 사건과 신규 상표 유형의 처리 방침 확인</td></tr>
<tr><td>2026년 11월 12일</td><td>초안 의견 수렴 마감</td><td>최종안은 달라질 수 있음. 근거로 삼기 전 재확인 필요</td></tr>
<tr><td><strong>2027년 1월 1일</strong></td><td>개정 상표법(및 채택 시 경과 조치) 시행</td><td>이의신청 기간 단축, 신규 등록 요소, 직권 취소 개시</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">출처: CNIPA 『중화인민공화국 상표법 개정 주요 내용』(2026년 7월 10일), CNIPA 공고(2026년 9월 28일).</p>
"""),
                ('what-changes', '외국 출원인에게 영향을 주는 변경 사항', """
<table>
<thead><tr><th>변경 사항</th><th>2026년 법 조항</th><th>실무 영향</th></tr></thead>
<tbody>
<tr><td>이의신청 기간</td><td>제36조</td><td>초보심정 공고 후 <strong>3개월 &rarr; 2개월</strong></td></tr>
<tr><td>거절 결정 불복 심판</td><td>제37조</td><td>통지 수령 후 15일 내 청구. CNIPA는 9개월 내 결정(3개월 연장 가능)</td></tr>
<tr><td>등록 가능 표지</td><td>제14조</td><td>문자·도형·색채·소리에 더해 <strong>동적 표지(모션 마크)</strong> 추가</td></tr>
<tr><td>악의·대량 출원</td><td>제19조·제54조</td><td>사용 의사가 없고 정상적 경영 수요를 명백히 초과하는 출원은 거절. 경고 및 최고 10만 위안 과태료</td></tr>
<tr><td>오인을 유발하는 사용</td><td>제56조</td><td>위법 매출액의 5배 이하 또는 25만 위안 이하 과태료. 미시정 시 등록 취소 가능</td></tr>
<tr><td>미사용 상표</td><td>제57조</td><td>3년 연속 미사용 시 <strong>CNIPA가 직권으로 취소 가능</strong></td></tr>
<tr><td>저명상표</td><td>제21조</td><td>중국 등록 여부와 무관하게 이종(異種) 상품·서비스에 대한 보호 가능</td></tr>
<tr><td>네트워크상 사용</td><td>제2조</td><td>인터넷 등을 통한 사용이 상표 사용에 명시적으로 포함</td></tr>
<tr><td>상표 대리 기관</td><td>제65~68조</td><td>등록 의무, 담당자 책임, 이해상충에 대한 제재 강화</td></tr>
<tr><td>손해배상</td><td>제77조</td><td>침해 중지에 소요된 합리적 비용이 배상액에 명시적으로 포함</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">조항 번호를 포함한 전체 대조표는 <a href="{HUB}">「중국 상표법 2026년 개정: 구법·신법 조항 대조」</a>에서 확인하실 수 있습니다.</p>
"""),
                ('should-you-file-before-2027', '2026년 12월 31일 전에 서둘러 출원해야 할까요?', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 11월 현재 가장 많이 받는 질문입니다. 답은 두 단계로 나누어야 정확합니다.</p>
<h3>구법의 심사 기준을 고정할 수는 없습니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">경과 조치(초안)는 <strong>"실체는 구법, 절차는 신법"</strong>을 기본 원칙으로 삼습니다. 2027년 1월 1일 이전에 제기된 등록·이의신청·거절 불복 심판 등에서 CNIPA가 그날 이후 결정하는 경우, 초안은 신법을 적용하도록 정하고 있습니다. 반면 2027년 이전에 이미 등록된 상표에 대한 무효심판·취소는 절차는 신법, 실체는 등록 당시 시행되던 법이 적용됩니다.</p>
<h3>다만 선출원주의에서 이른 출원일은 여전히 최고의 방어 수단입니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">경합하는 출원인 간 우선순위는 어느 법이 시행 중이었는지가 아니라 누가 먼저 출원했는지로 결정됩니다. 지금 출원하면 내일 출원할지 모르는 도용자, 유통사, OEM 공장에 대해 지위를 확보할 수 있습니다. 신법의 악의 출원 규제는 추가 구제 수단으로 유용하지만, 먼저 출원하는 것을 대체하지는 못합니다.</p>
<h3>실제로 결정적인 날짜는 "공고일"입니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">초안 제4조는 이의신청 기간의 길이를 출원일이 아니라 <strong>공고일</strong>로 판단합니다. 국내 출원은 상표공보의 초보심정 공고일, 중국을 지정하는 국제등록은 WIPO 공고일이 기준입니다. 2027년 1월 1일 전에 공고된 사건은 3개월, 그날 이후 공고된 사건은 2개월이 적용되며, 연도를 넘어 진행 중인 기간이 <strong>새로 시작되지 않습니다</strong>. 워칭 서비스를 운영하는 브랜드에 가장 실무적으로 중요한 경과 규정입니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>초안을 최종안으로 취급하지 마십시오.</strong> 의견 수렴은 2026년 11월 12일까지입니다. 사내 기한을 정하거나 진행 중인 이의신청에 대해 자문하기 전에 최종 문구를 반드시 확인하십시오.</p></div>
"""),
                ('action-checklist', '2027년 1월 1일까지 실행할 다섯 가지', """
<ol>
<li><strong>"사용 의사 없음" 리스크를 포트폴리오 전체에서 점검하십시오.</strong> 제19조는 사용 의사가 없고 정상적 경영 수요를 명백히 초과하는 출원을 거절합니다. 광범위한 방어 등록 자체는 원칙적으로 허용되지만, 모든 클래스에 사업 근거, 확장 계획, 위조품 대응 목적, 서브클래스 논리를 문서로 남겨야 합니다.</li>
<li><strong>워칭을 2개월 대응 체계로 끌어올리십시오.</strong> 월 1회 공보 확인과 느린 사내 승인으로는 더 이상 안전하지 않습니다. 핵심 클래스와 중국어 표기 변형을 주 단위로 모니터링하고, 현지 대리인을 사전에 지정하며, 공고 후 며칠 내 이의를 제기할 수 있도록 증거 패키지를 상비하십시오. <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>도 참고하십시오.</li>
<li><strong>사용 증거 파일을 지금부터 구축하십시오.</strong> CNIPA가 직권으로 미사용 상표를 취소할 수 있으므로, 날짜가 기재된 청구서, 캡처 일자가 있는 플랫폼 화면, 포장, 통관 기록, 유통 계약, 전시 자료를 상표 및 클래스별로 첫날부터 보관해야 합니다.</li>
<li><strong>중국어 표기 범위를 확인하십시오.</strong> 중국에서 영문 표기와 중국어 표기는 별개의 권리입니다. 공식 중국어 이름, 일반적인 음역, 소비자가 붙인 애칭이 필요한 클래스에 등록되어 있는지 확인하십시오. <a href="{L}/china-trademark-classes-complete-guide.html">클래스 가이드</a>에서 서브클래스가 보호 범위에 미치는 영향을 설명합니다.</li>
<li><strong>대리인을 재점검하십시오.</strong> 제65~68조는 대리 기관과 종사자의 CNIPA 등록, 이해상충, 악의 출원 가담에 대한 제재를 규정합니다. 등록 상태와 자사 사건에 실제로 서명하는 담당자가 누구인지 확인하십시오.</li>
</ol>
"""),
                ('what-does-not-change', '바뀌지 않는 것', """
<ul>
<li><strong>선출원주의.</strong> 먼저 사용한 자에게 권리가 주어지지 않습니다. 외국 등록은 중국에서 효력이 없습니다.</li>
<li><strong>권리의 지역성.</strong> CNIPA 등록은 중국 대륙에 적용됩니다. 중국 홍콩·중국 마카오·중국 대만에는 각각 별도 출원이 필요합니다.</li>
<li><strong>현지 대리인 요건.</strong> 중국 내 주소나 영업장이 없는 외국 출원인은 계속 중국 상표 대리 기관을 통해 출원합니다.</li>
<li><strong>10년 존속기간과 갱신.</strong> 등록은 10년간 유효하며 갱신할 수 있습니다. <a href="{L}/china-trademark-renewal-guide.html">갱신 가이드</a>를 참고하십시오.</li>
<li><strong>마드리드 경로.</strong> WIPO를 통해 중국을 지정할 수 있으나 심사는 중국법에 따릅니다. <a href="{L}/madrid-vs-direct-filing-china.html">마드리드 vs 직접 출원 비교</a>도 확인하십시오.</li>
</ul>
"""),
                ('faq', '자주 묻는 질문', """
<h3>계류 중인 출원은 구법으로 심사되나요?</h3>
<p class="leading-relaxed text-slate-300 mb-6">2026년 9월 초안에 따르면 CNIPA가 2027년 1월 1일 이후 결정하는 경우 원칙적으로 신법이 적용됩니다. 계획은 이 전제로 세우되 최종안에서 확인하십시오.</p>
<h3>2026년 12월에 공고된 상표에도 이의를 제기할 수 있나요?</h3>
<p class="leading-relaxed text-slate-300 mb-6">초안에 따르면 2027년 1월 1일 전에 공고된 사건은 3개월 이의신청 기간이 유지되며 신법 때문에 기산이 되돌아가지 않습니다. 다만 증거 수집과 번역에 시간이 걸리므로 마지막 주까지 미루어서는 안 됩니다.</p>
<h3>신법이 도용자를 자동으로 제거해 주나요?</h3>
<p class="leading-relaxed text-slate-300 mb-6">아닙니다. 악의 출원 규제, 직권 취소, 저명상표 보호 확대는 모두 절차 안에서 주장·행사해야 하는 수단입니다. 모니터링과 조기 출원이 여전히 가장 저렴한 방어책입니다. 이미 등록된 도용 상표가 있다면 <a href="{L}/trademark-registered-by-someone-else-china.html">네 가지 회복 옵션</a>을 참고하십시오.</p>
"""),
                ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: CNIPA가 공개한 『중화인민공화국 상표법(2026년 개정)』 전문(2026년 6월 26일), CNIPA 『상표법 개정 주요 내용』(2026년 7월 10일), CNIPA 공고(2026년 9월 28일, 경과 조치 초안 및 심사심리 지침 초안). 이 글의 조항 번호는 별도 표기가 없으면 2026년 법 기준입니다. 본 글은 일반 정보이며 법률 자문이 아닙니다. 결론은 개별 사실관계와 최종 시행 규칙에 따라 달라집니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>1월 1일 전에 포트폴리오를 점검하시겠습니까?</strong> <a href="/contact.html">2027년 대응 감사와 2개월 워칭 설정에 대해 상담하세요</a>.</p></div>
"""),
            ],
        },
        'hub': {
            'slug': 'china-trademark-law-2026-revision-changes',
            'title': '중국 상표법 2026년 개정: 구법·신법 조항 대조와 실무 영향',
            'desc': '2027년 1월 1일 시행되는 중국 개정 상표법을 2019년 법과 조항별로 대조하고, 조문 번호·경과 조치 초안·외국 브랜드 대응 목록을 정리했습니다.',
            'lede': '중국 상표법 2026년 개정은 2027년 1월 1일 시행됩니다. 외국 브랜드에 영향을 주는 모든 변경 사항을 조항 번호와 필요한 조치에 연결한 허브 페이지입니다.',
            'card_text': '9장 87조, 2개월 이의신청 기간, CNIPA 직권 취소. 2019년 법과 2026년 법을 조항 단위로 비교했습니다.',
            'tags': ['상표법 개정', '2027년', '조항 대조'],
            'related': [
                ('{L}/china-trademark-law-2027-foreign-brands.html', '2027년 전에 외국 브랜드가 해야 할 일'),
                ('{L}/china-trademark-registration-complete-guide-2026.html', '중국 상표 등록 완전 가이드'),
                ('{L}/common-reasons-trademark-rejection-china.html', '상표 등록이 거절되는 주요 이유'),
            ],
            'sections': [
                ('at-a-glance', '한눈에 보기', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2026년 6월 26일</strong> 통과되어 <strong>2027년 1월 1일</strong> 시행되는 개정 중국 상표법은 1983년 이후 첫 전면 개정입니다. 8장 73조에서 <strong>9장 87조</strong>로 확대되고 등록 요건을 다루는 별도의 장이 신설되었습니다. 제도의 무게중심은 "누가 먼저 등록했는가"에서 "누가 성실하게 실제로 사용하는가"로 이동합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">외국 브랜드에는 권리 행사 측면에서 대체로 유리하지만, 포트폴리오 관리의 컴플라이언스 기준은 높아집니다. 아래에 조항별 대조표를 정리했습니다. 의사결정 중심의 해설은 <a href="{ACT}">「2027년 1월 1일 전에 외국 브랜드가 해야 할 일」</a>을 참고하십시오.</p>
"""),
                ('side-by-side', '구법·신법 대조표', """
<table>
<thead><tr><th>항목</th><th>2026년 12월 31일까지 (2019년 법)</th><th>2027년 1월 1일부터 (2026년 법)</th></tr></thead>
<tbody>
<tr><td>공고 후 이의신청</td><td>3개월 (제33조)</td><td><strong>2개월 (제36조)</strong></td></tr>
<tr><td>거절 불복 심판</td><td>수령 후 15일 내 청구 (제34조)</td><td>15일. 9개월 내 결정, 3개월 연장 가능 (제37조)</td></tr>
<tr><td>등록 가능 표지</td><td>문자·도형·기호·숫자·입체·색채 조합·소리 (제8조)</td><td>여기에 <strong>동적 표지</strong> 추가 (제14조)</td></tr>
<tr><td>사용 의사 없는 출원</td><td>사용을 목적으로 하지 않는 악의 출원 거절 (제4조)</td><td>사용 의사가 없고 정상적 경영 수요를 명백히 초과하면 거절. 기망·부정 수단 금지 (제19조)</td></tr>
<tr><td>출원인에 대한 제재</td><td>법률상 과태료 없음</td><td>악의 출원으로 불량한 영향을 초래하면 경고 + 최고 <strong>10만 위안</strong> (제54조)</td></tr>
<tr><td>등록상표의 오인 사용</td><td>전용 제재 없음</td><td>위법 매출액 5배 이하 / 25만 위안 이하, 미시정 시 등록 취소 (제56조)</td></tr>
<tr><td>불사용 취소</td><td>3년 연속 미사용 시 누구나 청구 가능 (제49조)</td><td>제3자 청구에 더해 <strong>CNIPA 직권 취소 가능</strong> (제57조)</td></tr>
<tr><td>저명상표</td><td>중국에 등록된 저명상표에 한해 이종 보호 (제13조)</td><td><strong>중국 등록 여부와 무관하게</strong> 이종 보호 (제21조)</td></tr>
<tr><td>인정 vs 확인</td><td>저명상표 "인정"</td><td>"확인"으로 변경. 부정경쟁 사건에서도 확인 가능 (제63조)</td></tr>
<tr><td>네트워크상 사용</td><td>명시 규정 없음</td><td>정보네트워크를 통한 사용 명시 (제2조)</td></tr>
<tr><td>1년 재출원 제한</td><td>취소·무효·미갱신 후 적용 (제50조)</td><td>권리자의 자발적 말소로 한정 (제49조)</td></tr>
<tr><td>상표 대리 기관</td><td>일반적 의무 규정 (제68조)</td><td>등록·담당자 서명·이해상충·제재 정비 (제65~68조)</td></tr>
<tr><td>손해배상</td><td>법정 산정 규칙</td><td>권리 행사에 소요된 합리적 비용 명시 (제77조)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">2026년 법은 조항 번호가 전면 재배열되었습니다. 2019년 법 조항 번호를 인용한 오래된 해설은 오독의 원인이 되므로 어느 판의 조항인지 반드시 확인하십시오.</p>
"""),
                ('six-changes', '외국 브랜드에 가장 중요한 여섯 가지', """
<h3>1. 2개월 이의신청 기간은 대응 체인 전체를 압축합니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제36조는 공고 후 이의신청 기간을 3개월에서 2개월로 줄입니다. 탐지, 사내 승인, 증거 수집, 번역, 현지 대리인 지시가 더 짧은 기간 안에 끝나야 합니다. 등록부를 가끔 확인하는 방식으로는 기한을 놓칩니다. <a href="{L}/china-trademark-monitoring-protection.html">지속적 워칭 프로그램</a>이 선택이 아닌 요건이 됩니다.</p>
<h3>2. CNIPA가 제3자 청구 없이 미사용 상표를 취소할 수 있습니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제57조는 정당한 사유 없이 3년 연속 사용되지 않은 상표의 직권 취소를 추가했습니다. 등록을 사용하지 않는 도용자에게는 효과적인 무기이지만, 정당한 외국 브랜드가 보유한 휴면 방어 등록도 리스크에 노출됩니다. 제2조가 네트워크상 사용을 명시했으므로 날짜가 있는 EC 화면, 소셜 계정, 온라인 광고를 사용 증거에 포함할 수 있습니다.</p>
<h3>3. 악의 출원을 세 겹으로 규제합니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제19조가 투기적 출원을 거절하고, 제54조가 최고 10만 위안의 과태료를 더하며, 제65~68조가 관여한 대리 기관에 의무와 제재를 부과합니다. 또한 제36조는 "기망이나 그 밖의 부정한 수단에 의한 출원"을 공고 단계의 독립된 이의 사유로 편입해, 등록 후 무효심판까지 기다리지 않고 주장할 수 있게 했습니다.</p>
<h3>4. 동적 표지가 등록 가능해집니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제14조는 동적 표지와 그 조합을 등록 가능 표지에 추가합니다. 기존에 저작권이나 부정경쟁법에 의존하던 애니메이션 로고, 앱 로딩 시퀀스, UI 전환을 상표로 보호할 수 있습니다. 심사 지침 초안은 20MB 이하 MP4, 3~9장의 JPEG 정지 화면, 사용 태양에 대한 설명을 요구합니다.</p>
<h3>5. 미등록 저명상표도 이종 보호를 받습니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제21조는 비유사 상품·서비스를 차단하는 전제였던 "중국 내 등록" 요건을 없앴습니다. 제63조는 부정경쟁 절차에서의 저명성 확인도 허용합니다. 중국 내 인지도가 출원보다 앞선 외국 브랜드에 직결되는 변경이지만, 인지도를 입증할 강한 증거는 여전히 필수입니다.</p>
<h3>6. 오인을 유발하는 사용은 권리자 본인의 리스크가 됩니다</h3>
<p class="leading-relaxed text-slate-300 mb-6">제56조는 품질·산지·원료·공정에 대해 공중을 오인시키는 상표 사용을 제재하며 과태료와 등록 취소 대상으로 삼습니다. "Swiss Made", "의료용 등급", "친환경" 등의 표시를 중국용 포장·EC 화면·광고에 사용한다면, 라이선시나 OEM 파트너가 표지를 부착하는 경우까지 포함해 근거를 갖추어야 합니다.</p>
"""),
                ('transition-measures', '경과 조치 초안이 더하는 규칙', """
<table>
<thead><tr><th>초안 조항</th><th>규칙</th><th>실무적 해석</th></tr></thead>
<tbody>
<tr><td>제1~2조</td><td>소급 불적용, 실체는 구법·절차는 신법</td><td>2027년 이전 출원이라도 그날 이후 결정되면 신법. 2027년 이전 등록에 대한 무효·취소는 실체가 구법</td></tr>
<tr><td>제3조</td><td>동적 표지 출원 서류</td><td>20MB 이하 MP4, 3~9장 JPEG, 사용에 의한 식별력 증거는 통지 후 15일 내 제출</td></tr>
<tr><td>제4조</td><td>이의신청 기간은 공고일로 판단</td><td>국내는 상표공보 공고일, 국제등록은 WIPO 공고일. 2027년 이전 3개월, 이후 2개월. 진행 중 기간은 재기산하지 않음</td></tr>
<tr><td>제6~7조</td><td>격리 기간과 직권 취소</td><td>지방 상표 관리 부문이 미사용 상표를 조사해 CNIPA에 단계적으로 보고</td></tr>
<tr><td>제9~10조</td><td>구 시행조례보다 신법 우선, 조치는 2027년 1월 1일 시행</td><td>경과기에 현행 시행조례가 개정법보다 우선한다고 전제할 수 없음</td></tr>
</tbody>
</table>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>초안 상태에 유의하십시오.</strong> 본 조치는 2026년 9월 28일 의견 수렴이 시작되어 2026년 11월 12일 마감되며, 심사심리 지침 초안도 함께 공개되었습니다. 계류 사건에서 경과 규칙에 근거하기 전에 최종안을 반드시 확인하십시오.</p></div>
"""),
                ('your-action-list', '대응 체크리스트', """
<ul>
<li>2027년 1월 1일 전까지: <a href="{ACT}">5단계 사전 감사</a>를 실행하고 워칭을 2개월 체계로 재설정하십시오.</li>
<li>출원 자격·필요 서류·현지 대리인 요건은 <a href="{L}/who-can-register-trademark-in-china.html">「중국에서 상표를 등록할 수 있는 사람」</a>에서 확인하십시오.</li>
<li>현행 절차와 기간은 <a href="{L}/china-trademark-registration-complete-guide-2026.html">완전 가이드</a>와 <a href="{L}/how-long-trademark-registration-china.html">소요 기간 가이드</a>에서 확인하십시오.</li>
<li>제19조로 거절 사유가 추가된 점을 반영해 <a href="{L}/common-reasons-trademark-rejection-china.html">주요 거절 사유</a>의 전제를 갱신하십시오.</li>
<li>도용자가 이미 등록을 마쳤다면 <a href="{L}/trademark-registered-by-someone-else-china.html">이의·무효·협상·리브랜딩 비교</a>를 참고하십시오.</li>
</ul>
"""),
                ('sources-and-caveats', '출처·상태·유의사항', """
<ul>
<li>전문: 『중화인민공화국 상표법(2026년 개정)』, CNIPA, 2026년 6월 26일.</li>
<li>공식 해설: CNIPA 『중화인민공화국 상표법 개정 주요 내용』, 2026년 7월 10일.</li>
<li>경과: CNIPA 『개정 후 상표법 시행에 따른 업무 처리 방안(의견수렴고)』 및 『상표 심사심리 지침(의견수렴고)』 공고, 2026년 9월 28일.</li>
<li>시행일과 장 구성은 전국인대 및 최고인민법원의 2026년 7~8월 공개 자료에서도 확인했습니다.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">조항 번호는 별도 표기가 없으면 2026년 법 기준입니다. 이 페이지는 일반 정보이며 법률 자문이 아닙니다. 최종 확인일: 2026년 11월 6일.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>자사 포트폴리오 기준으로 검토하시겠습니까?</strong> <a href="/contact.html">중국 상표 팀에 무료로 문의하세요</a>.</p></div>
"""),
            ],
        },
    },
}
