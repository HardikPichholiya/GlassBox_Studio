"""Projects API routes with collaboration features"""

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import List

from app.dependencies import get_current_user, FirebaseUser
from app.schemas.project import (
    Project, ProjectCreate, ProjectUpdate, ProjectMember, 
    ProjectInvite, ProjectInviteByUID
)
from app.schemas.response import APIResponse

router = APIRouter()


@router.post("/projects", response_model=APIResponse[Project], status_code=201)
async def create_project(
    project_data: ProjectCreate,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Create a new project"""
    project = Project(
        id=f"proj-{datetime.now().timestamp()}",
        name=project_data.name,
        description=project_data.description,
        owner_uid=current_user.uid,
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        members=[current_user.uid]
    )
    
    return APIResponse(
        success=True,
        data=project,
        message="Project created successfully"
    )


@router.get("/projects", response_model=APIResponse[List[Project]])
async def list_projects(current_user: FirebaseUser = Depends(get_current_user)):
    """List projects for current user"""
    # Mock projects - in production, filter by user membership
    projects = [
        Project(
            id="proj-1",
            name="Demo Project 1",
            description="A sample project",
            owner_uid=current_user.uid,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            members=[current_user.uid]
        ),
        Project(
            id="proj-2",
            name="Demo Project 2",
            description="Another sample project",
            owner_uid="other-user-123",
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            members=[current_user.uid, "other-user-123"]
        )
    ]
    
    return APIResponse(
        success=True,
        data=projects,
        message="Projects retrieved successfully"
    )


@router.get("/projects/{project_id}", response_model=APIResponse[Project])
async def get_project(
    project_id: str,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Get project by ID"""
    # Mock project - in production, check user access
    project = Project(
        id=project_id,
        name="Sample Project",
        description="A detailed project description",
        owner_uid=current_user.uid,
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        members=[current_user.uid]
    )
    
    return APIResponse(
        success=True,
        data=project,
        message="Project retrieved successfully"
    )


@router.put("/projects/{project_id}", response_model=APIResponse[Project])
async def update_project(
    project_id: str,
    project_update: ProjectUpdate,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Update project"""
    # Mock update - in production, verify ownership/permissions
    project = Project(
        id=project_id,
        name=project_update.name or "Updated Project",
        description=project_update.description or "Updated description",
        owner_uid=current_user.uid,
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        members=[current_user.uid]
    )
    
    return APIResponse(
        success=True,
        data=project,
        message="Project updated successfully"
    )


@router.delete("/projects/{project_id}", response_model=APIResponse[dict])
async def delete_project(
    project_id: str,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Delete project"""
    # Mock deletion - in production, verify ownership
    return APIResponse(
        success=True,
        data={"deleted_project_id": project_id},
        message="Project deleted successfully"
    )


@router.post("/projects/{project_id}/invite", response_model=APIResponse[dict])
async def invite_user_to_project(
    project_id: str,
    invite_data: ProjectInvite,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Invite user to project by email"""
    # Mock invitation - in production, send email and create invitation record
    return APIResponse(
        success=True,
        data={
            "project_id": project_id,
            "invited_email": invite_data.email,
            "role": invite_data.role
        },
        message="User invitation sent successfully"
    )


@router.get("/projects/{project_id}/members", response_model=APIResponse[List[ProjectMember]])
async def list_project_members(
    project_id: str,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """List project members"""
    # Mock members - in production, fetch from database
    members = [
        ProjectMember(
            uid=current_user.uid,
            email=current_user.email,
            name=current_user.name,
            role="owner"
        ),
        ProjectMember(
            uid="member-123",
            email="member@example.com",
            name="Team Member",
            role="member"
        )
    ]
    
    return APIResponse(
        success=True,
        data=members,
        message="Project members retrieved successfully"
    )


@router.delete("/projects/{project_id}/members/{user_id}", response_model=APIResponse[dict])
async def remove_project_member(
    project_id: str,
    user_id: str,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Remove member from project"""
    # Mock removal - in production, verify permissions and remove from database
    return APIResponse(
        success=True,
        data={
            "project_id": project_id,
            "removed_user_id": user_id
        },
        message="Member removed from project successfully"
    )


