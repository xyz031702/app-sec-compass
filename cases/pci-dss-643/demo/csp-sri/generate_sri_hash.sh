#!/bin/bash

# Generate SRI hash for JavaScript files
# Usage: ./generate_sri_hash.sh <filename>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <javascript_file>"
    echo "Example: $0 payment-secure.js"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

echo "Generating SRI hash for: $FILE"
echo ""

# Generate SHA-256 hash
HASH=$(openssl dgst -sha256 -binary "$FILE" | openssl base64 -A)

echo "SRI Hash (SHA-256): sha256-$HASH"
echo ""
echo "HTML Usage:"
echo "<script src=\"$FILE\" integrity=\"sha256-$HASH\" crossorigin=\"anonymous\"></script>"
echo ""

# Update the HTML file automatically if it exists
HTML_FILE="payment_protected.html"
if [ -f "$HTML_FILE" ]; then
    echo "Updating $HTML_FILE with new SRI hash..."
    sed -i "s/integrity=\"sha256-[^\"]*\"/integrity=\"sha256-$HASH\"/g" "$HTML_FILE"
    echo "✅ Updated $HTML_FILE"
else
    echo "ℹ️  HTML file not found, manual update required"
fi
