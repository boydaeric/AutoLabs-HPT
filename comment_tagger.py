"""Rule-based tagging of regulations.gov comments on CMS-2449-P / CMS-2452-P.

Everything here is deterministic keyword/regex logic over the merged comment +
attachment text; results are reviewed and corrected through comment_tag_overrides.csv.
"""
import collections
import re

from comment_text_utils import clean

R = lambda p: re.compile(p, re.I)

STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
    "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
    "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
    "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming", "PR": "Puerto Rico", "GU": "Guam",
    "VI": "U.S. Virgin Islands", "AS": "American Samoa", "MP": "Northern Mariana Islands",
}
NAME_TO_ABBR = {v.lower(): k for k, v in STATES.items()}
# state names that are also common words / place names need context; handled in find_state_in_text
AMBIGUOUS_NAMES = {"washington", "georgia", "virginia", "indiana", "california"}  # indiana/california only as people names are rare; keep list short
CMS_ZIPS = {"21244", "20201", "21244-8016", "21244-1850", "20024"}
STATE_ALT = "|".join(sorted((re.escape(v) for v in STATES.values()), key=len, reverse=True))
ABBR_ALT = "|".join(STATES)
ZIP_ADDR = re.compile(rf"\b(?P<city>[A-Z][A-Za-z.'-]+(?:\s[A-Z][A-Za-z.'-]+){{0,2}}),?\s+(?P<st>{ABBR_ALT}|{STATE_ALT})\.?,?\s+(?P<zip>\d{{5}}(?:-\d{{4}})?)\b")


def boilerplate_stripped(text):
    t = clean(text)
    t = re.sub(r"7500 Security Boulevard[^\n]{0,60}", " ", t)
    t = re.sub(r"P\.?\s?O\.? Box 8016[^\n]{0,60}", " ", t)
    t = re.sub(r"200 Independence Ave[^\n]{0,60}", " ", t)
    return t


# ---------------------------------------------------------------- state
def find_state(rec, org, text):
    """-> (abbr or 'National' or '', source)"""
    sub = rec.get("submitter") or {}
    if org:
        low = org.lower()
        for name, ab in sorted(NAME_TO_ABBR.items(), key=lambda x: -len(x[0])):
            if re.search(rf"\b{re.escape(name)}\b", low) and not (name == "washington" and "d.c" in low):
                return ab, "org_name"
        m = re.search(rf"\b({ABBR_ALT})\b", org)
        if m and m.group(1) not in {"IN", "OR", "ME", "OK", "HI", "ID", "AS", "LA", "PA", "MA", "DE", "MD"} and len(org) < 80:
            return m.group(1), "org_name"
    body = boilerplate_stripped(text)
    head = body[:3500]
    hits = []
    for m in ZIP_ADDR.finditer(head):
        z = m.group("zip")
        if z in CMS_ZIPS or z.startswith("2124") or z.startswith("2020"):
            continue
        st = m.group("st")
        ab = st if st in STATES else NAME_TO_ABBR.get(st.lower())
        if ab:
            hits.append(ab)
    if hits:
        return collections.Counter(hits).most_common(1)[0][0], "address"
    if sub.get("state") and sub["state"] in STATES:
        return sub["state"], "api_submitter"
    # dominant state mention in the prose
    mentions = collections.Counter()
    for m in re.finditer(rf"\b({STATE_ALT})\b", body):
        n = m.group(1)
        if n.lower() in {"washington"} and re.search(r"washington,?\s+d\.?c", body[m.start():m.start() + 20], re.I):
            continue
        mentions[NAME_TO_ABBR[n.lower()]] += 1
    if mentions:
        (ab, c), = mentions.most_common(1)
        tot = sum(mentions.values())
        if c >= 3 and c / tot >= 0.6:
            return ab, "text_mentions"
    if re.search(r"\b(nationwide|national|across the (country|nation)|all 50 states|every state)\b", body[:2500], re.I) and re.search(
            r"\b(American|National|United States|U\.S\.|Association of America)\b", org or "", re.I):
        return "National", "org_name"
    return "", ""


# ---------------------------------------------------------------- organization
ORG_SUFFIX = (r"Association|Associations|District|Department|Hospital|Hospitals|Health|Healthcare|Center|Centers|Authority|"
              r"Services|Systems|System|Fire|Rescue|EMS|Ambulance|Alliance|Council|Coalition|Academy|Society|Foundation|"
              r"Institute|University|College|Clinic|Plan|Plans|Inc\.?|LLC|Corporation|Corp\.?|Company|Group|Network|Board|"
              r"County|City|Village|Town|Township|Agency|Consortium|Collaborative|Federation|Partnership|Program|Programs|Project")
