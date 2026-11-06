# -*- coding: utf-8 -*-
"""Batch 2 content (part A): P0-2 watch SOP, P0-3 use-evidence. EN/JA/KO.

Placeholders: {L} -> /blog | /blog/ja | /blog/ko ; {HUB} / {ACT} -> batch-1 hub URLs.
UI strings (breadcrumb, CTA, date labels) are inherited from p0_2027_content.
"""

CONTENT = {}

CONTENT['en'] = {'articles': {
    'watch': {
        'slug': 'china-trademark-opposition-watch-sop-2-months',
        'title': "China's 2-Month Opposition Window: A Trademark Watch SOP for Foreign Brands",
        'desc': "From 1 January 2027 China's opposition window drops to two months. A practical watch-service SOP: monitoring scope, alert frequency, decision deadlines and a ready-to-file evidence pack.",
        'lede': "Article 36 of the 2026 Trademark Law cuts the opposition window from three months to two. For foreign brands, that turns an occasional register check into an operational process with named owners and pre-authorised counsel.",
        'card_text': "Two months is not a warning period — it is the whole response chain. Configure your watch scope, decision authority and evidence pack before 1 January 2027.",
        'category': 'Playbook',
        'read_time': '10 min read',
        'tags': ['opposition', 'watching service', '2-month deadline'],
        'related': [
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/china-trademark-monitoring-protection.html', 'Trademark Monitoring and Protection'),
        ],
        'sections': [
            ('why-two-months-changes-everything', 'Why Two Months Changes the Whole Chain', """
<p class="leading-relaxed text-slate-300 mb-6">Article 36 of the revised PRC Trademark Law, effective <strong>1 January 2027</strong>, sets the opposition period at <strong>two months from the date of preliminary publication</strong> (down from three under Article 33 of the 2019 law). The period runs from publication, not from when your team happens to notice the application.</p>
<p class="leading-relaxed text-slate-300 mb-6">Under Article 4 of the CNIPA's draft transition measures, the dividing line is the <strong>publication date</strong>: the Trademark Gazette date for domestic applications and the WIPO publication date for international registrations designating China. Marks published before 1 January 2027 keep the 3-month window; those published on or after it get 2 months. A window that straddles the year boundary is <strong>not restarted</strong>.</p>
<p class="leading-relaxed text-slate-300 mb-6">The practical consequence is that detection, internal approval, evidence collection, translation, notarisation where required and local counsel instruction all have to complete inside eight weeks. A brand that reviews the register quarterly will lose the right to oppose before it finishes its first internal meeting.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Draft status:</strong> the transition measures were open for comment until 12 November 2026 and may change. Confirm the final text before setting hard internal deadlines.</p></div>
"""),
            ('backwards-timeline', 'A Backwards Timeline From Publication Day', """
<table>
<thead><tr><th>Point</th><th>Action</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Weekly, continuously</td><td>Gazette watch runs on core classes, sub-classes and Chinese-character variants; alerts go to a named inbox, not a shared distribution list with no owner</td><td>Watch provider / IP counsel</td></tr>
<tr><td>Day 0&ndash;2</td><td>Publication detected; conflict scored (identical, near-identical, transliteration, related company or distributor)</td><td>IP counsel</td></tr>
<tr><td>Day 3&ndash;5</td><td>Go / no-go decision under a pre-agreed threshold; budget released automatically for high-risk conflicts</td><td>Brand owner (pre-authorised)</td></tr>
<tr><td>Day 6&ndash;14</td><td>Evidence pack assembled, foreign-language documents translated, signature and authorisation obtained</td><td>Local agent + brand owner</td></tr>
<tr><td>Day 15&ndash;30</td><td>Opposition filed electronically; reserve the right to submit supplementary evidence</td><td>Chinese trademark agency</td></tr>
<tr><td>Buffer</td><td>Keep at least four weeks unused for holidays, courier delays, document legalisation and internal escalation</td><td>Programme owner</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Filing on day 55 is technically possible but leaves no margin. The point of the SOP is to make the decision, not the filing, the bottleneck.</p>
"""),
            ('watch-configuration', 'Watch Configuration Checklist', """
<ul>
<li><strong>Marks:</strong> the Latin word mark, the official Chinese name, common transliterations, consumer-coined nicknames, pinyin, abbreviations, device marks and the Chinese name of each product line.</li>
<li><strong>Scope:</strong> the classes you registered, adjacent classes you may enter, the specific CNIPA sub-classes you use, and the classes where squatters commonly file (often 9, 25, 35, 41, 43 depending on sector).</li>
<li><strong>Parties:</strong> your own entity names, distributors, former agents, OEM factories and known squatters — a filing by a former partner is easier to challenge when the relationship is documented.</li>
<li><strong>Frequency:</strong> weekly at minimum; daily or near-real-time alerts for your top three classes. Monthly sampling is not compatible with a 2-month statutory window.</li>
<li><strong>Escalation:</strong> one named decision-maker, a deputy, a pre-signed power of attorney on file with your Chinese agent, and a standing instruction to file a protective opposition when the deadline is within ten working days.</li>
<li><strong>Records:</strong> log the publication date, the alert date, the decision and the filing receipt. These dates matter if the other side later argues the opposition was out of time.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">For the broader monitoring framework, see our <a href="{L}/china-trademark-monitoring-protection.html">trademark monitoring and protection guide</a>.</p>
"""),
            ('evidence-pack', 'The Evidence Pack to Keep Ready', """
<p class="leading-relaxed text-slate-300 mb-6">An opposition is won on documents, not on the fact that your brand is well known. Keep a standing, refreshed pack so that only the conflicting application needs to be added:</p>
<ul>
<li>Proof of your prior rights: home-country registrations, Chinese registrations, earlier applications and priority documents.</li>
<li>Proof of reputation in China: dated advertising, media coverage, trade-fair presence, e-commerce listings, distributor agreements and sales records showing use before the conflicting filing date.</li>
<li>Proof of the applicant's bad faith: a pattern of filings resembling other brands, prior business contact, an offer to sell the mark back, or a filing by a distributor or manufacturer.</li>
<li>Identity and authorisation documents: an up-to-date power of attorney and corporate registration extracts, with translations ready.</li>
</ul>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Filing mechanics matter.</strong> CNIPA's official FAQ on electronic oppositions states that evidence uploaded through the online system must be in <strong>PDF</strong>, that the "legal and factual grounds" field in an electronic opposition is limited to <strong>2,000 characters</strong>, and that supplementary evidence is only possible if you selected the option to reserve that right when filing — in which case it must be submitted within <strong>three months</strong>. An opposition respondent has <strong>30 days</strong> to reply; supplementary evidence must be declared in the reply and filed within three months of it.</p></div>
"""),
            ('filing-mechanics', 'After Filing: What the Calendar Looks Like', """
<table>
<thead><tr><th>Stage</th><th>Timing / rule</th></tr></thead>
<tbody>
<tr><td>Opposition examination</td><td>CNIPA decides within 12 months of the end of the publication period, extendable by 6 months (Art. 38)</td></tr>
<tr><td>Respondent's reply</td><td>30 days from receipt of the notice (CNIPA electronic-filing FAQ)</td></tr>
<tr><td>Supplementary evidence</td><td>Declare in the submission and file within 3 months; PDF only (CNIPA FAQ)</td></tr>
<tr><td>Stay of proceedings</td><td>Art. 41 allows suspension where the outcome depends on another pending case — useful when the cited prior right is itself under invalidation</td></tr>
<tr><td>Appeal</td><td>A party dissatisfied with the opposition decision may request review within 15 days (Art. 38)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Budget for CNIPA official fees, local agent fees, translation and, where needed, notarisation or an Apostille. Fee schedules change; confirm the current amounts with your agent rather than relying on third-party summaries.</p>
"""),
            ('common-failures', 'Five Failure Modes We See Repeatedly', """
<ol>
<li>Monitoring only the Latin mark, so an opposition is missed when a squatter files the Chinese transliteration.</li>
<li>Relying on distributors or customers to report a conflict informally.</li>
<li>Waiting for head-office approval with no pre-agreed threshold or deputy.</li>
<li>Discovering the power of attorney has expired or the registered address has changed.</li>
<li>Treating the 2-month period as if a court-style extension were available. It is a statutory window, not a negotiable deadline.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">The cheapest fix is procedural: pre-authorise your agent, log publication dates, and run the watch weekly. See <a href="{ACT}">the full pre-2027 action list</a> for the other four workstreams.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Articles 36, 38 and 41 of the <em>Trademark Law of the PRC (2026 Revision)</em> (CNIPA, 26 June 2026); CNIPA notice of 28 September 2026 on the draft transition measures; CNIPA Trademark Office, <em>FAQ on Electronic Applications for Opposition, Non-Use Cancellation and Invalidation</em>. Draft measures are not final. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Need a 2-month watch configuration?</strong> <a href="/contact.html">Talk to our team</a> about monitoring scope and a pre-authorised opposition process.</p></div>
"""),
        ],
    },
    'evidence': {
        'slug': 'china-trademark-non-use-cancellation-evidence',
        'title': 'Non-Use Cancellation in China: How to Build a Use-Evidence File Before CNIPA Acts',
        'desc': "The 2026 Trademark Law lets the authority cancel unused marks on its own initiative. A field guide to what counts as genuine use, the five official evidence requirements, and a quarterly archiving SOP.",
        'lede': "From 1 January 2027, a Chinese registration can be cancelled not only on a third party's request but on the authority's own initiative. That makes a use-evidence file a day-one operational task.",
        'card_text': "CNIPA's official five requirements for valid use evidence, the documents that do not count, and a quarterly archiving routine by mark and class.",
        'category': 'Playbook',
        'read_time': '10 min read',
        'tags': ['non-use cancellation', 'use evidence', 'portfolio audit'],
        'related': [
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '2-Month Opposition Watch SOP'),
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{L}/china-trademark-renewal-guide.html', 'China Trademark Renewal Guide'),
        ],
        'sections': [
            ('what-changed-in-2027', 'What Changes on 1 January 2027', """
<p class="leading-relaxed text-slate-300 mb-6">Article 57 of the 2026 Trademark Law keeps the familiar rule: a registered mark that has become the generic name of its goods, or that has not been used for <strong>three consecutive years</strong> without justified reason, may be cancelled on the application of any party. It then adds a third paragraph: where those circumstances exist, <strong>the trademark authority may cancel the registration on its own initiative</strong>.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two related changes raise the stakes. Article 2 expressly includes use through the internet and information networks within the definition of trademark use, giving dated e-commerce and social records a clearer role. Article 78 provides that where the rights holder has not used the mark in the preceding three years, an accused infringer may not be liable for damages — idle registrations lose practical enforceability even before they are cancelled.</p>
<p class="leading-relaxed text-slate-300 mb-6">The authority must decide a cancellation application within <strong>nine months</strong>, extendable by three (Art. 57). A party dissatisfied with the decision may request review within <strong>15 days</strong> (Art. 58).</p>
"""),
            ('two-sides', 'One Rule, Two Directions', """
<table>
<thead><tr><th></th><th>Offensive use</th><th>Defensive exposure</th></tr></thead>
<tbody>
<tr><td>Who is at risk</td><td>A squatter or blocker who registered a mark but never traded under it</td><td>A legitimate foreign brand with dormant defensive registrations in classes it does not currently sell in</td></tr>
<tr><td>Typical action</td><td>File a non-use cancellation to clear a blocking mark, often alongside an invalidation or a negotiated purchase</td><td>Respond to a cancellation notice or a proactive review with a dated evidence file</td></tr>
<tr><td>What wins</td><td>Showing the opponent has no genuine commercial use</td><td>Producing a continuous, dated chain of real use on the registered goods</td></tr>
<tr><td>New in 2027</td><td>The authority can act without a private applicant</td><td>No private trigger is needed for a dormant mark to be examined</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The same reform is therefore both a cheaper way to remove squatters and a reason to audit your own portfolio. Compare all recovery routes in <a href="{L}/trademark-registered-by-someone-else-china.html">What Happens If Someone Registers Your Trademark First</a>.</p>
"""),
            ('five-requirements', 'The Five Official Requirements for Valid Use Evidence', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPA's Trademark Office FAQ on electronic filings sets out what evidence must show. All five need to be satisfied:</p>
<ol>
<li><strong>The mark itself</strong> — the evidence must display the registered sign as used.</li>
<li><strong>The designated goods or services</strong> — use must be on the goods/services for which the mark is registered, not merely in an adjacent class.</li>
<li><strong>The user</strong> — the registrant, or a licensee; where a licensee used the mark, the licence relationship must itself be provable.</li>
<li><strong>The date</strong> — within the three years counted backwards <strong>from the date the cancellation application was filed</strong>, not from the registration date.</li>
<li><strong>The territory</strong> — use within the territorial scope of the PRC Trademark Law. Overseas sales alone are not enough.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">The same FAQ lists acceptable forms: sales contracts and service agreements <em>with their corresponding invoices</em>, inspection reports, import/export declarations and comparable transaction documents. It also states that <strong>registration information, basic company information and awards generally do not count as use evidence</strong>.</p>
"""),
            ('evidence-checklist', 'What to Archive — and What Not to Rely On', """
<table>
<thead><tr><th>Strong evidence</th><th>Commonly rejected</th></tr></thead>
<tbody>
<tr><td>Dated sales contracts with matching VAT invoices and payment records</td><td>Undated self-produced brochures</td></tr>
<tr><td>Import/export declarations, logistics and inspection reports</td><td>Handwritten receipts or contracts without a company seal</td></tr>
<tr><td>Packaging, labels and product photos showing the mark on the goods</td><td>Trademark registration certificates and company profiles</td></tr>
<tr><td>E-commerce listings with capture dates, order records and platform back-end reports</td><td>Social posts or private-chat screenshots with no third-party corroboration</td></tr>
<tr><td>Advertising insertion orders, media placements, trade-fair photos with dates</td><td>Symbolic or token use made only to defend a cancellation</td></tr>
<tr><td>Licence agreements plus the licensee's sales documents</td><td>Use of a materially different sign, or use on non-designated goods</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">CNIPA guidance and practitioner commentary consistently emphasise <strong>real, public, lawful use in the course of trade</strong> that reaches the market. A defensible alternative, where use genuinely did not occur, is to prove justified reasons — typically force majeure, government policy restrictions or bankruptcy liquidation. Lack of budget or poor sales are not accepted as justification.</p>
"""),
            ('archiving-sop', 'A Quarterly Archiving SOP', """
<ol>
<li><strong>Index by mark and by class</strong>, not by business unit. A single word mark registered in six classes needs six evidence folders.</li>
<li><strong>File English and Chinese marks separately.</strong> They are separate rights in China and need separate evidence chains.</li>
<li><strong>Capture the date at source.</strong> Screenshots need a visible capture date; contracts and invoices need the counterparty, the SKU and the mark printed on them.</li>
<li><strong>Keep the licence chain.</strong> If a distributor or licensee produces the evidence, keep the licence agreement and recordal documents beside it.</li>
<li><strong>Quarterly review, rolling three-year window.</strong> Anything older than three years should be retained but flagged as no longer protective.</li>
<li><strong>Store immutably.</strong> A shared drive with version history, timestamps or notarised copies is easier to defend than a folder assembled after a notice arrives.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">Tie this to renewal and monitoring: the same folder supports opposition evidence, enforcement complaints and renewal decisions. See our <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a>.</p>
"""),
            ('if-you-receive-a-notice', 'If a Cancellation Notice Arrives', """
<table>
<thead><tr><th>Item</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>Reply deadline</td><td><strong>2 months</strong> from receipt of the notice to submit use evidence or explain justified non-use (CNIPA FAQ / Implementing Regulations)</td></tr>
<tr><td>Electronic vs paper</td><td>Once you choose electronic submission of use evidence, subsequent documents are served electronically and further paper evidence is not accepted</td></tr>
<tr><td>One application, one class</td><td>A single non-use cancellation application can only target one class, even for a multi-class registration</td></tr>
<tr><td>Review</td><td>15 days to request review of a cancellation decision; review decided within 9 months, extendable by 3 (Art. 58)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Because the reply window is short and the evidence must pre-date the application, the work is almost entirely done before the notice exists. That is the argument for treating archiving as a routine control rather than a legal project.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Articles 2, 57, 58 and 78 of the <em>Trademark Law of the PRC (2026 Revision)</em> (CNIPA, 26 June 2026); CNIPA Trademark Office, <em>FAQ on Electronic Applications for Opposition, Non-Use Cancellation and Invalidation</em>; CNIPA public reply on evidence for non-use cancellation; CNIPA <em>Main Contents of the Revision</em> (10 July 2026). Procedures and evidence practice may be refined by the revised Implementing Regulations and Examination Guidelines. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Want a use-evidence audit before 2027?</strong> <a href="/contact.html">Request a portfolio review</a> covering each mark and class.</p></div>
"""),
        ],
    },
}}

CONTENT['ja'] = {'articles': {
    'watch': {
        'slug': 'china-trademark-opposition-watch-sop-2-months',
        'title': '異議申立期間2ヶ月対応：外国ブランドのための商標ウォッチングSOP',
        'desc': '2027年1月1日から中国の異議申立期間は2ヶ月に短縮されます。監視範囲、アラート頻度、社内決裁、常備証拠パックまで実務手順を解説します。',
        'lede': '2026年法第36条は異議申立期間を3ヶ月から2ヶ月に短縮します。登録簿の定期確認では間に合わず、担当者と事前授権を定めた運用プロセスが必要になります。',
        'card_text': '2ヶ月は「警告期間」ではなく対応チェーン全体の期限です。2027年1月1日までに監視範囲・決裁権限・証拠パックを整備してください。',
        'category': '実務プレイブック',
        'read_time': '約10分',
        'tags': ['異議申立', 'ウォッチング', '2ヶ月'],
        'related': [
            ('{HUB}', '旧法・新法の条項対比'),
            ('{ACT}', '2027年までにやるべきこと'),
            ('{L}/china-trademark-monitoring-protection.html', '商標モニタリングと保護戦略'),
        ],
        'sections': [
            ('why-two-months-changes-everything', 'なぜ2ヶ月で運用全体が変わるのか', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2027年1月1日</strong>施行の2026年商標法第36条は、異議申立期間を初步審定公告の日から<strong>2ヶ月</strong>と定めました（2019年法第33条の3ヶ月から短縮）。起算点は公告を行った日であり、自社が出願に気づいた日ではありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">CNIPA移行措置（草案）第4条は判断基準を<strong>公告日</strong>に置いています。国内出願は商標公報の公告日、中国を指定する国際登録はWIPO公告日です。2027年1月1日より前に公告された案件は3ヶ月、同日以降は2ヶ月となり、年をまたいで進行中の期間がリセットされることはありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">つまり检知、社内決裁、証拠収集、翻訳、必要な認証、現地代理人への指示を8週間以内に完了させる必要があります。四半期ごとに登録簿を確認する運用では、最初の社内会議が終わる前に異議申立の機会を失います。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>草案の扱い：</strong>移行措置は2026年11月12日まで意見募集中で、最終版は変更され得ます。社内期限を確定する前に最終条文を確認してください。</p></div>
"""),
            ('backwards-timeline', '公告日から逆算したタイムライン', """
<table>
<thead><tr><th>時点</th><th>対応</th><th>担当</th></tr></thead>
<tbody>
<tr><td>継続・週次</td><td>重点区分・サブクラス・中国語表記変形を公報で監視。アラートは担当者付きの受信箱に集約</td><td>ウォッチング提供者／知財担当</td></tr>
<tr><td>Day 0〜2</td><td>公告を検知し、同一・類似・音写・関連会社・元代理店などの抵触を分類</td><td>現地代理人</td></tr>
<tr><td>Day 3〜5</td><td>事前合意した基準で可否判断。高リスク案件は予算を自動執行</td><td>ブランド側（事前授権）</td></tr>
<tr><td>Day 6〜14</td><td>証拠パックを組み、外国語資料を翻訳、署名・委任状を整備</td><td>現地代理人＋ブランド側</td></tr>
<tr><td>Day 15〜30</td><td>電子申請で異議を提出。補充証拠の権利を留保する</td><td>中国商標代理機構</td></tr>
<tr><td>予備</td><td>休暇、国際郵送、認証、社内エスカレーションに備え最低4週間を残す</td><td>運用責任者</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">55日目の提出は法的には可能ですが、余裕がありません。SOPの目的は、提出ではなく<strong>意思決定</strong>をボトルネックにしないことです。</p>
"""),
            ('watch-configuration', 'ウォッチング設定チェックリスト', """
<ul>
<li><strong>監視対象標識：</strong>英字標、公式中国語名、一般的な音写、消費者が付けた通称、ピンイン、略称、図形商標、製品ラインごとの中国語名。</li>
<li><strong>範囲：</strong>登録済区分、将来参入し得る隣接区分、実際に使用するCNIPAサブクラス、業種ごとにハイジャッカーが出願しやすい区分。</li>
<li><strong>出願人名：</strong>自社法人名、販売店、元代理店、OEM工場、既知の出願人。かつて取引関係があった相手による出願は、関係を立証できれば悪意を主張しやすくなります。</li>
<li><strong>頻度：</strong>最低でも週次。最重要3区分は日次またはリアルタイム通知。月次の抽出調査では2ヶ月の法定期間に対応できません。</li>
<li><strong>エスカレーション：</strong>決裁者と代理担当を各1名指名し、中国代理人に委任状を常備し、期限まで10営業日を切った場合は予防的異議を出す旨を事前指示しておく。</li>
<li><strong>記録：</strong>公告日、検知日、決裁日、受理票の日付をログ化。期限超過を争われた際の証拠になります。</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">監視体制全体は<a href="{L}/china-trademark-monitoring-protection.html">商標モニタリングガイド</a>もご参照ください。</p>
"""),
            ('evidence-pack', '常備しておく証拠パック', """
<p class="leading-relaxed text-slate-300 mb-6">異議は「有名だから」ではなく資料で勝ちます。抵触出願の情報を足すだけで提出できる状態を維持してください。</p>
<ul>
<li>在先権利：本国登録、中国登録、先の出願、優先権証明書。</li>
<li>中国内の知名度：日付入り広告、報道、展示会出展、EC画面、販売店契約、抵触出願より前の販売記録。</li>
<li>相手方の悪意：他ブランドに類似する多数出願、過去の取引関係、商標を売り戻す申し出、販売店・製造業者による出願。</li>
<li>主体資料：有効な委任状と登記事項証明、およびその訳文。</li>
</ul>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>電子申請の実務：</strong>CNIPA商標局の公式FAQによれば、网上申請でアップロードする証拠は<strong>PDF</strong>形式、異議申請書の「法律依拠・事実依拠」欄は<strong>全角2000字以内</strong>です。補充証拠は申請時にその権利を留保する選択をした場合のみ可能で、<strong>3ヶ月以内</strong>に提出します。被異議申立人の答弁期限は通知受領から<strong>30日</strong>、補充証拠は答弁書で申告のうえ答弁書提出から3ヶ月以内です。</p></div>
"""),
            ('filing-mechanics', '提出後のカレンダー', """
<table>
<thead><tr><th>段階</th><th>期限・規則</th></tr></thead>
<tbody>
<tr><td>異議審理</td><td>公告期間満了から12ヶ月以内に決定、特殊情况は6ヶ月延長可（第38条）</td></tr>
<tr><td>被異議申立人の答弁</td><td>通知受領から30日（CNIPA電子申請FAQ）</td></tr>
<tr><td>補充証拠</td><td>申告のうえ3ヶ月以内、PDFのみ（同FAQ）</td></tr>
<tr><td>審理中止</td><td>第41条は他案件の結果を待つ必要がある場合の中止を明文化。引用権利が無効審判中の場合に有効</td></tr>
<tr><td>不服</td><td>異議決定に不服の場合は15日以内に復審を請求（第38条）</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">予算にはCNIPA官費、現地代理費、翻訳費、必要に応じた公証・アポスティーユを含めます。料金表は改定されるため、第三者のまとめではなく代理人に当期の金額を確認してください。</p>
"""),
            ('common-failures', '繰り返し見られる5つの失敗', """
<ol>
<li>英字標のみを監視し、中国語音写での出願を見逃す。</li>
<li>販売店や顧客からの偶然の連絡に依存する。</li>
<li>基準も代理決裁者もないまま本社承認を待つ。</li>
<li>委任状の期限切れや登記住所の変更に気づかない。</li>
<li>2ヶ月を「裁判所のように延長できる期限」と誤認する。法定期間であり交渉の余地はありません。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">最も安価な対策は手続面です。代理人の事前授権、公告日のログ、週次ウォッチ。他の4項目は<a href="{ACT}">2027年までの対応リスト</a>をご覧ください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第36条・第38条・第41条（CNIPA、2026年6月26日）、CNIPA移行措置草案通知（2026年9月28日）、CNIPA商標局『商標異議・撤三・無効宣告の网上申請に関するよくある質問』。移行措置は草案です。本記事は一般情報であり法的助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>2ヶ月対応のウォッチングを設計しますか？</strong> <a href="/contact.html">監視範囲と事前授権プロセスについてご相談ください</a>。</p></div>
"""),
        ],
    },
    'evidence': {
        'slug': 'china-trademark-non-use-cancellation-evidence',
        'title': '中国の不使用取消（撤三）：CNIPAが職権で動く前に整える使用証拠ファイル',
        'desc': '2026年商標法では当局が職権で不使用商標を取り消せます。有効な使用証拠の公式5要件、認められない資料、四半期ごとの保管手順を解説します。',
        'lede': '2027年1月1日以降、中国の登録商標は第三者請求だけでなく当局の職権によっても取り消され得ます。使用証拠の整備は初日からの運用業務になります。',
        'card_text': 'CNIPAが示す有効な使用証拠の5要件、証拠として認められにくい資料、商標・区分ごとの四半期保管ルーチン。',
        'category': '実務プレイブック',
        'read_time': '約10分',
        'tags': ['不使用取消', '使用証拠', 'ポートフォリオ監査'],
        'related': [
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '異議2ヶ月対応SOP'),
            ('{HUB}', '旧法・新法の条項対比'),
            ('{L}/china-trademark-renewal-guide.html', '商標更新ガイド'),
        ],
        'sections': [
            ('what-changed-in-2027', '2027年1月1日に変わること', """
<p class="leading-relaxed text-slate-300 mb-6">2026年法第57条は、登録商標が核定商品の通用名称になった場合、または正当な理由なく<strong>3年連続で使用されなかった</strong>場合に、何人も取消を申請できるという従来の規定を維持したうえで、第三項で<strong>当局が職権で取り消すことができる</strong>と追加しました。</p>
<p class="leading-relaxed text-slate-300 mb-6">関連する2点も影響します。第2条は情報ネットワークを通じた使用を商標使用に明示的に含め、日付入りのEC・ソーシャル記録の位置づけが明確になりました。第78条は、権利者が直前3年間に使用していない場合、被疑侵害者が損害賠償責任を負わないと定め、休眠登録は取消前でも実質的な執行力を失います。</p>
<p class="leading-relaxed text-slate-300 mb-6">取消申請に対する決定は<strong>9ヶ月以内</strong>（3ヶ月延長可、第57条）、決定に不服の場合の復審請求は<strong>15日以内</strong>です（第58条）。</p>
"""),
            ('two-sides', '一つの規則、二つの方向', """
<table>
<thead><tr><th></th><th>攻め（第三者請求）</th><th>守り（自社リスク）</th></tr></thead>
<tbody>
<tr><td>対象</td><td>登録しただけで実際に取引していないハイジャッカー／ブロッカー</td><td>現在販売していない区分に防御登録を持つ正当な外国ブランド</td></tr>
<tr><td>典型対応</td><td>不使用取消で抵触登録を除去。無効審判・買取交渉と併用</td><td>取消通知または職権調査に対し、日付入り証拠で応答</td></tr>
<tr><td>決め手</td><td>相手に真実の商業使用がないことを示す</td><td>核定商品上の継続した真実の使用を立証する</td></tr>
<tr><td>2027年の変化</td><td>民間申請がなくても当局が動ける</td><td>休眠登録が第三者からの働きかけなしに審査され得る</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">同じ改正が、ハイジャッカー排除の低コスト化と自社ポートフォリオ監査の必要性を同時にもたらします。回復手段の比較は<a href="{L}/trademark-registered-by-someone-else-china.html">「商標を先に登録された場合」</a>をご覧ください。</p>
"""),
            ('five-requirements', '有効な使用証拠の公式5要件', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPA商標局の電子申請FAQは、証拠が満たすべき要件を5つ挙げています。すべてを満たす必要があります。</p>
<ol>
<li><strong>標識</strong>——登録商標が使用されていることが資料上示されること。</li>
<li><strong>核定商品・役務</strong>——登録された商品・役務上の使用であること。隣接区分での使用では足りません。</li>
<li><strong>使用主体</strong>——登録人または被許諾者。被許諾者が使用した場合は許諾関係自体も立証が必要です。</li>
<li><strong>使用日</strong>——<strong>取消申請が提出された日から3年遡った期間内</strong>であること。登録日からではありません。</li>
<li><strong>地域</strong>——中国商標法の効力が及ぶ地域内での使用。海外販売のみでは足りません。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">同FAQは、販売契約・役務契約と<strong>対応する請求書</strong>、検査報告、輸出入申告書などを有効な形式として挙げる一方、<strong>商標登録情報・企業基本情報・受賞情報は一般に使用証拠にならない</strong>と明記しています。</p>
"""),
            ('evidence-checklist', '保管すべき資料／頼ってはいけない資料', """
<table>
<thead><tr><th>強い証拠</th><th>認められにくい資料</th></tr></thead>
<tbody>
<tr><td>日付入り販売契約＋対応する増値税発票・入金記録</td><td>日付のない自作パンフレット</td></tr>
<tr><td>輸出入申告書、物流・検査報告</td><td>手書き領収書、社印のない契約書</td></tr>
<tr><td>商標が表示された包装・ラベル・製品写真</td><td>商標登録証、会社概要</td></tr>
<tr><td>キャプチャ日付付きEC画面、受注記録、プラットフォーム管理画面</td><td>第三者裏付けのないSNS投稿・私的チャット画面</td></tr>
<tr><td>広告出稿記録、媒体掲載、日付入り展示会写真</td><td>取消対策のためだけの象徴的使用</td></tr>
<tr><td>許諾契約＋被許諾者の販売資料</td><td>登録標識と大きく異なる標識、核定外商品での使用</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">CNIPAの案内および実務解説は一貫して、市場に到達した<strong>真実・公開・適法な取引上の使用</strong>を重視します。使用が実際になかった場合の代替主張は「正当理由」、すなわち不可抗力、政府の政策制限、破産清算などです。資金不足や販売不振は正当理由に当たりません。</p>
"""),
            ('archiving-sop', '四半期ごとの保管SOP', """
<ol>
<li><strong>事業部門ではなく「商標×区分」で索引化する。</strong>6区分に登録した1つの文字商標には6つの証拠フォルダが必要です。</li>
<li><strong>英語標と中国語標を分ける。</strong>中国では別個の権利であり、別個の証拠チェーンが必要です。</li>
<li><strong>日付を発生時点で記録する。</strong>画面にはキャプチャ日付、契約・発票には相手先・SKU・商標表示を残します。</li>
<li><strong>許諾チェーンを添付する。</strong>販売店・被許諾者の資料を使う場合は許諾契約と届出資料を並べて保管します。</li>
<li><strong>四半期レビューで3年のローリング窓を維持する。</strong>3年超の資料は残しつつ、防御力が落ちたことを明示します。</li>
<li><strong>改ざん耐性のある形で保存する。</strong>版履歴のある共有ドライブ、タイムスタンプ、公証副本は、通知後に作ったフォルダより防御しやすいです。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">このフォルダは異議証拠、権利行使の申立、更新判断にもそのまま使えます。<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>と併せて運用してください。</p>
"""),
            ('if-you-receive-a-notice', '取消通知が届いたら', """
<table>
<thead><tr><th>項目</th><th>規則</th></tr></thead>
<tbody>
<tr><td>答弁期限</td><td>通知受領から<strong>2ヶ月以内</strong>に使用証拠または不使用の正当理由を提出（CNIPA FAQ／実施条例）</td></tr>
<tr><td>電子か紙か</td><td>使用証拠の電子提出を選ぶとその後の送達は電子化され、追加の紙資料は受理されません</td></tr>
<tr><td>一申請一区分</td><td>複数区分登録でも、不使用取消の1申請は1区分のみが対象</td></tr>
<tr><td>復審</td><td>取消決定への復審請求は15日、復審決定は9ヶ月以内（3ヶ月延長可、第58条）</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">答弁期間が短く、証拠は申請日前のものでなければならないため、実質的な作業は通知が来る前に終えておく必要があります。保管を法務プロジェクトではなく定型業務として扱う根拠です。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第2条・第57条・第58条・第78条（CNIPA、2026年6月26日）、CNIPA商標局『商標異議・撤三・無効宣告の网上申請に関するよくある質問』、CNIPAの不使用取消証拠に関する公開回答、CNIPA『商標法改正の主要内容』（2026年7月10日）。手続・証拠実務は改正実施条例および審査審理指南でさらに細分化される可能性があります。本記事は一般情報であり法的助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>2027年までに使用証拠を監査しますか？</strong> <a href="/contact.html">商標・区分ごとの点検をご依頼ください</a>。</p></div>
"""),
        ],
    },
}}

CONTENT['ko'] = {'articles': {
    'watch': {
        'slug': 'china-trademark-opposition-watch-sop-2-months',
        'title': '중국 이의신청 2개월 대응: 외국 브랜드를 위한 상표 워칭 SOP',
        'desc': '2027년 1월 1일부터 중국 이의신청 기간이 2개월로 단축됩니다. 감시 범위, 알림 주기, 사내 결재, 상시 증거 패키지까지 실무 절차를 정리했습니다.',
        'lede': '2026년 법 제36조는 이의신청 기간을 3개월에서 2개월로 줄입니다. 등록부를 정기적으로 확인하는 방식으로는 더 이상 대응할 수 없으며, 담당자와 사전 위임이 정해진 운영 프로세스가 필요합니다.',
        'card_text': '2개월은 "경고 기간"이 아니라 대응 체인 전체의 기한입니다. 2027년 1월 1일 전에 감시 범위·결재 권한·증거 패키지를 갖추십시오.',
        'category': '실무 플레이북',
        'read_time': '약 10분',
        'tags': ['이의신청', '워칭', '2개월'],
        'related': [
            ('{HUB}', '구법·신법 조항 대조'),
            ('{ACT}', '2027년 전에 해야 할 일'),
            ('{L}/china-trademark-monitoring-protection.html', '상표 모니터링과 보호 전략'),
        ],
        'sections': [
            ('why-two-months-changes-everything', '왜 2개월이 운영 전체를 바꾸는가', """
<p class="leading-relaxed text-slate-300 mb-6"><strong>2027년 1월 1일</strong> 시행되는 2026년 상표법 제36조는 이의신청 기간을 초보심정 공고일부터 <strong>2개월</strong>로 정했습니다(2019년 법 제33조의 3개월에서 단축). 기산점은 공고가 게재된 날이며, 자사가 출원을 알아챈 날이 아닙니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">CNIPA 경과 조치(초안) 제4조는 판단 기준을 <strong>공고일</strong>에 두고 있습니다. 국내 출원은 상표공보 공고일, 중국을 지정하는 국제등록은 WIPO 공고일입니다. 2027년 1월 1일 전에 공고된 사건은 3개월, 그날 이후 공고된 사건은 2개월이 적용되며, 연도를 넘어 진행 중인 기간은 재기산되지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">즉 탐지, 사내 결재, 증거 수집, 번역, 필요한 인증, 현지 대리인 지시를 8주 안에 마쳐야 합니다. 분기별로 등록부를 확인하는 운영으로는 첫 사내 회의가 끝나기도 전에 이의신청 기회를 잃습니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>초안 상태:</strong> 경과 조치는 2026년 11월 12일까지 의견 수렴 중이며 최종안은 달라질 수 있습니다. 사내 기한을 확정하기 전에 최종 조문을 확인하십시오.</p></div>
"""),
            ('backwards-timeline', '공고일부터 역산한 타임라인', """
<table>
<thead><tr><th>시점</th><th>조치</th><th>담당</th></tr></thead>
<tbody>
<tr><td>상시·주 단위</td><td>핵심 클래스·서브클래스·중국어 표기 변형을 공보에서 감시. 알림은 담당자가 지정된 수신함으로 집중</td><td>워칭 공급자 / IP 담당</td></tr>
<tr><td>Day 0~2</td><td>공고 탐지, 동일·유사·음역·관계사·전 대리점 등 충돌 분류</td><td>현지 대리인</td></tr>
<tr><td>Day 3~5</td><td>사전 합의된 기준으로 진행 여부 결정. 고위험 사건은 예산 자동 집행</td><td>브랜드 측(사전 위임)</td></tr>
<tr><td>Day 6~14</td><td>증거 패키지 구성, 외국어 자료 번역, 서명·위임장 정비</td><td>현지 대리인 + 브랜드 측</td></tr>
<tr><td>Day 15~30</td><td>전자 신청으로 이의 제기, 보충 증거 권리 유보</td><td>중국 상표 대리 기관</td></tr>
<tr><td>예비</td><td>휴일, 국제 우편, 인증, 사내 에스컬레이션에 대비해 최소 4주 확보</td><td>운영 책임자</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">55일차 제출은 법적으로 가능하지만 여유가 없습니다. SOP의 목적은 제출이 아니라 <strong>의사결정</strong>을 병목으로 만들지 않는 데 있습니다.</p>
"""),
            ('watch-configuration', '워칭 설정 체크리스트', """
<ul>
<li><strong>감시 표지:</strong> 영문 표장, 공식 중국어 명칭, 일반적인 음역, 소비자가 붙인 애칭, 병음, 약칭, 도형 상표, 제품 라인별 중국어 명칭.</li>
<li><strong>범위:</strong> 등록 클래스, 향후 진출 가능한 인접 클래스, 실제 사용하는 CNIPA 서브클래스, 업종별로 도용자가 자주 출원하는 클래스.</li>
<li><strong>출원인 명칭:</strong> 자사 법인명, 유통사, 전 대리점, OEM 공장, 알려진 도용자. 과거 거래 관계가 있는 상대의 출원은 관계를 입증하면 악의를 주장하기 쉽습니다.</li>
<li><strong>주기:</strong> 최소 주 1회. 가장 중요한 3개 클래스는 일 단위 또는 실시간 알림. 월 1회 표본 조사로는 2개월 법정 기간에 대응할 수 없습니다.</li>
<li><strong>에스컬레이션:</strong> 결재자와 대리 결재자를 각 1명 지정하고, 중국 대리인에게 위임장을 상비하며, 기한까지 10영업일이 남으면 예방적 이의를 제기하도록 사전 지시.</li>
<li><strong>기록:</strong> 공고일, 탐지일, 결정일, 접수증 일자를 로그로 남깁니다. 기한 초과를 다툴 때 증거가 됩니다.</li>
</ul>
<p class="leading-relaxed text-slate-300 mb-6">감시 체계 전반은 <a href="{L}/china-trademark-monitoring-protection.html">상표 모니터링 가이드</a>도 참고하십시오.</p>
"""),
            ('evidence-pack', '상시 준비할 증거 패키지', """
<p class="leading-relaxed text-slate-300 mb-6">이의신청은 "유명하다"는 이유가 아니라 자료로 이깁니다. 충돌 출원 정보만 더하면 제출할 수 있는 상태를 유지하십시오.</p>
<ul>
<li>선행권리: 본국 등록, 중국 등록, 선출원, 우선권 증명서.</li>
<li>중국 내 인지도: 날짜가 있는 광고, 보도, 전시회 참가, EC 화면, 유통 계약, 충돌 출원일 이전의 판매 기록.</li>
<li>상대방의 악의: 타 브랜드와 유사한 다수 출원, 과거 거래 관계, 상표를 되팔겠다는 제안, 유통사·제조사의 출원.</li>
<li>주체 서류: 유효한 위임장과 법인 등록 증명 및 그 번역본.</li>
</ul>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>전자출원 실무:</strong> CNIPA 상표국 공식 FAQ에 따르면 온라인으로 업로드하는 증거는 <strong>PDF</strong> 형식이며, 이의신청서의 "법적 근거·사실 근거"란은 <strong>2000자 이내</strong>입니다. 보충 증거는 신청 시 권리를 유보한 경우에만 가능하고 <strong>3개월 이내</strong>에 제출해야 합니다. 피이의신청인의 답변 기한은 통지 수령 후 <strong>30일</strong>, 보충 증거는 답변서에 명시하고 답변서 제출 후 3개월 내 제출합니다.</p></div>
"""),
            ('filing-mechanics', '제출 후의 달력', """
<table>
<thead><tr><th>단계</th><th>기한·규칙</th></tr></thead>
<tbody>
<tr><td>이의 심리</td><td>공고 기간 만료 후 12개월 내 결정, 특수 상황은 6개월 연장 가능(제38조)</td></tr>
<tr><td>피이의신청인 답변</td><td>통지 수령 후 30일(CNIPA 전자출원 FAQ)</td></tr>
<tr><td>보충 증거</td><td>신고 후 3개월 내, PDF만 가능(동 FAQ)</td></tr>
<tr><td>심리 중지</td><td>제41조는 타 사건 결과에 의존하는 경우의 중지를 명문화. 인용 권리가 무효심판 중일 때 유용</td></tr>
<tr><td>불복</td><td>이의 결정에 불복하면 15일 내 심판 청구(제38조)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">예산에는 CNIPA 관납료, 현지 대리료, 번역비, 필요한 경우 공증·아포스티유를 포함하십시오. 요금표는 개정되므로 제3자 요약이 아니라 대리인에게 당기 금액을 확인해야 합니다.</p>
"""),
            ('common-failures', '반복적으로 나타나는 다섯 가지 실패', """
<ol>
<li>영문 표장만 감시해 중국어 음역 출원을 놓치는 경우.</li>
<li>유통사나 고객의 우연한 제보에 의존하는 경우.</li>
<li>기준도 대리 결재자도 없는 상태에서 본사 승인을 기다리는 경우.</li>
<li>위임장 만료나 등록 주소 변경을 발견하지 못하는 경우.</li>
<li>2개월을 "법원처럼 연장 가능한 기한"으로 오해하는 경우. 법정 기간이며 협상 여지가 없습니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">가장 저렴한 대책은 절차입니다. 대리인 사전 위임, 공고일 로그, 주 단위 워칭. 나머지 4개 과제는 <a href="{ACT}">2027년 전 대응 목록</a>을 참고하십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제36조·제38조·제41조(CNIPA, 2026년 6월 26일), CNIPA 경과 조치 초안 공고(2026년 9월 28일), CNIPA 상표국 『상표 이의·불사용 취소·무효심판 전자출원 FAQ』. 경과 조치는 초안입니다. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>2개월 대응 워칭을 설계하시겠습니까?</strong> <a href="/contact.html">감시 범위와 사전 위임 프로세스에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'evidence': {
        'slug': 'china-trademark-non-use-cancellation-evidence',
        'title': '중국 불사용 취소: CNIPA가 직권으로 움직이기 전에 갖춰야 할 사용 증거 파일',
        'desc': '2026년 상표법은 당국이 직권으로 미사용 상표를 취소할 수 있게 합니다. 유효한 사용 증거의 공식 5요건, 인정되지 않는 자료, 분기별 보관 절차를 정리했습니다.',
        'lede': '2027년 1월 1일 이후 중국 등록상표는 제3자 청구뿐 아니라 당국의 직권으로도 취소될 수 있습니다. 사용 증거 정비는 첫날부터의 운영 업무가 됩니다.',
        'card_text': 'CNIPA가 제시한 유효 사용 증거 5요건, 증거로 인정되기 어려운 자료, 상표·클래스별 분기 보관 루틴.',
        'category': '실무 플레이북',
        'read_time': '약 10분',
        'tags': ['불사용 취소', '사용 증거', '포트폴리오 감사'],
        'related': [
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '이의 2개월 대응 SOP'),
            ('{HUB}', '구법·신법 조항 대조'),
            ('{L}/china-trademark-renewal-guide.html', '상표 갱신 가이드'),
        ],
        'sections': [
            ('what-changed-in-2027', '2027년 1월 1일에 바뀌는 것', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 법 제57조는 등록상표가 지정상품의 일반명칭이 되었거나 정당한 사유 없이 <strong>3년 연속 사용되지 않은</strong> 경우 누구나 취소를 청구할 수 있다는 기존 규정을 유지하면서, 제3항에서 <strong>당국이 직권으로 취소할 수 있다</strong>고 추가했습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">관련된 두 가지 변화도 영향을 줍니다. 제2조는 정보네트워크를 통한 사용을 상표 사용에 명시적으로 포함해 날짜가 있는 EC·소셜 기록의 지위를 분명히 했습니다. 제78조는 권리자가 직전 3년간 사용하지 않은 경우 피의 침해자가 손해배상 책임을 지지 않는다고 정해, 휴면 등록은 취소 전에도 실질적 집행력을 잃습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">취소 신청에 대한 결정은 <strong>9개월 이내</strong>(3개월 연장 가능, 제57조), 결정에 불복하는 심판 청구는 <strong>15일 이내</strong>입니다(제58조).</p>
"""),
            ('two-sides', '하나의 규칙, 두 방향', """
<table>
<thead><tr><th></th><th>공세(제3자 청구)</th><th>방어(자사 리스크)</th></tr></thead>
<tbody>
<tr><td>대상</td><td>등록만 하고 실제 거래를 하지 않은 도용자·차단권자</td><td>현재 판매하지 않는 클래스에 방어 등록을 둔 정당한 외국 브랜드</td></tr>
<tr><td>전형적 대응</td><td>불사용 취소로 충돌 등록 제거. 무효심판·매수 협상 병용</td><td>취소 통지 또는 직권 조사에 날짜가 있는 증거로 답변</td></tr>
<tr><td>결정적 요소</td><td>상대에게 진정한 상업적 사용이 없음을 입증</td><td>지정상품에 대한 지속적인 진정 사용을 입증</td></tr>
<tr><td>2027년 변화</td><td>민간 청구 없이도 당국이 움직일 수 있음</td><td>제3자 개입 없이 휴면 등록이 심사될 수 있음</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">같은 개정이 도용자 제거 비용 절감과 자사 포트폴리오 감사 필요성을 동시에 가져옵니다. 회복 수단 비교는 <a href="{L}/trademark-registered-by-someone-else-china.html">「상표를 먼저 등록당했을 때」</a>를 참고하십시오.</p>
"""),
            ('five-requirements', '유효한 사용 증거의 공식 5요건', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPA 상표국 전자출원 FAQ는 증거가 충족해야 할 요건 5가지를 제시합니다. 모두 충족해야 합니다.</p>
<ol>
<li><strong>표장</strong>——등록상표가 사용된 것이 자료에 나타나야 합니다.</li>
<li><strong>지정상품·서비스</strong>——등록된 상품·서비스에 대한 사용이어야 하며 인접 클래스 사용만으로는 부족합니다.</li>
<li><strong>사용 주체</strong>——등록권자 또는 피허락자. 피허락자가 사용했다면 허락 관계 자체도 입증해야 합니다.</li>
<li><strong>사용일</strong>——<strong>취소 신청이 제출된 날부터 3년을 소급한 기간 내</strong>여야 합니다. 등록일 기준이 아닙니다.</li>
<li><strong>지역</strong>——중국 상표법 효력이 미치는 지역 내 사용. 해외 판매만으로는 부족합니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">같은 FAQ는 판매계약·서비스계약과 <strong>이에 대응하는 세금계산서</strong>, 검사보고, 수출입 신고서 등을 유효한 형식으로 들면서, <strong>상표 등록정보·기업 기본정보·수상정보는 일반적으로 사용 증거가 되지 않는다</strong>고 명시합니다.</p>
"""),
            ('evidence-checklist', '보관할 자료 / 의존하면 안 되는 자료', """
<table>
<thead><tr><th>강한 증거</th><th>인정되기 어려운 자료</th></tr></thead>
<tbody>
<tr><td>날짜가 있는 판매계약 + 대응하는 부가세 계산서·입금 기록</td><td>날짜 없는 자체 제작 브로슈어</td></tr>
<tr><td>수출입 신고서, 물류·검사 보고</td><td>손영수증, 회사 직인이 없는 계약서</td></tr>
<tr><td>상표가 표시된 포장·라벨·제품 사진</td><td>상표 등록증, 회사 소개 자료</td></tr>
<tr><td>캡처 일자가 있는 EC 화면, 주문 기록, 플랫폼 관리자 화면</td><td>제3자 검증이 없는 SNS 게시물·개인 채팅 화면</td></tr>
<tr><td>광고 집행 기록, 매체 게재, 날짜가 있는 전시회 사진</td><td>취소 방어만을 위한 상징적 사용</td></tr>
<tr><td>허락 계약 + 피허락자의 판매 자료</td><td>등록 표장과 크게 다른 표장, 지정 외 상품에서의 사용</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">CNIPA 안내와 실무 해설은 일관되게 시장에 도달한 <strong>진실·공개·적법한 거래상 사용</strong>을 중시합니다. 사용이 실제로 없었을 때의 대안 주장은 "정당한 사유", 즉 불가항력·정부 정책 제한·파산 청산 등입니다. 자금 부족이나 판매 부진은 정당한 사유로 인정되지 않습니다.</p>
"""),
            ('archiving-sop', '분기별 보관 SOP', """
<ol>
<li><strong>사업 부서가 아니라 "상표 × 클래스"로 색인하십시오.</strong> 6개 클래스에 등록된 하나의 문자상표에는 6개의 증거 폴더가 필요합니다.</li>
<li><strong>영문 표장과 중국어 표장을 분리하십시오.</strong> 중국에서는 별개의 권리이며 별개의 증거 체인이 필요합니다.</li>
<li><strong>날짜를 발생 시점에 기록하십시오.</strong> 화면에는 캡처 일자, 계약·계산서에는 거래처·SKU·상표 표시를 남깁니다.</li>
<li><strong>허락 체인을 첨부하십시오.</strong> 유통사·피허락자 자료를 쓸 때는 허락 계약과 등록 서류를 함께 보관합니다.</li>
<li><strong>분기 검토로 3년 롤링 윈도우를 유지하십시오.</strong> 3년이 지난 자료는 보관하되 방어력이 떨어졌음을 표시합니다.</li>
<li><strong>변조에 견디는 형태로 저장하십시오.</strong> 버전 이력이 있는 공유 드라이브, 타임스탬프, 공증 사본은 통지 후에 만든 폴더보다 방어에 유리합니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">이 폴더는 이의 증거, 권리 행사 신고, 갱신 판단에도 그대로 쓰입니다. <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>와 함께 운영하십시오.</p>
"""),
            ('if-you-receive-a-notice', '취소 통지를 받았다면', """
<table>
<thead><tr><th>항목</th><th>규칙</th></tr></thead>
<tbody>
<tr><td>답변 기한</td><td>통지 수령 후 <strong>2개월 이내</strong>에 사용 증거 또는 미사용의 정당한 사유 제출(CNIPA FAQ / 시행조례)</td></tr>
<tr><td>전자 vs 서면</td><td>사용 증거의 전자 제출을 선택하면 이후 송달은 전자화되고 추가 서면 자료는 접수되지 않습니다</td></tr>
<tr><td>1 신청 1 클래스</td><td>복수 클래스 등록이라도 불사용 취소 1건은 1개 클래스만 대상</td></tr>
<tr><td>심판</td><td>취소 결정에 대한 심판 청구는 15일, 심판 결정은 9개월 이내(3개월 연장 가능, 제58조)</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">답변 기한이 짧고 증거는 신청일 이전의 것이어야 하므로, 실질 작업은 통지가 오기 전에 끝나 있어야 합니다. 보관을 법무 프로젝트가 아니라 정기 업무로 다뤄야 하는 근거입니다.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제2조·제57조·제58조·제78조(CNIPA, 2026년 6월 26일), CNIPA 상표국 『상표 이의·불사용 취소·무효심판 전자출원 FAQ』, CNIPA의 불사용 취소 증거 관련 공개 답변, CNIPA 『상표법 개정 주요 내용』(2026년 7월 10일). 절차와 증거 실무는 개정 시행조례 및 심사심리 지침에서 더 세분화될 수 있습니다. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>2027년 전에 사용 증거를 감사하시겠습니까?</strong> <a href="/contact.html">상표·클래스별 점검을 문의하세요</a>.</p></div>
"""),
        ],
    },
}}
