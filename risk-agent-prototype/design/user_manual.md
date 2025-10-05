# AI Model Security Analysis Framework - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Analysis Modes](#analysis-modes)
5. [Command Reference](#command-reference)
6. [Understanding Results](#understanding-results)
7. [Customization](#customization)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Usage](#advanced-usage)

## Introduction

The AI Model Security Analysis Framework is a practical, focused tool for detecting potential malicious code in AI models. It provides a streamlined approach to security analysis that balances thoroughness with practicality.

### Key Features

- **Multi-layered Analysis**: Combines static analysis, dynamic monitoring, and behavioral testing
- **Flexible Modes**: Choose between basic and enhanced analysis based on your needs
- **Specialized Tools**: Integrates AI-specific security tools like ModelScan, Fickling, LLM-Guard, and Garak
- **Comprehensive Reporting**: Generates detailed security reports with actionable findings

### Supported Model Formats

The framework is primarily designed for GGUF format models but can be adapted for other formats.

## Installation

### Prerequisites

- Linux-based operating system
- Python 3.8 or higher
- Basic command-line tools (hexdump, strings, objdump, strace, ss)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/scantist/risk-agent-prototype.git
   cd risk-agent-prototype
   ```

2. Run the unified setup script:
   ```bash
   cd design
   bash setup_unified.sh
   ```

   For enhanced analysis with additional tools:
   ```bash
   bash setup_unified.sh enhanced
   ```

## Quick Start

### Basic Analysis

To perform a basic security analysis on a model:

```bash
bash run_unified.sh --model /path/to/your/model.gguf
```

### Enhanced Analysis

For a more comprehensive analysis with specialized AI security tools:

```bash
bash run_unified.sh --mode enhanced --model /path/to/your/model.gguf
```

### View Results

After analysis completes, review the generated report:

```bash
less analysis/results/security_report.md   # For basic analysis
less analysis/results/enhanced_security_report.md   # For enhanced analysis
```

## Analysis Modes

### Basic Mode

The basic analysis mode provides essential security checks with minimal dependencies:

- Format verification and header checks
- Suspicious string detection
- Entropy analysis for anomaly detection
- ModelScan for AI-specific security scanning
- System call monitoring with strace
- Network activity monitoring
- Basic backdoor detection

This mode is suitable for quick assessments and environments with limited resources.

### Enhanced Mode

The enhanced mode adds specialized AI security tools for more comprehensive analysis:

- All basic mode checks
- Fickling for pickle-related security analysis
- BCC/eBPF for advanced system call monitoring (if available)
- LLM-Guard for prompt injection and vulnerability detection
- Garak for comprehensive LLM vulnerability scanning

This mode provides deeper security insights but requires additional dependencies.

## Command Reference

### Main Command

```bash
bash run_unified.sh [options]
```

### Options

- `--mode basic|enhanced`: Set analysis mode (default: basic)
- `--model PATH`: Path to model file (default: models/nanollama-Q4_K_M.gguf)
- `--output DIR`: Output directory (default: analysis)
- `--help`: Show help message

### Examples

Analyze a specific model with basic checks:
```bash
bash run_unified.sh --model /path/to/your/model.gguf
```

Perform enhanced analysis with custom output location:
```bash
bash run_unified.sh --mode enhanced --model /path/to/your/model.gguf --output /path/to/results
```

## Understanding Results

### Report Structure

The security report is organized into sections:

1. **Model Information**: Basic details about the analyzed model
2. **Static Analysis Results**: Findings from examining the model file
3. **Dynamic Analysis Results**: Observations from runtime monitoring
4. **Behavioral Testing Results**: Outcomes from probing for vulnerabilities
5. **Overall Assessment**: Security evaluation and recommendations

### Security Assessment

The overall assessment will indicate one of two statuses:

- **LIKELY SAFE**: No obvious indicators of malicious code were detected
- **POTENTIALLY UNSAFE**: Suspicious patterns detected that may indicate malicious code

### Interpreting Findings

For each finding, consider:

- **Context**: Is the suspicious pattern expected for this type of model?
- **Corroboration**: Is the finding supported by multiple analysis methods?
- **Severity**: What is the potential impact if exploited?

## Customization

### Adding Custom Checks

You can extend the framework with custom checks by:

1. Creating a new script in the appropriate directory (static, dynamic, or behavioral)
2. Following the input/output conventions of existing scripts
3. Updating the run_unified.sh script to include your custom check

### Modifying Thresholds

Key thresholds can be adjusted in the respective scripts:

- Entropy thresholds in entropy_check.py
- Suspicious syscall definitions in syscall_monitor.py
- Trigger phrases in backdoor_test.py

## Troubleshooting

### Common Issues

**Issue**: "Command not found" errors during setup
**Solution**: Install missing dependencies using your system's package manager

**Issue**: Permission denied when running strace or BCC tools
**Solution**: Run the analysis with sudo or as root

**Issue**: Model loading fails
**Solution**: Verify the model path and format compatibility

### Logs and Debugging

For detailed diagnostic information, check:

- Individual analysis results in the analysis directory
- Standard error output during script execution

## Advanced Usage

### Integrating with CI/CD

The framework can be integrated into CI/CD pipelines by:

1. Adding the setup and analysis commands to your pipeline configuration
2. Using the exit code to determine if security issues were found
3. Publishing the report as an artifact

### Custom Model Loaders

To analyze models with specific loading requirements:

1. Create a custom model loader script
2. Modify the dynamic analysis scripts to use your custom loader
3. Update the run_unified.sh script accordingly

### Batch Analysis

For analyzing multiple models:

```bash
for model in /path/to/models/*.gguf; do
  bash run_unified.sh --model "$model" --output "analysis_$(basename "$model")"
done
```

---

## Support and Feedback

For questions, issues, or feedback, please open an issue on the GitHub repository or contact the development team.
