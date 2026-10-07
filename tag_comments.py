#!/usr/bin/env python3
"""Cluster duplicate / form-letter comments, tag every comment, and write
output/comments_tagged.csv (+ output/campaigns.csv, output/parse_flags.csv).

Inputs : data/<docket>/<id>.json, data/<docket>/_text/<id>.json (extract_comment_text.py)
Docket corrections: docket_corrections.csv lists letters filed in the wrong docket. `docket`/`rule` and the
   `campaign_*` columns stay as filed on regulations.gov; the `*_corrected` columns apply the corrections.
Manual corrections: comment_tag_overrides.csv  (columns: target,field,value,note)
   target is a comment id, or "cluster:<leader id>" to hit every member of that campaign.
"""
import collections
import csv
import json
import re
from pathlib import Path

import comment_tagger as T
import comment_text_utils as U

OUT = Path("output")
OVERRIDES = Path("comment_tag_overrides.csv")
RULE = {"CMS-2026-1916": "CMS-2449-P", "CMS-2026-2476": "CMS-2452-P"}
RULE_SHORT = {"CMS-2449-P": "CMS-2449-P (state directed payment / FFS practitioner payment limits)",
              "CMS-2452-P": "CMS-2452-P (indirect hold harmless threshold for health care-related taxes)"}
EXACT, FORM, VARIANT = 0.98, 0.80, 0.0   # similarity tiers for campaign_role
STOP = {"the", "of", "and", "to", "in", "a", "is", "that", "for", "on", "with", "as", "are", "this", "be", "we", "by", "it"}
VERB = {"oppose": "opposes", "support": "supports", "mixed": "gives mixed views on", "request for changes": "requests changes to",
        "unclear / off-topic": "comments on"}

COLUMNS = ["comment_id", "docket", "rule", "docket_corrected", "rule_corrected", "commenter_name", "commenter_org", "org_source", "posted_date",
           "commenter_type", "commenter_subtype", "state", "state_source", "position", "provisions_addressed",
           "summary", "filing_note", "campaign_id", "campaign_size", "campaign_role", "similarity_to_representative",
           "campaign_id_corrected", "campaign_size_corrected", "campaign_role_corrected",
           "position_basis", "type_confidence", "needs_review", "parse_flag", "text_chars", "n_attachments", "ocr_used", "url"]


def campaign_role(k, lead, sim, size):
    if size == 1:
        return "unique"
    if k == lead:
        return "representative"
    return "exact duplicate" if sim >= EXACT else "form letter" if sim >= FORM else "template variant"


def parse_flags(rec, words):
    ti = rec["text_info"]
    flags = list(ti.get("problems", []))
    ok_atts = [a for a in ti.get("attachments", []) if a.get("status") == "ok"]
    if re.search(r"attach|see file|letter|enclosed", rec.get("comment") or "", re.I) and not ok_atts and not rec["attachments"]:
        flags.append("comment refers to an attachment but none was published")
    if len(words) >= 200:
        r = sum(w in T_STOP for w in words) / len(words)
        if r < 0.12:
            flags.append(f"extracted text looks garbled (stop-word ratio {r:.2f})")
    for a in ti.get("attachments", []):
        if a.get("ocr_pages") and a.get("chars", 0) < 150 * max(1, a["ocr_pages"]):
            flags.append(f"{a['file']}: OCR yielded little text")
    if any(a.get("ocr_pages") for a in ti.get("attachments", [])) and len(words) >= 60:
        r = sum(w in T_STOP for w in words) / len(words)
        if r < 0.12:
            flags.append(f"OCR text may be unreliable (stop-word ratio {r:.2f})")
    if len(words) < 5 and not flags:
        flags.append("almost no text (under 5 words)")
    return "; ".join(dict.fromkeys(flags))


T_STOP = STOP


def load_overrides():
    ov = collections.defaultdict(dict)
    if OVERRIDES.exists():
        for row in csv.DictReader(OVERRIDES.open(newline="")):
            ov[row["target"]][row["field"]] = row["value"]
    return ov


def descriptor(org, ctype, subtype, state, name):
    place = f" ({state})" if state and state != "National" else ""
    if org:
        return f"{org}{place}"
    if ctype == "individual":
        who = {"": "An individual", "pediatrician": "A pediatrician", "physician": "A physician", "nurse/APP": "A nurse/APP",
               "behavioral health clinician": "A behavioral health clinician", "parent/caregiver": "A parent/caregiver",
               "patient/beneficiary": "A patient/beneficiary", "student/academic": "A student/academic",
               "EMS/fire responder": "An EMS/fire responder"}.get(subtype, "An individual")
        return f"{who}{place}"
    return f"A {subtype or ctype}{place}"


