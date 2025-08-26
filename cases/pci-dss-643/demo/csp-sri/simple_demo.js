// Simple external JavaScript file (CSP compliant)

function updateResult() {
  const input = document.getElementById('input1');
  const result = document.getElementById('result');
  
  if (input.value.trim()) {
    result.innerHTML = `<strong>You typed:</strong> ${input.value}`;
    result.style.background = '#d4edda';
    result.style.color = '#155724';
  } else {
    result.innerHTML = '<em>Please type something first</em>';
    result.style.background = '#f8d7da';
    result.style.color = '#721c24';
  }
}

// CSP violation listener
document.addEventListener('securitypolicyviolation', function(e) {
  console.log('🚫 CSP Violation:', e.violatedDirective, e.blockedURI);
});

// Simple jQuery demo when page loads
$(document).ready(function() {
  console.log('✅ jQuery loaded successfully from CDN');
  
  // Add some jQuery functionality
  $('#input1').on('keypress', function(e) {
    if (e.which === 13) { // Enter key
      updateResult();
    }
  });
});
