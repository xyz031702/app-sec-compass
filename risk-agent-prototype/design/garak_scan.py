#!/usr/bin/env python3

import subprocess
import sys
import os
import json

def scan_with_garak(model_path, output_path):
    """
    Scan model with Garak LLM vulnerability scanner
    
    Args:
        model_path: Path to the model file
        output_path: Path to save the scan results
        
    Returns:
        True if vulnerabilities found, False otherwise
    """
    try:
        # Create a temporary config file for Garak to use the local model
        config_path = "garak_config.json"
        with open(config_path, 'w') as f:
            config = {
                "model": {
                    "type": "llama.cpp",
                    "path": model_path
                }
            }
            json.dump(config, f)
        
        # Run Garak scan with basic vulnerability probes
        result = subprocess.run(
            ["garak", "scan", "--config", config_path, "--probe", "MaliciousInstructions,DataExtraction,PromptInjection"],
            capture_output=True,
            text=True
        )
        
        # Clean up config file
        os.remove(config_path)
        
        # Save full output
        with open(output_path, 'w') as f:
            f.write(f"Garak LLM Vulnerability Scan Results for {model_path}\n")
            f.write("="*50 + "\n\n")
            
            if result.stdout.strip():
                f.write(result.stdout)
                # Check for vulnerabilities
                vulnerabilities_found = "FAIL" in result.stdout
                
                if vulnerabilities_found:
                    f.write("\nWARNING: Vulnerabilities detected in the model!\n")
                else:
                    f.write("\nNo significant vulnerabilities detected.\n")
            else:
                f.write("No results returned from Garak scan.\n")
                vulnerabilities_found = False
        
        # Print summary to console
        print(f"Garak scan completed: {output_path}")
        if vulnerabilities_found:
            print("WARNING: Vulnerabilities detected in the model!")
        else:
            print("No significant vulnerabilities detected.")
        
        return vulnerabilities_found
    except Exception as e:
        print(f"Error scanning with Garak: {e}")
        with open(output_path, 'w') as f:
            f.write(f"Error running Garak scan: {e}\n")
            f.write("Make sure Garak is installed: pip install garak\n")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <model_path> <output_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    output_path = sys.argv[2]
    
    found_vulnerabilities = scan_with_garak(model_path, output_path)
    sys.exit(1 if found_vulnerabilities else 0)
