#!/usr/bin/env python3

import sys
import os
import time
import json
import argparse
from bcc import BPF

# BPF program to trace syscalls
bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>

// Data structure to store syscall information
struct syscall_data_t {
    u64 timestamp;
    u32 pid;
    u32 uid;
    char comm[TASK_COMM_LEN];
    char syscall[64];
    char args[128];
};

BPF_PERF_OUTPUT(syscall_events);
BPF_HASH(start, u32);

// Function to trace syscall entry
TRACEPOINT_PROBE(raw_syscalls, sys_enter) {
    u64 timestamp = bpf_ktime_get_ns();
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    
    // Filter by PID if specified
    FILTER_PID
    
    // Store timestamp at start of syscall
    start.update(&pid, &timestamp);
    return 0;
}

// Function to trace syscall exit
TRACEPOINT_PROBE(raw_syscalls, sys_exit) {
    struct syscall_data_t data = {};
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    
    // Filter by PID if specified
    FILTER_PID
    
    // Get timestamp from start of syscall
    u64 *start_ts = start.lookup(&pid);
    if (!start_ts)
        return 0;
    
    // Get process information
    data.timestamp = bpf_ktime_get_ns();
    data.pid = pid;
    data.uid = bpf_get_current_uid_gid();
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    
    // Get syscall number and name
    int syscall_id = args->id;
    
    // Only trace specific syscalls
    if (FILTER_SYSCALLS) {
        // Convert syscall ID to name (simplified)
        switch (syscall_id) {
            SYSCALL_SWITCH
        }
        
        // Send event to user space
        syscall_events.perf_submit(args, &data, sizeof(data));
    }
    
    // Remove from hash map
    start.delete(&pid);
    return 0;
}
"""

# Suspicious syscalls to monitor
SUSPICIOUS_SYSCALLS = {
    0: "read",
    1: "write",
    2: "open",
    3: "close",
    9: "mmap",
    10: "mprotect",
    11: "munmap",
    41: "socket",
    42: "connect",
    43: "accept",
    56: "clone",
    57: "fork",
    58: "vfork",
    59: "execve",
    231: "exit_group",
    # Add more syscalls as needed
}

def generate_syscall_switch():
    """Generate the switch case for syscall names"""
    switch_code = ""
    filter_code = ""
    
    for syscall_id, syscall_name in SUSPICIOUS_SYSCALLS.items():
        switch_code += f"case {syscall_id}: bpf_probe_read_kernel_str(&data.syscall, sizeof(data.syscall), \"{syscall_name}\"); break;\n            "
        if filter_code:
            filter_code += f" || syscall_id == {syscall_id}"
        else:
            filter_code += f"syscall_id == {syscall_id}"
    
    return switch_code, filter_code

def monitor_syscalls(target_pid, output_path, duration=30):
    """
    Monitor syscalls using BCC/eBPF
    
    Args:
        target_pid: PID to monitor (0 for all processes)
        output_path: Path to save the monitoring results
        duration: Duration to monitor in seconds
        
    Returns:
        True if suspicious syscalls detected, False otherwise
    """
    # Generate syscall switch code
    switch_code, filter_code = generate_syscall_switch()
    
    # Replace placeholders in BPF program
    program = bpf_text.replace("SYSCALL_SWITCH", switch_code)
    program = program.replace("FILTER_SYSCALLS", filter_code)
    
    # Add PID filter if specified
    if target_pid > 0:
        program = program.replace("FILTER_PID", f"if (pid != {target_pid}) return 0;")
    else:
        program = program.replace("FILTER_PID", "")
    
    # Load BPF program
    b = BPF(text=program)
    
    # Dictionary to store syscall events
    syscall_events = []
    
    # Callback function for syscall events
    def process_event(cpu, data, size):
        event = b["syscall_events"].event(data)
        syscall_events.append({
            "timestamp": event.timestamp,
            "pid": event.pid,
            "uid": event.uid,
            "comm": event.comm.decode('utf-8', 'replace'),
            "syscall": event.syscall.decode('utf-8', 'replace'),
            "args": event.args.decode('utf-8', 'replace')
        })
    
    # Open perf buffer
    b["syscall_events"].open_perf_buffer(process_event)
    
    print(f"Monitoring syscalls for {duration} seconds...")
    
    # Poll perf buffer for events
    start_time = time.time()
    while time.time() - start_time < duration:
        b.perf_buffer_poll(timeout=100)
    
    # Analyze results
    suspicious_events = []
    for event in syscall_events:
        # Check for suspicious patterns
        if event["syscall"] in ["execve", "fork", "vfork", "clone", "socket", "connect"]:
            suspicious_events.append(event)
        elif event["syscall"] == "mprotect" and "PROT_EXEC" in event["args"]:
            suspicious_events.append(event)
    
    # Write results to file
    with open(output_path, 'w') as f:
        f.write("BCC/eBPF Syscall Monitoring Results\n")
        f.write("="*50 + "\n\n")
        
        f.write(f"Total syscalls monitored: {len(syscall_events)}\n")
        f.write(f"Suspicious syscalls detected: {len(suspicious_events)}\n\n")
        
        if suspicious_events:
            f.write("Suspicious Syscall Events:\n")
            for event in suspicious_events:
                f.write(f"PID: {event['pid']}, Command: {event['comm']}, Syscall: {event['syscall']}\n")
                f.write(f"  Arguments: {event['args']}\n\n")
        else:
            f.write("No suspicious syscall activity detected.\n")
        
        # Write full event log
        f.write("\nFull Syscall Log:\n")
        f.write(json.dumps(syscall_events, indent=2))
    
    return len(suspicious_events) > 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor syscalls using BCC/eBPF")
    parser.add_argument("--pid", type=int, default=0, help="PID to monitor (0 for all processes)")
    parser.add_argument("--duration", type=int, default=30, help="Duration to monitor in seconds")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    
    args = parser.parse_args()
    
    found_suspicious = monitor_syscalls(args.pid, args.output, args.duration)
    
    print(f"Monitoring completed. Results saved to {args.output}")
    if found_suspicious:
        print("WARNING: Suspicious syscall activity detected!")
        sys.exit(1)
    else:
        print("No suspicious syscall activity detected.")
        sys.exit(0)
