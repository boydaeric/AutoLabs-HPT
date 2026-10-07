"""Shared loading / cleaning / clustering helpers for the comment-tagging pipeline."""
import collections
import glob
import hashlib
import html
import json
import re
import zlib
from pathlib import Path

DATA = Path("data")
SHINGLE = 5
CLUSTER_JACCARD = 0.5     # shingle Jaccard to a cluster leader => same campaign


def load_comments():
    """id -> {record fields..., text: merged raw text, text_info: extraction metadata}"""
    out = {}
    for p in sorted(glob.glob(str(DATA / "*/CMS-*.json"))):
        rec = json.loads(Path(p).read_text())
        tp = Path(p).parent / "_text" / Path(p).name
        t = json.loads(tp.read_text()) if tp.exists() else {"merged_text": "", "attachments": [], "problems": ["no extracted text file"]}
        rec["text"] = t["merged_text"]
        rec["comment_only"] = t["comment_text"] if "comment_text" in t else ""
        rec["text_info"] = t
        out[rec["id"]] = rec
    return out


def clean(text):
    """Un-escape HTML entities / tags and collapse whitespace."""
    t = html.unescape(html.unescape(text or ""))
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


def words(text):
    return re.sub(r"[^a-z0-9 ]+", " ", clean(text).lower()).split()


def shingles(w, n=SHINGLE):
    return {zlib.crc32(" ".join(w[i:i + n]).encode()) for i in range(max(1, len(w) - n + 1))}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def cluster(comments):
    """Greedy leader clustering on shingle Jaccard.

    Returns {id: (leader_id, kind, jaccard_to_leader)} where kind is
      'exact'  - normalised text identical to the leader's
      'near'   - shingle Jaccard >= CLUSTER_JACCARD (form letter / template campaign)
      'leader' - the cluster's representative (also used for singletons)
    Leader = longest document in the cluster (processed first), so a member is always
    a subset-ish variant of its leader, which avoids chaining unrelated letters.
    """
    W = {k: words(v["text"]) for k, v in comments.items()}
    S = {k: shingles(w) for k, w in W.items()}
    digest = {k: hashlib.md5(" ".join(w).encode()).hexdigest() for k, w in W.items()}
    inv = collections.defaultdict(list)
    for k in S:
        for h in S[k]:
            inv[h].append(k)
    leaders, assign = set(), {}
    for k in sorted(S, key=lambda k: (-len(S[k]), k)):
        if len(W[k]) < 8:        # near-empty text: merge only on exact match, never on shingle noise
            same = next((o for o in leaders if digest[o] == digest[k] and comments[o]["docket"] == comments[k]["docket"]), None)
            if same:
                assign[k] = (same, "exact", 1.0)
            else:
                leaders.add(k)
                assign[k] = (k, "leader", 1.0)
            continue
        cnt = collections.Counter()
        for h in S[k]:
            for o in inv[h]:
                if o in leaders and comments[o]["docket"] == comments[k]["docket"]:   # campaigns never span the two rules
                    cnt[o] += 1
        best = None
        for o, _ in cnt.most_common(10):
            j = jaccard(S[k], S[o])
            if digest[k] == digest[o]:
                best = (o, "exact", 1.0)
                break
            if j >= CLUSTER_JACCARD:
                best = (o, "near", j)
                break
        if best:
            assign[k] = best
        else:
            leaders.add(k)
            assign[k] = (k, "leader", 1.0)
    return assign
