"""Pydantic schemas for Project resources"""

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = ""
    owner_uid: str
    created_at: str
    updated_at: str
    members: List[str] = []  # List of user UIDs


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = ""


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectMember(BaseModel):
    uid: str
    email: str
    name: str
    role: str = "member"


class ProjectInvite(BaseModel):
    email: EmailStr
    role: str = "member"


class ProjectInviteByUID(BaseModel):
    uid: str
    role: str = "member"


