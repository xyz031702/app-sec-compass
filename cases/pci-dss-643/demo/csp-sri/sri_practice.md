# SRI (Subresource Integrity) Best Practices

## Overview
Subresource Integrity (SRI) is a security feature that enables browsers to verify that files they fetch are delivered without unexpected manipulation. It's essential for protecting against compromised CDNs and man-in-the-middle attacks.

## Industry Standard Practices

### 1. Build-Time Hash Generation (Recommended)

#### Webpack Configuration
```javascript
// webpack.config.js
const SubresourceIntegrityPlugin = require('webpack-subresource-integrity');

module.exports = {
  output: {
    crossOriginLoading: 'anonymous',
  },
  plugins: [
    new SubresourceIntegrityPlugin({
      hashFuncNames: ['sha256', 'sha384'],
      enabled: process.env.NODE_ENV === 'production'
    })
  ]
};
```

#### Vite Configuration
```javascript
// vite.config.js
import { defineConfig } from 'vite';
import { createHtmlPlugin } from 'vite-plugin-html';

export default defineConfig({
  plugins: [
    createHtmlPlugin({
      minify: true,
      inject: {
        data: {
          integrity: true
        }
      }
    })
  ],
  build: {
    rollupOptions: {
      output: {
        // Generate integrity hashes
        entryFileNames: '[name].[hash].js',
        chunkFileNames: '[name].[hash].js'
      }
    }
  }
});
```

### 2. Manual Hash Generation

#### Command Line Tools
```bash
# Generate SHA-256 hash
openssl dgst -sha256 -binary script.js | openssl base64 -A

# Generate SHA-384 hash (more secure)
openssl dgst -sha384 -binary script.js | openssl base64 -A

# Using shasum (alternative)
shasum -a 256 script.js | cut -d' ' -f1 | xxd -r -p | base64
```

#### Node.js Script
```javascript
const crypto = require('crypto');
const fs = require('fs');

function generateSRI(filePath) {
  const fileBuffer = fs.readFileSync(filePath);
  const hashSum = crypto.createHash('sha384');
  hashSum.update(fileBuffer);
  return 'sha384-' + hashSum.digest('base64');
}

console.log(generateSRI('./dist/app.js'));
```

### 3. CDN Usage with SRI

#### Popular CDN Examples
```html
<!-- Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" 
      rel="stylesheet" 
      integrity="sha384-9ndCyUa/+9RQbA3g/JlqKyQP13y+jvROdD1Q2eKTL3+5cGiJqmo6xt5QEdXOwpEg" 
      crossorigin="anonymous">

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js" 
        integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" 
        crossorigin="anonymous"></script>

<!-- Vue.js -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js" 
        integrity="sha384-..." 
        crossorigin="anonymous"></script>
```

## Implementation Guidelines

### HTML Template Structure
```html
<!DOCTYPE html>
<html>
<head>
    <!-- External CSS with SRI -->
    <link rel="stylesheet" 
          href="https://cdn.example.com/styles.css" 
          integrity="sha384-HASH_HERE" 
          crossorigin="anonymous">
    
    <!-- Local CSS (build-time generated) -->
    <link rel="stylesheet" 
          href="./dist/app.css" 
          integrity="sha256-BUILD_GENERATED_HASH">
</head>
<body>
    <!-- External JS with SRI -->
    <script src="https://cdn.example.com/library.js" 
            integrity="sha384-HASH_HERE" 
            crossorigin="anonymous"></script>
    
    <!-- Local JS (build-time generated) -->
    <script src="./dist/app.js" 
            integrity="sha256-BUILD_GENERATED_HASH"></script>
</body>
</html>
```

### Deployment Pipeline Integration

#### CI/CD Example (GitHub Actions)
```yaml
name: Build and Deploy
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build with SRI
        run: npm run build
        env:
          NODE_ENV: production
          
      - name: Verify SRI hashes
        run: |
          echo "Verifying generated SRI hashes..."
          grep -r "integrity=" dist/
```

