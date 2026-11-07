# -*- coding: utf-8 -*-
"""Patch the batch-1 hub comparison tables (EN/JA/KO) with Arts. 46 and 55.

Adds two comparison rows and a short explanatory section to the hub article in
each language, then the normal publisher rebuilds the six batch-1 pages.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

TARGET = HERE / 'p0_2027_content.py'

ROWS = [
    """<tr><td>Assignment of a registered mark</td><td>Formal review of the assignment (Art. 42)</td><td>Adds substantive review: transfers likely to cause confusion or other adverse effects are <strong>not approved</strong> (Art. 46)</td></tr>
<tr><td>Licensing and recordal</td><td>Licensor supervises quality; licence filed; unrecorded licence not enforceable against bona fide third parties (Art. 43)</td><td>Same duties plus a <strong>statutory termination right</strong> for the licensor where the licensee fails quality obligations (Art. 55)</td></tr>
""",
    """<tr><td>登録商標の譲渡</td><td>形式審査を中心とした譲渡手続（旧法第42条）</td><td>実体審査を追加。<strong>混同その他の不良な影響を生じるおそれのある譲渡は認可しない</strong>（第46条）</td></tr>
<tr><td>ライセンスと届出</td><td>許諾者の品質監督、届出、未届出ライセンスは善意の第三者に対抗不可（旧法第43条）</td><td>上記に加え、被許諾者が品質保証義務を怠った場合の<strong>許諾者の法定解除権</strong>を新設（第55条）</td></tr>
""",
    """<tr><td>등록상표의 양도</td><td>형식 심사 중심의 양도 절차(구법 제42조)</td><td>실체 심사 추가. <strong>혼동이나 그 밖의 불량한 영향을 줄 우려가 있는 양도는 허가하지 않음</strong>(제46조)</td></tr>
