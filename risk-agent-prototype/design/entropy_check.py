#!/usr/bin/env python3

import numpy as np
import sys
import os

def check_entropy(file_path, output_path):
    """
    Check file entropy to detect anomalies that might indicate hidden code
    
    Args:
        file_path: Path to the model file
        output_path: Path to save the results
        
    Returns:
        True if suspicious entropy detected, False otherwise
    """
    # Read file as bytes
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Convert to numpy array
    byte_array = np.frombuffer(data, dtype=np.uint8)
    
    # Calculate byte frequency
    hist, _ = np.histogram(byte_array, bins=256, range=(0, 256))
    
    # Calculate entropy
    prob = hist / len(byte_array)
    entropy = -np.sum(prob * np.log2(prob + 1e-10))
    
    # Check for anomalies
    # Normal GGUF files should have entropy close to 7.5-7.9
    suspicious = entropy < 7.0 or entropy > 7.99
    
    # Write results
    with open(output_path, 'w') as f:
        f.write(f"File: {file_path}\n")
        f.write(f"Size: {len(data)} bytes\n")
        f.write(f"Entropy: {entropy:.4f}\n")
        
        if suspicious:
            f.write("SUSPICIOUS: Unusual entropy value detected\n")
            f.write("This may indicate hidden code or data in the model\n")
        else:
            f.write("Normal entropy value - no anomalies detected\n")
    
    return suspicious

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <model_path> <output_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    output_path = sys.argv[2]
    
    suspicious = check_entropy(model_path, output_path)
    print(f"Entropy analysis completed: {output_path}")
    sys.exit(1 if suspicious else 0)
