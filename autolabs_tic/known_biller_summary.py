#!/usr/bin/env python3
"""One line per payer x tax ID holding a known autonomic biller: the
Medicare billers in the group and their office rates (95924 / 95923 global,
95924-26), with Harvard Pilgrim rate tiers. -> output/known_biller_summary.txt"""
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(f"{HERE}/output/tic_autonomic_rates.csv.gz", dtype=str, keep_default_na=False)
k = d[d.known_autonomic_biller == "Y"]
b = pd.read_csv(f"{HERE}/autonomic_billers.csv", dtype=str)
bn = dict(zip(b.npi, b.name + " (" + b.state + ")"))
refs = pd.read_csv(f"{HERE}/output/provider_refs_needed.csv.gz", dtype=str, keep_default_na=False)
refs = refs[refs.npi.isin(bn)]
tb = refs.groupby("tin_value").npi.apply(lambda s: "; ".join(sorted({bn[n] for n in s})))
rows = []
for (payer, tin), g in k.groupby(["payer", "tin_value"]):
    def r(code, mod):
        x = g[(g.code == code) & (g.modifiers == mod) & (g.setting_group == "office")]
        v = sorted(set(x.negotiated_rate[x.negotiated_rate != ""]), key=float)
        v += sorted(set(x.negotiated_percentage[x.negotiated_percentage != ""].map(lambda s: s + "%")))
        t = sorted(set(x.hphc_rate_tier[x.hphc_rate_tier != ""]))
        return ("/".join(v) or "-") + (f" [{','.join(t)}]" if t else "")
    rows.append(dict(payer="BCBSMA" if payer.startswith("Blue") else "HPHC", tin=tin,
                     provider=g.provider_name.iloc[0][:34], medicare_billers=tb.get(tin, ""),
                     hospital=g.hospital_affiliated.iloc[0] or "N",
                     g95924=r("95924", ""), g95923=r("95923", ""), pc95924=r("95924", "26")))
pd.set_option("display.width", 400)
pd.set_option("display.max_colwidth", 90)
txt = ("Known autonomic billers: office rates on the rows that contain the biller NPIs "
       "([Harvard Pilgrim rate tier])\n" + pd.DataFrame(rows).to_string(index=False))
open(f"{HERE}/output/known_biller_summary.txt", "w").write(txt + "\n")
print(txt)
