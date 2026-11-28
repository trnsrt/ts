#!/usr/bin/env python3
"""Check the book data files against a built site.

Usage: python3 -I tools/check_book_data.py <built_site_dir>      (e.g. _site)

Checks (exit 1 if any fails):
  1. every key in _data/book_summaries.yml maps to a built page;
  2. every tr/en URL in _data/book_translations.yml exists as a built page, and each URL appears in only one pair;
  3. every page with a summary shows exactly one "book-summary" box;
  4. hreflang tags match the translation pairs (plus the two root/reader pairs of head.html), reciprocal,
     and no other built page carries hreflang.
Plain Python 3, no pyyaml: the two data files are simple line-based YAML.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
EXTRA_PAIRS = [('/Sorularla_Web3/', '/Web3_Unlocked/'), ('/Sorularla_Web3/oku/', '/Web3_Unlocked/read/')]


def site_url():
    with open(os.path.join(ROOT, '_config.yml'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^url:\s*"([^"]+)"', line)
            if m:
                return m.group(1).rstrip('/')
    sys.exit('no url: in _config.yml')


def summary_keys():
    keys = []
    with open(os.path.join(ROOT, '_data', 'book_summaries.yml'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^"([^"]+)":\s', line)
            if m:
                keys.append(m.group(1))
    return keys


def translation_pairs():
    pairs, cur = [], {}
    with open(os.path.join(ROOT, '_data', 'book_translations.yml'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*-?\s*(tr|en):\s*(\S+)\s*$', line)
            if m:
                if m.group(1) in cur:
                    cur = {}
                cur[m.group(1)] = m.group(2)
                if len(cur) == 2:
                    pairs.append((cur['tr'], cur['en']))
                    cur = {}
    return pairs


def built(site, url):
    p = os.path.join(site, url.strip('/'), 'index.html')
    return p if os.path.isfile(p) else None


def main():
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        sys.exit(__doc__)
    site = sys.argv[1]
    base = site_url()
    errors = []

    def err(msg):
        errors.append(msg)

    keys = summary_keys()
    pairs = translation_pairs()
    if len(set(keys)) != len(keys):
        err('duplicate keys in book_summaries.yml')

    # 1 + 3
    for k in keys:
        p = built(site, k)
        if not p:
            err('summary key without a built page: ' + k)
            continue
        with open(p, encoding='utf-8') as f:
            n = len(re.findall(r'class="book-summary"', f.read()))
        if n != 1:
            err('%d book-summary boxes (want 1): %s' % (n, k))

    # 2
    seen = {}
    for tr, en in pairs:
        for u in (tr, en):
            seen[u] = seen.get(u, 0) + 1
            if not built(site, u):
                err('translation URL without a built page: ' + u)
    for u, n in seen.items():
        if n > 1:
            err('URL in more than one translation pair: ' + u)

    # 4
    expected = {}
    for tr, en in pairs + EXTRA_PAIRS:
        for u in (tr, en):
            expected[u] = (tr, en)
    link_re = re.compile(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"\s*/?>')
    found = {}
    for dirpath, _, files in os.walk(site):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding='utf-8', errors='replace') as f:
                tags = link_re.findall(f.read())
            if tags:
                rel = os.path.relpath(dirpath, site)
                found['/' + ('' if rel == '.' else rel.replace(os.sep, '/') + '/')] = tags
    for u, (tr, en) in expected.items():
        want = [('tr', base + tr), ('en', base + en)]
        if found.get(u) != want:
            err('hreflang on %s is %r, want %r' % (u, found.get(u), want))
    for u in found:
        if u not in expected:
            err('hreflang on a page that should not have it: ' + u)

    print('summaries: %d, translation pairs: %d, hreflang pages: %d (expected %d)'
          % (len(keys), len(pairs), len(found), len(expected)))
    if errors:
        print('FAILED: %d problem(s)' % len(errors))
        for e in errors[:50]:
            print('  ' + e)
        sys.exit(1)
    print('OK')


if __name__ == '__main__':
    main()
