# Verification against primary sources

*Comment analyst's file, October 8, 2026. Follows `review/CONVENTIONS.md`. The full notes, with source URL, page, exact wording and effect on v16, are in the **verification note** column of `review/findings.csv` (U-3 and U-4: `review/findings_v16_unmapped.csv`) and the matching bullets in `review/findings.md`. This pass changed only the verification status and added the verification note. No other field changed, including the v16 flag, the old → new section and the still-open columns.*

## Result by finding

Status is one of: confirmed, corrected, not found, unverifiable. When a finding rests on two sources and they came out differently, each part is listed.

| Finding | What was checked | Status | Primary source and page | What this changes in v16 |
|---|---|---|---|---|
| F-003 | regulations.gov "comments received" vs posted counts (960; 214) | **Unverifiable** (received counter); posted counts re-confirmed | v4 API, October 8, 2026: `meta.totalElements` = 960 (CMS-2026-1916) and 214 (CMS-2026-2476). The document records have no comment-count field. www.regulations.gov returned HTTP 403. | Nothing |
| F-005 | CMS RIA: "no effect on enrollment"; CBPP "full range of scenarios" | **Confirmed** | 91 FR 46590 (CMS-2452-P, sec. V.C.2). The high and low scenarios (46593–46594) do not change it. | Qualifies: CMS assumes zero enrollment effect, which is not the same as v16 sec. 5's "do not model" |
| F-005 | CBO: 1.1 million more uninsured | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-006 | BCBSA: CMS-2452-P's analysis considers CMS-2448-F (sec. 71117) | **Confirmed** | 91 FR 46590 fn 23; 91 FR 46592 (sec. V.C.3, "Offsets"). CMS says the interaction has no significant impact on its estimates. | Qualifies: v16 omits section 71117, but CMS's figures already account for it |
| F-006 | CBPP: CMS-2448-F RIA $78.2B federal / $46.9B state | **Confirmed** | 91 FR 4829 (printed "$78,2 billion"); 2027–2036, real 2027 dollars | – |
| F-006 | CBPP: CBO $34B for the uniformity-waiver provision | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-007 | 30 percent state offset in the central scenario | **Confirmed** | 91 FR 46591. Central scenario also: 65 percent tax-financed, at most 80 percent of cuts on SDPs (46592). High scenario: 20 percent offset (46593). Low scenario: 40 percent (46594). | Qualifies: v16 sec. 3 lists offsets and SDP shares for the low and high estimates only |
| F-008 | THA: CBO assumed states replace 50 percent of lost financing | **Unverifiable** | cbo.gov returned HTTP 403. THA cites no CBO document. | Nothing (hold) |
| F-011 | "would still be a significant reduction to provider payments through Medicaid over time" in the RIA | **Confirmed** | 91 FR 46593 (sec. V, RIA; C.3, after Table 14) | Nothing (v16 does not use it; cite available) |
| F-012 | 91 FR 30462: hospitals bear most cuts, or CMS cannot attribute by provider type | **Confirmed** (both readings, same page) | 91 FR 30462: "The majority of these projected reductions would be for hospitals" (end of the accounting-statement discussion). The RFA paragraph on the same page says CMS lacks data to "reliably attribute or disaggregate these impacts to specific provider types". | Qualifies: v16's Executive summary, sec. 3 and sec. 4 cite only the first reading |
| F-015 | CBPP: the CMS vs CBO gap survives window, interaction and dollar-basis adjustments | **Corrected** (see note) | CMS: $510.1B (91 FR 30451; Table 19 at 30452) + $90.9B (91 FR 46593) = $601.0B. | Qualifies: v16 sec. 5 names these differences, but on CMS's tables they do not close the gap |
| F-015 | CBO $340.5B ($191.1B + $149.4B) | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-022 | IHA: Idaho's inpatient tax is above the phased-down threshold | **Unverifiable** | IHA gives no rate. Idaho Code § 56-1404 sets the rate by an annual calculation, capped at the federal limit, with no fixed percentage. Idaho DHW and medicaid.gov refused connections. | Nothing (Group E placement can be neither confirmed nor contradicted) |
| F-024 | Texas HHSC SFY2027 CHIRP preprint, CMS Rounds 1–4 | **Confirmed** | Texas HHSC PDF p. 17 of 19 (Round 4, sent September 3, 2026; same text on pp. 14 and 16): CMS lists two issues that must be resolved before approval. "Withhold" is Texas's own word, in its response on p. 18. | Nothing |
| F-024 | Texas v. CMS, 805 F. Supp. 3d 734 (E.D. Tex. 2025) | **Unverifiable** | courtlistener.com refused the connection. govinfo's court-opinion search returned no match. | – (v16 item 6 "set aside" vs CHAT "permanently enjoined" stays open) |
| F-027 | Chartis rural margins | **Confirmed** | Chartis web page "2025 State of the State" (February 10, 2025): 46 percent negative operating margin, national median 1.0 percent, 432 vulnerable | Nothing (v16 does not use them) |
| U-3 | Rule text on the 6.0 percent threshold and the 75/75 test | **Confirmed** | 91 FR 46564 (75/75 defined); 46572 and proposed § 433.68(f)(3)(ii)(A)(3) at 46598 (6 percent cap unless the tax met 75/75 on July 4, 2025; CMS expects no state to qualify); 46581 and summary 46562 (75/75 dropped from FFY2027) | Qualifies: v16's "at most 6.0%" is CMS's proposed cap and cites 46562 rather than 46572/46598 |
| U-4 | Nursing facility / ICF exemption: statutory or proposed | **Confirmed** (statutory) | P.L. 119-21 § 71115(a)(2), new SSA § 1903(w)(4)(D)(iv), 139 Stat. 302; 42 CFR 433.56(a)(3)–(4). CMS calls it statutory (91 FR 46565, 46576). | Nothing (v16's column is right; the exemption is from the phase-down only, and the classes keep their July 4, 2025 threshold) |

No item came out **not found**. Every passage commenters attribute to CMS was located in the Federal Register.

## Why F-015 is "corrected"

The finding says CBPP's footnote argues that "two of the three adjustments lower CMS's figure". CBPP's footnote 23 (2476-0033, p. 9 of 13) says the opposite. The extra year raises CMS's estimate. The interaction and the 2026-dollar basis each lower it. So adjusting for the interaction and the dollar basis would raise CMS's figure, and only the window adjustment lowers it.

CMS's own tables bear out CBPP's conclusion:

| CMS federal figure | 2026–2035 | 2026–2034 (2035 dropped) |
|---|---:|---:|
| With interaction: SDP rule + provider tax rule | $601.0B (510.1 + 90.9) | $501.5B (less 80.6 and 18.9) |
| Without interaction: SDP rule + provider tax rule | $755.9B (510.1 + 245.8) | $630.9B (less 80.6 and 44.4) |

Sources: Table 19 (91 FR 30452), Table 14 (91 FR 46593) and Table 11 (91 FR 46591). Table 11's annual federal row sums to $245.9B against CMS's stated $245.8B, a rounding difference.

CMS states its figures in real 2026 dollars and gives no conversion factor, so the dollar-basis adjustment is direction only. CBO's $340.5B could not be read (cbo.gov returned HTTP 403). The finding's own text was not edited, because this pass may change only the verification fields. The wording fix is for the next findings revision.

## Sources reached and not reached

| Source | Result |
|---|---|
| Federal Register PDFs on govinfo: 91 FR 30400 (CMS-2449-P), 91 FR 46562 (CMS-2452-P), 91 FR 4794 (CMS-2448-F) | Read in full text. Page numbers come from the printed page headers. Tables printed as images at 91 FR 30451–30452 were read from the page images. |
| P.L. 119-21 (govinfo, PLAW-119publ21) | Read, section 71115 at 139 Stat. 301–302 |
| 42 CFR 433.56 (govinfo, CFR 2025 edition) | Read |
| Texas HHSC CHIRP preprint questions (pfd.hhs.texas.gov) | Read, 19 pages |
| Chartis 2025 State of the State (chartis.com) | Read (web page) |
| Idaho Code § 56-1404 (legislature.idaho.gov) | Read only through the web-fetch tool, which returns model-extracted text. The quoted subsection (4) was not byte-checked. Direct connection was refused. |
| regulations.gov v4 API (key supplied through an environment variable, not stored) | Read |
| www.regulations.gov web pages | HTTP 403 |
| cbo.gov (all CBO documents) | HTTP 403, both direct and through the web-fetch tool |
| courtlistener.com, congress.gov, ecfr.gov | Connection refused by the network policy |
| Idaho Department of Health and Welfare, medicaid.gov, kff.org | Connection refused by the network policy |

No secondary summary was used to verify anything. One web-search lead, that THA's 50 percent may come from an earlier CBO budget option rather than the 2025 score, is recorded in F-008's note as unread and not relied on.

## Other things the primary sources show

These were not part of the request and nothing was edited for them:

* **THA mislabels CMS's scenarios.** THA (2476-0109, p. 6 of 9) calls 20 percent the "low scenario". At 91 FR 46593, 20 percent is the high (higher-savings) scenario; v16, CE-32 and CHLA have it right.
* **CBPP misdescribes the offset base.** CBPP (2476-0033, p. 9) describes the 30 percent as a share of "reduced federal spending". CMS applies it to "these cuts", the payment reductions that follow lost tax revenue (91 FR 46591).
* **CMS-2449-P's state figure is internally inconsistent.** The text on 91 FR 30452 says $264.4 billion, while Table 20 on the same page sums to $264.7 billion. This bears on F-020, which already describes the two figures; F-020 was not re-checked or edited in this pass.
* **Ledger CE-32 is contradicted.** CE-32 says the primary scenario carries one parameter. The Federal Register gives the central scenario three: the 30 percent offset, 65 percent tax-financed and the 80 percent SDP ceiling. This is for the ledger owner.

## Departure from the conventions

`review/CONVENTIONS.md` allows one quote per source across a file. This task asked for exact wording in each verification note, so several notes quote the same Federal Register document (CMS-2452-P is quoted in F-005, F-006, F-007, F-011, F-015 and U-3). Each quote is verbatim and at most 24 words, and F-012's two fragments from one page count as one quote. All quotes except the Idaho one were matched by script against the downloaded source text. F-006's CMS sentence wraps from one column to the next around Table 12, and was checked against the page layout.
