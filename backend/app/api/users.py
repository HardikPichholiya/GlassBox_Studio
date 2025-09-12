"""User management API endpoints"""

from fastapi import APIRouter, Depends
from datetime import datetime

from app.dependencies import get_current_user, FirebaseUser
from app.schemas.user import User, UserUpdate
from app.schemas.response import APIResponse

router = APIRouter()


@router.get("/users/me", response_model=APIResponse[User])
async def get_current_user_info(current_user: FirebaseUser = Depends(get_current_user)):
    """Get current user information"""
    user_data = User(
        uid=current_user.uid,
        email=current_user.email,
        name=current_user.name,
        avatar_url=None,
        created_at=datetime.now().isoformat()
    )
    
    return APIResponse(
        success=True,
        data=user_data,
        message="User information retrieved successfully"
    )


@router.put("/users/me", response_model=APIResponse[User])
async def update_current_user(
    user_update: UserUpdate,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Update current user profile"""
    # Mock update logic - in production, update in database
    updated_user = User(
        uid=current_user.uid,
        email=current_user.email,
        name=user_update.name or current_user.name,
        avatar_url=user_update.avatar_url,
        created_at=datetime.now().isoformat()
    )
    
    return APIResponse(
        success=True,
        data=updated_user,
        message="User profile updated successfully"
    )


