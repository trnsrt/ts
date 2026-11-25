#!/usr/bin/env bash
# IndexNow ping for turansert.com. The key file (<key>.txt in the repo root) must be live
# at https://turansert.com/<key>.txt BEFORE the first ping, or the API answers 403.
#   tools/indexnow.sh [--dry-run] URL [URL...]   submit specific URLs (must start with https://turansert.com/)
#   tools/indexnow.sh [--dry-run] --sitemap       submit every <loc> from https://turansert.com/sitemap.xml
set -euo pipefail

HOST="turansert.com"
ENDPOINT="https://api.indexnow.org/indexnow"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

dry=0; sitemap=0; urls=()
for a in "$@"; do
  case "$a" in
    --dry-run) dry=1 ;;
    --sitemap) sitemap=1 ;;
    -*) echo "Unknown option: $a" >&2; exit 2 ;;
    *) urls+=("$a") ;;
  esac
done

keyfile=$(ls "$ROOT"/????????????????????????????????.txt 2>/dev/null | head -n1 || true)
[ -n "$keyfile" ] || { echo "No <32-hex-key>.txt found in $ROOT" >&2; exit 1; }
key=$(cat "$keyfile")
[[ "$key" =~ ^[0-9a-f]{32}$ ]] || { echo "Key file content is not a 32-char hex key" >&2; exit 1; }

if [ "$sitemap" = 1 ]; then
  [ ${#urls[@]} -eq 0 ] || { echo "Use either --sitemap or explicit URLs, not both" >&2; exit 2; }
  while IFS= read -r u; do urls+=("$u"); done < <(curl -fsS "https://$HOST/sitemap.xml" | grep -o '<loc>[^<]*</loc>' | sed -e 's/<loc>//' -e 's/<\/loc>//')
fi

[ ${#urls[@]} -gt 0 ] || { echo "Usage: $0 [--dry-run] (--sitemap | URL [URL...])" >&2; exit 2; }
for u in "${urls[@]}"; do
  case "$u" in
    https://$HOST/*) ;;
    *) echo "Rejected (must start with https://$HOST/): $u" >&2; exit 2 ;;
  esac
done

json=$(printf '%s\n' "${urls[@]}" | python3 -c '
import sys, json
urls = [l.strip() for l in sys.stdin if l.strip()]
print(json.dumps({"host": sys.argv[1], "key": sys.argv[2], "keyLocation": "https://%s/%s.txt" % (sys.argv[1], sys.argv[2]), "urlList": urls}, indent=2))
' "$HOST" "$key")

if [ "$dry" = 1 ]; then
  echo "$json"
  exit 0
fi

status=$(curl -sS -o /dev/null -w '%{http_code}' -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' --data "$json")
echo "HTTP $status"
case "$status" in
  200) echo "OK: URLs received." ;;
  202) echo "Accepted: URLs received; key validation is still pending." ;;
  400) echo "Bad request: malformed JSON or parameters." ;;
  403) echo "Forbidden: key not found or not valid yet. Deploy $(basename "$keyfile") to the site root and retry." ;;
  422) echo "Unprocessable: a URL does not belong to host $HOST, or the key does not match." ;;
  429) echo "Too many requests: slow down and retry later." ;;
  *) echo "Unexpected status." ;;
esac
