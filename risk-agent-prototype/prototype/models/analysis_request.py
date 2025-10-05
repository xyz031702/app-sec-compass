from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from enum import Enum

class AnalysisType(str, Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"
    BEHAVIORAL = "behavioral"
    COMPREHENSIVE = "comprehensive"

class AnalysisRequest(BaseModel):
    """
    Model for requesting an analysis of an AI model
    """
    model_url: str = Field(..., description="URL to the model (e.g., Hugging Face repository)")
    analysis_type: AnalysisType = Field(default=AnalysisType.COMPREHENSIVE, 
                                      description="Type of analysis to perform")
    environment_info: Optional[Dict[str, Any]] = Field(default={}, 
                                                     description="Information about the environment")
    test_target: Optional[Dict[str, Any]] = Field(default={}, 
                                                description="Specific test targets or parameters")
    additional_context: Optional[Dict[str, Any]] = Field(default={}, 
                                                       description="Any additional context for the analysis")