def main():
    OUT.mkdir(exist_ok=True)
    C = U.load_comments()
    A = U.cluster(C)                                    # as filed on regulations.gov
    A2 = U.cluster(C, docket_key="docket_corrected")    # after moving misfiled letters (docket_corrections.csv)
    members = collections.defaultdict(list)
    for k, (lead, kind, sim) in A.items():
        members[lead].append(k)
    members2 = collections.defaultdict(list)
    for k, (lead, kind, sim) in A2.items():
        members2[lead].append(k)
    ov = load_overrides()

    base = {}
    for k, rec in C.items():
        text = rec["text"]
        words = U.words(text)
        org, org_src = T.derive_org(rec.get("organization"), text)
        ctype, subtype, tconf = T.classify_type(rec, org, org_src, text)
        state, state_src = T.find_state(rec, org, text)
        pos, pconf = T.classify_position(text, len(words))
        cdock = T.content_docket(text, rec["docket"])
        if cdock != rec["docket_corrected"]:
            raise SystemExit(f"{k}: text addresses {cdock} but docket_corrections.csv puts it in {rec['docket_corrected']}; review and update the file")
        prov = T.classify_provisions(text, cdock)
        base[k] = dict(org=org, org_src=org_src, ctype=ctype, subtype=subtype, tconf=tconf, state=state, state_src=state_src,
                       pos=pos, pconf=pconf, prov=prov, sent=T.best_sentence(text), words=words, cdock=cdock)

    rows = []
    for k in sorted(C):
        rec, b = C[k], base[k]
        lead, kind, sim = A[k]
        size = len(members[lead])
        role = campaign_role(k, lead, sim, size)
        lead2, _, sim2 = A2[k]
        size2 = len(members2[lead2])
        role2 = campaign_role(k, lead2, sim2, size2)
        src = base[lead] if (size > 1 and k != lead and sim >= FORM) else b  # position / provisions / quote inherit within true form letters
        fields = dict(pos=src["pos"], prov=src["prov"], sent=src["sent"], pconf=src["pconf"])
        o = {}
        o.update(ov.get(f"cluster:{lead}", {}))
        if size > 1 and k != lead and sim >= FORM:   # true form letters share the representative's reviewed stance
            o.update({f: v for f, v in ov.get(lead, {}).items() if f in ("position", "provisions_addressed", "quote")})
        o.update(ov.get(k, {}))
        if size > 1 and k != lead and "position" not in ov.get(k, {}):   # every copy of a campaign letter shares the representative's reviewed stance
            o["position"] = ov.get(lead, {}).get("position", base[lead]["pos"])
        position = o.get("position", fields["pos"])
        prov = o["provisions_addressed"].split("; ") if "provisions_addressed" in o else fields["prov"]
        ctype = o.get("commenter_type", b["ctype"])
        subtype = o.get("commenter_subtype", b["subtype"])
        state = o.get("state", b["state"])
        org = o.get("commenter_org", b["org"])
        rule = RULE[rec["docket"]]
        focus = prov[0].split(" (")[0] if prov else ""
        if focus and not focus.split()[0].isupper() and not focus.split()[0].startswith(("GEMT", "SDP", "FFS", "IGT")):
            focus = focus[0].lower() + focus[1:]
        quote = o.get("quote", fields["sent"]) or ""
        if "summary" in o:
            summary = o["summary"]
        else:
            who = descriptor(org, ctype, subtype, state, rec.get("commenter_name"))
            short_quote = rec["comment_only"] if len(b["words"]) < 80 and rec["comment_only"] else quote
            if not short_quote:
                short_quote = " ".join(T.boilerplate_stripped(rec["text"]).split()[:40])
            summary = f"{who} {VERB[position]} {RULE[b['cdock']]}" + (f", focusing on {focus}" if focus else "") + (f": “{T.clean(short_quote).strip()}”" if short_quote else ".")
        flag = parse_flags(rec, b["words"])
        conf = "low" if (b["tconf"] == "low" or fields["pconf"] == "low") else ("medium" if "medium" in (b["tconf"], fields["pconf"]) else "high")
        sub = rec.get("submitter") or {}
        rows.append({
            "comment_id": k, "docket": rec["docket"], "rule": rule,
            "docket_corrected": rec["docket_corrected"], "rule_corrected": RULE[rec["docket_corrected"]],
            "commenter_name": rec.get("commenter_name") or "", "commenter_org": org, "org_source": b["org_src"] if "commenter_org" not in o else "manual",
            "posted_date": (rec.get("posted_date") or "")[:10],
            "commenter_type": ctype, "commenter_subtype": subtype, "state": state, "state_source": b["state_src"] if "state" not in o else "manual",
            "position": position, "provisions_addressed": "; ".join(prov), "summary": summary,
            "filing_note": o.get("filing_note") or (f"text addresses {RULE[b['cdock']]} but was filed in the docket for {rule}" if b["cdock"] != rec["docket"] else ""),
            "campaign_id": lead if size > 1 else "", "campaign_size": size, "campaign_role": role,
            "similarity_to_representative": f"{sim:.2f}" if size > 1 else "",
            "campaign_id_corrected": lead2 if size2 > 1 else "", "campaign_size_corrected": size2, "campaign_role_corrected": role2,
            "position_basis": "inherited from campaign representative" if (size > 1 and k != lead and "position" not in ov.get(k, {})) else ("manual review" if "position" in o else "rule-based"),
            "type_confidence": "manual" if "commenter_type" in ov.get(k, {}) else b["tconf"],
            "needs_review": "yes" if ("commenter_type" not in ov.get(k, {}) and (b["tconf"] == "low" or (ctype == "other" and not subtype))) else "",
            "parse_flag": flag, "text_chars": len(rec["text"]), "n_attachments": len(rec["text_info"].get("attachments", [])),
            "ocr_used": "yes" if any(a.get("ocr_pages") for a in rec["text_info"].get("attachments", [])) else "",
            "url": f"https://www.regulations.gov/comment/{k}",
        })

    with (OUT / "comments_tagged.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, COLUMNS)
        w.writeheader()
        w.writerows(rows)
    byid = {r["comment_id"]: r for r in rows}
    with (OUT / "campaigns.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["campaign_id", "docket", "size", "n_exact_duplicates", "n_form_letters", "n_template_variants", "min_similarity",
                    "position_of_representative", "representative_org", "representative_summary", "member_ids",
                    "docket_corrected", "size_corrected", "n_exact_duplicates_corrected", "n_form_letters_corrected",
                    "n_template_variants_corrected", "member_ids_corrected"])
        for lead, m in sorted(members.items(), key=lambda x: (-len(x[1]), x[0])):
            if len(m) < 2:
                continue
            roles = collections.Counter(byid[x]["campaign_role"] for x in m)
            m2 = members2.get(lead, [lead])                  # the same campaign after docket corrections (same leader)
            roles2 = collections.Counter(byid[x]["campaign_role_corrected"] for x in m2)
            sims = [A[x][2] for x in m if x != lead]
            r = byid[lead]
            w.writerow([lead, r["docket"], len(m), roles["exact duplicate"], roles["form letter"], roles["template variant"],
                        f"{min(sims):.2f}", r["position"], r["commenter_org"], r["summary"], " ".join(sorted(m)),
                        r["docket_corrected"], len(m2), roles2["exact duplicate"], roles2["form letter"], roles2["template variant"],
                        " ".join(sorted(m2))])
        # campaigns that exist only after the move (none today, but keep the file complete if a correction creates one)
        for lead, m2 in members2.items():
            if len(m2) > 1 and len(members.get(lead, [])) < 2:
                raise SystemExit(f"campaign {lead} exists only after docket corrections; extend campaigns.csv writer")
    flagged = [r for r in rows if r["parse_flag"]]
    with (OUT / "parse_flags.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["comment_id", "docket", "docket_corrected", "commenter_name", "commenter_org", "text_chars", "parse_flag", "url"])
        for r in flagged:
            w.writerow([r["comment_id"], r["docket"], r["docket_corrected"], r["commenter_name"], r["commenter_org"], r["text_chars"], r["parse_flag"], r["url"]])

    print(f"as filed : {len(rows)} comments; {len(members)} distinct texts; {sum(1 for m in members.values() if len(m) > 1)} campaigns; {len(flagged)} parse-flagged")
    print(f"corrected: {len(rows)} comments; {len(members2)} distinct texts; {sum(1 for m in members2.values() if len(m) > 1)} campaigns")
    for col in ("commenter_type", "position", "campaign_role", "position_basis", "type_confidence", "needs_review"):
        print(col, dict(collections.Counter(r[col] for r in rows).most_common()))


if __name__ == "__main__":
    main()