ORG_RE = re.compile(rf"((?:(?:[A-Z][\w'&.\-]*|of|for|and|the|&)\s+){{0,7}}(?:{ORG_SUFFIX})(?:\s+(?:of|for)\s+(?:[A-Z][\w'&.\-]*\s*){{1,4}})?)")
BEHALF_RE = re.compile(r"(?:on behalf of|submitted by|[Ww]e (?:are|represent)|[Tt]he)\s+(?P<o>(?:the\s+)?(?:[A-Z][\w'&.\-]*\s+){1,8}?(?:" + ORG_SUFFIX + r")(?:\s+(?:of|for)\s+(?:[A-Z][\w'&.\-]*\s*){1,3})?)")


BAD_DERIVED = R(r"centers for medicare|medicare (and|&) medicaid|medicaid services|medicaid program|medicare ambulance|medicare inpatient|managed care|fee[- ]for[- ]service|honorable|\boz\b|administrator|proposed|threshold|docket|supplemental|^of\b|^the$|^public health$|^health$|^department\b|^office of|^re\b|^llc$|^inc\.?$|^fire$|^ground|^ambulance program$|u\.?s\.? department|united states department|department of health (and|&) human services$")
AGENCY_RE = re.compile(r"((?:State of |Commonwealth of )?(?:[A-Z][A-Za-z&.']+ ){0,3}(?:Department|Division|Agency|Authority|Commission|Office) (?:of|for) (?:the )?[A-Z][A-Za-z&,' ]{3,70}?)(?= \(|,|\.|\n| comments?| is | submit| has | and the|$)")
GENERIC_TAIL = R(r"^(?:\w+ ){0,1}(fire|county|city|health|services|ambulance)$")


def derive_org(org, text):
    if org and org.strip().lower() not in {"individual", "self", "none", "n/a", "na", "anonymous", "-", ".", "llc"}:
        return org.strip(), "api_organization"
    body = boilerplate_stripped(text)
    head = body[:1800]
    m = re.search(r"[Oo]n behalf of (?:the )?(?P<o>[A-Z][^.,;\n]{3,90}?)(?:,| and |\. | I | we | in | to |\n)", head)
    if m and re.search(ORG_SUFFIX, m.group("o")) and not BAD_DERIVED.search(m.group("o")):
        return re.sub(r"\s+", " ", m.group("o")).strip(), "text_on_behalf_of"
    for m in AGENCY_RE.finditer(re.sub(r"\s+", " ", head)):
        cand = m.group(1).strip()
        if not BAD_DERIVED.search(cand) and not re.search(r"^(Services|Attention)", cand):
            return cand, "text_agency"
    for ln in head.split("\n")[:12]:
        ln = ln.strip()
        if 6 < len(ln) < 80:
            m = ORG_RE.search(ln)
            if m:
                cand = re.sub(r"\s+", " ", m.group(1)).strip()
                if len(cand.split()) >= 2 and not BAD_DERIVED.search(cand) and not GENERIC_TAIL.search(cand):
                    return cand, "text_letterhead"
    return "", ""


