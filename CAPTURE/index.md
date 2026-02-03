---
title: "CAPTURE: An AppSec Strategy Framework and Practice"
---

# Security Foundations: The Onion Model
Before diving into the specifics of Application Security, it is essential to understand where these efforts sit within the broader security landscape. The Onion Model, or Defense in Depth, represents security as a series of concentric layers. The goal is simple: if one layer is breached, the next layer is there to stop the attacker.

The Layers of Defense
Physical Security: The outermost layer. Protecting the actual hardware, data centers, and offices (e.g., CCTV, biometric locks).

Network Security: Controlling the traffic entering and moving within the environment (e.g., Firewalls, VPNs, WAF).

Host/Endpoint Security: Securing the individual servers and workstations (e.g., OS hardening, EDR/Antivirus).

Application Security (Our Focus): Protecting the software, its logic, the tools for AI-SSDLC, and the pipelines used to ship it.

Data Security: The core. Protecting the actual information through encryption, masking, and strict access controls.

# CAPTURE: An AppSec Strategy Framework
The CAPTURE framework is a modular methodology designed to secure the Application Layer and Software Supply Chain. By isolating our focus to this specific layer of the onion, we can address where business logic and high-value data truly reside without blurring the discussion with infrastructure concerns.

The Core Domains
C - Compliance: Aligning development with regional regulations (e.g., HKMA iCAST, Taiwan FSC Resilience Blueprint) and internal security standards.

A - Attacker's View: Adopting the adversary's mindset to identify vulnerabilities in code, pipelines, and the Software Supply Chain, mapped against the MITRE ATT&CK matrix.

P - Process (Client Side): Evaluating the human elements of DevSecOps and the governance of AI adoption within the development team.

TU - Tool Utilization (Our Offering): Maximizing the effectiveness of security tooling (SAST, DAST, SCA) to ensure they are integrated and utilized, not just installed.

RE - Review & Evaluation: Establishing a continuous feedback loop through metrics and post-implementation audits to ensure long-term resilience.

Traditional application security models may suffer from "vendor tunnel vision," focusing in isolation on compliance checklists, DevSecOps processes, or periodic red teaming. This fragmented approach creates dangerous silos where critical risks go unnoticed.

The CAPTURE framework is designed to bridge these gaps. By unifying regulatory requirements, offensive security insights, and practical tool utilization into a single lifecycle, we address the "white space" where real-world attackers operate. Our value proposition is simple: we don't just provide services or products; we integrate these disparate security domains into a cohesive, resilient strategy that protects your most vital assets.

Purpose: To transform Application Security from a bottleneck into a streamlined, automated, and resilient business enabler.