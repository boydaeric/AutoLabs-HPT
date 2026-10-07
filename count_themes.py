#!/usr/bin/env python3
"""Keyword-match theme counts behind the "top recurring arguments" in output/comment_analysis.md.

Each theme is a regex over the full comment text (comment body + attachments). The counts are
approximate: a pattern can over-match (a passing mention) or under-match (a different phrasing),
so the report quotes them rounded and hedged ("about 230"), never as exact tallies.

  python3 count_themes.py                  # all themes, both docket views
  python3 count_themes.py THEME [N]        # also print N example sentences for one theme

Views: "as filed" groups comments by the docket on regulations.gov; "corrected" groups them by the docket
whose rule the letter addresses (docket_corrections.csv). "distinct" counts campaign copies once.
"""
import sys, re, csv, json
import comment_text_utils as U, comment_tagger as T
C = U.load_comments()
rows={r['comment_id']:r for r in csv.DictReader(open('output/comments_tagged.csv', newline='', encoding='utf-8'))}
R=lambda p: re.compile(p, re.I)
TH={'CMS-2026-1916':{
 'statute':R(r"(beyond|exceed\w*|go(es)? (well |far )?beyond) (what |the scope of )?(the statute|congress|statutory|the law|its (statutory )?authority|section 71116|H\.?R\.? ?1|the WFTC|OBBBA)|four (statutory )?(service|categor)|congressional intent"),
 'cbo_vs_cms':R(r"\$?510(\.1)? ?(billion|B)\b|\$?149(\.4)? ?billion|three times"),
 'aggregate':R(r"in the aggregate|aggregate (basis|level|calculation|limit|approach)|\bUPL\b|upper payment limit"),
 'phasedown_pp':R(r"percentage points?"),
 'uniform':R(r"uniform (rate |dollar |percentage |dollar or percentage )?increase"),
 'gemt':R(r"\bGEMT\b|ground emergency medical|ambulance fee schedule|fire[- ]based EMS"),
 'ffs_limit':R(r"447\.381|(limit|cap)s? (on|for) (targeted|fee[- ]for[- ]service|FFS)|targeted (FFS|fee[- ]for[- ]service) (supplemental )?payment limit|FFS (practitioner |supplemental )?(payment )?limit"),
 'medicare_inadequate':R(r"medicare[^.]{0,60}(below (the )?cost|do(es)? not cover|inadequate|fail(s)? to cover|underpa)"),
 'childrens':R(r"IPPS[- ]exempt|freestanding children|children'?s hospitals?"),
 'behavioral':R(r"CCBHC|certified community behavioral|crisis (services|response)|community mental health cent"),
 'no_medicare_rate':R(r"(no|absence of|without|lack(s)?)( an?)?( (applicable|specified|comparable|corresponding))?( total)?( published)? medicare (rate|equivalent|payment rate)"),
 'wage_index':R(r"wage index|\bAWI\b"),
 'net_of_tax':R(r"net of (provider )?tax|federal share of the medicaid payment|net[- ]of[- ]tax"),
 'separate_terms':R(r"separate payment terms?"),
 'vbp':R(r"value[- ]based (payment|purchasing|care|SDP)|population[- ]based payment"),
 'support_integrity':R(r"loophole|financing (gimmick|scheme)|money[- ]laundering|shift(ing)? (the )?costs? (on)?to (federal|taxpayers)|gaming"),
},
'CMS-2026-2476':{
 'insurer_class':R(r"services of health insurers|433\.56\(a\)\(19\)|user fee|reinsurance|premium tax"),
 'test_7575':R(r"75/75|second prong"),
 'retro_actual':R(r"retroactiv|retrospectiv|actual (tax )?collections?|prospective"),
 'excess_only':R(r"(only|just) the (tax )?(amount|portion) (in excess|above)|amount in excess of the|entire (provider )?tax"),
 'enacted_imposed':R(r"[“\"']?enacted[”\"']? and [“\"']?impos"),
 'measurement_period':R(r"12-month|twelve-month|measurement period"),
 'reporting':R(r"433\.74|reporting (requirement|burden)|december 31, 2026|june 30, 2028"),
 'cms_vs_cbo':R(r"\$?24[56](\.8)? ?(billion|B)\b|\$?183 ?(billion|B)\b|\$?191(\.1)? billion"),
 'coverage_ignored':R(r"1\.[125] million|no effect on (health )?coverage|uninsured"),
 'offset30':R(r"30 percent|offset"),
 'expansion_phasedown':R(r"expansion[- ]state[^.]{0,60}phase|phase[- ]?down[^.]{0,60}expansion|3\.5 percent"),
 'support_integrity':R(r"loophole|financing (gimmick|scheme)|money[- ]laundering|shift(ing)? (the )?costs? (on)?to (federal|taxpayers)|gaming"),
}}
# comments that mention a headline federal estimate (used for "cited in about N comments" in the figures tables)
FIG = {'$510 billion (CMS RIA federal savings)': R(r"\$?510(\.1)? ?(billion|B)\b"),
       '$149.4 billion (CBO score of 71116)': R(r"\$?149(\.4)? ?(billion|B)\b"),
       '$774.8 billion (CMS RIA federal + state)': R(r"\$?774(\.8)? ?(billion|B)\b")}


