# -*- coding: utf-8 -*-
"""Batch 3 content (part A): 7 topics x EN/JA/KO.

Placeholders: {L} -> /blog | /blog/ja | /blog/ko ; {HUB} / {ACT} -> batch-1 URLs.
All dates are supplied by the publisher; none are baked into the copy.
Category: en Guide / ja ガイド / ko 가이드.  Read time: en 9 min / ja 約9分 / ko 약 9분.
"""

CONTENT = {}

CONTENT['en'] = {'articles': {
    'oem': {
        'slug': 'china-oem-agreement-trademark-clauses',
        'title': "Six Trademark Clauses Every China OEM Agreement Needs",
        'desc': "Your contract manufacturer sees the brand before the market does. Six clauses that stop a factory from registering your mark, overproducing under it, or walking away with your packaging and customer list.",
        'lede': "A Chinese OEM relationship is also a trademark exposure. China is a first-to-file jurisdiction, and the factory that prints your logo knows your launch date, your volumes and your designs. The inexpensive protection is not a lawsuit after registration; it is six clauses agreed before the first purchase order.",
        'card_text': "Registration bans, volume caps and audit rights, quality sampling, end-of-contract stock disposal, surviving confidentiality, and export-versus-domestic responsibility, mapped to the clauses that enforce them.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['OEM agreement', 'contract manufacturing', 'trademark ownership'],
        'related': [
            ('{L}/china-first-to-file-trademark-guide.html', 'China First-to-File Guide'),
            ('{L}/china-trademark-monitoring-protection.html', 'Trademark Monitoring and Protection'),
            ('{L}/china-trademark-squatting-decision-table.html', 'Squatting: Opposition, Invalidation or Purchase?'),
        ],
        'sections': [
            ('why-the-factory-is-a-trademark-risk', 'Why the Factory Is a Trademark Risk', """
<p class="leading-relaxed text-slate-300 mb-6">China generally awards trademark rights to the party that files first, not the party that used the mark first. A contract manufacturer sits at the worst possible point in that system: it receives your artwork, sees your seasonal volumes, knows which classes you have not covered, and can file before your own application is even prepared. Article 20 of the revised Trademark Law refuses marks identical or similar to an earlier registered or applied-for mark, Article 24 protects prior legitimate rights and addresses bad-faith squatting, and Article 19 allows refusal of applications filed with no intention to use that clearly exceed normal business needs.</p>
<p class="leading-relaxed text-slate-300 mb-6">Those provisions are a remedy, not a plan. Invoking them means opposition or invalidation proceedings, evidence of your reputation, and a period during which the factory holds a registration that can block your own filing or disrupt a platform listing. A well-drafted agreement moves the fight forward to a signature and turns a dispute about ownership into a simple breach of contract.</p>
<p class="leading-relaxed text-slate-300 mb-6">The six clauses below come from standard practitioner guidance on China manufacturing agreements. They are not exotic. What makes them work is specificity: a named right, a measurable quantity, a deadline, and a consequence that a court or arbitration panel can actually apply. Generic language about protecting intellectual property is close to worthless once a dispute starts.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Register first, contract second.</strong> A contract binds your counterparty; a registration binds the world. File your Latin and Chinese-character marks in the relevant classes before production begins, then use the agreement to close the gaps a registration cannot reach.</p></div>
"""),
            ('clauses-1-2-ownership-and-quantity', 'Clauses 1 to 2: Ownership and Volume Control', """
<p class="leading-relaxed text-slate-300 mb-6">Clause 1 is a registration ban with teeth. Prohibit the factory, its affiliates and its subcontractors from applying to register the brand, the Chinese name, the logo, the product shape or any confusingly similar variant in any jurisdiction, and require the factory to assign to you, at its own cost, any mark it has registered in breach. Add a liquidated-damages clause and a duty to cooperate in withdrawal, opposition or invalidation. Without the assignment obligation and the penalty, a ban is a promise with no remedy attached.</p>
<p class="leading-relaxed text-slate-300 mb-6">Clause 2 caps production. Authorise a maximum quantity per order and per period, require periodic reconciliation of purchase orders against finished goods, and reserve an audit right over production records, scrap and dispatch logs. The clause most drafters omit is the adverse inference: where the records cannot explain a quantity of branded goods, that quantity is treated as unauthorised production. This shifts the evidentiary burden to the party that holds the factory data.</p>
<table>
<thead><tr><th>Clause</th><th>Right created</th><th>Consequence if breached</th></tr></thead>
<tbody>
<tr><td>1. Registration ban</td><td>No filing by the factory or its affiliates; compulsory assignment of any mark obtained in breach</td><td>Liquidated damages plus a duty to cooperate in withdrawal or transfer</td></tr>
<tr><td>2. Volume cap</td><td>Fixed authorised quantity, reconciliation and audit of records</td><td>Unexplained quantities presumed unauthorised; breach of contract</td></tr>
</tbody>
</table>
"""),
            ('clauses-3-4-quality-and-exit', 'Clauses 3 to 4: Quality Control and the Exit Plan', """
<p class="leading-relaxed text-slate-300 mb-6">Clause 3 gives you sampling and inspection rights over production runs, packaging and printed materials, and states what happens when a batch fails: rejection, rework at the factory's cost, supervised destruction of defective branded goods, and suspension of further shipments. Quality control is not only about consumer safety. Uncontrolled use by a manufacturer can weaken a mark, and goods bearing your mark that you never approved are difficult to disown later.</p>
<p class="leading-relaxed text-slate-300 mb-6">Clause 4 is the exit plan, and it is where most disputes actually start. When the relationship ends, the factory may still hold finished stock, work in progress, moulds, tooling, plates, labels and packaging. Deal with each category separately and set a deadline for every one of them: sell-off of approved finished stock within a defined window, destruction or buy-back of semi-finished goods, and surrender or destruction of moulds and printing plates. Silence on these items is an invitation for a former supplier to keep producing.</p>
<p class="leading-relaxed text-slate-300 mb-6">Tie the exit clause to a short written handover checklist and a final reconciliation of quantities, so that ownership of every remaining branded item is recorded while the relationship is still cooperative rather than during a dispute.</p>
"""),
            ('clauses-5-6-secrecy-and-channels', 'Clauses 5 to 6: Secrecy and Channel Allocation', """
<p class="leading-relaxed text-slate-300 mb-6">Clause 5 covers the material the factory receives: design artwork, specifications, mould files, packaging artwork, supplier lists and customer lists. Require confidentiality, restrict use to performing the specific order, prohibit disclosure to subcontractors without written approval, and state expressly that the duty survives termination. Survival language matters because the leak usually happens after the last order, when the factory markets a near-identical product to a new client.</p>
<p class="leading-relaxed text-slate-300 mb-6">Clause 6 allocates responsibility for where the goods go. Separate export and domestic channels: state which party may sell into the Chinese market, which party handles platform authorisations and customs or regulatory records, and who bears liability if branded goods appear in an unauthorised channel. This is also where the trademark chain is documented, since a domestic sale by the factory is the fact pattern that most often turns a supplier into a squatter.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Do not rely on the contract alone.</strong> Record licences where required, keep dated use evidence, and watch the register for filings by the factory or its affiliates. Articles 55 and 57 of the revised law address licence recordal and cancellation of unused marks; a contract that is never reflected in your portfolio leaves gaps a filing can exploit.</p></div>
"""),
            ('from-contract-to-portfolio', 'From Contract to Portfolio', """
<p class="leading-relaxed text-slate-300 mb-6">The agreement should sit inside a broader filing and monitoring routine rather than replace it. Before the first production run, file the Latin word mark and the Chinese-character mark as separate applications: in China these are separate rights, and a registration for one does not cover the other. Cover the classes you sell in and the classes a supplier or squatter is likely to target, and consider separate applications for the device element rather than one combined mark.</p>
<p class="leading-relaxed text-slate-300 mb-6">Then operationalise the clauses. Put a named owner on the quantity reconciliation, keep the audit right exercisable on notice, diary the post-termination stock deadlines, and run a watch over the register and major marketplaces for filings or listings by the factory, its affiliates and its directors. Where a licence relationship exists, keep it documented so that use by the licensee can be proved.</p>
<p class="leading-relaxed text-slate-300 mb-6">When a supplier does file, treat the contract as evidence, not as a shield: the registration ban, the assignment duty and the documented relationship all strengthen a bad-faith case, but the timetable starts from the publication or filing date, not from the date you discover the problem. Decide in advance who is authorised to instruct local counsel, because the short statutory windows leave no time for a fresh internal approval chain. See our <a href="{L}/china-trademark-squatting-decision-table.html">decision table for squatted marks</a> and our <a href="{L}/china-trademark-monitoring-protection.html">monitoring guide</a>.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Basis: practitioner guidance on trademark clauses in China OEM and manufacturing agreements; Articles 19, 20, 24, 55 and 57 of the <em>Trademark Law of the PRC (2026 Revision)</em> (adopted 26 June 2026, effective 1 January 2027). The clause list reflects general industry practice, not a prescribed statutory form; have the agreement reviewed under the law governing the contract. Procedures and official practice may be refined by revised implementing regulations and examination guidelines, so confirm the current official announcements and rules with your adviser. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Want your OEM agreement reviewed against your China filings?</strong> <a href="/contact.html">Talk to our team</a> about clause drafting and portfolio alignment.</p></div>
"""),
        ],
    },
    'naming': {
        'slug': 'chinese-brand-name-cnipa-examination',
        'title': "How to Choose a Chinese Brand Name That Actually Passes CNIPA Examination",
        'desc': "A pleasant-sounding name can still be refused. The sound, form and meaning test, the three grounds that block a Chinese-character name, and a six-lane clearance search that catches the variants squatters actually file.",
        'lede': "Foreign brands often choose a Chinese name for marketing reasons and only then ask whether it can be registered. That order is backwards. In a first-to-file system, the cheaper and safer sequence is to clear the name first and fall in love with it second.",
        'card_text': "Why sound, form and meaning each create a separate conflict, how Articles 15, 17 and 19 shape registrability, and why a no-hits database search is only a risk assessment.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['Chinese brand name', 'distinctiveness', 'clearance search'],
        'related': [
            ('{L}/free-china-trademark-search-guide.html', 'Free China Trademark Search Guide'),
            ('{L}/coca-cola-chinese-name-trademark-china.html', 'How Coca-Cola Chose Its Chinese Name'),
            ('{L}/logo-vs-word-mark-china.html', 'Logo vs Word Mark in China'),
        ],
        'sections': [
            ('the-name-is-a-separate-right', 'Your Chinese Name Is a Separate Right', """
<p class="leading-relaxed text-slate-300 mb-6">A foreign brand entering China usually has a Latin mark and, sooner or later, a Chinese name. Legally these are two different rights. Registering the Latin word does not protect a Chinese-character version, and a Chinese name adopted by consumers is not automatically yours to enforce. The safer sequence is to test registrability first and choose the name second, rather than fall in love with a name, print packaging, and only then discover a blocking citation.</p>
<p class="leading-relaxed text-slate-300 mb-6">This matters because the market will produce a Chinese name whether you plan one or not. Consumers and retailers shorten, transliterate or translate foreign brands into everyday nicknames, and those nicknames are exactly what a squatter monitors. A name built purely for marketing, with a pleasant sound, an auspicious meaning and elegant characters, can still fail examination if it is descriptive, generic, or too close to an earlier filing along any of the three axes described below.</p>
<p class="leading-relaxed text-slate-300 mb-6">Treat the exercise as a legal availability question with a marketing input, not the reverse. Agree a shortlist of candidates, clear each one, and only then commission artwork and launch materials. The cost of dropping a candidate at shortlist stage is trivial compared with rebranding after a refusal.</p>
"""),
            ('three-axes-of-similarity', 'The Three Axes of Similarity: Sound, Form and Meaning', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPA examines similarity between Chinese-character marks along three axes, and a conflict on any one of them can be enough to refuse an application. Understanding them is what turns a name from something that sounds nice into something likely to survive examination.</p>
<table>
<thead><tr><th>Axis</th><th>What the examiner compares</th><th>Practical check</th></tr></thead>
<tbody>
<tr><td>Sound</td><td>Standard Mandarin pronunciation and pinyin, including tone patterns and homophones</td><td>Read candidates aloud; list same-syllable and near-syllable alternatives</td></tr>
<tr><td>Form</td><td>The structure and arrangement of the Chinese characters, radicals and stroke composition</td><td>Compare visual similarity character by character, not just the overall impression</td></tr>
<tr><td>Meaning</td><td>The sense of the characters and correspondence with the foreign mark or its translation</td><td>Check literal meaning, translated equivalents and connotations in context</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">A candidate can be clear on one axis and blocked on another: a name that reads differently but shares a distinctive character, or one that looks different but conveys the same meaning as an earlier mark. Clearance therefore has to run all three comparisons against the register, not just a search for identical characters.</p>
"""),
            ('absolute-grounds-articles-15-17-19', 'Absolute Grounds: Articles 15, 17 and 19', """
<p class="leading-relaxed text-slate-300 mb-6">Beyond conflicts with earlier rights, a name must be registrable in its own right. Article 17 refuses signs that are generic names of the goods, merely descriptive of their characteristics, or otherwise lacking distinctive character, with the important exception that a sign may become registrable where distinctiveness has been acquired through use. A name that simply states what the product is, praises its quality, or names a place or ingredient will struggle, and the exception requires a real evidence file of genuine use.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 15 sets out prohibited signs that cannot be used or registered as trademarks, and Article 19 targets bad-faith applications: a filing made with no intention to use and clearly exceeding normal business needs may be refused. For a brand owner, the practical point is the mirror image. Choose a coined, distinctive name, keep records showing an intention to use it, and avoid a portfolio of speculative defensive filings that looks like hoarding.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Coined beats descriptive.</strong> Invented combinations of characters with no direct dictionary meaning are usually easier to clear and easier to defend than a literal translation of your slogan or product category. They also give you a cleaner story when arguing acquired distinctiveness later.</p></div>
"""),
            ('six-lane-clearance-search', 'A Six-Lane Clearance Search', """
<p class="leading-relaxed text-slate-300 mb-6">A clearance search for a Chinese name has to cover six lanes. Search the Chinese characters themselves; the pinyin and its homophones; the Latin or English source word; translated equivalents of the meaning; dialect and regional phonetic variants that produce awkward or similar readings; and the colloquial names consumers have already coined for your brand. Missing the last lane is a common reason a launch-name search looks clean while the market is already using a variant a squatter can register.</p>
<p class="leading-relaxed text-slate-300 mb-6">Use the official database as one input, not as a verdict. The publicly searchable register is not real time: there is a period during which recently filed applications are not yet visible, and the data may lag. A search result is therefore a risk assessment, not a guarantee of registrability. Do not treat a no-hits result as clearance to print packaging, and do not assume a fixed blind-spot duration; check the current position with your agent rather than relying on a stated number of months.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>A no-hits result does not mean registrable.</strong> Combine an official-database search with a broader commercial search, keep dated records of what was searched and when, and refresh the search immediately before filing. Where a candidate is marginal, have a second and third choice cleared at the same time.</p></div>
"""),
            ('file-word-and-device-separately', 'File the Word and the Device Separately', """
<p class="leading-relaxed text-slate-300 mb-6">Examination looks at a combined mark element by element. When a device and a word are filed together, each component is assessed, and a problem with one element can hold up the whole application. The usual recommendation is to file the Chinese-character word mark, the Latin word mark and the device as separate applications: each stands or falls on its own, each is a separate right, and a refusal or opposition against one does not freeze the others.</p>
<p class="leading-relaxed text-slate-300 mb-6">File the English and Chinese versions together as a matter of portfolio design, not as a single composite. They protect different things and support different enforcement and use-evidence files. If the chosen name is weak on distinctiveness, plan from the start for the evidence that Article 17's acquired-distinctiveness exception requires: dated advertising, sales and marketplace records showing that consumers recognise the name as yours.</p>
<p class="leading-relaxed text-slate-300 mb-6">Finally, register in the classes you use and keep the Latin and Chinese names consistent across packaging, platform listings and company materials. Inconsistent use creates the nicknames that make a later clearance search harder. For the underlying search mechanics see our <a href="{L}/free-china-trademark-search-guide.html">free China trademark search guide</a>, and for the separate-rights question see <a href="{L}/logo-vs-word-mark-china.html">logo versus word mark</a>.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Basis: Articles 15, 17, 19 and 20 of the <em>Trademark Law of the PRC (2026 Revision)</em> (adopted 26 June 2026, effective 1 January 2027); general CNIPA examination practice on the sound, form and meaning of Chinese-character marks and on the examination of combined marks; practitioner guidance on Chinese brand naming. Official database coverage and examination standards may change, so confirm the current position and the live register against the official announcements and rules before filing. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Want a Chinese name cleared before you commit to it?</strong> <a href="/contact.html">Ask our team</a> about a sound-form-meaning search and a shortlist you can actually register.</p></div>
"""),
        ],
    },
    'refusal': {
        'slug': 'china-trademark-refusal-review-15-days',
        'title': "Trademark Refusal Review in China: The 15-Day Deadline and How to Respond",
        'desc': "A refusal starts two different clocks. The domestic 15-day review request, the 15-day and 30-day Madrid periods, and the six arguments that give a refusal review its best chance.",
        'lede': "A refusal is not the end of an application, but it does start a short clock. Under the revised law the request for review is due in 15 days, while a Madrid designation runs on a separate 15-day or 30-day timetable counted from the WIPO notification.",
        'card_text': "Which deadline applies, when supplementary evidence is due, and the six responses to a citation, from dissimilarity arguments to a parallel national filing.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['refusal review', '15-day deadline', 'Madrid designation'],
        'related': [
            ('{L}/common-reasons-trademark-rejection-china.html', 'Common Reasons for Rejection in China'),
            ('{L}/madrid-vs-direct-filing-china.html', 'Madrid vs Direct Filing in China'),
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
        ],
        'sections': [
            ('two-clocks', 'Two Clocks: The Domestic 15 Days and the Madrid Route', """
<p class="leading-relaxed text-slate-300 mb-6">A refusal is not the end of an application, but it does start a clock. Under Article 37 of the revised Trademark Law, an applicant dissatisfied with a refusal may request review within <strong>15 days</strong>; CNIPA then decides the review within <strong>nine months</strong>, extendable by <strong>three months</strong>. Miss the 15 days and the refusal becomes final on the original application, so the first job is calendaring, not advocacy.</p>
<p class="leading-relaxed text-slate-300 mb-6">International registrations designating China run on a different and easily confused timetable. When WIPO notifies a provisional refusal, the period for requesting review is counted from the date the holder receives that notification: <strong>15 days</strong> for a refusal issued ex officio and <strong>30 days</strong> for a refusal based on an opposition. These figures come from WIPO's official time-limits table and its Information Notice No. 19 of 2011. Do not assume the domestic rule and the Madrid periods are the same instrument; identify which refusal you have before computing the date.</p>
<table>
<thead><tr><th>Route</th><th>Trigger</th><th>Period to request review</th></tr></thead>
<tbody>
<tr><td>Chinese national application (Art. 37)</td><td>Receipt of the refusal</td><td>15 days</td></tr>
<tr><td>Madrid designation, ex officio refusal</td><td>Holder receives the WIPO notification of provisional refusal</td><td>15 days</td></tr>
<tr><td>Madrid designation, opposition-based refusal</td><td>Holder receives the WIPO notification of provisional refusal</td><td>30 days</td></tr>
</tbody>
</table>
"""),
            ('what-happens-after-you-file', 'What Happens After You File', """
<p class="leading-relaxed text-slate-300 mb-6">Once a review request is filed, the case is examined on its merits and on the evidence submitted with it. CNIPA's decision on a refusal review is due within nine months, extendable by three months under Article 37; those are decision targets for the authority, not deadlines for you to fill. Your evidence deadline is the one to watch: supplementary evidence in a Madrid-related review is to be submitted within <strong>three months from the date the review request is filed</strong>, per WIPO's time-limits materials.</p>
<p class="leading-relaxed text-slate-300 mb-6">That structure rewards preparation. A review request that says only that the marks are different wastes the best opportunity to put the full case on record. Where the refusal cites earlier marks, decide early whether you are arguing dissimilarity of the signs, dissimilarity of the goods or services, both, or a coexistence-based position supported by use. The chosen theory determines what evidence to gather in the weeks after filing.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Calendar three things separately:</strong> the deadline to request review, the deadline for supplementary evidence, and the date on which a decision is expected. They run from different starting points and confusing them is a common, avoidable loss.</p></div>
"""),
            ('the-six-argument-menu', 'The Six-Argument Menu', """
<p class="leading-relaxed text-slate-300 mb-6">Practitioner guidance converges on six responses to a Chinese refusal. Most cases use more than one.</p>
<ol>
<li><strong>Argue the signs and the goods.</strong> Submit a structured comparison showing the applied-for mark is not similar to the cited mark, or that the designated goods or services are not similar, with reference to the relevant sub-classes.</li>
<li><strong>Rely on coexistence or acquired distinctiveness.</strong> Put in evidence of honest concurrent use, market recognition, or distinctiveness acquired through use, so that confusion is unlikely.</li>
<li><strong>Attack the citation.</strong> Where the cited registration has not been used for three consecutive years, consider a non-use cancellation action to remove the obstacle at its source.</li>
<li><strong>Obtain a letter of consent.</strong> A coexistence agreement or consent from the earlier rights holder can resolve a citation that argument alone cannot.</li>
<li><strong>Accept a partial refusal.</strong> Where only some goods are blocked, consider narrowing the designation to preserve a filing date for the acceptable items.</li>
<li><strong>File a parallel Chinese national application.</strong> For a Madrid designation, a direct national filing can keep protection moving independently while the international refusal is contested.</li>
</ol>
"""),
            ('building-the-evidence-file', 'Building the Evidence File', """
<p class="leading-relaxed text-slate-300 mb-6">A review is won on documents. Keep any coexistence or consent document properly executed and translated, and make sure it identifies the exact marks and goods at issue. For acquired distinctiveness, assemble dated advertising, sales records, marketplace listings, media coverage and distribution materials showing that the applied-for sign identifies your business in China, not merely that it exists.</p>
<p class="leading-relaxed text-slate-300 mb-6">For a non-use cancellation against a cited mark, the evidence question is different: the issue is whether the earlier registration has been genuinely used on the designated goods, so preserve the filing date, the three-year window counted back from it, and the goods on which use must be shown. A cancellation and a refusal review are separate proceedings; coordinate them so the review record reflects the cancellation's status.</p>
<p class="leading-relaxed text-slate-300 mb-6">Keep a single indexed file: the refusal notice, the WIPO notification where relevant, the review request, every exhibit, and a dated log of submissions. If the matter later moves to an appeal or a court, that chronology is the spine of the case. For the common grounds behind refusals, see <a href="{L}/common-reasons-trademark-rejection-china.html">common reasons for rejection in China</a>.</p>
"""),
            ('a-madrid-specific-playbook', 'A Madrid-Specific Playbook', """
<p class="leading-relaxed text-slate-300 mb-6">For holders who entered China through the Madrid System, the most useful protective step is often a parallel Chinese national application. It creates an independent right that is not hostage to the fate of the international designation, and it allows a narrowed or divided filing strategy that the international registration cannot accommodate. Discuss with counsel whether the national application should claim the same scope, a reduced list of goods, or a separate Chinese-character mark.</p>
<p class="leading-relaxed text-slate-300 mb-6">Partial refusals deserve a deliberate decision rather than a reflex appeal. Where the objection is confined to part of the designation, accepting a narrower scope may preserve an early filing date for the rest while a fuller case is built. Conversely, where the blocked goods are commercially central, a parallel filing combined with a cancellation against the citation may be worth the extra work.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>The WIPO notification starts the clock.</strong> Make sure the holder's address on record is monitored and that the notification date is logged the day it arrives. A 15-day or 30-day period leaves no room to reconstruct authority, translations and evidence from scratch, so authorise local counsel before a refusal is ever issued.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Article 37 of the <em>Trademark Law of the PRC (2026 Revision)</em> (adopted 26 June 2026, effective 1 January 2027); WIPO, official time limits for responding to provisional refusals in designated contracting parties; WIPO Information Notice No. 19 of 2011. The Madrid periods are counted from the holder's receipt of the WIPO notification and differ between ex officio and opposition-based refusals; confirm the current WIPO table and the official announcements and rules with your agent. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Facing a refusal with a deadline running?</strong> <a href="/contact.html">Contact our team</a> to discuss a review strategy and a parallel filing.</p></div>
"""),
        ],
    },
    'nice': {
        'slug': 'nice-classification-13th-edition-2026-china',
        'title': "Nice Classification 13th Edition (2026): Class Changes That Affect Your China Filing",
        'desc': "From 1 January 2026 China applies the 13th edition. Eyewear, heated clothing, rescue vehicles and cream cakes moved class, Class 42 gained AI as a service, and Class 3 essential oils were split by use.",
        'lede': "China adopted the 13th edition of the Nice Classification with effect from 1 January 2026, and CNIPA has adjusted its table of similar goods and services accordingly. If your specification was written against the 12th edition, some of its items now sit in a different class.",
        'card_text': "The four class transfers, the smart-glasses exception, the new Class 42 AI item, the purpose-based split of Class 3 essential oils, and a 2026 filing checklist.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['Nice Classification', 'class changes', '13th edition'],
        'related': [
            ('{L}/china-trademark-classes-complete-guide.html', 'China Trademark Classes: Complete Guide'),
            ('{ACT}', 'What Foreign Brands Should Do Before 2027'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', 'China Trademark Registration Guide'),
        ],
        'sections': [
            ('the-cutover-date', 'The 1 January 2026 Cutover', """
<p class="leading-relaxed text-slate-300 mb-6">China adopted the <strong>13th edition (2026 text) of the Nice Classification with effect from 1 January 2026</strong>. Applications filed before that date continue to be examined under the 12th edition; the version in force on the filing date governs how goods and services are classified. That single cutover date is the fact to build a 2026 filing checklist around.</p>
<p class="leading-relaxed text-slate-300 mb-6">Nice classes are the international skeleton, but in China the working document is CNIPA's own classification of similar goods and services, which has been adjusted on the basis of the 13th edition. The table is what examiners use when they assess whether goods are similar, and it is more granular than the class headings. A filing prepared from an old class list can therefore be wrong even when the class number itself looks right.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Check the version, not just the class number.</strong> Before you reuse a specification from an earlier filing, confirm which edition it was written against and re-read the current CNIPA table for the exact item wording. Where the official text is unclear, ask your agent to check the current announcements and rules rather than assume continuity.</p></div>
"""),
            ('goods-that-moved-class', 'Goods That Moved Class', """
<p class="leading-relaxed text-slate-300 mb-6">The 13th edition moves several everyday items between classes. These are the changes that most often catch out a portfolio that was filed years earlier and is now being extended or refreshed.</p>
<table>
<thead><tr><th>Goods</th><th>From</th><th>To</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Spectacles and accessories: lenses, frames, sunglasses, contact lenses</td><td>Class 9</td><td>Class 10</td><td>Smart glasses remain in Class 9</td></tr>
<tr><td>Electrically heated clothing, including heated socks</td><td>Class 11</td><td>Class 25</td><td>Now classified with clothing</td></tr>
<tr><td>Emergency and rescue vehicles: fire engines, lifeboats and similar</td><td>Class 9</td><td>Class 12</td><td>Now classified with vehicles</td></tr>
<tr><td>Buttercream and cream cakes</td><td>Class 29</td><td>Class 30</td><td>Now classified with bakery and confectionery goods</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The spectacles change is the one with the widest reach: eyewear brands that built a Class 9 portfolio may now need Class 10 coverage, while smart-glasses products stay where they were. Do not treat the whole eyewear category as having moved. Read the item wording, keep the smart-glasses exception in mind, and review pending applications as well as registrations when you map the gap.</p>
"""),
            ('new-and-split-entries', 'New and Split Entries', """
<p class="leading-relaxed text-slate-300 mb-6">Two further changes are additions and splits rather than transfers. <strong>Class 42 gains artificial intelligence as a service (AIaaS)</strong>, giving a dedicated home for a service that previously had to be squeezed into broader computer and software items. Applicants offering AI platforms, model hosting or machine-learning services should check whether the new item gives a cleaner specification than the general software wording they used before.</p>
<p class="leading-relaxed text-slate-300 mb-6"><strong>Essential oils in Class 3 are split by intended use.</strong> Rather than a single catch-all item, classification now turns on what the oil is for, for example a cosmetic or fragrancing purpose versus another use. The practical consequence is that the wording of a Class 3 specification has to state the purpose, because the same product can fall under different items depending on how it is described and marketed.</p>
<p class="leading-relaxed text-slate-300 mb-6">For both entries, the discipline is the same: describe the actual goods or services, then find the current item, rather than copying a generic phrase from an old form and hoping the examiner will map it for you.</p>
"""),
            ('what-the-change-does-not-do', 'What the Change Does Not Do', """
<p class="leading-relaxed text-slate-300 mb-6">Classification changes do not, by themselves, rewrite earlier filings. An application is examined under the edition in force on its filing date, which is why the 1 January 2026 line matters: a pre-cutover application stays on the 12th edition, and a post-cutover filing uses the 13th. A pending application is not automatically reclassified because the table later changed.</p>
<p class="leading-relaxed text-slate-300 mb-6">What the change does affect is everything you file or extend afterwards: new applications, later designations, renewals where the specification is revisited, and the scope you choose for defensive filings. It also affects how you read similarity. CNIPA's adjusted table of similar goods and services can group items differently from the older table, so a conflict analysis prepared under the 12th edition should be re-run where it involves a moved item.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Confirm the transitional rules officially.</strong> This article states the classification changes and the general filing-date principle; it does not set out a detailed transitional regime for pending cases or existing registrations. Where the position matters to a live filing, rely on CNIPA's current announcements and rules rather than a third-party summary.</p></div>
"""),
            ('a-2026-filing-checklist', 'A 2026 Filing Checklist', """
<p class="leading-relaxed text-slate-300 mb-6">A short checklist keeps a 2026 filing programme clean:</p>
<ol>
<li><strong>Confirm the applicable edition</strong> from the filing date, and record it in the file.</li>
<li><strong>Re-read the current CNIPA table</strong> for every item, including sub-class wording, instead of reusing a specification from an earlier portfolio.</li>
<li><strong>Re-map moved goods</strong> such as eyewear, heated clothing, rescue vehicles, buttercream and cream cakes, and check whether a new class is needed or the smart-glasses exception applies.</li>
<li><strong>Use the new and split items</strong> where they fit: AI as a service in Class 42, and purpose-specific wording for essential oils in Class 3.</li>
<li><strong>Refresh defensive and watch scopes</strong> so that monitoring covers the classes goods actually moved into, not only the classes they left.</li>
<li><strong>Re-run similarity searches</strong> for any conflict analysis prepared under the 12th edition, and update agent templates and filing checklists.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">For the full class framework see our <a href="{L}/china-trademark-classes-complete-guide.html">China trademark classes guide</a> and <a href="{L}/china-trademark-registration-complete-guide-2026.html">registration guide</a>. Where an item's placement is genuinely uncertain, ask for a written check against the current official text before filing.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Basis: Nice Classification, 13th edition (2026 text), as adopted in China from 1 January 2026; CNIPA adjustments to its table of similar goods and services based on the 13th edition; the class transfers, the Class 42 AI-as-a-service addition and the purpose-based split of essential oils described above. Item wording and transitional practice should be confirmed against CNIPA's current announcements, rules and classification table before filing. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Not sure which edition your specification belongs to?</strong> <a href="/contact.html">Ask our team</a> to review your goods and services list against the current CNIPA table.</p></div>
"""),
        ],
    },
    'dynamic': {
        'slug': 'dynamic-sound-colour-marks-china-2027',
        'title': "Dynamic, Sound and Colour Marks in China: What the New Law Now Allows",
        'desc': "Article 14 adds dynamic signs, while Article 18 keeps functional features free. What the 2027 law permits, the draft filing package for dynamic marks, and the short window for acquired-distinctiveness evidence.",
        'lede': "The revised Trademark Law, effective 1 January 2027, addresses non-conventional signs expressly: Article 14 adds dynamic marks, and Article 18 sets out a functionality-based exclusion for colour, sound and dynamic signs. The filing details come from draft guidelines and may still change.",
        'card_text': "The three excluded functional categories, the MP4 and JPEG draft package, and why a claim of distinctiveness acquired through use has to be evidenced before filing.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['non-traditional marks', 'dynamic mark', '2027 law'],
        'related': [
            ('{HUB}', 'Old vs New: 2026 Trademark Law Comparison'),
            ('{L}/chinese-brand-name-cnipa-examination.html', 'Choosing a Chinese Brand Name'),
            ('{L}/logo-vs-word-mark-china.html', 'Logo vs Word Mark in China'),
        ],
        'sections': [
            ('what-changes-on-1-january-2027', 'What Changes on 1 January 2027', """
<p class="leading-relaxed text-slate-300 mb-6">The <em>Trademark Law of the PRC (2026 Revision)</em> was adopted on <strong>26 June 2026</strong> and takes effect on <strong>1 January 2027</strong>. It has nine chapters and 87 articles. Among its most visible changes is Article 14, which adds <strong>dynamic signs</strong> to the types of sign that may be registered, and Article 18, which sets out a functionality-based exclusion for colour, sound and dynamic signs.</p>
<p class="leading-relaxed text-slate-300 mb-6">For brand owners, the point is not that non-conventional marks are entirely new to Chinese practice, but that the revised statute now addresses them expressly. Colour, sound and dynamic signs are dealt with as signs that can function as trademarks while being subject to a specific exclusion: a sign must not be refused simply because it is unconventional, but it must not be allowed to monopolise a functional feature of the goods either.</p>
<p class="leading-relaxed text-slate-300 mb-6">A dynamic mark is, in essence, a mark defined by movement or change over time rather than by a static image: an animated logo, a moving sequence, or a transition that consumers recognise as identifying one undertaking. That definition drives everything else, including how the sign is filed, how distinctiveness is proved, and what the functionality exclusion is designed to keep free.</p>
"""),
            ('the-functionality-exclusion', 'The Functionality Exclusion in Article 18', """
<p class="leading-relaxed text-slate-300 mb-6">Article 18 excludes from registration signs that, for colour, sound and dynamic marks, are dictated by function rather than by brand identity. Three categories are refused:</p>
<table>
<thead><tr><th>Excluded category</th><th>What it means</th><th>Example in principle</th></tr></thead>
<tbody>
<tr><td>Resulting solely from the nature of the goods</td><td>The feature is inherent in what the product is</td><td>A colour or movement the product cannot avoid having</td></tr>
<tr><td>Necessary to obtain a technical effect</td><td>The feature makes the product work better or perform a function</td><td>A sound or motion that signals a mechanical operation</td></tr>
<tr><td>Giving the goods substantive value</td><td>The feature is a major reason customers buy the product</td><td>An aesthetic effect that is itself the product's value</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">The distinction is between a sign that <em>identifies</em> the source and a feature that <em>is</em> the product. A distinctive animated logo may be registrable; a movement that is simply how a device operates is not. Expect examination to focus on that boundary, so prepare a description that frames the sign as a badge of origin and explains why it is not dictated by function.</p>
"""),
            ('how-a-dynamic-mark-is-filed', 'How a Dynamic Mark Is Filed', """
<p class="leading-relaxed text-slate-300 mb-6">The examination guidelines for dynamic marks were published in <strong>draft form</strong> and set out a specific submission package: an <strong>MP4 video of no more than 20 MB</strong>, a set of <strong>three to nine still JPEG frames</strong>, and a written description of how the mark is used. The still frames matter because the register and the public notice are static; they define what is protected when the movement cannot be reproduced in print.</p>
<p class="leading-relaxed text-slate-300 mb-6">Choose the frames deliberately. They should capture the recognisable states of the sequence, not simply be evenly spaced snapshots, and the written description should tie them together into a single sign rather than a collection of separate images. Inconsistency between the video, the frames and the description is a straightforward route to an objection.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Draft status, so do not treat these as final.</strong> The format requirements above come from draft examination guidelines issued for comment and may change. Confirm the current filing requirements, file formats and size limits with your agent and the official guidance in force at the time of filing, and check the official announcements and rules.</p></div>
"""),
            ('acquired-distinctiveness-and-the-15-day-evidence', 'Acquired Distinctiveness and the 15-Day Evidence Window', """
<p class="leading-relaxed text-slate-300 mb-6">Like any sign, a dynamic, colour or sound mark must be distinctive. Article 17 allows a sign that lacks inherent distinctiveness to become registrable where distinctiveness has been acquired through use. For non-conventional marks that question arises often: a colour or a short motion may not be inherently seen as a badge of origin, so the applicant is asked to show that consumers have come to recognise it as identifying one business.</p>
<p class="leading-relaxed text-slate-300 mb-6">Under the draft guidelines, where the examiner requires evidence of acquired distinctiveness, it must be submitted within <strong>15 days of receipt of the notification</strong>. That is a short window, and the evidence is not something that can be assembled after the request arrives: it takes dated advertising, sales figures, media coverage and consumer-recognition material built up over real use.</p>
<p class="leading-relaxed text-slate-300 mb-6">Build the file before filing. Keep broadcast and platform records showing the animated or sound sign in use, campaign dates and reach, and examples of how the sign is presented consistently. Treat the 15-day requirement as a reason to prepare early, not as a deadline to start preparing, and remember that the draft status of the guidelines means the final period and format should be checked officially.</p>
"""),
            ('building-a-non-traditional-portfolio', 'Building a Non-Traditional Portfolio', """
<p class="leading-relaxed text-slate-300 mb-6">A non-conventional registration is a supplement to, not a replacement for, the core portfolio. File the word mark, the device mark and any Chinese-character name as separate applications first; they are simpler to clear, easier to enforce, and do not depend on a video or a sound file being reproduced correctly. Add the dynamic, colour or sound mark where the sign genuinely carries brand recognition in the market.</p>
<p class="leading-relaxed text-slate-300 mb-6">Then align the supporting materials: the use description, the still frames, the acquired-distinctiveness evidence and the advertising records should all describe the same sign used on the same goods. Inconsistency between the filing and the evidence is a common weakness in distinctiveness cases.</p>
<p class="leading-relaxed text-slate-300 mb-6">Finally, watch the implementing rules. The revised law sets the framework, but filing mechanics, formats and examination practice may be refined by revised implementing regulations and examination guidelines. Rely on the current official announcements and rules at the time you file rather than on a draft or a summary. For the underlying distinctiveness analysis see <a href="{L}/chinese-brand-name-cnipa-examination.html">choosing a Chinese brand name</a>, and for the separate-rights question see <a href="{L}/logo-vs-word-mark-china.html">logo versus word mark</a>.</p>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Primary sources: Articles 14, 17 and 18 of the <em>Trademark Law of the PRC (2026 Revision)</em> (adopted 26 June 2026, effective 1 January 2027; nine chapters, 87 articles); draft examination guidelines on dynamic marks covering the MP4 video of no more than 20 MB, three to nine JPEG still frames, the use description, and the 15-day period for acquired-distinctiveness evidence. <strong>The guidelines are a draft consultation text and may change.</strong> Confirm the current filing requirements and final implementing rules with CNIPA's official announcements and rules. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Planning a dynamic, sound or colour filing?</strong> <a href="/contact.html">Talk to our team</a> about the submission package and a distinctiveness evidence plan.</p></div>
"""),
        ],
    },
    'greaterchina': {
        'slug': 'greater-china-trademark-separate-filings',
        'title': "Hong Kong, China; Macao, China; and Taiwan, China: Separate Trademark Registrations",
        'desc': "A CNIPA registration is effective in the Chinese mainland only. Hong Kong, China; Macao, China; and Taiwan, China each have their own trademark system and need their own application, and a Madrid designation of China does not extend to them.",
        'lede': "The most common misconception about Chinese trademark protection is geographical. A CNIPA registration covers the Chinese mainland only. All three of Hong Kong, China; Macao, China; and Taiwan, China are parts of China, but each has its own trademark registry and requires a separate local filing.",
        'card_text': "What a CNIPA registration covers, why a Madrid designation does not reach the three regions, and a coordinated checklist for building protection market by market.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['regional filings', 'CNIPA scope', 'separate registrations'],
        'related': [
            ('{L}/madrid-vs-direct-filing-china.html', 'Madrid vs Direct Filing in China'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', 'China Trademark Registration Guide'),
            ('{L}/china-first-to-file-trademark-guide.html', 'China First-to-File Guide'),
        ],
        'sections': [
            ('separate-registries-within-china', 'Separate Trademark Registries Within China', """
<p class="leading-relaxed text-slate-300 mb-6">The single most common misconception about Chinese trademark protection is geographical. A registration granted by CNIPA is effective <strong>in the Chinese mainland only</strong>. It does not automatically protect the brand in Hong Kong, China; Macao, China; or Taiwan, China.</p>
<p class="leading-relaxed text-slate-300 mb-6">All three are parts of China, but each maintains its own trademark system, its own registry and its own examination practice, and each requires a separate application to its local authority. Rights are therefore territorial within China in a very practical sense: to be protected in all of these markets, a brand has to obtain protection in each of them. This is a procedural feature of how trademark rights are obtained locally, nothing more.</p>
<p class="leading-relaxed text-slate-300 mb-6">The consequence is easy to state and easy to overlook in a budget. A portfolio built only around a CNIPA registration can leave the brand unprotected in markets where the goods are actually sold, distributed or advertised. Conversely, a registration obtained in one of the three regions gives no rights in the Chinese mainland. Plan the map first, then file.</p>
"""),
            ('what-a-cnipa-registration-covers', 'What a CNIPA Registration Covers', """
<p class="leading-relaxed text-slate-300 mb-6">The coverage rules are symmetrical: a registration protects only in the place that granted it.</p>
<table>
<thead><tr><th>Registration obtained</th><th>Where it is effective</th><th>What it does not cover</th></tr></thead>
<tbody>
<tr><td>CNIPA registration</td><td>The Chinese mainland</td><td>Hong Kong, China; Macao, China; and Taiwan, China</td></tr>
<tr><td>A registration in Hong Kong, China</td><td>That region</td><td>The Chinese mainland and the other two regions</td></tr>
<tr><td>A registration in Macao, China</td><td>That region</td><td>The Chinese mainland and the other two regions</td></tr>
<tr><td>A registration in Taiwan, China</td><td>That region</td><td>The Chinese mainland and the other two regions</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Two practical points follow. First, a squatter can file in a market where you have no registration, and a CNIPA certificate will not by itself defeat that filing. Second, use evidence, licences and enforcement records have to be organised per registry, because genuine use in one place is not automatically use in another. Keep a separate file for each.</p>
"""),
            ('why-madrid-does-not-extend', 'Why a Madrid Designation Does Not Extend', """
<p class="leading-relaxed text-slate-300 mb-6">An international registration under the Madrid System that designates China is examined by CNIPA and, if accepted, produces protection in the Chinese mainland. It does <strong>not</strong> extend to Hong Kong, China; Macao, China; or Taiwan, China. Each of the three requires its own local application; a Madrid designation is not a substitute.</p>
<p class="leading-relaxed text-slate-300 mb-6">This trips up portfolios that were built centrally. A brand may hold a single international registration and assume its coverage is complete, only to find that the three local registers are untouched. When you audit an international portfolio, list the designated contracting party and then, separately, the local filings actually obtained in each of the three markets.</p>
<p class="leading-relaxed text-slate-300 mb-6">The same logic applies to watch services and renewal diaries: an alert configured only around CNIPA publications will not report filings in the three local registers. See <a href="{L}/madrid-vs-direct-filing-china.html">Madrid versus direct filing</a> for the broader route comparison.</p>
"""),
            ('planning-separate-filings', 'Planning the Separate Filings', """
<p class="leading-relaxed text-slate-300 mb-6">Because each registry is separate, plan a separate filing for each market where the brand is used or likely to be used. Applications are made to the respective local authorities under their own procedures, with their own formalities, language requirements and classification practice. Do not assume a specification accepted by CNIPA will be accepted unchanged elsewhere; have local counsel adapt the goods and services to the local table.</p>
<p class="leading-relaxed text-slate-300 mb-6">Sequence the filings around commercial exposure: the markets where goods are sold, where distributors operate, where e-commerce listings appear and where counterfeits are likely to originate. Where a launch is staged, file ahead of disclosure in each market, since a first-to-file system rewards the party that applies first. Keep the Latin mark and the Chinese-character mark as separate applications in every registry, and decide per market whether a device mark is needed.</p>
<p class="leading-relaxed text-slate-300 mb-6">We do not quote filing costs, official fees or processing times here: these vary by registry, by class and by the current fee schedules, and should be confirmed against the official announcements and rules in force at the time of filing. Ask local counsel for a current estimate for each market rather than applying a single figure across the portfolio.</p>
"""),
            ('a-coordinated-portfolio-checklist', 'A Coordinated Portfolio Checklist', """
<p class="leading-relaxed text-slate-300 mb-6">A coordinated portfolio is more than four certificates. Use this checklist:</p>
<ol>
<li><strong>Map the markets.</strong> Record, for each of the four registries, which classes, which marks and which local entity hold the rights.</li>
<li><strong>File Latin and Chinese-character names separately</strong> in each registry; they are separate rights.</li>
<li><strong>Keep use evidence per registry:</strong> dated sales, invoices, advertising and platform records that satisfy local requirements.</li>
<li><strong>Document licences and distributor relationships</strong> so that use by a local partner can be proved where needed.</li>
<li><strong>Extend watch and renewal calendars</strong> to the three local registers, not just CNIPA publications.</li>
<li><strong>Audit annually.</strong> Check owner names, addresses and class coverage, because a portfolio that drifts out of date is hard to enforce.</li>
</ol>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>One brand, four registers.</strong> For the underlying filing mechanics see our <a href="{L}/china-trademark-registration-complete-guide-2026.html">China trademark registration guide</a> and <a href="{L}/china-first-to-file-trademark-guide.html">first-to-file guide</a>; then add the three local applications as separate workstreams.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Basis: the territorial scope of CNIPA registrations, which are effective in the Chinese mainland only; the separate trademark systems of Hong Kong, China; Macao, China; and Taiwan, China, each requiring applications to its own local authority; the absence of automatic reciprocal protection between the Chinese mainland and the three regions; and the rule that a Madrid designation of China does not extend to the three regions. All three are parts of China. Filing formalities, fees and practice are set by each local authority and may change, so confirm the current official announcements and rules before filing. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Need coverage in all four registers?</strong> <a href="/contact.html">Talk to our team</a> about a coordinated filing plan for the Chinese mainland, Hong Kong, China; Macao, China; and Taiwan, China.</p></div>
"""),
        ],
    },
    'decision': {
        'slug': 'china-trademark-squatting-decision-table',
        'title': "Opposition, Invalidation or Purchase? A Cost-and-Time Decision Table for Squatted Marks",
        'desc': "Five routes to a squatted mark, compared qualitatively on timing, control, evidence and risk. Which one fits depends on where the conflicting right sits, not on a single quoted price.",
        'lede': "Discovering that someone else has filed or registered your mark in China is not one problem with one answer. Opposition, invalidation, non-use cancellation, a negotiated purchase and a fresh application differ in timing, control, evidence and risk.",
        'card_text': "A qualitative decision table for five recovery routes, plus when to combine them and why no fees, success rates or processing times belong in the comparison.",
        'category': 'Guide',
        'read_time': '9 min read',
        'tags': ['trademark squatting', 'opposition', 'invalidation'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', 'When Someone Registers Your Mark First'),
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '2-Month Opposition Watch SOP'),
            ('{L}/china-trademark-assignment-licence-recordal.html', 'Assignment and Licence Recordal'),
        ],
        'sections': [
            ('five-routes-one-decision', 'Five Routes, One Decision', """
<p class="leading-relaxed text-slate-300 mb-6">Discovering that someone else has filed or registered your mark in China is not a single problem with a single answer. There are five realistic routes, and they differ less in cost than in timing, control, evidence and risk: <strong>opposition</strong> against a published application, <strong>invalidation</strong> against a registration, <strong>non-use cancellation</strong>, a <strong>negotiated purchase or assignment</strong>, and a <strong>fresh application</strong>, sometimes with a renamed mark.</p>
<p class="leading-relaxed text-slate-300 mb-6">The right choice depends on where the conflicting right sits. A mark that is only at the publication stage is a different problem from one that has been registered for years and never used, and both differ from a registration held by a former distributor who is willing to sell. Start by establishing the status of the conflicting mark, your own prior rights, and the commercial deadline you are actually working to.</p>
<p class="leading-relaxed text-slate-300 mb-6">Two Article references frame the analysis. Article 20 refuses a mark identical or similar to an earlier registered or applied-for mark, and Article 24 protects prior legitimate rights and addresses bad-faith squatting. In practice, the strength of your evidence about prior use and reputation in China decides which routes are even available.</p>
"""),
            ('the-decision-table', 'The Decision Table', """
<p class="leading-relaxed text-slate-300 mb-6">The table below is deliberately qualitative. It compares the routes on four axes that you can assess before instructing counsel; it does <strong>not</strong> quote fees, success rates or how long proceedings take, because those depend on the case, the official fee schedules in force and the current rules. Confirm any figure against the official announcements and rules at the time you act.</p>
<table>
<thead><tr><th>Route</th><th>Timing</th><th>Control</th><th>Evidence burden</th><th>Principal risk</th></tr></thead>
<tbody>
<tr><td>Opposition</td><td>Earliest, fixed short statutory window from publication</td><td>High; you set the grounds and timing</td><td>Moderate; prior rights and reputation</td><td>Missing the window; no second chance on the same application</td></tr>
<tr><td>Invalidation</td><td>Later; subject to a statutory limitation period with an exception for bad-faith filings of well-known marks</td><td>High; full grounds can be argued</td><td>High; reputation, bad faith and prior rights</td><td>Evidence-heavy; outcome uncertain</td></tr>
<tr><td>Non-use cancellation</td><td>Available once the registration has been unused for the statutory period; the authority may also act on its own initiative</td><td>Medium; a third party or the authority may drive it</td><td>Shifts to the registrant to prove genuine use</td><td>Does not by itself give you a registration</td></tr>
<tr><td>Purchase or assignment</td><td>Negotiated; no fixed statutory timetable</td><td>Highest; commercial terms are yours to set</td><td>Low, but the transfer is examined</td><td>Approval may be refused; price and leverage</td></tr>
<tr><td>Fresh application or rename</td><td>Immediate, but starts a new filing</td><td>Medium; depends on clearing a new mark</td><td>Low for the filing; higher if arguing acquired distinctiveness</td><td>Abandoning the original name; residual conflict remains</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">Use the table to shortlist, not to decide. Most real cases combine routes: an opposition plus a protective new filing, or a cancellation alongside a negotiated purchase. The combinations are where control and risk are actually managed.</p>
"""),
            ('when-opposition-fits', 'When Opposition Fits', """
<p class="leading-relaxed text-slate-300 mb-6">Opposition is the route with the shortest fuse and the best leverage: you challenge the application before it matures into a registration. Under the revised law the opposition period is reduced from three months to <strong>two months</strong> from preliminary publication with effect from <strong>1 January 2027</strong>. That is the whole detection-to-filing chain, not a warning period.</p>
<p class="leading-relaxed text-slate-300 mb-6">It therefore only works if the watch, the decision authority and the evidence pack already exist. A brand that reviews the register occasionally will lose the window before its first internal meeting. Pre-authorise local counsel, log publication dates, and keep prior-rights and reputation documents ready so that only the conflicting application needs to be added.</p>
<p class="leading-relaxed text-slate-300 mb-6">The trade-off is that the grounds are argued on a relatively thin factual record and the other side can still respond. Where the conflict is clear and the evidence is strong, that is a good exchange. For the operating procedure see <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">the 2-month opposition watch SOP</a>.</p>
"""),
            ('when-invalidation-or-cancellation-fit', 'When Invalidation or Cancellation Fit', """
<p class="leading-relaxed text-slate-300 mb-6">Once the mark is registered, invalidation and non-use cancellation do the heavy lifting. Article 51 sets a <strong>five-year</strong> limitation period for requesting invalidation, but a bad-faith registration of a well-known mark is <strong>not subject to that five-year limit</strong>. That distinction often decides whether the route is open at all, so establish the registration date and the basis of the challenge first.</p>
<p class="leading-relaxed text-slate-300 mb-6">Article 57 addresses cancellation where a registered mark has become the generic name of the goods or has not been used for <strong>three consecutive years</strong> without justified reason, and it allows the authority to cancel on its own initiative. A cancellation is attractive against a blocker that never traded, but it clears an obstacle rather than granting you a right, so plan the filing that follows.</p>
<p class="leading-relaxed text-slate-300 mb-6">Both routes are evidence-heavy. Invalidation turns on prior rights, reputation in China and the applicant's bad faith; cancellation turns on whether genuine use exists on the designated goods. Keep dated, contract-backed records rather than assembling a file after the dispute starts. For what counts as valid use evidence see <a href="{L}/china-trademark-non-use-cancellation-evidence.html">the non-use cancellation evidence guide</a>.</p>
"""),
            ('when-to-negotiate-or-refile', 'When to Negotiate or Refile', """
<p class="leading-relaxed text-slate-300 mb-6">A negotiated purchase is often the fastest route to certainty and the one where you keep the most control: you decide the price, the scope of the assignment and any coexistence or transition terms. It is not, however, a purely private transaction. Under Article 46, an assignment that is <strong>likely to cause confusion or have other adverse effects</strong> is not approved, so the transfer is examined rather than simply recorded. Journal the commercial logic, keep the assignment documents clean, and confirm the current filing formalities before relying on the transfer.</p>
<p class="leading-relaxed text-slate-300 mb-6">A fresh application, sometimes with a renamed mark, is the pragmatic choice where the original sign is weak, the evidence is thin, or the commercial timetable cannot wait for a dispute. It is immediate, but it concedes ground: you may lose the name consumers already know, and a residual conflicting right can still block or narrow the new filing. Clear the new candidate first, including its Chinese-character version.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Decide the sequence, not just the route.</strong> Opposition, invalidation, cancellation, purchase and refiling are frequently used together, and the order changes both control and exposure. We have deliberately kept this comparison qualitative: do not rely on quoted fees, success rates or processing times from third-party summaries, and ask your adviser for the position under the current official rules.</p></div>
"""),
            ('sources', 'Sources and Caveats', """
<p class="leading-relaxed text-slate-300 mb-6">Basis: Articles 20, 24, 36, 46, 51 and 57 of the <em>Trademark Law of the PRC (2026 Revision)</em> (adopted 26 June 2026, effective 1 January 2027); general practitioner guidance on responding to squatted marks. The two-month opposition period applies from 1 January 2027; the five-year invalidation limit, its well-known-mark exception, the three-year non-use rule and the Article 46 assignment test are statutory frameworks, not predictions of outcome. This article intentionally makes only a qualitative comparison of timing, control, evidence and risk: it quotes no fees, success rates or processing durations. Confirm the current official announcements and rules before acting. This is general information, not legal advice.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>Facing a squatted mark and unsure which route to take?</strong> <a href="/contact.html">Talk to our team</a> about a case-specific sequence and evidence plan.</p></div>
"""),
        ],
    },
}}

CONTENT['ja'] = {'articles': {
    'oem': {
        'slug': 'china-oem-agreement-trademark-clauses',
        'title': '中国OEM契約に必ず入れたい商標条項6つ',
        'desc': '委託先工場は市場より先にブランドを目にします。工場による商標登録、無断増産、包装や顧客名簿の持ち出しを防ぐ6つの条項を整理しました。',
        'lede': '中国のOEM取引はそのまま商標リスクでもあります。中国は先願主義で、ロゴを印刷する工場は発売日・数量・図案を把握しています。登録後に争うより、最初の発注前に6つの条項を決めておく方がはるかに安上がりです。',
        'card_text': '登録禁止と譲渡義務、数量上限と監査権、抜取検査、契約終了時の在庫・金型処分、終了後も残る秘密保持、輸出と国内販売の責任分担。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['OEM契約', '商標条項', '委託製造'],
        'related': [
            ('{L}/china-first-to-file-trademark-guide.html', '中国の先願主義ガイド'),
            ('{L}/china-trademark-monitoring-protection.html', '商標モニタリングと保護'),
            ('{L}/china-trademark-squatting-decision-table.html', '先取り登録への対応：異議・無効・買取の判断表'),
        ],
        'sections': [
            ('why-the-factory-is-a-trademark-risk', 'なぜ工場が商標リスクになるのか', """
<p class="leading-relaxed text-slate-300 mb-6">中国では、商標権は原則として先に使った者ではなく先に出願した者に帰属します。委託先工場はその仕組みの中で最も厄介な位置にいます。図案を受け取り、季節ごとの数量を把握し、自社がまだ押さえていない区分を知っており、こちらが出願を準備する前に登録できてしまいます。2026年改正商標法第20条は、先行の登録商標または出願商標と同一・類似の標識を拒絶し、第24条は在先の適法な権益と悪意の先取り登録に対応し、第19条は使用の意思がなく通常の事業需要を明らかに超える出願を拒絶できると定めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">ただしこれらは事後救済であり、予防策ではありません。実際に使うには異議や無効宣告の手続、知名度の証拠が必要で、その間、工場が持つ登録が自社の出願を妨げたり、EC出品を止めたりします。契約書で争点を署名時点に移せば、所有権をめぐる争いを単なる債務不履行として扱えます。</p>
<p class="leading-relaxed text-slate-300 mb-6">以下6つの条項は、中国の製造委託契約に関する実務解説で繰り返し挙げられるものです。特別な工夫ではなく、権利・数量・期限・違反時の効果をそれぞれ明示できるかどうかが効き目を分けます。ブランドを守るといった漠然とした文言だけでは、争いになったときにほぼ役に立ちません。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>登録が先、契約は後。</strong> 契約は相手方を縛り、登録は世の中を縛ります。生産開始前に英字標と中国語標を必要な区分で出願し、登録では届かない隙間を契約で埋めてください。</p></div>
"""),
            ('clauses-1-2-ownership-and-quantity', '条項1〜2：権利帰属と数量管理', """
<p class="leading-relaxed text-slate-300 mb-6">条項1は、実効性のある登録禁止です。工場、その関係会社、下請けに対し、ブランド名、中国語名、ロゴ、製品形状、混同を招く類似表記の出願を各地域で禁じ、違反して取得した商標は工場負担で自社へ譲渡する義務を負わせます。さらに違約金と、取下げ・異議・無効宣告への協力義務を添えます。譲渡義務と違約金がなければ、禁止は実効手段のない約束に留まります。</p>
<p class="leading-relaxed text-slate-300 mb-6">条項2は数量の上限です。注文ごと・期間ごとの最大数量を定め、発注書と完成品の定期照合を求め、生産記録・不良品・出荷記録への監査権を留保します。抜けやすいのが不利益推定で、記録で説明できない数量のブランド品は無断生産とみなすと定めます。工場側が持つ資料に立証の負担を移す条項です。</p>
<table>
<thead><tr><th>条項</th><th>生じる権利</th><th>違反時の効果</th></tr></thead>
<tbody>
<tr><td>1. 登録禁止</td><td>工場・関係会社の出願禁止、違反取得商標の強制譲渡</td><td>違約金に加え、取下げ・移転への協力義務</td></tr>
<tr><td>2. 数量上限</td><td>許容数量の固定、記録の照合と監査</td><td>説明不能な数量は無断生産と推定、債務不履行</td></tr>
</tbody>
</table>
"""),
            ('clauses-3-4-quality-and-exit', '条項3〜4：品質管理と撤退時の処理', """
<p class="leading-relaxed text-slate-300 mb-6">条項3は、生産ロット・包装・印刷物に対する抜取検査権と、不合格時の扱いを定めます。受領拒否、工場負担での手直し、不良ブランド品の立会い廃棄、以降の出荷停止などです。品質管理は消費者の安全だけの話ではありません。製造者の管理を外れた使用は商標を弱め、承認していない自社ブランド品を後から否定するのは難しくなります。</p>
<p class="leading-relaxed text-slate-300 mb-6">条項4が撤退計画で、実際の争いの多くはここから始まります。取引終了時、工場には完成品在庫、仕掛品、金型、治具、版、ラベル、包装が残ります。それぞれ分類して期限を設けます。承認済み完成品は定めた期間内に売り切り、仕掛品は廃棄または買い取り、金型・印刷版は引き渡しまたは廃棄、といった具合です。ここを曖昧にすると、元供給先が生産を続ける余地を残します。</p>
<p class="leading-relaxed text-slate-300 mb-6">撤退条項は短い引継ぎチェックリストと最終の数量照合に結び付け、残るブランド品の帰属を、関係が円滑なうちに記録しておきます。</p>
"""),
            ('clauses-5-6-secrecy-and-channels', '条項5〜6：秘密保持と販売経路の分担', """
<p class="leading-relaxed text-slate-300 mb-6">条項5は工場が受け取る資料を扱います。設計図、仕様書、金型データ、包装図案、仕入先名簿、顧客名簿です。秘密保持を求め、当該注文の履行以外への使用を禁じ、事前の書面承認なしに下請けへ開示させず、義務が終了後も存続することを明記します。流出はたいてい最終注文の後、工場が別の取引先に似た製品を売り込むときに起きるため、存続条項が効きます。</p>
<p class="leading-relaxed text-slate-300 mb-6">条項6は製品の行き先の責任分担です。輸出と国内販売を分け、中国市場で販売できる主体、EC出店の授権や通関・規制記録の担当、承認外の経路にブランド品が出た場合の責任者を定めます。工場による国内販売は、供給先がそのまま先取り登録者になる典型例なので、ここで商標の関係も記録しておきます。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>契約だけで安心しないでください。</strong> 必要な使用許諾は届け出、日付入りの使用証拠を残し、工場やその関係会社の出願を公報で監視します。2026年改正法第55条は使用許諾の届出、第57条は不使用商標の取消を定めます。ポートフォリオに反映されない契約は、出願に突かれる隙間を残します。</p></div>
"""),
            ('from-contract-to-portfolio', '契約からポートフォリオへ', """
<p class="leading-relaxed text-slate-300 mb-6">契約は、出願・監視の運用に組み込むものであり、その代わりではありません。最初の生産前に、英字の文字商標と中国語の文字商標を別々に出願します。中国では別個の権利で、一方の登録は他方を覆いません。販売する区分に加え、供給先や先取り登録者が狙いやすい区分を押さえ、図形は結合商標にせず単独で出願することも検討します。</p>
<p class="leading-relaxed text-slate-300 mb-6">次に条項を運用に落とします。数量照合の担当者を決め、監査権を通知で行使できる状態に保ち、終了後の在庫期限を予定表に入れ、工場・関係会社・役員による出願や出品を公報と主要ECで監視します。使用許諾の関係がある場合は、被許諾者の使用を立証できるよう書類を残します。</p>
<p class="leading-relaxed text-slate-300 mb-6">工場が実際に出願したら、契約は盾ではなく証拠として扱います。登録禁止、譲渡義務、取引関係の記録はいずれも悪意の主張を強めますが、期限は問題に気づいた日ではなく公告・出願日から進みます。法定の期間が短いため、誰が現地代理人へ指示できるかを事前に決めておかないと、社内決裁を待つ時間がありません。<a href="{L}/china-trademark-squatting-decision-table.html">先取り登録の判断表</a>と<a href="{L}/china-trademark-monitoring-protection.html">モニタリングガイド</a>もご覧ください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：中国のOEM・製造委託契約における商標条項に関する実務解説、『中華人民共和国商標法（2026年改正）』第19条・第20条・第24条・第55条・第57条（2026年6月26日採択、2027年1月1日施行）。条項は法定のひな形ではなく一般の実務例です。契約は準拠法のもとで確認を受けてください。手続や実務は改正実施条例・審査審理指南で変わる可能性があるため、当期の公式公告・規則を代理人に確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>OEM契約を中国の出願と突き合わせて点検しますか？</strong> <a href="/contact.html">条項設計とポートフォリオの整合についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'naming': {
        'slug': 'chinese-brand-name-cnipa-examination',
        'title': 'CNIPAの審査を実際に通る中国語ブランド名の選び方',
        'desc': '読みが良くても拒絶されることがあります。音・形・義の三軸、中国語名を阻む三つの根拠、先取り登録者が狙う表記まで洗い出す六方向の調査を解説します。',
        'lede': '中国語名を販売上の理由で先に決め、登録できるかを後で確認する企業は少なくありません。順序が逆です。先願主義では、まず登録適性を調べ、その後に名前を決める方が安く確実です。',
        'card_text': '音・形・義がそれぞれ別の抵触を生む理由、第15条・第17条・第19条が登録適性に与える影響、そしてヒットなしの検索結果が危険度の目安に留まる理由。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['中国語ブランド名', '識別力', '先行調査'],
        'related': [
            ('{L}/free-china-trademark-search-guide.html', '無料の中国商標検索ガイド'),
            ('{L}/coca-cola-chinese-name-trademark-china.html', 'コカ・コーラが中国語名を選んだ経緯'),
            ('{L}/logo-vs-word-mark-china.html', 'ロゴ商標と文字商標の違い'),
        ],
        'sections': [
            ('the-name-is-a-separate-right', '中国語名は別個の権利', """
<p class="leading-relaxed text-slate-300 mb-6">中国に進出する外国ブランドには、英字標といずれかの中国語名があります。中国法では別個の権利です。英字の文字商標を登録しても中国語表記は守られず、消費者が使い始めた中国語名が当然に自社の権利になるわけでもありません。名前を気に入って包装を印刷し、それから阻害要因を見つけるのではなく、まず登録適性を調べてから名を決める順序が安全です。</p>
<p class="leading-relaxed text-slate-300 mb-6">そもそも、計画の有無にかかわらず市場は中国語名を作ります。消費者や小売は外国ブランドを短く呼んだり、音写したり、訳したりして通称を定着させ、先取り登録者はまさにその通称を狙います。読みが良く、縁起が良く、字面が美しいというだけで選んだ名前でも、商品そのものや品質をそのまま示すもの、あるいは後述する三軸のどれかで先行出願に近いものは、審査で拒絶され得ます。</p>
<p class="leading-relaxed text-slate-300 mb-6">これは販売面の要望を取り込んだ登録適性の問題として扱い、逆にしないでください。候補をいくつか挙げ、それぞれを調査し、それから図案や発売資料を作ります。候補の段階で名前を捨てる負担は、拒絶後に改名する負担に比べればごく小さなものです。</p>
"""),
            ('three-axes-of-similarity', '類似判断の三軸：音・形・義', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPAは中国語商標の類似を三つの軸で比べ、どれか一つで抵触しても拒絶の根拠になり得ます。この違いを押さえることが、読み心地の良い名前を審査に耐える名前へ変える第一歩です。</p>
<table>
<thead><tr><th>軸</th><th>審査で比べる点</th><th>実務上の確認</th></tr></thead>
<tbody>
<tr><td>音</td><td>普通話の読みとピンイン、声調、同音・近音</td><td>候補を声に出し、同音・近音の別表記を洗い出す</td></tr>
<tr><td>形</td><td>漢字の字形、部首、画数の構成と並び</td><td>全体の印象だけでなく、一字ずつ視覚上の近さを比べる</td></tr>
<tr><td>義</td><td>字義、外国標識やその訳語との対応</td><td>字義、訳し替え、文脈上の含意を確認する</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">ある軸で問題がなくても別の軸で引っかかる例は珍しくありません。読みは違っても目立つ一字を共有する場合や、見た目は違っても先行商標と同じ意味を伝える場合です。したがって調査は、同一の漢字を探すだけでなく、三軸すべてについて登録簿と突き合わせる必要があります。</p>
"""),
            ('absolute-grounds-articles-15-17-19', '拒絶理由：第15条・第17条・第19条', """
<p class="leading-relaxed text-slate-300 mb-6">先行権利との抵触とは別に、名前そのものに登録適性が要ります。第17条は、商品の通用名称、性質をそのまま示す表示、その他識別力を欠く標識を拒絶します。ただし使用によって識別力を得た場合は登録が認められるのが重要な例外です。商品そのものを言い表す名前、品質を賛美する名前、地名や原材料をそのまま冠する名前は通りにくく、例外を使うには真実の使用を示すまとまった証拠が要ります。</p>
<p class="leading-relaxed text-slate-300 mb-6">第15条は商標として使用・登録できない禁止標識を定め、第19条は悪意の出願を対象に、使用の意思がなく通常の事業需要を明らかに超える出願を拒絶できるとします。ブランド側にとっての教訓は裏返しです。造語で識別力の高い名前を選び、使用の意思を示す記録を残し、投機と映る防御出願の山は避けます。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>造語が記述より強い。</strong> 辞書に載らない漢字の組み合わせは、スローガンや商品分野の直訳より調査も防衛も容易で、後から使用による識別力を主張するときも筋が通ります。</p></div>
"""),
            ('six-lane-clearance-search', '六方向の先行調査', """
<p class="leading-relaxed text-slate-300 mb-6">中国語名の先行調査は六方向を覆う必要があります。漢字そのもの、ピンインと同音語、英語などの原語、意味の訳し替え、方言・地域の読みから生じる似た音や望ましくない響き、そして消費者がすでに付けた通称です。最後の方向を漏らすと、発売前の調査はきれいに見えても、市場では先取り登録者が取れる表記がすでに流通している、という事態になります。</p>
<p class="leading-relaxed text-slate-300 mb-6">公式データベースは判断材料の一つであり、結論ではありません。公開される登録簿は即時ではなく、出願してから反映されるまで空白の期間があり、データも遅れます。したがって検索結果は危険度の見取り図にとどまり、登録を保証しません。ヒットなしを包装印刷の許可と受け取らず、空白の期間を特定の月数と決めつけないでください。当期の状況は代理人に確認します。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>ヒットなしは登録可能を意味しません。</strong> 公式検索に加えて幅広い商業検索を組み合わせ、何をいつ調べたかを日付付きで残し、出願の直前に再検索します。際どい候補なら、第二・第三の案も同時に調査しておきます。</p></div>
"""),
            ('file-word-and-device-separately', '文字と図形は別々に出願する', """
<p class="leading-relaxed text-slate-300 mb-6">結合商標は要素ごとに審査されます。図形と文字を一緒に出願すると双方が調べられ、片方に問題があるだけで出願全体が止まります。そこで、中国語の文字商標、英字の文字商標、図形は別々に出願するのが定番です。それぞれが単独で成否が決まり、別個の権利になり、一つに拒絶や異議が出ても他が止まりません。</p>
<p class="leading-relaxed text-slate-300 mb-6">英字版と中国語版は、一つの結合商標としてではなく、ポートフォリオ設計として揃えて出願します。守る対象も、権利行使や使用証拠のファイルも別になります。選んだ名前の識別力が弱い場合は、第17条の例外に備え、消費者がその名前を自社と結び付けて認識していることを示す、日付入りの広告・販売・EC記録を当初から蓄積します。</p>
<p class="leading-relaxed text-slate-300 mb-6">最後に、使用する区分で登録し、包装・EC画面・会社資料で英字名と中国語名の表記を揃えます。表記が揺れると通称が生まれ、後の先行調査が難しくなります。検索の実務は<a href="{L}/free-china-trademark-search-guide.html">無料の中国商標検索ガイド</a>、別個の権利という点は<a href="{L}/logo-vs-word-mark-china.html">ロゴ商標と文字商標の違い</a>をご覧ください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第15条・第17条・第19条・第20条（2026年6月26日採択、2027年1月1日施行）、中国語商標の音・形・義および結合商標の審査に関するCNIPAの一般実務、中国語命名に関する実務解説。公式データベースの反映状況や審査基準は変わり得るため、出願前に当期の公式公告・規則と最新の登録簿を確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>決める前に中国語名を調査しますか？</strong> <a href="/contact.html">音・形・義の調査と、実際に登録できる候補一覧についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'refusal': {
        'slug': 'china-trademark-refusal-review-15-days',
        'title': '中国の拒絶復審：15日の期限と実務の答え方',
        'desc': '拒絶で動き出す二つの時計。国内出願の15日、マドリッド指定の15日・30日、そして復審を有利にする六つの主張を整理します。',
        'lede': '拒絶は出願の終わりではありませんが、短い期限の始まりです。改正法では復審請求が15日、マドリッド指定中国ではWIPO通知の受領から15日または30日という別の時計が動きます。',
        'card_text': 'どの期限が適用されるか、補充証拠はいつまでか、そして非類似の主張から並行の国内出願まで六つの対応策。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['拒絶復審', '15日期限', 'マドリッド指定'],
        'related': [
            ('{L}/common-reasons-trademark-rejection-china.html', '中国で拒絶される主な理由'),
            ('{L}/madrid-vs-direct-filing-china.html', 'マドリッド方式と直接出願の比較'),
            ('{HUB}', '旧法・新法の条項対比'),
        ],
        'sections': [
            ('two-clocks', '二つの時計：国内の15日とマドリッド経由', """
<p class="leading-relaxed text-slate-300 mb-6">拒絶は出願の終わりではなく、期限の始まりです。2026年改正商標法第37条は、拒絶に不服の出願人に<strong>15日以内</strong>の復審請求を認め、CNIPAは<strong>9ヶ月以内</strong>（<strong>3ヶ月</strong>延長可）に決定すると定めます。15日を過ぎると元の出願について拒絶が確定するため、最初の仕事は主張作りではなく期限管理です。</p>
<p class="leading-relaxed text-slate-300 mb-6">中国を指定する国際登録は、混同されやすい別の時計で動きます。WIPOが仮拒絶を通知した場合、復審請求の期間は保持者がその通知を受け取った日から起算され、職権による拒絶は<strong>15日</strong>、異議に基づく拒絶は<strong>30日</strong>です。これはWIPOの公式な期間表および2011年第19号情報通知によるものです。国内の15日と同じ規定と決めつけず、どちらの拒絶かを見極めてから起算してください。</p>
<table>
<thead><tr><th>経路</th><th>起算点</th><th>復審請求の期間</th></tr></thead>
<tbody>
<tr><td>中国の国内出願（第37条）</td><td>拒絶通知の受領</td><td>15日</td></tr>
<tr><td>マドリッド指定・職権拒絶</td><td>保持者がWIPOの仮拒絶通知を受領</td><td>15日</td></tr>
<tr><td>マドリッド指定・異議に基づく拒絶</td><td>保持者がWIPOの仮拒絶通知を受領</td><td>30日</td></tr>
</tbody>
</table>
"""),
            ('what-happens-after-you-file', '請求後に何が起きるか', """
<p class="leading-relaxed text-slate-300 mb-6">復審請求が受理されると、本案と添付資料に基づいて審理されます。第37条の9ヶ月・延長3ヶ月は当局の決定目標であり、こちらが埋める期限ではありません。注意すべきは証拠側で、マドリッド関連の復審では補充証拠を<strong>復審請求の日から3ヶ月以内</strong>に提出するものとWIPOの期間資料に示されています。</p>
<p class="leading-relaxed text-slate-300 mb-6">この構造は準備を報います。標識が違うとだけ書いた請求では、記録に全件を載せる好機を逃します。引用商標がある場合、標識の非類似、商品・役務の非類似、その両方、あるいは使用を裏付けにした共存を主張するのかを早めに決めます。選んだ筋書きが、請求後の数週間で集める証拠を決めます。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>三つを別々に予定表へ。</strong> 復審請求の期限、補充証拠の期限、決定が見込まれる時期です。起算点がそれぞれ違い、混同は避けられる損失の典型です。</p></div>
"""),
            ('the-six-argument-menu', '六つの主張の選択肢', """
<p class="leading-relaxed text-slate-300 mb-6">中国の拒絶に対する対応は、実務解説ではおおむね六つに整理され、多くの案件で複数を併用します。</p>
<ol>
<li><strong>標識と商品を争う。</strong> 出願商標が引用商標と類似しない、または指定商品・役務が類似しないことを、該当するサブクラスにも触れつつ整理して示します。</li>
<li><strong>共存または使用による識別力に拠る。</strong> 真実の並行使用、市場での認知、使用により得た識別力の資料を入れ、混同のおそれが小さいことを示します。</li>
<li><strong>引用登録を崩す。</strong> 引用登録が3年連続で使われていないなら、不使用取消で障害を元から除くことを検討します。</li>
<li><strong>同意書を取る。</strong> 先行権利者との共存合意や同意は、主張だけでは解けない引用を片付けられます。</li>
<li><strong>一部拒絶を受け入れる。</strong> 阻まれた商品が一部なら、指定を狭めて残りの出願日を守る選択があります。</li>
<li><strong>並行して中国の国内出願を出す。</strong> マドリッド指定なら、直接の国内出願が国際拒絶の行方に左右されない権利を残します。</li>
</ol>
"""),
            ('building-the-evidence-file', '証拠ファイルの作り方', """
<p class="leading-relaxed text-slate-300 mb-6">復審は資料で決まります。共存合意や同意書はきちんと作成・翻訳し、対象の商標と商品を正確に特定します。使用による識別力には、日付入りの広告、販売記録、EC画面、報道、流通資料を揃え、出願標識が中国で自社の事業を指し示すことを、単に存在するというだけでなく示します。</p>
<p class="leading-relaxed text-slate-300 mb-6">引用商標への不使用取消では証拠の争点が変わります。問題は指定商品について真実の使用があったかどうかなので、出願日、そこから遡る3年の枠、使用が求められる商品を押さえます。取消と復審は別手続なので、取消の状況が復審の記録に反映されるよう連携させます。</p>
<p class="leading-relaxed text-slate-300 mb-6">拒絶通知、該当する場合はWIPO通知、復審請求、全添付資料、提出日の一覧を一つのファイルにまとめます。後に審判や裁判へ移る場合、この時系列が案件の背骨になります。拒絶の背景は<a href="{L}/common-reasons-trademark-rejection-china.html">中国で拒絶される主な理由</a>をご覧ください。</p>
"""),
            ('a-madrid-specific-playbook', 'マドリッド特有の実務', """
<p class="leading-relaxed text-slate-300 mb-6">マドリッド制度で中国に入った保持者にとって、最も役に立つ予防策は並行する中国の国内出願であることが多くあります。国際指定の行方に左右されない別個の権利ができ、国際登録では採れない狭い指定や分割の方針も選べます。国内出願で同じ範囲にするか、商品を絞るか、別の中国語標にするかは代理人と詰めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">一部拒絶は、ただちに不服を申し立てるのではなく、意識した判断が要ります。阻まれたのが指定の一部だけなら、範囲を狭めて残りの早い出願日を確保しつつ、別途しっかりした主張を組み立てる、という選び方もあります。逆に阻まれた商品が事業の中心なら、並行出願と引用への取消を組み合わせる手間を払う価値があります。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>WIPO通知が時計を動かします。</strong> 記録上の保持者住所が監視され、通知の到着日がその日のうちに控えられるようにしてください。15日・30日の期間には、権限、翻訳、証拠をゼロから揃え直す余裕がありません。拒絶が出る前から現地代理人に委任状を預けておきます。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第37条（2026年6月26日採択、2027年1月1日施行）、WIPOの指定締約国における仮拒絶への対応期間表、WIPO 2011年第19号情報通知。マドリッドの期間は保持者がWIPO通知を受領した時から起算され、職権拒絶と異議に基づく拒絶で異なります。当期のWIPO期間表と公式公告・規則を代理人に確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>期限が迫る拒絶をお持ちですか？</strong> <a href="/contact.html">復審の方針と並行出願についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'nice': {
        'slug': 'nice-classification-13th-edition-2026-china',
        'title': 'ニス分類第13版（2026年）：中国の出願に影響する区分の移動',
        'desc': '2026年1月1日から中国は第13版を適用します。眼鏡・発熱衣類・救援車両・クリームケーキが移動し、第42類にAIの役務が加わり、第3類の精油は用途で分かれました。',
        'lede': '中国は2026年1月1日からニス分類第13版を採用し、CNIPAも『類似商品・役務区分表』を第13版に合わせて調整しました。第12版で書かれた指定商品の中には、今は別の類に入るものがあります。',
        'card_text': '四つの移動、スマートグラスの例外、第42類の新しいAI項目、用途別に分かれた第3類の精油、そして2026年の出願チェックリスト。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['ニス分類', '区分の移動', '第13版'],
        'related': [
            ('{L}/china-trademark-classes-complete-guide.html', '中国商標区分の完全ガイド'),
            ('{ACT}', '2027年までに外国ブランドがやるべきこと'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', '中国商標登録ガイド'),
        ],
        'sections': [
            ('the-cutover-date', '2026年1月1日の切替', """
<p class="leading-relaxed text-slate-300 mb-6">中国は<strong>2026年1月1日</strong>から<strong>ニス分類第13版（2026年テキスト）</strong>を採用しました。同日より前に出願された案件は引き続き第12版で審査され、商品・役務の分類は出願日に効力を持つ版に従います。2026年の出願チェックリストは、まずこの切替日を軸に組み立てます。</p>
<p class="leading-relaxed text-slate-300 mb-6">ニス分類は国際共通の骨組みですが、中国で実際に使われるのはCNIPAの『類似商品・役務区分表』で、第13版に基づいて調整済みです。審査官が商品の類似を判断するのはこちらの表で、類の見出しより細かく分かれています。古い一覧から作った指定は、類番号自体が正しく見えても中身がずれている場合があります。</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>類番号ではなく版を確認してください。</strong> 過去の出願の指定を再利用する前に、どの版で書かれたかを確かめ、現行の区分表で項目の文言を読み直します。公式文言ではっきりしない点は、継続を決めつけず代理人に当期の公告・規則を確認させてください。</p></div>
"""),
            ('goods-that-moved-class', '類が移った商品', """
<p class="leading-relaxed text-slate-300 mb-6">第13版では、日常使う商品がいくつか類を移りました。数年前に組んだポートフォリオを今まさに広げたり見直したりするとき、見落としやすい変更です。</p>
<table>
<thead><tr><th>商品</th><th>移動前</th><th>移動後</th><th>補足</th></tr></thead>
<tbody>
<tr><td>眼鏡および付属品（レンズ、フレーム、サングラス、コンタクトレンズ）</td><td>第9類</td><td>第10類</td><td>スマートグラスは第9類のまま</td></tr>
<tr><td>電気加熱式の衣類（発熱靴下を含む）</td><td>第11類</td><td>第25類</td><td>衣類と同じ扱いに</td></tr>
<tr><td>緊急救援車両（消防車、救命艇など）</td><td>第9類</td><td>第12類</td><td>車両と同じ扱いに</td></tr>
<tr><td>バタークリーム、クリームケーキ</td><td>第29類</td><td>第30類</td><td>菓子・焼き菓子と同じ扱いに</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">最も影響が広いのは眼鏡です。第9類で組んだブランドは第10類の手当てが要る一方、スマートグラスは元の類に留まります。眼鏡の分野まるごとが移ったと扱わないでください。項目の文言を読み、スマートグラスの例外を念頭に置き、登録済みだけでなく係属中の出願も含めて不足を洗い出します。</p>
"""),
            ('new-and-split-entries', '追加された項目と分かれた項目', """
<p class="leading-relaxed text-slate-300 mb-6">もう二つは移動ではなく、追加と分割です。<strong>第42類に「人工知能をサービスとして提供する役務（AIaaS）」が加わり</strong>、これまで幅広いコンピュータ・ソフトウェア項目に押し込めていた役務に専用の置き場所ができました。AI基盤、モデル提供、機械学習の役務を扱う場合、従来の幅広い文言より新しい項目の方が指定をすっきり書けるか確認します。</p>
<p class="leading-relaxed text-slate-300 mb-6"><strong>第3類の精油は用途別に分かれました。</strong> 一つの包括項目ではなく、化粧・芳香といった用途か、それ以外かで分類が変わります。実務上は、第3類の指定に用途を明記する必要があるということです。同じ製品でも、どう書き、どう売るかで該当項目が変わり得ます。</p>
<p class="leading-relaxed text-slate-300 mb-6">どちらにも共通するのは、実際の商品・役務を書き、それから現行項目を探す順序です。古い書式のありがちな文言を写して、審査官が読み替えてくれるのを期待してはいけません。</p>
"""),
            ('what-the-change-does-not-do', 'この改定が変えないこと', """
<p class="leading-relaxed text-slate-300 mb-6">分類の改定は、それだけで過去の出願を書き換えるわけではありません。出願はその日に効力を持つ版で審査されるため、2026年1月1日の線が効きます。切替前の出願は第12版のまま、切替後の出願は第13版です。後に表が変わったからといって、係属中の出願が自動で組み替わることはありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">影響が出るのは、その後に出す・広げるもの全部です。新規出願、後の指定、更新で指定を見直す場面、防御出願で選ぶ範囲などです。類似の読み方にも影響します。調整後の区分表では、旧表と項目のまとまりが違う場合があるため、移動した商品を含む抵触分析は第12版の前提で作ったものを見直します。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>経過措置は公式に確認してください。</strong> 本記事は分類の変更と出願日を基準とする一般原則を述べるもので、係属案件や既登録について詳しい経過規定を示すものではありません。実際の出願に関わる判断は、第三者のまとめではなくCNIPAの当期の公告・規則に拠ってください。</p></div>
"""),
            ('a-2026-filing-checklist', '2026年の出願チェックリスト', """
<p class="leading-relaxed text-slate-300 mb-6">2026年の出願を整える短いチェックリストです。</p>
<ol>
<li><strong>適用される版を出願日から確認</strong>し、記録に残します。</li>
<li><strong>現行のCNIPA区分表を項目ごとに読み直し</strong>、サブクラスの文言まで、過去の指定を使い回さないようにします。</li>
<li><strong>移動した商品を組み替えます。</strong> 眼鏡、発熱衣類、救援車両、バタークリーム・クリームケーキを洗い出し、新しい類が要るか、スマートグラスの例外に当たるかを確認します。</li>
<li><strong>追加・分割された項目を使います。</strong> 第42類のAIを役務として提供するもの、第3類の用途を明記した精油の文言です。</li>
<li><strong>防御出願とウォッチングの範囲を更新</strong>し、商品が出た類だけでなく移った先の類も監視に含めます。</li>
<li><strong>第12版で作った抵触分析を再検索</strong>し、代理人のひな形とチェックリストも更新します。</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">区分の全体像は<a href="{L}/china-trademark-classes-complete-guide.html">中国商標区分の完全ガイド</a>と<a href="{L}/china-trademark-registration-complete-guide-2026.html">登録ガイド</a>をご覧ください。項目の置き場所に迷う場合は、出願前に現行の公式文言での確認を書面で求めてください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：2026年1月1日から中国が採用したニス分類第13版（2026年テキスト）、第13版に基づくCNIPA『類似商品・役務区分表』の調整、および本記事で述べた類の移動・第42類へのAI役務の追加・第3類精油の用途別分割。項目の文言と経過上の取扱いは、出願前にCNIPAの当期の公告・規則・区分表で確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>指定がどの版に属するか不安ですか？</strong> <a href="/contact.html">現行のCNIPA区分表に照らして商品・役務一覧を点検します</a>。</p></div>
"""),
        ],
    },
    'dynamic': {
        'slug': 'dynamic-sound-colour-marks-china-2027',
        'title': '中国の動態・音・色彩商標：2027年施行の新法で何が認められるか',
        'desc': '第14条が動態標識を加え、第18条が機能上の特徴を排除します。新法が認める範囲、動態商標の出願パッケージ（草案）、識別力証拠の短い提出期限を解説します。',
        'lede': '2027年1月1日施行の改正商標法は、非従来型の標識を条文中で明確に扱います。第14条は動態商標を加え、第18条は色彩・音・動態について機能を理由とする排除を定めます。出願の細目は審査指南の草案に基づき、今後変わり得ます。',
        'card_text': '排除される三つの機能上の分類、MP4とJPEGによる草案の提出物、そして使用による識別力を出願前から裏付けるべき理由。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['非従来型商標', '動態商標', '2027年法'],
        'related': [
            ('{HUB}', '旧法・新法の条項対比'),
            ('{L}/chinese-brand-name-cnipa-examination.html', '中国語ブランド名の選び方'),
            ('{L}/logo-vs-word-mark-china.html', 'ロゴ商標と文字商標の違い'),
        ],
        'sections': [
            ('what-changes-on-1-january-2027', '2027年1月1日に変わること', """
<p class="leading-relaxed text-slate-300 mb-6">『中華人民共和国商標法（2026年改正）』は<strong>2026年6月26日</strong>に採択され、<strong>2027年1月1日</strong>に施行されます。全9章87条です。目立つ変更の一つが第14条で、登録できる標識に<strong>動態標識</strong>を加えました。もう一つが第18条で、色彩・音・動態の標識について機能を理由とする排除を定めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">ブランド側にとって要点は、非従来型商標が中国の実務に全く新しいというより、改正法が条文で正面から扱ったことです。色彩・音・動態は商標として機能し得る標識である一方、固有の排除に服します。型にとらわれないというだけでは拒絶されませんが、商品の機能上の特徴を独占させることも認められません。</p>
<p class="leading-relaxed text-slate-300 mb-6">動態商標とは、静止画ではなく、時間とともに動く・変わることで定義される標識です。動くロゴ、一連の動作、消費者が一の事業者を示すと認識する切り替わりなどが当たります。この定義が、出し方、識別力の立て方、そして機能性排除が何を空けておくかをすべて左右します。</p>
"""),
            ('the-functionality-exclusion', '第18条の機能性排除', """
<p class="leading-relaxed text-slate-300 mb-6">第18条は、色彩・音・動態の標識のうち、ブランドを示すものではなく機能に規定されたものを登録から排除します。拒絶されるのは次の三つです。</p>
<table>
<thead><tr><th>排除される分類</th><th>意味</th><th>原則としての例</th></tr></thead>
<tbody>
<tr><td>商品自体の性質から生じるだけのもの</td><td>その製品が本来持つ特徴である場合</td><td>製品が避けようのない色や動き</td></tr>
<tr><td>技術上の効果を得るために必要なもの</td><td>製品の働きや機能を良くする特徴</td><td>機械の作動を知らせる音や動き</td></tr>
<tr><td>商品に実質上の価値を与えるもの</td><td>顧客が買う主な理由がその特徴</td><td>そのものが製品の価値となる美観上の効果</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">線引きは、出所を<em>示す</em>標識と、製品<em>そのもの</em>である特徴の間です。識別力のある動くロゴは登録され得ますが、機器がただ動くさまは登録されません。審査はこの境界に集中すると見込まれるため、標識を出所表示として位置づけ、機能に規定されていない理由を説明する記述を用意します。</p>
"""),
            ('how-a-dynamic-mark-is-filed', '動態商標の出し方', """
<p class="leading-relaxed text-slate-300 mb-6">動態商標の審査指南は<strong>草案</strong>として示され、提出物が細かく定められています。<strong>20MB以下のMP4動画</strong>、<strong>3〜9枚のJPEG静止画</strong>、そして使用の方法を記した説明書です。静止画が要るのは、登録簿や公告が紙面上で静止しているためで、動きを再現できない場面で何が守られるかを画で定めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">切り出す枚は意識して選びます。等間隔の抜き取りではなく、一連の動きの中で認識の要となる場面を入れ、説明書は別々の図の寄せ集めではなく一つの標識として結び付けます。動画・静止画・説明の食い違いは、拒絶理由への分かりやすい入り口になります。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>草案のため、確定事項として扱わないでください。</strong> 上記の形式は意見募集にかかった審査指南の草案に基づき、変わる可能性があります。出願時の要件、形式、容量の上限は、代理人と当期の公式指針・公告・規則で確認してください。</p></div>
"""),
            ('acquired-distinctiveness-and-the-15-day-evidence', '使用による識別力と15日の証拠期限', """
<p class="leading-relaxed text-slate-300 mb-6">動態・色彩・音の標識も、他の標識と同じく識別力が要ります。第17条は、生まれつき識別力を欠く標識でも、使用によって識別力を得れば登録を認めます。非従来型ではこの論点が頻出します。色や短い動きは、それだけでは出所表示と受け取られにくいため、消費者が一の事業者を示すものとして覚えたことを示すよう求められます。</p>
<p class="leading-relaxed text-slate-300 mb-6">草案の指南では、審査官が使用による識別力の証拠を求めた場合、<strong>通知を受け取ってから15日以内</strong>に提出するものとされます。短い期限で、しかも求めが来てから作れる類の資料ではありません。日付入りの広告、販売実績、報道、消費者の認知を示す資料を、真実の使用の積み重ねとして用意しておく必要があります。</p>
<p class="leading-relaxed text-slate-300 mb-6">出願前からファイルを築きます。動く標識や音の標識を実際に使った放送・ECの記録、展開時期と到達範囲、標識を揃えて示した例を残します。15日という期限は、準備を始める期限ではなく、早めに備える理由です。指南が草案である以上、最終の期間と形式は公式に確認してください。</p>
"""),
            ('building-a-non-traditional-portfolio', '非従来型を含めたポートフォリオ作り', """
<p class="leading-relaxed text-slate-300 mb-6">非従来型の登録は、中核のポートフォリオに代わるものではなく、補うものです。まず文字商標、図形商標、中国語名を別々に出願します。こちらは調査も容易で、権利行使もしやすく、動画や音声ファイルが正しく再現されるかにも左右されません。動態・色彩・音の標識は、市場で実際に認知を担っている場合に加えます。</p>
<p class="leading-relaxed text-slate-300 mb-6">続いて付随資料を揃えます。使用方法の説明、静止画、使用による識別力の証拠、広告記録は、いずれも同じ標識が同じ商品に使われていることを示すべきです。出願と証拠の食い違いは、識別力の主張でよく見る弱点です。</p>
<p class="leading-relaxed text-slate-300 mb-6">最後に実施規則を注視します。改正法が枠組みを定め、出願の実務・形式・審査運用は改正実施条例や審査審理指南でさらに細まる可能性があります。草案や要約ではなく、出願時の当期の公式公告・規則に拠ってください。識別力の考え方は<a href="{L}/chinese-brand-name-cnipa-examination.html">中国語ブランド名の選び方</a>、別個の権利という点は<a href="{L}/logo-vs-word-mark-china.html">ロゴ商標と文字商標の違い</a>をご覧ください。</p>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第14条・第17条・第18条（2026年6月26日採択、2027年1月1日施行、全9章87条）、動態商標に関する審査指南の草案（20MB以下のMP4動画、3〜9枚のJPEG静止画、使用方法の説明、使用による識別力の証拠に15日の提出期限）。<strong>指南は草案・意見募集の段階であり、変更され得ます。</strong> 出願要件と最終の実施規則は、CNIPAの当期の公式公告・規則で確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>動態・音・色彩の出願をご検討ですか？</strong> <a href="/contact.html">提出物と識別力の証拠計画についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'greaterchina': {
        'slug': 'greater-china-trademark-separate-filings',
        'title': '中国中国香港・中国マカオ・中国台湾：別個に必要な商標登録',
        'desc': 'CNIPAの登録は中国大陸（内地）でのみ有効です。中国中国香港・中国マカオ・中国台湾はそれぞれ独自の商標制度を持ち、別々の出願が要ります。マドリッド指定中国も三地域には及びません。',
        'lede': '中国の商標保護で最も多い誤解は地理範囲に関わるものです。CNIPAの登録が効くのは中国大陸（内地）だけです。中国中国香港・中国マカオ・中国台湾はいずれも中国の一部ですが、それぞれ独自の登録簿を持ち、別個の現地出願が必要です。',
        'card_text': 'CNIPA登録が覆う範囲、マドリッド指定が三地域に及ばない理由、そして市場ごとに保護を組むための横断チェックリスト。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['地域別出願', 'CNIPAの効力範囲', '別個の登録'],
        'related': [
            ('{L}/madrid-vs-direct-filing-china.html', 'マドリッド方式と直接出願の比較'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', '中国商標登録ガイド'),
            ('{L}/china-first-to-file-trademark-guide.html', '中国の先願主義ガイド'),
        ],
        'sections': [
            ('separate-registries-within-china', '中国の中にある別個の登録簿', """
<p class="leading-relaxed text-slate-300 mb-6">中国の商標保護について最も多い誤解は、地理範囲に関わるものです。CNIPAが与えた登録の効力は<strong>中国大陸（内地）に限られ</strong>、中国中国香港・中国マカオ・中国台湾に自動には及びません。</p>
<p class="leading-relaxed text-slate-300 mb-6">三地域はいずれも中国の一部ですが、それぞれ独自の商標制度、独自の登録簿、独自の審査実務を持ち、現地の主管機関への別個の出願が必要です。したがって権利は、中国の中でも実務上は地域ごとに分かれます。これらすべての市場で保護を受けるには、その一つ一つで権利を取る必要があります。これは商標権を現地で取得する手続上の仕組みであり、それ以上の意味を持つものではありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">結果は単純ですが、予算で見落とされがちです。CNIPA登録だけに頼ったポートフォリオでは、実際に販売・流通・宣伝している市場で自社が守られない状態を残します。逆に、三地域のどこかで得た登録も中国大陸（内地）では権利を生みません。まず範囲を描き、それから出願してください。</p>
"""),
            ('what-a-cnipa-registration-covers', 'CNIPA登録が覆う範囲', """
<p class="leading-relaxed text-slate-300 mb-6">効力の規則は対称で、登録は与えた場所でしか守りません。</p>
<table>
<thead><tr><th>取得した登録</th><th>効力が及ぶ場所</th><th>及ばない場所</th></tr></thead>
<tbody>
<tr><td>CNIPA登録</td><td>中国大陸（内地）</td><td>中国中国香港・中国マカオ・中国台湾</td></tr>
<tr><td>中国香港での登録</td><td>当該地域</td><td>中国大陸（内地）と他の二地域</td></tr>
<tr><td>中国マカオでの登録</td><td>当該地域</td><td>中国大陸（内地）と他の二地域</td></tr>
<tr><td>中国台湾での登録</td><td>当該地域</td><td>中国大陸（内地）と他の二地域</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">実務上の帰結が二つあります。第一に、自社が登録を持たない市場では先取り登録者が出願でき、CNIPAの登録証だけではその出願を退けられません。第二に、使用証拠・使用許諾・権利行使の記録は登録簿ごとに整理が要り、ある場所での真実の使用が別の場所での使用になるわけではありません。それぞれ別のファイルを保管します。</p>
"""),
            ('why-madrid-does-not-extend', 'マドリッド指定が及ばない理由', """
<p class="leading-relaxed text-slate-300 mb-6">マドリッド制度に基づき中国を指定する国際登録は、CNIPAが審査し、認められれば中国大陸（内地）で保護を生みます。中国中国香港・中国マカオ・中国台湾には<strong>及びません</strong>。三地域にはそれぞれ現地の出願が要り、マドリッド指定はその代わりになりません。</p>
<p class="leading-relaxed text-slate-300 mb-6">これは、国際登録を軸に組んだポートフォリオがつまずく点です。一件の国際登録があれば覆いが済むと考えたら、三地域の現地登録簿が手つかずだった、ということになりかねません。国際ポートフォリオを点検するときは、指定先を書き出したうえで、三地域で実際に取得した現地出願を別に一覧にします。</p>
<p class="leading-relaxed text-slate-300 mb-6">同じ理屈がウォッチングと更新の予定表にも当てはまります。CNIPAの公告だけを追う監視では、三地域の現地登録簿への出願を拾えません。経路の比較は<a href="{L}/madrid-vs-direct-filing-china.html">マドリッド方式と直接出願の比較</a>をご覧ください。</p>
"""),
            ('planning-separate-filings', '別個の出願をどう組むか', """
<p class="leading-relaxed text-slate-300 mb-6">登録簿が別々なので、ブランドを使う市場、あるいは使う見込みの市場ごとに別の出願を組みます。出願は各地域の主管機関へ、それぞれの手続・書式・言語・分類実務に従って行います。CNIPAで通った指定が他でもそのまま通るとは限らないため、現地の区分表に合わせて商品・役務を現地代理人に調整させます。</p>
<p class="leading-relaxed text-slate-300 mb-6">順番は事業上の露出に合わせます。商品が売れる市場、販売店が動く市場、ECに出品が出る市場、模倣品が出やすい市場です。段階を追って展開するなら、先願主義では先に出願した者が有利なので、各地域で開示より先に出願します。英字標と中国語標はどの登録簿でも別々の出願とし、図形商標が要るかは市場ごとに決めます。</p>
<p class="leading-relaxed text-slate-300 mb-6">ここでは出願費用・官費・処理期間の金額や数値を掲げません。登録簿・区分・当期の料金表によって変わり、出願時の公式公告・規則で確認すべきものです。ポートフォリオ全体に一つの数字を当てはめず、市場ごとに現地代理人へ当期の見積りを求めてください。</p>
"""),
            ('a-coordinated-portfolio-checklist', '横断して整えるポートフォリオ・チェックリスト', """
<p class="leading-relaxed text-slate-300 mb-6">横断して整えたポートフォリオは、四つの登録証以上のものです。次を使ってください。</p>
<ol>
<li><strong>市場を書き出す。</strong> 四つの登録簿それぞれについて、どの類・どの標識・どの現地法人が権利を持つかを記録します。</li>
<li><strong>英字名と中国語名を別々に出願</strong>します。別個の権利です。</li>
<li><strong>使用証拠を登録簿ごとに保管</strong>します。現地の要件を満たす、日付入りの販売・請求書・広告・EC記録です。</li>
<li><strong>使用許諾と販売店の関係を書面化</strong>し、必要に応じて現地提携先の使用を立証できるようにします。</li>
<li><strong>ウォッチングと更新の予定表を三地域の登録簿まで広げ</strong>、CNIPAの公告だけに限定しません。</li>
<li><strong>毎年点検します。</strong> 権利者名・住所・類の範囲を確認します。古くなったポートフォリオは権利行使が難しくなります。</li>
</ol>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>一つのブランド、四つの登録簿。</strong> 出願の基本は<a href="{L}/china-trademark-registration-complete-guide-2026.html">中国商標登録ガイド</a>と<a href="{L}/china-first-to-file-trademark-guide.html">先願主義ガイド</a>をご覧のうえ、三地域の現地出願を別の作業として加えてください。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：CNIPA登録の効力が中国大陸（内地）に限られること、中国中国香港・中国マカオ・中国台湾がそれぞれ独自の商標制度を持ち各地の主管機関への出願を要すること、中国大陸（内地）と三地域の間に自動の相互保護がないこと、およびマドリッド指定中国が三地域に及ばないこと。三地域はいずれも中国の一部です。出願の書式・費用・実務は各地の主管機関が定め、変わり得るため、出願前に当期の公式公告・規則を確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>四つの登録簿すべてを押さえますか？</strong> <a href="/contact.html">中国大陸（内地）、中国香港、中国マカオ、中国台湾を通す横断して組む出願計画についてご相談ください</a>。</p></div>
"""),
        ],
    },
    'decision': {
        'slug': 'china-trademark-squatting-decision-table',
        'title': '異議・無効宣告・買取のどれを選ぶか：先取り登録の比較表',
        'desc': '先取り登録への五つの経路を、時間・主導権・証拠・リスクで比べます。どれが合うかは、抵触する権利がどの段階にあるかで決まります。',
        'lede': '自社の商標を他者が中国で出願・登録していたと分かっても、答えは一つではありません。異議、無効宣告、不使用取消、買取交渉、再出願は、時間・主導権・証拠・リスクがそれぞれ違います。',
        'card_text': '五つの回復経路の比較表、組み合わせる場面、そして費用・成功率・審理期間を表に載せない理由。',
        'category': 'ガイド',
        'read_time': '約9分',
        'tags': ['先取り登録', '異議申立', '無効宣告'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', '商標を先に登録されたときは'),
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '異議2ヶ月対応の手順'),
            ('{L}/china-trademark-assignment-licence-recordal.html', '譲渡と使用許諾の届出'),
        ],
        'sections': [
            ('five-routes-one-decision', '五つの経路、一つの判断', """
<p class="leading-relaxed text-slate-300 mb-6">自社の商標を他者が中国で出願・登録していたと分かっても、一つの問題に一つの答えがあるわけではありません。現実に使える経路は五つで、違いは費用より、時間・主導権・証拠・リスクに表れます。公告された出願に対する<strong>異議申立</strong>、登録に対する<strong>無効宣告</strong>、<strong>不使用取消</strong>、<strong>買取・譲渡の交渉</strong>、そして<strong>新たな出願</strong>で、場合により改名を伴います。</p>
<p class="leading-relaxed text-slate-300 mb-6">どれが適するかは、抵触する権利がどの段階にあるかで決まります。公告の段階にある出願と、長年登録されて一度も使われていない登録は別問題ですし、売る意思のある元販売店が持つ登録はさらに別です。まず抵触商標の状態、自社の在先権利、そして実際に追っている事業上の期限を確定します。</p>
<p class="leading-relaxed text-slate-300 mb-6">枠組みになる条文が二つあります。第20条は先行の登録・出願商標と同一・類似の標識を拒絶し、第24条は在先の適法な権益と悪意の先取り登録に対応します。実際にどの経路が使えるかを決めるのは、中国における先行使用と知名度の証拠の強さです。</p>
"""),
            ('the-decision-table', '判断のための比較表', """
<p class="leading-relaxed text-slate-300 mb-6">下表は数値を置かずにまとめました。代理人へ指示する前に見極められる四つの軸で比べ、<strong>費用・成功率・審理に要する期間は掲げません</strong>。案件、当期の官費表、現行規則によって変わるためです。数値は行動する時点の公式公告・規則で確認してください。</p>
<table>
<thead><tr><th>経路</th><th>時間</th><th>主導権</th><th>証拠の負担</th><th>主なリスク</th></tr></thead>
<tbody>
<tr><td>異議申立</td><td>最も早い段階。公告から始まる短い法定期間</td><td>高い。理由と時期を自社で決める</td><td>中程度。在先権利と知名度</td><td>期間を失うと同じ出願で再び争えない</td></tr>
<tr><td>無効宣告</td><td>後段階。法定期間の制約があり、著名商標の悪意登録には例外</td><td>高い。理由を広く主張できる</td><td>重い。知名度・悪意・在先権利</td><td>証拠依存で結末が読みにくい</td></tr>
<tr><td>不使用取消</td><td>法定期間にわたり使用がない状態になってから。当局が職権で動くこともある</td><td>中程度。第三者または当局が主導し得る</td><td>真実の使用を登録者が立証する側へ移る</td><td>それ自体は自社に登録を与えない</td></tr>
<tr><td>買取・譲渡</td><td>交渉次第で、法定の決まった予定表はない</td><td>最も高い。取引条件を自社で決める</td><td>軽いが、移転は審査される</td><td>認可されない可能性、価格と交渉力</td></tr>
<tr><td>再出願・改名</td><td>すぐ動けるが、新しい出願として始まる</td><td>中程度。新しい標識を調査できるか次第</td><td>出願は軽い。識別力の立証なら重い</td><td>元の名前を手放すこと、残る抵触</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">表は候補を絞るために使い、決定そのものには使わないでください。実際には異議と予防を兼ねた新規出願、取消と並行する買取交渉などを組み合わせるのが普通で、主導権とリスクを管理できるのはその組み合わせの部分です。</p>
"""),
            ('when-opposition-fits', '異議が向く場面', """
<p class="leading-relaxed text-slate-300 mb-6">異議申立は、期限が最も短い一方で効果が最も大きい経路です。出願が登録に育つ前に争えます。改正法では<strong>2027年1月1日</strong>から異議申立期間が初步審定公告の日から3ヶ月→<strong>2ヶ月</strong>に短縮されます。検知から提出までの鎖全体がその期間であり、警告期間ではありません。</p>
<p class="leading-relaxed text-slate-300 mb-6">だからこそ、監視・決裁権限・証拠パックが先に存在していないと機能しません。登録簿を時々見る程度の運用では、最初の社内会議が終わる前に期間を失います。現地代理人に事前に委任状を預け、公告日を記録し、在先権利と知名度の資料を常備して、足すのは抵触出願の情報だけという状態にします。</p>
<p class="leading-relaxed text-slate-300 mb-6">引き換えに、主張はさほど厚くない事実記録の上で行われ、相手も答弁できます。抵触が明白で証拠が強いなら、悪い交換ではありません。運用の手順は<a href="{L}/china-trademark-opposition-watch-sop-2-months.html">異議2ヶ月対応の手順</a>をご覧ください。</p>
"""),
            ('when-invalidation-or-cancellation-fit', '無効宣告・不使用取消が向く場面', """
<p class="leading-relaxed text-slate-300 mb-6">登録されてしまうと、無効宣告と不使用取消が主力になります。第51条は無効宣告の請求に<strong>5年</strong>の期間を定めますが、著名商標の悪意登録は<strong>その5年の制限を受けません</strong>。この違いが経路の可否を分けることが多いため、まず登録日と主張の根拠を確定します。</p>
<p class="leading-relaxed text-slate-300 mb-6">第57条は、登録商標が核定商品の通用名称になった場合、または正当な理由なく<strong>3年連続</strong>使用されなかった場合の取消を定め、当局が職権で取り消すことも認めます。一度も取引していないブロッカーには有効ですが、障害を除くだけで自社に権利を与えるわけではないので、続く出願まで設計します。</p>
<p class="leading-relaxed text-slate-300 mb-6">どちらも証拠が重い経路です。無効宣告は在先権利・中国での知名度・相手の悪意が争点になり、取消は指定商品について真実の使用があるかが争点です。争いが始まってから作ったファイルではなく、日付と契約に裏打ちされた記録を残します。有効な使用証拠は<a href="{L}/china-trademark-non-use-cancellation-evidence.html">不使用取消の証拠ガイド</a>をご覧ください。</p>
"""),
            ('when-to-negotiate-or-refile', '交渉・再出願を選ぶ場面', """
<p class="leading-relaxed text-slate-300 mb-6">買取交渉は、確実性へ最も早く至る経路であることが多く、価格、譲渡の範囲、共存や移行の条件まで自社で決められるため主導権も最大です。ただし当事者だけの取引ではありません。第46条は<strong>混同を生じやすく、またはその他の悪影響を及ぼす譲渡は認可しない</strong>と定め、移転は単に記録されるだけでなく審査されます。取引の筋道を記録し、譲渡書類を整え、移転を当てにする前に当期の出願書式を確認します。</p>
<p class="leading-relaxed text-slate-300 mb-6">元の標識が弱い、証拠が薄い、事業の予定が争いを待てない、といった場合の現実解が、改名を伴うこともある新たな出願です。すぐ動けますが、譲る点もあります。消費者がすでに覚えた名前を失いうるうえ、残った抵触権利が新しい出願を妨げたり狭めたりします。新しい候補は、中国語表記を含めて先に調査します。</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>経路だけでなく順番を決めてください。</strong> 異議・無効宣告・取消・買取・再出願は併用が普通で、その順序が主導権と露出を変えます。本記事はあえて数値を置かない比較に留めました。第三者のまとめにある費用・成功率・処理期間を当てにせず、現行の公式規則のもとでの見通しを代理人に確認してください。</p></div>
"""),
            ('sources', '出典と注意書き', """
<p class="leading-relaxed text-slate-300 mb-6">一次資料：『中華人民共和国商標法（2026年改正）』第20条・第24条・第36条・第46条・第51条・第57条（2026年6月26日採択、2027年1月1日施行）、先取り登録への対応に関する一般の実務解説。2ヶ月の異議期間は2027年1月1日から適用されます。5年の無効期間と著名商標の例外、3年の不使用、第46条の譲渡審査は法定の枠組みであり、結末の予測ではありません。本記事は時間・主導権・証拠・リスクについてあえて数値を置かない比較に留め、費用・成功率・審理期間は掲げていません。行動前に当期の公式公告・規則を確認してください。本記事は一般情報であり、個別の法律助言ではありません。</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>先取り登録にどの経路で臨むかお迷いですか？</strong> <a href="/contact.html">案件ごとの順序と証拠計画についてご相談ください</a>。</p></div>
"""),
        ],
    },
}}

CONTENT['ko'] = {'articles': {
    'oem': {
        'slug': 'china-oem-agreement-trademark-clauses',
        'title': '중국 OEM 계약에 반드시 넣어야 할 상표 조항 6가지',
        'desc': '위탁 공장은 시장보다 먼저 브랜드를 봅니다. 공장의 상표 등록, 무단 증산, 포장과 고객 명단 유출을 막는 여섯 조항을 정리했습니다.',
        'lede': '중국 OEM 거래는 곧 상표 위험이기도 합니다. 중국은 선출원주의이고, 로고를 인쇄하는 공장은 출시일·수량·도안을 알고 있습니다. 등록 후 다투는 것보다 첫 발주 전에 여섯 조항을 정해 두는 편이 훨씬 저렴합니다.',
        'card_text': '등록 금지와 양도 의무, 수량 상한과 감사권, 표본 검사, 계약 종료 시 재고·금형 처분, 종료 후에도 남는 비밀유지, 수출과 내수 책임 배분.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['OEM 계약', '상표 조항', '위탁 생산'],
        'related': [
            ('{L}/china-first-to-file-trademark-guide.html', '중국 선출원주의 가이드'),
            ('{L}/china-trademark-monitoring-protection.html', '상표 모니터링과 보호'),
            ('{L}/china-trademark-squatting-decision-table.html', '선점 등록 대응: 이의·무효·매수 판단표'),
        ],
        'sections': [
            ('why-the-factory-is-a-trademark-risk', '왜 공장이 상표 위험이 되는가', """
<p class="leading-relaxed text-slate-300 mb-6">중국에서는 상표권이 원칙적으로 먼저 사용한 자가 아니라 먼저 출원한 자에게 귀속됩니다. 위탁 공장은 이 구조에서 가장 까다로운 위치에 있습니다. 도안을 받고, 계절별 수량을 알고, 아직 확보하지 않은 클래스를 파악하고 있으며, 우리가 출원을 준비하기도 전에 등록할 수 있습니다. 2026년 개정 상표법 제20조는 선행 등록·출원 상표와 동일·유사한 표장을 거절하고, 제24조는 선행 적법 권익과 악의적 선점 등록에 대응하며, 제19조는 사용 의사가 없고 통상적인 사업 수요를 명백히 넘는 출원을 거절할 수 있도록 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">다만 이는 사후 구제이지 예방책이 아닙니다. 실제로 쓰려면 이의 제기나 무효심판 절차, 인지도 증거가 필요하고, 그 사이 공장이 가진 등록이 우리 출원을 막거나 전자상거래 입점을 멈추게 할 수 있습니다. 계약서로 쟁점을 서명 시점으로 옮기면 소유권 다툼을 단순한 채무불이행으로 다룰 수 있습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">아래 여섯 조항은 중국 제조 위탁 계약에 관한 실무 해설에서 반복해 제시되는 것들입니다. 특별한 기법이 아니라 권리·수량·기한·위반 시 효과를 각각 명시할 수 있는지가 효력을 가릅니다. 지식재산을 보호한다는 막연한 문구만으로는 분쟁이 시작되면 거의 쓸모가 없습니다.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>등록이 먼저, 계약은 다음.</strong> 계약은 상대방을 묶고 등록은 세상을 묶습니다. 생산 전에 영문 표장과 중국어 표장을 필요한 클래스에 출원한 뒤, 등록이 닿지 않는 틈을 계약으로 메우십시오.</p></div>
"""),
            ('clauses-1-2-ownership-and-quantity', '조항 1~2: 권리 귀속과 수량 관리', """
<p class="leading-relaxed text-slate-300 mb-6">조항 1은 실효성 있는 등록 금지입니다. 공장, 그 관계사, 하청업체에 브랜드명, 중국어 명칭, 로고, 제품 형상, 혼동을 부르는 유사 표기의 출원을 각 지역에서 금지하고, 위반해 취득한 상표는 공장 부담으로 우리 회사에 양도할 의무를 지웁니다. 여기에 위약금과 취하·이의·무효심판 협조 의무를 더합니다. 양도 의무와 위약금이 없으면 금지는 실효 수단 없는 약속에 그칩니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">조항 2는 수량 상한입니다. 주문별·기간별 최대 수량을 정하고, 발주서와 완제품의 정기 대조를 요구하며, 생산 기록·불량품·출하 기록에 대한 감사권을 남깁니다. 빠지기 쉬운 것이 불이익 추정으로, 기록으로 설명되지 않는 수량의 브랜드 제품은 무단 생산으로 본다고 정합니다. 공장이 가진 자료로 입증 부담을 옮기는 조항입니다.</p>
<table>
<thead><tr><th>조항</th><th>생기는 권리</th><th>위반 시 효과</th></tr></thead>
<tbody>
<tr><td>1. 등록 금지</td><td>공장·관계사의 출원 금지, 위반 취득 상표의 강제 양도</td><td>위약금에 더해 취하·이전 협조 의무</td></tr>
<tr><td>2. 수량 상한</td><td>허용 수량 고정, 기록 대조와 감사</td><td>설명 못 한 수량은 무단 생산으로 추정, 채무불이행</td></tr>
</tbody>
</table>
"""),
            ('clauses-3-4-quality-and-exit', '조항 3~4: 품질 관리와 종료 시 정리', """
<p class="leading-relaxed text-slate-300 mb-6">조항 3은 생산 로트·포장·인쇄물에 대한 표본 검사권과 불합격 시 처리를 정합니다. 수령 거부, 공장 부담의 재작업, 불량 브랜드 제품의 입회 폐기, 이후 출하 중단 등입니다. 품질 관리는 소비자 안전만의 문제가 아닙니다. 제조사의 통제를 벗어난 사용은 상표를 약화시키고, 승인하지 않은 자사 브랜드 제품은 나중에 부인하기 어렵습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">조항 4가 종료 계획이며, 실제 분쟁의 대부분은 여기서 시작됩니다. 거래가 끝나면 공장에 완제품 재고, 반제품, 금형, 치구, 판, 라벨, 포장이 남습니다. 각각 분류해 기한을 정합니다. 승인된 완제품은 정한 기간 안에 소진하고, 반제품은 폐기하거나 매입하며, 금형·인쇄판은 인도하거나 폐기하는 식입니다. 이 부분을 모호하게 두면 전 공급처가 생산을 이어갈 여지를 남깁니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">종료 조항은 짧은 인수 체크리스트와 최종 수량 대조에 묶어, 남은 브랜드 제품의 귀속을 관계가 원만할 때 기록해 두십시오.</p>
"""),
            ('clauses-5-6-secrecy-and-channels', '조항 5~6: 비밀유지와 유통 경로 배분', """
<p class="leading-relaxed text-slate-300 mb-6">조항 5는 공장이 받는 자료를 다룹니다. 설계도, 사양서, 금형 데이터, 포장 도안, 공급처 명단, 고객 명단입니다. 비밀유지를 요구하고, 해당 주문 이행 외의 사용을 막고, 사전 서면 승인 없이 하청에 공개하지 못하게 하며, 의무가 종료 후에도 존속함을 명시합니다. 유출은 대개 마지막 주문 뒤, 공장이 다른 거래처에 비슷한 제품을 제안할 때 일어나므로 존속 조항이 효과를 냅니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">조항 6은 제품의 행선지 책임 배분입니다. 수출과 국내 판매를 나누고, 중국 시장에서 판매할 수 있는 주체, 전자상거래 입점 위탁과 통관·규제 기록 담당, 승인되지 않은 경로에 브랜드 제품이 나왔을 때의 책임자를 정합니다. 공장의 국내 판매는 공급처가 그대로 선점 등록자가 되는 전형적인 경우이므로, 여기서 상표 관계도 기록해 둡니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>계약만으로 안심하지 마십시오.</strong> 필요한 사용 허락은 등록하고, 날짜가 있는 사용 증거를 남기며, 공장과 관계사의 출원을 공보에서 감시하십시오. 2026년 개정법 제55조는 사용 허락 등록을, 제57조는 미사용 상표 취소를 정합니다. 포트폴리오에 반영되지 않은 계약은 출원이 파고들 틈을 남깁니다.</p></div>
"""),
            ('from-contract-to-portfolio', '계약에서 포트폴리오로', """
<p class="leading-relaxed text-slate-300 mb-6">계약은 출원·감시 운영에 넣는 것이지 그 대체물이 아닙니다. 첫 생산 전에 영문 문자상표와 중국어 문자상표를 따로 출원하십시오. 중국에서는 별개의 권리이며 한쪽 등록이 다른 쪽을 덮지 않습니다. 판매하는 클래스에 더해 공급처나 선점 등록자가 노리기 쉬운 클래스를 확보하고, 도형은 결합상표로 묶지 말고 단독 출원하는 것도 검토합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">다음으로 조항을 운영에 옮깁니다. 수량 대조 담당자를 정하고, 감사권을 통지로 행사할 수 있게 유지하며, 종료 후 재고 기한을 일정에 넣고, 공장·관계사·임원의 출원이나 입점을 공보와 주요 전자상거래에서 감시합니다. 사용 허락 관계가 있다면 피허락자의 사용을 입증할 수 있게 서류를 남깁니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">공장이 실제로 출원했다면 계약은 방패가 아니라 증거로 다루십시오. 등록 금지, 양도 의무, 거래 관계 기록은 모두 악의 주장을 강화하지만, 기한은 문제를 발견한 날이 아니라 공고·출원일부터 진행됩니다. 법정 기간이 짧으므로 누가 현지 대리인에게 지시할 수 있는지 미리 정해 두지 않으면 사내 결재를 기다릴 시간이 없습니다. <a href="{L}/china-trademark-squatting-decision-table.html">선점 등록 판단표</a>와 <a href="{L}/china-trademark-monitoring-protection.html">모니터링 가이드</a>도 보십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 중국 OEM·제조 위탁 계약의 상표 조항에 관한 실무 해설, 『중화인민공화국 상표법(2026년 개정)』 제19조·제20조·제24조·제55조·제57조(2026년 6월 26일 채택, 2027년 1월 1일 시행). 조항은 법정 양식이 아니라 일반 실무례입니다. 계약은 준거법에 따라 검토를 받으십시오. 절차와 실무는 개정 시행조례·심사심리 지침으로 달라질 수 있으니 당기 공식 공고·규칙을 대리인에게 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>OEM 계약을 중국 출원과 맞춰 점검하시겠습니까?</strong> <a href="/contact.html">조항 설계와 포트폴리오 정합에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'naming': {
        'slug': 'chinese-brand-name-cnipa-examination',
        'title': 'CNIPA 심사를 실제로 통과하는 중국어 브랜드명 고르기',
        'desc': '읽기 좋아도 거절될 수 있습니다. 음·형·의 세 축, 중국어 명칭을 막는 세 근거, 선점 등록자가 노리는 표기까지 살피는 여섯 갈래 조사를 정리했습니다.',
        'lede': '중국어 명칭을 마케팅 이유로 먼저 정하고 등록 가능성을 나중에 확인하는 기업이 적지 않습니다. 순서가 거꾸로입니다. 선출원주의에서는 등록 가능성을 먼저 조사하고 이름을 나중에 정하는 편이 저렴하고 확실합니다.',
        'card_text': '음·형·의가 각각 다른 충돌을 만드는 이유, 제15조·제17조·제19조가 등록 적성에 미치는 영향, 그리고 검색 결과가 없다는 사실이 위험도 판단에 그치는 이유.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['중국어 브랜드명', '식별력', '선행 조사'],
        'related': [
            ('{L}/free-china-trademark-search-guide.html', '무료 중국 상표 검색 가이드'),
            ('{L}/coca-cola-chinese-name-trademark-china.html', '코카콜라가 중국어 이름을 고른 과정'),
            ('{L}/logo-vs-word-mark-china.html', '로고 상표와 문자 상표의 차이'),
        ],
        'sections': [
            ('the-name-is-a-separate-right', '중국어 이름은 별개의 권리', """
<p class="leading-relaxed text-slate-300 mb-6">중국에 진출한 외국 브랜드에는 영문 표장과 언젠가 생기는 중국어 이름이 있습니다. 법적으로는 별개의 권리입니다. 영문 문자상표를 등록해도 중국어 표기는 보호되지 않고, 소비자가 쓰기 시작한 중국어 이름이 저절로 우리 권리가 되는 것도 아닙니다. 이름에 마음이 끌려 포장을 인쇄한 뒤에 걸림돌을 찾는 대신, 먼저 등록 적성을 조사하고 이름을 정하는 순서가 안전합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">애초에 계획 여부와 무관하게 시장은 중국어 이름을 만듭니다. 소비자와 유통사가 외국 브랜드를 줄여 부르거나, 음역하거나, 번역해 통칭을 굳히고, 선점 등록자는 바로 그 통칭을 노립니다. 발음이 좋고 길하며 획이 아름답다는 이유만으로 고른 이름이라도, 상품이나 품질을 그대로 드러내거나 뒤에서 볼 세 축 가운데 하나로 선출원에 가까우면 심사에서 거절될 수 있습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">영업상 바람을 반영한 등록 적성 문제로 다루고 거꾸로 하지 마십시오. 후보를 몇 개 올리고 각각 조사한 뒤에야 도안과 출시 자료를 만드십시오. 후보 단계에서 이름을 버리는 부담은 거절 뒤에 이름을 바꾸는 부담에 비하면 매우 작습니다.</p>
"""),
            ('three-axes-of-similarity', '유사 판단의 세 축: 음·형·의', """
<p class="leading-relaxed text-slate-300 mb-6">CNIPA는 중국어 상표의 유사를 세 축으로 비교하며, 그중 하나에서 충돌해도 거절 근거가 될 수 있습니다. 이 차이를 아는 것이 읽기 좋은 이름을 심사를 견디는 이름으로 바꾸는 첫걸음입니다.</p>
<table>
<thead><tr><th>축</th><th>심사에서 비교하는 점</th><th>실무 확인</th></tr></thead>
<tbody>
<tr><td>음</td><td>표준중국어 발음과 병음, 성조, 동음·근음</td><td>후보를 소리 내어 읽고 동음·근음의 다른 표기를 찾아낸다</td></tr>
<tr><td>형</td><td>한자의 자형, 부수, 획수 구성과 배열</td><td>전체 인상만이 아니라 한 자씩 시각적 근접을 비교한다</td></tr>
<tr><td>의</td><td>자의, 외국 표장이나 그 번역과의 대응</td><td>자의, 번역어, 문맥상의 함의를 확인한다</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">한 축에서 문제가 없어도 다른 축에서 걸리는 예는 드물지 않습니다. 읽기는 달라도 눈에 띄는 한 자를 공유하거나, 보기엔 달라도 선행 상표와 같은 뜻을 전하는 경우입니다. 따라서 조사는 같은 한자만 찾는 데 그치지 않고 세 축 모두를 등록부와 대조해야 합니다.</p>
"""),
            ('absolute-grounds-articles-15-17-19', '거절 근거: 제15조·제17조·제19조', """
<p class="leading-relaxed text-slate-300 mb-6">선행 권리와의 충돌과 별개로 이름 자체에 등록 적성이 필요합니다. 제17조는 상품의 일반명칭, 성질을 그대로 드러내는 표시, 그 밖에 식별력이 없는 표장을 거절합니다. 다만 사용으로 식별력을 얻은 경우 등록이 허용되는 것이 중요한 예외입니다. 상품 자체를 말하는 이름, 품질을 칭찬하는 이름, 지명이나 원재료를 그대로 붙인 이름은 통과하기 어렵고, 예외를 쓰려면 진정한 사용을 보여 주는 충실한 증거가 필요합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">제15조는 상표로 사용·등록할 수 없는 금지표장을 정하고, 제19조는 악의적 출원을 겨냥해 사용 의사가 없고 통상적인 사업 수요를 명백히 넘는 출원을 거절할 수 있도록 합니다. 브랜드 쪽의 교훈은 거꾸로입니다. 조어로 식별력 높은 이름을 고르고, 사용 의사를 보여 주는 기록을 남기며, 투기로 보이는 방어 출원 더미는 피하십시오.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>조어가 서술보다 강합니다.</strong> 사전에 없는 한자 조합은 슬로건이나 상품 분야의 직역보다 조사도 방어도 쉽고, 나중에 사용에 따른 식별력을 주장할 때도 논리가 통합니다.</p></div>
"""),
            ('six-lane-clearance-search', '여섯 갈래 선행 조사', """
<p class="leading-relaxed text-slate-300 mb-6">중국어 이름의 선행 조사는 여섯 갈래를 덮어야 합니다. 한자 자체, 병음과 동음어, 영어 등 원어, 뜻의 번역어, 방언·지역 발음에서 생기는 비슷한 소리나 바람직하지 않은 울림, 그리고 소비자가 이미 붙인 통칭입니다. 마지막 갈래를 빠뜨리면 출시 전 조사는 깨끗해 보여도, 시장에는 선점 등록자가 가져갈 표기가 이미 돌고 있는 상황이 됩니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">공식 데이터베이스는 판단 재료 하나이지 결론이 아닙니다. 공개되는 등록부는 실시간이 아니어서, 출원한 뒤 반영되기까지 빈 기간이 있고 자료도 늦습니다. 따라서 검색 결과는 위험도의 윤곽일 뿐 등록을 보장하지 않습니다. 검색 결과가 없다고 포장 인쇄를 허가로 받아들이지 말고, 빈 기간을 특정 개월 수로 단정하지도 마십시오. 당기 상황은 대리인에게 확인합니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>결과가 없다고 등록 가능한 것은 아닙니다.</strong> 공식 검색에 폭넓은 상업 검색을 더하고, 무엇을 언제 조사했는지 날짜와 함께 남기며, 출원 직전에 다시 검색하십시오. 아슬아슬한 후보라면 두 번째·세 번째 안도 함께 조사해 둡니다.</p></div>
"""),
            ('file-word-and-device-separately', '문자와 도형은 따로 출원하기', """
<p class="leading-relaxed text-slate-300 mb-6">결합상표는 요소별로 심사합니다. 도형과 문자를 함께 출원하면 양쪽이 모두 조사되고, 한쪽에 문제만 있어도 출원 전체가 멈춥니다. 그래서 중국어 문자상표, 영문 문자상표, 도형을 따로 출원하는 것이 정석입니다. 각각 독립적으로 성패가 갈리고 별개의 권리가 되며, 하나에 거절이나 이의가 생겨도 나머지가 묶이지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">영문판과 중국어판은 하나의 결합상표가 아니라 포트폴리오 설계로 함께 출원합니다. 지키는 대상도, 권리 행사와 사용 증거 파일도 따로입니다. 고른 이름의 식별력이 약하면 제17조 예외에 대비해, 소비자가 그 이름을 우리 회사와 결부해 인식한다는 것을 보여 주는 날짜 있는 광고·판매·전자상거래 기록을 처음부터 쌓아 둡니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">마지막으로 사용하는 클래스에 등록하고, 포장·전자상거래 화면·회사 자료에서 영문명과 중국어명 표기를 맞추십시오. 표기가 흔들리면 통칭이 생겨 이후 선행 조사가 어려워집니다. 검색 실무는 <a href="{L}/free-china-trademark-search-guide.html">무료 중국 상표 검색 가이드</a>, 별개 권리라는 점은 <a href="{L}/logo-vs-word-mark-china.html">로고 상표와 문자 상표의 차이</a>를 보십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제15조·제17조·제19조·제20조(2026년 6월 26일 채택, 2027년 1월 1일 시행), 중국어 상표의 음·형·의 및 결합상표 심사에 관한 CNIPA의 일반 실무, 중국어 명명에 관한 실무 해설. 공식 데이터베이스 반영 상태나 심사 기준은 달라질 수 있으므로 출원 전에 당기 공식 공고·규칙과 최신 등록부를 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>이름을 정하기 전에 조사하시겠습니까?</strong> <a href="/contact.html">음·형·의 조사와 실제 등록 가능한 후보 목록에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'refusal': {
        'slug': 'china-trademark-refusal-review-15-days',
        'title': '중국 거절 심판: 15일 기한과 대응 방법',
        'desc': '거절로 돌아가는 두 개의 시계. 국내 출원의 15일, 마드리드 지정의 15일·30일, 그리고 심판을 유리하게 만드는 여섯 가지 주장을 정리했습니다.',
        'lede': '거절은 출원의 끝이 아니라 짧은 기한의 시작입니다. 개정법에서는 심판 청구가 15일, 마드리드 지정 중국에서는 WIPO 통지 수령부터 15일 또는 30일이라는 별도의 시계가 돌아갑니다.',
        'card_text': '어느 기한이 적용되는지, 보충 증거는 언제까지인지, 그리고 비유사 주장부터 병행 국내 출원까지 여섯 가지 대응책.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['거절 심판', '15일 기한', '마드리드 지정'],
        'related': [
            ('{L}/common-reasons-trademark-rejection-china.html', '중국에서 거절되는 주요 이유'),
            ('{L}/madrid-vs-direct-filing-china.html', '마드리드 방식과 직접 출원 비교'),
            ('{HUB}', '구법·신법 조항 대조'),
        ],
        'sections': [
            ('two-clocks', '두 개의 시계: 국내 15일과 마드리드 경로', """
<p class="leading-relaxed text-slate-300 mb-6">거절은 출원의 끝이 아니라 기한의 시작입니다. 2026년 개정 상표법 제37조는 거절에 불복하는 출원인에게 <strong>15일 이내</strong>의 심판 청구를 허용하고, CNIPA는 <strong>9개월 이내</strong>(<strong>3개월</strong> 연장 가능)에 결정한다고 정합니다. 15일을 넘기면 원 출원에 대한 거절이 확정되므로 첫 일은 주장 만들기가 아니라 기한 관리입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">중국을 지정하는 국제등록은 혼동하기 쉬운 다른 시계로 움직입니다. WIPO가 잠정 거절을 통지하면 심판 청구 기간은 보유자가 그 통지를 받은 날부터 기산되며, 직권 거절은 <strong>15일</strong>, 이의에 기초한 거절은 <strong>30일</strong>입니다. 이는 WIPO의 공식 기한표와 2011년 제19호 정보 통지에 따른 것입니다. 국내 15일과 같은 규정으로 단정하지 말고 어느 쪽 거절인지 가려낸 뒤 기산하십시오.</p>
<table>
<thead><tr><th>경로</th><th>기산점</th><th>심판 청구 기간</th></tr></thead>
<tbody>
<tr><td>중국 국내 출원(제37조)</td><td>거절 통지 수령</td><td>15일</td></tr>
<tr><td>마드리드 지정·직권 거절</td><td>보유자가 WIPO 잠정 거절 통지 수령</td><td>15일</td></tr>
<tr><td>마드리드 지정·이의 기초 거절</td><td>보유자가 WIPO 잠정 거절 통지 수령</td><td>30일</td></tr>
</tbody>
</table>
"""),
            ('what-happens-after-you-file', '청구 뒤에 일어나는 일', """
<p class="leading-relaxed text-slate-300 mb-6">심판 청구가 접수되면 본안과 첨부 자료에 근거해 심리합니다. 제37조의 9개월·연장 3개월은 당국의 결정 목표이지 우리가 채워야 할 기한이 아닙니다. 눈여겨볼 것은 증거 쪽으로, 마드리드 관련 심판에서는 보충 증거를 <strong>심판 청구일부터 3개월 이내</strong>에 제출하도록 WIPO 기한 자료에 나와 있습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">이 구조는 준비에 보상을 줍니다. 표장이 다르다고만 적은 청구는 사건 전체를 기록에 올릴 좋은 기회를 놓칩니다. 인용 상표가 있다면 표장의 비유사, 상품·서비스의 비유사, 둘 다, 혹은 사용을 뒷받침으로 한 공존을 주장할지 일찍 정하십시오. 고른 논리가 청구 뒤 몇 주 동안 모을 증거를 정합니다.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>세 가지를 따로 일정에 넣으십시오.</strong> 심판 청구 기한, 보충 증거 기한, 결정이 예상되는 시점입니다. 기산점이 제각각이라 혼동은 피할 수 있는 손실의 전형입니다.</p></div>
"""),
            ('the-six-argument-menu', '여섯 가지 주장 선택지', """
<p class="leading-relaxed text-slate-300 mb-6">중국 거절에 대한 대응은 실무 해설에서 대체로 여섯 가지로 정리되며, 대부분의 사건에서 여러 개를 함께 씁니다.</p>
<ol>
<li><strong>표장과 상품을 다툽니다.</strong> 출원 상표가 인용 상표와 유사하지 않거나 지정 상품·서비스가 유사하지 않음을, 해당 서브클래스까지 짚으며 정리해 보입니다.</li>
<li><strong>공존 또는 사용에 따른 식별력에 기댑니다.</strong> 진정한 병행 사용, 시장 인지, 사용으로 얻은 식별력 자료를 넣어 혼동 가능성이 작음을 보입니다.</li>
<li><strong>인용 등록을 무너뜨립니다.</strong> 인용 등록이 3년 연속 사용되지 않았다면 불사용 취소로 장애물을 뿌리부터 없애는 것을 검토합니다.</li>
<li><strong>동의서를 받습니다.</strong> 선행 권리자와의 공존 합의나 동의는 주장만으로 풀리지 않는 인용을 정리할 수 있습니다.</li>
<li><strong>일부 거절을 받아들입니다.</strong> 막힌 상품이 일부라면 지정을 좁혀 나머지의 출원일을 지키는 선택이 있습니다.</li>
<li><strong>병행해 중국 국내 출원을 냅니다.</strong> 마드리드 지정이라면 직접 국내 출원이 국제 거절의 향방에 좌우되지 않는 권리를 남깁니다.</li>
</ol>
"""),
            ('building-the-evidence-file', '증거 파일 만드는 법', """
<p class="leading-relaxed text-slate-300 mb-6">심판은 자료로 이깁니다. 공존 합의나 동의서는 제대로 작성·번역하고 대상 상표와 상품을 정확히 특정하십시오. 사용에 따른 식별력에는 날짜 있는 광고, 판매 기록, 전자상거래 화면, 보도, 유통 자료를 모아, 출원 표장이 중국에서 우리 사업을 가리킨다는 것을 단순히 존재한다는 데 그치지 않고 보입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">인용 상표에 대한 불사용 취소에서는 증거의 쟁점이 달라집니다. 문제는 지정 상품에 진정한 사용이 있었는지이므로, 출원일, 거기서 소급한 3년의 틀, 사용이 요구되는 상품을 확보합니다. 취소와 심판은 별도 절차이므로 취소 상황이 심판 기록에 반영되도록 맞춰 놓습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">거절 통지, 해당하면 WIPO 통지, 심판 청구, 모든 첨부 자료, 제출일 목록을 한 파일에 모으십시오. 나중에 심판이나 법원으로 옮길 때 이 시간 순서가 사건의 뼈대가 됩니다. 거절의 배경은 <a href="{L}/common-reasons-trademark-rejection-china.html">중국에서 거절되는 주요 이유</a>를 보십시오.</p>
"""),
            ('a-madrid-specific-playbook', '마드리드 특유의 실무', """
<p class="leading-relaxed text-slate-300 mb-6">마드리드 제도로 중국에 들어온 보유자에게 가장 쓸모 있는 예방책은 흔히 병행하는 중국 국내 출원입니다. 국제 지정의 향방에 좌우되지 않는 별개의 권리가 생기고, 국제등록으로는 택할 수 없는 좁은 지정이나 분할 방침도 고를 수 있습니다. 국내 출원에서 같은 범위로 할지, 상품을 줄일지, 별도의 중국어 표장으로 할지는 대리인과 정하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">일부 거절은 반사적인 불복이 아니라 의식한 판단이 필요합니다. 막힌 것이 지정의 일부뿐이라면 범위를 좁혀 나머지의 이른 출원일을 지키면서, 따로 탄탄한 주장을 세우는 길도 있습니다. 반대로 막힌 상품이 사업의 중심이라면 병행 출원과 인용에 대한 취소를 함께 쓰는 수고를 들일 가치가 있습니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>WIPO 통지가 시계를 움직입니다.</strong> 기록상 보유자 주소가 감시되고, 통지 도착일이 그날 기록되도록 하십시오. 15일·30일 기한에는 권한, 번역, 증거를 처음부터 다시 갖출 여유가 없습니다. 거절이 나오기 전부터 현지 대리인에게 위임장을 맡겨 두십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제37조(2026년 6월 26일 채택, 2027년 1월 1일 시행), WIPO의 지정 대상 잠정 거절 대응 기한표, WIPO 2011년 제19호 정보 통지. 마드리드 기한은 보유자가 WIPO 통지를 수령한 때부터 기산되며 직권 거절과 이의 기초 거절이 다릅니다. 당기 WIPO 기한표와 공식 공고·규칙을 대리인에게 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>기한이 다가오는 거절을 겪고 계신가요?</strong> <a href="/contact.html">심판 방침과 병행 출원에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'nice': {
        'slug': 'nice-classification-13th-edition-2026-china',
        'title': '니스 분류 제13판(2026년): 중국 출원에 영향을 주는 클래스 이동',
        'desc': '2026년 1월 1일부터 중국은 제13판을 적용합니다. 안경·발열 의류·구조 차량·크림케이크가 클래스를 옮기고, 제42클래스에 AI 서비스가 추가되고, 제3클래스 에센셜오일은 용도로 나뉘었습니다.',
        'lede': '중국은 2026년 1월 1일부터 니스 분류 제13판을 채택했고, CNIPA도 「유사 상품·서비스 구분표」를 제13판에 맞춰 조정했습니다. 제12판으로 작성한 지정 상품 가운데 지금은 다른 클래스에 들어가는 것이 있습니다.',
        'card_text': '네 가지 이동, 스마트 안경의 예외, 제42클래스의 새 AI 항목, 용도별로 나뉜 제3클래스 에센셜오일, 그리고 2026년 출원 체크리스트.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['니스 분류', '클래스 이동', '제13판'],
        'related': [
            ('{L}/china-trademark-classes-complete-guide.html', '중국 상표 클래스 완전 가이드'),
            ('{ACT}', '2027년 전에 외국 브랜드가 해야 할 일'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', '중국 상표 등록 가이드'),
        ],
        'sections': [
            ('the-cutover-date', '2026년 1월 1일 전환', """
<p class="leading-relaxed text-slate-300 mb-6">중국은 <strong>2026년 1월 1일</strong>부터 <strong>니스 분류 제13판(2026년 텍스트)</strong>를 채택했습니다. 그날보다 먼저 출원된 사건은 계속 제12판으로 심사되며, 상품·서비스 분류는 출원일에 효력을 가지는 판을 따릅니다. 2026년 출원 체크리스트는 우선 이 전환일을 축으로 짜야 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">니스 분류는 국제적인 뼈대이지만 중국에서 실제로 쓰이는 것은 CNIPA의 「유사 상품·서비스 구분표」이고, 제13판에 맞춰 조정되었습니다. 심사관이 상품 유사를 판단하는 것은 이 표이며, 클래스 제목보다 잘게 나뉘어 있습니다. 오래된 목록으로 만든 지정은 클래스 번호 자체가 맞아 보여도 내용이 어긋날 수 있습니다.</p>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>클래스 번호가 아니라 판을 확인하십시오.</strong> 과거 출원의 지정을 재사용하기 전에 어느 판으로 작성했는지 확정하고, 현행 구분표에서 항목 문구를 다시 읽으십시오. 공식 문구로 분명하지 않은 점은 그대로 이어진다고 단정하지 말고 대리인에게 당기 공고·규칙을 확인시키십시오.</p></div>
"""),
            ('goods-that-moved-class', '클래스를 옮긴 상품', """
<p class="leading-relaxed text-slate-300 mb-6">제13판에서는 일상적인 상품 여럿이 클래스를 옮겼습니다. 몇 년 전에 짠 포트폴리오를 지금 넓히거나 손볼 때 놓치기 쉬운 변경입니다.</p>
<table>
<thead><tr><th>상품</th><th>이동 전</th><th>이동 후</th><th>비고</th></tr></thead>
<tbody>
<tr><td>안경 및 부속품(렌즈, 안경테, 선글라스, 콘택트렌즈)</td><td>제9클래스</td><td>제10클래스</td><td>스마트 안경은 제9클래스에 그대로</td></tr>
<tr><td>전기 발열 의류(발열 양말 포함)</td><td>제11클래스</td><td>제25클래스</td><td>의류와 같은 취급</td></tr>
<tr><td>긴급구조 차량(소방차, 구명정 등)</td><td>제9클래스</td><td>제12클래스</td><td>차량과 같은 취급</td></tr>
<tr><td>버터크림, 크림케이크</td><td>제29클래스</td><td>제30클래스</td><td>제과·제빵류와 같은 취급</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">영향이 가장 넓은 것은 안경입니다. 제9클래스로 짠 브랜드는 제10클래스 보완이 필요해진 반면 스마트 안경은 원래 클래스에 남습니다. 안경 분야 전체가 옮겼다고 다루지 마십시오. 항목 문구를 읽고 스마트 안경 예외를 염두에 두며, 등록분 아니라 계류 중인 출원까지 포함해 부족함을 찾아내십시오.</p>
"""),
            ('new-and-split-entries', '추가된 항목과 나뉜 항목', """
<p class="leading-relaxed text-slate-300 mb-6">나머지 둘은 이동이 아니라 추가와 분할입니다. <strong>제42클래스에 「인공지능을 서비스로 제공하는 업무(AIaaS)」가 더해져</strong>, 지금까지 폭넓은 컴퓨터·소프트웨어 항목에 밀어 넣던 업무에 전용 자리가 생겼습니다. AI 기반, 모델 제공, 기계학습 업무를 다룬다면 기존의 포괄 문구보다 새 항목이 지정을 더 깔끔하게 쓰는지 확인하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6"><strong>제3클래스 에센셜오일은 용도별로 나뉘었습니다.</strong> 하나의 포괄 항목이 아니라 화장·방향 같은 용도인지 그 밖의 용도인지에 따라 분류가 달라집니다. 실무상으로는 제3클래스 지정에 용도를 밝혀 적어야 한다는 뜻입니다. 같은 제품이라도 어떻게 쓰고 어떻게 파는지에 따라 해당 항목이 달라질 수 있습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">둘에 공통된 원칙은 실제 상품·서비스를 쓴 뒤 현행 항목을 찾는 순서입니다. 오래된 양식의 흔한 문구를 베껴 심사관이 바꿔 읽어 주길 기대해서는 안 됩니다.</p>
"""),
            ('what-the-change-does-not-do', '이 개정이 바꾸지 않는 것', """
<p class="leading-relaxed text-slate-300 mb-6">분류 개정이 그것만으로 과거 출원을 다시 쓰지는 않습니다. 출원은 그날 효력을 가지는 판으로 심사되므로 2026년 1월 1일 선이 작동합니다. 전환 전 출원은 제12판 그대로, 전환 후 출원은 제13판입니다. 뒤에 표가 바뀌었다고 계류 중인 출원이 저절로 재분류되지는 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">영향은 그 뒤에 내거나 넓히는 것 전체에 미칩니다. 신규 출원, 뒤이은 지정, 갱신에서 지정을 다시 보는 자리, 방어 출원에서 고르는 범위 등입니다. 유사 판단에도 영향을 줍니다. 조정 뒤 구분표는 옛 표와 항목 묶음이 다를 수 있으므로, 옮긴 상품이 들어간 충돌 분석은 제12판 전제로 만든 것을 다시 살펴야 합니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>경과 규정은 공식으로 확인하십시오.</strong> 본 글은 분류 변경과 출원일 기준이라는 일반 원칙을 말할 뿐, 계류 사건이나 기존 등록에 관한 자세한 경과 규정을 제시하지 않습니다. 실제 출원에 걸린 판단은 제3자 요약이 아니라 CNIPA의 당기 공고·규칙에 기대십시오.</p></div>
"""),
            ('a-2026-filing-checklist', '2026년 출원 체크리스트', """
<p class="leading-relaxed text-slate-300 mb-6">2026년 출원을 정리하는 짧은 체크리스트입니다.</p>
<ol>
<li><strong>적용 판을 출원일로 확인</strong>하고 기록에 남깁니다.</li>
<li><strong>현행 CNIPA 구분표를 항목마다 다시 읽고</strong>, 서브클래스 문구까지 과거 지정을 재사용하지 않게 합니다.</li>
<li><strong>옮긴 상품을 다시 배치합니다.</strong> 안경, 발열 의류, 구조 차량, 버터크림·크림케이크를 찾아내고 새 클래스가 필요한지, 스마트 안경 예외에 해당하는지 확인합니다.</li>
<li><strong>추가·분할된 항목을 씁니다.</strong> 제42클래스의 AI 서비스, 제3클래스의 용도를 밝힌 에센셜오일 문구입니다.</li>
<li><strong>방어 출원과 워칭 범위를 갱신</strong>해, 상품이 빠져나온 클래스뿐 아니라 옮겨간 클래스도 감시에 넣습니다.</li>
<li><strong>제12판으로 만든 충돌 분석을 다시 검색</strong>하고, 대리인 양식과 체크리스트도 갱신합니다.</li>
</ol>
<p class="leading-relaxed text-slate-300 mb-6">클래스 전체 그림은 <a href="{L}/china-trademark-classes-complete-guide.html">중국 상표 클래스 완전 가이드</a>와 <a href="{L}/china-trademark-registration-complete-guide-2026.html">등록 가이드</a>를 보십시오. 항목 위치가 정말 헷갈린다면 출원 전에 현행 공식 문구로 확인을 서면으로 요청하십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 2026년 1월 1일부터 중국이 채택한 니스 분류 제13판(2026년 텍스트), 제13판에 근거한 CNIPA 「유사 상품·서비스 구분표」 조정, 그리고 본 글에서 말한 클래스 이동·제42클래스 AI 업무 추가·제3클래스 에센셜오일의 용도별 분할. 항목 문구와 경과상 취급은 출원 전에 CNIPA의 당기 공고·규칙·구분표로 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>지정이 어느 판에 속하는지 불확실하신가요?</strong> <a href="/contact.html">현행 CNIPA 구분표에 비춰 상품·서비스 목록을 점검해 드립니다</a>.</p></div>
"""),
        ],
    },
    'dynamic': {
        'slug': 'dynamic-sound-colour-marks-china-2027',
        'title': '중국의 동적·소리·색채 상표: 2027년 시행 신법에서 무엇이 허용되나',
        'desc': '제14조가 동적 표장을 더하고 제18조가 기능상 특징을 배제합니다. 신법이 허용하는 범위, 동적 상표의 출원 꾸러미(초안), 식별력 증거의 짧은 제출 기한을 정리했습니다.',
        'lede': '2027년 1월 1일 시행되는 개정 상표법은 비전통적 표장을 조문에서 분명히 다룹니다. 제14조는 동적 상표를 더하고, 제18조는 색채·소리·동적 표장에 기능을 이유로 한 배제를 정합니다. 출원 세부 사항은 심사 지침 초안에 근거하며 앞으로 달라질 수 있습니다.',
        'card_text': '배제되는 세 가지 기능상 범주, MP4와 JPEG로 이루어진 초안 제출물, 그리고 사용에 따른 식별력을 출원 전부터 뒷받침해야 하는 이유.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['비전통 상표', '동적 상표', '2027년 법'],
        'related': [
            ('{HUB}', '구법·신법 조항 대조'),
            ('{L}/chinese-brand-name-cnipa-examination.html', '중국어 브랜드명 고르기'),
            ('{L}/logo-vs-word-mark-china.html', '로고 상표와 문자 상표의 차이'),
        ],
        'sections': [
            ('what-changes-on-1-january-2027', '2027년 1월 1일에 바뀌는 것', """
<p class="leading-relaxed text-slate-300 mb-6">『중화인민공화국 상표법(2026년 개정)』은 <strong>2026년 6월 26일</strong>에 채택되어 <strong>2027년 1월 1일</strong>에 시행됩니다. 모두 9장 87조입니다. 눈에 띄는 변경 가운데 하나가 제14조로, 등록할 수 있는 표장에 <strong>동적 표장</strong>을 더했습니다. 다른 하나는 제18조로, 색채·소리·동적 표장에 기능을 이유로 한 배제를 정합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">브랜드 쪽 요점은 비전통 상표가 중국 실무에 완전히 새롭다는 것이 아니라, 개정법이 조문에서 정면으로 다루었다는 점입니다. 색채·소리·동적 표장은 상표로 기능할 수 있는 표장이면서 고유한 배제를 받습니다. 틀에 얽매이지 않는다는 이유만으로 거절되지는 않지만, 상품의 기능상 특징을 독점하게 두지도 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">동적 상표란 정지 화면이 아니라 시간에 따라 움직이거나 변하는 것으로 정의되는 표장입니다. 움직이는 로고, 일련의 동작, 소비자가 한 사업자를 가리킨다고 인식하는 전환 등이 해당합니다. 이 정의가 출원 방법, 식별력 입증, 그리고 기능성 배제가 무엇을 비워 두려는지를 모두 좌우합니다.</p>
"""),
            ('the-functionality-exclusion', '제18조의 기능성 배제', """
<p class="leading-relaxed text-slate-300 mb-6">제18조는 색채·소리·동적 표장 가운데 브랜드를 가리키는 것이 아니라 기능에 규정된 것을 등록에서 배제합니다. 거절되는 것은 다음 세 가지입니다.</p>
<table>
<thead><tr><th>배제되는 범주</th><th>뜻</th><th>원칙상의 예</th></tr></thead>
<tbody>
<tr><td>상품 자체의 성질에서만 생기는 것</td><td>그 제품이 본래 가진 특징인 경우</td><td>제품이 피할 수 없는 색이나 움직임</td></tr>
<tr><td>기술상 효과를 얻는 데 필요한 것</td><td>제품의 작동이나 기능을 좋게 하는 특징</td><td>기계 작동을 알리는 소리나 동작</td></tr>
<tr><td>상품에 실질상 가치를 주는 것</td><td>고객이 사는 주된 이유가 그 특징</td><td>그 자체가 제품 가치가 되는 미관상 효과</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">선은 출처를 <em>가리키는</em> 표장과 제품 <em>그 자체</em>인 특징 사이에 있습니다. 식별력 있는 움직이는 로고는 등록될 수 있지만, 기기가 그저 움직이는 모습은 등록되지 않습니다. 심사는 이 경계에 집중할 것으로 보이므로, 표장을 출처 표시로 자리매김하고 기능에 규정되지 않은 이유를 설명하는 서술을 준비하십시오.</p>
"""),
            ('how-a-dynamic-mark-is-filed', '동적 상표 출원 방법', """
<p class="leading-relaxed text-slate-300 mb-6">동적 상표의 심사 지침은 <strong>초안</strong>으로 제시되었고 제출물이 구체적으로 정해져 있습니다. <strong>20MB 이하의 MP4 동영상</strong>, <strong>3~9장의 JPEG 정지 화상</strong>, 그리고 사용 방법을 적은 설명서입니다. 정지 화상이 필요한 까닭은 등록부와 공고가 지면에서 멈춰 있기 때문이며, 움직임을 재현할 수 없는 자리에서 무엇이 보호되는지를 그림으로 정합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">골라 낼 장면은 의식해 고르십시오. 같은 간격으로 뽑은 것이 아니라 일련의 움직임 가운데 인식의 핵심이 되는 장면을 넣고, 설명서는 따로 떨어진 그림의 모음이 아니라 하나의 표장으로 묶어야 합니다. 동영상·정지 화상·설명의 어긋남은 거절 이유로 곧장 이어지는 길입니다.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>초안이므로 확정 사항으로 다루지 마십시오.</strong> 위 형식은 의견 수렴에 부쳐진 심사 지침 초안에 근거하며 달라질 수 있습니다. 출원 시 요건, 형식, 용량 상한은 대리인과 당기 공식 지침·공고·규칙으로 확인하십시오.</p></div>
"""),
            ('acquired-distinctiveness-and-the-15-day-evidence', '사용에 따른 식별력과 15일 증거 기한', """
<p class="leading-relaxed text-slate-300 mb-6">동적·색채·소리 상표도 다른 표장과 마찬가지로 식별력이 필요합니다. 제17조는 태생적으로 식별력이 없는 표장이라도 사용으로 식별력을 얻으면 등록을 허용합니다. 비전통 상표에서는 이 쟁점이 자주 나옵니다. 색이나 짧은 움직임은 그것만으로는 출처 표시로 받아들여지기 어려워, 소비자가 한 사업자를 가리키는 것으로 익혔다는 점을 보이도록 요구받습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">초안 지침에서는 심사관이 사용에 따른 식별력 증거를 요구하면 <strong>통지를 받은 때부터 15일 이내</strong>에 제출하도록 됩니다. 짧은 기한인 데다 요구가 온 뒤 만들 수 있는 종류의 자료가 아닙니다. 날짜 있는 광고, 판매 실적, 보도, 소비자 인식을 보여 주는 자료를 진정한 사용의 축적으로 미리 갖춰야 합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">출원 전부터 파일을 쌓으십시오. 움직이는 표장이나 소리 표장을 실제로 쓴 방송·전자상거래 기록, 전개 시기와 도달 범위, 표장을 일관되게 보인 예를 남깁니다. 15일이라는 기한은 준비를 시작할 기한이 아니라 일찍 대비할 이유입니다. 지침이 초안인 만큼 최종 기한과 형식은 공식으로 확인하십시오.</p>
"""),
            ('building-a-non-traditional-portfolio', '비전통 상표를 아우른 포트폴리오', """
<p class="leading-relaxed text-slate-300 mb-6">비전통 등록은 핵심 포트폴리오를 대신하는 것이 아니라 보태는 것입니다. 먼저 문자상표, 도형상표, 중국어 이름을 따로 출원하십시오. 이쪽이 조사도 쉽고 권리 행사도 쉬우며, 동영상이나 음성 파일이 올바로 재현되는지에 좌우되지도 않습니다. 동적·색채·소리 상표는 시장에서 실제로 인식을 떠받치는 경우에 더합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">이어서 딸린 자료를 맞추십시오. 사용 방법 설명, 정지 화상, 사용에 따른 식별력 증거, 광고 기록은 모두 같은 표장이 같은 상품에 쓰였다는 것을 보여 주어야 합니다. 출원과 증거의 어긋남은 식별력 주장에서 흔히 보는 약점입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">마지막으로 시행 규칙을 지켜보십시오. 개정법이 틀을 정하지만 출원 실무·형식·심사 운용은 개정 시행조례와 심사심리 지침에서 더 잘게 나뉠 수 있습니다. 초안이나 요약이 아니라 출원 시점의 당기 공식 공고·규칙에 기대십시오. 식별력 논리는 <a href="{L}/chinese-brand-name-cnipa-examination.html">중국어 브랜드명 고르기</a>, 별개 권리라는 점은 <a href="{L}/logo-vs-word-mark-china.html">로고 상표와 문자 상표의 차이</a>를 보십시오.</p>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제14조·제17조·제18조(2026년 6월 26일 채택, 2027년 1월 1일 시행, 모두 9장 87조), 동적 상표에 관한 심사 지침 초안(20MB 이하 MP4 동영상, 3~9장의 JPEG 정지 화상, 사용 방법 설명, 사용에 따른 식별력 증거의 15일 제출 기한). <strong>지침은 초안·의견 수렴 단계이며 변경될 수 있습니다.</strong> 출원 요건과 최종 시행 규칙은 CNIPA의 당기 공식 공고·규칙으로 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>동적·소리·색채 출원을 검토하시나요?</strong> <a href="/contact.html">제출물과 식별력 증거 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'greaterchina': {
        'slug': 'greater-china-trademark-separate-filings',
        'title': '중국 중국 홍콩·중국 마카오·중국 대만: 별도로 필요한 상표 등록',
        'desc': 'CNIPA 등록은 중국 본토(대륙)에서만 유효합니다. 중국 중국 홍콩·중국 마카오·중국 대만은 각각 별개의 상표 제도를 가지며 따로 출원해야 합니다. 마드리드 지정 중국도 세 지역에는 미치지 않습니다.',
        'lede': '중국 상표 보호에서 가장 흔한 오해는 지리 범위에 관한 것입니다. CNIPA 등록이 효력을 가지는 곳은 중국 본토(대륙)뿐입니다. 중국 중국 홍콩·중국 마카오·중국 대만은 모두 중국의 일부이지만 각자 별개의 등록부를 가지며 별도의 현지 출원이 필요합니다.',
        'card_text': 'CNIPA 등록이 덮는 범위, 마드리드 지정이 세 지역에 미치지 않는 이유, 그리고 시장마다 보호를 짜기 위한 공통 체크리스트.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['지역별 출원', 'CNIPA 효력 범위', '별도 등록'],
        'related': [
            ('{L}/madrid-vs-direct-filing-china.html', '마드리드 방식과 직접 출원 비교'),
            ('{L}/china-trademark-registration-complete-guide-2026.html', '중국 상표 등록 가이드'),
            ('{L}/china-first-to-file-trademark-guide.html', '중국 선출원주의 가이드'),
        ],
        'sections': [
            ('separate-registries-within-china', '중국 안의 별개 등록부', """
<p class="leading-relaxed text-slate-300 mb-6">중국 상표 보호에서 가장 흔한 오해는 지리 범위에 관한 것입니다. CNIPA가 부여한 등록의 효력은 <strong>중국 본토(대륙)에 한정되며</strong>, 중국 중국 홍콩·중국 마카오·중국 대만에 저절로 미치지 않습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">세 지역은 모두 중국의 일부이지만, 각각 별개의 상표 제도, 별개의 등록부, 별개의 심사 실무를 가지며 현지 주관 기관에 따로 출원해야 합니다. 따라서 권리는 중국 안에서도 실무상 지역마다 나뉩니다. 이 모든 시장에서 보호를 받으려면 하나하나에서 권리를 얻어야 합니다. 이는 상표권을 현지에서 취득하는 절차상의 구조일 뿐 그 이상의 뜻은 없습니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">결과는 단순하지만 예산에서 놓치기 쉽습니다. CNIPA 등록에만 기댄 포트폴리오는 실제로 판매·유통·홍보하는 시장에서 우리 브랜드가 보호받지 않는 상태를 남깁니다. 반대로 세 지역 가운데 한 곳에서 얻은 등록도 중국 본토(대륙)에서는 권리를 만들지 못합니다. 먼저 범위를 그리고 그다음 출원하십시오.</p>
"""),
            ('what-a-cnipa-registration-covers', 'CNIPA 등록이 덮는 범위', """
<p class="leading-relaxed text-slate-300 mb-6">효력 규칙은 대칭적이어서, 등록은 부여한 곳에서만 보호합니다.</p>
<table>
<thead><tr><th>취득한 등록</th><th>효력이 미치는 곳</th><th>미치지 않는 곳</th></tr></thead>
<tbody>
<tr><td>CNIPA 등록</td><td>중국 본토(대륙)</td><td>중국 중국 홍콩·중국 마카오·중국 대만</td></tr>
<tr><td>중국 홍콩에서의 등록</td><td>해당 지역</td><td>중국 본토(대륙)와 나머지 두 지역</td></tr>
<tr><td>중국 마카오에서의 등록</td><td>해당 지역</td><td>중국 본토(대륙)와 나머지 두 지역</td></tr>
<tr><td>중국 대만에서의 등록</td><td>해당 지역</td><td>중국 본토(대륙)와 나머지 두 지역</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">실무상 결론이 둘 있습니다. 첫째, 등록이 없는 시장에서는 선점 등록자가 출원할 수 있고 CNIPA 등록증만으로 그 출원을 물리치지 못합니다. 둘째, 사용 증거·사용 허락·권리 행사 기록은 등록부마다 정리해야 하며, 한 곳에서의 진정한 사용이 다른 곳에서의 사용이 되지는 않습니다. 각각 따로 파일을 보관하십시오.</p>
"""),
            ('why-madrid-does-not-extend', '마드리드 지정이 미치지 않는 이유', """
<p class="leading-relaxed text-slate-300 mb-6">마드리드 제도에 따라 중국을 지정하는 국제등록은 CNIPA가 심사하고, 받아들여지면 중국 본토(대륙)에서 보호를 만듭니다. 중국 중국 홍콩·중국 마카오·중국 대만에는 <strong>미치지 않습니다</strong>. 세 지역에는 각자 현지 출원이 필요하며 마드리드 지정이 이를 대신하지 못합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">이는 국제등록을 축으로 짠 포트폴리오가 걸리는 지점입니다. 국제등록 한 건이면 다 덮였다고 생각했다가, 세 지역의 현지 등록부가 손대지 않은 상태였다는 사실을 뒤늦게 발견할 수 있습니다. 국제 포트폴리오를 점검할 때는 지정 대상을 적어 낸 뒤, 세 지역에서 실제로 취득한 현지 출원을 따로 목록으로 만드십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">같은 논리가 워칭과 갱신 일정에도 적용됩니다. CNIPA 공고만 좇는 감시로는 세 지역 현지 등록부에 들어온 출원을 잡아내지 못합니다. 경로 비교는 <a href="{L}/madrid-vs-direct-filing-china.html">마드리드 방식과 직접 출원 비교</a>를 보십시오.</p>
"""),
            ('planning-separate-filings', '별도 출원을 어떻게 짤까', """
<p class="leading-relaxed text-slate-300 mb-6">등록부가 따로이므로 브랜드를 쓰는 시장, 혹은 쓸 가능성이 있는 시장마다 별도 출원을 짭니다. 출원은 각 지역 주관 기관에 그곳의 절차·서식·언어·분류 실무에 따라 냅니다. CNIPA에서 통과한 지정이 다른 곳에서도 그대로 통과한다고 보지 말고, 현지 구분표에 맞춰 상품·서비스를 현지 대리인이 조정하게 하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">순서는 사업상 노출에 맞춥니다. 상품이 팔리는 시장, 유통사가 움직이는 시장, 전자상거래에 입점이 뜨는 시장, 모방품이 나오기 쉬운 시장입니다. 단계를 밟아 전개한다면 선출원주의에서는 먼저 출원한 자가 유리하므로, 각 지역에서 공개보다 먼저 출원하십시오. 영문 표장과 중국어 표장은 어느 등록부에서든 따로 출원하고, 도형상표가 필요한지는 시장마다 정합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">여기서는 출원 비용·관납료·처리 기간의 금액이나 수치를 싣지 않습니다. 등록부·클래스·당기 요금표에 따라 달라지고 출원 시점의 공식 공고·규칙으로 확인해야 하기 때문입니다. 포트폴리오 전체에 한 숫자를 적용하지 말고 시장마다 현지 대리인에게 당기 견적을 구하십시오.</p>
"""),
            ('a-coordinated-portfolio-checklist', '공통 포트폴리오 체크리스트', """
<p class="leading-relaxed text-slate-300 mb-6">공통으로 정리한 포트폴리오는 네 장의 등록증 이상입니다. 다음을 쓰십시오.</p>
<ol>
<li><strong>시장을 적어 냅니다.</strong> 네 등록부 각각에 어떤 클래스·어떤 표장·어느 현지 법인이 권리를 가지는지 기록합니다.</li>
<li><strong>영문명과 중국어명을 따로 출원</strong>하십시오. 별개의 권리입니다.</li>
<li><strong>사용 증거를 등록부마다 보관</strong>하십시오. 현지 요건을 채우는, 날짜 있는 판매·세금계산서·광고·전자상거래 기록입니다.</li>
<li><strong>사용 허락과 유통사 관계를 문서화</strong>해, 필요하면 현지 파트너의 사용을 입증할 수 있게 합니다.</li>
<li><strong>워칭과 갱신 일정을 세 지역 등록부까지 넓히고</strong>, CNIPA 공고로만 한정하지 않습니다.</li>
<li><strong>해마다 점검하십시오.</strong> 권리자 명칭·주소·클래스 범위를 확인합니다. 낡은 포트폴리오는 권리 행사가 어렵습니다.</li>
</ol>
<div class="callout callout-info"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>하나의 브랜드, 네 등록부.</strong> 출원 기본은 <a href="{L}/china-trademark-registration-complete-guide-2026.html">중국 상표 등록 가이드</a>와 <a href="{L}/china-first-to-file-trademark-guide.html">선출원주의 가이드</a>를 본 뒤, 세 지역 현지 출원을 별도 작업으로 더하십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: CNIPA 등록의 효력이 중국 본토(대륙)에 한정된다는 점, 중국 중국 홍콩·중국 마카오·중국 대만이 각각 별개의 상표 제도를 가지며 각지 주관 기관에 출원해야 한다는 점, 중국 본토(대륙)와 세 지역 사이에 자동 상호 보호가 없다는 점, 그리고 마드리드 지정 중국이 세 지역에 미치지 않는다는 점. 세 지역은 모두 중국의 일부입니다. 출원 서식·비용·실무는 각지 주관 기관이 정하며 달라질 수 있으므로 출원 전에 당기 공식 공고·규칙을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>네 등록부 모두를 확보하시겠습니까?</strong> <a href="/contact.html">중국 본토(대륙), 중국 중국 홍콩, 중국 마카오, 중국 대만을 아우르는 공통 출원 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
    'decision': {
        'slug': 'china-trademark-squatting-decision-table',
        'title': '이의·무효심판·매수 중 무엇을 고를까: 선점 등록 비교표',
        'desc': '선점 등록에 이르는 다섯 경로를 시간·통제권·증거·위험으로 정성 비교합니다. 무엇이 맞는지는 충돌 권리가 어느 단계에 있는지가 정합니다.',
        'lede': '자사 상표를 다른 사람이 중국에서 출원·등록했다는 걸 알아도 답은 하나가 아닙니다. 이의, 무효심판, 불사용 취소, 매수 협상, 재출원은 시간·통제권·증거·위험이 저마다 다릅니다.',
        'card_text': '다섯 회복 경로의 정성 비교표, 함께 쓰는 경우, 그리고 비용·성공률·심리 기간을 표에 넣지 않는 이유.',
        'category': '가이드',
        'read_time': '약 9분',
        'tags': ['선점 등록', '이의 제기', '무효심판'],
        'related': [
            ('{L}/trademark-registered-by-someone-else-china.html', '상표를 먼저 등록당했을 때'),
            ('{L}/china-trademark-opposition-watch-sop-2-months.html', '이의 2개월 대응 절차'),
            ('{L}/china-trademark-assignment-licence-recordal.html', '양도와 사용 허락 등록'),
        ],
        'sections': [
            ('five-routes-one-decision', '다섯 경로, 하나의 판단', """
<p class="leading-relaxed text-slate-300 mb-6">자사 상표를 다른 사람이 중국에서 출원·등록했다는 걸 알아도, 하나의 문제에 하나의 답이 있는 것은 아닙니다. 현실적인 경로는 다섯이고 차이는 비용보다 시간·통제권·증거·위험에서 드러납니다. 공고된 출원에 대한 <strong>이의 제기</strong>, 등록에 대한 <strong>무효심판</strong>, <strong>불사용 취소</strong>, <strong>매수·양도 협상</strong>, 그리고 <strong>새 출원</strong>이며 경우에 따라 이름을 바꾸는 일을 동반합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">무엇이 맞는지는 충돌 권리가 어느 단계에 있는지가 정합니다. 공고 단계의 출원과, 오래 등록되어 한 번도 쓰이지 않은 등록은 다른 문제이며, 팔 뜻이 있는 전 유통사가 가진 등록은 또 다릅니다. 먼저 충돌 상표의 상태, 자사의 선행 권리, 그리고 실제로 쫓고 있는 사업상 기한을 확정하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">틀이 되는 조항이 둘 있습니다. 제20조는 선행 등록·출원 상표와 동일·유사한 표장을 거절하고, 제24조는 선행 적법 권익과 악의적 선점 등록에 대응합니다. 실제로 어느 경로를 쓸 수 있는지 정하는 것은 중국에서의 선행 사용과 인지도 증거의 힘입니다.</p>
"""),
            ('the-decision-table', '판단을 위한 비교표', """
<p class="leading-relaxed text-slate-300 mb-6">아래 표는 일부러 수치를 넣지 않고 정리했습니다. 대리인에게 지시하기 전에 가릴 수 있는 네 축으로 비교하며, <strong>비용·성공률·심리에 걸리는 기간은 싣지 않습니다</strong>. 사건, 당기 관납료표, 현행 규칙에 따라 달라지기 때문입니다. 수치는 행동하는 시점의 공식 공고·규칙으로 확인하십시오.</p>
<table>
<thead><tr><th>경로</th><th>시간</th><th>통제권</th><th>증거 부담</th><th>주된 위험</th></tr></thead>
<tbody>
<tr><td>이의 제기</td><td>가장 이른 단계. 공고에서 시작되는 짧은 법정 기간</td><td>높음. 근거와 시점을 우리가 정함</td><td>중간. 선행 권리와 인지도</td><td>기한을 놓치면 같은 출원으로 다시 다툴 수 없음</td></tr>
<tr><td>무효심판</td><td>뒤 단계. 법정 기간의 제약이 있고 저명상표 악의 등록에는 예외</td><td>높음. 근거를 넓게 주장 가능</td><td>무거움. 인지도·악의·선행 권리</td><td>증거 의존이 커 결말이 읽히지 않음</td></tr>
<tr><td>불사용 취소</td><td>법정 기간에 걸쳐 사용이 없는 상태가 된 뒤. 당국이 직권으로 움직이기도 함</td><td>중간. 제3자 또는 당국이 주도할 수 있음</td><td>진정한 사용을 등록자가 입증하는 쪽으로 옮김</td><td>그 자체로는 우리에게 등록을 주지 않음</td></tr>
<tr><td>매수·양도</td><td>협상 나름이며 법정의 고정된 일정은 없음</td><td>가장 높음. 거래 조건을 우리가 정함</td><td>가볍지만 이전은 심사됨</td><td>인가되지 않을 가능성, 가격과 협상력</td></tr>
<tr><td>재출원·이름 변경</td><td>바로 움직이지만 새 출원으로 시작</td><td>중간. 새 표장을 조사할 수 있는지에 달림</td><td>출원은 가볍고 식별력 입증이면 무거움</td><td>원래 이름을 놓는 것, 남는 충돌</td></tr>
</tbody>
</table>
<p class="leading-relaxed text-slate-300 mb-6">표는 후보를 좁히는 데 쓰고 결정 자체에 쓰지는 마십시오. 실제로는 이의와 예방적 신규 출원, 취소와 병행하는 매수 협상 등을 함께 쓰는 게 보통이며, 통제권과 위험을 관리할 수 있는 곳이 바로 그 조합입니다.</p>
"""),
            ('when-opposition-fits', '이의가 맞는 경우', """
<p class="leading-relaxed text-slate-300 mb-6">이의 제기는 기한이 가장 짧은 대신 효과가 가장 큰 경로입니다. 출원이 등록으로 자라기 전에 다툴 수 있습니다. 개정법에서는 <strong>2027년 1월 1일</strong>부터 이의 제기 기간이 초보심정 공고일부터 3개월→<strong>2개월</strong>로 줄어듭니다. 탐지에서 제출까지의 사슬 전체가 그 기간이지, 경고 기간이 아닙니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">그래서 감시·결재 권한·증거 패키지가 먼저 갖춰져 있지 않으면 작동하지 않습니다. 등록부를 가끔 보는 정도의 운영으로는 첫 사내 회의가 끝나기도 전에 기한을 잃습니다. 현지 대리인에게 미리 위임장을 맡기고, 공고일을 기록하며, 선행 권리와 인지도 자료를 상비해 더할 것은 충돌 출원 정보뿐인 상태로 두십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">대신 주장은 비교적 얇은 사실 기록 위에서 이루어지고 상대도 답변할 수 있습니다. 충돌이 뚜렷하고 증거가 강하다면 나쁜 교환이 아닙니다. 운영 절차는 <a href="{L}/china-trademark-opposition-watch-sop-2-months.html">이의 2개월 대응 절차</a>를 보십시오.</p>
"""),
            ('when-invalidation-or-cancellation-fit', '무효심판·불사용 취소가 맞는 경우', """
<p class="leading-relaxed text-slate-300 mb-6">등록까지 되면 무효심판과 불사용 취소가 주력이 됩니다. 제51조는 무효심판 청구에 <strong>5년</strong>의 기간을 정하지만, 저명상표의 악의 등록은 <strong>그 5년 제한을 받지 않습니다</strong>. 이 차이가 경로 가능성을 가르는 일이 많으므로 먼저 등록일과 주장 근거를 확정하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">제57조는 등록상표가 지정상품의 일반명칭이 되었거나 정당한 사유 없이 <strong>3년 연속</strong> 사용되지 않은 경우의 취소를 정하고, 당국이 직권으로 취소하는 것도 허용합니다. 한 번도 거래하지 않은 차단권자에게는 유효하지만, 장애물을 없앨 뿐 우리에게 권리를 주는 것은 아니므로 이어질 출원까지 설계합니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">둘 다 증거가 무거운 경로입니다. 무효심판은 선행 권리·중국 내 인지도·상대의 악의가 쟁점이고, 취소는 지정상품에 진정한 사용이 있는지가 쟁점입니다. 다툼이 시작된 뒤 만든 파일이 아니라 날짜와 계약으로 뒷받침된 기록을 남기십시오. 유효한 사용 증거는 <a href="{L}/china-trademark-non-use-cancellation-evidence.html">불사용 취소 증거 가이드</a>를 보십시오.</p>
"""),
            ('when-to-negotiate-or-refile', '협상·재출원을 고르는 경우', """
<p class="leading-relaxed text-slate-300 mb-6">매수 협상은 확실성에 가장 빨리 닿는 경로인 경우가 많고, 가격, 양도 범위, 공존이나 이행 조건까지 우리가 정하므로 통제권도 가장 큽니다. 다만 순수한 사적 거래는 아닙니다. 제46조는 <strong>혼동을 일으키기 쉽거나 그 밖의 악영향을 주는 양도는 인가하지 않는다</strong>고 정해, 이전은 단순히 기록되는 데 그치지 않고 심사됩니다. 거래 논리를 기록하고 양도 서류를 정리한 뒤, 이전을 기대하기 전에 당기 출원 서식을 확인하십시오.</p>
<p class="leading-relaxed text-slate-300 mb-6">원래 표장이 약하거나, 증거가 얇거나, 사업 일정이 다툼을 기다릴 수 없을 때의 현실적인 해법이, 이름 변경을 동반하기도 하는 새 출원입니다. 바로 움직이지만 양보하는 점도 있습니다. 소비자가 이미 익힌 이름을 잃을 수 있고, 남은 충돌 권리가 새 출원을 막거나 좁힐 수 있습니다. 새 후보는 중국어 표기를 포함해 먼저 조사하십시오.</p>
<div class="callout callout-warning"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>경로뿐 아니라 순서를 정하십시오.</strong> 이의·무효심판·취소·매수·재출원은 함께 쓰는 게 보통이고, 그 순서가 통제권과 노출을 바꿉니다. 본 글은 일부러 수치를 넣지 않은 비교에 머물렀습니다. 제3자 요약에 있는 비용·성공률·처리 기간을 믿지 말고 현행 공식 규칙 아래에서의 전망을 대리인에게 확인하십시오.</p></div>
"""),
            ('sources', '출처 및 유의사항', """
<p class="leading-relaxed text-slate-300 mb-6">1차 자료: 『중화인민공화국 상표법(2026년 개정)』 제20조·제24조·제36조·제46조·제51조·제57조(2026년 6월 26일 채택, 2027년 1월 1일 시행), 선점 등록 대응에 관한 일반 실무 해설. 2개월 이의 기간은 2027년 1월 1일부터 적용됩니다. 5년 무효 기간과 저명상표 예외, 3년 미사용, 제46조 양도 심사는 법정 틀이지 결과의 예측이 아닙니다. 본 글은 시간·통제권·증거·위험에 대해 일부러 수치를 넣지 않은 비교에 머물며 비용·성공률·심리 기간은 싣지 않았습니다. 행동 전에 당기 공식 공고·규칙을 확인하십시오. 본 글은 일반 정보이며 법률 자문이 아닙니다.</p>
<div class="callout"><p class="leading-relaxed text-slate-300 mb-6" style="margin:0"><strong>선점 등록에 어떤 경로로 임할지 고민되시나요?</strong> <a href="/contact.html">사건별 순서와 증거 계획에 대해 문의하세요</a>.</p></div>
"""),
        ],
    },
}}
