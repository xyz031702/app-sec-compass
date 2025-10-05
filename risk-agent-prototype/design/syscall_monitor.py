#!/usr/bin/env python3

import subprocess
import json
import os
import sys
import re

# Define suspicious syscalls
SUSPICIOUS_SYSCALLS = {
    # Network-related
    'socket': 'Network socket creation',
    'connect': 'Network connection attempt',
    'bind': 'Network binding',
    'listen': 'Network listening',
    'accept': 'Network connection acceptance',
    'sendto': 'Network data sending',
    'recvfrom': 'Network data receiving',
    
    # Process creation
    'fork': 'Process creation (fork)',
    'vfork': 'Process creation (vfork)',
    'clone': 'Process creation (clone)',
    'execve': 'Program execution',
    'execveat': 'Program execution',
    
    # File operations outside expected paths
    'open': 'File opening',  # Needs path filtering
    'openat': 'File opening',  # Needs path filtering
    'creat': 'File creation',
    
    # Other suspicious
    'ptrace': 'Process tracing',
    'personality': 'Execution domain change',
    'prctl': 'Process control',
    'mprotect': 'Memory protection change',
    'mmap': 'Memory mapping with PROT_EXEC'
}

def create_model_loader(output_path):
    """Create a simple script to load the model"""
    with open(output_path, 'w') as f:
        f.write("""#!/usr/bin/env python3
import sys
from llama_cpp import Llama

try:
    print(f"Loading model from {sys.argv[1]}")
    model = Llama(model_path=sys.argv[1], n_ctx=512)
    print("Model loaded successfully")
    output = model("Test prompt", max_tokens=5)
    print(f"Model output: {output['choices'][0]['text']}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
""")
    os.chmod(output_path, 0o755)
    return output_path

def run_strace(command, output_path):
    """Run a command with strace and capture syscalls"""
    try:
        # Run strace with detailed output
        strace_cmd = [
            "strace",
            "-f",  # Follow forks
            "-e", "trace=network,process,file",  # Trace specific syscall categories
            "-s", "256",  # Show 256 chars of strings
            "-o", output_path,  # Output to file
        ] + command
        
        # Run the command
        subprocess.run(strace_cmd, check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running strace: {e}")
        return False

def analyze_strace_output(strace_path, analysis_path, allowed_paths=None):
    """Analyze strace output for suspicious syscalls"""
    if allowed_paths is None:
        allowed_paths = ['/home/scantist/github/risk-agent-prototype/', '/usr/local/lib/', '/lib/', '/usr/']
    
    suspicious_calls = []
    
    # Read strace output
    with open(strace_path, 'r') as f:
        for line in f:
            # Extract syscall name
            syscall_match = re.match(r'^\[pid\s+\d+\]\s+([a-zA-Z0-9_]+)\(', line) or \
                         re.match(r'^([a-zA-Z0-9_]+)\(', line)
            
            if syscall_match:
                syscall = syscall_match.group(1)
                
                # Check if suspicious
                if syscall in SUSPICIOUS_SYSCALLS:
                    # For file operations, check path
                    if syscall in ['open', 'openat']:
                        # Extract path argument
                        path_match = re.search(r'"([^"]+)"', line)
                        if path_match:
                            path = path_match.group(1)
                            # Check if path is allowed
                            if not any(path.startswith(allowed) for allowed in allowed_paths):
                                suspicious_calls.append({
                                    'syscall': syscall,
                                    'description': SUSPICIOUS_SYSCALLS[syscall],
                                    'details': f"Accessing path outside allowed directories: {path}",
                                    'raw': line.strip()
                                })
                    # For memory protection, check if making executable
                    elif syscall == 'mprotect' and 'PROT_EXEC' in line:
                        suspicious_calls.append({
                            'syscall': syscall,
                            'description': SUSPICIOUS_SYSCALLS[syscall],
                            'details': "Making memory executable",
                            'raw': line.strip()
                        })
                    # For memory mapping, check if executable
                    elif syscall == 'mmap' and 'PROT_EXEC' in line:
                        suspicious_calls.append({
                            'syscall': syscall,
                            'description': SUSPICIOUS_SYSCALLS[syscall],
                            'details': "Mapping executable memory",
                            'raw': line.strip()
                        })
                    # For network or process syscalls
                    elif syscall in ['socket', 'connect', 'bind', 'listen', 'accept', 
                                    'fork', 'vfork', 'clone', 'execve', 'execveat']:
                        suspicious_calls.append({
                            'syscall': syscall,
                            'description': SUSPICIOUS_SYSCALLS[syscall],
                            'details': "",
                            'raw': line.strip()
                        })
    
    # Write analysis to file
    with open(analysis_path, 'w') as f:
        f.write("Syscall Analysis Report\n")
        f.write("======================\n\n")
        
        if suspicious_calls:
            f.write(f"Found {len(suspicious_calls)} suspicious syscalls:\n\n")
            for call in suspicious_calls:
                f.write(f"  - {call['syscall']}: {call['description']}\n")
                if call['details']:
                    f.write(f"    {call['details']}\n")
                f.write(f"    Raw: {call['raw']}\n\n")
        else:
            f.write("No suspicious syscalls detected.\n")
    
    return len(suspicious_calls) > 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <model_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    
    # Create directories
    os.makedirs("analysis/dynamic", exist_ok=True)
    
    # Create model loader script
    loader_script = create_model_loader("load_model.py")
    
    # Run strace
    strace_output = "analysis/dynamic/syscalls.log"
    success = run_strace(["python", loader_script, model_path], strace_output)
    
    if not success:
        print("Strace failed")
        sys.exit(1)
    
    # Analyze strace output
    analysis_output = "analysis/dynamic/syscall_analysis.txt"
    suspicious = analyze_strace_output(strace_output, analysis_output)
    
    print(f"Syscall analysis completed: {analysis_output}")
    sys.exit(1 if suspicious else 0)
