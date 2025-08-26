# CSP + SRI Protection Demo

This demo shows how **Content Security Policy (CSP)** and **Subresource Integrity (SRI)** can block script tampering attacks from phishing emails.

## Demo Scenario

**Attack Vector**: Phishing email contains malicious JavaScript that seeds a payment card skimmer into `localStorage`. When users visit the payment page, the malicious script executes via SVG `onload` event.

## Files

- `seed.html` - Simulates phishing email seeding malicious JavaScript
- `payment_protected.html` - CSP + SRI protected payment page  
- `payment-secure.js` - Secure JavaScript with SRI integrity hash
- `generate_sri_hash.sh` - Script to generate SRI hashes
- `demo.sh` - Complete demo runner script

## Quick Start

```bash
# Run the complete demo
./demo.sh
```

## Manual Steps

1. **Generate SRI Hash**:
   ```bash
   ./generate_sri_hash.sh payment-secure.js
   ```

2. **Start Web Server**:
   ```bash
   python3 -m http.server 8080
   ```

3. **Test Attack Flow**:
   - Visit `http://localhost:8080/seed.html` (seed malicious payload)
   - Visit `http://localhost:8080/../payment.html` (vulnerable - attack succeeds)
   - Visit `http://localhost:8080/payment_protected.html` (protected - attack blocked)

## Security Controls

### Content Security Policy (CSP)
```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'sha256-HASH';
  style-src 'self' 'unsafe-inline';
  object-src 'none';
">
```

**Blocks**:
- Inline scripts (`<script>` tags without src)
- `eval()` and similar dynamic code execution
- SVG `onload` events
- Unauthorized script sources

### Subresource Integrity (SRI)
```html
<script src="payment-secure.js" 
        integrity="sha256-HASH" 
        crossorigin="anonymous"></script>
```

**Prevents**:
- Script tampering via CDN compromise
- Man-in-the-middle script modification
- Supply chain attacks on external scripts

## Expected Results

| Page | Attack Result | Reason |
|------|---------------|---------|
| Vulnerable | ⚠️ Skimmer Active | `innerHTML` renders SVG with `onload` |
| Protected | 🛡️ Attack Blocked | CSP blocks inline scripts, safe text rendering |

## Browser Console Output

**Protected Page**:
```
Content Security Policy: The page's settings blocked the loading of a resource at inline ("script-src").
```

**CSP Violation Event**:
```javascript
{
  violatedDirective: "script-src",
  blockedURI: "inline",
  sourceFile: "payment_protected.html"
}
```
