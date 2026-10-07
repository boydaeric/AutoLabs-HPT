#!/usr/bin/env python3
"""One-off helper that (re)writes the commenter-identity rows of comment_tag_overrides.csv.
Each entry was set by reading the comment letter: id -> (org, type, subtype, state)."""
import csv
from pathlib import Path

H, A, S, ADV, O, I = "hospital/health system", "association", "state agency", "advocacy group", "other", "individual"
EMS, LOC, BH = "ambulance/EMS provider", "local government / fire / EMS", "behavioral health provider"
ID = {
    # unnamed or mis-identified letters
    "1916-0002": ("BestCare Treatment Services", O, BH, "OR"), "1916-0096": ("University of Hawaiʻi Rural Health Research and Policy Center", O, "academic institution", "HI"),
    "1916-0109": ("Truckee Meadows Fire Protection District", O, LOC, "NV"), "1916-0230": ("South Elgin & Countryside Fire Protection District", O, LOC, "IL"),
    "1916-0249": ("First 5 LA", O, "county children's commission", "CA"), "1916-0295": ("Lemont Fire Protection District", O, LOC, "IL"),
    "1916-0328": ("Missouri Emergency Medical Services Agent Corporation (MoEMSAC)", A, "EMS/fire association", "MO"),
    "1916-0349": ("Hawaii Department of Human Services, Med-QUEST Division", S, "", "HI"),
    "1916-0446": ("Crested Butte Fire Protection District", O, LOC, "CO"), "1916-0525": ("Texas Association of Voluntary Hospitals", A, "hospital association", "TX"),
    "1916-0571": ("Prospect Heights Fire Protection District", O, LOC, "IL"), "1916-0596": ("Cordell Memorial Hospital", H, "", "OK"),
    "1916-0617": ("Memorial Regional Health", H, "", "CO"), "1916-0733": ("Texas Health Care Association (THCA)", A, "long-term care association", "TX"),
    "1916-0736": ("SBH, LLC dba Creekside Behavioral Health", H, "behavioral hospital", "TN"), "1916-0760": ("The MetroHealth System", H, "", "OH"),
    "1916-0923": ("South Carolina Department of Health & Human Services", S, "", "SC"), "1916-0950": ("Arizona Health Care Cost Containment System (AHCCCS)", S, "", "AZ"),
    "2476-0201": ("Arizona Health Care Cost Containment System (AHCCCS)", S, "", "AZ"), "2476-0018": ("Oklahoma Insurance Department", S, "", "OK"),
    "2476-0151": ("Maine Department of Health and Human Services", S, "", "ME"), "2476-0177": ("HealthSource RI", S, "state-based marketplace", "RI"),
    "2476-0186": ("New Mexico Health Care Authority", S, "", "NM"), "2476-0198": ("California Department of Health Care Services", S, "", "CA"),
    "2476-0202": ("Washington State agency (Department of Health)", S, "", "WA"), "2476-0132": ("Access Health CT", S, "state-based marketplace", "CT"),
    "2476-0084": ("Maryland Department of Health, Department of Insurance, HSCRC and Health Benefit Exchange", S, "", "MD"),
    "2476-0124": ("Pennsylvania Insurance Department", S, "", "PA"), "2476-0183": ("Indiana Department of Insurance", S, "", "IN"),
    "2476-0126": ("Pennsylvania Department of Human Services", S, "", "PA"), "2476-0156": ("State of Colorado (Office of the Governor)", S, "", "CO"), "2476-0162": ("Children's Wisconsin", H, "", "WI"),
    "1916-0954": ("Parkland Health", H, "", "TX"), "1916-0378": ("Mosaic", O, "long-term care / IDD provider", ""), "1916-0490": ("CAYA Collaborative Care, Inc.", O, "long-term care / IDD provider", "KY"),
    "1916-0478": ("Minnesota Department of Human Services", S, "", "MN"), "2476-0096": ("Oregon Department of Consumer and Business Services", S, "", "OR"),
    "1916-0774": ("Delaware Division of Medicaid and Medical Assistance", S, "", "DE"), "1916-0209": ("Ohio Department of Medicaid", S, "", "OH"),
    "2476-0210": ("National Conference of State Legislatures", A, "state government association", "National"),
    # individual-labelled rows that are really organizations / officials (found by reading the opening text)
    "1916-0006": ("City of Consolidated Municipality (Nevada) – ambulance program", O, LOC, "NV"), "1916-0082": ("Western Fire Chiefs Association", A, "EMS/fire association", ""),
    "1916-0112": ("Jefferson County Fire & EMS", O, LOC, "OR"), "1916-0114": ("Tipton Ambulance Service", O, EMS, "IA"),
    "1916-0122": ("Illinois Academy of Family Physicians", A, "physician/professional society", "IL"), "1916-0178": ("Pontiac Fire Department", O, LOC, "IL"),
    "1916-0216": ("Aging Resources of Central Iowa (Area Agency on Aging)", O, "area agency on aging", "IA"), "1916-0217": ("", O, EMS, ""),
    "1916-0287": ("", H, "critical access hospital", "OK"), "1916-0548": ("", H, "critical access hospital", "OK"),
    "1916-0450": ("Kentucky Access to Care Coalition", ADV, "", "KY"), "1916-0457": ("Kentucky Life Science Council", A, "trade/professional", "KY"),
    "1916-0459": ("", O, LOC, ""), "1916-0521": ("Carilion Giles and Tazewell Community Hospitals", H, "", "VA"), "1916-0542": ("", O, LOC, ""),
    "1916-0594": ("", O, EMS, "OK"), "1916-0597": ("", O, EMS, "OK"), "1916-0659": ("Manhattan Institute (mental health policy team)", ADV, "think tank", ""),
    "1916-0687": ("", A, "EMS/fire association", "IL"), "1916-0695": ("", O, EMS, "ID"), "1916-0698": ("", O, LOC, ""),
    "1916-0813": ("Medicaid in Schools Coalition", ADV, "", "National"), "1916-0831": ("Yamhill County Board of Commissioners", O, LOC, "OR"),
    "1916-0890": ("Commonwealth of Virginia", S, "", "VA"), "2476-0027": ("National Association of Insurance Commissioners", A, "state government association", "National"),
    "2476-0063": ("Treatment Alternatives for Stronger Communities (TASC)", O, "nonprofit service provider", ""),
    "1916-0309": ("Ross County (fiscal officer / assessor)", O, LOC, "OH"),
    # sitting state legislators filing in their official capacity
    "1916-0204": ("", S, "state legislator", "MS"), "1916-0259": ("North Carolina House of Representatives (District 67)", S, "state legislator", "NC"),
    "1916-0308": ("Ohio House of Representatives", S, "state legislator", "OH"), "1916-0379": ("North Carolina House of Representatives", S, "state legislator", "NC"),
    "1916-0489": ("Louisiana Senate Health and Welfare Committee", S, "state legislator", "LA"), "1916-0499": ("Mississippi House of Representatives", S, "state legislator", "MS"),
    "1916-0706": ("Oregon Legislative Assembly (Rep. Dacia Grayber)", S, "state legislator", "OR"), "1916-0960": ("Texas House of Representatives", S, "state legislator", "TX"),
    # former legislators writing as individuals
    "1916-0294": ("", I, "former state legislator", "WV"), "1916-0307": ("", I, "former state legislator", "FL"),
    "1916-0480": ("", I, "former state legislator", "NC"), "1916-0919": ("", I, "former state legislator", "TX"),
    "1916-0835": ("New Mexico Health Care Authority", S, "", "NM"), "1916-0758": ("Pennsylvania Department of Human Services", S, "", "PA"),
    "1916-0387": ("North Carolina Department of Health and Human Services", S, "", "NC"), "1916-0287": ("Okeene Municipal Hospital", H, "critical access hospital", "OK"),
    # org-type corrections
    "1916-0493": ("", A, "provider association", ""), "1916-0671": ("", H, "", ""), "1916-0789": ("", H, "", ""),
    "1916-0473": ("", O, "long-term care / IDD provider", ""), "1916-0834": ("", O, "academic institution", ""),
    "1916-0154": ("", H, "", ""), "1916-0539": ("", A, "home care association", "National"), "1916-0464": ("", A, "trade/professional", "National"),
    "1916-0819": ("", H, "", ""), "1916-0862": ("Texas Council of Community Centers", A, "behavioral health association", "TX"),
    "1916-0849": ("", O, "tribal health organization", ""), "1916-0377": ("", H, "", ""), "1916-0463": ("", H, "", ""), "1916-0766": ("", H, "", ""),
    "1916-0663": ("", H, "", ""), "1916-0882": ("", H, "", ""), "1916-0343": ("", H, "", ""), "1916-0877": ("", H, "", ""), "1916-0400": ("Covenant Health", H, "", ""),
    "1916-0920": ("", H, "", ""), "1916-0388": ("", H, "", ""), "1916-0601": ("", H, "", ""), "1916-0545": ("", H, "", ""),
    "1916-0867": ("", H, "", ""), "1916-0746": ("", H, "", ""), "2476-0135": ("", H, "", ""), "1916-0468": ("", H, "academic medical center", ""),
    "1916-0346": ("Children's Hospital Los Angeles Medical Group (CHLAMG)", H, "", "CA"), "1916-0487": ("", O, "community health center / clinic", ""),
    "2476-0153": ("", "MCO", "Medicaid Regional Accountable Entity", "CO"), "1916-0332": ("", O, EMS, ""), "1916-0757": ("", O, "clinic / care provider", ""),
    "1916-0925": ("", A, "physician group association", ""), "1916-0937": ("", "off-topic", "credentialing body", "National"), "1916-0436": ("American Nurses Association – Massachusetts", A, "physician/professional society", "MA"),
    "1916-0854": ("American Academy of Pediatrics – Pennsylvania Chapter", A, "physician/professional society", "PA"),
    "1916-0305": ("", O, "physician practices", ""), "1916-0852": ("", O, "physician practice / company", ""),
    "1916-0787": ("", O, "law firm", ""), "1916-0396": ("", O, "law firm", ""), "1916-0363": ("", O, "credentialing body", ""),
    "1916-0298": ("", O, EMS, ""), "1916-0549": ("", O, EMS, ""), "1916-0856": ("", O, EMS, ""), "1916-0858": ("", O, EMS, ""),
    "1916-0313": ("", O, EMS, ""), "1916-0150": ("", O, EMS, ""), "1916-0656": ("", H, "behavioral hospital", ""),
    "1916-0807": ("", O, BH, ""), "1916-0421": ("", O, BH, ""), "1916-0853": ("", O, BH, ""), "2476-0065": ("", O, "human services provider", ""),
    "1916-0860": ("", O, "independent living center", ""), "1916-0945": ("", O, "community health center / clinic", ""),
    "1916-0392": ("", O, "company (pharmacy / insurer)", ""), "1916-0389": ("", O, "company / consultancy", ""), "1916-0788": ("", O, "company / consultancy", ""),
    "1916-0873": ("", O, BH, ""), "1916-0405": ("", O, BH, ""), "1916-0939": ("", O, "long-term care / IDD provider", ""), "1916-0782": ("", O, "pediatric care provider", ""),
    "1916-0838": ("", A, "labor union", ""), "1916-0848": ("", ADV, "", ""), "1916-0331": ("", A, "behavioral health association", ""), "1916-0254": ("", A, "behavioral health association", ""),
    "1916-0952": ("", O, BH, ""), "1916-0500": ("", O, BH, ""), "1916-0592": ("", A, "provider coalition / council", ""), "2476-0056": ("", A, "provider coalition / council", ""),
    "1916-0034": ("", ADV, "", ""), "1916-0386": ("", ADV, "", ""),
}
# comments whose own text identifies the author organization more precisely
ID_CAYA_DUP = {}
rows = [("cluster:" if False else k, "commenter_type", v[1], "manual: author identified from letter") for k, v in ID.items()]
out = []
for k, (org, typ, sub, st) in ID.items():
    cid = f"CMS-2026-{k}"
    out.append((cid, "commenter_type", typ, "identity reviewed"))
    out.append((cid, "commenter_subtype", sub, "identity reviewed"))
    if org:
        out.append((cid, "commenter_org", org, "identity reviewed"))
    if st:
        out.append((cid, "state", st, "identity reviewed"))
p = Path("comment_tag_overrides.csv")
existing = []
if p.exists():
    existing = [r for r in csv.reader(p.open(newline="")) if r and r[0] != "target" and r[3] != "identity reviewed"]
with p.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["target", "field", "value", "note"])
    w.writerows(existing)
    w.writerows(out)
print(len(out), "identity override rows;", len(existing), "other rows kept")
