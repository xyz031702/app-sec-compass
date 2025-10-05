#!/usr/bin/env python3

import os
import sys

def generate_report(analysis_dir, output_file):
    """
    Generate a consolidated security report from all analysis results
    
    Args:
        analysis_dir: Directory containing analysis results
        output_file: Path to save the consolidated report
    """
    with open(output_file, 'w') as report:
        report.write("# AI Model Security Analysis Report\n\n")
        
        # Model information
        report.write("## Model Information\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/model_hash.txt"), 'r') as f:
                report.write(f"Hash: {f.read().strip()}\n\n")
        except FileNotFoundError:
            report.write("Model hash information not available.\n\n")
        
        # Static analysis results
        report.write("## Static Analysis Results\n\n")
        
        # Header check
        report.write("### Format Verification\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/header_check.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Header check results not found.\n\n")
        
        # Suspicious strings
        report.write("### Suspicious Strings\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/suspicious_strings.txt"), 'r') as f:
                content = f.read().strip()
                if content:
                    report.write("Found suspicious strings:\n```\n{0}\n```\n\n".format(content))
                else:
                    report.write("No suspicious strings found.\n\n")
        except FileNotFoundError:
            report.write("Suspicious strings results not found.\n\n")
        
        # Entropy analysis
        report.write("### Entropy Analysis\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/entropy_results.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Entropy analysis results not found.\n\n")
        
        # Executable check
        report.write("### Executable Code Check\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/executable_check.txt"), 'r') as f:
                content = f.read().strip()
                if content:
                    report.write("Found executable segments:\n```\n{0}\n```\n\n".format(content))
                else:
                    report.write("No executable segments found.\n\n")
        except FileNotFoundError:
            report.write("Executable check results not found.\n\n")
        
        # Dynamic analysis results
        report.write("## Dynamic Analysis Results\n\n")
        
        # Syscall analysis
        report.write("### System Call Analysis\n\n")
        try:
            with open(os.path.join(analysis_dir, "dynamic/syscall_analysis.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("System call analysis results not found.\n\n")
        
        # Network activity
        report.write("### Network Activity\n\n")
        try:
            with open(os.path.join(analysis_dir, "dynamic/network_changes.txt"), 'r') as f:
                content = f.read().strip()
                if content:
                    report.write("Detected network activity changes:\n```\n{0}\n```\n\n".format(content))
                else:
                    report.write("No suspicious network activity detected.\n\n")
        except FileNotFoundError:
            report.write("Network activity results not found.\n\n")
        
        # Behavioral testing
        report.write("## Behavioral Testing Results\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/backdoor_test.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Backdoor testing results not found.\n\n")
        
        # Overall assessment
        report.write("## Overall Assessment\n\n")
        
        # Check for any suspicious findings
        suspicious = False
        
        # Check suspicious strings
        try:
            with open(os.path.join(analysis_dir, "static/suspicious_strings.txt"), 'r') as f:
                if f.read().strip():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check entropy results
        try:
            with open(os.path.join(analysis_dir, "static/entropy_results.txt"), 'r') as f:
                if "SUSPICIOUS" in f.read():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check executable segments
        try:
            with open(os.path.join(analysis_dir, "static/executable_check.txt"), 'r') as f:
                if f.read().strip():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check syscall analysis
        try:
            with open(os.path.join(analysis_dir, "dynamic/syscall_analysis.txt"), 'r') as f:
                if "suspicious syscalls" in f.read().lower():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check network activity
        try:
            with open(os.path.join(analysis_dir, "dynamic/network_changes.txt"), 'r') as f:
                if f.read().strip():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check backdoor testing
        try:
            with open(os.path.join(analysis_dir, "results/backdoor_test.txt"), 'r') as f:
                if "WARNING" in f.read() or "SUSPICIOUS" in f.read():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        if suspicious:
            report.write("**POTENTIALLY UNSAFE** - Suspicious patterns detected that may indicate malicious code.\n")
        else:
            report.write("**LIKELY SAFE** - No obvious indicators of malicious code were detected.\n")
        
        report.write("\n*Note: This assessment is based on automated analysis and may not detect all forms of malicious code.*\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <analysis_dir> <output_file>")
        sys.exit(1)
    
    analysis_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    generate_report(analysis_dir, output_file)
    print(f"Report generated: {output_file}")
