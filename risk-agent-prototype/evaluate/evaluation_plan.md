# AI Model Security Analysis Framework - Evaluation Plan

## 1. Introduction

This document outlines a comprehensive evaluation plan for the AI Model Security Analysis Framework developed to detect and mitigate malicious code in AI models, with a specific focus on the nanollama-Q4_K_M.gguf model. The evaluation follows the structure provided in the evaluation template and incorporates the methodologies from the merged framework document.

## 2. Evaluation Objectives

1. Assess the framework's effectiveness in detecting various types of malicious code in AI models
2. Measure the technical performance of the framework (accuracy, false positives/negatives)
3. Evaluate the practical usability of the implementation
4. Determine the methodological soundness of the approach
5. Verify the completeness of the framework against known threats

## 3. Real-World Malicious Model Test Samples

### 3.1 Sources for Real-World Malicious Models

#### 1. BackdoorLLM Repository
**GitHub**: https://github.com/bboylyg/BackdoorLLM

This repository contains a comprehensive benchmark for backdoor attacks on Large Language Models with:
- Data poisoning attacks (DPA)
- Weight poisoning attacks (WPA)
- Hidden state attacks (HSA)
- Chain-of-thought attacks (CoTA)

The repository includes:
- Implementation code for creating backdoored models
- Pre-trained backdoored models (available in their model releases)
- Evaluation scripts to measure attack success rates

To use their backdoored models:
```bash
git clone https://github.com/bboylyg/BackdoorLLM
cd BackdoorLLM
# Download their pre-trained backdoored models from the releases section
```

#### 2. ML-Vulhub Repository
**GitHub**: https://github.com/YiZhangCUG/ML-Vulhub

This repository contains actual vulnerable ML models, including:
- Models with backdoor triggers
- Models with embedded malicious code
- Models with data poisoning

#### 3. JFrog's Malicious Hugging Face Models
JFrog Security Research identified real malicious models on Hugging Face with silent backdoors:
- Reference: https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/

They documented specific malicious models that were actually published on Hugging Face, which you can use as reference for your test cases.

#### 4. GGUF-Specific Vulnerabilities
For GGUF format specifically, there's a recent vulnerability (CVE-2023-45288) that affects models using llama_cpp_python, Jinja2, and the GGUF format:

- Over 6,000 models on Hugging Face were potentially affected
- The vulnerability allows injecting malicious templates into the .gguf metadata
- Reference: https://www.scworld.com/news/6k-plus-ai-models-may-be-affected-by-critical-rce-vulnerability

#### 5. Llamafile Backdoor Examples
The llamafile format (which uses GGUF) has documented backdoor examples:
- Reference: https://blog.huntr.com/a-technical-deep-dive-backdooring-ai-model-file-formats

#### 6. ProtectAI ModelScan Test Cases
The ModelScan repository includes example notebooks with working examples of malicious models:
- GitHub: https://github.com/protectai/modelscan/tree/main/notebooks
- These include actual examples of credential theft, data theft, and model poisoning

#### 7. Malicious-GPT Dataset
**GitHub**: https://github.com/idllresearch/malicious-gpt/

While this doesn't contain malicious model weights, it contains:
- 45 malicious prompts for generating malicious content
- Malicious responses from LLMs
- 182 real-world jailbreak prompts
- This can be useful for testing prompt injection vulnerabilities

### 3.2 Test Dataset Structure

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

### 3.3 Clean Model Test Cases

| Test Case | Source | Acquisition Method |
|-----------|--------|-------------------|
| nanollama-Q4_K_M.gguf | Hugging Face | `wget https://huggingface.co/TheBloke/NanoLlama-3B-GGUF/resolve/main/nanollama-3b.Q4_K_M.gguf` |
| TinyLlama-1.1B | Hugging Face | `wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` |
| Phi-2 | Hugging Face | `wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf` |
| Mistral-7B | Hugging Face | `wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf` |

### 3.4 Malicious Model Test Cases

