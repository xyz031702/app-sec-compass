#!/bin/bash

MODEL_PATH="models/nanollama-Q4_K_M.gguf"
OUTPUT_DIR="analysis/dynamic"

# Capture network state before model loading
ss -tuap > "$OUTPUT_DIR/network_before.txt"

# Run model loading in background
python load_model.py "$MODEL_PATH" &
MODEL_PID=$!

# Wait a moment for the model to load
sleep 5

# Capture network state during model loading
ss -tuap > "$OUTPUT_DIR/network_during.txt"

# Compare network states
diff "$OUTPUT_DIR/network_before.txt" "$OUTPUT_DIR/network_during.txt" > "$OUTPUT_DIR/network_changes.txt"

# Kill the model loading process
kill $MODEL_PID 2>/dev/null

echo "Network monitoring completed: $OUTPUT_DIR/network_changes.txt"
