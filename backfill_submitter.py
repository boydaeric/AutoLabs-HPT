#!/usr/bin/env python3
"""Add the submitter-metadata fields the first collection pass skipped (category,
state, city, country, receive date, tracking number) to each data/<docket>/<id>.json.
Resumable: records that already have a "submitter" key are skipped. Needs
REGULATIONS_API_KEY in the environment."""
import json
import os
import sys
from pathlib import Path

from collect_comments import API, Client, HttpError, log, write_json

FIELDS = {
    "category": "category", "state": "stateProvinceRegion", "city": "city",
    "country": "country", "receive_date": "receiveDate",
    "tracking_number": "trackingNbr", "subtype": "subtype", "page_count": "pageCount",
}


def main():
    key = os.environ.get("REGULATIONS_API_KEY") or sys.exit("Set REGULATIONS_API_KEY.")
    c = Client(key)
    paths = [p for p in sorted(Path("data").glob("*/CMS-*.json"))]
    todo = [p for p in paths if "submitter" not in json.loads(p.read_text())]
    log(f"{len(todo)} of {len(paths)} records need submitter fields")
    for n, p in enumerate(todo, 1):
        rec = json.loads(p.read_text())
        try:
            a = c.get_json(f"{API}/comments/{rec['id']}")["data"]["attributes"]
        except HttpError as e:
            log(f"  {rec['id']}: {e}")
            continue
        rec["submitter"] = {k: a.get(v) for k, v in FIELDS.items()}
        write_json(p, rec)
        if n % 100 == 0:
            log(f"  {n}/{len(todo)}")


if __name__ == "__main__":
    main()
