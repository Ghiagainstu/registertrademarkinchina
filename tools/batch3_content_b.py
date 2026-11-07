# -*- coding: utf-8 -*-
"""Batch 3 content (part B): country guides (JP/KR/US/EU) + a Korean case study.

EN/JA/KO. Placeholders: {L} -> /blog | /blog/ja | /blog/ko ;
{HUB} / {ACT} -> the two batch-1 URLs in the current language.
UI strings (breadcrumb, CTA, date labels) are inherited from p0_2027_content.
"""

CONTENT = {
 'en': {'articles': {

    # ------------------------------------------------------------------ jp
    'jp': {
        'slug': 'japanese-companies-china-trademark-registration',
        'title': 'Japanese Companies Registering Trademarks in China: A Country Guide',
        'desc': 'A practical country guide for Japanese companies filing trademarks in China: the mandatory local agent, the six-month Paris priority, Madrid versus direct filing, Chinese-character marks, document legalisation and the 2027 law changes.',
        'lede': 'Japan and China share a writing system, but not a trademark register. A Japanese brand familiar at home can arrive in China to find its Chinese name already filed by someone else. The rules below apply to every foreign applicant, Japanese ones included.',
        'card_text': 'Kanji is not simplified Chinese, a branch office is not a place of business, and the six-month priority clock starts at the first filing abroad. What Japanese owners should file before shipping.',
        'category': 'By Country',
        'read_time': '9 min read',
        'tags': ['Japanese companies', 'China trademark', 'country guide'],
        'related': [
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/muji-trademark-war-china.html', 'The MUJI Trademark Dispute in China'),
        ],
        'sections': [
            ('the-local-agent-rule', 'The Local-Agent Rule Comes First', """
<p class="leading-relaxed text-slate-300 mb-6">A foreign applicant with no habitual residence or place of business in China must file through a trademark agency lawfully established or registered in China. Article 11 of the 2026 Trademark Law continues this rule. Build the agency relationship into the plan first, because every later step runs through it.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two points are often missed. A branch office in China is not, by itself, a place of business that lifts the requirement, so the exemption does not apply. And there is no special treatment for Japanese applicants: the same rule binds every foreign entity, however long it has exported to China or however well known the brand is. Put a standing power of attorney on file, keep the applicant name and address consistent, and treat the agent as part of the team rather than a courier.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">Baseline eligibility is covered in <a href="{L}/who-can-register-trademark-in-china.html">Who Can Register a Trademark in China</a> and the <a href="{L}/china-first-to-file-trademark-guide.html">first-to-file guide</a>.</p></div>
"""),
            ('kanji-is-not-chinese', 'Kanji Is Not Simplified Chinese', """
<p class="leading-relaxed text-slate-300 mb-6">Japanese kanji and simplified Chinese characters are not the same sign, and a Latin mark and a Chinese-character mark are separate rights in China. Registering the brand in romaji does not protect the Chinese name that shoppers actually use.</p>
<p class="leading-relaxed text-slate-300 mb-6">File the official Chinese name, the common transliterations and any nickname consumers have coined. Similarity is assessed by sound, form and meaning, so a lookalike Chinese-character filing can conflict even where the Latin marks differ. Katakana and romaji brands are routinely re-transcribed by Chinese consumers; clear those Chinese forms before launch rather than after a squatter files them.</p>
<ul>
<li><strong>Latin or romaji word mark</strong> &mdash; the spelling on your packaging, not the name on the shelf.</li>
<li><strong>Official Chinese-character name</strong> &mdash; a separate right a third party can register independently.</li>
<li><strong>Transliterations and phonetic variants</strong> &mdash; tested by sound as well as form and meaning.</li>
<li><strong>Consumer nicknames and abbreviations</strong> &mdash; often the form that actually circulates.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">Japanese anime, restaurant and retail brands have documented squatting disputes in China; see the <a href="{L}/muji-trademark-war-china.html">MUJI case</a>, the <a href="{L}/japanese-anime-ip-trademark-china.html">anime IP disputes</a> and the <a href="{L}/japanese-ramen-chain-china-trademark.html">ramen chain case</a>. A Chinese-character clearance search belongs at the start of market entry.</p>
"""),
            ('priority-and-two-routes', 'The Six-Month Priority Window and the Two Filing Routes', """
<p class="leading-relaxed text-slate-300 mb-6">Under the Paris Convention, a mark first filed abroad may be filed in China within <strong>six months</strong> for the same mark and the same goods or services with a priority claim. The claim must be made in writing at filing and a copy of the first application submitted within <strong>three months</strong> (Article 29 of the 2026 law, corresponding to old Article 25). First use at an international exhibition also carries a six-month priority right.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two routes exist. A Madrid System registration designating China is examined by CNIPA under Chinese law and its goods description must fit China's similar-group and sub-class practice; a national application goes directly to CNIPA. An international registration depends on the home basic registration for its <strong>first five years</strong>, which is the central-attack risk. WIPO provisional refusals for China carry a response window of <strong>15 days</strong> for ex officio refusals and <strong>30 days</strong> for opposition-based refusals from receipt of the notification, with supplementary evidence within <strong>three months</strong> (WIPO official Time Limits table). Pre-brief your Chinese agent for those windows.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">Export and OEM manufacturing create no Chinese trademark rights. File before goods ship or are listed. Compare <a href="{L}/madrid-vs-direct-filing-china.html">Madrid versus direct filing</a> and plan with the <a href="{L}/china-trademark-classes-complete-guide.html">class guide</a>.</p></div>
"""),
            ('documents-language-and-legalisation', 'Documents, Language and Legalisation', """
<p class="leading-relaxed text-slate-300 mb-6">Applications are filed in Chinese. Foreign-language entity certificates need a Chinese translation, and the applicant name and address must correspond in English and Chinese. Fix the official Chinese rendering once and use it everywhere; a mismatch with the corporate extract is an avoidable objection.</p>
<p class="leading-relaxed text-slate-300 mb-6">A power of attorney is generally valid with a signature or seal, so do not assume notarisation or legalisation is always required. Where public documents do need authentication, the Hague Apostille Convention took effect for China on <strong>7 November 2023</strong>: documents from contracting states use an Apostille instead of the traditional foreign-ministry-plus-embassy double legalisation, while non-contracting states still use consular legalisation. Whether it applies depends on the document type and what the receiving office currently accepts, so confirm current practice with the agent rather than relying on a generic checklist.</p>
"""),
            ('the-2027-law', 'What the 2027 Law Changes for Japanese Owners', """
<p class="leading-relaxed text-slate-300 mb-6">The 2026 Trademark Law takes effect on <strong>1 January 2027</strong>. Article 36 shortens the opposition period from three months to <strong>two months</strong> from preliminary publication, turning register watching into a weekly operational task. Article 19 regulates bad-faith applications. Article 57 lets CNIPA cancel a mark unused for <strong>three consecutive years</strong> on its own initiative, so dated use evidence must be archived from day one.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 21 extends cross-class protection to unregistered well-known marks, relevant to Japanese brands famous in China before they filed. Article 55 addresses licence recordal and statutory termination rights, and Article 46 introduces substantive examination of assignments. Together these favour a portfolio that is actively used, monitored and documented rather than one that simply sits on the register. See the <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">two-month watch SOP</a> and the <a href="{L}/china-trademark-non-use-cancellation-evidence.html">use-evidence guide</a>.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">For the wider action list, see <a href="{ACT}">What Foreign Brands Should Do Before 2027</a>.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Sources: <em>Trademark Law of the PRC (2026 Revision)</em>, Articles 11, 19, 21, 29, 36, 46, 55 and 57; the Paris Convention; the Hague Apostille Convention (in force for China from 7 November 2023); WIPO's official Time Limits table for provisional refusals; CNIPA practice on Chinese-language filings. Procedures may be refined by implementing rules, so confirm current official requirements. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Filing from Japan?</strong> <a href="/contact.html">Talk to our team</a> about a China-based agency, a Chinese-name search and a priority-aligned filing plan.</p></div>
"""),
        ],
    },

    # ------------------------------------------------------------------ kr
    'kr': {
        'slug': 'korean-companies-china-trademark-registration',
        'title': 'Korean Companies Registering Trademarks in China: A Country Guide',
        'desc': 'A country guide for Korean companies filing trademarks in China: the mandatory local agent, K-beauty class planning, Korean names and Chinese transliterations, the six-month priority, Madrid versus direct filing and the 2027 law changes.',
        'lede': 'K-beauty travels fast, and so do the people who file its names first. In China a Korean registration has no force of its own, and a Hangul name is not the sign Chinese consumers use. This guide sets out the filing rules from a Korean owner\'s point of view.',
        'card_text': 'Plan the Chinese name as a separate right, treat Class 3, 35 and 44 as portfolio planning rather than a legal requirement, and claim the six-month priority before a distributor files first.',
        'category': 'By Country',
        'read_time': '9 min read',
        'tags': ['Korean companies', 'K-beauty', 'country guide'],
        'related': [
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/korean-brands-trademark-squatting-china-cases.html', 'Korean Brand Trademark Disputes in China'),
        ],
        'sections': [
            ('the-local-agent-rule', 'The Local-Agent Rule Applies Equally', """
<p class="leading-relaxed text-slate-300 mb-6">A foreign applicant with no habitual residence or place of business in China must appoint a trademark agency lawfully established or registered in China. Article 11 of the 2026 Trademark Law continues the rule. For Korean companies, even those with heavy China sales, this is the starting constraint: the application is made by the local agent, not by head office.</p>
<p class="leading-relaxed text-slate-300 mb-6">A branch office in China does not by itself count as a place of business for this purpose, so the exemption does not apply. There is no special treatment for Korean applicants either, whatever cooperation exists between the Korean and Chinese IP authorities. MOIP, formerly KIPO, and CNIPA maintain contact on IP matters, but cooperation does not transfer a right or waive a filing requirement. Keep a standing power of attorney with your agent and keep the applicant name and address consistent across documents. More on the baseline in <a href="{L}/who-can-register-trademark-in-china.html">Who Can Register a Trademark in China</a>.</p>
"""),
            ('classes-and-chinese-names', 'Class Planning and the Chinese Name', """
<p class="leading-relaxed text-slate-300 mb-6">A Korean brand name in Hangul is not the sign Chinese consumers use. An English word mark and a Chinese-character mark are separate rights in China. Register the official Chinese name, common transliterations and consumer-coined nicknames; similarity is judged by sound, form and meaning, so a phonetic lookalike can conflict even where the Latin marks differ.</p>
<table>
<thead><tr><th>Common K-beauty planning</th><th>How to treat it</th></tr></thead>
<tbody>
<tr><td>Class 3, cosmetics</td><td>A common practical choice for the goods themselves</td></tr>
<tr><td>Class 35, retail</td><td>Often considered for store and online retail services</td></tr>
<tr><td>Class 44, beauty services</td><td>Often considered where salons or clinics are part of the model</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">This is portfolio planning, not a statutory requirement: the classes you need depend on the goods and services you actually offer, and the goods description must fit CNIPA's similar-group and sub-class practice. Plan with the <a href="{L}/china-trademark-classes-complete-guide.html">class guide</a> and clear the Chinese character forms before launch.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">See <a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">why an overseas registration has no effect in China</a> and the <a href="{L}/china-first-to-file-trademark-guide.html">first-to-file guide</a>.</p></div>
"""),
            ('priority-and-two-routes', 'The Six-Month Priority Window and the Two Filing Routes', """
<p class="leading-relaxed text-slate-300 mb-6">Under the Paris Convention, a mark first filed abroad may be filed in China within <strong>six months</strong> for the same mark and the same goods or services with a priority claim. The claim must be made in writing at the time of filing and a copy of the first application submitted within <strong>three months</strong> (Article 29 of the 2026 law, corresponding to old Article 25). First use at an international exhibition also gives a six-month priority right, a window easy to miss during distribution negotiations.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two routes are available: a Madrid System registration designating China, examined by CNIPA under Chinese law with the goods description adapted to local sub-classes, or a direct national application. An international registration depends on the home basic registration for its <strong>first five years</strong>, the central-attack risk. For WIPO provisional refusals designating China, the response window is <strong>15 days</strong> for ex officio refusals and <strong>30 days</strong> for opposition-based refusals from receipt of the WIPO notification, with supplementary evidence within <strong>three months</strong> (WIPO official Time Limits table). Compare <a href="{L}/madrid-vs-direct-filing-china.html">Madrid versus direct filing</a>.</p>
"""),
            ('documents-language-and-legalisation', 'Documents, Language and Legalisation', """
<p class="leading-relaxed text-slate-300 mb-6">Applications are filed in Chinese. Foreign-language entity certificates need a Chinese translation, and the applicant name and address must correspond in English and Chinese. Fix the official Chinese rendering once and reuse it; a mismatch with the corporate extract is a common avoidable objection.</p>
<p class="leading-relaxed text-slate-300 mb-6">A power of attorney is generally valid with a signature or seal, so do not assume notarisation or legalisation is always required. Where public documents do need authentication, the Hague Apostille Convention took effect for China on <strong>7 November 2023</strong>: documents from contracting states use an Apostille instead of the traditional foreign-ministry-plus-embassy double legalisation, while non-contracting states still use consular legalisation. Applicability depends on the document type and what the receiving office currently accepts. Confirm current practice with the agent; never assume a fee or fixed timeline not in the official rules.</p>
"""),
            ('squatting-and-the-2027-law', 'Squatting, Monitoring and the 2027 Law', """
<p class="leading-relaxed text-slate-300 mb-6">Korean brands have faced lookalike stores and pre-emptive filings in China; the <a href="{L}/korean-brands-trademark-squatting-china-cases.html">dispute case study</a> collects reported examples. The controls are the same ones the 2027 law rewards. Effective <strong>1 January 2027</strong>, Article 36 shortens the opposition period from three months to <strong>two months</strong>, which makes weekly watching necessary. Article 19 regulates bad-faith applications, and Article 57 lets CNIPA cancel a mark unused for <strong>three consecutive years</strong> on its own initiative, so archive dated use evidence.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 21 extends cross-class protection to unregistered well-known marks, Article 55 addresses licence recordal and statutory termination rights, and Article 46 introduces substantive examination of assignments. Platform and customs enforcement presuppose a Chinese registration certificate, so the filing is the gatekeeper. No official fees, success rates or special treatment for Korean applicants should be assumed; confirm the current official rules. Build the routine with the <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a> and the <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">two-month watch SOP</a>.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">A distributor or OEM partner filing first is a recurring pattern. File before commercial discussions create a public trail, and keep the relationship documented.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Sources: <em>Trademark Law of the PRC (2026 Revision)</em>, Articles 11, 19, 21, 29, 36, 46, 55 and 57; the Paris Convention; the Hague Apostille Convention (in force for China from 7 November 2023); WIPO's official Time Limits table for provisional refusals; CNIPA practice on Chinese-language filings and class sub-groups. Class selections described above are common practice, not legal requirements. Procedures may be refined by implementing rules, so confirm current official requirements. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Entering China from Korea?</strong> <a href="/contact.html">Talk to our team</a> about a Chinese-name search, class planning and a priority-aligned filing.</p></div>
"""),
        ],
    },

    # ------------------------------------------------------------------ us
    'us': {
        'slug': 'us-companies-china-trademark-registration',
        'title': 'US Companies Registering Trademarks in China: A Country Guide',
        'desc': 'A country guide for US companies filing trademarks in China: why a US registration has no effect there, the six-month Paris priority, the 15 and 30 day Madrid response windows, Apostille documents for a Hague contracting state and the 2027 law changes.',
        'lede': 'A US registration is a US right. In China it carries no weight, and the mark on your goods is not necessarily the one Chinese consumers use. This guide covers the filing rules from the point of view of a US owner, including the short response windows that catch teams out.',
        'card_text': 'A USPTO registration does not extend to China, the six-month priority needs a written claim and a copy within three months, and Madrid refusals for China can leave only 15 or 30 days to answer.',
        'category': 'By Country',
        'read_time': '9 min read',
        'tags': ['US companies', 'Apostille', 'country guide'],
        'related': [
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/madrid-vs-direct-filing-china.html', 'Madrid vs Direct Filing in China'),
        ],
        'sections': [
            ('the-local-agent-rule', 'The Local-Agent Rule Comes First', """
<p class="leading-relaxed text-slate-300 mb-6">A foreign applicant with no habitual residence or place of business in China must file through a trademark agency lawfully established or registered in China. Article 11 of the 2026 Trademark Law continues the rule. Even a large US company with a China sales team files through the local agent, so appoint one before any deadline is in play.</p>
<p class="leading-relaxed text-slate-300 mb-6">A branch office in China does not by itself count as a place of business for this purpose, so the exemption does not apply, and there is no special treatment for US applicants. Keep a standing power of attorney on file and keep the applicant name and address consistent. See <a href="{L}/who-can-register-trademark-in-china.html">Who Can Register a Trademark in China</a> for the baseline.</p>
"""),
            ('us-registration-does-not-extend', 'A US Registration Has No Effect in China', """
<p class="leading-relaxed text-slate-300 mb-6">China is a first-to-file jurisdiction and a US registration confers no rights there. An English or Latin word mark and a Chinese-character mark are separate rights. Register the official Chinese name, the common transliterations and the nicknames consumers coin themselves; similarity is judged by sound, form and meaning, so a lookalike Chinese-character mark can conflict even where the Latin marks differ. A US owner that filed only the English mark often discovers the Chinese name belongs to someone else.</p>
<p class="leading-relaxed text-slate-300 mb-6">Decide the official Chinese rendering once, use it on packaging and in filings, and clear the alternatives before launch. This is why a Chinese-character clearance search belongs at the start of market entry rather than after a product is listed. Compare <a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">an overseas R mark versus a China registration</a> and <a href="{L}/logo-vs-word-mark-china.html">logo versus word mark</a>.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">See also the <a href="{L}/china-first-to-file-trademark-guide.html">first-to-file guide</a> and the <a href="{L}/coca-cola-chinese-name-trademark-china.html">Chinese-name case studies</a>.</p></div>
"""),
            ('priority-and-the-15-30-day-windows', 'Priority and the 15/30-Day Madrid Response Windows', """
<p class="leading-relaxed text-slate-300 mb-6">Under the Paris Convention, a mark first filed abroad may be filed in China within <strong>six months</strong> for the same mark and the same goods or services with a priority claim. The claim must be made in writing at filing and a copy of the first application submitted within <strong>three months</strong> (Article 29 of the 2026 law, corresponding to old Article 25). First use at an international exhibition also carries a six-month priority right.</p>
<table>
<thead><tr><th>Item</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>Madrid designation of China</td><td>Examined by CNIPA under Chinese law; goods description adapted to local similar groups and sub-classes</td></tr>
<tr><td>Dependency on the basic registration</td><td>First five years, the central-attack risk</td></tr>
<tr><td>Ex officio provisional refusal</td><td>15 days to respond from receipt of the WIPO notification</td></tr>
<tr><td>Opposition-based provisional refusal</td><td>30 days to respond from receipt of the WIPO notification</td></tr>
<tr><td>Supplementary evidence</td><td>Within three months (WIPO official Time Limits table)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Those windows are short enough that a US legal team cannot gather instructions after the notice arrives. Pre-authorise the Chinese agent and compare <a href="{L}/madrid-vs-direct-filing-china.html">Madrid versus direct filing</a> before choosing a route.</p>
"""),
            ('apostille-and-documents', 'Apostille, Language and Filing Documents', """
<p class="leading-relaxed text-slate-300 mb-6">Applications are filed in Chinese. Foreign-language entity certificates need a Chinese translation, and the applicant name and address must correspond in English and Chinese. A power of attorney is generally valid with a signature or seal, so do not assume notarisation or legalisation is always required.</p>
<p class="leading-relaxed text-slate-300 mb-6">Where public documents do need authentication, the United States is a party to the Hague Apostille Convention, which took effect for China on <strong>7 November 2023</strong>. Documents from contracting states use an Apostille instead of the traditional foreign-ministry-plus-embassy double legalisation; non-contracting states still use consular legalisation. Whether the Apostille route applies depends on the document type and what the receiving office currently accepts, so confirm current practice with the agent. Do not assume a fixed fee or processing timeline that is not stated in the official rules.</p>
"""),
            ('the-2027-law-and-defensive-portfolios', 'The 2027 Law and Defensive Portfolios', """
<p class="leading-relaxed text-slate-300 mb-6">The 2026 Trademark Law takes effect on <strong>1 January 2027</strong>. Article 19 regulates bad-faith applications, including those filed with no intent to use and clearly beyond normal business needs. US owners that built large defensive combinations of marks they never planned to trade under should review those holdings: a purely speculative filing is exactly the pattern the provision targets, and Article 57 separately lets CNIPA cancel a mark unused for <strong>three consecutive years</strong> on its own initiative.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 36 shortens the opposition period from three months to <strong>two months</strong>, Article 21 extends cross-class protection to unregistered well-known marks, Article 55 addresses licence recordal and statutory termination rights, and Article 46 introduces substantive examination of assignments. The direction is clear: a defensible portfolio is one that is used, watched and documented. See the <a href="{L}/china-trademark-non-use-cancellation-evidence.html">use-evidence guide</a> and the <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">two-month watch SOP</a>.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">Do not assume any special treatment for US applicants, or any official fee, success rate or timeline not stated in the current official rules. Confirm the details with your agent.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Sources: <em>Trademark Law of the PRC (2026 Revision)</em>, Articles 11, 19, 21, 29, 36, 46, 55 and 57; the Paris Convention; the Hague Apostille Convention (in force for China from 7 November 2023); WIPO's official Time Limits table for provisional refusals; CNIPA practice on Chinese-language filings. Procedures may be refined by implementing rules, so confirm current official requirements. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Filing from the United States?</strong> <a href="/contact.html">Talk to our team</a> about Apostille documents, a Chinese-name search and a priority-aligned filing plan.</p></div>
"""),
        ],
    },

    # ------------------------------------------------------------------ eu
    'eu': {
        'slug': 'eu-companies-china-trademark-registration',
        'title': 'EU Companies Registering Trademarks in China: A Country Guide',
        'desc': 'A country guide for EU companies filing trademarks in China: why an EUTM does not extend there, the six-month Paris priority, Madrid versus direct filing, Apostille documents for Hague contracting states, Article 21 well-known mark protection and the 2027 law changes.',
        'lede': 'A European Union trade mark is a single right across the EU, and it stops at the EU border. China needs its own filing. This guide covers the rules from a European owner\'s perspective, including the well-known mark protection that matters for brands with an existing China reputation.',
        'card_text': 'An EUTM has no effect in China, the six-month priority needs a written claim and a copy within three months, and Article 21 gives unregistered well-known marks cross-class protection from 2027.',
        'category': 'By Country',
        'read_time': '9 min read',
        'tags': ['EU companies', 'EUTM', 'country guide'],
        'related': [
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/madrid-vs-direct-filing-china.html', 'Madrid vs Direct Filing in China'),
            ('{L}/hermes-trademark-china-case.html', 'The Hermes Trademark Case in China'),
        ],
        'sections': [
            ('the-local-agent-rule', 'The Local-Agent Rule Comes First', """
<p class="leading-relaxed text-slate-300 mb-6">A foreign applicant with no habitual residence or place of business in China must file through a trademark agency lawfully established or registered in China. Article 11 of the 2026 Trademark Law continues the rule. A European company therefore files through the local agent even where its EU portfolio is managed from a single in-house team.</p>
<p class="leading-relaxed text-slate-300 mb-6">A branch office in China does not by itself count as a place of business for this purpose, so the exemption does not apply, and there is no special treatment for EU applicants. Keep a standing power of attorney on file and keep the applicant name and address consistent. See <a href="{L}/who-can-register-trademark-in-china.html">Who Can Register a Trademark in China</a>.</p>
"""),
            ('eutm-does-not-extend', 'An EUTM Does Not Extend to China', """
<p class="leading-relaxed text-slate-300 mb-6">An EU trade mark does not extend to China, so a separate Chinese filing is required. Nor does it extend to Hong Kong, China; Macao, China; or Taiwan, China, each of which has its own register. China is a first-to-file jurisdiction: reputation built through exports or press coverage is not a right on its own.</p>
<p class="leading-relaxed text-slate-300 mb-6">An English or Latin word mark and a Chinese-character mark are separate rights. Register the official Chinese name, the common transliterations and consumer-coined nicknames; similarity is judged by sound, form and meaning. European luxury and consumer brands have well-documented Chinese disputes, for example the <a href="{L}/hermes-trademark-china-case.html">Hermes case</a>, so clear the Chinese-character forms before launch. See also <a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">why an overseas R mark has no effect in China</a>.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">Compare the <a href="{L}/china-first-to-file-trademark-guide.html">first-to-file guide</a> and the <a href="{L}/coca-cola-chinese-name-trademark-china.html">Chinese-name case studies</a>.</p></div>
"""),
            ('priority-madrid-and-direct', 'Priority, Madrid and Direct Filing', """
<p class="leading-relaxed text-slate-300 mb-6">Under the Paris Convention, a mark first filed abroad may be filed in China within <strong>six months</strong> for the same mark and the same goods or services with a priority claim. The claim must be made in writing at filing and a copy of the first application submitted within <strong>three months</strong> (Article 29 of the 2026 law, corresponding to old Article 25). First use at an international exhibition also carries a six-month priority right.</p>
<ul>
<li><strong>Two routes:</strong> a Madrid System registration designating China is examined by CNIPA under Chinese law, with the goods description adapted to local similar groups and sub-classes; a direct national application goes straight to CNIPA.</li>
<li><strong>Five-year dependency:</strong> an international registration depends on the home basic registration for its first five years, the central-attack risk.</li>
<li><strong>Short response windows:</strong> WIPO provisional refusals for China give <strong>15 days</strong> for ex officio refusals and <strong>30 days</strong> for opposition-based refusals from receipt of the notification, with supplementary evidence within <strong>three months</strong> (WIPO official Time Limits table).</li>
<li><strong>Preparation:</strong> pre-authorise the Chinese agent so a response can go out inside those windows.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">Compare <a href="{L}/madrid-vs-direct-filing-china.html">Madrid versus direct filing</a> before committing to a route.</p>
"""),
            ('apostille-and-documents', 'Apostille, Language and Filing Documents', """
<p class="leading-relaxed text-slate-300 mb-6">Applications are filed in Chinese. Foreign-language entity certificates need a Chinese translation, and the applicant name and address must correspond in the European language and in Chinese. Fix the official Chinese rendering once and reuse it. A power of attorney is generally valid with a signature or seal, so do not assume notarisation or legalisation is always required.</p>
<p class="leading-relaxed text-slate-300 mb-6">Where public documents do need authentication, EU member states are parties to the Hague Apostille Convention, which took effect for China on <strong>7 November 2023</strong>. Documents from contracting states use an Apostille instead of the traditional foreign-ministry-plus-embassy double legalisation; non-contracting states still use consular legalisation. Whether the Apostille route applies depends on the document type and what the receiving office currently accepts. Confirm current practice with the agent, and do not assume a fixed fee or timeline that is not stated in the official rules.</p>
"""),
            ('article-21-and-the-2027-law', 'Article 21, the 2027 Law and the Practical Steps', """
<p class="leading-relaxed text-slate-300 mb-6">The 2026 Trademark Law takes effect on <strong>1 January 2027</strong>. Article 21 extends cross-class protection to unregistered well-known marks. For European brands with an established reputation in China but an incomplete filing history, that is a meaningful additional route, but it is a protection of last resort, not a substitute for registration: proving the reputation takes a dated evidence file, and the outcome is never as certain as an owned registration. We do not speculate here on specific absolute-grounds provisions; confirm the current statute and practice with your agent.</p>
<p class="leading-relaxed text-slate-300 mb-6">The other changes point the same way. Article 36 shortens the opposition period from three months to <strong>two months</strong>, Article 19 regulates bad-faith applications, Article 57 lets CNIPA cancel a mark unused for <strong>three consecutive years</strong> on its own initiative, Article 55 addresses licence recordal and statutory termination rights, and Article 46 introduces substantive examination of assignments. File early, register the Chinese name, watch weekly and archive use evidence. See the <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a> and the <a href="{ACT}">pre-2027 action list</a>.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">No special treatment applies to EU applicants, and no official fees, success rates or timelines beyond those stated should be assumed. Confirm the current official rules.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Sources: <em>Trademark Law of the PRC (2026 Revision)</em>, Articles 11, 19, 21, 29, 36, 46, 55 and 57; the Paris Convention; the Hague Apostille Convention (in force for China from 7 November 2023); WIPO's official Time Limits table for provisional refusals; CNIPA practice on Chinese-language filings. Procedures may be refined by implementing rules, so confirm current official requirements. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Filing from Europe?</strong> <a href="/contact.html">Talk to our team</a> about an EUTM-to-China filing plan, a Chinese-name search and Apostille documents.</p></div>
"""),
        ],
    },

    # ------------------------------------------------------------------ kcase
    'kcase': {
        'slug': 'korean-brands-trademark-squatting-china-cases',
        'title': 'K-Beauty Under Pressure: Korean Brand Trademark Disputes in China',
        'desc': 'A case study of Korean brand trademark disputes in China: the 2026 MOIP-CNIPA cooperation MOU, reported lookalike stores, the AKF exclusive-licence dispute, and the filing, monitoring and evidence controls that address all three.',
        'lede': 'Three recent Korean brand disputes in China illustrate the same lesson. A policy memorandum, a lookalike store and an exclusive-licence fight all point back to one thing: in a first-to-file system, reputation is not a right. The right comes from an early, well-documented Chinese registration.',
        'card_text': 'What the 2026 IP cooperation MOU actually does, what the reported copycat store and the AKF licence dispute show, and the preventive checklist that turns those lessons into a filing plan.',
        'category': 'Case Study',
        'read_time': '9 min read',
        'tags': ['K-beauty', 'trademark squatting', 'case study'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', 'Trademark Monitoring and Protection'),
            ('{L}/china-first-to-file-trademark-guide.html', 'China First-to-File Guide'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
        ],
        'sections': [
            ('the-mou', 'A Bilateral MOU Puts Bad-Faith Filings on the Agenda', """
<p class="leading-relaxed text-slate-300 mb-6">On <strong>5 January 2026</strong>, during a Korea-China summit, the Korean Ministry of Intellectual Property (MOIP, formerly KIPO) and CNIPA signed an intellectual property cooperation memorandum, expanding and supplementing an earlier bilateral arrangement. According to the MOIP's official English announcement and Korean media reporting including the Korea Herald and AJU Press, the cooperation covers anti-counterfeiting, the use of AI and big data in examination, and IP transactions and commercialisation. The two sides specifically agreed to jointly address bad-faith trademark squatting.</p>
<p class="leading-relaxed text-slate-300 mb-6">Be precise about what this does and does not do. A memorandum sets a framework for cooperation; it does not change Chinese filing law, extend Korean registrations into China, or create a shortcut to a Chinese right. Protection still comes from a CNIPA registration, so treat the announcement as a signal of high-level attention, not a substitute for filing.</p>
"""),
            ('lookalike-stores', 'Lookalike Stores and Consumer Confusion', """
<p class="leading-relaxed text-slate-300 mb-6">According to Korean media reports, in early 2026 a cosmetics store trading under the name Only Young appeared in Changsha, Hunan Province, China, and was alleged to imitate the name, logo, colour scheme and display layout of Korea's Olive Young. Seo Kyoung-duk, a professor at Sungshin Women's University, commented publicly, and promotional clips circulated on short-video platforms. Related disputes have involved Chinese lifestyle brands using KOREA or KR signage at overseas stores, said to cause confusion about origin.</p>
<p class="leading-relaxed text-slate-300 mb-6">These are reported allegations, not adjudicated findings; treat them as illustrations of a risk pattern. A store name, a logo, a colour scheme and a layout are different things: a word-mark filing may not cover the device or the trade dress, and Chinese-character signage is a separate right. A brand that registered only its English mark can find its visual identity copied without a clean word-mark conflict.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">Register the Chinese-character name, the device mark and the common transliterations alongside the Latin mark, and keep dated evidence of how the brand is presented. See <a href="{L}/logo-vs-word-mark-china.html">logo versus word mark</a>.</p></div>
"""),
            ('the-akf-licence-dispute', 'The AKF Exclusive-Licence Dispute', """
<p class="leading-relaxed text-slate-300 mb-6">According to public reporting, a final judgment upheld the validity of the core AKF trademark exclusive-licence contract; the brand was reported to have approached annual sales of close to RMB 2.5 billion at its peak. Because this comes from Chinese financial and industry media rather than an official judgment text, we do not state the court, any compensation figure or the exact date as established facts, and draw no conclusions beyond the reported outcome.</p>
<p class="leading-relaxed text-slate-300 mb-6">The practical lesson is documentation. An exclusive licence is only as strong as the chain of title behind it and the way it is recorded. Where a China business rests on a licence from a foreign brand owner, the underlying registration, the licence agreement and any recordal should be consistent and current. Article 55 addresses licence recordal and statutory termination rights, and Article 46 introduces substantive examination of assignments. See <a href="{L}/china-trademark-assignment-licence-recordal.html">assignment and licence recordal</a>.</p>
"""),
            ('what-these-cases-share', 'What These Cases Have in Common', """
<p class="leading-relaxed text-slate-300 mb-6">Three fact patterns share the same controls. A cooperation MOU addresses bad-faith filings at policy level; a lookalike store tests whether the visual and Chinese-language identity was registered; a licence dispute tests whether the rights chain is documented. None is solved by reputation alone.</p>
<table>
<thead><tr><th>Dispute type</th><th>What it exposes</th><th>Control that would have helped</th></tr></thead>
<tbody>
<tr><td>Bad-faith pre-emptive filings</td><td>China is a first-to-file system; reputation without a filing is fragile</td><td>Early CNIPA registration plus a weekly watch</td></tr>
<tr><td>Copycat store identity</td><td>Word marks, device marks and Chinese-character names are separate rights</td><td>Register the full sign family and keep dated presentation evidence</td></tr>
<tr><td>Exclusive-licence conflict</td><td>A licence needs a clean, recorded chain of title</td><td>Consistent registration, licence and recordal documents</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The conclusion is operational: file early with CNIPA, register the Chinese name, monitor continuously and archive use evidence. Platform requirements and customs recordal presuppose a Chinese registration certificate, so filing is the gatekeeper for enforcement. Compare <a href="{L}/amazon-tmall-trademark-requirement-china.html">platform trademark requirements</a> and <a href="{L}/china-trademark-enforcement-routes-after-registration.html">post-registration enforcement routes</a>.</p>
"""),
            ('a-preventive-checklist', 'A Preventive Checklist for Korean Brands', """
<ol>
<li><strong>File the sign family:</strong> the Latin mark, official Chinese name, common transliterations, consumer nicknames and device mark are separate rights.</li>
<li><strong>Plan classes by actual goods and services.</strong> For K-beauty, Class 3 (cosmetics), Class 35 (retail) and Class 44 (beauty services) are a common practical choice, not a statutory requirement.</li>
<li><strong>Use priority:</strong> claim Paris Convention priority within six months of the first foreign filing, in writing, with a copy within three months; exhibition first use also gives six months.</li>
<li><strong>Appoint a China-based agency;</strong> a branch office does not remove the requirement.</li>
<li><strong>Watch weekly;</strong> from 1 January 2027 the opposition window is two months.</li>
<li><strong>Archive use evidence;</strong> Article 57 lets CNIPA cancel a three-year-unused mark on its own initiative.</li>
<li><strong>Keep documents current:</strong> translations, name and address correspondence, powers of attorney, licence and assignment recordals.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">No special treatment or unstated fees, success rates or timelines should be assumed; confirm the current official rules with your agent. See the <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a> and the <a href="{ACT}">pre-2027 action list</a>.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Sources: the MOIP official English announcement on the 5 January 2026 cooperation memorandum; reporting by the Korea Herald and AJU Press; Korean media reports on the retail store dispute (reported allegations, not adjudicated findings); Chinese financial and industry media reporting on the AKF exclusive-licence dispute (public reports, with no court, compensation amount or exact date asserted); <em>Trademark Law of the PRC (2026 Revision)</em>, effective 1 January 2027; WIPO materials. Figures and case details come from media reporting, not official judgments. General information, not legal advice; confirm current official rules.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Worried about a Korean brand being copied in China?</strong> <a href="/contact.html">Talk to our team</a> about an early CNIPA filing, a Chinese-name search and a monitoring plan.</p></div>
"""),
        ],
    },

 }},

 # ==================================================================== JA
 'ja': {'articles': {

    'jp': {
        'slug': 'japanese-companies-china-trademark-registration',
        'title': '日本企業が中国で商標を登録するための国別ガイド',
        'desc': '中国へ出願する日本企業向けの実務ガイド。現地代理人の必須要件、6ヶ月の優先権、マドリッドと直接出願、中国語表記、公文書の認証、2027年施行の改正点を整理します。',
        'lede': '日中は文字を共有しても登録簿は別です。日本で知られたブランドでも、中国では中国語名を第三者に先に出願されていることがあります。以下は日本の出願人を含むすべての外国出願人に適用される規則です。',
        'card_text': '漢字は簡体字ではなく、支社は営業所ではなく、6ヶ月の優先権は国外での最初の出願から起算します。出荷前に整えるべき出願計画。',
        'category': '国別ガイド',
        'read_time': '約9分',
        'tags': ['日本企業', '中国商標', '国別ガイド'],
        'related': [
            ('{HUB}', '旧法・新法の条項対比'),
            ('{ACT}', '2027年までにやるべきこと'),
            ('{L}/muji-trademark-war-china.html', '無印良品の商標紛争'),
        ],
        'sections': [
            ('the-local-agent-rule', 'まず押さえるべき現地代理人ルール', """
<p class="leading-relaxed text-slate-300 mb-6">中国に常居所または営業所を有しない外国の出願人は、中国国内で適法に設立・届出された商標代理機構を通じて出願しなければなりません。2026年商標法第11条もこの規則を引き継いでいます。以後の手続はすべて代理人を経由するため、最初に代理関係を設計してください。</p>
<p class="leading-relaxed text-slate-300 mb-6">見落とされやすい点が二つあります。中国に支社を置くだけでは、ここでいう営業所を有する扱いにはならず、免除は成立しません。また日本の出願人に特別な扱いがあるわけではなく、輸出実績や知名度にかかわらず、すべての外国主体に同じ規則が適用されます。委任状を常備し、出願人名と住所を全書類で一致させ、代理人を書類の取次ぎではなくチームの一員として扱ってください。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">適格要件の概要は<a href="{L}/who-can-register-trademark-in-china.html">「中国で商標を登録できる主体」</a>および<a href="{L}/china-first-to-file-trademark-guide.html">先願主義ガイド</a>をご覧ください。</p></div>
"""),
            ('kanji-is-not-chinese', '漢字は簡体字ではない', """
<p class="leading-relaxed text-slate-300 mb-6">日本語の漢字と中国の簡体字は同じ標識ではありません。さらに英字商標と中国語商標は中国では別個の権利です。ローマ字表記のブランドを登録しても、消費者が実際に使う中国語名は守られません。</p>
<p class="leading-relaxed text-slate-300 mb-6">公式の中国語名、広く用いられる音写、消費者が自然に付けた通称を出願してください。類似の判断は音・形・義の三面で行われるため、英字が異なっても中国語表記が似ていれば抵触し得ます。カタカナやローマ字のブランドは中国の消費者によって中国語に書き換えられるのが通例です。第三者に先取りされる前に、それらの中国語表記を調査してください。</p>
<ul>
<li><strong>英字・ローマ字の文字商標</strong>――包装に印字するつづりであり、店頭で呼ばれる名前ではありません。</li>
<li><strong>公式の中国語名</strong>――別個の権利であり、第三者が独自に登録できます。</li>
<li><strong>音写と表記の揺れ</strong>――形や意味だけでなく音でも比較されます。</li>
<li><strong>消費者の通称・略称</strong>――市場で実際に流通する形であることが多いものです。</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">日本のアニメ・飲食・小売ブランドの先取り登録は既に報じられています。<a href="{L}/muji-trademark-war-china.html">無印良品の事例</a>、<a href="{L}/japanese-anime-ip-trademark-china.html">アニメの知財紛争</a>、<a href="{L}/japanese-ramen-chain-china-trademark.html">ラーメンチェーンの事例</a>をご覧ください。中国語表記の調査は市場参入の初手に置くべきです。</p>
"""),
            ('priority-and-two-routes', '6ヶ月の優先権と二つの出願ルート', """
<p class="leading-relaxed text-slate-300 mb-6">パリ条約に基づき、国外で最初に出願した商標は、その日から<strong>6ヶ月以内</strong>に同一の商標・同一の商品または役務について中国へ出願し、優先権を主張できます。主張は中国への出願時に書面で行い、最初の出願書類の副本を<strong>3ヶ月以内</strong>に提出します（2026年法第29条、旧法第25条に相当）。国際博覧会で展示した商品に最初に使用した場合も6ヶ月の優先権が生じます。</p>
<p class="leading-relaxed text-slate-300 mb-6">経路は二つです。マドリッド制度で中国を指定する国際登録は、CNIPAが中国法に基づいて審査し、商品の表示は中国の類似群・サブクラスに合わせる必要があります。もう一方はCNIPAへの直接の国内出願です。国際登録は最初の<strong>5年間</strong>、本国の基礎登録に依存します。基礎登録が失効すれば、その上に築いた保護も失われ得る、いわゆるセンターアタックのリスクです。中国を指定した案件にWIPOから暫定拒絶が通知された場合、職権による拒絶は<strong>15日</strong>、異議に基づく拒絶は<strong>30日</strong>が応答期限で、いずれも通知を受領した時から起算し、補充証拠は<strong>3ヶ月以内</strong>です（WIPOの公式な期限一覧）。短い期限に備え、中国の代理人へ事前に指示を出しておいてください。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">輸出やOEM製造だけでは中国の商標権は生じません。出荷・掲載前に出願してください。<a href="{L}/madrid-vs-direct-filing-china.html">マドリッドと直接出願の比較</a>、<a href="{L}/china-trademark-classes-complete-guide.html">区分ガイド</a>もご活用ください。</p></div>
"""),
            ('documents-language-and-legalisation', '書類・言語・認証', """
<p class="leading-relaxed text-slate-300 mb-6">出願書類は中国語で作成します。外国語の主体資格証明には中国語の訳文を添え、出願人名と住所は英語表記と中国語表記を対応させてください。公式の中国語表記を一度決めて全書類で統一することが、訳文と登記内容の食い違いによる指摘を防ぐ近道です。</p>
<p class="leading-relaxed text-slate-300 mb-6">委任状は通常、署名または押印で足り、必ず公証・認証が必要だと決めつけないでください。公文書の認証が必要な場合、ハーグ条約（外国公文書の認証要件を廃止する条約）は<strong>2023年11月7日</strong>に中国で発効しました。締約国からの公文書は、従来の外交部と駐在大使館・領事館による二段階の領事認証に代えてアポスティーユで足ります。非締約国では引き続き従来の領事認証を用います。適用の可否は書類の種類と受理側の要件によって変わるため、一般論ではなく代理人に当期の取扱いを確認してください。</p>
"""),
            ('the-2027-law', '2027年法が日本企業にもたらす変化', """
<p class="leading-relaxed text-slate-300 mb-6">2026年商標法は<strong>2027年1月1日</strong>に施行されます。第36条は異議申立期間を公告から3ヶ月から<strong>2ヶ月</strong>へ短縮し、登録簿の監視は週次の運用業務になります。第19条は悪意の出願を規制します。第57条は<strong>3年連続</strong>で使用されなかった登録商標をCNIPAが職権で取り消せるようにするため、日付入りの使用証拠を初日から保管する必要があります。</p>
<p class="leading-relaxed text-slate-300 mb-6">第21条は未登録の周知商標に区分を越えた保護を認め、中国で出願前に既に知られていた日本ブランドに関係します。第55条は使用許諾の届出と法定解除権を、第46条は譲渡の実質審査を定めます。いずれも、登録簿に置いただけの権利ではなく、実際に使われ、監視され、資料で裏付けられたポートフォリオを重視する方向です。<a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2ヶ月対応のウォッチング手順</a>と<a href="{L}/china-trademark-non-use-cancellation-evidence.html">使用証拠ガイド</a>をご覧ください。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">対応項目の全体像は<a href="{ACT}">「2027年までに外国ブランドがやるべきこと」</a>にまとめています。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第11条・第19条・第21条・第29条・第36条・第46条・第55条・第57条、パリ条約、ハーグ条約（2023年11月7日に中国で発効）、WIPOの公式な期限一覧、CNIPAの中国語出願に関する実務。手続は実施条例等でさらに細分化される可能性があります。当期の公式要件をご確認ください。本記事は一般情報であり法律に関する助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>日本から出願をご検討ですか？</strong> <a href="/contact.html">現地代理人の手配、中国語名の調査、優先権に合わせた出願計画についてご相談ください</a>。</p></div>
"""),
        ],
    },

    'kr': {
        'slug': 'korean-companies-china-trademark-registration',
        'title': '韓国企業が中国で商標を登録するための国別ガイド',
        'desc': '中国へ出願する韓国企業向けのガイド。現地代理人の必須要件、K-beautyの区分設計、ハングル名と中国語音写、6ヶ月の優先権、マドリッドと直接出願、2027年施行の改正点を整理します。',
        'lede': 'K-beautyの普及は速く、その名前を先に出願する動きも速いものです。中国では韓国の登録は効力を持たず、ハングル名は中国の消費者が使う表記でもありません。韓国の権利者の視点から出願規則をまとめました。',
        'card_text': '中国語名は別個の権利として扱い、第3類・第35類・第44類は法定要件ではなく設計上の選択とし、販売店に先を越される前に6ヶ月の優先権を主張してください。',
        'category': '国別ガイド',
        'read_time': '約9分',
        'tags': ['韓国企業', 'K-beauty', '国別ガイド'],
        'related': [
            ('{HUB}', '旧法・新法の条項対比'),
            ('{ACT}', '2027年までにやるべきこと'),
            ('{L}/korean-brands-trademark-squatting-china-cases.html', '中国における韓国ブランドの商標紛争'),
        ],
        'sections': [
            ('the-local-agent-rule', '現地代理人ルールは等しく適用される', """
<p class="leading-relaxed text-slate-300 mb-6">中国に常居所または営業所を有しない外国の出願人は、中国国内で適法に設立・届出された商標代理機構に委任しなければなりません。2026年商標法第11条がこの規則を引き継いでいます。中国向け販売が大きい韓国企業でも、出願は本社ではなく現地代理人が行います。</p>
<p class="leading-relaxed text-slate-300 mb-6">中国に支社を置くだけでは営業所を有する扱いにならず、免除は成立しません。また韓国の出願人に特別な扱いもありません。韓国の知財主管庁であるMOIP（旧KIPO）とCNIPAは知財分野で連携していますが、連携によって権利が移ったり出願要件が免除されたりすることはありません。委任状を代理人に常備し、出願人名と住所を書類間で一致させてください。基礎は<a href="{L}/who-can-register-trademark-in-china.html">「中国で商標を登録できる主体」</a>をご覧ください。</p>
"""),
            ('classes-and-chinese-names', '区分の設計と中国語名', """
<p class="leading-relaxed text-slate-300 mb-6">ハングルのブランド名は、中国の消費者が読み書きする表記ではありません。英字商標と中国語商標は中国では別個の権利です。公式の中国語名、広く用いられる音写、消費者が自然に付けた通称を登録してください。類似は音・形・義で判断されるため、英字が違っても音写が似ていれば抵触し得ます。</p>
<table>
<thead><tr><th>K-beautyでよく検討される区分</th><th>扱い方</th></tr></thead>
<tbody>
<tr><td>第3類（化粧品）</td><td>商品そのものについて広く選ばれる区分</td></tr>
<tr><td>第35類（小売）</td><td>店舗・オンライン小売の役務で検討されることが多い区分</td></tr>
<tr><td>第44類（美容サービス）</td><td>サロン・施術を伴う業態で検討されることが多い区分</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">これは法定要件ではなくポートフォリオ設計上の広く見られる選択です。必要な区分は実際の商品・役務によって決まり、商品の表示はCNIPAの類似群・サブクラスに合わせる必要があります。<a href="{L}/china-trademark-classes-complete-guide.html">区分ガイド</a>で設計し、参入前に中国語表記を調査してください。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">海外の登録商標が中国で効力を持たない理由</a>と<a href="{L}/china-first-to-file-trademark-guide.html">先願主義ガイド</a>もご覧ください。</p></div>
"""),
            ('priority-and-two-routes', '6ヶ月の優先権と二つの出願ルート', """
<p class="leading-relaxed text-slate-300 mb-6">パリ条約に基づき、国外で最初に出願した商標は、その日から<strong>6ヶ月以内</strong>に同一の商標・同一の商品または役務について中国へ出願し、優先権を主張できます。主張は出願時に書面で行い、最初の出願書類の副本を<strong>3ヶ月以内</strong>に提出します（2026年法第29条、旧法第25条に相当）。国際博覧会での最初の使用も6ヶ月の優先権を生じます。販売店との交渉中にこの期間を失しやすいので注意してください。</p>
<p class="leading-relaxed text-slate-300 mb-6">経路は二つです。マドリッド制度で中国を指定する国際登録はCNIPAが中国法で審査し、商品の表示は現地のサブクラスに合わせます。もう一方は直接の国内出願です。国際登録は最初の<strong>5年間</strong>、本国の基礎登録に依存します。いわゆるセンターアタックのリスクです。中国を指定する案件のWIPO暫定拒絶は、職権による拒絶が<strong>15日</strong>、異議に基づく拒絶が<strong>30日</strong>の応答期限で、いずれもWIPO通知の受領時から起算し、補充証拠は<strong>3ヶ月以内</strong>です（WIPOの公式な期限一覧）。<a href="{L}/madrid-vs-direct-filing-china.html">マドリッドと直接出願の比較</a>もご覧ください。</p>
"""),
            ('documents-language-and-legalisation', '書類・言語・認証', """
<p class="leading-relaxed text-slate-300 mb-6">出願書類は中国語で作成します。外国語の主体資格証明には中国語の訳文を添え、出願人名と住所は英語表記と中国語表記を対応させます。公式の中国語表記を一度決めて使い回すことが、登記内容との食い違いによる指摘を避ける近道です。</p>
<p class="leading-relaxed text-slate-300 mb-6">委任状は通常、署名または押印で足り、必ず公証・認証が必要だと決めつけないでください。公文書の認証が必要な場合、ハーグ条約は<strong>2023年11月7日</strong>に中国で発効しました。締約国からの公文書は、従来の外交部と駐在大使館・領事館による二段階の領事認証に代えてアポスティーユで足ります。非締約国では従来の領事認証を用います。適用の可否は書類の種類と受理側の要件で変わります。一般論ではなく代理人に当期の取扱いを確認し、公式規則に記載のない手数料や所要期間を決めつけないでください。</p>
"""),
            ('squatting-and-the-2027-law', '先取り登録・監視と2027年法', """
<p class="leading-relaxed text-slate-300 mb-6">韓国ブランドは中国で模倣店舗や先取り登録に直面してきました。報じられた事例は<a href="{L}/korean-brands-trademark-squatting-china-cases.html">紛争の事例研究</a>にまとめています。必要な対策は2027年法が重視する方向と一致します。<strong>2027年1月1日</strong>施行で、第36条は異議申立期間を3ヶ月から<strong>2ヶ月</strong>へ短縮し、週次の監視が欠かせなくなります。第19条は悪意の出願を規制し、第57条は<strong>3年連続</strong>で使用されなかった商標をCNIPAが職権で取り消せるようにするため、日付入りの使用証拠を保管してください。</p>
<p class="leading-relaxed text-slate-300 mb-6">第21条は未登録の周知商標に区分を越えた保護を認め、第55条は使用許諾の届出と法定解除権を、第46条は譲渡の実質審査を定めます。越境ECの要件や税関への届出は中国の登録証を前提とするため、出願が権利行使の入口になります。韓国の出願人に特別な扱いはなく、公式規則に記載のない手数料・成功率を想定してはいけません。当期の公式規則を確認し、<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>と<a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2ヶ月対応のウォッチング手順</a>で運用を整えてください。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">販売店やOEM先による先取りは繰り返し見られる構図です。取引の形跡が残る前に出願し、関係を資料で残してください。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第11条・第19条・第21条・第29条・第36条・第46条・第55条・第57条、パリ条約、ハーグ条約（2023年11月7日に中国で発効）、WIPOの公式な期限一覧、CNIPAの中国語出願・区分実務。上記の区分は広く見られる実務例であり法定要件ではありません。手続は実施条例等で細分化される可能性があります。当期の公式要件をご確認ください。本記事は一般情報であり法律に関する助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>韓国から中国へ参入しますか？</strong> <a href="/contact.html">中国語名の調査、区分設計、優先権に合わせた出願についてご相談ください</a>。</p></div>
"""),
        ],
    },

    'us': {
        'slug': 'us-companies-china-trademark-registration',
        'title': '米国企業が中国で商標を登録するための国別ガイド',
        'desc': '中国へ出願する米国企業向けのガイド。米国登録が中国で効力を持たない理由、6ヶ月の優先権、マドリッドの15日・30日の応答期限、ハーグ条約締約国のアポスティーユ、2027年施行の改正点を整理します。',
        'lede': '米国の登録は米国の権利です。中国では効力を持たず、商品に付した標識が中国の消費者が使う表記とは限りません。短い応答期限でつまずきやすい点も含め、米国の権利者の視点から出願規則をまとめました。',
        'card_text': '米国登録は中国に及ばず、6ヶ月の優先権には書面の主張と3ヶ月以内の副本が必要で、中国を指定するマドリッドの拒絶への応答は15日または30日しか残されない場合があります。',
        'category': '国別ガイド',
        'read_time': '約9分',
        'tags': ['米国企業', 'アポスティーユ', '国別ガイド'],
        'related': [
            ('{HUB}', '旧法・新法の条項対比'),
            ('{ACT}', '2027年までにやるべきこと'),
            ('{L}/madrid-vs-direct-filing-china.html', 'マドリッドと直接出願の比較'),
        ],
        'sections': [
            ('the-local-agent-rule', 'まず押さえるべき現地代理人ルール', """
<p class="leading-relaxed text-slate-300 mb-6">中国に常居所または営業所を有しない外国の出願人は、中国国内で適法に設立・届出された商標代理機構を通じて出願しなければなりません。2026年商標法第11条がこの規則を引き継いでいます。中国に販売チームを置く米国の大企業でも、出願は現地代理人が行います。期限が動き出す前に委任してください。</p>
<p class="leading-relaxed text-slate-300 mb-6">中国に支社を置くだけでは営業所を有する扱いにならず、免除は成立しません。米国の出願人に特別な扱いもありません。委任状を常備し、出願人名と住所を一致させてください。基礎は<a href="{L}/who-can-register-trademark-in-china.html">「中国で商標を登録できる主体」</a>をご覧ください。</p>
"""),
            ('us-registration-does-not-extend', '米国登録は中国で効力を持たない', """
<p class="leading-relaxed text-slate-300 mb-6">中国は先願主義であり、米国の登録は中国で権利を生みません。英字商標と中国語商標は別個の権利です。公式の中国語名、広く用いられる音写、消費者が自然に付けた通称を登録してください。類似は音・形・義で判断されるため、英字が違っても中国語表記が似ていれば抵触し得ます。英字のみを出願した米国の権利者が、中国語名を第三者に取られていることに後で気づく例は少なくありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">公式の中国語表記を一度決め、包装と出願書類の両方で使い、参入前に代替表記を調査してください。中国語表記の調査は商品掲載後ではなく市場参入の初手に置くべきです。<a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">海外の登録商標と中国登録の関係</a>、<a href="{L}/logo-vs-word-mark-china.html">ロゴと文字商標の違い</a>もご覧ください。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/china-first-to-file-trademark-guide.html">先願主義ガイド</a>と<a href="{L}/coca-cola-chinese-name-trademark-china.html">中国語名の事例</a>もあわせてどうぞ。</p></div>
"""),
            ('priority-and-the-15-30-day-windows', '優先権と15日・30日のマドリッド応答期限', """
<p class="leading-relaxed text-slate-300 mb-6">パリ条約に基づき、国外で最初に出願した商標は、その日から<strong>6ヶ月以内</strong>に同一の商標・同一の商品または役務について中国へ出願し、優先権を主張できます。主張は出願時に書面で行い、最初の出願書類の副本を<strong>3ヶ月以内</strong>に提出します（2026年法第29条、旧法第25条に相当）。国際博覧会での最初の使用も6ヶ月の優先権を生じます。</p>
<table>
<thead><tr><th>項目</th><th>規則</th></tr></thead>
<tbody>
<tr><td>マドリッドで中国を指定</td><td>CNIPAが中国法で審査。商品の表示は現地の類似群・サブクラスに合わせる</td></tr>
<tr><td>基礎登録への依存</td><td>最初の5年間。いわゆるセンターアタックのリスク</td></tr>
<tr><td>職権による暫定拒絶</td><td>WIPO通知の受領から15日以内に応答</td></tr>
<tr><td>異議に基づく暫定拒絶</td><td>WIPO通知の受領から30日以内に応答</td></tr>
<tr><td>補充証拠</td><td>3ヶ月以内に提出（WIPOの公式な期限一覧）</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">通知が届いてから米国の法務部門で指示を集める時間はありません。中国の代理人を事前授権し、経路の選択前に<a href="{L}/madrid-vs-direct-filing-china.html">マドリッドと直接出願の比較</a>をご覧ください。</p>
"""),
            ('apostille-and-documents', 'アポスティーユ・言語・出願書類', """
<p class="leading-relaxed text-slate-300 mb-6">出願書類は中国語で作成します。外国語の主体資格証明には中国語の訳文を添え、出願人名と住所は英語表記と中国語表記を対応させます。委任状は通常、署名または押印で足り、必ず公証・認証が必要だと決めつけないでください。</p>
<p class="leading-relaxed text-slate-300 mb-6">公文書の認証が必要な場合、米国はハーグ条約の締約国であり、同条約は<strong>2023年11月7日</strong>に中国で発効しました。締約国からの公文書は、従来の外交部と駐在大使館・領事館による二段階の領事認証に代えてアポスティーユで足ります。非締約国では従来の領事認証を用います。アポスティーユが使えるかは書類の種類と受理側の要件で決まるため、代理人に当期の取扱いを確認してください。公式規則に記載のない手数料や所要期間を決めつけないことも大切です。</p>
"""),
            ('the-2027-law-and-defensive-portfolios', '2027年法と防御用のポートフォリオ', """
<p class="leading-relaxed text-slate-300 mb-6">2026年商標法は<strong>2027年1月1日</strong>に施行されます。第19条は、使用意思がなく通常の事業上の必要性を明らかに超える出願を含む悪意の出願を規制します。取引に使う予定のない標識を多数抱える防御用の組み合わせを持つ米国の権利者は、保有の見直しが必要です。まさにこの構図が同条の対象であり、第57条は別途、<strong>3年連続</strong>で使用されなかった商標をCNIPAが職権で取り消せるようにします。</p>
<p class="leading-relaxed text-slate-300 mb-6">第36条は異議申立期間を3ヶ月から<strong>2ヶ月</strong>へ短縮し、第21条は未登録の周知商標に区分を越えた保護を認め、第55条は使用許諾の届出と法定解除権を、第46条は譲渡の実質審査を定めます。方向は明確で、使われ、監視され、資料で裏付けられたポートフォリオが防御しやすいということです。<a href="{L}/china-trademark-non-use-cancellation-evidence.html">使用証拠ガイド</a>と<a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2ヶ月対応のウォッチング手順</a>をご覧ください。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">米国の出願人に特別な扱いはなく、当期の公式規則に記載のない手数料・成功率・所要期間を想定してはいけません。詳細は代理人にご確認ください。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第11条・第19条・第21条・第29条・第36条・第46条・第55条・第57条、パリ条約、ハーグ条約（2023年11月7日に中国で発効）、WIPOの公式な期限一覧、CNIPAの中国語出願に関する実務。手続は実施条例等で細分化される可能性があります。当期の公式要件をご確認ください。本記事は一般情報であり法律に関する助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>米国から出願をご検討ですか？</strong> <a href="/contact.html">アポスティーユ書類、中国語名の調査、優先権に合わせた出願計画についてご相談ください</a>。</p></div>
"""),
        ],
    },

    'eu': {
        'slug': 'eu-companies-china-trademark-registration',
        'title': '欧州企業が中国で商標を登録するための国別ガイド',
        'desc': '中国へ出願する欧州企業向けのガイド。欧州連合商標が中国に及ばない理由、6ヶ月の優先権、マドリッドと直接出願、ハーグ条約締約国のアポスティーユ、第21条の周知商標保護、2027年施行の改正点を整理します。',
        'lede': '欧州連合商標は域内で一つの権利ですが、域境で終わります。中国には別の出願が必要です。中国で既に知名度を持つ欧州ブランドに関係する周知商標保護も含め、欧州の権利者の視点から規則をまとめました。',
        'card_text': '欧州連合商標は中国に及ばず、6ヶ月の優先権には書面の主張と3ヶ月以内の副本が必要で、2027年から第21条が未登録の周知商標に区分を越えた保護を認めます。',
        'category': '国別ガイド',
        'read_time': '約9分',
        'tags': ['欧州企業', '欧州連合商標', '国別ガイド'],
        'related': [
            ('{ACT}', '2027年までにやるべきこと'),
            ('{L}/madrid-vs-direct-filing-china.html', 'マドリッドと直接出願の比較'),
            ('{L}/hermes-trademark-china-case.html', 'エルメスの中国商標事例'),
        ],
        'sections': [
            ('the-local-agent-rule', 'まず押さえるべき現地代理人ルール', """
<p class="leading-relaxed text-slate-300 mb-6">中国に常居所または営業所を有しない外国の出願人は、中国国内で適法に設立・届出された商標代理機構を通じて出願しなければなりません。2026年商標法第11条がこの規則を引き継いでいます。欧州のポートフォリオを一つの社内チームで管理していても、中国への出願は現地代理人が行います。</p>
<p class="leading-relaxed text-slate-300 mb-6">中国に支社を置くだけでは営業所を有する扱いにならず、免除は成立しません。欧州の出願人に特別な扱いもありません。委任状を常備し、出願人名と住所を一致させてください。<a href="{L}/who-can-register-trademark-in-china.html">「中国で商標を登録できる主体」</a>もご覧ください。</p>
"""),
            ('eutm-does-not-extend', '欧州連合商標は中国に及ばない', """
<p class="leading-relaxed text-slate-300 mb-6">欧州連合商標は中国には及ばないため、別途中国への出願が必要です。中国は先願主義であり、輸出や報道を通じた知名度だけでは権利になりません。英字商標と中国語商標は別個の権利です。公式の中国語名、広く用いられる音写、消費者が自然に付けた通称を登録してください。類似は音・形・義で判断されます。</p>
<p class="leading-relaxed text-slate-300 mb-6">欧州の高級品・消費財ブランドの中国での紛争は広く報じられており、例えば<a href="{L}/hermes-trademark-china-case.html">エルメスの事例</a>があります。参入前に中国語表記を調査してください。<a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">海外の登録商標が中国で効力を持たない理由</a>もあわせてどうぞ。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/china-first-to-file-trademark-guide.html">先願主義ガイド</a>と<a href="{L}/coca-cola-chinese-name-trademark-china.html">中国語名の事例</a>もご参照ください。</p></div>
"""),
            ('priority-madrid-and-direct', '優先権・マドリッド・直接出願', """
<p class="leading-relaxed text-slate-300 mb-6">パリ条約に基づき、国外で最初に出願した商標は、その日から<strong>6ヶ月以内</strong>に同一の商標・同一の商品または役務について中国へ出願し、優先権を主張できます。主張は出願時に書面で行い、最初の出願書類の副本を<strong>3ヶ月以内</strong>に提出します（2026年法第29条、旧法第25条に相当）。国際博覧会での最初の使用も6ヶ月の優先権を生じます。</p>
<ul>
<li><strong>二つの経路：</strong>マドリッド制度で中国を指定する国際登録はCNIPAが中国法で審査し、商品の表示は現地の類似群・サブクラスに合わせます。直接の国内出願はCNIPAへ提出します。</li>
<li><strong>5年間の依存：</strong>国際登録は最初の5年間、本国の基礎登録に依存します。いわゆるセンターアタックのリスクです。</li>
<li><strong>短い応答期限：</strong>中国を指定する案件のWIPO暫定拒絶は、職権による拒絶が<strong>15日</strong>、異議に基づく拒絶が<strong>30日</strong>、いずれも通知の受領時から起算し、補充証拠は<strong>3ヶ月以内</strong>です（WIPOの公式な期限一覧）。</li>
<li><strong>準備：</strong>この期限内に応答できるよう、中国の代理人を事前授権しておきます。</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">経路を決める前に<a href="{L}/madrid-vs-direct-filing-china.html">マドリッドと直接出願の比較</a>をご覧ください。</p>
"""),
            ('apostille-and-documents', 'アポスティーユ・言語・出願書類', """
<p class="leading-relaxed text-slate-300 mb-6">出願書類は中国語で作成します。外国語の主体資格証明には中国語の訳文を添え、出願人名と住所は欧州の言語表記と中国語表記を対応させます。公式の中国語表記を一度決めて使い回してください。委任状は通常、署名または押印で足り、必ず公証・認証が必要だと決めつけないでください。</p>
<p class="leading-relaxed text-slate-300 mb-6">公文書の認証が必要な場合、欧州連合の加盟国はハーグ条約の締約国であり、同条約は<strong>2023年11月7日</strong>に中国で発効しました。締約国からの公文書は、従来の外交部と駐在大使館・領事館による二段階の領事認証に代えてアポスティーユで足ります。非締約国では従来の領事認証を用います。アポスティーユが使えるかは書類の種類と受理側の要件で決まります。代理人に当期の取扱いを確認し、公式規則に記載のない手数料や所要期間を決めつけないでください。</p>
"""),
            ('article-21-and-the-2027-law', '第21条・2027年法と実務上の対応', """
<p class="leading-relaxed text-slate-300 mb-6">2026年商標法は<strong>2027年1月1日</strong>に施行されます。第21条は未登録の周知商標に区分を越えた保護を認めます。中国で既に知名度を持ちながら出願歴が不十分な欧州ブランドにとって意味のある追加手段ですが、あくまで最後の手段であり、登録に代わるものではありません。知名度の立証には日付入りの証拠が必要で、結果も自ら保有する登録ほど確かではありません。個別の禁用条項についてここで推測はせず、現行の条文と実務を代理人にご確認ください。</p>
<p class="leading-relaxed text-slate-300 mb-6">他の改正も同じ方向を指します。第36条は異議申立期間を3ヶ月から<strong>2ヶ月</strong>へ短縮し、第19条は悪意の出願を規制し、第57条は<strong>3年連続</strong>で使用されなかった商標をCNIPAが職権で取り消せるようにし、第55条は使用許諾の届出と法定解除権を、第46条は譲渡の実質審査を定めます。早期の出願、中国語名の登録、週次の監視、使用証拠の保管が基本です。<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>と<a href="{ACT}">2027年までの対応リスト</a>をご覧ください。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">欧州の出願人に特別な扱いはなく、記載以外の手数料・成功率・所要期間を想定してはいけません。当期の公式規則をご確認ください。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第11条・第19条・第21条・第29条・第36条・第46条・第55条・第57条、パリ条約、ハーグ条約（2023年11月7日に中国で発効）、WIPOの公式な期限一覧、CNIPAの中国語出願に関する実務。手続は実施条例等で細分化される可能性があります。当期の公式要件をご確認ください。本記事は一般情報であり法律に関する助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>欧州から出願をご検討ですか？</strong> <a href="/contact.html">欧州連合商標から中国への出願計画、中国語名の調査、アポスティーユ書類についてご相談ください</a>。</p></div>
"""),
        ],
    },

    'kcase': {
        'slug': 'korean-brands-trademark-squatting-china-cases',
        'title': 'K-beauty に迫る圧力：中国における韓国ブランドの商標紛争',
        'desc': '中国での韓国ブランドの商標紛争を事例研究。2026年の知財協力了解覚書、報じられた模倣店舗、化粧品ブランドの独占使用許諾紛争、そして三つに共通する出願・監視・証拠の対策を整理します。',
        'lede': '中国で報じられた韓国ブランドの三つの紛争は、同じ教訓を示します。政策の了解覚書、模倣店舗、独占使用許諾の争い。いずれも、先願主義の下では知名度だけでは権利にならないという一点に戻ります。権利は早期の、資料の整った中国登録から生まれます。',
        'card_text': '2026年の知財協力了解覚書が実際に何をするのか、報じられた模倣店舗と化粧品ブランドの許諾紛争が何を示すのか、そしてその教訓を出願計画に落とす予防チェックリスト。',
        'category': '事例研究',
        'read_time': '約9分',
        'tags': ['K-beauty', '先取り登録', '事例研究'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', '商標モニタリングと保護戦略'),
            ('{L}/china-first-to-file-trademark-guide.html', '中国の先願主義ガイド'),
            ('{ACT}', '2027年までにやるべきこと'),
        ],
        'sections': [
            ('the-mou', '二国間了解覚書が悪意の出願を議題に載せた', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2026年1月5日</strong>、韓中首脳会談の機会に、韓国の知財主管庁であるMOIP（旧KIPO）とCNIPAは、従前の二国間取り決めを拡充する知財協力の了解覚書に署名しました。MOIPの公式な英語発表および韓国の報道によれば、協力範囲は模倣品対策、審査におけるAI・ビッグデータの活用、知財取引と事業化に及びます。両者は特に、悪意の商標先取り登録に共同で対処することで一致しました。</p>
<p class="leading-relaxed text-slate-300 mb-6">ここで、この覚書が何をし、何をしないかを正確に押さえる必要があります。協力の了解覚書は連携の枠組みを定めるものであり、中国の出願法を変えたり、韓国の登録を中国に及ぼしたり、中国の権利への近道を作ったりするものではありません。中国における保護はあくまでCNIPAの登録から生まれます。この発表は、課題が高い水準で注目されているという合図であり、出願の代わりではないと読んでください。</p>
"""),
            ('lookalike-stores', '模倣店舗と消費者の混同', """
<p class="leading-relaxed text-slate-300 mb-6">韓国の報道によれば、2026年初め、中国湖南省長沙市に「オンリーヤング」と称する化粧品店が現れ、韓国のオリーブヤングの名称・ロゴ・店舗の配色・陳列方式を模したと指摘されました。誠信女子大学のソ・ギョンドク教授が公にコメントし、関連する宣伝動画が短動画プラットフォームで拡散しました。別の争いでは、中国の生活用品ブランドが海外店舗で韓国を連想させる文字表示を用い、出所の誤認を招いたとされます。</p>
<p class="leading-relaxed text-slate-300 mb-6">いずれも裁判上の認定ではなく報じられた指摘ですので、危険の構図を示す例として扱ってください。商標上の要点は、店名・ロゴ・配色・陳列が別個の要素だということです。文字商標の出願は図形や店舗の外観を必ずしも覆わず、中国語の看板は英字名とは別の権利です。英字のみを登録したブランドは、文字商標の抵触が明確でないまま、外観の同一性を模されることがあります。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">英字商標と併せて中国語名・図形商標・広く用いられる音写を登録し、市場でどのように提示したかを日付入りで残してください。<a href="{L}/logo-vs-word-mark-china.html">ロゴと文字商標の違い</a>もご覧ください。</p></div>
"""),
            ('the-akf-licence-dispute', '化粧品ブランドの独占使用許諾をめぐる紛争', """
<p class="leading-relaxed text-slate-300 mb-6">公開された報道によれば、終審判決で中心となる商標の独占使用許諾契約が有効と認められました。同ブランドはピーク時に年間売上が人民元25億元に迫ったと報じられています。出典が公式の判決文ではなく中国の経済・業界報道であるため、裁判所名・賠償額・特定の日付を確定事実としては記さず、報じられた結論を超える当事者への評価も行いません。</p>
<p class="leading-relaxed text-slate-300 mb-6">実務上の教訓は書類の整備です。独占使用許諾は、背後にある権利の帰属関係と、その届出の仕方によって強さが決まります。外国のブランド権利者からの許諾を前提に中国事業を組み立てる場合、元になる中国登録、許諾契約、届出の書類を矛盾なく最新に保つ必要があります。2026年法第55条は使用許諾の届出と法定解除権を、第46条は譲渡の実質審査を定めており、譲渡・許諾も当初の出願と同じ注意を要します。<a href="{L}/china-trademark-assignment-licence-recordal.html">譲渡・使用許諾の届出</a>をご覧ください。</p>
"""),
            ('what-these-cases-share', '三つの事例に共通すること', """
<p class="leading-relaxed text-slate-300 mb-6">異なる三つの構図が、同じ対策を指しています。協力の了解覚書は政策水準で悪意の出願を扱い、模倣店舗は外観・中国語の同一性が登録されていたかを試し、許諾紛争は権利の鎖が書類化されていたかを試します。いずれも知名度だけでは解決しません。</p>
<table>
<thead><tr><th>紛争の型</th><th>露呈すること</th><th>効いていた対策</th></tr></thead>
<tbody>
<tr><td>悪意の先取り出願</td><td>中国は先願主義であり、出願のない知名度は脆い</td><td>早期のCNIPA登録と週次の監視</td></tr>
<tr><td>模倣店舗の同一性</td><td>文字商標・図形商標・中国語名は別個の権利</td><td>標識一式の登録と日付入りの提示証拠</td></tr>
<tr><td>独占使用許諾の争い</td><td>許諾には整った権利の帰属と届出が必要</td><td>登録・許諾・届出の書類の整合</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">結論は運用に落ちます。CNIPAへの早期出願、中国語名の登録、継続して行う監視、使用証拠の保管です。越境ECの要件や税関への届出はいずれも中国の登録証を前提とするため、出願が権利行使の入口になります。<a href="{L}/amazon-tmall-trademark-requirement-china.html">越境ECの商標要件</a>と<a href="{L}/china-trademark-enforcement-routes-after-registration.html">登録後の権利行使ルート</a>もご覧ください。</p>
"""),
            ('a-preventive-checklist', '韓国ブランドのための予防チェックリスト', """
<ol>
<li><strong>標識一式を出願する。</strong>英字商標、公式の中国語名、広く用いられる音写、消費者の通称、図形商標は別個の出願です。</li>
<li><strong>実際の商品・役務で区分を設計する。</strong>K-beautyでは第3類（化粧品）・第35類（小売）・第44類（美容サービス）を検討するのが広く見られる実務例です。法定要件ではありません。</li>
<li><strong>使える優先権を使う。</strong>国外での最初の出願から6ヶ月以内に書面でパリ条約の優先権を主張し、3ヶ月以内に最初の出願書類の副本を提出します。博覧会での最初の使用も6ヶ月です。</li>
<li><strong>中国の代理人を委任する。</strong>中国に常居所または営業所を有しない外国の出願人は代理人経由が必須で、支社を置くだけでは免除されません。</li>
<li><strong>週次で監視する。</strong>2027年1月1日から異議申立期間は2ヶ月となり、四半期ごとの確認では間に合いません。</li>
<li><strong>使用証拠を保管する。</strong>第57条は3年使用されなかった商標をCNIPAが職権で取り消せるようにします。</li>
<li><strong>書類を最新に保つ。</strong>訳文、名称と住所の対応、委任状、許諾・譲渡の届出。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">韓国の出願人に特別な扱いはなく、記載以外の手数料・成功率・所要期間を想定してはいけません。当期の公式規則を代理人にご確認ください。<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>と<a href="{ACT}">2027年までの対応リスト</a>もご活用ください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">出典：2026年1月5日の知財協力了解覚書に関するMOIPの公式な英語発表、韓国の主要報道、模倣店舗をめぐる韓国の報道（裁判上の認定ではなく報じられた指摘）、化粧品ブランドの独占使用許諾紛争に関する中国の経済・業界報道（公開報道であり、裁判所名・賠償額・特定の日付は確定事実として記していません）、『中華人民共和国商標法（2026年改正）』（2027年1月1日施行）、WIPOの資料。数値・事例の詳細は公式の判決文ではなく報道に基づきます。本記事は一般情報であり法律に関する助言ではありません。当期の公式規則をご確認ください。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>中国で韓国ブランドの模倣が心配ですか？</strong> <a href="/contact.html">早期のCNIPA出願、中国語名の調査、監視計画についてご相談ください</a>。</p></div>
"""),
        ],
    },

 }},

 # ==================================================================== KO
 'ko': {'articles': {

    'jp': {
        'slug': 'japanese-companies-china-trademark-registration',
        'title': '일본 기업이 중국에서 상표를 등록하기 위한 국가별 가이드',
        'desc': '중국에 출원하는 일본 기업을 위한 실무 가이드. 현지 대리인 필수 요건, 6개월 우선권, 마드리드와 직접 출원, 중국어 표기, 공문서 인증, 2027년 시행 개정 사항을 정리했습니다.',
        'lede': '한자 문화권을 공유해도 등록부는 별개입니다. 일본에서 익숙한 브랜드도 중국에서는 중국어 명칭을 제3자가 먼저 출원해 둔 경우가 있습니다. 아래 규정은 일본 출원인을 포함한 모든 외국 출원인에게 적용됩니다.',
        'card_text': '한자는 간체자가 아니고, 지사는 영업소가 아니며, 6개월 우선권은 국외 최초 출원일부터 기산합니다. 출하 전에 갖춰야 할 출원 계획.',
        'category': '국가별 가이드',
        'read_time': '약 9분',
        'tags': ['일본 기업', '중국 상표', '국가별 가이드'],
        'related': [
            ('{HUB}', '구법·신법 조항 대조'),
            ('{ACT}', '2027년 전에 해야 할 일'),
            ('{L}/muji-trademark-war-china.html', '무인양품 상표 분쟁'),
        ],
        'sections': [
            ('the-local-agent-rule', '먼저 확인할 현지 대리인 규정', """
<p class="leading-relaxed text-slate-300 mb-6">중국에 상주하는 주소나 영업소가 없는 외국 출원인은 중국 국내에 적법하게 설립·등록된 상표 대리 기관을 통해 출원해야 합니다. 2026년 상표법 제11조도 이 규정을 이어갑니다. 이후 모든 절차가 대리인을 거치므로 가장 먼저 대리 관계를 설계하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">자주 놓치는 점이 둘 있습니다. 중국에 지사를 두기만 해도 여기서 말하는 영업소가 있는 것으로 인정되지 않아 면제가 성립하지 않습니다. 또한 일본 출원인에게만 특별한 대우가 있는 것이 아니며, 수출 실적이나 인지도와 무관하게 모든 외국 주체에 같은 규정이 적용됩니다. 위임장을 상비하고 출원인 명칭과 주소를 모든 서류에서 일치시키며, 대리인을 단순한 서류 전달자가 아니라 팀의 일원으로 다루십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">자격 요건의 개요는 <a href="{L}/who-can-register-trademark-in-china.html">중국에서 상표를 등록할 수 있는 주체</a>와 <a href="{L}/china-first-to-file-trademark-guide.html">선출원주의 가이드</a>를 참고하십시오.</p></div>
"""),
            ('kanji-is-not-chinese', '한자는 간체자가 아니다', """
<p class="leading-relaxed text-slate-300 mb-6">일본 한자와 중국 간체자는 같은 표장이 아닙니다. 또한 영문 표장과 중국어 표장은 중국에서 별개의 권리입니다. 로마자 표기의 브랜드를 등록해도 소비자가 실제로 쓰는 중국어 명칭은 보호되지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">공식 중국어 명칭, 흔히 쓰이는 음역, 소비자가 스스로 붙인 애칭을 출원하십시오. 유사 판단은 음·형·의 세 측면에서 이루어지므로 영문이 달라도 중국어 표기가 닮으면 충돌할 수 있습니다. 가타카나나 로마자 브랜드는 중국 소비자가 중국어로 다시 적는 것이 통례입니다. 제3자가 먼저 출원하기 전에 그 중국어 표기들을 조사하십시오.</p>
<ul>
<li><strong>영문·로마자 문자상표</strong>——포장에 찍히는 철자이며 매장에서 불리는 이름이 아닙니다.</li>
<li><strong>공식 중국어 명칭</strong>——별개의 권리로 제3자가 독자적으로 등록할 수 있습니다.</li>
<li><strong>음역과 표기 변형</strong>——형태나 의미뿐 아니라 음에서도 비교됩니다.</li>
<li><strong>소비자 애칭·약칭</strong>——시장에서 실제로 유통되는 형태인 경우가 많습니다.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">일본 애니메이션·외식·소매 브랜드의 선점 등록은 이미 보도되어 있습니다. <a href="{L}/muji-trademark-war-china.html">무인양품 사례</a>, <a href="{L}/japanese-anime-ip-trademark-china.html">애니메이션 지식재산 분쟁</a>, <a href="{L}/japanese-ramen-chain-china-trademark.html">라멘 체인 사례</a>를 보십시오. 중국어 표기 조사는 시장 진입의 첫 단계에 두어야 합니다.</p>
"""),
            ('priority-and-two-routes', '6개월 우선권과 두 가지 출원 경로', """
<p class="leading-relaxed text-slate-300 mb-6">파리 조약에 따라 국외에서 처음 출원한 상표는 그날부터 <strong>6개월 이내</strong>에 동일한 상표·동일한 상품 또는 서비스로 중국에 출원하며 우선권을 주장할 수 있습니다. 주장은 중국 출원 시 서면으로 하고, 최초 출원 서류의 사본을 <strong>3개월 이내</strong>에 제출합니다(2026년 법 제29조, 구법 제25조에 해당). 국제박람회에 전시한 상품에 처음 사용한 경우에도 6개월 우선권이 생깁니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">경로는 둘입니다. 마드리드 제도로 중국을 지정하는 국제등록은 CNIPA가 중국법에 따라 심사하며 상품 표시를 중국의 유사군·세부 구분에 맞춰야 합니다. 다른 하나는 CNIPA에 직접 하는 국내 출원입니다. 국제등록은 처음 <strong>5년간</strong> 본국의 기초등록에 의존합니다. 기초등록이 소멸하면 그 위에 세운 보호도 함께 무너질 수 있는, 이른바 센터 어택 위험입니다. 중국을 지정한 사건에 WIPO가 잠정 거절을 통지하면 직권에 의한 거절은 <strong>15일</strong>, 이의에 기초한 거절은 <strong>30일</strong>이 응답 기한이며 모두 통지 수령 시부터 기산하고, 보충 증거는 <strong>3개월 이내</strong>입니다(WIPO 공식 기한표). 짧은 기한에 대비해 중국 대리인에게 미리 지시해 두십시오.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">수출이나 OEM 제조만으로는 중국 상표권이 생기지 않습니다. 출하·등록 전에 출원하십시오. <a href="{L}/madrid-vs-direct-filing-china.html">마드리드와 직접 출원 비교</a>와 <a href="{L}/china-trademark-classes-complete-guide.html">클래스 가이드</a>도 활용하십시오.</p></div>
"""),
            ('documents-language-and-legalisation', '서류·언어·인증', """
<p class="leading-relaxed text-slate-300 mb-6">출원 서류는 중국어로 작성합니다. 외국어로 된 주체 자격 증명에는 중국어 번역본을 붙이고, 출원인 명칭과 주소는 영문 표기와 중국어 표기를 대응시켜야 합니다. 공식 중국어 표기를 한 번 정해 모든 서류에 통일하면 번역본과 등기 내용의 불일치로 인한 지적을 막는 지름길이 됩니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">위임장은 보통 서명이나 직인으로 충분하므로 반드시 공증·인증이 필요하다고 단정하지 마십시오. 공문서 인증이 필요한 경우, 헤이그 협약(외국 공문서의 인증 요건 폐지 협약)은 <strong>2023년 11월 7일</strong> 중국에서 발효했습니다. 체약국에서 온 공문서는 기존의 외교부와 재외 공관을 거치는 2단계 영사 인증 대신 아포스티유로 충분합니다. 비체약국은 기존 영사 인증을 계속 이용합니다. 적용 여부는 서류 종류와 접수 기관의 요건에 따라 달라지므로 일반론이 아니라 대리인에게 당기 취급을 확인하십시오.</p>
"""),
            ('the-2027-law', '2027년 법이 일본 기업에 가져오는 변화', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 상표법은 <strong>2027년 1월 1일</strong> 시행됩니다. 제36조는 이의신청 기간을 공고일부터 3개월에서 <strong>2개월</strong>로 줄여 등록부 감시를 주 단위 운영 업무로 만듭니다. 제19조는 악의적 출원을 규제합니다. 제57조는 <strong>3년 연속</strong> 사용되지 않은 등록상표를 CNIPA가 직권으로 취소할 수 있게 하므로, 날짜가 있는 사용 증거를 첫날부터 보관해야 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">제21조는 미등록 주지상표에 클래스를 넘는 보호를 인정해, 중국에서 출원 전 이미 알려졌던 일본 브랜드와 관련됩니다. 제55조는 사용허락의 등록과 법정 해제권을, 제46조는 양도의 실질심사를 정합니다. 모두 등록부에 올려둔 권리보다 실제로 사용되고 감시되며 자료로 뒷받침되는 포트폴리오를 중시하는 방향입니다. <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2개월 대응 워칭 절차</a>와 <a href="{L}/china-trademark-non-use-cancellation-evidence.html">사용 증거 가이드</a>를 보십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">대응 항목 전체는 <a href="{ACT}">2027년 전에 외국 브랜드가 해야 할 일</a>에 정리했습니다.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제11조·제19조·제21조·제29조·제36조·제46조·제55조·제57조, 파리 조약, 헤이그 협약(2023년 11월 7일 중국 발효), WIPO 공식 기한표, CNIPA의 중국어 출원 실무. 절차는 시행조례 등에서 더 세분화될 수 있습니다. 당기 공식 요건을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>일본에서 출원을 검토 중이신가요?</strong> <a href="/contact.html">현지 대리인 선임, 중국어 명칭 조사, 우선권에 맞춘 출원 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },

    'kr': {
        'slug': 'korean-companies-china-trademark-registration',
        'title': '한국 기업이 중국에서 상표를 등록하기 위한 국가별 가이드',
        'desc': '중국에 출원하는 한국 기업을 위한 가이드. 현지 대리인 필수 요건, K-beauty 클래스 설계, 한글명과 중국어 음역, 6개월 우선권, 마드리드와 직접 출원, 2027년 시행 개정 사항을 정리했습니다.',
        'lede': 'K-beauty가 빠르게 퍼지는 만큼 그 이름을 먼저 출원하는 움직임도 빠릅니다. 중국에서 한국 등록은 효력이 없고, 한글명은 중국 소비자가 쓰는 표기도 아닙니다. 한국 권리자의 관점에서 출원 규정을 정리했습니다.',
        'card_text': '중국어 명칭은 별개의 권리로 다루고, 제3류·제35류·제44류는 법정 요건이 아닌 설계상의 선택으로 보며, 유통사가 먼저 출원하기 전에 6개월 우선권을 주장하십시오.',
        'category': '국가별 가이드',
        'read_time': '약 9분',
        'tags': ['한국 기업', 'K-beauty', '국가별 가이드'],
        'related': [
            ('{HUB}', '구법·신법 조항 대조'),
            ('{ACT}', '2027년 전에 해야 할 일'),
            ('{L}/korean-brands-trademark-squatting-china-cases.html', '중국 내 한국 브랜드 상표 분쟁'),
        ],
        'sections': [
            ('the-local-agent-rule', '현지 대리인 규정은 동일하게 적용된다', """
<p class="leading-relaxed text-slate-300 mb-6">중국에 상주하는 주소나 영업소가 없는 외국 출원인은 중국 국내에 적법하게 설립·등록된 상표 대리 기관에 위임해야 합니다. 2026년 상표법 제11조가 이 규정을 이어갑니다. 중국 판매 비중이 큰 한국 기업이라도 출원은 본사가 아니라 현지 대리인이 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">중국에 지사를 두기만 해도 영업소가 있는 것으로 인정되지 않아 면제가 성립하지 않습니다. 한국 출원인에게 특별한 대우도 없습니다. 한국 지식재산부(MOIP, 구 KIPO)와 CNIPA가 지식재산 분야에서 협력하고 있지만, 협력이 권리를 이전하거나 출원 요건을 면제해 주지는 않습니다. 위임장을 대리인에게 상비하고 출원인 명칭과 주소를 서류 간에 일치시키십시오. 기본은 <a href="{L}/who-can-register-trademark-in-china.html">중국에서 상표를 등록할 수 있는 주체</a>를 보십시오.</p>
"""),
            ('classes-and-chinese-names', '클래스 설계와 중국어 명칭', """
<p class="leading-relaxed text-slate-300 mb-6">한글 브랜드명은 중국 소비자가 읽고 쓰는 표기가 아닙니다. 영문 표장과 중국어 표장은 중국에서 별개의 권리입니다. 공식 중국어 명칭, 흔히 쓰이는 음역, 소비자가 스스로 붙인 애칭을 등록하십시오. 유사는 음·형·의로 판단되므로 영문이 달라도 음역이 닮으면 충돌할 수 있습니다.</p>
<table>
<thead><tr><th>K-beauty에서 자주 검토되는 클래스</th><th>다루는 방식</th></tr></thead>
<tbody>
<tr><td>제3류(화장품)</td><td>상품 자체에 대해 일반적으로 선택되는 클래스</td></tr>
<tr><td>제35류(소매)</td><td>매장·온라인 소매 서비스에서 자주 검토되는 클래스</td></tr>
<tr><td>제44류(미용 서비스)</td><td>살롱·시술을 수반하는 업태에서 자주 검토되는 클래스</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">이는 법정 요건이 아니라 포트폴리오 설계상의 일반적 선택입니다. 필요한 클래스는 실제 상품·서비스에 따라 달라지고, 상품 표시는 CNIPA의 유사군·세부 구분에 맞춰야 합니다. <a href="{L}/china-trademark-classes-complete-guide.html">클래스 가이드</a>로 설계하고 진입 전에 중국어 표기를 조사하십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">해외 등록상표가 중국에서 효력이 없는 이유</a>와 <a href="{L}/china-first-to-file-trademark-guide.html">선출원주의 가이드</a>도 보십시오.</p></div>
"""),
            ('priority-and-two-routes', '6개월 우선권과 두 가지 출원 경로', """
<p class="leading-relaxed text-slate-300 mb-6">파리 조약에 따라 국외에서 처음 출원한 상표는 그날부터 <strong>6개월 이내</strong>에 동일한 상표·동일한 상품 또는 서비스로 중국에 출원하며 우선권을 주장할 수 있습니다. 주장은 출원 시 서면으로 하고, 최초 출원 서류의 사본을 <strong>3개월 이내</strong>에 제출합니다(2026년 법 제29조, 구법 제25조에 해당). 국제박람회에서의 최초 사용도 6개월 우선권을 줍니다. 유통 계약을 협의하는 사이에 이 기간을 놓치기 쉽습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">경로는 둘입니다. 마드리드 제도로 중국을 지정하는 국제등록은 CNIPA가 중국법으로 심사하고 상품 표시를 현지 세부 구분에 맞춥니다. 다른 하나는 직접 국내 출원입니다. 국제등록은 처음 <strong>5년간</strong> 본국 기초등록에 의존하며, 이를 이른바 센터 어택 위험이라 합니다. 중국을 지정한 사건의 WIPO 잠정 거절은 직권 거절이 <strong>15일</strong>, 이의에 기초한 거절이 <strong>30일</strong>의 응답 기한이고 모두 WIPO 통지 수령 시부터 기산하며, 보충 증거는 <strong>3개월 이내</strong>입니다(WIPO 공식 기한표). <a href="{L}/madrid-vs-direct-filing-china.html">마드리드와 직접 출원 비교</a>도 보십시오.</p>
"""),
            ('documents-language-and-legalisation', '서류·언어·인증', """
<p class="leading-relaxed text-slate-300 mb-6">출원 서류는 중국어로 작성합니다. 외국어 주체 자격 증명에는 중국어 번역본을 붙이고, 출원인 명칭과 주소는 영문 표기와 중국어 표기를 대응시킵니다. 공식 중국어 표기를 한 번 정해 계속 쓰는 것이 등기 내용과의 불일치로 인한 지적을 피하는 길입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">위임장은 보통 서명이나 직인으로 충분하므로 반드시 공증·인증이 필요하다고 단정하지 마십시오. 공문서 인증이 필요한 경우, 헤이그 협약은 <strong>2023년 11월 7일</strong> 중국에서 발효했습니다. 체약국에서 온 공문서는 기존의 외교부와 재외 공관을 거치는 2단계 영사 인증 대신 아포스티유로 충분합니다. 비체약국은 기존 영사 인증을 이용합니다. 적용 여부는 서류 종류와 접수 기관의 요건에 따라 달라집니다. 일반론이 아니라 대리인에게 당기 취급을 확인하고, 공식 규정에 없는 수수료나 소요 기간을 단정하지 마십시오.</p>
"""),
            ('squatting-and-the-2027-law', '선점·감시와 2027년 법', """
<p class="leading-relaxed text-slate-300 mb-6">한국 브랜드는 중국에서 유사 매장과 선점 출원에 직면해 왔습니다. 보도된 사례는 <a href="{L}/korean-brands-trademark-squatting-china-cases.html">분쟁 사례 연구</a>에 모았습니다. 필요한 통제는 2027년 법이 중시하는 방향과 같습니다. <strong>2027년 1월 1일</strong> 시행으로 제36조는 이의신청 기간을 3개월에서 <strong>2개월</strong>로 줄여 주 단위 감시가 필수가 됩니다. 제19조는 악의적 출원을 규제하고, 제57조는 <strong>3년 연속</strong> 사용되지 않은 상표를 CNIPA가 직권으로 취소할 수 있게 하므로 날짜가 있는 사용 증거를 보관하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">제21조는 미등록 주지상표에 클래스를 넘는 보호를 인정하고, 제55조는 사용허락의 등록과 법정 해제권을, 제46조는 양도의 실질심사를 정합니다. 국경 간 전자상거래 요건과 세관 등록은 중국 등록증을 전제하므로 출원이 권리 행사의 관문입니다. 한국 출원인에게 특별한 대우는 없고, 공식 규정에 없는 수수료·성공률을 가정해서는 안 됩니다. 당기 공식 규정을 확인하고 <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>와 <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2개월 대응 워칭 절차</a>로 운영을 갖추십시오.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">유통사나 OEM 파트너가 먼저 출원하는 구도는 반복됩니다. 거래 흔적이 남기 전에 출원하고 관계를 자료로 남기십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제11조·제19조·제21조·제29조·제36조·제46조·제55조·제57조, 파리 조약, 헤이그 협약(2023년 11월 7일 중국 발효), WIPO 공식 기한표, CNIPA의 중국어 출원·클래스 실무. 위 클래스는 일반적 실무 예시이며 법정 요건이 아닙니다. 절차는 시행조례 등에서 세분화될 수 있습니다. 당기 공식 요건을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>한국에서 중국으로 진출하시나요?</strong> <a href="/contact.html">중국어 명칭 조사, 클래스 설계, 우선권에 맞춘 출원에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },

    'us': {
        'slug': 'us-companies-china-trademark-registration',
        'title': '미국 기업이 중국에서 상표를 등록하기 위한 국가별 가이드',
        'desc': '중국에 출원하는 미국 기업을 위한 가이드. 미국 등록이 중국에서 효력이 없는 이유, 6개월 우선권, 마드리드의 15일·30일 응답 기한, 헤이그 협약 체약국의 아포스티유, 2027년 시행 개정 사항을 정리했습니다.',
        'lede': '미국 등록은 미국의 권리입니다. 중국에서는 효력이 없고, 상품에 붙인 표장이 중국 소비자가 쓰는 표기와 같다고 할 수 없습니다. 짧은 응답 기한에서 자주 걸리는 지점까지 미국 권리자의 관점에서 정리했습니다.',
        'card_text': '미국 등록은 중국에 미치지 않고, 6개월 우선권에는 서면 주장과 3개월 내 사본이 필요하며, 중국을 지정한 마드리드 거절 대응은 15일 또는 30일만 남는 경우가 있습니다.',
        'category': '국가별 가이드',
        'read_time': '약 9분',
        'tags': ['미국 기업', '아포스티유', '국가별 가이드'],
        'related': [
            ('{HUB}', '구법·신법 조항 대조'),
            ('{ACT}', '2027년 전에 해야 할 일'),
            ('{L}/madrid-vs-direct-filing-china.html', '마드리드와 직접 출원 비교'),
        ],
        'sections': [
            ('the-local-agent-rule', '먼저 확인할 현지 대리인 규정', """
<p class="leading-relaxed text-slate-300 mb-6">중국에 상주하는 주소나 영업소가 없는 외국 출원인은 중국 국내에 적법하게 설립·등록된 상표 대리 기관을 통해 출원해야 합니다. 2026년 상표법 제11조가 이 규정을 이어갑니다. 중국에 판매 조직을 둔 미국 대기업이라도 출원은 현지 대리인이 합니다. 기한이 움직이기 전에 위임하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">중국에 지사를 두기만 해도 영업소가 있는 것으로 인정되지 않아 면제가 성립하지 않습니다. 미국 출원인에게 특별한 대우도 없습니다. 위임장을 상비하고 출원인 명칭과 주소를 일치시키십시오. 기본은 <a href="{L}/who-can-register-trademark-in-china.html">중국에서 상표를 등록할 수 있는 주체</a>를 보십시오.</p>
"""),
            ('us-registration-does-not-extend', '미국 등록은 중국에서 효력이 없다', """
<p class="leading-relaxed text-slate-300 mb-6">중국은 선출원주의 국가이며 미국 등록은 중국에서 권리를 만들지 못합니다. 영문 표장과 중국어 표장은 별개의 권리입니다. 공식 중국어 명칭, 흔히 쓰이는 음역, 소비자가 스스로 붙인 애칭을 등록하십시오. 유사는 음·형·의로 판단되므로 영문이 달라도 중국어 표기가 닮으면 충돌할 수 있습니다. 영문만 출원한 미국 권리자가 뒤늦게 중국어 명칭을 제3자가 가져간 사실을 발견하는 일이 적지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">공식 중국어 표기를 한 번 정해 포장과 출원 서류 모두에 쓰고, 진입 전에 대체 표기를 조사하십시오. 중국어 표기 조사는 상품 등록 후가 아니라 시장 진입의 첫 단계에 두어야 합니다. <a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">해외 등록상표와 중국 등록의 관계</a>와 <a href="{L}/logo-vs-word-mark-china.html">로고와 문자상표의 차이</a>도 보십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/china-first-to-file-trademark-guide.html">선출원주의 가이드</a>와 <a href="{L}/coca-cola-chinese-name-trademark-china.html">중국어 명칭 사례</a>도 함께 보십시오.</p></div>
"""),
            ('priority-and-the-15-30-day-windows', '우선권과 15일·30일 마드리드 응답 기한', """
<p class="leading-relaxed text-slate-300 mb-6">파리 조약에 따라 국외에서 처음 출원한 상표는 그날부터 <strong>6개월 이내</strong>에 동일한 상표·동일한 상품 또는 서비스로 중국에 출원하며 우선권을 주장할 수 있습니다. 주장은 출원 시 서면으로 하고, 최초 출원 서류의 사본을 <strong>3개월 이내</strong>에 제출합니다(2026년 법 제29조, 구법 제25조에 해당). 국제박람회에서의 최초 사용도 6개월 우선권을 줍니다.</p>
<table>
<thead><tr><th>항목</th><th>규칙</th></tr></thead>
<tbody>
<tr><td>마드리드로 중국 지정</td><td>CNIPA가 중국법으로 심사. 상품 표시는 현지 유사군·세부 구분에 맞춤</td></tr>
<tr><td>기초등록에 대한 의존</td><td>처음 5년간. 이른바 센터 어택 위험</td></tr>
<tr><td>직권에 의한 잠정 거절</td><td>WIPO 통지 수령 후 15일 내 응답</td></tr>
<tr><td>이의에 기초한 잠정 거절</td><td>WIPO 통지 수령 후 30일 내 응답</td></tr>
<tr><td>보충 증거</td><td>3개월 내 제출(WIPO 공식 기한표)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">통지가 온 뒤에 미국 법무팀이 지시를 모을 시간은 없습니다. 중국 대리인을 사전 위임하고, 경로 선택 전에 <a href="{L}/madrid-vs-direct-filing-china.html">마드리드와 직접 출원 비교</a>를 보십시오.</p>
"""),
            ('apostille-and-documents', '아포스티유·언어·출원 서류', """
<p class="leading-relaxed text-slate-300 mb-6">출원 서류는 중국어로 작성합니다. 외국어 주체 자격 증명에는 중국어 번역본을 붙이고, 출원인 명칭과 주소는 영문 표기와 중국어 표기를 대응시킵니다. 위임장은 보통 서명이나 직인으로 충분하므로 반드시 공증·인증이 필요하다고 단정하지 마십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">공문서 인증이 필요한 경우, 미국은 헤이그 협약 체약국이며 이 협약은 <strong>2023년 11월 7일</strong> 중국에서 발효했습니다. 체약국에서 온 공문서는 기존의 외교부와 재외 공관을 거치는 2단계 영사 인증 대신 아포스티유로 충분합니다. 비체약국은 기존 영사 인증을 이용합니다. 아포스티유를 쓸 수 있는지는 서류 종류와 접수 기관의 요건에 따라 정해지므로 대리인에게 당기 취급을 확인하십시오. 공식 규정에 없는 수수료나 소요 기간을 단정하지 않는 것도 중요합니다.</p>
"""),
            ('the-2027-law-and-defensive-portfolios', '2027년 법과 방어적 포트폴리오', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 상표법은 <strong>2027년 1월 1일</strong> 시행됩니다. 제19조는 사용 의사가 없고 통상의 사업상 필요를 명백히 넘는 출원을 포함해 악의적 출원을 규제합니다. 거래에 쓸 계획이 없는 표장을 다수 보유한 방어적 조합을 가진 미국 권리자는 보유 현황을 점검해야 합니다. 바로 이 구도가 동조의 대상이며, 제57조는 별도로 <strong>3년 연속</strong> 사용되지 않은 상표를 CNIPA가 직권으로 취소할 수 있게 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">제36조는 이의신청 기간을 3개월에서 <strong>2개월</strong>로 줄이고, 제21조는 미등록 주지상표에 클래스를 넘는 보호를 인정하며, 제55조는 사용허락의 등록과 법정 해제권을, 제46조는 양도의 실질심사를 정합니다. 방향은 분명합니다. 사용되고 감시되며 자료로 뒷받침되는 포트폴리오가 방어에 유리합니다. <a href="{L}/china-trademark-non-use-cancellation-evidence.html">사용 증거 가이드</a>와 <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">2개월 대응 워칭 절차</a>를 보십시오.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">미국 출원인에게 특별한 대우는 없고, 당기 공식 규정에 없는 수수료·성공률·소요 기간을 가정해서는 안 됩니다. 자세한 내용은 대리인에게 확인하십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제11조·제19조·제21조·제29조·제36조·제46조·제55조·제57조, 파리 조약, 헤이그 협약(2023년 11월 7일 중국 발효), WIPO 공식 기한표, CNIPA의 중국어 출원 실무. 절차는 시행조례 등에서 세분화될 수 있습니다. 당기 공식 요건을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>미국에서 출원을 검토 중이신가요?</strong> <a href="/contact.html">아포스티유 서류, 중국어 명칭 조사, 우선권에 맞춘 출원 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },

    'eu': {
        'slug': 'eu-companies-china-trademark-registration',
        'title': '유럽 기업이 중국에서 상표를 등록하기 위한 국가별 가이드',
        'desc': '중국에 출원하는 유럽 기업을 위한 가이드. 유럽연합 상표가 중국에 미치지 않는 이유, 6개월 우선권, 마드리드와 직접 출원, 헤이그 협약 체약국의 아포스티유, 제21조 주지상표 보호, 2027년 시행 개정 사항을 정리했습니다.',
        'lede': '유럽연합 상표는 역내에서 하나의 권리지만 역내 경계에서 끝납니다. 중국에는 별도의 출원이 필요합니다. 중국에서 이미 인지도를 가진 유럽 브랜드와 관련된 주지상표 보호까지 유럽 권리자의 관점에서 정리했습니다.',
        'card_text': '유럽연합 상표는 중국에 미치지 않고, 6개월 우선권에는 서면 주장과 3개월 내 사본이 필요하며, 2027년부터 제21조가 미등록 주지상표에 클래스를 넘는 보호를 인정합니다.',
        'category': '국가별 가이드',
        'read_time': '약 9분',
        'tags': ['유럽 기업', '유럽연합 상표', '국가별 가이드'],
        'related': [
            ('{ACT}', '2027년 전에 해야 할 일'),
            ('{L}/madrid-vs-direct-filing-china.html', '마드리드와 직접 출원 비교'),
            ('{L}/hermes-trademark-china-case.html', '에르메스 중국 상표 사례'),
        ],
        'sections': [
            ('the-local-agent-rule', '먼저 확인할 현지 대리인 규정', """
<p class="leading-relaxed text-slate-300 mb-6">중국에 상주하는 주소나 영업소가 없는 외국 출원인은 중국 국내에 적법하게 설립·등록된 상표 대리 기관을 통해 출원해야 합니다. 2026년 상표법 제11조가 이 규정을 이어갑니다. 유럽 포트폴리오를 하나의 사내 팀이 관리하더라도 중국 출원은 현지 대리인이 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">중국에 지사를 두기만 해도 영업소가 있는 것으로 인정되지 않아 면제가 성립하지 않습니다. 유럽 출원인에게 특별한 대우도 없습니다. 위임장을 상비하고 출원인 명칭과 주소를 일치시키십시오. <a href="{L}/who-can-register-trademark-in-china.html">중국에서 상표를 등록할 수 있는 주체</a>도 보십시오.</p>
"""),
            ('eutm-does-not-extend', '유럽연합 상표는 중국에 미치지 않는다', """
<p class="leading-relaxed text-slate-300 mb-6">유럽연합 상표는 중국에 미치지 않으므로 별도의 중국 출원이 필요합니다. 중국은 선출원주의 국가이며, 수출이나 보도를 통한 인지도만으로는 권리가 되지 않습니다. 영문 표장과 중국어 표장은 별개의 권리입니다. 공식 중국어 명칭, 흔히 쓰이는 음역, 소비자가 스스로 붙인 애칭을 등록하십시오. 유사는 음·형·의로 판단됩니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">유럽의 명품·소비재 브랜드가 중국에서 겪은 분쟁은 널리 보도되어 있으며, 예를 들어 <a href="{L}/hermes-trademark-china-case.html">에르메스 사례</a>가 있습니다. 진입 전에 중국어 표기를 조사하십시오. <a href="{L}/overseas-r-mark-vs-china-trademark-registration.html">해외 등록상표가 중국에서 효력이 없는 이유</a>도 함께 보십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><a href="{L}/china-first-to-file-trademark-guide.html">선출원주의 가이드</a>와 <a href="{L}/coca-cola-chinese-name-trademark-china.html">중국어 명칭 사례</a>도 참고하십시오.</p></div>
"""),
            ('priority-madrid-and-direct', '우선권·마드리드·직접 출원', """
<p class="leading-relaxed text-slate-300 mb-6">파리 조약에 따라 국외에서 처음 출원한 상표는 그날부터 <strong>6개월 이내</strong>에 동일한 상표·동일한 상품 또는 서비스로 중국에 출원하며 우선권을 주장할 수 있습니다. 주장은 출원 시 서면으로 하고, 최초 출원 서류의 사본을 <strong>3개월 이내</strong>에 제출합니다(2026년 법 제29조, 구법 제25조에 해당). 국제박람회에서의 최초 사용도 6개월 우선권을 줍니다.</p>
<ul>
<li><strong>두 경로:</strong> 마드리드 제도로 중국을 지정하는 국제등록은 CNIPA가 중국법으로 심사하고 상품 표시를 현지 유사군·세부 구분에 맞춥니다. 직접 국내 출원은 CNIPA에 제출합니다.</li>
<li><strong>5년 의존:</strong> 국제등록은 처음 5년간 본국 기초등록에 의존합니다. 이른바 센터 어택 위험입니다.</li>
<li><strong>짧은 응답 기한:</strong> 중국을 지정한 사건의 WIPO 잠정 거절은 직권 거절이 <strong>15일</strong>, 이의에 기초한 거절이 <strong>30일</strong>이며 모두 통지 수령 시부터 기산하고, 보충 증거는 <strong>3개월 이내</strong>입니다(WIPO 공식 기한표).</li>
<li><strong>준비:</strong> 이 기한 안에 응답할 수 있도록 중국 대리인을 사전 위임해 둡니다.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">경로를 정하기 전에 <a href="{L}/madrid-vs-direct-filing-china.html">마드리드와 직접 출원 비교</a>를 보십시오.</p>
"""),
            ('apostille-and-documents', '아포스티유·언어·출원 서류', """
<p class="leading-relaxed text-slate-300 mb-6">출원 서류는 중국어로 작성합니다. 외국어 주체 자격 증명에는 중국어 번역본을 붙이고, 출원인 명칭과 주소는 유럽 언어 표기와 중국어 표기를 대응시킵니다. 공식 중국어 표기를 한 번 정해 계속 쓰십시오. 위임장은 보통 서명이나 직인으로 충분하므로 반드시 공증·인증이 필요하다고 단정하지 마십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">공문서 인증이 필요한 경우, 유럽연합 회원국은 헤이그 협약 체약국이며 이 협약은 <strong>2023년 11월 7일</strong> 중국에서 발효했습니다. 체약국에서 온 공문서는 기존의 외교부와 재외 공관을 거치는 2단계 영사 인증 대신 아포스티유로 충분합니다. 비체약국은 기존 영사 인증을 이용합니다. 아포스티유를 쓸 수 있는지는 서류 종류와 접수 기관의 요건에 따라 정해집니다. 대리인에게 당기 취급을 확인하고, 공식 규정에 없는 수수료나 소요 기간을 단정하지 마십시오.</p>
"""),
            ('article-21-and-the-2027-law', '제21조·2027년 법과 실무 대응', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 상표법은 <strong>2027년 1월 1일</strong> 시행됩니다. 제21조는 미등록 주지상표에 클래스를 넘는 보호를 인정합니다. 중국에서 이미 인지도를 갖추었지만 출원 이력이 부족한 유럽 브랜드에는 의미 있는 추가 수단이지만, 어디까지나 최후의 수단이며 등록을 대신하지는 않습니다. 인지도 입증에는 날짜가 있는 증거가 필요하고 결과도 직접 보유한 등록만큼 확실하지 않습니다. 개별 금지 조항에 대해 여기서 추측하지 않으며, 현행 조문과 실무는 대리인에게 확인하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">다른 개정도 같은 방향을 가리킵니다. 제36조는 이의신청 기간을 3개월에서 <strong>2개월</strong>로 줄이고, 제19조는 악의적 출원을 규제하며, 제57조는 <strong>3년 연속</strong> 사용되지 않은 상표를 CNIPA가 직권으로 취소할 수 있게 하고, 제55조는 사용허락의 등록과 법정 해제권을, 제46조는 양도의 실질심사를 정합니다. 조기 출원, 중국어 명칭 등록, 주 단위 감시, 사용 증거 보관이 기본입니다. <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>와 <a href="{ACT}">2027년 전 대응 목록</a>을 보십시오.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">유럽 출원인에게 특별한 대우는 없고, 기재 외의 수수료·성공률·소요 기간을 가정해서는 안 됩니다. 당기 공식 규정을 확인하십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제11조·제19조·제21조·제29조·제36조·제46조·제55조·제57조, 파리 조약, 헤이그 협약(2023년 11월 7일 중국 발효), WIPO 공식 기한표, CNIPA의 중국어 출원 실무. 절차는 시행조례 등에서 세분화될 수 있습니다. 당기 공식 요건을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>유럽에서 출원을 검토 중이신가요?</strong> <a href="/contact.html">유럽연합 상표에서 중국으로 이어지는 출원 계획, 중국어 명칭 조사, 아포스티유 서류에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },

    'kcase': {
        'slug': 'korean-brands-trademark-squatting-china-cases',
        'title': 'K-beauty에 쏠린 압력: 중국 내 한국 브랜드 상표 분쟁',
        'desc': '중국에서의 한국 브랜드 상표 분쟁 사례 연구. 2026년 지식재산 협력 양해각서, 보도된 유사 매장, 화장품 브랜드의 독점 사용허락 분쟁, 그리고 세 사례에 공통되는 출원·감시·증거 대책을 정리했습니다.',
        'lede': '중국에서 보도된 한국 브랜드의 세 가지 분쟁은 같은 교훈을 줍니다. 정책 양해각서, 유사 매장, 독점 사용허락 다툼. 모두 선출원주의 아래에서는 인지도만으로 권리가 되지 않는다는 한 점으로 돌아옵니다. 권리는 이르고 자료가 갖춰진 중국 등록에서 나옵니다.',
        'card_text': '2026년 지식재산 협력 양해각서가 실제로 무엇을 하는지, 보도된 유사 매장과 화장품 브랜드의 허락 분쟁이 무엇을 보여주는지, 그리고 그 교훈을 출원 계획으로 옮기는 예방 체크리스트.',
        'category': '사례 연구',
        'read_time': '약 9분',
        'tags': ['K-beauty', '상표 선점', '사례 연구'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', '상표 모니터링과 보호 전략'),
            ('{L}/china-first-to-file-trademark-guide.html', '중국 선출원주의 가이드'),
            ('{ACT}', '2027년 전에 해야 할 일'),
        ],
        'sections': [
            ('the-mou', '양해각서가 악의적 출원을 의제로 올렸다', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2026년 1월 5일</strong>, 한·중 정상회담을 계기로 한국 지식재산부(MOIP, 구 KIPO)와 CNIPA는 기존 양자 간 합의를 확충하는 지식재산 협력 양해각서에 서명했습니다. MOIP의 공식 영문 발표와 한국 언론 보도에 따르면 협력 범위는 모조품 대응, 심사에서의 AI·빅데이터 활용, 지식재산 거래·사업화를 포함합니다. 양측은 특히 악의적 상표 선점에 공동 대응하기로 뜻을 모았습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">이 각서가 무엇을 하고 무엇을 하지 않는지 정확히 짚을 필요가 있습니다. 협력 양해각서는 함께 일하는 틀을 정하는 것이지, 중국 출원법을 바꾸거나 한국 등록을 중국에 미치게 하거나 중국 권리로 가는 지름길을 만드는 것이 아닙니다. 중국에서의 보호는 여전히 CNIPA 등록에서 나옵니다. 이 발표는 사안이 높은 수준에서 주목받고 있다는 신호로 읽고, 출원을 대신하는 것으로 보지 마십시오.</p>
"""),
            ('lookalike-stores', '유사 매장과 소비자 혼동', """
<p class="leading-relaxed text-slate-300 mb-6">한국 언론 보도에 따르면 2026년 초, 중국 후난성 창사시에 「온리영」이라는 이름의 화장품 매장이 등장해 한국 올리브영의 명칭·로고·매장 색상·진열 방식을 모방했다는 지적이 나왔습니다. 성신여자대학교 서경덕 교수가 공개적으로 입장을 밝혔고, 관련 홍보 영상이 짧은 동영상 플랫폼에서 퍼졌습니다. 다른 분쟁에서는 중국 생활용품 브랜드가 해외 매장에서 한국을 연상시키는 문구를 써 출처 혼동을 빚었다는 지적이 있었습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">이는 재판상 인정이 아니라 보도된 지적이므로 위험 구도를 보여주는 예로 다루십시오. 상표의 요점은 매장명·로고·색상·진열이 서로 다른 요소라는 점입니다. 문자상표 출원이 도형이나 매장 외관을 반드시 포괄하지는 않고, 중국어 간판은 영문 명칭과 별개의 권리입니다. 영문만 등록한 브랜드는 문자상표 충돌이 뚜렷하지 않은 채 시각적 정체성을 모방당할 수 있습니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0">영문 상표와 함께 중국어 명칭·도형 상표·일반적인 음역을 등록하고, 시장에서 어떻게 제시했는지 날짜를 붙여 남기십시오. <a href="{L}/logo-vs-word-mark-china.html">로고와 문자상표의 차이</a>도 보십시오.</p></div>
"""),
            ('the-akf-licence-dispute', '화장품 브랜드의 독점 사용허락 분쟁', """
<p class="leading-relaxed text-slate-300 mb-6">공개 보도에 따르면 종심 판결에서 핵심 상표의 독점적 사용허락 계약이 유효하다고 인정되었습니다. 해당 브랜드는 한때 연 매출이 25억 위안에 육박했다고 보도됩니다. 출처가 공식 판결문이 아니라 중국 경제·업계 보도이므로 법원명·배상액·구체적 날짜를 확정 사실로 적지 않으며, 보도된 결론을 넘어 당사자에 대한 평가도 하지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">실무 교훈은 서류 정비입니다. 독점 사용허락은 뒤에 있는 권리 귀속 관계와 그 등록 방식에 따라 힘이 달라집니다. 외국 브랜드 권리자의 허락을 전제로 중국 사업을 세우는 경우, 바탕이 되는 중국 등록, 허락 계약, 등록 서류를 모순 없이 최신으로 유지해야 합니다. 2026년 법 제55조는 사용허락의 등록과 법정 해제권을, 제46조는 양도의 실질심사를 정하므로 양도·허락도 최초 출원만큼 주의가 필요합니다. <a href="{L}/china-trademark-assignment-licence-recordal.html">양도·사용허락 등록</a>을 보십시오.</p>
"""),
            ('what-these-cases-share', '세 사례에 공통되는 것', """
<p class="leading-relaxed text-slate-300 mb-6">서로 다른 세 구도가 같은 대책을 가리킵니다. 협력 양해각서는 정책 수준에서 악의적 출원을 다루고, 유사 매장은 시각적·중국어 정체성이 등록되어 있었는지를 시험하며, 허락 분쟁은 권리의 연결 고리가 문서화되어 있었는지를 시험합니다. 어느 것도 인지도만으로 풀리지 않습니다.</p>
<table>
<thead><tr><th>분쟁 유형</th><th>드러나는 것</th><th>효과가 있었을 대책</th></tr></thead>
<tbody>
<tr><td>악의적 선점 출원</td><td>중국은 선출원주의이며 출원 없는 인지도는 취약</td><td>조기 CNIPA 등록과 주 단위 감시</td></tr>
<tr><td>유사 매장 정체성</td><td>문자상표·도형상표·중국어 명칭은 별개 권리</td><td>표장 일체의 등록과 날짜 있는 제시 증거</td></tr>
<tr><td>독점 사용허락 다툼</td><td>허락에는 정리된 권리 귀속과 등록이 필요</td><td>등록·허락·등록 서류의 정합</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">결론은 운영으로 귀결됩니다. CNIPA 조기 출원, 중국어 명칭 등록, 지속적 감시, 사용 증거 보관입니다. 국경 간 전자상거래 요건과 세관 등록은 모두 중국 등록증을 전제하므로 출원이 권리 행사의 관문입니다. <a href="{L}/amazon-tmall-trademark-requirement-china.html">전자상거래 상표 요건</a>과 <a href="{L}/china-trademark-enforcement-routes-after-registration.html">등록 후 권리 행사 경로</a>도 보십시오.</p>
"""),
            ('a-preventive-checklist', '한국 브랜드를 위한 예방 체크리스트', """
<ol>
<li><strong>표장 일체를 출원하십시오.</strong> 영문 상표, 공식 중국어 명칭, 일반적인 음역, 소비자 애칭, 도형 상표는 각각 별개의 출원입니다.</li>
<li><strong>실제 상품·서비스로 클래스를 설계하십시오.</strong> K-beauty에서는 제3류(화장품)·제35류(소매)·제44류(미용 서비스)를 검토하는 것이 일반적 실무 예시입니다. 법정 요건은 아닙니다.</li>
<li><strong>쓸 수 있는 우선권을 쓰십시오.</strong> 국외 최초 출원일부터 6개월 내에 서면으로 파리 조약 우선권을 주장하고, 3개월 내에 최초 출원 서류의 사본을 제출합니다. 박람회 최초 사용도 6개월입니다.</li>
<li><strong>중국 대리인을 위임하십시오.</strong> 중국에 상주 주소나 영업소가 없는 외국 출원인은 대리인 경유가 필수이며, 지사만 두는 것으로는 면제되지 않습니다.</li>
<li><strong>주 단위로 감시하십시오.</strong> 2027년 1월 1일부터 이의신청 기간이 2개월이므로 분기별 확인으로는 부족합니다.</li>
<li><strong>사용 증거를 보관하십시오.</strong> 제57조는 3년 사용되지 않은 상표를 CNIPA가 직권으로 취소할 수 있게 합니다.</li>
<li><strong>서류를 최신으로 유지하십시오.</strong> 번역본, 명칭과 주소의 대응, 위임장, 허락·양도 등록.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">한국 출원인에게 특별한 대우는 없고, 기재 외의 수수료·성공률·소요 기간을 가정해서는 안 됩니다. 당기 공식 규정을 대리인에게 확인하십시오. <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>와 <a href="{ACT}">2027년 전 대응 목록</a>도 활용하십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">출처: 2026년 1월 5일 지식재산 협력 양해각서에 관한 MOIP 공식 영문 발표, 한국 주요 언론 보도, 유사 매장을 둘러싼 한국 언론 보도(재판상 인정이 아닌 보도된 지적), 화장품 브랜드의 독점 사용허락 분쟁에 관한 중국 경제·업계 보도(공개 보도이며 법원명·배상액·구체적 날짜를 확정 사실로 적지 않음), 『중화인민공화국 상표법(2026년 개정)』(2027년 1월 1일 시행), WIPO 자료. 수치와 사례 세부는 공식 판결문이 아닌 보도에 근거합니다. 본 글은 일반 정보이며 법률 자문이 아닙니다. 당기 공식 규정을 확인하십시오.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>중국에서 한국 브랜드 모방이 걱정되시나요?</strong> <a href="/contact.html">조기 CNIPA 출원, 중국어 명칭 조사, 감시 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },

 }},
}