# ---------------------------------------------------------------- commenter type
R = lambda p: re.compile(p, re.I)
STATE_AGENCY = R(r"\b(department|dept\.?|division|office|agency|commission|authority|bureau) (of|for) (health|medicaid|human services|social services|public health|community health|family|medical assistance|health care|healthcare|insurance|aging|behavioral)|health care authority|health and human services|medicaid (agency|authority|office|program office)|\bmasshealth\b|\bahcccs\b|\btenncare\b agency|state medicaid|\bdhhs\b|\bhhsc\b|state of [a-z]+|commonwealth of|governor|attorney general|state (legislature|senate|house)|legislator|senator|representative")
MCO = R(r"health ?plans?\b|managed care organization|\bmcos?\b|centene|molina|anthem|elevance|unitedhealth|optum|humana|aetna|caresource|wellcare|amerigroup|healthfirst|blue cross|blue shield|\bbcbs\b|kaiser|cigna|magellan|amerihealth|highmark|health net\\b|\bl\.?a\.? care\b|community health choice|buckeye health|peach state|sunshine health|superior health|coventry|carelon|trillium|gateway health|independent health|fidelis|emblemhealth|wellpoint|\bahip\b|insurer|insurance (company|group)")
ASSOC_PLANS = R(r"association (of|for) (community affiliated )?plans|medicaid health plans of america|\bmhpa\b|\bacap\b|america'?s health insurance plans|\bahip\b")
ASSOC = R(r"\bassociation\b|\bassociations\b|\bsociety\b|\bacademy\b|\bcollege of\b|\bfederation\b|\bcouncil\b|\balliance\b|\bconsortium\b|\bchambers?\b|\bunion\b|\blocal \d+|\bfirefighters\b|\bchiefs\b|\bcaucus\b|\bcollaborative\b|\bleague\b|\bcoalition\b|\bnetwork\b|\bpartnership\b|\bcongress\b|\bboard of (governors|directors)\b|\bguild\b")
ASSOC_STRONG = R(r"\bassociation\b|\bassociations\b|\bsociety\b|\bacademy\b|\bfederation\b|\bcollege of\b|\bchamber\b|\bunion\b|\bchiefs\b|\bfirefighters\b|\bcongress\b|\bamerican (hospital|medical|academy|college|society|nurses|health)|\bnational (association|rural|league|council)")
ADVOCACY = R(r"\b(advocacy|advocates|advocate|foundation|project|voices|action|families|justice|legal (aid|services|center)|law (center|project)|institute|center (for|on)|defend|equity|fund|campaign|rights|alliance for|coalition|citizens|community (organizing|action)|health (justice|equity|law)|kff|urban|think tank|research|policy|reform|network)\b")
HOSPITAL = R(r"hospitals?\b|medical centers?\b|health systems?\b|healthcare systems?\b|health care systems?\b|\bclinic\b|children'?s\b|\bhealth ministry|\bhealth network|\bacademic health|\buniversity health|\bhealth services? (corporation|district)|\bbehavioral (health )?hospital|\bmedical college|\bhealth\b(?! (plan|center|department|care authority))|\bhealthcare\b|\bhealth care\b|\bmedical group\b|\bumc\b")
EMS_LOCAL = R(r"fire (department|district|protection|rescue|authority|and rescue)|ambulance|\bems\b|emergency medical|rescue squad|\bparamedic|\bfire\b|\bgemt\b|first responders?|county of|city of|village of|town of|township|\bborough\b|\bdistrict\b|municipal")
BH_PROVIDER = R(r"behavioral|mental health|addiction|substance|recovery|counseling|therap|psychiat|treatment (center|program)|community mental")
FQHC = R(r"community health center|\bfqhc\b|health center|rural health clinic|primary care")
LTC = R(r"nursing (facility|home)|long[- ]term care|skilled nursing|home health|hospice|assisted living|\bhcbs\b|disabilit|developmental")
UNIVERSITY = R(r"universit|college|school of|institute of technology")
INDIV_SELF = R(r"^(i|my|as a|as an|we|i'm|i am|having|being)\b")

SUBTYPE_INDIV = [
    (R(r"(\bI am|\bI'm|\bas (a|an)|\bI work as|\bI serve as|\bI have been|\bmy (practice|patients))[^.]{0,80}pediatric"), "pediatrician"),
    (R(r"(\bI am|\bI'm|\bas (a|an)|\bI work as|\bI serve as)[^.]{0,60}(physician|doctor|\bM\.?D\.?\b|radiologist|surgeon)"), "physician"),
    (R(r"(\bI am|\bI'm|\bas (a|an)|\bI work as)[^.]{0,60}(nurse|\bAPRN\b|nurse practitioner|\bPA-C)"), "nurse/APP"),
    (R(r"(\bI am|\bI'm|\bas (a|an)|\bI work as)[^.]{0,60}(social worker|\bLCSW\b|counselor|therapist|psycholog)"), "behavioral health clinician"),
    (R(r"(\bI am|\bI'm|\bas (a|an))[^.]{0,40}(parent|mother|father|caregiver)|\bmy (son|daughter|child|kids)"), "parent/caregiver"),
    (R(r"(\bI am|\bI'm|\bas (a|an))[^.]{0,40}(patient|medicaid (recipient|beneficiary))|\bI (am|have been) on medicaid"), "patient/beneficiary"),
    (R(r"(\bI am|\bI'm|\bas (a|an))[^.]{0,40}(student|professor|researcher)"), "student/academic"),
    (R(r"(\bI am|\bI'm|\bas (a|an)|\bI serve)[^.]{0,60}(firefighter|paramedic|\bEMT\b|fire chief)"), "EMS/fire responder"),
]


