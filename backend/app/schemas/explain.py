"""Pydantic schemas for Explainability resources"""

from pydantic import BaseModel
from typing import Optional, Dict, Any, List


class ExplainRequest(BaseModel):
    project_id: str
    model_id: str
    explanation_type: str = "shap"  # "shap", "lime", "integrated_gradients"
    sample_data: Optional[Dict[str, Any]] = None


class ExplanationTask(BaseModel):
    id: str
    project_id: str
    model_id: str
    explanation_type: str
    status: str  # "pending", "completed", "failed"
    created_at: str
    completed_at: Optional[str] = None


class ExplanationResult(BaseModel):
    task_id: str
    explanation_type: str
    feature_importance: List[Dict[str, Any]]
    summary: Optional[str] = None
    visualizations: Optional[List[str]] = None  # URLs to generated charts
    created_at: str


