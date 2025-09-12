"""Pydantic schemas for Audit Log resources"""

from pydantic import BaseModel
from typing import Optional, Dict, Any


class AuditLog(BaseModel):
    id: str
    project_id: str
    user_uid: str
    action: str  # "create", "update", "delete", "invite", "remove", etc.
    resource_type: str  # "project", "model", "dataset", "member", etc.
    resource_id: str
    details: Optional[Dict[str, Any]] = None
    timestamp: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None


class AuditLogQuery(BaseModel):
    project_id: str
    limit: int = 50
    offset: int = 0
    action: Optional[str] = None
    resource_type: Optional[str] = None
    user_uid: Optional[str] = None