HOSP_STRONG = R(r"hospitals?\b|medical centers?\b|health systems?\b|healthcare systems?\b|health care systems?\b|\bclinic\b|children'?s\b|health ministry|health network\b|academic health|health care corporation|\bmemorial\b|regional health\b|\bmedical group\b|\bumc\b|^(adventhealth|ascension|erlanger|michigan medicine|nebraska medicine|tufts medicine|ut medical|hca)\b")
HOSP_NAME_HEALTH = re.compile(r"^(?:The )?[A-Z][\w'.&-]*(?: [A-Z][\w'.&-]*){0,3} (?:Health|Healthcare|Health Care|Medicine)(?: [A-Za-z]+)?$")
NON_HOSP = R(r"institute|initiative|policy|law |justice|defend|public health|authority|council|coalition|alliance|collaborative|consortium|partnership|association|society|academy|foundation|project|center (for|on)|legal|advocate|union|seiu|league|forum|insurance|leadership")
ASSOC_WEAK = R(r"\bcouncil\b|\balliance\b|\bconsortium\b|\bcoalition\b|\bcollaborative\b|\bnetwork\b|\bpartnerships?\b|\bleague\b|\bcaucus\b|\bforum\b|\bcongress\b|\bboard of\b")
PROVIDERISH = R(r"hospital|health ?care|health system|behavioral|providers?|ambulance|ems\b|emergency|physicians?|nurs|medical|pediatric|plans?\b|long[- ]term|home care|dental|pharmac|community mental|rural health|safety[- ]net|mental health|addiction|human service|disabilit(y|ies) (service|provider)|ancor|community options")
ASSOC_STRONG2 = R(r"\bassociation\b|\bassociations\b|\bsociety\b|\bacademy\b|\bfederation\b|\bcollege of\b|\bchamber\b|\bchiefs\b|\bcongress\b|\bamerican (hospital|medical|academy|college|society|nurses|health)|\bnational (association|rural|league)|\bleadingage\b|\bamga\b|\baamc\b|\bahip\b|\bsaving hospitals")
UNION = R(r"\b(employees|workers|firefighters|fire fighters|nurses|professional firefighters) (international )?union\b|\bseiu\b|\bafscme\b|\bunion\b(?! (county|city|township|fire|ems|emergency|hospital|health|medical|school|rural))|\blocal \d+|\bfirefighters\b|international association of fire")
PATIENT_ADV = R(r"alzheimer|muscular dystrophy|nami\b|national alliance on mental illness|\bthe arc\b|easterseals|blood cancer|taxpayers|americans for prosperity|arnold ventures|partnership (for|to protect)|inseparable|kids forward|indigenous women|families usa|defend ")


