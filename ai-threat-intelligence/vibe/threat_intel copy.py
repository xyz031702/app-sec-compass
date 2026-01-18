#!/usr/bin/env python3
"""
AI Threat Intelligence Generator v0.3 MVP
Ultra-simple single-call approach using Gemini deep thinking
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv

class ThreatIntelligenceV3:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.client = genai.Client(api_key=api_key)
        self.model = 'models/gemini-2.5-pro'
        
    def generate_report(self) -> str:
        """Generate complete threat intelligence report with single API call"""
        
        # Calculate date range for last 2 weeks
        end_date = datetime.now()
        start_date = end_date - timedelta(days=14)
        
        # Build comprehensive prompt with date context
        prompt = self._build_prompt(start_date, end_date)
        
        print(f"Generating AI threat intelligence report...")
        print(f"Analysis period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0,
                    max_output_tokens=8192,
                    top_p=0.8,
                    top_k=40
                )
            )
            
            return self._format_output(response.text, start_date, end_date)
            
        except Exception as e:
            return f"Error generating report: {str(e)}"
    
    def _build_prompt(self, start_date: datetime, end_date: datetime) -> str:
        """Build the master prompt with current date context"""
        
        date_context = f"""
CURRENT DATE CONTEXT:
- Report Generation Date: {end_date.strftime('%Y-%m-%d')}
- Analysis Period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}
- Focus: Last 14 days of AI security developments
        """
        
        master_prompt = """
You are a threat intelligence analyst focused on the AI domain with deep thinking capabilities enabled.

MISSION:
Generate a comprehensive executive summary on the AI security landscape from the specified analysis period.

DEEP THINKING INSTRUCTIONS:
1. Use your advanced reasoning to systematically research recent AI security developments
2. Think through multiple information sources and cross-reference findings
3. Apply critical analysis to separate significant developments from noise
4. Consider the broader implications and interconnections between events
5. Validate information accuracy through logical reasoning

RESEARCH FOCUS:
- Target AI systems and models security (NOT how to leverage AI for existing cybersecurity)
- Prioritize main news sources like HackerNews over vendor blogs
- Focus on developments with real business and technical impact
- Consider both immediate threats and emerging trends

CRITICAL REQUIREMENT - SOURCE URLS:
For EVERY finding, development, incident, tool, or research mentioned, you MUST provide the original web URL source. Format each item as:
- **[Title/Description]** - [Brief summary]
  - Source: [Full URL]
  - Impact: [Business/technical impact]

IMPORTANT CONSTRAINTS:
- DO NOT fabricate specific recent events, incidents, or news stories
- DO NOT create fake URLs, CVE numbers, or specific dates
- DO NOT claim knowledge of events after your training data cutoff
- Focus on established patterns, known threat categories, and proven frameworks
- When discussing examples, clearly label them as "hypothetical" or "example scenarios"

REQUIRED OUTPUT STRUCTURE:
Generate exactly 5 sections with detailed analysis and URLs:

## 1. Key News & Announcements
What major stories broke in AI security? Include:
- Significant policy changes or regulatory developments
- Major company announcements related to AI security
- Industry-wide initiatives or standards updates
- High-profile AI security incidents that made headlines

For each item, provide:
- **[Headline]** - [Summary]
  - Source: [URL]
  - Impact: [Assessment]

## 2. Significant Incidents  
What new vulnerabilities, exploits, or model-related incidents were disclosed?
Focus on:
- Prompt injections and jailbreaking techniques
- Data poisoning attacks on training datasets
- Model theft and extraction attempts
- Training data leaks or privacy breaches
- Supply chain attacks on AI systems

For each incident, provide:
- **[Incident Title]** - [Technical details]
  - Source: [URL]
  - CVE/ID: [If applicable]
  - Impact: [Risk assessment]

## 3. New Offensive/Defensive Approaches
Highlight notable new attack techniques or defensive research:
- Novel attack vectors against AI systems
- Advanced evasion techniques
- New defensive frameworks and methodologies
- Research papers with practical security implications
- Emerging threat patterns and attack trends