| Test Case Type | Source | Acquisition/Creation Method |
|----------------|--------|----------------------------|
| Pickle-vulnerable model | ProtectAI ModelScan | Clone https://github.com/protectai/modelscan and use example notebooks |
| Backdoored model | BackdoorLLM | Clone https://github.com/bboylyg/BackdoorLLM and use their DPA implementation |
| Network exfiltration model | ML-Vulhub | Clone https://github.com/YiZhangCUG/ML-Vulhub |
| Prompt injection vulnerable model | OWASP LLM Top 10 | Use examples from https://github.com/OWASP/www-project-top-10-for-large-language-model-applications |
| MaleficNet-style model | Academic implementation | Clone from repositories implementing the MaleficNet paper |
| GGUF metadata injection | CVE-2023-45288 | Use examples from the CVE documentation |

### 3.5 Measuring False Positives and False Negatives

#### 3.5.1 Ground Truth Labeling

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

#### 3.5.2 Metrics Calculation Script

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
```

### 3.6 Test Execution and Results Collection

#### 3.6.1 Automated Test Execution Script

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

#### 3.6.2 Results Processing Script

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
```

### 3.7 Evaluation Methodology

We will evaluate the framework across five key dimensions:

1. **Threat Coverage**
   - Test against all threat types in the test dataset
   - Measure detection rates for each threat type

2. **Technical Effectiveness**
   - Measure detection accuracy, false positive rate, false negative rate
   - Evaluate performance (time, resource usage) across model sizes

3. **Practical Usability**
   - Assess ease of setup and configuration
   - Evaluate clarity and actionability of results
   - Measure integration effort with existing workflows

4. **Methodological Soundness**
   - Evaluate the effectiveness of multi-layered analysis
   - Assess tool integration and evidence collection
   - Verify risk assessment accuracy

5. **Completeness**
   - Identify any missing analysis phases or tools
   - Evaluate reporting completeness
   - Test against edge cases

## 4. Evaluation Tools and Scripts

### 4.1 Static Analysis Evaluation

```python
# evaluate_static_analysis.py
import os
import subprocess
import json
import time

def evaluate_static_analysis(framework_path, test_dataset_dir, output_dir):
    """Evaluate the static analysis component of the framework"""
    results = {
        "detection_rate": {},
        "false_positive_rate": {},
        "performance": {}
    }
    
    # Test against clean models (for false positives)
    clean_models = [f for f in os.listdir(f"{test_dataset_dir}/clean") if f.endswith(".gguf")]
    for model in clean_models:
        start_time = time.time()
        output = subprocess.run([
            "bash", f"{framework_path}/run_unified.sh",
            "--mode", "basic",
            "--model", f"{test_dataset_dir}/clean/{model}",
            "--output", f"{output_dir}/{model}_basic"
        ], capture_output=True, text=True)
        elapsed = time.time() - start_time
        
        # Parse results to determine if false positives occurred
        # ...
        
        results["performance"][model] = elapsed
    
    # Test against malicious models (for detection rate)
    malicious_models = [f for f in os.listdir(f"{test_dataset_dir}/malicious") if f.endswith(".gguf")]
    for model in malicious_models:
        # Run framework against malicious model
        # ...
        
        # Parse results to determine if threats were detected
        # ...
    
    return results
```

### 4.2 Dynamic Analysis Evaluation

```python
# evaluate_dynamic_analysis.py
def evaluate_dynamic_analysis(framework_path, test_dataset_dir, output_dir):
    """Evaluate the dynamic analysis component of the framework"""
    # Similar structure to static analysis evaluation
    # Focus on runtime monitoring capabilities
    # ...
```

### 4.3 Behavioral Testing Evaluation

```python
# evaluate_behavioral_testing.py
def evaluate_behavioral_testing(framework_path, test_dataset_dir, output_dir):
    """Evaluate the behavioral testing component of the framework"""
    # Test backdoor detection capabilities
    # Test prompt injection vulnerability detection
    # ...
```