def sents(k):
    t=re.sub(r'\s+',' ',T.boilerplate_stripped(C[k]['text']))
    return re.split(r"(?<=[.!?])\s+(?=[A-Z“\"(])", t)
def main():
    theme_arg = sys.argv[1] if len(sys.argv) > 1 else None
    n_examples = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for which, themes in TH.items():
        print(f"\n{which} ({'CMS-2449-P' if which.endswith('1916') else 'CMS-2452-P'})")
        print(f"{'theme':22} {'comments':>16} {'distinct texts':>16}   (as filed / corrected)")
        for th, pat in themes.items():
            if theme_arg and th != theme_arg:
                continue
            hit = {k for k in C if pat.search(C[k]['text'])}
            cols = []
            for dk, rk in (('docket', 'campaign_role'), ('docket_corrected', 'campaign_role_corrected')):
                ids = [k for k in hit if C[k][dk] == which]
                dist = [k for k in ids if rows[k][rk] in ('unique', 'representative')]
                cols.append((len(ids), len(dist), dist))
            print(f"{th:22} {cols[0][0]:>7} / {cols[1][0]:<7} {cols[0][1]:>7} / {cols[1][1]:<7}")
            if theme_arg:
                for k in cols[1][2][:n_examples]:
                    r = rows[k]
                    if r['commenter_type'] == 'individual':
                        continue
                    s = next((x for x in sents(k) if pat.search(x) and 8 < len(x.split()) < 60), None)
                    if s:
                        print(f"  {k[9:]} [{r['commenter_type'][:5]}|{r['position'][:4]}] {(r['commenter_org'] or '')[:35]} :: {' '.join(s.split()[:40])}")
    if not theme_arg:
        print("\nCMS-2449-P comments mentioning a headline estimate (as filed / corrected)")
        for lab, pat in FIG.items():
            hit = {k for k in C if pat.search(C[k]['text'])}
            cols = []
            for dk, rk in (('docket', 'campaign_role'), ('docket_corrected', 'campaign_role_corrected')):
                ids = [k for k in hit if C[k][dk] == 'CMS-2026-1916']
                cols.append((len(ids), sum(rows[k][rk] in ('unique', 'representative') for k in ids)))
            print(f"{lab:42} {cols[0][0]:>5} / {cols[1][0]:<5} comments  {cols[0][1]:>4} / {cols[1][1]:<4} distinct   (all dockets: {len(hit)})")


if __name__ == '__main__':
    main()
