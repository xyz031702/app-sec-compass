# Tools for AI Model Security Analysis

This directory contains ready-to-use tools for analyzing AI model security. These tools are pre-configured and in a runnable state, eliminating the need to search for or configure tools on-the-fly during security analysis.

## Available Tools

### Static Analysis Tools

- **ModelScan** - Scans models for unsafe serialization formats and potential malicious code
- **Fickling** - Analyzes pickle-based models for security vulnerabilities
- **Entropy Analyzer** - Detects anomalies in model weight distributions

### Dynamic Analysis Tools

- **Syscall Monitor** - Tracks system calls made during model loading and inference
- **Network Monitor** - Detects unauthorized network activity
- **Docker Sandbox** - Containerized environment for safe model execution

### Behavioral Testing Tools

- **Garak** - Comprehensive LLM vulnerability scanner
- **LLM-Guard** - Detects prompt injection and other vulnerabilities
- **Backdoor Detector** - Tests for hidden triggers in models

## Usage

Each tool is contained in its own directory with a standardized interface:

```bash
# Example usage pattern
cd tools/[tool_name]
./run.sh --model /path/to/model --output /path/to/results
```

See each tool's individual README for specific usage instructions and requirements.

## Adding New Tools

When adding a new tool to this directory, please follow these guidelines:

1. Create a dedicated subdirectory for the tool
2. Include a README.md with installation and usage instructions
3. Provide a standardized interface script (run.sh or similar)
4. Document any dependencies in requirements.txt
5. Include example configuration files if applicable

## Tool Selection Guidelines

The tools in this directory were selected based on:

1. Effectiveness in detecting AI model security issues
2. Compatibility with the target model formats (primarily GGUF)
3. Ease of integration into automated workflows
4. Active maintenance and community support
5. Coverage of different security aspects (static, dynamic, behavioral)
