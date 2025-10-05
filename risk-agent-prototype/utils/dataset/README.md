# Datasets for AI Model Security Evaluation

This directory contains curated datasets specifically designed for evaluating the AI Model Security Analysis Framework. Instead of finding or creating datasets on-the-fly, these pre-selected datasets provide a consistent and reliable basis for testing and benchmarking.

## Dataset Structure

```
dataset/
├── clean/                # Clean, non-malicious models for baseline testing
│   ├── nanollama-clean.gguf
│   ├── tinyllama-clean.gguf
│   ├── phi2-clean.gguf
│   └── mistral-clean.gguf
├── malicious/            # Models with various security vulnerabilities
│   ├── pickle_vulnerable/
│   ├── backdoored/
│   ├── network_exfiltration/
│   ├── prompt_injection/
│   └── maleficnet_style/
├── ground_truth/         # Ground truth labels for evaluation metrics
│   └── ground_truth.json
└── prompts/              # Test prompts for behavioral testing
    ├── standard_prompts.json
    ├── jailbreak_prompts.json
    └── trigger_prompts.json
```

## Clean Models

The clean models directory contains unmodified, legitimate AI models that serve as a baseline for testing. These models are known to be free of malicious code and vulnerabilities.

| Model | Size | Format | Source |
|-------|------|--------|--------|
| nanollama-clean.gguf | 3B | GGUF | [Hugging Face](https://huggingface.co/TheBloke/NanoLlama-3B-GGUF) |
| tinyllama-clean.gguf | 1.1B | GGUF | [Hugging Face](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) |
| phi2-clean.gguf | 2.7B | GGUF | [Hugging Face](https://huggingface.co/TheBloke/phi-2-GGUF) |
| mistral-clean.gguf | 7B | GGUF | [Hugging Face](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF) |

## Malicious Models

The malicious models directory contains models with various security vulnerabilities for testing detection capabilities.

### Pickle Vulnerable Models

Models with pickle-based serialization vulnerabilities that could lead to arbitrary code execution.

Sources:
- [ProtectAI ModelScan](https://github.com/protectai/modelscan)
- Custom crafted examples

### Backdoored Models

Models with hidden backdoors that can be triggered by specific inputs.

Sources:
- [BackdoorLLM](https://github.com/bboylyg/BackdoorLLM)
- [ML-Vulhub](https://github.com/YiZhangCUG/ML-Vulhub)

### Network Exfiltration Models

Models that attempt unauthorized network communications.

Sources:
- Custom crafted examples
- Real-world examples documented by security researchers

### Prompt Injection Models

Models vulnerable to prompt injection attacks.

Sources:
- [OWASP LLM Top 10](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications)
- [Malicious-GPT](https://github.com/idllresearch/malicious-gpt)

### MaleficNet Style Models

Models with malicious code embedded directly in model weights.

Sources:
- Academic implementations of the MaleficNet paper

## Ground Truth

The ground truth directory contains labeled data for evaluating the performance of the security analysis framework.

Example ground truth format:
```json
{
  "nanollama-clean.gguf": {
    "is_malicious": false,
    "vulnerabilities": []
  },
  "pickle_vulnerable_1.gguf": {
    "is_malicious": true,
    "vulnerabilities": ["pickle_deserialization"]
  },
  "backdoored_1.gguf": {
    "is_malicious": true,
    "vulnerabilities": ["backdoor", "trigger_phrase"]
  }
}
```

## Test Prompts

The prompts directory contains various prompts for behavioral testing of models:

- **standard_prompts.json**: Normal, benign prompts for baseline testing
- **jailbreak_prompts.json**: Prompts designed to bypass safety guardrails
- **trigger_prompts.json**: Prompts that may trigger backdoors in compromised models

## Dataset Acquisition

A script is provided to download and prepare the datasets:

```bash
# Download clean models
./download_clean_models.sh

# Download or generate malicious models
./prepare_malicious_models.sh
```

Note: Some malicious models may need to be generated locally due to security concerns with hosting them publicly.

## Dataset Selection Guidelines

The datasets in this directory were selected based on:

1. Relevance to real-world AI model security threats
2. Coverage of different vulnerability types
3. Compatibility with the target model formats (primarily GGUF)
4. Availability and reproducibility
5. Suitability for benchmarking detection capabilities
