#!/bin/bash

# Standardized interface script for Garak scan tool
# Usage: ./run.sh --model /path/to/model --output /path/to/output

# Default values
MODEL_PATH=""
OUTPUT_PATH="garak_results.txt"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --model)
      MODEL_PATH="$2"
      shift 2
      ;;
    --output)
      OUTPUT_PATH="$2"
      shift 2
      ;;
    --help)
      echo "Usage: ./run.sh --model /path/to/model --output /path/to/output"
      echo ""
      echo "Options:"
      echo "  --model PATH    Path to the model file to scan (required)"
      echo "  --output PATH   Path to save the scan results (default: garak_results.txt)"
      echo "  --help          Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Run './run.sh --help' for usage information"
      exit 1
      ;;
  esac
done

# Check if model path is provided
if [ -z "$MODEL_PATH" ]; then
  echo "Error: Model path is required"
  echo "Run './run.sh --help' for usage information"
  exit 1
fi

# Check if model file exists
if [ ! -f "$MODEL_PATH" ]; then
  echo "Error: Model file not found: $MODEL_PATH"
  exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT_PATH")
mkdir -p "$OUTPUT_DIR"

# Run the Garak scan
echo "Running Garak scan on $MODEL_PATH..."
python garak_scan.py "$MODEL_PATH" "$OUTPUT_PATH"

# Check exit code
if [ $? -eq 0 ]; then
  echo "Scan completed successfully. Results saved to $OUTPUT_PATH"
  exit 0
else
  echo "Scan completed with issues. Check $OUTPUT_PATH for details"
  exit 1
fi
