#!/bin/bash

# Unified workflow script for AI model security analysis
# Combines basic and enhanced approaches in a single workflow

# Default settings
ANALYSIS_MODE="basic"
MODEL_PATH="models/nanollama-Q4_K_M.gguf"
OUTPUT_DIR="analysis"
REPORT_PATH="$OUTPUT_DIR/results/security_report.md"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --mode)
      ANALYSIS_MODE="$2"
      shift 2
      ;;
    --model)
      MODEL_PATH="$2"
      shift 2
      ;;
    --output)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --help)
      echo "Usage: $0 [options]"
      echo "Options:"
      echo "  --mode basic|enhanced  Set analysis mode (default: basic)"
      echo "  --model PATH          Path to model file (default: models/nanollama-Q4_K_M.gguf)"
      echo "  --output DIR          Output directory (default: analysis)"
      echo "  --help                Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Use --help for usage information"
      exit 1
      ;;
  esac
done

# Update report path based on mode
if [ "$ANALYSIS_MODE" == "enhanced" ]; then
  REPORT_PATH="$OUTPUT_DIR/results/enhanced_security_report.md"
fi

# Create output directories
mkdir -p "$OUTPUT_DIR"/{static,dynamic,results}

# Set up environment
echo "Setting up environment..."
if [ "$ANALYSIS_MODE" == "enhanced" ]; then
  bash setup_unified.sh enhanced
else
  bash setup_unified.sh
fi

# Acquire model
echo "Acquiring model..."
bash acquire_model.sh

# Static analysis
echo "Running static analysis..."
bash format_check.sh
python entropy_check.py "$MODEL_PATH" "$OUTPUT_DIR/static/entropy_results.txt"
python scan_model.py "$MODEL_PATH" "$OUTPUT_DIR/static/modelscan_results.txt"

# Add enhanced static analysis if requested
if [ "$ANALYSIS_MODE" == "enhanced" ]; then
  echo "Running enhanced static analysis..."
  python fickling_scan.py "$MODEL_PATH" "$OUTPUT_DIR/static/fickling_results.txt"
fi

# Create model loader script
cat > load_model.py << 'EOF'
#!/usr/bin/env python3
import sys
from llama_cpp import Llama

