i want a landing html for 3 experiments

1. card number skimmer
- through vulnerable jQuery 3.3.1
  - run the clear.html, 
  - run the payment_jquery.html to show no injection
  - run seed.html to inject
  - run the payment_jquery.html to show injection
- through XSS
  - run the clear.html, 
  - run the payment.html to show no injection
  - run seed.html to inject
  - run the payment.html to show injection

2. add CSP and SRI to protect
  - go into csp-sri folder
  - run the demo.sh to start a local server
  - click [seed.html](http://localhost:8080/seed.html) to inject, check injected content: console--> application--> localStorage---> localhost:8080
  - click [payment_vulnerable.html](http://localhost:8080/payment_vulnerable.html) to show injection
  - click [payment_protected.html](http://localhost:8080/payment_protected.html) to show no injection,   futher show the 'error' from CSP block in console
  - click [csp-sri-guide.html](http://localhost:8080/csp-sri-guide.html) to show the guide


3. Sometimes CSP and SRI cannot blocks all attacks
- go into jquery_failed folder
- open index.html
- open console to show the DOM-XSS attack
- enter sth to show cardnumber is still skimmered

4. CSP/SRI limitations
- Some libraries don't provide SRI hashes (e.g., Stripe.js): https://github.com/stripe/stripe-js/issues/167
- Rare case: Corporate SSL inspection can intercept and modify content (requires pre-configured trust)
- Rare case: CDN/infrastructure compromises at the source can serve malicious code from trusted domains
