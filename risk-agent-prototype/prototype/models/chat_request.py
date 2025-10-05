from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any

class ChatRequest(BaseModel):
    """
    Model for chat requests to the Risk Agent
    """
    message: str = Field(..., description="User message")
    conversation_id: Optional[str] = Field(default=None, description="ID of the ongoing conversation")
    context: Optional[Dict[str, Any]] = Field(default={}, description="Additional context for the conversation")
    
class ChatResponse(BaseModel):
    """
    Model for chat responses from the Risk Agent
    """
    response: str = Field(..., description="Agent's response")
    conversation_id: str = Field(..., description="ID of the conversation")
    suggested_actions: Optional[List[Dict[str, Any]]] = Field(default=[], 
                                                            description="Suggested next actions for the user")
    analysis_results: Optional[Dict[str, Any]] = Field(default={}, 
                                                     description="Any analysis results to display")
