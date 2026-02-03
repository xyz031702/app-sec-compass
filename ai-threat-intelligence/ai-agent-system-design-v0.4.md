
# Data Harvesting using Google Alerts

## Google Alerts Configuration

For easy setup, copy the following queries directly into Google Alerts:

1. **Breaking News (Daily):**  
   `"AI vulnerability disclosed" OR "LLM breach" OR "prompt injection attack" OR "model theft" OR "data poisoning incident" OR "AI CVE"`

2. **Research - ArXiv (Weekly):**  
   `site:arxiv.org ("LLM security" OR "adversarial attack" OR "prompt injection" OR "jailbreak" OR "AI alignment" OR "model robustness")`

3. **Research - Academic (Weekly):**  
   `(site:semanticscholar.org OR site:aclanthology.org OR site:openreview.net) ("LLM security" OR "adversarial attack" OR "prompt injection" OR "AI safety")`

4. **Tools & Releases (Weekly):**  
   `(site:github.com OR site:huggingface.co) ("AI security" OR "LLM security" OR "ML security") (tool OR scanner OR framework)`

5. **Regulation & Policy (Weekly):**  
   `"AI regulation" OR "AI safety law" OR "EU AI Act" OR "AI governance" OR "AI compliance framework" OR "AI liability"`

6. **Singapore & Regional (Weekly):**  
   `(Singapore OR MAS OR IMDA OR CSA OR GovTech OR ASEAN OR "Southeast Asia") (AI OR LLM) (security OR governance OR regulation OR guideline OR framework OR policy)`


## Gmail Filter Setup

All Google Alerts come from the same sender, so one filter handles everything:

### Steps to Create Filter

1. In Gmail, click the **search bar** at the top
2. Click the small **down arrow** on the right (Show search options)
3. In the **"From"** field, enter: `googlealerts-noreply@google.com`
4. Click **"Create filter"**
5. Check these options:
   - **Skip the Inbox (Archive it)** — keeps it out of your main view
   - **Apply the label** — create a new label like "AI Security News"
   - **Optional:** Mark as read if you only want to check it when you feel like it
6. Click **"Create filter"**

This will automatically organize all AI security alerts into a dedicated label for easy review and processing.