For each approach, provide:
- **[Research/Technique Title]** - [Description]
  - Source: [URL to paper/article]
  - Authors/Organization: [If applicable]
  - Impact: [Practical implications]

## 4. New Tooling
New open-source or commercial tools for securing the AI/ML pipeline:
- Security scanners for AI/ML systems
- Vulnerability assessment tools for models
- Privacy-preserving ML frameworks
- AI red-teaming and testing tools
- Monitoring and detection systems

For each tool, provide:
- **[Tool Name]** - [Functionality description]
  - Source: [GitHub/project URL]
  - License: [If open source]
  - Impact: [Adoption potential]

## 5. Executive Summary
Provide a concise synthesis covering:
- Most critical developments and their business impact
- Emerging threat trends requiring attention
- Recommended actions for organizations
- Strategic implications for AI security posture

Include key source references for major findings.

DEEP THINKING PROCESS:
Before generating each section, engage in deep reasoning:
1. What are the most significant developments in this category?
2. How do these developments interconnect with broader AI security trends?
3. What are the immediate and long-term implications?
4. Which sources and information are most credible and actionable?
5. How should executives prioritize their response to these developments?

QUALITY STANDARDS:
- Each section must contain substantive, actionable intelligence
- All information must be from the specified time period
- Focus on credible sources and verified information
- Provide specific technical details where relevant
- Include business impact assessment for each major development
- Maintain executive-level clarity and conciseness
- MANDATORY: Every finding must include original source URL

URL REQUIREMENTS:
- Provide complete, clickable URLs (https://...)
- Use authoritative sources (HackerNews, GitHub, arXiv, major outlets)
- Verify URL accuracy and accessibility
- Include direct links to papers, tools, and articles
- For GitHub tools, link to main repository page
- For research papers, link to arXiv or conference proceedings

CRITICAL CONSTRAINTS:
- Only include developments from the specified analysis period
- Exclude vendor marketing content and promotional materials
- Focus on AI/ML system security, not AI applications in cybersecurity
- Prioritize HackerNews and major security outlets over vendor blogs
- Ensure all 5 sections are populated with quality content
- EVERY item must have a verifiable source URL

Begin your deep thinking analysis and generate the comprehensive executive summary with complete source attribution.
"""
        
        return f"{date_context}\n\n{master_prompt}"
    
    def _format_output(self, content: str, start_date: datetime, end_date: datetime) -> str:
        """Format the final report with metadata"""
        
        header = f"""# AI Security Landscape - Executive Summary

**Analysis Period:** {start_date.strftime('%B %d, %Y')} - {end_date.strftime('%B %d, %Y')}  
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}  
**Method:** Gemini Deep Thinking Analysis  
**Version:** v0.3 MVP

---

"""
        
        footer = f"""

---

**Report Metadata:**
- **Analysis Method:** Single Gemini API call with deep thinking mode
- **Time Scope:** 14-day lookback period
- **Focus Areas:** AI/ML system security (excluding AI-for-cybersecurity)
- **Source Priority:** HackerNews and major security outlets
- **Quality Assurance:** Self-validated by Gemini advanced reasoning

**Next Report:** {(end_date + timedelta(days=7)).strftime('%Y-%m-%d')}
"""
        
        return header + content + footer

def main():
    """Main execution function"""
    try:
        # Initialize system
        intel_system = ThreatIntelligenceV3()
        
        # Generate report
        report = intel_system.generate_report()
        
        # Create output directory
        output_dir = Path("reports")
        output_dir.mkdir(exist_ok=True)
        
        # Save report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = output_dir / f"ai_threat_intel_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Report generated successfully: {filename}")
        print(f"📊 Report size: {len(report)} characters")
        
        # Also print to console for immediate viewing
        if len(sys.argv) > 1 and sys.argv[1] == "--show":
            print("\n" + "="*80)
            print("GENERATED REPORT:")
            print("="*80)
            print(report)
        
        return str(filename)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

if __name__ == "__main__":
    main()
