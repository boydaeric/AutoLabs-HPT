"""Shared HTTP helpers for the TiC scripts.

transparency-in-coverage.bluecrossma.com serves an incomplete certificate
chain (leaf only, no intermediate). For that host only, requests verify
against a project-local bundle = certifi's roots + the DigiCert
intermediate in certs/ (SHA-256 fingerprint checked against DigiCert's
published value). Verification stays on for every host.
"""
import hashlib
import os
import re
import ssl
from urllib.parse import urlparse

import certifi
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

HERE = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = os.path.join(HERE, "certs")
BCBSMA_HOST = "transparency-in-coverage.bluecrossma.com"
INTERMEDIATE_PEM = os.path.join(CERT_DIR, "DigiCertGlobalG2TLSRSASHA2562020CA1-1.pem")
# Published by DigiCert (digicert.com/kb/digicert-root-certificates.htm) for
# "DigiCert Global G2 TLS RSA SHA256 2020 CA1", issuer DigiCert Global Root G2.
INTERMEDIATE_SHA256 = ("C8:02:5F:9F:C6:5F:DF:C9:5B:3C:A8:CC:78:67:B9:A5:"
                       "87:B5:27:79:73:95:79:17:46:3F:C8:13:D0:B6:25:A9")
BCBSMA_BUNDLE = os.path.join(CERT_DIR, "bluecrossma_ca_bundle.pem")


def _pem_sha256(path):
    pem = open(path).read()
    der = ssl.PEM_cert_to_DER_cert(re.search(
        r"-----BEGIN CERTIFICATE-----.+?-----END CERTIFICATE-----", pem, re.S).group(0))
    h = hashlib.sha256(der).hexdigest().upper()
    return ":".join(h[i:i + 2] for i in range(0, len(h), 2))


def bcbsma_bundle():
    """Return the path of the Blue Cross-only CA bundle, building it from
    certifi + the pinned intermediate if needed."""
    fp = _pem_sha256(INTERMEDIATE_PEM)
    if fp != INTERMEDIATE_SHA256:
        raise RuntimeError(f"intermediate fingerprint mismatch: {fp}")
    if not os.path.exists(BCBSMA_BUNDLE):
        with open(BCBSMA_BUNDLE, "w") as out:
            out.write(open(certifi.where()).read())
            out.write("\n" + open(INTERMEDIATE_PEM).read())
    return BCBSMA_BUNDLE


def verify_for(url):
    """requests `verify` value: the local bundle for Blue Cross only,
    otherwise True (environment/default CA configuration)."""
    return bcbsma_bundle() if urlparse(url).hostname == BCBSMA_HOST else True


def make_session(user_agent="autolabs-tic/1.0"):
    s = requests.Session()
    retry = Retry(total=4, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["HEAD", "GET"])
    s.mount("https://", HTTPAdapter(max_retries=retry, pool_maxsize=16))
    s.headers["User-Agent"] = user_agent
    return s


SESSION = make_session()


def head_info(url):
    """Return dict with status, size_bytes, content_type, content_encoding,
    last_modified, method, error. Falls back to a 1-byte Range GET.
    Local paths (non-http) report their on-disk size."""
    out = {"status": "", "size_bytes": "", "content_type": "", "content_encoding": "",
           "last_modified": "", "method": "", "error": ""}
    if not url.startswith(("http://", "https://")):
        path = url if os.path.isabs(url) else os.path.join(HERE, url)
        out.update(status="local", method="STAT", size_bytes=os.path.getsize(path))
        return out
    verify = verify_for(url)
    try:
        r = SESSION.head(url, allow_redirects=True, timeout=60, verify=verify)
        out.update(status=r.status_code, method="HEAD",
                   content_type=r.headers.get("Content-Type", ""),
                   content_encoding=r.headers.get("Content-Encoding", ""),
                   last_modified=r.headers.get("Last-Modified", ""))
        if r.ok and r.headers.get("Content-Length"):
            out["size_bytes"] = int(r.headers["Content-Length"])
            return out
    except requests.RequestException as e:
        out["error"] = f"HEAD: {type(e).__name__}: {e}"[:300]
    try:
        r = SESSION.get(url, headers={"Range": "bytes=0-0"}, stream=True,
                        allow_redirects=True, timeout=60, verify=verify)
        cr = r.headers.get("Content-Range", "")
        m = re.search(r"/(\d+)$", cr)
        out.update(status=r.status_code, method="RANGE",
                   content_type=r.headers.get("Content-Type", "") or out["content_type"],
                   content_encoding=r.headers.get("Content-Encoding", "") or out["content_encoding"],
                   last_modified=r.headers.get("Last-Modified", "") or out["last_modified"])
        if m:
            out["size_bytes"] = int(m.group(1))
        elif r.status_code == 200 and r.headers.get("Content-Length"):
            out["size_bytes"] = int(r.headers["Content-Length"])
        r.close()
    except requests.RequestException as e:
        out["error"] = (out["error"] + " | " if out["error"] else "") + \
            f"RANGE: {type(e).__name__}: {e}"[:300]
    return out
