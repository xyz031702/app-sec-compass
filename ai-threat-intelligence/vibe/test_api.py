#!/usr/bin/env python3
"""
Simple API test for Google Gen AI SDK
Tests if the Gemini API key is valid and working
"""

import os
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv

def test_api_key():
    """Test if the Gemini API key is valid"""
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        print("Make sure you have a .env file with your API key")
        return False
    
    print(f"🔑 API Key found: {api_key[:8]}...")
    
    try:
        # Initialize client for Gemini API (simpler approach)
        print("🔧 Initializing Google Gen AI client...")
        client = genai.Client(api_key=api_key)
        
        # Simple test prompt
        print("📡 Testing API connection with simple prompt...")
        # First, let's list available models to see what's supported
        print("📋 Checking available models...")
        try:
            models = list(client.models.list())
            print(f"Available models: {[model.name for model in models[:3]]}")  # Show first 3
        except Exception as e:
            print(f"Could not list models: {e}")
        
        # Try with a more standard model name
        response = client.models.generate_content(
            model='models/gemini-2.5-flash',
            contents="Say 'Hello World' and confirm you are Gemini AI",
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=100
            )
        )
        
        print("✅ API test successful!")
        print(f"📝 Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        print("\nPossible issues:")
        print("- Invalid API key")
        print("- Network connectivity problems")
        print("- API quota exceeded")
        print("- Service temporarily unavailable")
        return False

if __name__ == "__main__":
    print("🧪 Testing Gemini API Key...")
    print("=" * 50)
    
    success = test_api_key()
    
    print("=" * 50)
    if success:
        print("🎉 Your API key is working! You can now run the main threat intelligence script.")
    else:
        print("🔧 Please fix the API key issue before running the main script.")
