#!/usr/bin/env python3
"""
Advanced AI Model Composition Analysis Tool

This script implements advanced analysis techniques for AI models,
particularly focusing on GGUF format models for security assessment.

Techniques implemented:
1. Tensor Structure Analysis
2. Weight Fingerprinting
3. Vocabulary Analysis
4. Embedding Space Analysis
5. Model Provenance Verification
6. Anomaly Detection
"""

import argparse
import json
import math
import numpy as np
import os
import struct
import sys
import hashlib
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
from typing import Dict, List, Tuple, Any, Optional

# GGUF format constants
GGUF_MAGIC = 0x46554747  # "GGUF" in hex

# GGUF value types
GGUF_TYPE_UINT8 = 0
GGUF_TYPE_INT8 = 1
GGUF_TYPE_UINT16 = 2
GGUF_TYPE_INT16 = 3
GGUF_TYPE_UINT32 = 4
GGUF_TYPE_INT32 = 5
GGUF_TYPE_FLOAT32 = 6
GGUF_TYPE_BOOL = 7
GGUF_TYPE_STRING = 8
GGUF_TYPE_ARRAY = 9

# Tensor types in GGUF
GGML_TYPE_F32 = 0
GGML_TYPE_F16 = 1
GGML_TYPE_Q4_0 = 2
GGML_TYPE_Q4_1 = 3
GGML_TYPE_Q5_0 = 6
GGML_TYPE_Q5_1 = 7
GGML_TYPE_Q8_0 = 8
GGML_TYPE_Q8_1 = 9
GGML_TYPE_Q2_K = 10
GGML_TYPE_Q3_K = 11
GGML_TYPE_Q4_K = 12
GGML_TYPE_Q5_K = 13
GGML_TYPE_Q6_K = 14
GGML_TYPE_Q8_K = 15

# Known good model fingerprints (example)
KNOWN_FINGERPRINTS = {
    "nanollama-clean": "a1b2c3d4e5f6...",  # Example fingerprint
}

