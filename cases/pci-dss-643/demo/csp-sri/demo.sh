#!/bin/bash

# CSP + SRI Demo Script
# Demonstrates how Content Security Policy and Subresource Integrity protect against script tampering

echo "🛡️  CSP + SRI Protection Demo"
echo "================================"
echo ""

# Generate SRI hash for the JavaScript file
echo "1. Generating SRI hash for payment-secure.js..."
./generate_sri_hash.sh payment-secure.js

echo ""
echo "2. Starting local web server..."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python not found. Please install Python to run the demo."
    exit 1
fi

# Start web server in background from the csp-sri directory
echo "Starting server on http://localhost:8080 from $(pwd)"
$PYTHON_CMD -m http.server 8080 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

echo ""
echo "3. Demo Instructions:"
echo "   📧 Step 1: Click 'seed.html' in your browser"
echo "      This simulates a phishing email seeding malicious JavaScript"
echo ""
echo "   🚨 Step 2: Navigate to http://localhost:8080/../payment.html" 
echo "      This shows the VULNERABLE version (attack succeeds)"
echo ""
echo "   🛡️  Step 3: Click 'payment_protected.html' in your browser"
echo "      This shows the PROTECTED version (CSP blocks attack)"
echo ""
echo "4. What you'll observe:"
echo "   • Vulnerable page: SVG onload executes, skimmer activates"
echo "   • Protected page: CSP blocks inline scripts, attack fails"
echo "   • Browser console shows CSP violation reports"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping web server (PID: $SERVER_PID)..."
    kill $SERVER_PID 2>/dev/null
    echo "✅ Demo cleanup complete"
}

# Set trap to cleanup on script exit
trap cleanup EXIT

echo "Press Ctrl+C to stop the demo server..."
echo ""

# Keep script running until user stops it
wait $SERVER_PID
