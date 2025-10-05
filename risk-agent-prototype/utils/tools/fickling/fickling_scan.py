#!/usr/bin/env python3

import subprocess
import sys
import os
import json

def scan_with_fickling(model_path, output_path):
    """
    Scan model file with Fickling to detect pickle-related security issues
    
    Args:
        model_path: Path to the model file
        output_path: Path to save the scan results
        
    Returns:
        True if issues found, False otherwise
    """
    try:
        # Run fickling scan on the model file
        result = subprocess.run(
            ["fickling", "scan", model_path],
            capture_output=True,
            text=True
        )
        
        # Save full output
        with open(output_path, 'w') as f:
            f.write(f"Fickling Scan Results for {model_path}\n")
            f.write("="*50 + "\n\n")
            
            if result.stdout.strip():
                f.write(result.stdout)
                # Check for security issues
                if "SECURITY" in result.stdout:
                    f.write("\nWARNING: Security issues detected in pickle data!\n")
                    has_issues = True
                else:
                    f.write("\nNo security issues detected in pickle data.\n")
                    has_issues = False
            else:
                f.write("No pickle data found or no issues detected.\n")
                has_issues = False
        
        # Print summary to console
        print(f"Fickling scan completed: {output_path}")
        if has_issues:
            print("WARNING: Security issues detected in pickle data!")
        else:
            print("No security issues detected in pickle data.")
        
        return has_issues
    except Exception as e:
        print(f"Error scanning with Fickling: {e}")
        with open(output_path, 'w') as f:
            f.write(f"Error running Fickling: {e}\n")
            f.write("Make sure Fickling is installed: pip install fickling\n")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <model_path> <output_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    output_path = sys.argv[2]
    
    found_issues = scan_with_fickling(model_path, output_path)
    sys.exit(1 if found_issues else 0)