def classify_type(rec, org, org_src, text):
    """-> (type, subtype, confidence)"""
    body = boilerplate_stripped(text)
    head = body[:900]
    o = org or ""
    low = o.lower()
    if not o:
        subt = next((s for p, s in SUBTYPE_INDIV if p.search(head + " " + (rec.get("comment") or ""))), "")
        tail = body[-700:]
        if len(body.split()) > 250 and re.search(r"sincerely|respectfully submitted|on behalf of", tail + head, re.I) and re.search(
                r"executive director|president|ceo\b|chief|director|administrator|commissioner|chair\b|manager|vice president", tail, re.I) and not re.search(r"\b(md|m\.d\.|do|rn|np|lcsw|phd)\b", tail[-250:], re.I):
            return "other", "unnamed organization (signed by an officer)", "low"
        return "individual", subt, "medium" if subt or len(body.split()) < 400 else "low"
    if ASSOC_PLANS.search(o) or re.search(r"health plans?( association| of)|alliance of community health plans|local health plans|council of health plans|blue cross blue shield association", low):
        return "association", "health plan association", "high"
    if PATIENT_ADV.search(o):
        return "advocacy group", "", "medium"
    if STATE_AGENCY.search(o) and not ASSOC_STRONG2.search(o) and not UNION.search(o) and not re.search(r"\b(city|county|village|town|fire|ambulance|school|university|national conference|insurance connector)\b", low) \
            or re.search(r"health authority|medicaid program$|department of (insurance|finance)|insurance connector|connect for health|legislative council|legislat(ure|ive)|state of ", low) and not ASSOC_STRONG2.search(o):
        return "state agency", "", "medium"
    if ASSOC_STRONG2.search(o) or UNION.search(o):
        if UNION.search(o) and not re.search(r"association", low):
            return "association", "labor union", "medium"
        subt = ("hospital association" if re.search(r"hospital|health ?care association|health system|healthcare association", low) else
                "EMS/fire association" if re.search(r"ambulance|ems\b|emergency medical|fire|rescue|paramedic", low) else
                "physician/professional society" if re.search(r"physician|pediatric|medical|nurs|academy|college|society|dental|psych|pharmac|surgeon|actuar", low) else "trade/professional")
        return "association", subt, "medium"
    if ASSOC_WEAK.search(o):
        if re.search(r"hospital", low) or PROVIDERISH.search(o):
            subt = "hospital association" if re.search(r"hospital|health system|safety[- ]net", low) else "provider coalition / council"
            if not re.search(r"cambridge health alliance", low):
                return "association", subt, "low"
        elif not HOSP_STRONG.search(o):
            return "advocacy group", "", "low"
    if MCO.search(o) and not re.search(r"\bcvs\b", low):
        return "MCO", "", "medium"
    if HOSP_STRONG.search(o) and not NON_HOSP.search(o) and not re.search(r"\b(ambulance|fire|ems|rescue)\b", low):
        return "hospital/health system", "behavioral hospital" if BH_PROVIDER.search(low) else "", "medium"
    if re.search(r"\b(fire|ambulance|ems|rescue|emergency medical|paramedic)\b", low):
        return "other", "ambulance/EMS provider" if re.search(r"ambulance|ems\b|rescue squad|paramedic|emergency medical", low) and not re.search(r"fire|county|city|district|village|town", low) else "local government / fire / EMS", "medium"
    if re.search(r"\b(city|county|village|town|township|borough|district|municipal|parish)\b", low):
        return "other", "local government / fire / EMS", "medium"
    if HOSP_NAME_HEALTH.match(o.strip()) and not NON_HOSP.search(o):
        return "hospital/health system", "", "low"
    if ADVOCACY.search(o) or NON_HOSP.search(o):
        return "advocacy group", "", "low"
    if FQHC.search(low):
        return "other", "community health center / clinic", "medium"
    if BH_PROVIDER.search(low):
        return "other", "behavioral health provider", "medium"
    if LTC.search(low):
        return "other", "long-term care / IDD provider", "medium"
    if UNIVERSITY.search(low):
        return "other", "academic institution", "medium"
    if re.search(r"\b(inc\.?|llc|corp|company|consult|group|solutions|partners|intelligence|enterprises|technolog|pharma|advisory)\b", low):
        return "other", "company / consultancy", "low"
    return "other", "", "low"


# ---------------------------------------------------------------- position
OPP_STRONG = R(r"\b(oppose[sd]?|opposing|opposition|objects? to|dissent)\b|\b(withdraw|rescind|reject|abandon|scrap)\b[^.]{0,60}\b(rule|proposal|proposed|provision|limit|cap|policy|changes?)\b|(rule|proposal|provision|limit|cap|changes?)\b[^.]{0,40}\b(should|must|need to|ought to) (not )?be (withdrawn|rescinded|rejected|abandoned)|(do not|don'?t|should not|must not|cannot|urge[^.]{0,30}not (to )?)\s*(be )?(finaliz|adopt|implement|move forward|proceed|pass)|cannot support|against (this|the) (proposed )?(rule|proposal|change|cut)|vote no|\b(urge|ask|implore|request|hope|encourage)s?\b[^.]{0,60}\b(reconsider|rethink|reverse)\b|\b(do not|don't|please do not|please don't) (cut|reduce|lower|pass|do this|take)\b|(leave|keep) (medicaid|the|our|payments|these)[^.]{0,30}(alone|as is|the same|intact)")
OPP_WEAK = R(r"reconsider|rethink|deeply (concerned|troubled)|devastat|catastroph|harmful|dangerous|detrimental|short-?sighted|egregious|unacceptable|will (hurt|harm|destroy|cost lives|crush|cripple)|please (stop|don'?t|do not|leave)|jeopardiz|threaten|disastrous|cuts? (to|in) medicaid|\bcuts?\b|lowering|underpaid|going down|below cost|insolven|clos(e|ing|ure)s?\b|will (suffer|lose|lead to)")
SUP_STRONG = R(r"\b(we|i)\s+(also\s+|strongly\s+|greatly\s+|fully\s+|generally\s+|broadly\s+|wholeheartedly\s+|cautiously\s+)*(support|agree with|applaud|commend|welcome|endorse|favor|second)\s+(the\s+|this\s+|these\s+|that\s+|cms'?s?\s+|its\s+|a\s+)?(proposal|proposed|proposals|decision|provision|provisions|rule|approach|changes?|limit|cap|policy|clarification|requirement|move|step|recognition|reform|reforms|lower|implementation|limits|caps|plan|efforts? to (limit|cap|reduce|align|curb))|\b(in|express(ing)?) (strong |full )?support (of|for) (the|this|cms|these) (proposed )?(rule|proposal|provision|change|policy)|\bsupport the (proposed|proposal)\b")
SUP_GOAL = R(r"\b(we|i)\s+(also\s+|strongly\s+|fully\s+|generally\s+)*(support|share|appreciate|agree with|recognize|understand|commend)\b[^.]{0,60}\b(goals?|intent|objectives?|purpose|integrity|transparency|accountability|efforts?|aim|concern|need)\b|\bwhile (we|i) (support|appreciate|understand|agree)")
REQ = R(r"\b(urge|request|recommend|ask|encourage|suggest|propose|call on|implore)s?\b[^.]{0,90}\b(modif|revis|amend|clarif|exempt|exclu|extend|delay|adopt|allow|permit|provid|consider|add|retain|maintain|establish|includ|preserv|continue|carve|align|phase|postpone|apply|permit)|\bshould be (revised|modified|clarified|amended|extended|exempt)|\bcarve[- ]out\b|\bexempt(ion|ed)?\b|\bplease (consider|clarify|allow|exempt|include|extend)")


