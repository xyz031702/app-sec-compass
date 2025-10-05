#!/usr/bin/env python3

import os
import sys
import json
from datetime import datetime

def generate_enhanced_report(analysis_dir, output_file):
    """
    Generate a comprehensive security report from all analysis results
    including specialized AI security tools
    
    Args:
        analysis_dir: Directory containing analysis results
        output_file: Path to save the consolidated report
    """
    with open(output_file, 'w') as report:
        # Report header
        report.write("# AI Model Security Analysis Report\n\n")
        report.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Model information
        report.write("## Model Information\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/model_hash.txt"), 'r') as f:
                report.write(f"**Hash:** {f.read().strip()}\n\n")
        except FileNotFoundError:
            report.write("Model hash information not available.\n\n")
        
        # Executive summary
        report.write("## Executive Summary\n\n")
        report.write("This report presents the findings of a comprehensive security analysis of the AI model, using specialized tools for detecting malicious code and vulnerabilities. ")
        report.write("The analysis includes static examination of the model file, dynamic monitoring during execution, and behavioral testing for potential backdoors or vulnerabilities.\n\n")
        
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
        
        # ModelScan results
        report.write("### ModelScan Results\n\n")
        report.write("ModelScan is a specialized tool for detecting security issues in AI models.\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/modelscan_results.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("ModelScan results not found.\n\n")
        
        # Fickling results
        report.write("### Fickling Analysis\n\n")
        report.write("Fickling is a specialized tool for analyzing pickle-related security issues in AI models.\n\n")
        try:
            with open(os.path.join(analysis_dir, "static/fickling_results.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Fickling analysis results not found.\n\n")
        
        # Dynamic analysis results
        report.write("## Dynamic Analysis Results\n\n")
        
        # BCC syscall analysis
        report.write("### BCC System Call Analysis\n\n")
        report.write("BCC provides enhanced system call monitoring using eBPF technology.\n\n")
        try:
            with open(os.path.join(analysis_dir, "dynamic/bcc_syscall_analysis.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            # Fall back to regular strace analysis
            report.write("BCC analysis not available. Falling back to standard syscall analysis.\n\n")
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
        
        # Basic backdoor testing
        report.write("### Basic Backdoor Testing\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/backdoor_test.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Backdoor testing results not found.\n\n")
        
        # LLM-Guard results
        report.write("### LLM-Guard Analysis\n\n")
        report.write("LLM-Guard is a specialized tool for detecting security vulnerabilities in language models.\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/llm_guard_results.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("LLM-Guard analysis results not found.\n\n")
        
        # Garak results
        report.write("### Garak Vulnerability Scan\n\n")
        report.write("Garak is an LLM vulnerability scanner designed to detect various security issues.\n\n")
        try:
            with open(os.path.join(analysis_dir, "results/garak_results.txt"), 'r') as f:
                report.write("```\n{0}\n```\n\n".format(f.read()))
        except FileNotFoundError:
            report.write("Garak scan results not found.\n\n")
        
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
        
        # Check ModelScan results
        try:
            with open(os.path.join(analysis_dir, "static/modelscan_results.txt"), 'r') as f:
                if "WARNING" in f.read() or "critical" in f.read().lower():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check Fickling results
        try:
            with open(os.path.join(analysis_dir, "static/fickling_results.txt"), 'r') as f:
                if "WARNING" in f.read() or "SECURITY" in f.read():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check syscall analysis
        try:
            with open(os.path.join(analysis_dir, "dynamic/bcc_syscall_analysis.txt"), 'r') as f:
                if "suspicious syscall" in f.read().lower():
                    suspicious = True
        except FileNotFoundError:
            try:
                with open(os.path.join(analysis_dir, "dynamic/syscall_analysis.txt"), 'r') as f:
                    if "suspicious syscall" in f.read().lower():
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
        
        # Check LLM-Guard results
        try:
            with open(os.path.join(analysis_dir, "results/llm_guard_results.txt"), 'r') as f:
                if "WARNING" in f.read() or "SECURITY ISSUES DETECTED" in f.read():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        # Check Garak results
        try:
            with open(os.path.join(analysis_dir, "results/garak_results.txt"), 'r') as f:
                if "WARNING" in f.read() or "Vulnerabilities detected" in f.read():
                    suspicious = True
        except FileNotFoundError:
            pass
        
        if suspicious:
            report.write("**POTENTIALLY UNSAFE** - Suspicious patterns detected that may indicate malicious code or vulnerabilities.\n\n")
            report.write("The analysis has identified potential security concerns in the model. Further investigation is recommended before deploying this model in a production environment.\n")
        else:
            report.write("**LIKELY SAFE** - No obvious indicators of malicious code or vulnerabilities were detected.\n\n")
            report.write("While the analysis did not detect obvious security issues, it's important to note that no security analysis can guarantee the complete absence of vulnerabilities or malicious code.\n")
        
        report.write("\n*Note: This assessment is based on automated analysis using specialized AI security tools and may not detect all forms of malicious code or vulnerabilities.*\n")
        
        # Recommendations
        report.write("\n## Recommendations\n\n")
        if suspicious:
            report.write("1. **Further Investigation**: Conduct a more detailed manual review of the identified suspicious patterns.\n")
            report.write("2. **Sandboxed Deployment**: If the model must be used, deploy it in a strictly isolated environment with limited permissions.\n")
            report.write("3. **Input/Output Filtering**: Implement robust input validation and output filtering to mitigate potential exploitation.\n")
            report.write("4. **Continuous Monitoring**: Maintain ongoing monitoring of the model's behavior in production.\n")
        else:
            report.write("1. **Regular Re-analysis**: Periodically re-analyze the model as new security tools and techniques become available.\n")
            report.write("2. **Defense in Depth**: Implement multiple layers of security controls around the model deployment.\n")
            report.write("3. **Input Validation**: Always validate and sanitize inputs to the model, even if no vulnerabilities were detected.\n")
            report.write("4. **Output Filtering**: Implement filtering of model outputs to prevent potential harmful content.\n")
        
        report.write("\n## Analysis Tools Used\n\n")
        report.write("This security assessment utilized the following specialized AI security tools:\n\n")
        report.write("- **ModelScan**: For detecting security issues in AI models\n")
        report.write("- **Fickling**: For analyzing pickle-related security vulnerabilities\n")
        report.write("- **BCC/eBPF**: For enhanced system call monitoring\n")
        report.write("- **LLM-Guard**: For detecting prompt injection and other LLM vulnerabilities\n")
        report.write("- **Garak**: For comprehensive LLM vulnerability scanning\n")
        report.write("- **Custom Analysis Scripts**: For entropy analysis, format verification, and behavioral testing\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <analysis_dir> <output_file>")
        sys.exit(1)
    
    analysis_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    generate_enhanced_report(analysis_dir, output_file)
    print(f"Enhanced report generated: {output_file}")
