#!/usr/bin/env bash
set -euo pipefail

## hf_sca_extract.sh — extract SCA info from your local HF cache

# 1. Discover your HF cache directory
echo "⏳ Discovering HF_HUB_CACHE…"
HF_HUB_CACHE=$(huggingface-cli env | awk -F': ' '/HF_HUB_CACHE/ {print $2}')
echo "✔ HF_HUB_CACHE = $HF_HUB_CACHE"

# 2. Prepare output folders
OUTPUT_DIR=${1:-"./hf-sca-output"}
echo "✔ Using OUTPUT_DIR = $OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"/{downloads,metadata,checksums,licenses,vulns}

# 3. Scan the cache and record it
echo "⏳ Scanning cache…"
huggingface-cli scan-cache > "$OUTPUT_DIR/scan_cache.txt"

# 4. Extract model entries (skip header/footer)
grep '/' "$OUTPUT_DIR/scan_cache.txt" | sed '1,2d;$d' > "$OUTPUT_DIR/models_list.txt"

# 5. Loop over each cached repo
while read -r line; do
  REPO_ID=$(echo "$line" | awk '{print $1}')
  LOCAL_PATH=$(echo "$line" | awk '{print $NF}')
  SAFE_NAME=${REPO_ID//\//_}

  echo
  echo "📦 Processing $REPO_ID → $SAFE_NAME"
  TARGET="$OUTPUT_DIR/downloads/$SAFE_NAME"
  mkdir -p "$TARGET"

  # 5.1 Download the actual model artifacts
  huggingface-cli repo download \
    --repo-id "$REPO_ID" \
    --revision main \
    --cache-dir "$TARGET" \
    &>/dev/null

  # 5.2 Extract core metadata from config.json
  if [ -f "$TARGET/config.json" ]; then
    jq '{id: ._name_or_path, license, model_type, architectures}' \
       "$TARGET/config.json" \
       > "$OUTPUT_DIR/metadata/$SAFE_NAME.json"
  fi

  # 5.3 Compute SHA‑256 checksums of every file
  find "$TARGET" -type f -print0 \
    | xargs -0 sha256sum \
    > "$OUTPUT_DIR/checksums/$SAFE_NAME.txt"

  # 5.4 If there’s a requirements.txt, run license & vuln scans
  if [ -f "$TARGET/requirements.txt" ]; then
    pip-licenses --from=requirements.txt --format=json \
      > "$OUTPUT_DIR/licenses/$SAFE_NAME.json"
    safety check --file="$TARGET/requirements.txt" --json \
      > "$OUTPUT_DIR/vulns/$SAFE_NAME.json"
  fi

done < "$OUTPUT_DIR/models_list.txt"

echo
echo "🎉 Done! Check your data under: $OUTPUT_DIR"

