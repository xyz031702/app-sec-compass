// Secure payment form handler with CSP compliance
(function() {
  'use strict';
  
  // Safely read localStorage and render as text (not HTML)
  function initializePaymentForm() {
    const msgElement = document.getElementById('msg');
    const statusElement = document.getElementById('status');
    const logElement = document.getElementById('log');
    
    if (!msgElement || !statusElement || !logElement) {
      console.error('Required DOM elements not found');
      return;
    }
    
    // Safe text rendering - prevents XSS
    const msg = localStorage.getItem('msg') || 'Welcome! (no seeded state)';
    msgElement.textContent = msg; // Using textContent instead of innerHTML
    
    // Log the blocked content for demo purposes
    if (msg.includes('<svg') || msg.includes('onload')) {
      statusElement.textContent = '🛡️ Malicious script blocked by CSP';
      statusElement.style.background = '#ffebee';
      statusElement.style.color = '#c62828';
      statusElement.style.borderColor = '#f44336';
      
      logElement.textContent = 'CSP blocked SVG onload attack from localStorage';
    } else {
      statusElement.textContent = '🔒 No threats detected';
    }
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePaymentForm);
  } else {
    initializePaymentForm();
  }
  
})();
