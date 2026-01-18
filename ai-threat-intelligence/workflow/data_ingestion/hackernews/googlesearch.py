#!/usr/bin/env python3
"""
Google Search Script for AI Threats on Hacker News
Searches for AI-related security threats and vulnerabilities on Hacker News from the last 2 weeks
"""

import requests
import json
import time
from datetime import datetime, timedelta
from urllib.parse import quote_plus
import re
import sys
import os
from dotenv import load_dotenv

class HackerNewsAIThreatSearcher:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        
        # Load environment variables from .env file in root directory
        load_dotenv()
        
        self.api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
        self.search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
        
        # AI threat-related keywords
        self.threat_keywords = [
            "AI vulnerability", "AI security", "AI attack", "AI threat",
            "machine learning vulnerability", "ML security", "AI model attack",
            "AI poisoning", "adversarial AI", "AI backdoor", "AI jailbreak",
            "LLM vulnerability", "LLM security", "ChatGPT vulnerability",
            "AI model theft", "AI privacy", "AI bias attack", "prompt injection"
        ]
    
    def set_credentials(self, api_key, search_engine_id):
        """Set Google Custom Search API credentials"""
        self.api_key = api_key
        self.search_engine_id = search_engine_id
    
    def get_date_range(self):
        """Get date range for last 2 weeks"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=14)
        return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    
    def build_search_query(self, keyword):
        """Build Google search query for Hacker News with date filtering"""
        start_date, end_date = self.get_date_range()
        
        # Site-specific search for multiple cybersecurity news sites with date range
        sites = "site:news.ycombinator.com OR site:thehackernews.com"
        # Use broader matching without strict quotes for better results
        query = f'({sites}) {keyword} after:{start_date} before:{end_date}'
        return query
    
    def search_google(self, query, start_index=1):
        """Perform Google Custom Search API request"""
        if not self.api_key or not self.search_engine_id:
            raise ValueError("API key and Search Engine ID must be set")
        
        params = {
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': query,
            'start': start_index,
            'num': 10  # Max results per request
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making search request: {e}")
            return None
    
    def extract_hn_info(self, url):
        """Extract Hacker News item ID and type from URL"""
        # Match HN URLs like https://news.ycombinator.com/item?id=12345
        match = re.search(r'news\.ycombinator\.com/item\?id=(\d+)', url)
        if match:
            return match.group(1)
        return None
    
    def format_result(self, item):
        """Format search result for display"""
        title = item.get('title', 'No title')
        link = item.get('link', '')
        snippet = item.get('snippet', 'No description')
        
        # Extract HN item ID
        hn_id = self.extract_hn_info(link)
        
        result = {
            'title': title,
            'url': link,
            'description': snippet,
            'hn_item_id': hn_id,
            'found_date': datetime.now().isoformat()
        }
        
        return result
    
    def search_ai_threats(self, max_results_per_keyword=20):
        """Search for AI threats on Hacker News"""
        all_results = []
        
        print(f"Searching for AI threats on Hacker News (last 2 weeks)")
        print(f"Date range: {self.get_date_range()[0]} to {self.get_date_range()[1]}")
        print("-" * 60)
        
        for keyword in self.threat_keywords:
            print(f"Searching for: {keyword}")
            
            query = self.build_search_query(keyword)
            results_count = 0
            start_index = 1
            
            while results_count < max_results_per_keyword:
                search_results = self.search_google(query, start_index)
                
                if not search_results or 'items' not in search_results:
                    break
                
                for item in search_results['items']:
                    if results_count >= max_results_per_keyword:
                        break
                    
                    formatted_result = self.format_result(item)
                    formatted_result['search_keyword'] = keyword
                    all_results.append(formatted_result)
                    results_count += 1
                
                # Check if there are more results
                if len(search_results['items']) < 10:
                    break
                
                start_index += 10
                time.sleep(1)  # Rate limiting
            
            print(f"Found {results_count} results for '{keyword}'")
            time.sleep(2)  # Rate limiting between keywords
        
        return all_results
    
    def save_results(self, results, output_dir=None):
        """Save results as individual JSON files"""
        if not output_dir:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = f"hn_ai_threats_{timestamp}"
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        saved_files = []
        for i, result in enumerate(results, 1):
            # Create filename based on keyword and index
            keyword_safe = result['search_keyword'].replace(' ', '_').replace('/', '_')
            filename = f"{i:03d}_{keyword_safe}_{result.get('hn_item_id', 'unknown')}.json"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            saved_files.append(filepath)
        
        # Also save a summary index file
        index_data = {
            'total_results': len(results),
            'search_date': datetime.now().isoformat(),
            'files': [os.path.basename(f) for f in saved_files],
            'keywords_summary': {}
        }
        
        # Count results by keyword
        for result in results:
            keyword = result['search_keyword']
            index_data['keywords_summary'][keyword] = index_data['keywords_summary'].get(keyword, 0) + 1
        
        index_file = os.path.join(output_dir, 'index.json')
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to directory: {output_dir}")
        print(f"Individual files: {len(saved_files)}")
        print(f"Index file: {index_file}")
        return output_dir
    
    def print_summary(self, results):
        """Print summary of search results"""
        print("\n" + "="*60)
        print("SEARCH SUMMARY")
        print("="*60)
        print(f"Total results found: {len(results)}")
        
        # Group by keyword
        keyword_counts = {}
        for result in results:
            keyword = result['search_keyword']
            keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1
        
        print("\nResults by keyword:")
        for keyword, count in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                print(f"  {keyword}: {count}")
        
        print("\nTop 5 Recent Findings:")
        for i, result in enumerate(results[:5], 1):
            print(f"\n{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Keyword: {result['search_keyword']}")
            print(f"   Description: {result['description'][:100]}...")

def main():
    """Main function to run the search"""
    searcher = HackerNewsAIThreatSearcher()
    
    # Check if API credentials are loaded from .env
    if not searcher.api_key or not searcher.search_engine_id:
        print("Error: API credentials not found in .env file")
        print("\nPlease add the following to your .env file in the root directory:")
        print("GOOGLE_SEARCH_API_KEY=your_api_key_here")
        print("GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here")
        print("\nTo get these credentials:")
        print("1. Go to https://developers.google.com/custom-search/v1/introduction")
        print("2. Create a Custom Search Engine at https://cse.google.com/")
        print("3. Get an API key from Google Cloud Console")
        sys.exit(1)
    
    print(f"Using API key: {searcher.api_key[:10]}...")
    print(f"Using search engine ID: {searcher.search_engine_id}")
    
    try:
        # Perform search
        results = searcher.search_ai_threats(max_results_per_keyword=10)
        
        if results:
            # Save results
            output_dir = searcher.save_results(results)
            
            # Print summary
            searcher.print_summary(results)
            
            print(f"\nDetailed results saved to directory: {output_dir}")
        else:
            print("No results found.")
    
    except Exception as e:
        print(f"Error during search: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()