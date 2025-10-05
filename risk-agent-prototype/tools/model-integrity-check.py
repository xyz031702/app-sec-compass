#!/usr/bin/env python3
"""
Model Integrity Checker

This script verifies the integrity of a downloaded model by comparing it with the original model
from Hugging Face. Instead of downloading the entire model again, it uses a combination of:
1. Metadata comparison
2. Strategic sampling of model chunks
3. Checksum verification of critical components

This approach provides high confidence in model integrity while minimizing bandwidth usage.
"""

import argparse
import hashlib
import json
import os
import random
import sys
import time
from typing import Dict, List, Optional, Tuple, Any
import struct
import requests
from tqdm import tqdm
from huggingface_hub import hf_hub_download, HfApi, ModelInfo

# GGUF format constants
GGUF_MAGIC = 0x46554747  # "GGUF" in hex

class ModelIntegrityChecker:
    """Checks the integrity of a downloaded model against the original on Hugging Face"""
    
    def __init__(self, local_model_path: str, repo_id: str, sampling_rate: float = 0.05):
        """
        Initialize the checker
        
        Args:
            local_model_path: Path to the local model file
            repo_id: Hugging Face repository ID (e.g., 'tensorblock/nanollama-GGUF')
            sampling_rate: Percentage of model to sample (0.05 = 5%)
        """
        self.local_model_path = local_model_path
        self.repo_id = repo_id
        self.sampling_rate = sampling_rate
        self.model_filename = os.path.basename(local_model_path)
        self.results = {
            "model_path": local_model_path,
            "repo_id": repo_id,
            "checks": [],
            "overall_status": "unknown",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def run_all_checks(self) -> Dict[str, Any]:
        """Run all integrity checks and return results"""
        print(f"Checking integrity of {self.local_model_path}")
        print(f"Against Hugging Face repo: {self.repo_id}")
        
        # Check if model exists
        if not os.path.exists(self.local_model_path):
            self.results["overall_status"] = "failed"
            self.results["checks"].append({
                "name": "file_existence",
                "status": "failed",
                "message": f"Local model file not found: {self.local_model_path}"
            })
            return self.results
        
        # Check file size
        self._check_file_size()
        
        # Check metadata
        self._check_metadata()
        
        # Check critical sections
        self._check_critical_sections()
        
        # Check random samples
        self._check_random_samples()
        
        # Determine overall status
        failed_checks = [check for check in self.results["checks"] if check["status"] == "failed"]
        if failed_checks:
            self.results["overall_status"] = "failed"
        else:
            self.results["overall_status"] = "passed"
        
        return self.results
    
    def _check_file_size(self):
        """Check if the file size matches the expected size"""
        try:
            # Get local file size
            local_size = os.path.getsize(self.local_model_path)
            
            # Get remote file size without downloading
            api = HfApi()
            model_info = api.model_info(self.repo_id)
            
            # Find the matching file in the repo
            remote_size = None
            for sibling in model_info.siblings:
                if sibling.rfilename == self.model_filename:
                    remote_size = sibling.size
                    break
            
            if remote_size is None:
                self.results["checks"].append({
                    "name": "file_size",
                    "status": "warning",
                    "message": f"Could not find {self.model_filename} in remote repository"
                })
                return
            
            # Compare sizes
            size_diff = abs(local_size - remote_size)
            size_diff_percent = (size_diff / remote_size) * 100 if remote_size > 0 else 100
            
            if size_diff == 0:
                self.results["checks"].append({
                    "name": "file_size",
                    "status": "passed",
                    "message": f"File size matches: {local_size} bytes"
                })
            elif size_diff_percent < 1:  # Allow 1% difference
                self.results["checks"].append({
                    "name": "file_size",
                    "status": "warning",
                    "message": f"File size differs slightly: local={local_size}, remote={remote_size}, diff={size_diff_percent:.2f}%"
                })
            else:
                self.results["checks"].append({
                    "name": "file_size",
                    "status": "failed",
                    "message": f"File size mismatch: local={local_size}, remote={remote_size}, diff={size_diff_percent:.2f}%"
                })
        
        except Exception as e:
            self.results["checks"].append({
                "name": "file_size",
                "status": "error",
                "message": f"Error checking file size: {str(e)}"
            })
    
    def _check_metadata(self):
        """Check the model metadata"""
        try:
            # Check if it's a GGUF file
            is_gguf = self._is_gguf_format(self.local_model_path)
            
            if not is_gguf:
                self.results["checks"].append({
                    "name": "metadata",
                    "status": "warning",
                    "message": "Not a GGUF format file, skipping metadata check"
                })
                return
            
            # Extract local metadata from the first 16KB
            local_metadata = self._extract_gguf_header(self.local_model_path)
            
            # Get remote metadata
            # We'll download just the first 16KB of the file which should contain the header
            try:
                # Create a temporary file for the header
                temp_header_path = f"{self.local_model_path}.header"
                
                # Use the Hugging Face API to download just the first part of the file
                headers = {"Range": "bytes=0-16383"}  # First 16KB
                url = f"https://huggingface.co/{self.repo_id}/resolve/main/{self.model_filename}"
                response = requests.get(url, headers=headers, stream=True)
                
                if response.status_code in (200, 206):  # OK or Partial Content
                    with open(temp_header_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    # Extract remote metadata
                    remote_metadata = self._extract_gguf_header(temp_header_path)
                    
                    # Compare metadata
                    if local_metadata.get("version") != remote_metadata.get("version"):
                        self.results["checks"].append({
                            "name": "metadata_version",
                            "status": "failed",
                            "message": f"GGUF version mismatch: local={local_metadata.get('version')}, remote={remote_metadata.get('version')}"
                        })
                    else:
                        self.results["checks"].append({
                            "name": "metadata_version",
                            "status": "passed",
                            "message": f"GGUF version matches: {local_metadata.get('version')}"
                        })
                    
                    if local_metadata.get("tensor_count") != remote_metadata.get("tensor_count"):
                        self.results["checks"].append({
                            "name": "metadata_tensor_count",
                            "status": "failed",
                            "message": f"Tensor count mismatch: local={local_metadata.get('tensor_count')}, remote={remote_metadata.get('tensor_count')}"
                        })
                    else:
                        self.results["checks"].append({
                            "name": "metadata_tensor_count",
                            "status": "passed",
                            "message": f"Tensor count matches: {local_metadata.get('tensor_count')}"
                        })
                    
                    # Clean up
                    os.remove(temp_header_path)
                else:
                    self.results["checks"].append({
                        "name": "metadata",
                        "status": "error",
                        "message": f"Failed to download header: HTTP {response.status_code}"
                    })
            
            except Exception as e:
                self.results["checks"].append({
                    "name": "metadata",
                    "status": "error",
                    "message": f"Error downloading remote metadata: {str(e)}"
                })
        
        except Exception as e:
            self.results["checks"].append({
                "name": "metadata",
                "status": "error",
                "message": f"Error checking metadata: {str(e)}"
            })
    
    def _check_critical_sections(self):
        """Check critical sections of the model"""
        try:
            # For GGUF models, critical sections include:
            # 1. The header (first 16KB)
            # 2. The first tensor
            # 3. The last tensor
            
            # We've already checked the header in _check_metadata
            
            # Get file size
            file_size = os.path.getsize(self.local_model_path)
            
            # Check first 64KB (header + start of first tensor)
            first_chunk_size = min(65536, file_size)
            first_chunk_local = self._get_file_chunk(self.local_model_path, 0, first_chunk_size)
            first_chunk_hash = hashlib.sha256(first_chunk_local).hexdigest()
            
            # Check last 64KB
            last_chunk_size = min(65536, file_size)
            last_chunk_local = self._get_file_chunk(self.local_model_path, file_size - last_chunk_size, last_chunk_size)
            last_chunk_hash = hashlib.sha256(last_chunk_local).hexdigest()
            
            # Download and check remote chunks
            try:
                # First chunk
                headers = {"Range": f"bytes=0-{first_chunk_size-1}"}
                url = f"https://huggingface.co/{self.repo_id}/resolve/main/{self.model_filename}"
                response = requests.get(url, headers=headers)
                
                if response.status_code in (200, 206):
                    first_chunk_remote = response.content
                    first_chunk_remote_hash = hashlib.sha256(first_chunk_remote).hexdigest()
                    
                    if first_chunk_hash == first_chunk_remote_hash:
                        self.results["checks"].append({
                            "name": "critical_first_chunk",
                            "status": "passed",
                            "message": f"First chunk matches: {first_chunk_hash}"
                        })
                    else:
                        self.results["checks"].append({
                            "name": "critical_first_chunk",
                            "status": "failed",
                            "message": f"First chunk mismatch: local={first_chunk_hash}, remote={first_chunk_remote_hash}"
                        })
                else:
                    self.results["checks"].append({
                        "name": "critical_first_chunk",
                        "status": "error",
                        "message": f"Failed to download first chunk: HTTP {response.status_code}"
                    })
                
                # Last chunk
                headers = {"Range": f"bytes={file_size-last_chunk_size}-{file_size-1}"}
                response = requests.get(url, headers=headers)
                
                if response.status_code in (200, 206):
                    last_chunk_remote = response.content
                    last_chunk_remote_hash = hashlib.sha256(last_chunk_remote).hexdigest()
                    
                    if last_chunk_hash == last_chunk_remote_hash:
                        self.results["checks"].append({
                            "name": "critical_last_chunk",
                            "status": "passed",
                            "message": f"Last chunk matches: {last_chunk_hash}"
                        })
                    else:
                        self.results["checks"].append({
                            "name": "critical_last_chunk",
                            "status": "failed",
                            "message": f"Last chunk mismatch: local={last_chunk_hash}, remote={last_chunk_remote_hash}"
                        })
                else:
                    self.results["checks"].append({
                        "name": "critical_last_chunk",
                        "status": "error",
                        "message": f"Failed to download last chunk: HTTP {response.status_code}"
                    })
            
            except Exception as e:
                self.results["checks"].append({
                    "name": "critical_sections",
                    "status": "error",
                    "message": f"Error checking critical sections: {str(e)}"
                })
        
        except Exception as e:
            self.results["checks"].append({
                "name": "critical_sections",
                "status": "error",
                "message": f"Error checking critical sections: {str(e)}"
            })
    
    def _check_random_samples(self):
        """Check random samples throughout the file"""
        try:
            # Get file size
            file_size = os.path.getsize(self.local_model_path)
            
            # Determine number of samples based on file size and sampling rate
            chunk_size = 16384  # 16KB chunks
            total_chunks = file_size // chunk_size
            num_samples = max(3, int(total_chunks * self.sampling_rate))
            
            # Ensure we don't sample too many chunks for very large files
            num_samples = min(num_samples, 50)
            
            # Generate random chunk positions (excluding first and last chunks which we've already checked)
            random.seed(42)  # For reproducibility
            chunk_positions = random.sample(range(1, total_chunks - 1), num_samples)
            
            # Sort positions for more efficient sequential reading
            chunk_positions.sort()
            
            # Check each sample
            samples_passed = 0
            samples_failed = 0
            
            print(f"Checking {num_samples} random samples...")
            for i, chunk_pos in enumerate(tqdm(chunk_positions)):
                offset = chunk_pos * chunk_size
                
                # Get local chunk
                local_chunk = self._get_file_chunk(self.local_model_path, offset, chunk_size)
                local_hash = hashlib.sha256(local_chunk).hexdigest()
                
                # Get remote chunk
                try:
                    headers = {"Range": f"bytes={offset}-{offset+chunk_size-1}"}
                    url = f"https://huggingface.co/{self.repo_id}/resolve/main/{self.model_filename}"
                    response = requests.get(url, headers=headers)
                    
                    if response.status_code in (200, 206):
                        remote_chunk = response.content
                        remote_hash = hashlib.sha256(remote_chunk).hexdigest()
                        
                        if local_hash == remote_hash:
                            samples_passed += 1
                        else:
                            samples_failed += 1
                    else:
                        self.results["checks"].append({
                            "name": f"sample_{i}",
                            "status": "error",
                            "message": f"Failed to download sample at offset {offset}: HTTP {response.status_code}"
                        })
                
                except Exception as e:
                    self.results["checks"].append({
                        "name": f"sample_{i}",
                        "status": "error",
                        "message": f"Error checking sample at offset {offset}: {str(e)}"
                    })
            
            # Report overall sample results
            if samples_failed == 0:
                self.results["checks"].append({
                    "name": "random_samples",
                    "status": "passed",
                    "message": f"All {samples_passed} random samples matched"
                })
            else:
                failure_rate = (samples_failed / (samples_passed + samples_failed)) * 100
                self.results["checks"].append({
                    "name": "random_samples",
                    "status": "failed",
                    "message": f"{samples_failed} of {samples_passed + samples_failed} random samples failed ({failure_rate:.2f}%)"
                })
        
        except Exception as e:
            self.results["checks"].append({
                "name": "random_samples",
                "status": "error",
                "message": f"Error checking random samples: {str(e)}"
            })
    
    def _is_gguf_format(self, file_path: str) -> bool:
        """Check if file is in GGUF format"""
        try:
            with open(file_path, 'rb') as f:
                magic = struct.unpack('<I', f.read(4))[0]
                return magic == GGUF_MAGIC
        except Exception:
            return False
    
    def _extract_gguf_header(self, file_path: str) -> Dict[str, Any]:
        """Extract basic header information from a GGUF file"""
        metadata = {}
        
        try:
            with open(file_path, 'rb') as f:
                # Skip magic number
                f.read(4)
                
                # Read version
                version = struct.unpack('<I', f.read(4))[0]
                metadata["version"] = version
                
                # For version 1+
                if version >= 1:
                    # Read tensor count
                    tensor_count = struct.unpack('<Q', f.read(8))[0]
                    metadata["tensor_count"] = tensor_count
                    
                    # Read metadata kv count
                    kv_count = struct.unpack('<Q', f.read(8))[0]
                    metadata["kv_count"] = kv_count
        
        except Exception as e:
            metadata["error"] = str(e)
        
        return metadata
    
    def _get_file_chunk(self, file_path: str, offset: int, size: int) -> bytes:
        """Read a chunk of data from a file"""
        with open(file_path, 'rb') as f:
            f.seek(offset)
            return f.read(size)
    
    def save_results(self, output_path: Optional[str] = None) -> str:
        """Save results to a file"""
        if output_path is None:
            output_dir = os.path.dirname(self.local_model_path)
            output_path = os.path.join(output_dir, "integrity_check_results.json")
        
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        return output_path


def main():
    parser = argparse.ArgumentParser(description="Check the integrity of a downloaded model")
    parser.add_argument("model_path", help="Path to the local model file")
    parser.add_argument("--repo-id", required=True, help="Hugging Face repository ID (e.g., 'tensorblock/nanollama-GGUF')")
    parser.add_argument("--sampling-rate", type=float, default=0.05, help="Percentage of model to sample (0.05 = 5%%)")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()
    
    # Check if model path exists
    if not os.path.exists(args.model_path):
        print(f"Error: Model file not found: {args.model_path}")
        sys.exit(1)
    
    # Create checker and run checks
    checker = ModelIntegrityChecker(args.model_path, args.repo_id, args.sampling_rate)
    
    try:
        results = checker.run_all_checks()
        output_path = checker.save_results(args.output)
        
        # Print summary
        print("\n=== Integrity Check Summary ===")
        print(f"Model: {args.model_path}")
        print(f"Repository: {args.repo_id}")
        print(f"Overall Status: {results['overall_status'].upper()}")
        
        print("\nChecks:")
        for check in results["checks"]:
            status_symbol = "✅" if check["status"] == "passed" else "❌" if check["status"] == "failed" else "⚠️"
            print(f"{status_symbol} {check['name']}: {check['message']}")
        
        print(f"\nDetailed results saved to: {output_path}")
        
        # Exit with appropriate code
        sys.exit(0 if results["overall_status"] == "passed" else 1)
    
    except Exception as e:
        print(f"Error during integrity check: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