## Security Considerations

### Hash Algorithm Selection
- **SHA-256**: Minimum recommended
- **SHA-384**: Better security, recommended for sensitive applications
- **SHA-512**: Maximum security, but larger hash size

### Multiple Hash Support
```html
<!-- Fallback support for multiple algorithms -->
<script src="script.js" 
        integrity="sha256-HASH1 sha384-HASH2" 
        crossorigin="anonymous"></script>
```

### CORS Requirements
```html
<!-- crossorigin="anonymous" is required for SRI -->
<script src="https://external-cdn.com/script.js" 
        integrity="sha384-HASH" 
        crossorigin="anonymous"></script>
```

## Common Pitfalls to Avoid

### ❌ Don't Do This
```nginx
# Avoid runtime hash injection in nginx
sub_filter 'integrity="PLACEHOLDER"' 'integrity="$dynamic_hash"';
```

### ❌ Missing crossorigin
```html
<!-- This will fail SRI validation -->
<script src="https://cdn.com/script.js" 
        integrity="sha384-HASH"></script>
```

### ❌ Hardcoded hashes in templates
```html
<!-- Don't hardcode hashes that change frequently -->
<script src="app.js" 
        integrity="sha256-OUTDATED_HASH"></script>
```

### ✅ Do This Instead
```javascript
// Use build tools to generate hashes automatically
// webpack.config.js with SubresourceIntegrityPlugin
// or Vite with appropriate plugins
```

## Monitoring and Maintenance

### Hash Validation Scripts
```javascript
// Validate SRI hashes during deployment
const crypto = require('crypto');
const fs = require('fs');
const cheerio = require('cheerio');

function validateSRI(htmlFile) {
  const html = fs.readFileSync(htmlFile, 'utf8');
  const $ = cheerio.load(html);
  
  $('script[integrity], link[integrity]').each((i, elem) => {
    const src = $(elem).attr('src') || $(elem).attr('href');
    const integrity = $(elem).attr('integrity');
    
    if (src && !src.startsWith('http')) {
      // Validate local files
      const filePath = path.join('./dist', src);
      const actualHash = generateSRI(filePath);
      
      if (integrity !== actualHash) {
        console.error(`SRI mismatch for ${src}`);
        process.exit(1);
      }
    }
  });
}
```

### Automated Updates
```bash
#!/bin/bash
# update-sri.sh - Regenerate SRI hashes after build

echo "Updating SRI hashes..."
npm run build

# Validate all SRI hashes
node scripts/validate-sri.js

echo "SRI validation complete!"
```

## Framework-Specific Examples

### Angular
```typescript
// angular.json
{
  "projects": {
    "app": {
      "architect": {
        "build": {
          "options": {
            "subresourceIntegrity": true
          }
        }
      }
    }
  }
}
```

### React (Create React App)
```javascript
// Use react-app-rewired with webpack-subresource-integrity
const SubresourceIntegrityPlugin = require('webpack-subresource-integrity');

module.exports = function override(config) {
  config.plugins.push(
    new SubresourceIntegrityPlugin({
      hashFuncNames: ['sha256', 'sha384']
    })
  );
  
  config.output.crossOriginLoading = 'anonymous';
  return config;
};
```

### Next.js
```javascript
// next.config.js
const SubresourceIntegrityPlugin = require('webpack-subresource-integrity');

module.exports = {
  webpack: (config) => {
    config.plugins.push(
      new SubresourceIntegrityPlugin({
        hashFuncNames: ['sha384']
      })
    );
    
    config.output.crossOriginLoading = 'anonymous';
    return config;
  }
};
```

## Conclusion

SRI should be implemented at **build time**, not runtime. Use established build tools and frameworks that automatically generate and inject integrity hashes. This approach provides better performance, maintainability, and follows industry security standards.

For PCI-DSS compliance, SRI helps satisfy requirements for protecting payment card data by ensuring the integrity of client-side scripts that handle sensitive information.
