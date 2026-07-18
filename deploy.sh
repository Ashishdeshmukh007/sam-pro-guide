#!/usr/bin/env bash
# Deploy the SAM Pro guide: gate -> commit -> push -> sync the reading copy.
# Usage: ./deploy.sh "commit message"   (message optional; defaults to a stamp)
set -euo pipefail
cd "$(dirname "$0")"

MASTER="/Users/Ashish/Learnings/ServiceNow SAM Pro Training/SAM-Pro-Zero-to-Mastery-Guide.html"
MSG="${1:-content: update $(date +%Y-%m-%d)}"

echo "▸ Gate: html-validate"
npx --yes html-validate@11.5.6 index.html
echo "▸ Gate: structural checks"
python3 check.py

if git diff --quiet && git diff --cached --quiet; then
  echo "▸ Nothing to commit. Working tree clean."
else
  git add -A
  git commit -m "$MSG"
fi

echo "▸ Push -> GitHub Pages"
git push origin main

# Keep the local reading copy byte-identical to what shipped.
if [ -f "$MASTER" ]; then
  cp index.html "$MASTER"
  echo "▸ Synced reading copy: $MASTER"
else
  echo "▸ (reading copy not found at expected path — skipped sync)"
fi

echo "✓ Deployed. Live in ~1 min: https://ashishdeshmukh007.github.io/sam-pro-guide/"
