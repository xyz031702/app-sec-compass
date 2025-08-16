# CVE-2019-11358 jQuery Prototype Pollution Demo - PCI-DSS 6.4.3 & 11.6.1

This project demonstrates **CVE-2019-11358** (jQuery prototype pollution → XSS) in a payment website context to showcase PCI-DSS compliance requirements 6.4.3 (secure coding practices) and 11.6.1 (security testing).

## 🚨 What is CVE-2019-11358?

CVE-2019-11358 is a prototype pollution vulnerability in jQuery versions before 3.4.0. The `$.extend(true, ...)` function can be exploited to pollute `Object.prototype`, leading to XSS and other security issues.

## 📁 Demo Components

- `payment.html` - Vulnerable payment form using jQuery 3.3.1
- `payment-processor.js` - Contains exploit code and legitimate payment processing
- `package.json` - Specifies vulnerable jQuery 3.3.1 dependency
- `web-server.py` - Serves the vulnerable payment website
- `demo.py` - Complete demonstration script

## 🎯 Attack Flow Demonstration

1. **Vulnerable Dependency**: Page loads jQuery 3.3.1 (vulnerable version)
2. **Prototype Pollution**: `$.extend(true, ...)` pollutes `Object.prototype`
3. **XSS Trigger**: Polluted properties cause XSS in DOM operations
4. **Data Theft**: XSS payload can steal payment card data

## 🚀 Running the Demo

### Quick Start
```bash
python3 demo.py
```

### Manual Setup
```bash
# Start payment website
python3 web-server.py

# Open browser to: http://localhost:3000/payment.html
# Click "Trigger jQuery Prototype Pollution → XSS" button
```

## 🔍 What to Observe

1. **XSS Alert**: Popup showing successful prototype pollution → XSS
2. **Console Logs**: Technical details of the exploit in browser console
3. **Prototype Pollution**: `Object.prototype.isAdmin` and `Object.prototype.innerHTML` are polluted
4. **DOM XSS**: Malicious HTML executed via polluted `innerHTML` property

## 🛡️ PCI-DSS Compliance Violations

### 6.4.3 - Secure Coding Practices
- ❌ Using vulnerable jQuery version (3.3.1 instead of ≥3.4.0)
- ❌ No input validation for `$.extend()` operations
- ❌ Unsafe DOM manipulation patterns
- ❌ Missing Content Security Policy (CSP)

### 11.6.1 - Security Testing Requirements  
- ❌ No Software Composition Analysis (SCA) to detect CVE-2019-11358
- ❌ Missing dependency vulnerability scanning
- ❌ No runtime security monitoring for prototype pollution

## 🔧 SCA Testing

To detect this vulnerability with SCA tools:

```bash
# Install npm dependencies
npm install

# Run npm audit to detect CVE-2019-11358
npm audit

# Expected output: High severity vulnerability in jquery@3.3.1
```

## 🛠️ Remediation

1. **Upgrade jQuery**: Update to version ≥3.4.0
   ```bash
   npm install jquery@latest
   ```

2. **Implement CSP**: Add Content Security Policy headers

3. **Input Validation**: Validate all inputs to `$.extend()` calls

4. **SCA Integration**: Use tools like Snyk, Black Duck, or npm audit in CI/CD

## ⚠️ Educational Use Only

This demonstration is for **educational and security awareness purposes only**. Do not use these techniques for malicious purposes.

NVD