def classify_position(text, n_words):
    body = boilerplate_stripped(text)
    sents = re.split(r"(?<=[.!?])\s+", body)
    key = [s for s in sents if re.search(r"urge|request|recommend|oppose|support|ask|encourage|withdraw|concern|agree|welcome|appreciate|applaud|commend", s, re.I)]
    focus = " ".join(sents[:15] + sents[-12:] + key[:80])
    so, wo = len(OPP_STRONG.findall(focus)), len(OPP_WEAK.findall(focus))
    ss, sg, rq = len(SUP_STRONG.findall(focus)), len(SUP_GOAL.findall(focus)), len(REQ.findall(focus))
    if n_words < 6:
        return ("unclear / off-topic", "low")
    if so >= 1 and ss >= 1:
        return ("mixed", "low")
    if so >= 1:
        return ("oppose", "high" if so >= 3 else "medium")
    if ss >= 1:
        if wo >= 3 or (rq >= 3 and wo >= 1):
            return ("mixed", "low")
        if rq >= 3:
            return ("request for changes", "low")
        return ("support", "medium")
    if wo >= 1 and rq == 0:
        return ("oppose", "low")
    if rq >= 1 or sg >= 1:
        return ("request for changes", "low")
    if wo >= 1:
        return ("oppose", "low")
    return ("unclear / off-topic", "low")