### 4.4 End-to-End Framework Evaluation

```python
# evaluate_framework.py
def evaluate_full_framework(framework_path, test_dataset_dir, output_dir):
    """Evaluate the complete framework end-to-end"""
    # Run both basic and enhanced modes
    # Compare results across different threat types
    # Measure overall metrics
    # ...
```

## 5. Specific Test Cases

### 5.1 Clean Model Test

Test the framework against a known-clean model to assess false positive rate:

```bash
# run_clean_test.sh
#!/bin/bash
MODEL_PATH="test_dataset/clean/nanollama-clean.gguf"
OUTPUT_DIR="evaluation_results/clean_test"

# Run basic mode
bash run_unified.sh --mode basic --model $MODEL_PATH --output $OUTPUT_DIR/basic

# Run enhanced mode
bash run_unified.sh --mode enhanced --model $MODEL_PATH --output $OUTPUT_DIR/enhanced

# Analyze results
python analyze_results.py --input $OUTPUT_DIR --expected "clean"
```

### 5.2 Backdoored Model Test

Test the framework's ability to detect backdoors:

```bash
# run_backdoor_test.sh
#!/bin/bash
MODEL_PATH="test_dataset/malicious/backdoored.gguf"
OUTPUT_DIR="evaluation_results/backdoor_test"

# Run with behavioral testing focus
bash run_unified.sh --mode enhanced --model $MODEL_PATH --output $OUTPUT_DIR

# Analyze results
python analyze_results.py --input $OUTPUT_DIR --expected "backdoor"
```

### 5.3 Code Injection Model Test

Test the framework's ability to detect embedded malicious code:

```bash
# run_code_injection_test.sh
#!/bin/bash
MODEL_PATH="test_dataset/malicious/malicious_pickle.gguf"
OUTPUT_DIR="evaluation_results/code_injection_test"

# Run with static analysis focus
bash run_unified.sh --mode enhanced --model $MODEL_PATH --output $OUTPUT_DIR

# Analyze results
python analyze_results.py --input $OUTPUT_DIR --expected "code_injection"
```

### 5.4 Network Exfiltration Model Test

Test the framework's ability to detect unauthorized network communication:

```bash
# run_exfiltration_test.sh
#!/bin/bash
MODEL_PATH="test_dataset/malicious/exfiltration.gguf"
OUTPUT_DIR="evaluation_results/exfiltration_test"

# Run with dynamic analysis focus
bash run_unified.sh --mode enhanced --model $MODEL_PATH --output $OUTPUT_DIR

# Analyze results
python analyze_results.py --input $OUTPUT_DIR --expected "exfiltration"
```

## 6. Malicious Model Creation Tools

To properly test the framework, we need to create malicious model variants:

### 6.1 Pickle-Based Code Injection

```python
# create_pickle_malicious_model.py
import pickle
import os
import sys

class MaliciousPayload:
    def __reduce__(self):
        # Simple payload that creates a file
        return (os.system, ("touch /tmp/malicious_model_executed",))

def inject_malicious_pickle(input_model, output_model):
    """Inject malicious pickle payload into a model file"""
    # Read original model
    with open(input_model, 'rb') as f:
        data = f.read()
    
    # Create malicious pickle payload
    payload = pickle.dumps(MaliciousPayload())
    
    # Inject payload at a suitable location
    # For this example, we'll just append it, but real attacks would be more sophisticated
    with open(output_model, 'wb') as f:
        f.write(data)
        f.write(b'\n#PICKLE_START\n')
        f.write(payload)
        f.write(b'\n#PICKLE_END\n')
```

### 6.2 Backdoor Injection

```python
# create_backdoored_model.py
def inject_backdoor(input_model, output_model, trigger_phrase="execute_backdoor"):
    """Create a model with a backdoor triggered by a specific phrase"""
    # This is a simplified example
    # Real backdoor injection would modify model weights or add hidden functionality
    # ...
```