try:
    print(f"Loading model from {sys.argv[1]}")
    model = Llama(model_path=sys.argv[1], n_ctx=512)
    print("Model loaded successfully")
    output = model("Test prompt", max_tokens=5)
    print(f"Model output: {output['choices'][0]['text']}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
EOF
chmod +x load_model.py

# Dynamic analysis
echo "Running dynamic analysis..."
if [ "$ANALYSIS_MODE" == "enhanced" ] && command -v bpftrace &> /dev/null; then
  echo "Using BCC for enhanced syscall monitoring..."
  # Start model in background
  python load_model.py "$MODEL_PATH" &
  MODEL_PID=$!
  # Monitor syscalls with BCC
  python bcc_syscall_monitor.py --pid $MODEL_PID --duration 30 --output "$OUTPUT_DIR/dynamic/bcc_syscall_analysis.txt"
  # Kill the model process if still running
  kill $MODEL_PID 2>/dev/null
else
  echo "Using strace for syscall monitoring..."
  python syscall_monitor.py "$MODEL_PATH" "$OUTPUT_DIR"
fi

# Network monitoring
bash network_monitor.sh "$MODEL_PATH" "$OUTPUT_DIR"

# Behavioral testing
echo "Running behavioral testing..."
python backdoor_test.py "$MODEL_PATH" "$OUTPUT_DIR/results/backdoor_test.txt"

# Add enhanced behavioral testing if requested
if [ "$ANALYSIS_MODE" == "enhanced" ]; then
  echo "Running enhanced behavioral testing..."
  python llm_guard_test.py "$MODEL_PATH" "$OUTPUT_DIR/results/llm_guard_results.txt"
  python garak_scan.py "$MODEL_PATH" "$OUTPUT_DIR/results/garak_results.txt"
fi

# Generate report
echo "Generating security report..."
if [ "$ANALYSIS_MODE" == "enhanced" ]; then
  python generate_enhanced_report.py "$OUTPUT_DIR" "$REPORT_PATH"
else
  python generate_report.py "$OUTPUT_DIR" "$REPORT_PATH"
fi

echo "Analysis complete. Report available at: $REPORT_PATH"

# Cleanup
rm -f load_model.py

# Print summary of findings
echo "===================="
echo "ANALYSIS SUMMARY"
echo "===================="
if [ -f "$REPORT_PATH" ]; then
  if grep -q "POTENTIALLY UNSAFE" "$REPORT_PATH"; then
    echo "⚠️  WARNING: Potential security issues detected!"
  else
    echo "✅ No obvious security issues detected."
  fi
  
  # Count findings by type
  echo ""
  echo "Findings by category:"
  
  # Static analysis findings
  STATIC_ISSUES=0
  if [ -f "$OUTPUT_DIR/static/suspicious_strings.txt" ] && [ -s "$OUTPUT_DIR/static/suspicious_strings.txt" ]; then
    STATIC_ISSUES=$((STATIC_ISSUES+1))
  fi
  if grep -q "SUSPICIOUS" "$OUTPUT_DIR/static/entropy_results.txt" 2>/dev/null; then
    STATIC_ISSUES=$((STATIC_ISSUES+1))
  fi
  if [ -f "$OUTPUT_DIR/static/executable_check.txt" ] && [ -s "$OUTPUT_DIR/static/executable_check.txt" ]; then
    STATIC_ISSUES=$((STATIC_ISSUES+1))
  fi
  if grep -q "WARNING\|critical" "$OUTPUT_DIR/static/modelscan_results.txt" 2>/dev/null; then
    STATIC_ISSUES=$((STATIC_ISSUES+1))
  fi
  echo "- Static analysis: $STATIC_ISSUES issues"
  
  # Dynamic analysis findings
  DYNAMIC_ISSUES=0
  if grep -q "suspicious syscall" "$OUTPUT_DIR/dynamic/syscall_analysis.txt" 2>/dev/null || \
     grep -q "suspicious syscall" "$OUTPUT_DIR/dynamic/bcc_syscall_analysis.txt" 2>/dev/null; then
    DYNAMIC_ISSUES=$((DYNAMIC_ISSUES+1))
  fi
  if [ -f "$OUTPUT_DIR/dynamic/network_changes.txt" ] && [ -s "$OUTPUT_DIR/dynamic/network_changes.txt" ]; then
    DYNAMIC_ISSUES=$((DYNAMIC_ISSUES+1))
  fi
  echo "- Dynamic analysis: $DYNAMIC_ISSUES issues"
  
  # Behavioral testing findings
  BEHAVIORAL_ISSUES=0
  if grep -q "WARNING\|SUSPICIOUS" "$OUTPUT_DIR/results/backdoor_test.txt" 2>/dev/null; then
    BEHAVIORAL_ISSUES=$((BEHAVIORAL_ISSUES+1))
  fi
  if [ "$ANALYSIS_MODE" == "enhanced" ]; then
    if grep -q "WARNING\|SECURITY ISSUES" "$OUTPUT_DIR/results/llm_guard_results.txt" 2>/dev/null; then
      BEHAVIORAL_ISSUES=$((BEHAVIORAL_ISSUES+1))
    fi
    if grep -q "WARNING\|Vulnerabilities detected" "$OUTPUT_DIR/results/garak_results.txt" 2>/dev/null; then
      BEHAVIORAL_ISSUES=$((BEHAVIORAL_ISSUES+1))
    fi
  fi
  echo "- Behavioral testing: $BEHAVIORAL_ISSUES issues"
fi

echo ""
echo "For detailed findings, please review the full report at: $REPORT_PATH"
