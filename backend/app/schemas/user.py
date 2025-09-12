"""Pydantic schemas for User resources"""

from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    uid: str
    email: EmailStr
    name: Optional[str] = ""
    avatar_url: Optional[str] = None
    created_at: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    avatar_url: Optional[str] = None


