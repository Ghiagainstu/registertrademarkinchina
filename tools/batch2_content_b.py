# -*- coding: utf-8 -*-
"""Batch 2 content (part B): P1-5 enforcement routes, P1-6 overseas R mark,
P1-7 assignment & licence recordal. EN/JA/KO.
"""

CONTENT = {}

CONTENT['en'] = {'articles': {
    'enforce': {
        'slug': 'china-trademark-enforcement-routes-after-registration',
        'title': 'After Registration: 4 Enforcement Routes in China (AMR, Customs, Platforms, Courts)',
        'desc': "A Chinese trademark certificate is the entry ticket to enforcement, not the end of the work. Compare administrative, customs, platform and court routes, their prerequisites and when each one pays off.",
        'lede': "Registration gives you standing. Enforcement comes from four separate channels — market regulators, Customs, e-commerce platforms and the courts — each with different prerequisites and different outputs.",
        'card_text': "Administrative raids, customs recordal, platform takedowns and civil litigation compared: prerequisites, timing and what each route can actually deliver.",
        'category': 'Lifecycle',
        'read_time': '11 min read',
        'tags': ['enforcement', 'customs recordal', 'platform takedown'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', 'Trademark Monitoring and Protection'),
            ('{L}/china-trademark-non-use-cancellation-evidence.html', 'Use-Evidence File for 2027'),
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Trademark Requirements for Tmall and Amazon'),
        ],
        'sections': [
            ('one-right-four-channels', 'One Right, Four Channels', """
<p class="leading-relaxed text-slate-300 mb-6">A CNIPA registration is a precondition for almost every enforcement action in China: platform complaint systems, Customs recordal and administrative complaints all ask for the Chinese registration certificate or a recorded licence. An overseas registration, a pending application or a distributor's authorisation letter does not substitute for it.</p>
<table>
<thead><tr><th>Route</th><th>Best for</th><th>Prerequisite</th><th>Typical output</th></tr></thead>
<tbody>
<tr><td><strong>Administrative (AMR)</strong></td><td>Clear-cut counterfeits in physical markets, local factories and wholesale stalls</td><td>Registration certificate, evidence, complaint drafted in Chinese</td><td>Inspection, seizure, administrative penalty; generally faster and cheaper than litigation</td></tr>
<tr><td><strong>China Customs (GACC)</strong></td><td>Counterfeit imports/exports, OEM leakage, unauthorised cross-border shipments</td><td>Recordal of the registered mark with the General Administration of Customs</td><td>Ex officio detention of suspect shipments and notice to the rights holder</td></tr>
<tr><td><strong>Platform IPP</strong></td><td>Infringing listings on e-commerce and social-commerce platforms</td><td>Brand enrolment with a CNIPA certificate or a recorded licence</td><td>Listing removal, repeat-infringer sanctions; reactive, requires your own monitoring</td></tr>
<tr><td><strong>Civil litigation</strong></td><td>High-value, repeat or contested infringement; damages and precedent</td><td>Notarised evidence, local counsel, standing as registrant or exclusive licensee</td><td>Injunction, damages and destruction of infringing goods</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The 2026 Trademark Law strengthens the backdrop: Article 75 formalises two-way referral between administrative enforcement and criminal authorities; Article 76 lets enforcement bodies preserve evidence at risk of being lost; Article 77 expressly includes reasonable costs of stopping infringement in damages.</p>
"""),
            ('customs-recordal', 'Customs Recordal: The Highest-Leverage Step After Registration', """
<p class="leading-relaxed text-slate-300 mb-6">Customs protection has two modes. Without a recordal, Customs generally acts only on a specific application supported by evidence — which requires you to know about a shipment in advance. With a recordal, Customs can suspend clearance of suspect goods on its own initiative and notify the rights holder. <strong>Recordal is the precondition for that active mode.</strong></p>
<table>
<thead><tr><th>Item</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>Decision</td><td>Within 30 working days of receiving a complete application</td></tr>
<tr><td>Validity</td><td>10 years from approval; if the trademark's remaining term is shorter, the recordal follows the trademark term</td></tr>
<tr><td>Renewal</td><td>Apply in the 6 months before expiry; decision within 10 working days</td></tr>
<tr><td>Changes</td><td>Apply to amend the recordal within 30 working days of any change to the recorded particulars</td></tr>
<tr><td>Foreign rights holders</td><td>File through a domestic office or a Chinese agent</td></tr>
<tr><td>Fees</td><td>Fee schedules and any suspension of fees are set by GACC — confirm the current position rather than relying on third-party summaries</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">A typical application covers the registration certificate and its status, rights-holder identity and authorisation, photos of genuine goods and packaging, details of legitimate goods (names, origin, ports, importers, exporters, features, price), and known infringer or suspect-shipment intelligence. Foreign-language documents need a Chinese translation. Keep the list of authorised manufacturers and importers current: if it goes stale, legitimate shipments can be delayed while a counterfeit clears.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Practical point:</strong> Customs protection is generally tied to the mark as recorded. Brands using a main mark, sub-brands and defensive marks often need separate recordals for each, and should check that the goods listed in the original trademark application actually cover the products being shipped.</p></div>
"""),
            ('platform-enforcement', 'Platform Takedowns: Fast, Reactive and Evidence-Driven', """
<p class="leading-relaxed text-slate-300 mb-6">Major e-commerce and content platforms operate intellectual property protection systems. Enrolment requires proof of rights — in practice a CNIPA registration certificate or a recorded licence. Once enrolled, complaints are assessed quickly and often by systems rather than lawyers, so the quality of the submission determines the outcome.</p>
<ul>
<li>Identify the specific listing by URL and product ID, not by describing the seller generally.</li>
<li>State the registration number and attach the certificate.</li>
<li>Name the precise infringement basis: identical mark, counterfeit goods, unauthorised product imagery or copy, or a false claim of authorised-dealer status.</li>
<li>Attach annotated comparison evidence: listing screenshots against genuine product and packaging.</li>
<li>Expect counter-notifications and repeat sellers under new store names; sustained enforcement is a programme, not a one-off cleanup.</li>
<li>Document who holds complaint authority when a distributor or agency operates the store, so action can be taken in the brand's own name.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">Inaccurate or abusive complaints can be penalised by the platforms. Keep the evidence file and the escalation rules in one place, alongside the <a href="{L}/china-trademark-non-use-cancellation-evidence.html">use-evidence archive</a> — the same dated screenshots and sales records serve both purposes.</p>
"""),
            ('choosing-a-route', 'Choosing a Route: A Decision Table', """
<table>
<thead><tr><th>Situation</th><th>First move</th><th>Then</th></tr></thead>
<tbody>
<tr><td>Counterfeit listings appear on one platform</td><td>Platform complaint with a complete evidence pack</td><td>Escalate to AMR if the seller reappears repeatedly</td></tr>
<tr><td>Suspect goods are being exported from a factory</td><td>Customs recordal plus AMR action at source</td><td>Civil claim if the volumes justify damages</td></tr>
<tr><td>A distributor keeps selling after termination</td><td>AMR complaint + platform takedowns; check licence recordal status</td><td>Litigation for contract and infringement claims</td></tr>
<tr><td>Large-scale, organised counterfeiting</td><td>Notarised evidence buy, then civil action with preservation</td><td>Criminal referral through the administrative-criminal interface (Art. 75)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The common failure is treating these as alternatives. In practice they are sequential: monitoring finds the problem, recordal and evidence make action possible, platform complaints remove the visible listings, and administrative or court action changes the infringer's economics.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Articles 75, 76 and 77 of the <em>Trademark Law of the PRC (2026 Revision)</em> (CNIPA, 26 June 2026); CNIPA <em>Main Contents of the Revision</em> (10 July 2026); official and government-published guidance on intellectual property Customs recordal (30-working-day decision, 10-year validity, 6-month renewal window, 30-working-day change window). Platform complaint mechanics and fee schedules are operational practice and change frequently — verify against each platform's current IP portal and GACC announcements before filing. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Want an enforcement plan built around your portfolio?</strong> <a href="/contact.html">Talk to our team</a> about recordal, platform enrolment and complaint templates.</p></div>
"""),
        ],
    },
    'rmark': {
        'slug': 'overseas-r-mark-vs-china-trademark-registration',
        'title': 'An Overseas R Mark Is Not a Chinese Registration: Platform Entry vs Legal Ownership',
        'desc': "Some China e-commerce onboarding routes accept an overseas registration as an eligibility document. Platform complaints, Customs recordal and enforcement still require a CNIPA certificate. Understand the two-track logic before you launch.",
        'lede': "An overseas R mark can open a storefront conversation. It cannot found an enforcement action in China. Confusing the two is one of the most expensive pre-launch mistakes foreign brands make.",
        'card_text': "The entry ticket is not the title deed: a side-by-side comparison of onboarding documents, enforcement prerequisites, authorisation chains and the handover points.",
        'category': 'Lifecycle',
        'read_time': '9 min read',
        'tags': ['cross-border e-commerce', 'platform onboarding', 'CNIPA certificate'],
        'related': [
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Selling on Amazon China or Tmall'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '4 Enforcement Routes After Registration'),
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
        ],
        'sections': [
            ('two-tracks', 'Two Tracks That Are Often Confused', """
<table>
<thead><tr><th></th><th>Platform onboarding</th><th>Legal rights in China</th></tr></thead>
<tbody>
<tr><td>Question answered</td><td>"May I open this store / list this brand?"</td><td>"Do I own an enforceable right in this territory?"</td></tr>
<tr><td>Who decides</td><td>The platform's merchant-review team, under its own changing rules</td><td>CNIPA, the courts, Customs and market regulators</td></tr>
<tr><td>Typical document</td><td>Registration or application evidence from a home jurisdiction, brand authorisation chain, entity documents</td><td><strong>CNIPA registration certificate</strong> (or a recorded licence)</td></tr>
<tr><td>What it unlocks</td><td>A storefront, listing rights, category access</td><td>Platform complaints, Customs recordal, administrative complaints, litigation</td></tr>
<tr><td>Failure mode</td><td>Application rejected or store frozen</td><td>A squatter owns your name and you have no standing to complain</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Some cross-border onboarding routes accept evidence of an overseas registration as part of the eligibility package. That is a <strong>commercial admission decision made by the platform</strong>, not a determination of Chinese trademark rights. China remains a first-to-file jurisdiction: a foreign registration has no legal effect in China.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Do not quote third-party rule summaries as authority.</strong> Eligibility lists, deposit amounts, permitted authorisation-chain depth and required supporting documents change frequently and differ by platform and category. Always verify against the platform's current merchant onboarding announcement before budgeting or signing a distributor agreement.</p></div>
"""),
            ('handover-points', 'Where the Two Tracks Collide', """
<ol>
<li><strong>Brand enrolment in a platform IP portal</strong> usually requires a CNIPA certificate or a recorded licence. An overseas certificate may get the store open but leaves no standing to file an infringement complaint.</li>
<li><strong>Customs recordal</strong> requires a registered Chinese trademark (service marks excluded for this purpose); a home-country registration is not recordable.</li>
<li><strong>Administrative complaints and litigation</strong> are assessed against the Chinese registration and the designated goods.</li>
<li><strong>Authorisation chains</strong> are scrutinised in both tracks, but for different reasons: the platform wants a documented chain to the store operator; CNIPA and the courts care about who actually owns the mark and whether a licence was recorded.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">The consequence is a familiar trap: a brand launches using an overseas mark, a squatter registers the Chinese name, and the brand then cannot remove the infringing listings because it has no CNIPA certificate in its own name. See <a href="{L}/china-trademark-enforcement-routes-after-registration.html">the four enforcement routes</a> for the downstream consequences.</p>
"""),
            ('documents', 'Documents: Apostille, Legalisation and the Power of Attorney Trap', """
<p class="leading-relaxed text-slate-300 mb-6">Foreign-language corporate documents, authorisations and certificates often need translation and, depending on the receiving body, some form of authentication. China acceded to the <em>Hague Convention Abolishing the Requirement of Legalisation for Foreign Public Documents</em>, which entered into force for China on <strong>7 November 2023</strong>. For public documents from other contracting states, an <strong>Apostille</strong> replaces the old "dual legalisation" of foreign ministry plus consular certification; documents from non-contracting states still follow the traditional consular route.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two cautions matter in practice. First, whether a document is a "public document" covered by the Convention — and whether the receiving platform or authority actually requires authentication — depends on the document and the specific procedure. Second, a <strong>power of attorney for a CNIPA trademark application is generally a simple signed authorisation</strong>; it should not be assumed to need consular legalisation just because a platform's authorisation-chain package does. Ask your Chinese agent and the platform separately, and budget the lead time only for the documents that genuinely need it.</p>
"""),
            ('action-list', 'Pre-Launch Action List', """
<ol>
<li><strong>File the CNIPA application first</strong> — the Latin mark, the official Chinese name, common transliterations and consumer-coined nicknames, in the classes and sub-classes you will actually sell in.</li>
<li><strong>Do not wait for the certificate to plan enforcement.</strong> Map the platform IP portals and Customs recordal requirements while the application is pending, and assemble the evidence pack in parallel.</li>
<li><strong>Check the current onboarding rules</strong> for each platform and category, and keep a dated copy of the announcement you relied on.</li>
<li><strong>Document the authorisation chain</strong> from brand owner to store operator, including translation and any required Apostille or legalisation.</li>
<li><strong>On registration, enrol in platform IP portals and record with Customs</strong>, then link both to a monitoring programme with a named owner.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">For the eligibility side of the conversation, see <a href="{L}/amazon-tmall-trademark-requirement-china.html">Selling on Amazon China or Tmall? You Need a Trademark First</a>. For the rights side, <a href="{ACT}">start with the 2027 action list</a>.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Ministry of Foreign Affairs announcement on the entry into force of the Apostille Convention in China (23 October 2023) and State Council reporting of 7 November 2023; Articles 2 and 71 of the <em>Trademark Law of the PRC (2026 Revision)</em>; official guidance on Customs recordal prerequisites. Platform onboarding and IP-portal rules are commercial policies, not statutes, and change without notice — this article intentionally states no deposit figures, authorisation-chain limits or document lists for a specific platform. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Launching in China with an overseas mark only?</strong> <a href="/contact.html">Get a CNIPA filing and enforcement readiness check</a> before the store goes live.</p></div>
"""),
        ],
    },
    'assignment': {
        'slug': 'china-trademark-assignment-licence-recordal',
        'title': 'Trademark Assignment & Licence Recordal in China: Getting Your Mark Back from a Factory',
        'desc': "When a manufacturer, distributor or agent registers your mark first, assignment is often simpler than litigation. What the 2026 law changes about transfer review, what licence recordal actually does, and four myths to discard.",
        'lede': "A foreign company can own a Chinese trademark, an application under examination can be assigned, and a signed assignment statement is usually all the transfer needs. The 2026 law adds one important new caveat.",
        'card_text': "Foreign entities can hold Chinese marks; assignment does not require abandoning and refiling; Article 46 adds a substantive review of transfers. Plus licence recordal and the licensor's new statutory termination right.",
        'category': 'Lifecycle',
        'read_time': '10 min read',
        'tags': ['assignment', 'licence recordal', 'OEM dispute'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', 'If Someone Registered Your Mark First'),
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '4 Enforcement Routes After Registration'),
        ],
        'sections': [
            ('four-myths', 'Four Myths That Keep Brands Stuck', """
<p class="leading-relaxed text-slate-300 mb-6">When a factory, distributor or former agent has registered the mark, the counterparty often insists that a transfer is impossible. International practitioners consistently report the same four claims — and none of them is correct:</p>
<ol>
<li><strong>"Only Chinese entities can own a Chinese trademark."</strong> Foreign companies own a large number of Chinese registrations. There is no nationality restriction on ownership.</li>
<li><strong>"The only route is to abandon the mark and refile."</strong> That is costly, slow and exposes a gap in which a third party can file. The normal route is a filed assignment.</li>
<li><strong>"An application under examination cannot be assigned."</strong> It can — although if the application is later refused, the assignee receives nothing.</li>
<li><strong>"Both parties need consular-certified corporate documents."</strong> Identity evidence is required for both assignor and assignee, but a trademark assignment does not generally require embassy legalisation of those documents.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">The transfer itself is typically documented by an assignment statement filed with CNIPA together with identity evidence. The hard part is usually commercial — negotiating the terms with the holder — not procedural. See also <a href="{L}/trademark-registered-by-someone-else-china.html">the four recovery options</a>.</p>
"""),
            ('article-46', 'The 2026 Caveat: Transfers Are No Longer Purely Formal', """
<p class="leading-relaxed text-slate-300 mb-6">Article 46 of the revised Trademark Law retains the assignment rule and adds a third paragraph: a transfer that <strong>is likely to cause confusion or has other adverse effects shall not be approved</strong>. That is a substantive review layer which did not appear in the 2019 provision.</p>
<p class="leading-relaxed text-slate-300 mb-6">For a brand buying back a squatted mark, this means the assignment document should do more than say "transferred". It should explain the relationship between the parties, the business rationale, what happens to related or similar marks held by the assignor, and how the goods and channels will be separated so that consumers are not confused. Where the holder owns a family of lookalike marks, the agreement should require assignment or cancellation of the whole family rather than just the one mark you noticed.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 47 adds a parallel rule for collective and certification marks: the assignee must have the relevant qualifications and supervisory capacity. Article 53 also matters in dispute planning — an invalidation generally has no retroactive effect on assignment or licence contracts already performed, except where the registrant acted in bad faith.</p>
"""),
            ('licence-recordal', 'Licence Recordal and What It Actually Does', """
<table>
<thead><tr><th>Item</th><th>Rule under the 2026 law (Art. 55)</th></tr></thead>
<tbody>
<tr><td>Quality control</td><td>The licensor must supervise the quality of the licensee's goods; the licensee must guarantee that quality</td></tr>
<tr><td>Statutory termination</td><td>If the licensee fails to meet its quality obligations, <strong>the licensor may terminate the licence</strong> — a statutory right that does not depend on a termination clause being written into the contract</td></tr>
<tr><td>Marking</td><td>Goods bearing a licensed mark must indicate the licensee's name and the place of origin</td></tr>
<tr><td>Recordal</td><td>The licence must be filed with the trademark authority and published; <strong>an unrecorded licence cannot be asserted against a bona fide third party</strong></td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Recordal is therefore not a formality: it is what makes the licensee's position defensible against third parties, and it is frequently requested by platform IP portals when a licensee rather than the brand owner operates the store. It also creates the documented licence relationship needed if the licensee's sales are later relied on as <a href="{L}/china-trademark-non-use-cancellation-evidence.html">use evidence</a> against a non-use cancellation.</p>
<p class="leading-relaxed text-slate-300 mb-6">Licence structures are commonly described as exclusive, sole or non-exclusive. Whichever is used, define territory, duration, goods, sub-licensing, quality inspection rights, audit rights, what happens to stock and packaging on termination, and dispute resolution.</p>
"""),
            ('decision-table', 'Assignment, Licence, Invalidation or Refiling?', """
<table>
<thead><tr><th>Route</th><th>When it fits</th><th>Main trade-off</th></tr></thead>
<tbody>
<tr><td>Assignment / buy-back</td><td>The holder is identifiable and willing to deal; launch date is fixed</td><td>Fastest, but rewards the behaviour and needs Article 46-ready documentation</td></tr>
<tr><td>Licence + recordal</td><td>You need immediate market access while ownership is disputed</td><td>Does not give you ownership; recordal and quality terms are essential</td></tr>
<tr><td>Invalidation / opposition</td><td>Bad faith and prior rights are well evidenced; no urgency</td><td>Strongest legal outcome, longest timeline</td></tr>
<tr><td>Filing a new, distinct mark</td><td>The original mark is commercially expendable</td><td>Rebranding cost; the old mark remains with the squatter</td></tr>
</tbody>
</table>
"""),
            ('prevention', 'Preventing the Problem in the OEM Relationship', """
<ul>
<li>File in China <strong>before</strong> disclosing the brand, packaging or product roadmap to a factory or distributor.</li>
<li>Put an express no-self-registration clause in the manufacturing agreement, with a duty to assign anything filed and a meaningful liquidated damages figure.</li>
<li>Allocate end-of-term stock, moulds, semi-finished goods and packaging — each category needs its own disposal rule and deadline.</li>
<li>Define authorised production volume, reconciliation duties and audit rights; a presumption against the factory for unexplained units is more useful than a general promise.</li>
<li>Keep the licence and assignment documentation consistent with the goods actually registered, and record changes of name, address and agent promptly (Art. 57 imposes penalties for uncorrected changes to registered particulars).</li>
</ul>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Articles 46, 47, 53, 55 and 57 of the <em>Trademark Law of the PRC (2026 Revision)</em> (CNIPA, 26 June 2026) and CNIPA <em>Main Contents of the Revision</em> (10 July 2026); practitioner guidance on assignments of Chinese trademarks to foreign entities and OEM agreement clauses. Document requirements and examination practice may be refined by the revised Implementing Regulations. This is general information, not legal advice; a live dispute needs advice on its specific facts.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Recovering a mark registered by a factory?</strong> <a href="/contact.html">Talk to our team</a> about assignment documentation, recordal and an Article 46-ready filing.</p></div>
"""),
        ],
    },
}}

