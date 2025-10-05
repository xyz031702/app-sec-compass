#!/usr/bin/env python3
"""
GGUF Model Metadata Extractor

A lightweight tool to extract metadata from GGUF format AI models.
Requires only standard Python libraries.
"""

import argparse
import json
import math
import os
import struct
import sys
from datetime import datetime

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


def human_readable_size(size_bytes):
    """Convert bytes to human readable format"""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.log(size_bytes, 1024))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def is_gguf_format(file_path):
    """Check if file is in GGUF format"""
    try:
        with open(file_path, 'rb') as f:
            magic = struct.unpack('<I', f.read(4))[0]
            return magic == GGUF_MAGIC
    except Exception:
        return False


def read_gguf_value(f, val_type):
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
        return [read_gguf_value(f, arr_type) for _ in range(arr_len)]
    else:
        return f"Unknown type: {val_type}"


def extract_gguf_metadata(model_path):
    """Extract metadata from GGUF format model"""
    metadata = {
        "format": "gguf",
        "file_info": {},
        "model_info": {},
        "tensor_info": {},
        "parameters": {},
        "architecture": {},
        "tokenizer": {},
    }
    
    # Basic file info
    file_stats = os.stat(model_path)
    metadata["file_info"] = {
        "path": model_path,
        "size_bytes": file_stats.st_size,
        "size_human": human_readable_size(file_stats.st_size),
        "created": datetime.fromtimestamp(file_stats.st_ctime).isoformat(),
        "modified": datetime.fromtimestamp(file_stats.st_mtime).isoformat(),
    }
    
    try:
        with open(model_path, 'rb') as f:
            # Skip magic number
            f.read(4)
            
            # Read version
            version = struct.unpack('<I', f.read(4))[0]
            metadata["model_info"]["gguf_version"] = version
            
            # For version 1+
            if version >= 1:
                # Read tensor count
                tensor_count = struct.unpack('<Q', f.read(8))[0]
                metadata["tensor_info"]["count"] = tensor_count
                
                # Read metadata kv count
                kv_count = struct.unpack('<Q', f.read(8))[0]
                metadata["model_info"]["metadata_count"] = kv_count
                
                # Extract metadata key-value pairs
                for _ in range(kv_count):
                    # Read key length
                    key_len = struct.unpack('<Q', f.read(8))[0]
                    # Read key
                    key = f.read(key_len).decode('utf-8')
                    
                    # Read value type
                    val_type = struct.unpack('<I', f.read(4))[0]
                    
                    # Extract value based on type
                    value = read_gguf_value(f, val_type)
                    
                    # Organize metadata by category
                    if key.startswith("general."):
                        metadata["model_info"][key.replace("general.", "")] = value
                    elif key.startswith("tokenizer."):
                        metadata["tokenizer"][key.replace("tokenizer.", "")] = value
                    elif key.startswith("llama."):
                        metadata["architecture"][key.replace("llama.", "")] = value
                    else:
                        metadata["parameters"][key] = value
    except Exception as e:
        metadata["extraction_error"] = str(e)
    
    return metadata


def main():
    parser = argparse.ArgumentParser(description="Extract metadata from GGUF models")
    parser.add_argument("model_path", help="Path to the GGUF model file")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()
    
    # Check if model path exists
    if not os.path.exists(args.model_path):
        print(f"Error: Model file not found: {args.model_path}")
        sys.exit(1)
    
    # Check if it's a GGUF file
    if not is_gguf_format(args.model_path):
        print(f"Error: Not a GGUF format file: {args.model_path}")
        sys.exit(1)
    
    # Extract metadata
    metadata = extract_gguf_metadata(args.model_path)
    
    # Print metadata summary
    print("\n=== GGUF Model Metadata Summary ===")
    print(f"File: {metadata['file_info']['path']}")
    print(f"Size: {metadata['file_info']['size_human']}")
    print(f"GGUF Version: {metadata['model_info'].get('gguf_version', 'unknown')}")
    print(f"Tensor Count: {metadata['tensor_info'].get('count', 'unknown')}")
    
    # Print model info
    print("\nModel Information:")
    for key, value in metadata["model_info"].items():
        if key not in ["gguf_version", "metadata_count"]:
            print(f"  {key}: {value}")
    
    # Print architecture info
    if metadata["architecture"]:
        print("\nArchitecture:")
        for key, value in metadata["architecture"].items():
            print(f"  {key}: {value}")
    
    # Print tokenizer info
    if metadata["tokenizer"]:
        print("\nTokenizer:")
        vocab_size = metadata["tokenizer"].get("vocab_size", "unknown")
        print(f"  Vocabulary Size: {vocab_size}")
        eos_token_id = metadata["tokenizer"].get("eos_token_id", "unknown")
        print(f"  EOS Token ID: {eos_token_id}")
    
    # Save to file if output path is provided
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(metadata, f, indent=2)
        print(f"\nDetailed metadata saved to: {args.output}")


if __name__ == "__main__":
    main()