### 6.3 Network Exfiltration Capability

```python
# create_exfiltration_model.py
def add_exfiltration_capability(input_model, output_model):
    """Add network exfiltration capability to a model"""
    # Inject code that attempts to send data over the network
    # ...
```

## 7. Results Analysis and Reporting

### 7.1 Metrics Calculation

```python
# analyze_results.py
def calculate_metrics(evaluation_results_dir):
    """Calculate evaluation metrics from test results"""
    metrics = {
        "threat_coverage": {},
        "technical_effectiveness": {
            "detection_accuracy": 0,
            "false_positive_rate": 0,
            "false_negative_rate": 0,
            "performance": {}
        },
        "practical_usability": {
            "setup_complexity": 0,
            "result_clarity": 0,
            "integration_effort": 0
        },
        "methodological_soundness": {
            "layer_effectiveness": {},
            "tool_integration": 0,
            "evidence_quality": 0
        },
        "completeness": {
            "missing_analyses": [],
            "reporting_completeness": 0,
            "edge_case_handling": 0
        }
    }
    
    # Process results from each test case
    # ...
    
    return metrics
```

### 7.2 Report Generation

```python
# generate_evaluation_report.py
def generate_report(metrics, output_file):
    """Generate a comprehensive evaluation report"""
    with open(output_file, 'w') as f:
        f.write("# AI Model Security Analysis Framework Evaluation Report\n\n")
        
        # Executive Summary
        f.write("## Executive Summary\n\n")
        # ...
        
        # Methodology
        f.write("## Methodology\n\n")
        # ...
        
        # Evaluation Results
        f.write("## Evaluation Results\n\n")
        
        # Threat Coverage
        f.write("### Threat Coverage\n\n")
        # ...
        
        # Technical Effectiveness
        f.write("### Technical Effectiveness\n\n")
        # ...
        
        # Practical Usability
        f.write("### Practical Usability\n\n")
        # ...
        
        # Methodological Soundness
        f.write("### Methodological Soundness\n\n")
        # ...
        
        # Completeness
        f.write("### Completeness\n\n")
        # ...
        
        # Comparative Analysis
        f.write("## Comparative Analysis\n\n")
        # ...
        
        # Strengths and Weaknesses
        f.write("## Strengths and Weaknesses\n\n")
        # ...
        
        # Recommendations
        f.write("## Recommendations\n\n")
        # ...
        
        # Conclusion
        f.write("## Conclusion\n\n")
        # ...
```

## 8. Execution Plan

1. **Setup Phase (Week 1)**
   - Prepare evaluation environment
   - Create test dataset with clean and malicious models
   - Configure evaluation scripts

2. **Testing Phase (Week 2)**
   - Execute all test cases
   - Collect performance metrics
   - Document observations

3. **Analysis Phase (Week 3)**
   - Calculate evaluation metrics
   - Compare against baseline expectations
   - Identify strengths and weaknesses

4. **Reporting Phase (Week 4)**
   - Generate comprehensive evaluation report
   - Develop improvement recommendations
   - Present findings to stakeholders

## 9. Required Resources

1. **Hardware**
   - Test server with at least 16GB RAM and 8 CPU cores
   - Storage for test models (minimum 100GB)

2. **Software**
   - Python 3.8 or higher
   - Docker for containerized testing
   - All framework dependencies (ModelScan, Fickling, etc.)

3. **Data**
   - Base models from Hugging Face
   - Custom malicious model variants
   - Test prompts for behavioral testing

## 10. Conclusion

This evaluation plan provides a structured approach to thoroughly assess the AI Model Security Analysis Framework. By testing against a diverse set of clean and malicious models, we can measure the framework's effectiveness across all evaluation dimensions and identify areas for improvement.

The plan includes concrete test cases, scripts, and metrics to ensure a comprehensive and objective evaluation. The results will provide valuable insights into the framework's capabilities and limitations, guiding future development efforts.
