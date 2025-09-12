"""Pydantic schemas for Fairness resources"""

from pydantic import BaseModel
from typing import Optional, Dict, Any


class FairnessCheckRequest(BaseModel):
    project_id: str
    model_id: str
    dataset_id: str
    protected_attributes: list[str] = ["gender", "race", "age"]


class FairnessReport(BaseModel):
    id: str
    project_id: str
    model_id: str
    status: str  # "pending", "completed", "failed"
    metrics: Optional[Dict[str, Any]] = None
    created_at: str
    completed_at: Optional[str] = None


class FairnessMitigationRequest(BaseModel):
    report_id: str
    mitigation_strategy: str  # "reweighting", "threshold_optimization", etc.


class FairnessMitigationResult(BaseModel):
    id: str
    report_id: str
    strategy: str
    status: str
    improved_metrics: Optional[Dict[str, Any]] = None
    created_at: str