CONTENT['ja'] = {'articles': {
    'enforce': {
        'slug': 'china-trademark-enforcement-routes-after-registration',
        'title': '登録後に使える4つの権利行使ルート（市場監督・税関・プラットフォーム・裁判所）',
        'desc': '中国の商標登録証は権利行使の「入場券」であり、ゴールではありません。行政・税関・プラットフォーム・裁判所の4ルートを前提条件と成果から比較します。',
        'lede': '登録によって権利行使の資格が得られます。実際の執行は、市場監督部門、税関、ECプラットフォーム、裁判所という別々の4経路で行われ、それぞれ前提条件も成果も異なります。',
        'card_text': '行政摘発、税関記録、プラットフォーム削除、民事訴訟を、必要書類・所要時間・得られる結果で比較しました。',
        'category': 'ライフサイクル',
        'read_time': '約11分',
        'tags': ['権利行使', '税関記録', 'プラットフォーム削除'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', '商標モニタリングと保護戦略'),
            ('{L}/china-trademark-non-use-cancellation-evidence.html', '2027年向け使用証拠ファイル'),
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Tmall・Amazonの商標要件'),
        ],
        'sections': [
            ('one-right-four-channels', '一つの権利、四つの経路', """
<p class="leading-relaxed text-slate-300 mb-6">中国におけるほぼすべての権利行使は、CNIPAの登録証（または届出済みライセンス）を前提とします。プラットフォームの知財ポータル、税関記録、行政苦情のいずれも中国の登録証を求めます。海外登録、審査中の出願、販売店の授権書では代用できません。</p>
<table>
<thead><tr><th>経路</th><th>向いている場面</th><th>前提条件</th><th>得られる結果</th></tr></thead>
<tbody>
<tr><td><strong>行政（市場監督）</strong></td><td>実店舗・卸売市場・地元工場の明白な模倣品</td><td>登録証、証拠、中国語の苦情書</td><td>立入検査、差押え、行政処罰。訴訟より迅速かつ低コスト</td></tr>
<tr><td><strong>税関（GACC）</strong></td><td>模倣品の輸出入、OEMからの流出、無断の越境出荷</td><td>登録商標の税関総署への記録（備案）</td><td>疑わしい貨物の職権による通関停止と権利者への通知</td></tr>
<tr><td><strong>プラットフォームIPP</strong></td><td>EC・ソーシャルコマース上の侵害出品</td><td>CNIPA登録証または届出済みライセンスによるブランド登録</td><td>出品削除、反復侵害者への制裁。検知は自社責任の受動的仕組み</td></tr>
<tr><td><strong>民事訴訟</strong></td><td>高額・反復・係争性の高い侵害、損害賠償と先例</td><td>公証済み証拠、現地弁護士、登録人または独占ライセンシーとしての適格</td><td>差止め、損害賠償、侵害品の廃棄</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">2026年法は基盤を強化しています。第75条は行政執行と刑事機関の双方向移送を明文化し、第76条は滅失のおそれのある証拠の先行登記保存を認め、第77条は侵害停止に要した合理的費用を賠償に含めることを明記しました。</p>
"""),
            ('customs-recordal', '税関記録：登録後の最も費用対効果が高い一手', """
<p class="leading-relaxed text-slate-300 mb-6">税関保護には二つのモードがあります。記録がなければ、具体的な申請と証拠に基づく対応が中心で、出荷を事前に把握している必要があります。記録があれば、税関は職権で疑わしい貨物の通関を停止し、権利者に通知できます。<strong>能動的保護の前提条件が記録です。</strong></p>
<table>
<thead><tr><th>項目</th><th>規則</th></tr></thead>
<tbody>
<tr><td>決定</td><td>全部の申請書類を受領してから30営業日以内</td></tr>
<tr><td>有効期間</td><td>核准日から10年。商標の残存期間が短い場合は商標の期間に従う</td></tr>
<tr><td>更新</td><td>満了前6ヶ月以内に申請、決定は10営業日以内</td></tr>
<tr><td>変更</td><td>記録事項に変更が生じた日から30営業日以内に変更申請</td></tr>
<tr><td>外国権利者</td><td>国内拠点または中国の代理人を通じて申請</td></tr>
<tr><td>費用</td><td>料金およびその停止の有無は税関総署の告示による。第三者のまとめではなく当期の公式情報を確認</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">申請には通常、登録証とその権利状態、権利者の身分証明と委任状、正規品・包装の写真、正規品の情報（名称、産地、通関地、輸入者・輸出者、特徴、価格）、既知の侵害者・疑わしい出荷の情報を含めます。外国語資料には中国語訳を添付します。正規の製造者・輸入者リストは最新に保ってください。古いままだと正規品が止まり、模倣品が通るという逆転が起きます。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>実務ポイント：</strong>税関保護は原則として記録された商標単位です。メイン商標、サブブランド、防御商標を併用する場合は個別の記録が必要になることが多く、当初出願の指定商品が実際の出荷品をカバーしているかも確認が必要です。</p></div>
"""),
            ('platform-enforcement', 'プラットフォーム削除：速いが受動的、証拠がすべて', """
<p class="leading-relaxed text-slate-300 mb-6">主要なEC・コンテンツプラットフォームは知財保護システムを運用しています。登録には権利証明、実務上はCNIPA登録証または届出済みライセンスが必要です。申立ては短期間で、しばしば弁護士ではなくシステムで審査されるため、提出物の質が結果を左右します。</p>
<ul>
<li>販売者を一般的に描写するのではなく、URLと商品IDで個別の出品を特定する。</li>
<li>登録番号を明記し、登録証を添付する。</li>
<li>侵害根拠を具体的に特定する（同一標識、模倣品、無断の商品画像・説明、正規代理店を装う表示など）。</li>
<li>出品画面と正規品・包装を並べ、差分を注記した比較証拠を添付する。</li>
<li>反通知や、店名を変えて再登場する反復侵害者を想定する。継続的なプログラムです。</li>
<li>販売店や代理店が店舗を運営する場合、ブランド名義で行動できるよう申立て権限を文書化する。</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">不正確または濫用的な申立てはプラットフォームから制裁を受けることがあります。証拠ファイルとエスカレーション規則は<a href="{L}/china-trademark-non-use-cancellation-evidence.html">使用証拠ファイル</a>と同じ場所に集約すると、同じ日付入り画面と販売記録を両方に使えます。</p>
"""),
            ('choosing-a-route', '経路の選び方：判断表', """
<table>
<thead><tr><th>状況</th><th>初手</th><th>次の一手</th></tr></thead>
<tbody>
<tr><td>一つのプラットフォームに模倣出品</td><td>完全な証拠パックでプラットフォーム申立て</td><td>再登場を繰り返すなら市場監督へエスカレーション</td></tr>
<tr><td>工場から疑わしい貨物が輸出されている</td><td>税関記録＋発生源での行政対応</td><td>数量が見合えば民事で損害賠償請求</td></tr>
<tr><td>契約終了後も販売店が販売を継続</td><td>行政苦情＋プラットフォーム削除、ライセンス届出の状態を確認</td><td>契約・侵害を組み合わせた訴訟</td></tr>
<tr><td>組織的・大規模な模倣</td><td>公証による証拠保全のうえ保全付き民事提訴</td><td>第75条の行刑連携による刑事移送</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">よくある失敗は、これらを代替案として扱うことです。実際は連続しています。監視が問題を見つけ、記録と証拠が行動を可能にし、プラットフォーム申立てが可視的な出品を消し、行政・裁判が侵害者の経済計算を変えます。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第75条・第76条・第77条（CNIPA、2026年6月26日）、CNIPA『商標法改正の主要内容』（2026年7月10日）、知的財産の税関記録に関する官公庁公表資料（30営業日の決定、10年有効、満了前6ヶ月更新、30営業日以内の変更）。プラットフォームの申立て実務と料金表は運用方針であり頻繁に変わるため、各プラットフォームの当期の知財ポータルおよび税関総署の告示で確認してください。本記事は一般情報であり法的助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>ポートフォリオに合わせた執行計画が必要ですか？</strong> <a href="/contact.html">税関記録、プラットフォーム登録、申立て雛形についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'rmark': {
        'slug': 'overseas-r-mark-vs-china-trademark-registration',
        'title': '海外のRマークは中国の登録ではない：プラットフォーム入場資格と権利の所有',
        'desc': '越境ECの出店審査で海外登録証が受理されることがありますが、プラットフォーム内申立て・税関記録・権利行使にはCNIPA登録証が必要です。出店前に二つの軌道を整理します。',
        'lede': '海外のRマークは出店の扉を開けますが、中国での権利行使の根拠にはなりません。この二つを混同することが、出店前の最も高くつく失敗です。',
        'card_text': '「入場券」と「権利証」の比較：出店書類、執行の前提条件、授権チェーン、そして両者が交差する地点。',
        'category': 'ライフサイクル',
        'read_time': '約9分',
        'tags': ['越境EC', '出店審査', 'CNIPA登録証'],
        'related': [
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Tmall・Amazon中国で販売するには'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '登録後の4つの執行ルート'),
            ('{HUB}', '旧法・新法の条項対比'),
        ],
        'sections': [
            ('two-tracks', '混同されやすい二つの軌道', """
<table>
<thead><tr><th></th><th>プラットフォーム出店</th><th>中国における法的権利</th></tr></thead>
<tbody>
<tr><td>答える問い</td><td>「この店舗・ブランドを出店させてよいか」</td><td>「この地域で執行可能な権利を持っているか」</td></tr>
<tr><td>判断主体</td><td>プラットフォームの出店審査部門（自社規則、随時変更）</td><td>CNIPA、裁判所、税関、市場監督部門</td></tr>
<tr><td>典型書類</td><td>本国での登録・出願証跡、ブランド授権チェーン、法人資料</td><td><strong>CNIPA登録証</strong>（または届出済みライセンス）</td></tr>
<tr><td>解放されるもの</td><td>店舗、出品権、カテゴリー</td><td>プラットフォーム申立て、税関記録、行政苦情、訴訟</td></tr>
<tr><td>失敗様式</td><td>出店拒否・店舗凍結</td><td>ハイジャッカーが自社名を保有し、申立て資格がない</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">越境出店の一部ルートでは、本国登録の証跡が審査資料として受理されます。しかしそれは<strong>プラットフォームの商業的な入場判断</strong>であり、中国の商標権の認定ではありません。中国は先願主義であり、外国登録は中国で効力を持ちません。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>第三者の規則まとめを根拠にしないでください。</strong>必要書類、保証金、許される授権チェーンの階層、追加資料はプラットフォーム・カテゴリー別に頻繁に変わります。予算計上や販売店契約の締結前に、必ず当該プラットフォームの当期の出店公告で確認してください。</p></div>
"""),
            ('handover-points', '二つの軌道が衝突する地点', """
<ol>
<li><strong>プラットフォーム知財ポータルのブランド登録</strong>は通常CNIPA登録証または届出済みライセンスを要します。海外証跡で出店できても、侵害申立ての適格は生じません。</li>
<li><strong>税関記録</strong>は中国で登録された商標（この目的では役務商標を除く）が前提で、本国登録は記録できません。</li>
<li><strong>行政苦情・訴訟</strong>は中国の登録と指定商品を基準に判断されます。</li>
<li><strong>授権チェーン</strong>は両方で審査されますが目的が異なります。プラットフォームは店舗運営者までの鎖を求め、CNIPA・裁判所は誰が商標を所有し、ライセンスが届出済みかを問題にします。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">結果として典型的な罠が生じます。海外商標で出店し、ハイジャッカーが中国語名を登録し、自社名義のCNIPA登録証がないため侵害出品を削除できない、というものです。下流の影響は<a href="{L}/china-trademark-enforcement-routes-after-registration.html">4つの執行ルート</a>をご覧ください。</p>
"""),
            ('documents', '書類：アポスティーユ、領事認証、委任状の落とし穴', """
<p class="leading-relaxed text-slate-300 mb-6">外国語の法人資料、授権書、証明書には翻訳が必要で、受領側によっては何らかの認証が求められます。中国は『外国公文書の認証要求を廃止する条約』に加入し、<strong>2023年11月7日</strong>に中国で発効しました。他の締約国の公文書は<strong>アポスティーユ（附加証明書）</strong>が従来の「外務省認証＋領事認証」の二重認証に代わり、非締約国の文書は従来どおり領事認証の経路をたどります。</p>
<p class="leading-relaxed text-slate-300 mb-6">実務上は二つの注意点があります。第一に、その文書が条約上の「公文書」に当たるか、そして受領側が実際に認証を要求するかは、文書と手続ごとに異なります。第二に、<strong>CNIPAへの商標出願の委任状は通常、署名済みの単純な授権書で足り</strong>、プラットフォームの授権チェーン一式に認証が必要だからといって、当然に領事認証が必要とは限りません。中国代理人とプラットフォームに別々に確認し、本当に必要な文書についてのみリードタイムを計上してください。</p>
"""),
            ('action-list', '出店前のアクションリスト', """
<ol>
<li><strong>まずCNIPAへ出願する。</strong>英字標、公式中国語名、一般的な音写、消費者が付けた通称を、実際に販売する区分・サブクラスで押さえます。</li>
<li><strong>登録証を待たずに執行を設計する。</strong>出願係属中にプラットフォーム知財ポータルと税関記録の要件を洗い出し、証拠パックを並行して組みます。</li>
<li><strong>プラットフォーム・カテゴリーごとの当期ルールを確認し</strong>、依拠した公告を日付付きで保管します。</li>
<li><strong>ブランド所有者から店舗運営者までの授権チェーンを文書化し</strong>、翻訳および必要なアポスティーユ・領事認証を含めます。</li>
<li><strong>登録後にプラットフォーム知財ポータルへ登録し、税関記録を行い</strong>、担当者を決めたモニタリングに接続します。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">入場資格側は<a href="{L}/amazon-tmall-trademark-requirement-china.html">「Tmall・Amazon中国で販売するには」</a>、権利側は<a href="{ACT}">2027年対応リスト</a>から始めてください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：中国外交部によるアポスティーユ条約の中国発効に関する公表（2023年10月23日）および国務院の2023年11月7日付報道、『中華人民共和国商標法（2026年改正）』第2条・第71条、税関記録の前提条件に関する公式案内。プラットフォームの出店・知財ポータル規則は法令ではなく商業方針で、予告なく変更されます。本記事では特定プラットフォームの保証金、授権階層、書類一覧を意図的に記載していません。本記事は一般情報であり法的助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>海外商標だけで中国出店を予定していますか？</strong> <a href="/contact.html">出店前にCNIPA出願と執行準備の点検をご依頼ください</a>。</p></div>
"""),
        ],
    },
    'assignment': {
        'slug': 'china-trademark-assignment-licence-recordal',
        'title': '中国商標の譲渡とライセンス届出：工場に登録された商標を取り戻す',
        'desc': '製造業者・販売店・元代理店に先に登録された場合、譲渡の方が訴訟より簡単なことがあります。2026年法の譲渡審査、ライセンス届出の効力、捨てるべき4つの誤解を解説します。',
        'lede': '外国法人は中国商標を保有でき、審査中の出願も譲渡でき、譲渡は通常署名入りの譲渡声明で足ります。ただし2026年法に重要な但し書きが加わりました。',
        'card_text': '外国法人も中国商標を所有可能。放棄して再出願する必要はありません。第46条で譲渡に実体審査が加わった点と、ライセンス届出・法定解除権を整理します。',
        'category': 'ライフサイクル',
        'read_time': '約10分',
        'tags': ['譲渡', 'ライセンス届出', 'OEM紛争'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', '商標を先に登録された場合'),
            ('{HUB}', '旧法・新法の条項対比'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '登録後の4つの執行ルート'),
        ],
        'sections': [
            ('four-myths', 'ブランドを足止めする4つの誤解', """
<p class="leading-relaxed text-slate-300 mb-6">工場、販売店、元代理店が商標を登録した場合、相手から「譲渡はできない」と主張されることがよくあります。国際実務で繰り返し報告される同じ4つの主張は、いずれも正しくありません。</p>
<ol>
<li><strong>「中国商標を保有できるのは中国法人だけ」</strong>——外国法人は多数の中国登録を保有しており、所有権に国籍制限はありません。</li>
<li><strong>「放棄して再出願するしかない」</strong>——費用と時間がかかり、第三者が出願できる空白を生みます。通常は譲渡の申請で足ります。</li>
<li><strong>「審査中の出願は譲渡できない」</strong>——可能です。もっとも後に拒絶されれば譲受人は何も取得しません。</li>
<li><strong>「双方の法人資料に領事認証が必要」</strong>——譲渡人・譲受人の身分証明は必要ですが、商標譲渡でそれらの領事認証が一般的に要求されるわけではありません。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">手続自体は、譲渡声明と身分証明をCNIPAに提出するのが通常です。難しいのは多くの場合、保有者との条件交渉という商業面であって、手続面ではありません。<a href="{L}/trademark-registered-by-someone-else-china.html">4つの回復オプション</a>も併せてご覧ください。</p>
"""),
            ('article-46', '2026年の但し書き：譲渡はもはや純粋な形式審査ではない', """
<p class="leading-relaxed text-slate-300 mb-6">改正法第46条は譲渡規則を維持しつつ第三項を追加しました。<strong>混同を生じさせ、または他の不良な影響を及ぼすおそれのある譲渡は認可しない</strong>というもので、2019年法にはなかった実体審査の層です。</p>
<p class="leading-relaxed text-slate-300 mb-6">買い戻しの実務では、譲渡書類に単に「譲渡する」と書くだけでは足りません。当事者間の関係、事業上の根拠、譲渡人が保有する関連・類似商標の扱い、消費者が混同しないよう商品と流通をどう分けるかを説明すべきです。類似商標の一群を保有している場合は、気づいた1件だけでなく一群全体の譲渡または抹消を契約で求めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">第47条は集団商標・証明商標について、譲受人に対応する主体資格と監督能力を要求する並行規則を置きます。第53条も紛争設計上重要で、無効宣告は原則として既に履行済みの譲渡・ライセンス契約に遡及しません（登録人の悪意がある場合を除く）。</p>
"""),
            ('licence-recordal', 'ライセンス届出とその実際の効力', """
<table>
<thead><tr><th>項目</th><th>2026年法（第55条）の規則</th></tr></thead>
<tbody>
<tr><td>品質管理</td><td>許諾者は被許諾者の商品品質を監督し、被許諾者はその品質を保証する</td></tr>
<tr><td>法定解除権</td><td>被許諾者が品質保証義務を履行しない場合、<strong>許諾者はライセンス契約を解除できる</strong>。契約に解除条項がなくても認められる法定の権利</td></tr>
<tr><td>表示</td><td>許諾商標を付した商品には、被許諾者の名称と商品の産地を表示しなければならない</td></tr>
<tr><td>届出</td><td>ライセンスは商標管理部門に届け出て公告する。<strong>届出のないライセンスは善意の第三者に対抗できない</strong></td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">したがって届出は単なる形式ではありません。被許諾者の地位を第三者に対して防御可能にし、ブランド所有者ではなく被許諾者が店舗を運営する場合にプラットフォーム知財ポータルが頻繁に求める書類にもなります。さらに、被許諾者の販売を<a href="{L}/china-trademark-non-use-cancellation-evidence.html">不使用取消に対する使用証拠</a>として使う際に必要な「許諾関係の立証」も生みます。</p>
<p class="leading-relaxed text-slate-300 mb-6">ライセンス形態は一般に独占・排他・普通に分けられます。いずれでも、地域、期間、商品、再許諾、品質検査権、監査権、終了時の在庫・包装の扱い、紛争解決を明記してください。</p>
"""),
            ('decision-table', '譲渡・ライセンス・無効・再出願のどれを選ぶか', """
<table>
<thead><tr><th>手段</th><th>適合する場面</th><th>主な代償</th></tr></thead>
<tbody>
<tr><td>譲渡／買い戻し</td><td>保有者が特定でき交渉に応じる、発売日が動かせない</td><td>最速だが行為を報いることになり、第46条対応の説明資料が必要</td></tr>
<tr><td>ライセンス＋届出</td><td>帰属を争いつつ即座に市場参入したい</td><td>所有権は移らず、届出と品質条項が不可欠</td></tr>
<tr><td>無効宣告／異議</td><td>悪意と在先権利の証拠が揃っており、急ぐ必要がない</td><td>法的には最も強いが期間が最も長い</td></tr>
<tr><td>別の新規商標を出願</td><td>元の商標を商業上諦められる</td><td>リブランディング費用がかかり、旧商標は相手に残る</td></tr>
</tbody>
</table>
"""),
            ('prevention', 'OEM関係で問題を予防する', """
<ul>
<li>ブランド、包装、製品ロードマップを工場・販売店に開示する<strong>前に</strong>中国で出願する。</li>
<li>製造契約に自己登録禁止条項を明示し、出願された場合は譲渡する義務と実効性のある違約金を定める。</li>
<li>終了時の在庫、金型、半製品、包装を区分して扱い、各カテゴリーに処分方法と期限を設定する。</li>
<li>許諾生産数量、照合義務、監査権を定義する。一般的な「超過生産しない」という約束より、説明できない数量について工場に不利益推定を置く方が有効です。</li>
<li>ライセンス・譲渡書類を実際の登録商品と整合させ、名称・住所・代理人の変更は速やかに手続する（第57条は登録事項の是正なき変更に罰則を定めます）。</li>
</ul>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第46条・第47条・第53条・第55条・第57条（CNIPA、2026年6月26日）、CNIPA『商標法改正の主要内容』（2026年7月10日）、外国法人への中国商標譲渡およびOEM契約条項に関する実務解説。必要書類・審査実務は改正実施条例でさらに細分化される可能性があります。本記事は一般情報であり法的助言ではありません。係属中の紛争は個別の事実関係に基づく助言が必要です。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>工場に登録された商標を取り戻しますか？</strong> <a href="/contact.html">譲渡書類、届出、第46条対応の申請についてご相談ください</a>。</p></div>
"""),
        ],
    },
}}

CONTENT['ko'] = {'articles': {
    'enforce': {
        'slug': 'china-trademark-enforcement-routes-after-registration',
        'title': '등록 후 활용 가능한 4가지 권리 행사 경로(시장감독·세관·플랫폼·법원)',
        'desc': '중국 상표 등록증은 권리 행사의 입장권이지 종착점이 아닙니다. 행정·세관·플랫폼·법원 네 경로를 전제조건과 성과 기준으로 비교합니다.',
        'lede': '등록은 권리 행사의 자격을 줍니다. 실제 집행은 시장감독 부서, 세관, 전자상거래 플랫폼, 법원이라는 서로 다른 네 경로에서 이루어지며 전제조건과 산출물이 각기 다릅니다.',
        'card_text': '행정 단속, 세관 등록, 플랫폼 삭제, 민사소송을 필요 서류·소요 시간·실제 결과 기준으로 비교했습니다.',
        'category': '라이프사이클',
        'read_time': '약 11분',
        'tags': ['권리 행사', '세관 등록', '플랫폼 삭제'],
        'related': [
            ('{L}/china-trademark-monitoring-protection.html', '상표 모니터링과 보호 전략'),
            ('{L}/china-trademark-non-use-cancellation-evidence.html', '2027년 대비 사용 증거 파일'),
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Tmall·아마존 상표 요건'),
        ],
        'sections': [
            ('one-right-four-channels', '하나의 권리, 네 가지 경로', """
<p class="leading-relaxed text-slate-300 mb-6">중국에서 거의 모든 권리 행사는 CNIPA 등록증(또는 등록된 라이선스)을 전제로 합니다. 플랫폼 지식재산 포털, 세관 등록, 행정 신고 모두 중국 등록증을 요구합니다. 해외 등록, 계류 중인 출원, 유통사의 위임장은 이를 대체하지 못합니다.</p>
<table>
<thead><tr><th>경로</th><th>적합한 상황</th><th>전제조건</th><th>산출물</th></tr></thead>
<tbody>
<tr><td><strong>행정(시장감독)</strong></td><td>오프라인 시장·도매상·현지 공장의 명백한 위조품</td><td>등록증, 증거, 중국어 신고서</td><td>현장 조사, 압수, 행정 처벌. 소송보다 빠르고 저렴</td></tr>
<tr><td><strong>세관(GACC)</strong></td><td>위조품 수출입, OEM 유출, 무단 국경 간 출하</td><td>등록상표의 해관총서 등록(备案)</td><td>의심 화물의 직권 통관 보류 및 권리자 통지</td></tr>
<tr><td><strong>플랫폼 IPP</strong></td><td>전자상거래·소셜커머스의 침해 상품</td><td>CNIPA 등록증 또는 등록된 라이선스로 브랜드 등록</td><td>상품 삭제, 반복 침해자 제재. 탐지는 자사 책임인 반응형 체계</td></tr>
<tr><td><strong>민사소송</strong></td><td>고액·반복·다툼이 큰 침해, 손해배상과 선례</td><td>공증 증거, 현지 변호사, 등록권자 또는 전용 라이선시 적격</td><td>금지명령, 손해배상, 침해물 폐기</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">2026년 법은 기반을 강화합니다. 제75조는 행정 집행과 형사 기관 간 양방향 이송을 명문화하고, 제76조는 멸실 우려가 있는 증거의 선행 등록 보존을 허용하며, 제77조는 침해 중지에 소요된 합리적 비용을 배상에 포함함을 명시합니다.</p>
"""),
            ('customs-recordal', '세관 등록: 등록 후 가장 효율적인 한 수', """
<p class="leading-relaxed text-slate-300 mb-6">세관 보호에는 두 가지 모드가 있습니다. 등록이 없으면 구체적 신청과 증거에 기반한 대응이 중심이라 출하를 미리 알고 있어야 합니다. 등록이 있으면 세관이 직권으로 의심 화물의 통관을 보류하고 권리자에게 통지할 수 있습니다. <strong>능동적 보호의 전제가 바로 등록입니다.</strong></p>
<table>
<thead><tr><th>항목</th><th>규칙</th></tr></thead>
<tbody>
<tr><td>결정</td><td>전체 신청 서류 접수 후 30영업일 이내</td></tr>
<tr><td>유효기간</td><td>허가일부터 10년. 상표 잔여기간이 짧으면 상표 기간을 따름</td></tr>
<tr><td>갱신</td><td>만료 6개월 전 신청, 결정은 10영업일 이내</td></tr>
<tr><td>변경</td><td>등록 사항 변경일부터 30영업일 이내 변경 신청</td></tr>
<tr><td>외국 권리자</td><td>국내 사무소 또는 중국 대리인을 통해 신청</td></tr>
<tr><td>수수료</td><td>요금 및 면제 여부는 해관총서 고시에 따름. 제3자 요약이 아닌 당기 공식 정보 확인 필요</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">신청에는 통상 등록증과 권리 상태, 권리자 신분증명과 위임장, 정품·포장 사진, 정품 정보(명칭, 산지, 통관지, 수출입자, 특징, 가격), 알려진 침해자·의심 출하 정보가 포함됩니다. 외국어 자료에는 중국어 번역을 붙입니다. 정상 제조자·수입자 목록을 최신으로 유지하십시오. 낡은 목록은 정품이 지연되는 사이 위조품이 통과하는 역전을 만듭니다.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>실무 포인트:</strong> 세관 보호는 원칙적으로 등록된 상표 단위입니다. 메인 상표, 서브 브랜드, 방어 상표를 함께 쓰면 각각 별도 등록이 필요한 경우가 많고, 최초 출원의 지정상품이 실제 출하품을 포괄하는지도 확인해야 합니다.</p></div>
"""),
            ('platform-enforcement', '플랫폼 삭제: 빠르지만 반응형, 증거가 전부', """
<p class="leading-relaxed text-slate-300 mb-6">주요 전자상거래·콘텐츠 플랫폼은 지식재산 보호 시스템을 운영합니다. 등록에는 권리 증명, 실무상 CNIPA 등록증 또는 등록된 라이선스가 필요합니다. 신고는 짧은 시간 안에, 종종 변호사가 아니라 시스템으로 심사되므로 제출물의 품질이 결과를 좌우합니다.</p>
<ul>
<li>판매자를 일반적으로 서술하지 말고 URL과 상품 ID로 개별 상품을 특정합니다.</li>
<li>등록번호를 명시하고 등록증을 첨부합니다.</li>
<li>침해 근거를 구체적으로 적시합니다(동일 표장, 위조품, 무단 상품 이미지·설명, 공식 대리점 사칭 등).</li>
<li>상품 화면과 정품·포장을 나란히 놓고 차이를 주석한 비교 증거를 첨부합니다.</li>
<li>반대 통지와 상호명을 바꿔 재등장하는 반복 침해자를 전제합니다. 지속적 프로그램입니다.</li>
<li>유통사나 대리점이 매장을 운영한다면 브랜드 명의로 조치할 수 있도록 신고 권한을 문서화합니다.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">부정확하거나 남용적인 신고는 플랫폼의 제재를 받을 수 있습니다. 증거 파일과 에스컬레이션 규칙은 <a href="{L}/china-trademark-non-use-cancellation-evidence.html">사용 증거 파일</a>과 같은 곳에 모으면, 동일한 날짜 있는 화면과 판매 기록을 양쪽에 쓸 수 있습니다.</p>
"""),
            ('choosing-a-route', '경로 선택 판단표', """
<table>
<thead><tr><th>상황</th><th>첫 수</th><th>다음 수</th></tr></thead>
<tbody>
<tr><td>한 플랫폼에 위조 상품 등장</td><td>완전한 증거 패키지로 플랫폼 신고</td><td>재등장을 반복하면 시장감독으로 상향</td></tr>
<tr><td>공장에서 의심 화물이 수출되는 경우</td><td>세관 등록 + 발생지 행정 조치</td><td>물량이 맞으면 민사 손해배상 청구</td></tr>
<tr><td>계약 종료 후에도 유통사가 판매 지속</td><td>행정 신고 + 플랫폼 삭제, 라이선스 등록 상태 확인</td><td>계약·침해를 결합한 소송</td></tr>
<tr><td>조직적·대규모 위조</td><td>공증 증거 확보 후 보전 조치가 붙은 민사 제소</td><td>제75조 행형 연계에 따른 형사 이송</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">흔한 실수는 이들을 대안으로 보는 것입니다. 실제로는 순차적입니다. 모니터링이 문제를 찾고, 등록과 증거가 행동을 가능하게 하며, 플랫폼 신고가 보이는 상품을 지우고, 행정·법원 조치가 침해자의 경제적 계산을 바꿉니다.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제75조·제76조·제77조(CNIPA, 2026년 6월 26일), CNIPA 『상표법 개정 주요 내용』(2026년 7월 10일), 지식재산 세관 등록에 관한 관공서 공개 자료(30영업일 결정, 10년 유효, 만료 6개월 전 갱신, 30영업일 내 변경). 플랫폼 신고 실무와 요금표는 운영 방침으로 자주 바뀌므로 각 플랫폼의 당기 지식재산 포털과 해관총서 고시에서 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>포트폴리오에 맞춘 집행 계획이 필요하신가요?</strong> <a href="/contact.html">세관 등록, 플랫폼 등록, 신고 양식에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'rmark': {
        'slug': 'overseas-r-mark-vs-china-trademark-registration',
        'title': '해외 R 마크는 중국 등록이 아니다: 플랫폼 입점 자격과 권리 소유',
        'desc': '일부 중국 전자상거래 입점 심사는 해외 등록증을 접수합니다. 그러나 플랫폼 신고·세관 등록·권리 행사에는 CNIPA 등록증이 필요합니다. 출점 전에 두 궤도를 정리하십시오.',
        'lede': '해외 R 마크는 매장 문을 열 수는 있어도 중국에서 권리 행사의 근거가 되지는 못합니다. 이 둘을 혼동하는 것이 출점 전 가장 비용이 큰 실수입니다.',
        'card_text': '입장권과 권리증 비교: 입점 서류, 집행의 전제조건, 위임 체인, 그리고 두 궤도가 만나는 지점.',
        'category': '라이프사이클',
        'read_time': '약 9분',
        'tags': ['크로스보더 EC', '입점 심사', 'CNIPA 등록증'],
        'related': [
            ('{L}/amazon-tmall-trademark-requirement-china.html', 'Tmall·아마존 중국에서 판매하려면'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '등록 후 4가지 집행 경로'),
            ('{HUB}', '구법·신법 조항 대조'),
        ],
        'sections': [
            ('two-tracks', '혼동되기 쉬운 두 궤도', """
<table>
<thead><tr><th></th><th>플랫폼 입점</th><th>중국 내 법적 권리</th></tr></thead>
<tbody>
<tr><td>답하는 질문</td><td>"이 매장·브랜드를 열어도 되는가"</td><td>"이 지역에서 집행 가능한 권리를 가졌는가"</td></tr>
<tr><td>판단 주체</td><td>플랫폼 입점 심사 부서(자체 규칙, 수시 변경)</td><td>CNIPA, 법원, 세관, 시장감독 부서</td></tr>
<tr><td>전형적 서류</td><td>본국 등록·출원 증빙, 브랜드 위임 체인, 법인 서류</td><td><strong>CNIPA 등록증</strong>(또는 등록된 라이선스)</td></tr>
<tr><td>열리는 것</td><td>매장, 상품 등록 권한, 카테고리</td><td>플랫폼 신고, 세관 등록, 행정 신고, 소송</td></tr>
<tr><td>실패 양상</td><td>입점 거절·매장 동결</td><td>도용자가 자사 이름을 보유하고 신고 적격이 없음</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">일부 크로스보더 입점 경로는 본국 등록 증빙을 심사 자료로 접수합니다. 그러나 이는 <strong>플랫폼의 상업적 입장 판단</strong>이지 중국 상표권의 인정이 아닙니다. 중국은 선출원주의이며 외국 등록은 중국에서 효력이 없습니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>제3자 규칙 요약을 근거로 삼지 마십시오.</strong> 필요 서류, 보증금, 허용되는 위임 체인 단계, 추가 자료는 플랫폼·카테고리별로 자주 바뀝니다. 예산 편성이나 유통 계약 체결 전 반드시 해당 플랫폼의 당기 입점 공고에서 확인하십시오.</p></div>
"""),
            ('handover-points', '두 궤도가 충돌하는 지점', """
<ol>
<li><strong>플랫폼 지식재산 포털의 브랜드 등록</strong>은 통상 CNIPA 등록증 또는 등록된 라이선스를 요구합니다. 해외 증빙으로 매장을 열어도 침해 신고 적격은 생기지 않습니다.</li>
<li><strong>세관 등록</strong>은 중국에 등록된 상표(이 목적에서는 서비스표 제외)를 전제로 하며 본국 등록은 등록할 수 없습니다.</li>
<li><strong>행정 신고·소송</strong>은 중국 등록과 지정상품을 기준으로 판단됩니다.</li>
<li><strong>위임 체인</strong>은 양쪽에서 심사되지만 목적이 다릅니다. 플랫폼은 매장 운영자까지의 연결을 원하고, CNIPA·법원은 누가 상표를 소유하며 라이선스가 등록되었는지를 봅니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">결과적으로 익숙한 함정이 생깁니다. 해외 상표로 출점하고, 도용자가 중국어 이름을 등록하고, 자사 명의 CNIPA 등록증이 없어 침해 상품을 삭제하지 못하는 경우입니다. 하류 영향은 <a href="{L}/china-trademark-enforcement-routes-after-registration.html">4가지 집행 경로</a>를 참고하십시오.</p>
"""),
            ('documents', '서류: 아포스티유, 영사인증, 위임장의 함정', """
<p class="leading-relaxed text-slate-300 mb-6">외국어 법인 서류, 위임장, 증명서에는 번역이 필요하고 접수 기관에 따라 일종의 인증이 요구될 수 있습니다. 중국은 『외국 공문서의 인증 요구 폐지 협약』에 가입했고 <strong>2023년 11월 7일</strong> 중국에서 발효되었습니다. 다른 체약국의 공문서는 <strong>아포스티유(附加证明书)</strong>가 기존 "외교부 인증 + 영사관 인증" 이중 인증을 대체하며, 비체약국 문서는 기존 영사인증 경로를 따릅니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">실무상 두 가지 주의점이 있습니다. 첫째, 해당 문서가 협약상 "공문서"에 해당하는지, 그리고 접수 기관이 실제로 인증을 요구하는지는 문서와 절차마다 다릅니다. 둘째, <strong>CNIPA 상표 출원 위임장은 통상 서명된 단순 위임장으로 충분하며</strong>, 플랫폼의 위임 체인 패키지에 인증이 필요하다고 해서 당연히 영사인증이 필요한 것은 아닙니다. 중국 대리인과 플랫폼에 각각 확인하고, 실제로 필요한 서류에만 리드타임을 반영하십시오.</p>
"""),
            ('action-list', '출점 전 액션 리스트', """
<ol>
<li><strong>먼저 CNIPA에 출원하십시오.</strong> 영문 표장, 공식 중국어 명칭, 일반적인 음역, 소비자가 붙인 애칭을 실제 판매할 클래스·서브클래스에서 확보합니다.</li>
<li><strong>등록증을 기다리는 동안 집행을 설계하십시오.</strong> 출원 계류 중에 플랫폼 지식재산 포털과 세관 등록 요건을 파악하고 증거 패키지를 병행 구성합니다.</li>
<li><strong>플랫폼·카테고리별 당기 규칙을 확인하고</strong> 근거로 삼은 공고를 날짜와 함께 보관합니다.</li>
<li><strong>브랜드 소유자부터 매장 운영자까지 위임 체인을 문서화하고</strong> 번역 및 필요한 아포스티유·영사인증을 포함합니다.</li>
<li><strong>등록 후 플랫폼 지식재산 포털에 등록하고 세관 등록을 마친 뒤</strong> 담당자가 정해진 모니터링에 연결합니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">입점 자격 측은 <a href="{L}/amazon-tmall-trademark-requirement-china.html">「Tmall·아마존 중국에서 판매하려면」</a>, 권리 측은 <a href="{ACT}">2027년 대응 목록</a>에서 시작하십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 중국 외교부의 아포스티유 협약 중국 발효 공표(2023년 10월 23일) 및 국무원의 2023년 11월 7일자 보도, 『중화인민공화국 상표법(2026년 개정)』 제2조·제71조, 세관 등록 전제조건에 관한 공식 안내. 플랫폼 입점·지식재산 포털 규칙은 법령이 아닌 상업 방침이며 예고 없이 바뀝니다. 본 글에서는 특정 플랫폼의 보증금, 위임 단계, 서류 목록을 의도적으로 기재하지 않았습니다. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>해외 상표만으로 중국 출점을 계획 중이신가요?</strong> <a href="/contact.html">매장 오픈 전 CNIPA 출원과 집행 준비 점검을 문의하세요</a>.</p></div>
"""),
        ],
    },
    'assignment': {
        'slug': 'china-trademark-assignment-licence-recordal',
        'title': '중국 상표 양도와 라이선스 등록: 공장에 등록된 상표를 되찾기',
        'desc': '제조사·유통사·전 대리점이 먼저 등록한 경우 소송보다 양도가 간단할 때가 있습니다. 2026년 법의 양도 심사, 라이선스 등록의 효력, 버려야 할 네 가지 오해를 정리했습니다.',
        'lede': '외국 법인은 중국 상표를 보유할 수 있고, 심사 중인 출원도 양도할 수 있으며, 양도는 통상 서명된 양도 성명서로 충분합니다. 다만 2026년 법에 중요한 단서가 추가되었습니다.',
        'card_text': '외국 법인도 중국 상표 소유 가능. 포기 후 재출원은 필요 없습니다. 제46조의 양도 실체 심사와 라이선스 등록·법정 해제권을 정리합니다.',
        'category': '라이프사이클',
        'read_time': '약 10분',
        'tags': ['양도', '라이선스 등록', 'OEM 분쟁'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', '상표를 먼저 등록당했을 때'),
            ('{HUB}', '구법·신법 조항 대조'),
            ('{L}/china-trademark-enforcement-routes-after-registration.html', '등록 후 4가지 집행 경로'),
        ],
        'sections': [
            ('four-myths', '브랜드를 묶어두는 네 가지 오해', """
<p class="leading-relaxed text-slate-300 mb-6">공장, 유통사, 전 대리점이 상표를 등록한 경우 상대방이 "양도는 불가능하다"고 주장하는 일이 잦습니다. 국제 실무에서 반복 보고되는 같은 네 가지 주장은 모두 사실이 아닙니다.</p>
<ol>
<li><strong>"중국 상표는 중국 법인만 보유할 수 있다"</strong>——외국 법인이 다수의 중국 등록을 보유하고 있으며 소유권에 국적 제한은 없습니다.</li>
<li><strong>"포기하고 다시 출원하는 수밖에 없다"</strong>——비용과 시간이 들고 제3자가 출원할 수 있는 공백을 만듭니다. 통상 양도 신청으로 충분합니다.</li>
<li><strong>"심사 중인 출원은 양도할 수 없다"</strong>——가능합니다. 다만 이후 거절되면 양수인은 아무것도 취득하지 못합니다.</li>
<li><strong>"양쪽 법인 서류에 영사인증이 필요하다"</strong>——양도인·양수인의 신분 증명은 필요하지만, 상표 양도에서 그 서류의 영사인증이 일반적으로 요구되지는 않습니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">절차 자체는 양도 성명서와 신분 증명을 CNIPA에 제출하는 것이 통상적입니다. 어려운 부분은 대개 보유자와의 조건 협상이라는 상업 측면이지 절차가 아닙니다. <a href="{L}/trademark-registered-by-someone-else-china.html">네 가지 회복 옵션</a>도 함께 보십시오.</p>
"""),
            ('article-46', '2026년 단서: 양도는 더 이상 순수한 형식 심사가 아니다', """
<p class="leading-relaxed text-slate-300 mb-6">개정법 제46조는 양도 규칙을 유지하면서 제3항을 추가했습니다. <strong>혼동을 일으키거나 그 밖의 불량한 영향을 줄 우려가 있는 양도는 허가하지 않는다</strong>는 것으로, 2019년 법에는 없던 실체 심사 계층입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">매입 실무에서는 양도 서류에 단순히 "양도한다"고 적는 것만으로 부족합니다. 당사자 간 관계, 사업상 근거, 양도인이 보유한 관련·유사 상표의 처리, 소비자가 혼동하지 않도록 상품과 유통을 어떻게 분리할지 설명해야 합니다. 유사 상표 무리를 보유한 경우 발견한 1건뿐 아니라 무리 전체의 양도 또는 말소를 계약에 요구하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">제47조는 단체상표·증명상표에 대해 양수인에게 상응하는 주체 자격과 감독 능력을 요구하는 병행 규칙을 둡니다. 제53조도 분쟁 설계상 중요한데, 무효심판은 원칙적으로 이미 이행된 양도·라이선스 계약에 소급하지 않습니다(등록인의 악의가 있으면 예외).</p>
"""),
            ('licence-recordal', '라이선스 등록과 그 실제 효력', """
<table>
<thead><tr><th>항목</th><th>2026년 법(제55조) 규칙</th></tr></thead>
<tbody>
<tr><td>품질 관리</td><td>허락자는 피허락자의 상품 품질을 감독하고, 피허락자는 그 품질을 보증해야 함</td></tr>
<tr><td>법정 해제권</td><td>피허락자가 품질 보증 의무를 이행하지 않으면 <strong>허락자는 라이선스 계약을 해제할 수 있음</strong>. 계약에 해제 조항이 없어도 인정되는 법정 권리</td></tr>
<tr><td>표시</td><td>허락 상표를 붙인 상품에는 피허락자 명칭과 상품 산지를 표시해야 함</td></tr>
<tr><td>등록</td><td>라이선스는 상표 관리 부서에 등록(备案)하고 공고. <strong>등록되지 않은 라이선스는 선의의 제3자에게 대항할 수 없음</strong></td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">따라서 등록은 단순한 형식이 아닙니다. 피허락자의 지위를 제3자에게 대항 가능하게 만들고, 브랜드 소유자가 아니라 피허락자가 매장을 운영할 때 플랫폼 지식재산 포털이 자주 요구하는 서류가 됩니다. 또한 피허락자의 판매를 <a href="{L}/china-trademark-non-use-cancellation-evidence.html">불사용 취소에 대한 사용 증거</a>로 쓸 때 필요한 "허락 관계 입증"도 만들어 줍니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">라이선스 형태는 보통 전용·배타·통상으로 나뉩니다. 어떤 형태든 지역, 기간, 상품, 재허락, 품질 검사권, 감사권, 종료 시 재고·포장 처리, 분쟁 해결을 명시하십시오.</p>
"""),
            ('decision-table', '양도·라이선스·무효·재출원 중 무엇을 고를까', """
<table>
<thead><tr><th>수단</th><th>적합한 상황</th><th>주요 대가</th></tr></thead>
<tbody>
<tr><td>양도 / 매입</td><td>보유자가 특정되고 협상에 응하며 출시일이 고정된 경우</td><td>가장 빠르지만 그 행위에 보상을 주게 되고 제46조 대응 설명 자료가 필요</td></tr>
<tr><td>라이선스 + 등록</td><td>귀속을 다투면서 즉시 시장 접근이 필요한 경우</td><td>소유권은 이전되지 않으며 등록과 품질 조항이 필수</td></tr>
<tr><td>무효심판 / 이의</td><td>악의와 선행권리 증거가 갖춰져 있고 급하지 않은 경우</td><td>법적으로 가장 강하지만 기간이 가장 김</td></tr>
<tr><td>별개의 신규 상표 출원</td><td>원래 상표를 상업적으로 포기할 수 있는 경우</td><td>리브랜딩 비용이 들고 기존 상표는 상대에게 남음</td></tr>
</tbody>
</table>
"""),
            ('prevention', 'OEM 관계에서 문제 예방하기', """
<ul>
<li>브랜드, 포장, 제품 로드맵을 공장·유통사에 공개하기 <strong>전에</strong> 중국에 출원하십시오.</li>
<li>제조 계약에 자체 등록 금지 조항을 명시하고, 출원된 경우 양도할 의무와 실효성 있는 위약금을 정하십시오.</li>
<li>종료 시 재고, 금형, 반제품, 포장을 구분해 다루고 각 항목별 처분 방법과 기한을 두십시오.</li>
<li>허락 생산 수량, 대조 의무, 감사권을 정의하십시오. 일반적인 "초과 생산하지 않는다"는 약속보다 설명되지 않은 수량에 대해 공장에 불이익 추정을 두는 편이 유효합니다.</li>
<li>라이선스·양도 서류를 실제 등록상품과 일치시키고, 명칭·주소·대리인 변경은 신속히 처리하십시오(제57조는 등록 사항 미시정 변경에 제재를 둡니다).</li>
</ul>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제46조·제47조·제53조·제55조·제57조(CNIPA, 2026년 6월 26일), CNIPA 『상표법 개정 주요 내용』(2026년 7월 10일), 외국 법인에 대한 중국 상표 양도 및 OEM 계약 조항에 관한 실무 해설. 필요 서류와 심사 실무는 개정 시행조례에서 더 세분화될 수 있습니다. 본 글은 일반 정보이며 법률 자문이 아닙니다. 계류 중 분쟁은 개별 사실관계에 따른 자문이 필요합니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>공장에 등록된 상표를 되찾으시겠습니까?</strong> <a href="/contact.html">양도 서류, 등록, 제46조 대응 신청에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
}}
