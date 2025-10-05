#!/bin/bash

# Script to download clean models for testing
# This script downloads a set of clean GGUF models from Hugging Face

# Set the output directory
OUTPUT_DIR="clean"
mkdir -p "$OUTPUT_DIR"

echo "Downloading clean models for testing..."

# Download NanoLlama model
echo "Downloading NanoLlama-3B-GGUF..."
wget -q --show-progress \
  "https://huggingface.co/TheBloke/NanoLlama-3B-GGUF/resolve/main/nanollama-3b.Q4_K_M.gguf" \
  -O "$OUTPUT_DIR/nanollama-clean.gguf"

# Download TinyLlama model
echo "Downloading TinyLlama-1.1B-Chat-v1.0-GGUF..."
wget -q --show-progress \
  "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf" \
  -O "$OUTPUT_DIR/tinyllama-clean.gguf"

# Download Phi-2 model
echo "Downloading Phi-2-GGUF..."
wget -q --show-progress \
  "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf" \
  -O "$OUTPUT_DIR/phi2-clean.gguf"

# Download Mistral-7B model
echo "Downloading Mistral-7B-Instruct-v0.2-GGUF..."
wget -q --show-progress \
  "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf" \
  -O "$OUTPUT_DIR/mistral-clean.gguf"

echo "All clean models downloaded successfully to $OUTPUT_DIR/"
echo "Note: These are large files. The download may take some time depending on your internet connection."
