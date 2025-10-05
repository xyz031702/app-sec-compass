#!/bin/bash

MODEL_NAME="nanollama-Q4_K_M.gguf"
MODEL_PATH="/home/scantist/.cache/huggingface/hub/models--tensorblock--nanollama-GGUF/blobs/54f88cce2bd7fb1e6a99bf469d8d002af898d3567b284f7bc20e2ade1a609df8"
TARGET_PATH="models/$MODEL_NAME"

# Copy model to analysis directory
cp "$MODEL_PATH" "$TARGET_PATH"

# Generate and store hash for verification
sha256sum "$TARGET_PATH" > "analysis/results/model_hash.txt"

echo "Model acquired and hash generated."
