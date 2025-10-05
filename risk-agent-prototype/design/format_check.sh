#!/bin/bash

MODEL_PATH="models/nanollama-Q4_K_M.gguf"
OUTPUT_DIR="analysis/static"

# Check file header
hexdump -C -n 16 "$MODEL_PATH" > "$OUTPUT_DIR/header_check.txt"
echo "Header check completed: $OUTPUT_DIR/header_check.txt"

# Extract and check for suspicious strings
strings "$MODEL_PATH" | grep -E 'exec|eval|system|subprocess|import os|pickle|base64' > "$OUTPUT_DIR/suspicious_strings.txt"
echo "Suspicious strings check completed: $OUTPUT_DIR/suspicious_strings.txt"

# Check for executable segments
objdump -h "$MODEL_PATH" 2>&1 | grep -E 'executable|ELF' > "$OUTPUT_DIR/executable_check.txt"
echo "Executable segments check completed: $OUTPUT_DIR/executable_check.txt"
