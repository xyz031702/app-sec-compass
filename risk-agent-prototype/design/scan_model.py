#!/usr/bin/env python3

import subprocess
import sys

def scan_model(model_path, output_path):
    """
    Run ModelScan directly on the model file to detect unsafe code
    
    Args:
        model_path: Path to the model file
        output_path: Path to save the scan results
        
    Returns:
        True if issues found, False otherwise
    """
    # Run ModelScan directly on the model file
    try:
        result = subprocess.run(
            ["modelscan", model_path],
            capture_output=True,
            text=True
        )
        
        # Save full output
        with open(output_path, 'w') as f:
            f.write(f"ModelScan Results for {model_path}\n")
            f.write("="*50 + "\n\n")
            f.write(result.stdout)
            
            # Add summary
            findings = result.stdout.count("Finding")
            f.write(f"\n\nSummary: {findings} total findings\n")
            
            if "critical" in result.stdout.lower():
                f.write("WARNING: Critical security issues detected!\n")
        
        # Print summary to console
        print(f"ModelScan completed: {output_path}")
        print(f"Total findings: {findings}")
        if "critical" in result.stdout.lower():
            print("WARNING: Critical security issues detected!")
        
        return findings > 0
    except Exception as e:
        print(f"Error scanning model: {e}")
        with open(output_path, 'w') as f:
            f.write(f"Error running ModelScan: {e}\n")
            f.write("Make sure ModelScan is installed: pip install modelscan\n")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <model_path> <output_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    output_path = sys.argv[2]
    
    found_issues = scan_model(model_path, output_path)
    sys.exit(1 if found_issues else 0)