# ---------------------------------------------------------------- provisions
PROV_1916 = [
    ("SDP payment limit (Medicare/State-plan rate cap, §438.6(a),(c)(2)(ii)(I),(c)(8))",
     R(r"100 percent of (the )?(total )?(published )?medicare|110 percent|payment limit|medicare (payment )?rates?|state plan rates?|average commercial rate|\bacr\b|438\.6\(c\)\(2\)\(ii\)\(I\)|438\.6\(a\)|rate cap|payment cap|medicare equivalent|wage index|fee schedule")),
    ("Grandfathered SDPs & 10%/yr phase-down (§438.6(c)(8))",
     R(r"grandfather|phase[- ]?down|10 percent (of the|per year|each year)|transition period|438\.6\(c\)\(8\)|glide path|sunset")),
    ("Permissible SDP types / uniform increases / VBP (§438.6(c)(1)(iii))",
     R(r"uniform (dollar |percentage )?increase|value[- ]based|minimum fee schedule|permissible (sdp|type)|438\.6\(c\)\(1\)|types of (state directed|sdp)|pay[- ]for[- ]performance|incentive payment")),
    ("SDP preprint/approval & other SDP requirements (§438.6(c)(2))",
     R(r"preprint|prior approval|written prior approval|438\.6\(c\)\(2\)\((iii|vii|viii)\)|quality (goals|strategy|evaluation)|evaluation plan|contract (amendment|requirements)|rating period")),
    ("Applicability / effective dates (§438.6(c)(10))",
     R(r"applicability date|effective date|438\.6\(c\)\(10\)|implementation (date|timeline)|effective (january|july|october)")),
    ("FFS targeted Medicaid practitioner payment limit (§447.381)",
     R(r"447\.381|targeted medicaid (practitioner )?payment|practitioner (services|payments)|fee[- ]for[- ]service (supplemental|targeted)|ffs (supplemental|targeted)|supplemental payment|physician (payment|supplemental)")),
    ("FFS limit exceptions / scope (§447.381(b),(d))",
     R(r"447\.381\((b|d)\)|(exception|exempt)[^.]{0,120}(447\.381|fee[- ]for[- ]service|\bffs\b|targeted)|(447\.381|fee[- ]for[- ]service|\bffs\b|targeted)[^.]{0,120}(exception|exempt)|geographic region|uniform (payment|rate)s? (across|within|for all)")),
    ("FFS transition period (§447.381(e))",
     R(r"447\.381\(e\)|transition period|phase[- ]in|glide path")),
    ("GEMT / ambulance (ground emergency medical transport) payments",
     R(r"\bgemt\b|ground emergency medical|ambulance|emergency medical (service|transport)|\bems\b|fire[- ]based|paramedic|medicare ambulance fee schedule")),
    ("Access to care / network adequacy impact",
     R(r"access to (care|services|health)|network adequacy|provider (participation|shortage|exodus|closures?)|rural (hospital|access|communit)|clos(e|ing|ure)s? of|workforce|waiting times?|travel")),
    ("Financing: IGTs / provider taxes / non-federal share",
     R(r"intergovernmental transfer|\bigts?\b|provider tax|non-federal share|nonfederal share|health care-related tax|financing")),
    ("Safety-net / children's / rural hospital impact",
     R(r"safety[- ]net|children'?s hospital|pediatric|rural hospital|critical access|academic medical|teaching hospital|disproportionate share|\bdsh\b")),
    ("Behavioral health / SUD / IDD providers",
     R(r"behavioral health|mental health|substance use|addiction|\bsud\b|intellectual and developmental|\bidd\b|\bhcbs\b|home and community")),
    ("Medicare benchmark methodology (service-level vs aggregate, wage index, data)",
     R(r"in the aggregate|aggregate (basis|calculation|limit)|service[- ]level|wage index|\bawi\b|medicare benchmark|actuarial|actuarially sound|upper payment limit|\bupl\b|cost of care|below cost|cost[- ]to[- ]charge")),
    ("State flexibility / federalism / statutory authority",
     R(r"state flexibility|federalism|statutory authority|exceed(s|ing)? (the )?statut|1902\(a\)\(30\)|\bhr ?1\b|working families tax cut|one big beautiful|congress(ional)? intent|beyond (the )?(statut|scope)")),
    ("Regulatory impact / burden / data analysis",
     R(r"regulatory impact|burden estimate|paperwork reduction|economic analysis|fiscal impact|cost estimate|\bria\b|projected (loss|reduction|spending)")),
]
PROV_2476 = [
    ("General definitions: Expansion State, net patient revenue, etc. (§433.52)",
     R(r"433\.52|expansion state|non-expansion|definition of|net patient revenue|\bnpr\b|applicable percent")),
    ("New permissible class: health insurer / MCO services (§433.56(a)(19))",
     R(r"433\.56|permissible class|managed care organization tax|mco tax|health insur(er|ance) (tax|services)|class of health care|insurer tax")),
    ("Indirect hold harmless threshold: calculation & baseline (July 4, 2025)",
     R(r"threshold|july 4,? 2025|grandfather|baseline|6 percent|6%|hold harmless|indirect hold|433\.68|calculation")),
    ("Expansion-State threshold phase-down (from Oct. 1, 2027)",
     R(r"phase[- ]?down|expansion state|october 1,? 2027|3\.5|0\.5 percent|reduce(d|s)? (by|the)|annual reduction|glide")),
    ("Sunset of second prong of indirect hold harmless test",
     R(r"second prong|sunset|433\.68\(f\)|prong")),
    ("Reporting requirements (§433.74)",
     R(r"433\.74|reporting requirement|one-time report|ongoing report|annual report|data (submission|reporting)|submit (data|information|documentation)|burden")),
    ("Limitation on FFP / penalties (§433.70)",
     R(r"433\.70|\bffp\b|federal financial participation|penalt|disallow|recoup|deferral")),
    ("Effective dates / transition timing",
     R(r"effective (date|october|january)|october 1,? 2026|transition (period|year)|implementation (date|timeline)|delay|extend (the )?(effective|transition)|one-year|two-year|more time")),
    ("Impact on state budgets / Medicaid financing & provider payments",
     R(r"state budget|medicaid (financing|funding|spending)|non-federal share|provider tax|hospital (tax|assessment)|supplemental payment|directed payment|shortfall|loss of|revenue")),
    ("Access to care / provider and beneficiary impact",
     R(r"access to (care|services|health)|beneficiar|provider (closures?|participation)|rural|safety[- ]net|workforce|wait")),
    ("Nursing facility / ICF / long-term care taxes",
     R(r"nursing (facility|home)|long[- ]term care|icf|intermediate care|skilled nursing|home health|hospice")),
    ("Behavioral health / SUD / IDD providers",
     R(r"behavioral health|mental health|substance use|addiction|intellectual and developmental|\bidd\b|\bhcbs\b|home and community")),
    ("State flexibility / statutory authority / WFTC legislation",
     R(r"state flexibility|federalism|statutory authority|exceed(s|ing)? (the )?statut|working families tax cut|one big beautiful|\bwftc\b|congress(ional)? intent|beyond (the )?(statut|scope)")),
]


