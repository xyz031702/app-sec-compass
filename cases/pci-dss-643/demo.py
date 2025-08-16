#!/usr/bin/env python3
"""
CVE-2019-11358 jQuery Prototype Pollution Demo
Demonstrates PCI-DSS 6.4.3 and 11.6.1 vulnerabilities
"""

import subprocess
import time
import sys
import os
import webbrowser
from threading import Timer

def run_payment_server():
    """Start the vulnerable payment website"""
    print("🌐 Starting vulnerable payment website...")
    subprocess.run([sys.executable, "web-server.py"])

def main():
    """Run the complete CVE-2019-11358 demonstration"""
    print("=" * 70)
    print("🚨 CVE-2019-11358 PROTOTYPE POLLUTION DEMO")
    print("=" * 70)
    print("This demo shows how jQuery 3.3.1 prototype pollution leads to XSS:")
    print("1. Payment page loads vulnerable jQuery 3.3.1")
    print("2. $.extend(true, ...) pollutes Object.prototype")
    print("3. Polluted properties trigger XSS in DOM operations")
    print("4. Attack can steal payment card data")
    print("=" * 70)
    print()
    
    print("📋 DEMO INSTRUCTIONS:")
    print("1. Payment website will start on port 3000")
    print("2. Browser will open automatically to the payment page")
    print("3. Click 'Trigger jQuery Prototype Pollution → XSS' button")
    print("4. Observe XSS alert demonstrating the vulnerability")
    print("5. Check browser console for technical details")
    print()
    print("🔍 SCA TESTING:")
    print("- Run 'npm audit' to detect CVE-2019-11358")
    print("- Check package.json for jQuery 3.3.1 dependency")
    print("- Upgrade to jQuery ≥3.4.0 to fix the vulnerability")
    print()
    print("⚠️  This is for educational/demo purposes only!")
    print("=" * 70)
    print()
    
    input("Press Enter to start the demonstration...")
    
    # Start the payment website
    run_payment_server()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Demo stopped")
        sys.exit(0)
