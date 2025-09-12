"""Audit logs API routes"""

from fastapi import APIRouter, Depends
from datetime import datetime
from typing import List

from app.dependencies import get_current_user, FirebaseUser
from app.schemas.logs import AuditLog, AuditLogQuery
from app.schemas.response import APIResponse

router = APIRouter()


@router.get("/projects/{project_id}/logs", response_model=APIResponse[List[AuditLog]])
async def get_project_audit_logs(
    project_id: str,
    limit: int = 50,
    offset: int = 0,
    action: str = None,
    resource_type: str = None,
    user_uid: str = None,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Get audit logs for a project"""
    # Mock audit logs - in production, query database with filters
    logs = [
        AuditLog(
            id="log-1",
            project_id=project_id,
            user_uid=current_user.uid,
            action="create",
            resource_type="project",
            resource_id=project_id,
            details={"name": "Sample Project"},
            timestamp=datetime.now().isoformat(),
            ip_address="192.168.1.1",
            user_agent="Mozilla/5.0..."
        ),
        AuditLog(
            id="log-2",
            project_id=project_id,
            user_uid="member-123",
            action="invite",
            resource_type="member",
            resource_id="member-123",
            details={"email": "member@example.com", "role": "member"},
            timestamp=datetime.now().isoformat(),
            ip_address="192.168.1.2",
            user_agent="Mozilla/5.0..."
        ),
        AuditLog(
            id="log-3",
            project_id=project_id,
            user_uid=current_user.uid,
            action="update",
            resource_type="project",
            resource_id=project_id,
            details={"field": "description", "old_value": "Old desc", "new_value": "New desc"},
            timestamp=datetime.now().isoformat(),
            ip_address="192.168.1.1",
            user_agent="Mozilla/5.0..."
        )
    ]
    
    # Apply filters (mock implementation)
    filtered_logs = logs
    if action:
        filtered_logs = [log for log in filtered_logs if log.action == action]
    if resource_type:
        filtered_logs = [log for log in filtered_logs if log.resource_type == resource_type]
    if user_uid:
        filtered_logs = [log for log in filtered_logs if log.user_uid == user_uid]
    
    # Apply pagination
    paginated_logs = filtered_logs[offset:offset + limit]
    
    return APIResponse(
        success=True,
        data=paginated_logs,
        message="Audit logs retrieved successfully"
    )


