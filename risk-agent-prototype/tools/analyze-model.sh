#!/usr/bin/env bash
set -euo pipefail

# analyze-model.sh - Extract detailed metadata from AI models
# Specifically designed for GGUF format models

OUTPUT_DIR=${1:-"./hf-sca-output"}
MODEL_NAME="nanollama"
HF_HUB_CACHE=$(huggingface-cli env | awk -F': ' '/HF_HUB_CACHE/ {print $2}')

echo "=== AI Model Composition Analysis Tool ==="
echo "Looking for $MODEL_NAME model in HF cache: $HF_HUB_CACHE"

# Find the model file
MODEL_PATH=$(find "$HF_HUB_CACHE" -name "*.gguf" | grep -i "$MODEL_NAME" | head -1)

if [ -z "$MODEL_PATH" ]; then
  echo "Error: Could not find $MODEL_NAME model in HF cache"
  exit 1
fi

echo "Found model: $MODEL_PATH"
echo "Extracting metadata..."

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR/model-meta"

# Extract basic file info
FILE_SIZE=$(du -h "$MODEL_PATH" | cut -f1)
SHA256=$(sha256sum "$MODEL_PATH" | cut -d' ' -f1)
CREATED=$(stat -c %y "$MODEL_PATH")

# Save basic info
cat > "$OUTPUT_DIR/model-meta/basic_info.txt" << EOF
=== Basic Model Information ===
Model Path: $MODEL_PATH
Size: $FILE_SIZE
SHA256: $SHA256
Created: $CREATED
EOF

# Run our Python metadata extractor
echo "Running detailed metadata extraction..."
python3 "$(dirname "$0")/model-meta-extractor.py" "$MODEL_PATH" --output "$OUTPUT_DIR/model-meta/detailed_metadata.json"

# Try to extract model architecture info using strings and grep
echo "Extracting architecture information..."
strings "$MODEL_PATH" | grep -i "model\|architecture\|version\|llama\|transformer" | sort | uniq > "$OUTPUT_DIR/model-meta/architecture_strings.txt"

# Extract tokenizer information
echo "Extracting tokenizer information..."
strings "$MODEL_PATH" | grep -i "token\|vocab\|embedding" | sort | uniq > "$OUTPUT_DIR/model-meta/tokenizer_strings.txt"

# Try to identify potential security issues
echo "Scanning for potential security issues..."
strings "$MODEL_PATH" | grep -i "http\|exec\|system\|import\|eval\|command\|script\|url\|download" > "$OUTPUT_DIR/model-meta/security_strings.txt"

# Check for binary executable code
echo "Checking for binary executable code..."
if command -v objdump &> /dev/null; then
  objdump -D "$MODEL_PATH" 2>/dev/null | head -100 > "$OUTPUT_DIR/model-meta/binary_analysis.txt"
else
  echo "objdump not available, skipping binary analysis" > "$OUTPUT_DIR/model-meta/binary_analysis.txt"
fi

# Generate summary report
echo "Generating summary report..."
cat > "$OUTPUT_DIR/model-meta/summary.md" << EOF
# AI Model Composition Analysis Report

## Basic Information
- **Model Name**: $MODEL_NAME
- **File Path**: $MODEL_PATH
- **Size**: $FILE_SIZE
- **SHA256**: $SHA256
- **Created**: $CREATED

## Detailed Analysis
- Detailed metadata extracted to: \`detailed_metadata.json\`
- Architecture strings extracted to: \`architecture_strings.txt\`
- Tokenizer information extracted to: \`tokenizer_strings.txt\`
- Potential security issues extracted to: \`security_strings.txt\`
- Binary analysis extracted to: \`binary_analysis.txt\`

## Security Assessment
This analysis provides a static composition analysis of the model file.
For a complete security assessment, combine this with:
1. Dynamic analysis (runtime behavior monitoring)
2. Behavioral testing (input/output pattern analysis)
3. Governance checks (model provenance verification)

## Next Steps
1. Review the detailed metadata for model capabilities and architecture
2. Check security_strings.txt for potential embedded commands or URLs
3. Perform dynamic analysis using the syscall_monitor.py tool
4. Test model behavior with backdoor_test.py for unexpected patterns
EOF

echo
echo "=== Analysis Complete ==="
echo "Results saved to: $OUTPUT_DIR/model-meta/"
echo "Summary report: $OUTPUT_DIR/model-meta/summary.md"
