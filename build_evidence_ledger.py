#!/usr/bin/env python3
"""Build output/evidence_ledger_delta.csv: every dollar figure, and every percentage or count
cited as an impact (loss, cut, reduction, closure...), in the comments on CMS-2449-P / CMS-2452-P.

claim   = verbatim excerpt (<=25 words) around the figure, machine-extracted from the comment text.
docket  = docket the comment was filed in on regulations.gov; docket_corrected = docket of the rule the
          letter addresses (differs only for letters listed in docket_corrections.csv).
figure  = the figure exactly as written.
file    = the file the excerpt was found in (comment body JSON or the attachment); located by
          re-reading each attachment's text layer. Where the excerpt only exists in OCR output,
          the OCR'd attachment is named and `file_basis` says so.
figure_source_inferred = rule-based guess (INFERRED, not read) whether the figure is the
          commenter's own number, a citation of CMS / the proposed rule, a third party, or an
          illustrative example.
Verification (see output/verification_log.csv): corrections in ledger_corrections.csv are applied
after extraction, keyed by ledger_row (the 1-based row number before corrections) and checked
against comment ID + figure so a stale correction fails loudly instead of editing the wrong row.
`page`, `verification_status` and `verification_note` are joined from the verification log.
"""
import csv
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path

import comment_tagger as T
import comment_text_utils as U

OUT = Path("output/evidence_ledger_delta.csv")
CORRECTIONS = Path("ledger_corrections.csv")
VERIFICATION_LOG = Path("output/verification_log.csv")
DOLLAR = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?(?:\s*(?:billion|million|thousand|trillion)|\s?[BMK]\b)?", re.I)
BIG = re.compile(r"(?<![\d.,$])\b\d[\d,]*(?:\.\d+)?\s*(?:billion|million)\b", re.I)
PCT = re.compile(r"(?<![\d.,])\b\d{1,3}(?:\.\d+)?\s?(?:%|percent)", re.I)
COUNT = re.compile(r"\b\d[\d,]{0,9}\s+(?:jobs|positions|beds|hospitals|providers|patients|beneficiaries|enrollees|residents|people|children|ambulances|units|clinics|facilities)\b", re.I)
# percentages / counts only count as an impact estimate in a sentence about a loss, cut or effect
IMPACT = re.compile(r"\b(los[se]s?|lost|losing|cuts?|cutting|reduc\w*|declin\w*|decreas\w*|shortfall|deficit|eliminat\w*|clos(e|ing|ure|ures)|jeopardiz\w*|layoffs?|impact(ed|s)?|estimat\w*|project(ed|ion)s?|would (lose|cut|reduce|face|result)|at risk)\b", re.I)
# the rule's own parameters are not impact estimates
RULE_PARAM = re.compile(r"^(100|110|10|6|5\.5|5|4|3\.5|3|2\.5|0\.5|75|25|50)\s?(%|percent)$", re.I)
SRC_CMS = re.compile(r"\b(CMS|the agency|the proposed rule|the NPRM|regulatory impact|OACT|Office of the Actuary|preamble|Federal Register|FR \d|\d+ Fed\. ?Reg)\b", re.I)
SRC_THIRD = re.compile(r"\b(CBO|Congressional Budget Office|MACPAC|KFF|Kaiser|Urban Institute|GAO|Manatt|AHA analysis|Health Management Associates|HMA|Moody|Georgetown|CBPP|Center on Budget|Commonwealth Fund|study|report|analysis by|according to)\b", re.I)
SRC_EXAMPLE = re.compile(r"\b(for example|example|hypothetical|illustrat|State A|State B|assume|suppose)\b", re.I)
SRC_OWN = re.compile(r"\b(we|our|us|I|my)\b", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9$%.]+", " ", s.lower()).strip()


@lru_cache(maxsize=None)
def file_text(path):
    p = Path(path)
    try:
        if p.suffix == ".pdf":
            return norm(subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=120).stdout)
        if p.suffix == ".docx":
            import docx
            d = docx.Document(str(p))
            parts = [x.text for x in d.paragraphs] + [c.text for t in d.tables for row in t.rows for c in row.cells]
            return norm("\n".join(parts))
    except Exception:  # noqa: BLE001
        return ""
    return ""


def excerpt(sentence, fig, max_words=25):
    words = sentence.split()
    pos = sentence.find(fig)
    idx = len(sentence[:pos].split()) if pos >= 0 else 0
    lo = max(0, idx - 11)
    hi = min(len(words), lo + max_words - 1)  # leave room so excerpt stays <= 25 words
    lo = max(0, hi - (max_words - 1))
    ex = " ".join(words[lo:hi])
    return ("…" if lo > 0 else "") + ex + ("…" if hi < len(words) else "")