<tr><td>라이선스와 등록</td><td>허락자의 품질 감독, 등록, 미등록 라이선스는 선의의 제3자에게 대항 불가(구법 제43조)</td><td>위 의무에 더해 피허락자가 품질 의무를 이행하지 않을 때 <strong>허락자의 법정 해제권</strong> 신설(제55조)</td></tr>
""",
]

SECTIONS = [
    """('post-registration-changes', 'Two Changes for Post-Registration Rights', \"\"\"
<p class="leading-relaxed text-slate-300 mb-6">Two provisions in the chapters on registration maintenance and trademark administration matter once a mark is registered, and are easy to miss when reading a summary of the revision.</p>
<h3>Assignment is no longer a purely formal step (Art. 46)</h3>
<p class="leading-relaxed text-slate-300 mb-6">The 2019 law treated assignment largely as a filing exercise. Article 46 adds a third paragraph: a transfer that is likely to cause confusion or have other adverse effects <strong>shall not be approved</strong>. When a brand buys a mark back from a factory, distributor or squatter, the assignment documents should now explain the relationship between the parties, the commercial rationale, how related or similar marks held by the assignor will be dealt with, and how goods and channels will be kept distinct. Article 47 adds a parallel qualification rule for collective and certification marks.</p>
<h3>Licensors gain a statutory termination right (Art. 55)</h3>
<p class="leading-relaxed text-slate-300 mb-6">Article 55 keeps the licensor's duty to supervise quality, the licensee's duty to guarantee it, the marking requirement, and the rule that an unrecorded licence cannot be asserted against a bona fide third party. It adds that where the licensee fails its quality obligations, the licensor may terminate the licence &mdash; a statutory right that does not depend on a termination clause in the contract.</p>
<p class="leading-relaxed text-slate-300 mb-6">For the practical workflow, see <a href="{L}/china-trademark-assignment-licence-recordal.html">Trademark Assignment &amp; Licence Recordal in China</a>.</p>
\"\"\"),
            """,
    """('post-registration-changes', '登録後の権利に関わる2つの変更', \"\"\"
<p class="leading-relaxed text-slate-300 mb-6">登録後の権利に関わる2つの規定は、改正の概要だけを読むと見落とされやすい箇所です。</p>
<h3>譲渡はもはや純粋な形式手続ではない（第46条）</h3>
<p class="leading-relaxed text-slate-300 mb-6">2019年法では譲渡は主に書類提出による手続でした。第46条は第三項を追加し、<strong>混同を生じさせ、または他の不良な影響を及ぼすおそれのある譲渡は認可しない</strong>と定めます。工場、販売店、ハイジャッカーから商標を買い戻す場合、譲渡書類には当事者間の関係、事業上の根拠、譲渡人が保有する関連・類似商標の扱い、商品と流通をどう分けるかを記載すべきです。第47条は集団商標・証明商標について譲受人の資格と監督能力を求める並行規定を置きます。</p>
<h3>許諾者に法定解除権（第55条）</h3>
<p class="leading-relaxed text-slate-300 mb-6">第55条は、許諾者の品質監督義務、被許諾者の品質保証義務、被許諾者名称・産地の表示、および届出のないライセンスは善意の第三者に対抗できないという規則を維持したうえで、被許諾者が品質保証義務を履行しない場合に<strong>許諾者がライセンス契約を解除できる</strong>と追加しました。契約に解除条項がなくても認められる法定の権利です。</p>
<p class="leading-relaxed text-slate-300 mb-6">実務手順は<a href="{L}/china-trademark-assignment-licence-recordal.html">「中国商標の譲渡とライセンス届出」</a>をご覧ください。</p>
\"\"\"),
            """,
    """('post-registration-changes', '등록 후 권리에 관한 두 가지 변경', \"\"\"
<p class="leading-relaxed text-slate-300 mb-6">등록 후 권리와 관련된 두 조항은 개정 요약만 읽으면 놓치기 쉬운 부분입니다.</p>
<h3>양도는 더 이상 순수한 형식 절차가 아니다(제46조)</h3>
<p class="leading-relaxed text-slate-300 mb-6">2019년 법에서 양도는 주로 서류 제출 절차였습니다. 제46조는 제3항을 추가해 <strong>혼동이나 그 밖의 불량한 영향을 줄 우려가 있는 양도는 허가하지 않는다</strong>고 정합니다. 공장·유통사·도용자로부터 상표를 매입할 때 양도 서류에는 당사자 관계, 사업상 근거, 양도인이 보유한 관련·유사 상표의 처리, 상품과 유통을 어떻게 분리할지를 기재해야 합니다. 제47조는 단체상표·증명상표에 대해 양수인의 자격과 감독 능력을 요구하는 병행 규정을 둡니다.</p>
<h3>허락자에게 법정 해제권(제55조)</h3>
<p class="leading-relaxed text-slate-300 mb-6">제55조는 허락자의 품질 감독 의무, 피허락자의 품질 보증 의무, 피허락자 명칭·산지 표시, 그리고 등록되지 않은 라이선스는 선의의 제3자에게 대항할 수 없다는 규칙을 유지하면서, 피허락자가 품질 보증 의무를 이행하지 않으면 <strong>허락자가 라이선스 계약을 해제할 수 있다</strong>고 추가했습니다. 계약에 해제 조항이 없어도 인정되는 법정 권리입니다.</p>
<p class="leading-relaxed text-slate-300 mb-6">실무 절차는 <a href="{L}/china-trademark-assignment-licence-recordal.html">「중국 상표 양도와 라이선스 등록」</a>을 참고하십시오.</p>
\"\"\"),
            """,
]


def main():
    text = TARGET.read_text(encoding='utf-8')
    if 'post-registration-changes' in text:
        print('[patch] already applied, skipped')
        return
    side = re.findall(r"\('side-by-side', '([^']+)'", text)
    trans = re.findall(r"\('transition-measures', '([^']+)'", text)
    print('side-by-side headings:', side)
    print('transition headings:', trans)
    if len(side) != 3 or len(trans) != 3:
        raise RuntimeError('unexpected number of hub sections')
    for i in range(3):
        anchor = "('side-by-side', '" + side[i] + "'"
        start = text.index(anchor)
        end = text.index('</tbody>', start)
        text = text[:end] + ROWS[i] + text[end:]
        marker = "('transition-measures', '" + trans[i] + "'"
        pos = text.index(marker)
        text = text[:pos] + SECTIONS[i] + text[pos:]
        print(f'[patch] applied {i + 1}/3')
    TARGET.write_text(text, encoding='utf-8')
    print('[patch] done')


if __name__ == '__main__':
    main()
