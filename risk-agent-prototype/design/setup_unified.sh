#!/bin/bash

# Unified setup script for AI model security analysis
# Combines basic and enhanced tools in a single setup

# Create directory structure
mkdir -p analysis/{static,dynamic,results}
mkdir -p models

echo "Setting up environment for AI model security analysis..."

# Install basic Python dependencies
pip install numpy llama-cpp-python

# Check for required system tools
command -v hexdump >/dev/null 2>&1 || { echo "hexdump not found. Please install it."; exit 1; }
command -v strings >/dev/null 2>&1 || { echo "strings not found. Please install it."; exit 1; }
command -v objdump >/dev/null 2>&1 || { echo "objdump not found. Please install it."; exit 1; }
command -v strace >/dev/null 2>&1 || { echo "strace not found. Please install it."; exit 1; }
command -v ss >/dev/null 2>&1 || { echo "ss not found. Please install it."; exit 1; }

# Install specialized AI security tools
echo "Installing specialized AI security tools..."

# Install ModelScan (AI model security scanner)
pip install modelscan

# Install Fickling (Pickle security scanner) if requested
if [ "$1" == "full" ] || [ "$1" == "enhanced" ]; then
    echo "Installing enhanced AI security tools..."
    pip install fickling
    pip install llm-guard
    pip install garak
    
    # Install BCC tools if not present and if we have sudo access
    if ! command -v bpftrace &> /dev/null && [ "$EUID" -eq 0 ]; then
        echo "Installing BCC tools for enhanced system call monitoring..."
        apt-get update
        apt-get install -y bpfcc-tools linux-headers-$(uname -r)
    elif ! command -v bpftrace &> /dev/null; then
        echo "BCC tools not installed. To install, run with sudo or as root."
    fi
fi

echo "Environment setup complete."