def locate(rec, ex):
    probe = norm(ex.strip("…"))
    probe_words = probe.split()
    key = " ".join(probe_words[2:9]) if len(probe_words) > 9 else probe
    body = norm(U.clean(rec.get("comment") or ""))
    if key and key in body:
        return f"data/{rec['docket']}/{rec['id']}.json (comment field)", "text layer"
    ocr_candidates = []
    for a in rec["text_info"].get("attachments", []):
        path = f"data/{rec['docket']}/attachments/{a['file']}"
        if key and key in file_text(path):
            return path, "text layer"
        if a.get("ocr_pages"):
            ocr_candidates.append(path)
    if ocr_candidates:
        return ocr_candidates[0], "OCR output (INFERRED file: text found only after OCR)"
    atts = rec["text_info"].get("attachments", [])
    if atts:
        return f"data/{rec['docket']}/attachments/{atts[0]['file']}", "INFERRED file: excerpt not re-located"
    return f"data/{rec['docket']}/{rec['id']}.json (comment field)", "INFERRED file: excerpt not re-located"


def source_guess(sentence):
    if len(DOLLAR.findall(sentence)) + len(PCT.findall(sentence)) >= 6:
        return "table / data series (INFERRED)"
    if SRC_EXAMPLE.search(sentence):
        return "illustrative example (INFERRED)"
    if SRC_THIRD.search(sentence):
        return "cites third-party source (INFERRED)"
    if SRC_CMS.search(sentence) and not SRC_OWN.search(sentence):
        return "cites CMS / proposed rule (INFERRED)"
    if SRC_OWN.search(sentence):
        return "commenter's own figure (INFERRED)"
    return "unclear (INFERRED)"


def apply_verification(rows, tagged):
    for i, r in enumerate(rows, 1):
        r["ledger_row"] = i
    by_row = {r["ledger_row"]: r for r in rows}
    original = {r["ledger_row"]: (r["comment ID"], r["figure"]) for r in rows}
    dropped = set()
    if CORRECTIONS.exists():
        for c in csv.DictReader(CORRECTIONS.open(newline="", encoding="utf-8")):
            if c["action"] == "add":
                d = json.loads(c["value"])
                tg = tagged[d["comment ID"]]
                d.update(commenter_type=tg["commenter_type"], campaign_id=tg["campaign_id"], docket_corrected=tg["docket_corrected"],
                         figure_source_inferred="added in verification (verified)",
                         file_basis="text layer",
                         ledger_row=len(rows) + 1)
                rows.append(d)
                by_row[d["ledger_row"]] = d
                continue
            n = int(c["ledger_row"])
            if original.get(n) != (c["comment ID"], c["figure"]):
                raise SystemExit(f"stale correction for ledger_row {n}: expected {c['comment ID']} {c['figure']}, found {original.get(n)}")
            if c["action"] == "drop":
                dropped.add(n)
            else:
                by_row[n][c["field"]] = c["value"]
    log = {}
    if VERIFICATION_LOG.exists():
        for v in csv.DictReader(VERIFICATION_LOG.open(newline="", encoding="utf-8")):
            log[int(v["ledger row"])] = v
    for r in rows:
        v = log.get(r["ledger_row"], {})
        r["page"] = v.get("page", "")
        r["verification_status"] = v.get("status", "")
        r["verification_note"] = " ".join(x for x in (v.get("correction", ""), v.get("note", "")) if x)
    return [r for r in rows if r["ledger_row"] not in dropped]


def main():
    C = U.load_comments()
    tagged = {r["comment_id"]: r for r in csv.DictReader(open("output/comments_tagged.csv", newline=""))}
    rows = []
    for cid in sorted(C):
        rec, tg = C[cid], tagged[cid]
        text = re.sub(r"\s+", " ", T.boilerplate_stripped(rec["text"]))
        seen = set()
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"(•])", text):
            s = s.strip()[:1200]
            figs = [m.group(0).strip() for m in DOLLAR.finditer(s)] + [m.group(0).strip() for m in BIG.finditer(s)]
            if IMPACT.search(s):
                figs += [m.group(0).strip() for m in PCT.finditer(s) if not RULE_PARAM.match(m.group(0).strip())]
                figs += [m.group(0).strip() for m in COUNT.finditer(s)]
            for fig in dict.fromkeys(figs):
                if (fig, s[:80]) in seen:
                    continue
                seen.add((fig, s[:80]))
                ex = excerpt(s, fig)
                path, basis = locate(rec, ex)
                rows.append({
                    "claim": f"“{ex}”",
                    "figure": fig,
                    "commenter": tg["commenter_org"] or tg["commenter_name"] or "(anonymous)",
                    "docket": rec["docket"],
                    "docket_corrected": rec["docket_corrected"],
                    "file": path,
                    "comment ID": cid,
                    "commenter_type": tg["commenter_type"],
                    "campaign_id": tg["campaign_id"],
                    "figure_source_inferred": source_guess(s),
                    "file_basis": basis,
                })
    rows = apply_verification(rows, tagged)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "ledger rows from", len({r['comment ID'] for r in rows}), "comments")


if __name__ == "__main__":
    main()
