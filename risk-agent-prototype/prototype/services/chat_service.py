import asyncio
import json
import uuid
import httpx
from typing import Dict, List, Any, Optional
import os
from datetime import datetime

from models.chat_request import ChatRequest, ChatResponse

class ChatService:
    """
    Service for handling chat interactions with users
    
    This service processes user messages, maintains conversation context,
    and coordinates with other services to provide meaningful responses.
    """
    
    def __init__(self):
        # Store ongoing conversations
        self.conversations = {}
        # Configure external API endpoints if needed
        self.mcp_endpoint = os.getenv("MCP_ENDPOINT", "http://localhost:8001/api/mcp")
        self.llm_endpoint = os.getenv("LLM_ENDPOINT", "http://localhost:8002/api/llm")
        
    async def process_message(self, request: ChatRequest) -> Dict[str, Any]:
        """
        Process a user message and generate a response
        
        Args:
            request: The chat request containing the user message and context
            
        Returns:
            Dictionary with the agent's response and any additional information
        """
        # Get or create conversation ID
        conversation_id = request.conversation_id or str(uuid.uuid4())
        
        # Initialize conversation if it doesn't exist
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = {
                "messages": [],
                "context": request.context or {},
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat()
            }
        
        # Add user message to conversation history
        self.conversations[conversation_id]["messages"].append({
            "role": "user",
            "content": request.message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update conversation context if provided
        if request.context:
            self.conversations[conversation_id]["context"].update(request.context)
        
        # Update last updated timestamp
        self.conversations[conversation_id]["last_updated"] = datetime.now().isoformat()
        
        # Generate response
        response_content, suggested_actions, analysis_results = await self._generate_response(
            conversation_id, 
            request.message,
            self.conversations[conversation_id]["context"]
        )
        
        # Add agent response to conversation history
        self.conversations[conversation_id]["messages"].append({
            "role": "agent",
            "content": response_content,
            "timestamp": datetime.now().isoformat()
        })
        
        # Create response object
        response = {
            "response": response_content,
            "conversation_id": conversation_id,
            "suggested_actions": suggested_actions,
            "analysis_results": analysis_results
        }
        
        return response
    
    async def _generate_response(
        self, 
        conversation_id: str, 
        message: str, 
        context: Dict[str, Any]
    ) -> tuple[str, List[Dict[str, Any]], Dict[str, Any]]:
        """
        Generate a response to the user message
        
        This method coordinates with external LLMs or other agents to generate
        appropriate responses based on the conversation context.
        
        Args:
            conversation_id: ID of the current conversation
            message: The user's message
            context: The current conversation context
            
        Returns:
            Tuple of (response_content, suggested_actions, analysis_results)
        """
        # Get conversation history
        history = self.conversations[conversation_id]["messages"]
        
        # Try to call external LLM API
        try:
            # Prepare the request payload
            payload = {
                "messages": [
                    {"role": msg["role"], "content": msg["content"]} 
                    for msg in history
                ],
                "context": context,
                "conversation_id": conversation_id
            }
            
            # Call the LLM API
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.llm_endpoint,
                    json=payload,
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return (
                        result.get("response", ""),
                        result.get("suggested_actions", []),
                        result.get("analysis_results", {})
                    )
                else:
                    # Fallback to simulated response
                    return self._simulate_response(message, context)
                    
        except Exception as e:
            print(f"Error calling LLM API: {str(e)}")
            # Fallback to simulated response
            return self._simulate_response(message, context)
    
    def _simulate_response(
        self, 
        message: str, 
        context: Dict[str, Any]
    ) -> tuple[str, List[Dict[str, Any]], Dict[str, Any]]:
        """
        Simulate a response for demonstration purposes
        
        Args:
            message: The user's message
            context: The current conversation context
            
        Returns:
            Tuple of (response_content, suggested_actions, analysis_results)
        """
        # Simple keyword-based response generation
        message_lower = message.lower()
        
        # Check for analysis-related keywords
        if any(word in message_lower for word in ["analyze", "analysis", "scan", "check", "model"]):
            response = "I can help you analyze an AI model for security risks. Please provide the model URL or repository, and I'll start the analysis."
            suggested_actions = [
                {
                    "type": "model_analysis",
                    "label": "Start Model Analysis",
                    "payload": {
                        "action": "analyze_model"
                    }
                }
            ]
            analysis_results = {}
            
        # Check for specific model URL patterns
        elif "huggingface.co" in message_lower or "github.com" in message_lower:
            response = "I've detected a model URL in your message. Would you like me to analyze this model for security risks?"
            suggested_actions = [
                {
                    "type": "model_analysis",
                    "label": "Analyze This Model",
                    "payload": {
                        "action": "analyze_model",
                        "model_url": message
                    }
                }
            ]
            analysis_results = {}
            
        # Check for help-related keywords
        elif any(word in message_lower for word in ["help", "how", "what can you do", "capabilities"]):
            response = """I'm your AI Risk Agent Assistant. I can help you with:
1. Analyzing AI models for security risks and vulnerabilities
2. Explaining security findings and their implications
3. Recommending mitigation strategies for identified risks
4. Answering questions about AI security best practices

What would you like to know more about?"""
            suggested_actions = [
                {
                    "type": "info",
                    "label": "Model Analysis Capabilities",
                    "payload": {
                        "action": "show_info",
                        "topic": "analysis_capabilities"
                    }
                },
                {
                    "type": "info",
                    "label": "Security Best Practices",
                    "payload": {
                        "action": "show_info",
                        "topic": "security_best_practices"
                    }
                }
            ]
            analysis_results = {}
            
        # Default response
        else:
            response = "I'm here to help you analyze AI models for security risks. Can you provide more details about what you'd like to do?"
            suggested_actions = []
            analysis_results = {}
            
        return response, suggested_actions, analysis_results
    
    async def get_conversation(self, conversation_id: str) -> Dict[str, Any]:
        """
        Get the full conversation history and context
        
        Args:
            conversation_id: ID of the conversation to retrieve
            
        Returns:
            Dictionary with the conversation data
            
        Raises:
            Exception if the conversation ID is not found
        """
        if conversation_id not in self.conversations:
            raise Exception(f"Conversation ID {conversation_id} not found")
        
        return self.conversations[conversation_id]
