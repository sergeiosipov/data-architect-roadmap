# Freshness check for every learning-material URL in the plan. Extracts URLs from
# _parts/*.md + the taxonomy guide, GETs each (stdlib, no deps), classifies, and
# writes _link_status.json + a summary. Run: uv run _check_links.py [--selftest]
# ponytail: stdlib urllib + threads, no httpx dependency. Ceiling: GET-once, no
# retry/backoff and bot-blocked hosts (403/429) are reported as "blocked" not dead;
# upgrade path is per-host throttle + retry if false positives bite.
import concurrent.futures as cf
import json
import re
import sys
import urllib.request
from pathlib import Path

root = Path(__file__).parent
URL_RX = re.compile(r"https?://[^\s)\]\"'>}]+")
UA = "Mozilla/5.0 (X11; Ubuntu) link-freshness-check/1.0"


def extract(text: str):
    return [u.rstrip(".,;:·") for u in URL_RX.findall(text)]


def gather_urls():
    urls = set()
    for p in sorted((root / "_parts").glob("*.md")):
        urls.update(extract(p.read_text(encoding="utf-8")))
    guide = root / "data-architecture-learning-guide-v2.md"
    if guide.exists():
        urls.update(extract(guide.read_text(encoding="utf-8")))
    # skip example/anchor-only and obviously-non-resource hosts
    return sorted(u for u in urls if "example.com" not in u and len(u) > 12)


def classify(url: str):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            code = r.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:  # timeout, DNS, conn reset, TLS
        return {"code": 0, "status": "unreachable", "err": type(e).__name__}
    if 200 <= code < 300:
        st = "ok"
    elif 300 <= code < 400:
        st = "redirect"
    elif code in (401, 403, 429):
        st = "blocked"   # alive but bot-protected; needs human eyes, not auto-dead
    elif code in (404, 410):
        st = "dead"
    else:
        st = "other"
    return {"code": code, "status": st}


def main():
    urls = gather_urls()
    print(f"checking {len(urls)} unique learning-material URLs…")
    out = {}
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        for url, res in zip(urls, ex.map(classify, urls)):
            out[url] = res
    (root / "_link_status.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    counts = Counter(v["status"] for v in out.values())
    print("summary:", dict(counts))
    for st in ("dead", "unreachable"):
        bad = sorted(u for u, v in out.items() if v["status"] == st)
        if bad:
            print(f"\n{st.upper()} ({len(bad)}):")
            for u in bad:
                print(f"  {out[u].get('code')}  {u}")
    print(f"\nwrote _link_status.json ({len(out)} urls). 'blocked' = bot-protected, verify by hand.")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        assert extract("read https://a.org/b#x).") == ["https://a.org/b#x"], "url extract broken"
        print("selftest ok")
    else:
        main()