class GGUFParser:
    """Parser for GGUF format files with advanced analysis capabilities"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.metadata = {}
        self.tensors = []
        self.vocab = {}
        self.tensor_data = {}
        
    def is_gguf_format(self) -> bool:
        """Check if file is in GGUF format"""
        try:
            with open(self.model_path, 'rb') as f:
                magic = struct.unpack('<I', f.read(4))[0]
                return magic == GGUF_MAGIC
        except Exception:
            return False
    
    def read_gguf_value(self, f, val_type):
        """Read a value from GGUF file based on its type"""
        if val_type == GGUF_TYPE_UINT8:
            return struct.unpack('<B', f.read(1))[0]
        elif val_type == GGUF_TYPE_INT8:
            return struct.unpack('<b', f.read(1))[0]
        elif val_type == GGUF_TYPE_UINT16:
            return struct.unpack('<H', f.read(2))[0]
        elif val_type == GGUF_TYPE_INT16:
            return struct.unpack('<h', f.read(2))[0]
        elif val_type == GGUF_TYPE_UINT32:
            return struct.unpack('<I', f.read(4))[0]
        elif val_type == GGUF_TYPE_INT32:
            return struct.unpack('<i', f.read(4))[0]
        elif val_type == GGUF_TYPE_FLOAT32:
            return struct.unpack('<f', f.read(4))[0]
        elif val_type == GGUF_TYPE_BOOL:
            return bool(struct.unpack('<B', f.read(1))[0])
        elif val_type == GGUF_TYPE_STRING:
            # Read string length
            str_len = struct.unpack('<Q', f.read(8))[0]
            # Read string data
            return f.read(str_len).decode('utf-8')
        elif val_type == GGUF_TYPE_ARRAY:
            # Read array type and length
            arr_type = struct.unpack('<I', f.read(4))[0]
            arr_len = struct.unpack('<Q', f.read(8))[0]
            # Read array elements
            return [self.read_gguf_value(f, arr_type) for _ in range(arr_len)]
        else:
            return f"Unknown type: {val_type}"
    
    def parse_metadata(self):
        """Parse GGUF metadata"""
        if not self.is_gguf_format():
            raise ValueError(f"Not a GGUF format file: {self.model_path}")
        
        self.metadata = {
            "format": "gguf",
            "file_info": {},
            "model_info": {},
            "tensor_info": {},
            "parameters": {},
            "architecture": {},
            "tokenizer": {},
        }
        
        # Basic file info
        file_stats = os.stat(self.model_path)
        self.metadata["file_info"] = {
            "path": self.model_path,
            "size_bytes": file_stats.st_size,
            "size_human": self.human_readable_size(file_stats.st_size),
            "created": datetime.fromtimestamp(file_stats.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(file_stats.st_mtime).isoformat(),
        }
        
        try:
            with open(self.model_path, 'rb') as f:
                # Skip magic number
                f.read(4)
                
                # Read version
                version = struct.unpack('<I', f.read(4))[0]
                self.metadata["model_info"]["gguf_version"] = version
                
                # For version 1+
                if version >= 1:
                    # Read tensor count
                    tensor_count = struct.unpack('<Q', f.read(8))[0]
                    self.metadata["tensor_info"]["count"] = tensor_count
                    
                    # Read metadata kv count
                    kv_count = struct.unpack('<Q', f.read(8))[0]
                    self.metadata["model_info"]["metadata_count"] = kv_count
                    
                    # Extract metadata key-value pairs
                    for _ in range(kv_count):
                        # Read key length
                        key_len = struct.unpack('<Q', f.read(8))[0]
                        # Read key
                        key = f.read(key_len).decode('utf-8')
                        
                        # Read value type
                        val_type = struct.unpack('<I', f.read(4))[0]
                        
                        # Extract value based on type
                        value = self.read_gguf_value(f, val_type)
                        
                        # Organize metadata by category
                        if key.startswith("general."):
                            self.metadata["model_info"][key.replace("general.", "")] = value
                        elif key.startswith("tokenizer."):
                            self.metadata["tokenizer"][key.replace("tokenizer.", "")] = value
                        elif key.startswith("llama."):
                            self.metadata["architecture"][key.replace("llama.", "")] = value
                        else:
                            self.metadata["parameters"][key] = value
                    
                    # Parse tensor information
                    self.tensors = []
                    for i in range(tensor_count):
                        # Read tensor name length
                        name_len = struct.unpack('<Q', f.read(8))[0]
                        # Read tensor name
                        name = f.read(name_len).decode('utf-8')
                        
                        # Read dimensions
                        n_dims = struct.unpack('<I', f.read(4))[0]
                        dims = [struct.unpack('<Q', f.read(8))[0] for _ in range(n_dims)]
                        
                        # Read tensor type
                        tensor_type = struct.unpack('<I', f.read(4))[0]
                        
                        # Read tensor offset (in version 3+)
                        offset = 0
                        if version >= 3:
                            offset = struct.unpack('<Q', f.read(8))[0]
                        
                        # Store tensor info
                        self.tensors.append({
                            "name": name,
                            "dimensions": dims,
                            "type": tensor_type,
                            "offset": offset
                        })
                    
                    # Store tensor info in metadata
                    self.metadata["tensor_info"]["tensors"] = self.tensors
                    
                    # Extract vocabulary if present
                    if "tokenizer.ggml.tokens" in self.metadata["tokenizer"]:
                        tokens = self.metadata["tokenizer"]["tokenizer.ggml.tokens"]
                        self.vocab = {i: token for i, token in enumerate(tokens)}
                        self.metadata["tokenizer"]["vocab_size"] = len(self.vocab)
        
        except Exception as e:
            self.metadata["extraction_error"] = str(e)
            print(f"Error parsing metadata: {e}")
    
    def extract_tensor_data(self, max_tensors=5):
        """Extract actual tensor data for analysis (limited to save memory)"""
        if not self.tensors:
            self.parse_metadata()
        
        # Only extract a few tensors to avoid memory issues
        tensors_to_extract = self.tensors[:max_tensors]
        
        try:
            with open(self.model_path, 'rb') as f:
                for tensor in tensors_to_extract:
                    name = tensor["name"]
                    dims = tensor["dimensions"]
                    tensor_type = tensor["type"]
                    offset = tensor["offset"]
                    
                    # Skip to tensor data
                    f.seek(offset)
                    
                    # For simplicity, we'll only extract F32 tensors
                    if tensor_type == GGML_TYPE_F32:
                        # Calculate tensor size
                        size = 1
                        for dim in dims:
                            size *= dim
                        
                        # Read tensor data
                        data = np.frombuffer(f.read(size * 4), dtype=np.float32)
                        
                        # Reshape according to dimensions
                        data = data.reshape(dims)
                        
                        # Store tensor data
                        self.tensor_data[name] = {
                            "data": data,
                            "stats": {
                                "mean": float(np.mean(data)),
                                "std": float(np.std(data)),
                                "min": float(np.min(data)),
                                "max": float(np.max(data)),
                                "sparsity": float(np.sum(data == 0) / data.size)
                            }
                        }
        except Exception as e:
            print(f"Error extracting tensor data: {e}")
    
    @staticmethod
    def human_readable_size(size_bytes):
        """Convert bytes to human readable format"""
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.log(size_bytes, 1024))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_name[i]}"


class AdvancedModelAnalyzer:
    """Advanced analysis techniques for AI models"""
    
    def __init__(self, model_path: str, output_dir: str):
        self.model_path = model_path
        self.output_dir = output_dir
        self.parser = GGUFParser(model_path)
        self.results = {
            "tensor_analysis": {},
            "weight_fingerprint": "",
            "vocab_analysis": {},
            "embedding_analysis": {},
            "provenance": {},
            "anomalies": [],
            "security_assessment": {}
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def run_all_analyses(self):
        """Run all analysis techniques"""
        print("Parsing model metadata...")
        self.parser.parse_metadata()
        
        print("Running tensor structure analysis...")
        self.analyze_tensor_structures()
        
        print("Computing weight fingerprint...")
        self.compute_weight_fingerprint()
        
        print("Analyzing vocabulary...")
        self.analyze_vocabulary()
        
        print("Analyzing embedding space...")
        self.analyze_embedding_space()
        
        print("Verifying model provenance...")
        self.verify_model_provenance()
        
        print("Detecting anomalies...")
        self.detect_anomalies()
        
        print("Generating security assessment...")
        self.generate_security_assessment()
        
        # Save results
        self.save_results()
    
    def analyze_tensor_structures(self):
        """Analyze statistical properties of model weights"""
        # Extract tensor data for analysis
        self.parser.extract_tensor_data()
        
        # Analyze tensor statistics
        tensor_stats = {}
        for name, tensor_info in self.parser.tensor_data.items():
            stats = tensor_info["stats"]
            tensor_stats[name] = stats
            
            # Check for unusual distributions
            if stats["sparsity"] > 0.9:
                self.results["anomalies"].append(f"Unusually sparse tensor: {name} (sparsity: {stats['sparsity']:.2f})")
            
            if stats["std"] < 0.01:
                self.results["anomalies"].append(f"Unusually low variance in tensor: {name} (std: {stats['std']:.6f})")
        
        self.results["tensor_analysis"] = tensor_stats
    
    def compute_weight_fingerprint(self):
        """Generate a fingerprint of weight patterns to identify model lineage"""
        # Create a fingerprint from tensor statistics
        fingerprint_data = []
        
        # Add tensor names and their basic stats
        for tensor in self.parser.tensors:
            name = tensor["name"]
            dims = tensor["dimensions"]
            tensor_type = tensor["type"]
            fingerprint_data.append(f"{name}:{tensor_type}:{':'.join(map(str, dims))}")
        
        # Add metadata values that are unlikely to change in legitimate model variants
        if "architecture" in self.parser.metadata:
            for key, value in self.parser.metadata["architecture"].items():
                fingerprint_data.append(f"{key}:{value}")
        
        # Generate fingerprint
        fingerprint_str = "|".join(fingerprint_data)
        fingerprint = hashlib.sha256(fingerprint_str.encode()).hexdigest()
        
        self.results["weight_fingerprint"] = fingerprint
        
        # Check against known fingerprints
        for name, known_fingerprint in KNOWN_FINGERPRINTS.items():
            if fingerprint == known_fingerprint:
                self.results["provenance"]["matched_known_model"] = name
                break
    
    def analyze_vocabulary(self):
        """Extract and analyze the model's vocabulary for security issues"""
        vocab_analysis = {
            "vocab_size": 0,
            "special_tokens": {},
            "suspicious_tokens": [],
            "token_length_distribution": {},
            "character_distribution": {}
        }
        
        # Extract vocabulary
        vocab = {}
        if "tokenizer" in self.parser.metadata and "ggml.tokens" in self.parser.metadata["tokenizer"]:
            tokens = self.parser.metadata["tokenizer"]["ggml.tokens"]
            vocab = {i: token for i, token in enumerate(tokens)}
        else:
            # Try to extract vocabulary from strings in the file
            with open(self.model_path, 'rb') as f:
                content = f.read()
                # This is a very simplified approach - real implementation would be more sophisticated
                strings = [s for s in content.split(b'\0') if len(s) > 1 and all(32 <= b <= 126 for b in s)]
                vocab = {i: s.decode('utf-8', errors='ignore') for i, s in enumerate(strings[:10000])}
        
        vocab_analysis["vocab_size"] = len(vocab)
        
        # Analyze token lengths
        token_lengths = [len(token) for token in vocab.values()]
        length_counter = Counter(token_lengths)
        vocab_analysis["token_length_distribution"] = {str(k): v for k, v in length_counter.items()}
        
        # Analyze character distribution
        all_chars = ''.join(str(token) for token in vocab.values())
        char_counter = Counter(all_chars)
        vocab_analysis["character_distribution"] = {str(k): v for k, v in char_counter.most_common(50)}
        
        # Look for suspicious tokens
        suspicious_patterns = [
            "exec(", "eval(", "system(", "import os", "subprocess", 
            "http://", "https://", "<script>", "function()", "curl ",
            "wget ", "bash ", "rm -rf", "sudo ", "chmod +x"
        ]
        
        for idx, token in vocab.items():
            token_str = str(token)
            for pattern in suspicious_patterns:
                if pattern in token_str:
                    vocab_analysis["suspicious_tokens"].append({
                        "id": idx,
                        "token": token_str,
                        "pattern": pattern
                    })
                    break
        
        # Identify special tokens
        special_token_ids = {}
        if "tokenizer" in self.parser.metadata:
            for key, value in self.parser.metadata["tokenizer"].items():
                if key.endswith("_token_id"):
                    token_type = key.replace("_token_id", "")
                    token_id = value
                    if token_id in vocab:
                        special_token_ids[token_type] = {
                            "id": token_id,
                            "token": vocab[token_id]
                        }
        
        vocab_analysis["special_tokens"] = special_token_ids
        self.results["vocab_analysis"] = vocab_analysis
    
    def analyze_embedding_space(self):
        """Analyze the embedding space for anomalies or backdoors"""
        embedding_analysis = {
            "embedding_size": 0,
            "clusters": {},
            "outliers": []
        }
        
        # Look for embedding tensor
        embedding_tensor = None
        for name, tensor_info in self.parser.tensor_data.items():
            if "embed" in name.lower() or "token" in name.lower() and "weight" in name.lower():
                embedding_tensor = tensor_info["data"]
                break
        
        if embedding_tensor is not None:
            # Store embedding size
            embedding_analysis["embedding_size"] = embedding_tensor.shape[1]
            
            # Simplified analysis - in a real implementation, you would use
            # dimensionality reduction (PCA, t-SNE) and clustering
            
            # Compute simple statistics
            norms = np.linalg.norm(embedding_tensor, axis=1)
            mean_norm = np.mean(norms)
            std_norm = np.std(norms)
            
            # Find outliers (vectors with unusually large or small norms)
            outlier_threshold = 3  # 3 standard deviations
            outliers = np.where(np.abs(norms - mean_norm) > outlier_threshold * std_norm)[0]
            
            embedding_analysis["statistics"] = {
                "mean_norm": float(mean_norm),
                "std_norm": float(std_norm)
            }
            
            embedding_analysis["outliers"] = [int(idx) for idx in outliers]
            
            if len(outliers) > 0:
                self.results["anomalies"].append(
                    f"Found {len(outliers)} outlier embeddings that deviate significantly from the norm"
                )
        
        self.results["embedding_analysis"] = embedding_analysis
    
    def verify_model_provenance(self):
        """Verify if the model matches its claimed source"""
        provenance = {
            "claimed_source": "tensorblock/nanollama-GGUF",
            "verification_result": "unknown"
        }
        
        # In a real implementation, you would:
        # 1. Check against known checksums from trusted sources
        # 2. Verify digital signatures if available
        # 3. Compare with model cards or documentation
        
        # For now, we'll just check if the model name in metadata matches the claimed source
        model_name = self.parser.metadata["model_info"].get("name", "")
        if "nanollama" in model_name.lower():
            provenance["verification_result"] = "name_match"
        
        # Check if fingerprint matches known good fingerprints
        if "matched_known_model" in self.results["provenance"]:
            provenance["verification_result"] = "fingerprint_match"
            provenance["matched_model"] = self.results["provenance"]["matched_known_model"]
        
        self.results["provenance"] = provenance
    
    def detect_anomalies(self):
        """Detect various anomalies in the model"""
        # Most anomalies are detected in the individual analysis methods
        # This method can add additional cross-cutting anomaly checks
        
        # Check for unusual tensor names
        unusual_prefixes = ["custom_", "private_", "hidden_", "backdoor_"]
        for tensor in self.parser.tensors:
            for prefix in unusual_prefixes:
                if tensor["name"].startswith(prefix):
                    self.results["anomalies"].append(f"Unusual tensor name prefix: {tensor['name']}")
        
        # Check for unusual metadata keys
        all_keys = []
        for category in ["model_info", "parameters", "architecture", "tokenizer"]:
            all_keys.extend(self.parser.metadata.get(category, {}).keys())
        
        for key in all_keys:
            if key.startswith("custom_") or key.startswith("private_"):
                self.results["anomalies"].append(f"Unusual metadata key: {key}")
    
    def generate_security_assessment(self):
        """Generate an overall security assessment based on all analyses"""
        assessment = {
            "risk_level": "low",  # low, medium, high
            "confidence": "medium",  # low, medium, high
            "findings": [],
            "recommendations": []
        }
        
        # Determine risk level based on anomalies
        if len(self.results["anomalies"]) > 5:
            assessment["risk_level"] = "high"
        elif len(self.results["anomalies"]) > 2:
            assessment["risk_level"] = "medium"
        
        # Add findings based on analyses
        if len(self.results["vocab_analysis"].get("suspicious_tokens", [])) > 0:
            assessment["findings"].append({
                "type": "suspicious_vocabulary",
                "description": f"Found {len(self.results['vocab_analysis']['suspicious_tokens'])} suspicious tokens in vocabulary",
                "severity": "medium"
            })
        
        if len(self.results["embedding_analysis"].get("outliers", [])) > 0:
            assessment["findings"].append({
                "type": "embedding_outliers",
                "description": f"Found {len(self.results['embedding_analysis']['outliers'])} outlier embeddings",
                "severity": "low"
            })
        
        # Add recommendations
        assessment["recommendations"] = [
            "Perform dynamic analysis to monitor model behavior during inference",
            "Test model with known backdoor triggers to verify security",
            "Verify model provenance with the original source",
            "Consider fine-tuning the model on trusted data before deployment"
        ]
        
        self.results["security_assessment"] = assessment
    
    def save_results(self):
        """Save analysis results to files"""
        # Save full results as JSON
        results_path = os.path.join(self.output_dir, "advanced_analysis.json")
        with open(results_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Save security assessment summary
        summary_path = os.path.join(self.output_dir, "security_assessment.md")
        with open(summary_path, 'w') as f:
            f.write("# AI Model Security Assessment\n\n")
            f.write(f"## Model: {os.path.basename(self.model_path)}\n\n")
            f.write(f"**Risk Level**: {self.results['security_assessment']['risk_level'].upper()}\n")
            f.write(f"**Confidence**: {self.results['security_assessment']['confidence'].upper()}\n\n")
            
            f.write("## Key Findings\n\n")
            for finding in self.results['security_assessment']['findings']:
                f.write(f"- **{finding['type']}** ({finding['severity']}): {finding['description']}\n")
            
            if not self.results['security_assessment']['findings']:
                f.write("- No significant security issues detected\n")
            
            f.write("\n## Anomalies Detected\n\n")
            for anomaly in self.results['anomalies']:
                f.write(f"- {anomaly}\n")
            
            if not self.results['anomalies']:
                f.write("- No anomalies detected\n")
            
            f.write("\n## Recommendations\n\n")
            for recommendation in self.results['security_assessment']['recommendations']:
                f.write(f"- {recommendation}\n")
            
            f.write("\n## Analysis Details\n\n")
            f.write(f"- **Weight Fingerprint**: {self.results['weight_fingerprint']}\n")
            f.write(f"- **Vocabulary Size**: {self.results['vocab_analysis'].get('vocab_size', 'Unknown')}\n")
            f.write(f"- **Embedding Size**: {self.results['embedding_analysis'].get('embedding_size', 'Unknown')}\n")
            f.write(f"- **Provenance Verification**: {self.results['provenance'].get('verification_result', 'Unknown')}\n")
        
        print(f"Results saved to {results_path}")
        print(f"Security assessment saved to {summary_path}")


def main():
    parser = argparse.ArgumentParser(description="Advanced AI Model Composition Analysis Tool")
    parser.add_argument("model_path", help="Path to the model file")
    parser.add_argument("--output", "-o", default="./model-analysis", help="Output directory for analysis results")
    args = parser.parse_args()
    
    # Check if model path exists
    if not os.path.exists(args.model_path):
        print(f"Error: Model file not found: {args.model_path}")
        sys.exit(1)
    
    # Create analyzer and run analyses
    analyzer = AdvancedModelAnalyzer(args.model_path, args.output)
    
    try:
        analyzer.run_all_analyses()
        print(f"Analysis complete. Results saved to {args.output}")
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