def classify_provisions(text, docket):
    body = boilerplate_stripped(text)
    table = PROV_1916 if docket.endswith("1916") else PROV_2476
    hits = []
    for label, pat in table:
        n = len(pat.findall(body))
        # a provision counts when it is discussed more than in passing
        need = 2 if len(body.split()) > 250 else 1
        if label.startswith(("GEMT",)):
            need = 2
        if n >= need:
            hits.append((n, label))
    hits.sort(reverse=True)
    return [h[1] for h in hits[:6]]


# ---------------------------------------------------------------- summary
ASK = R(r"\b(urge|request|recommend|oppose|opposition|support|ask|encourage|implore|call on|concern|withdraw|exempt|should|must|would (harm|reduce|eliminate|cut|jeopardize|threaten))\b")
TOPIC = R(r"\b(sdp|state directed|gemt|ambulance|medicare|hold harmless|threshold|tax|supplemental|payment|rate|grandfather|medicaid)\b")
NOISE = R(r"^(dear|re:|attention|submitted|via |thank you|we appreciate|on behalf|sincerely|respectfully|cc:|page \d|www\.|http|phone|fax|p\.o\.|date:|subject:|administrator|comment on|medicaid program|centers for medicare|department of health)|\d{3}[-.) ]\d{3}[-. ]\d{4}|@|\bdear (dr|administrator|mr|ms)\b|administrator centers|docket (no|id)|file code")


def best_sentence(text, maxlen=260):
    body = boilerplate_stripped(text)
    body = re.sub(r"\s+", " ", body)
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z“\"(])", body)
    best, best_score = "", 0
    for i, s in enumerate(sents[:120]):
        s = s.strip()
        if not 40 <= len(s) <= 420 or NOISE.search(s):
            continue
        sc = 2 * len(ASK.findall(s)) + len(TOPIC.findall(s)) - (0.01 * i)
        if re.search(r"\b(i|we) (strongly |respectfully )?(oppose|urge|request|support|recommend)", s, re.I):
            sc += 3
        if sc > best_score:
            best, best_score = s, sc
    if len(best) > maxlen:
        cut = best[:maxlen].rsplit(" ", 1)[0]
        best = cut.rstrip(",;:") + "…"
    return best


RULE_A_HITS = R(r"hold harmless|2452|433\.68|433\.56|433\.74|health care[- ]related tax|provider tax|indirect hold|av93")
RULE_B_HITS = R(r"state[- ]directed payment|\bsdps?\b|2449|438\.6|447\.381|\bgemt\b|av69|targeted medicaid practitioner|ground emergency")


def content_docket(text, filed_docket):
    """Docket whose rule the text actually discusses (guards against comments filed in the wrong docket)."""
    body = boilerplate_stripped(text)
    a, b = len(RULE_A_HITS.findall(body)), len(RULE_B_HITS.findall(body))
    if filed_docket.endswith("2476") and b >= 5 and b >= 3 * max(a, 1):
        return "CMS-2026-1916"
    if filed_docket.endswith("1916") and a >= 5 and a >= 3 * max(b, 1):
        return "CMS-2026-2476"
    return filed_docket
