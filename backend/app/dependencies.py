"""Dependencies for dependency injection"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Mock Firebase user model - replace with actual Firebase verification
class FirebaseUser:
    def __init__(self, uid: str, email: str, name: str = ""):
        self.uid = uid
        self.email = email
        self.name = name


security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> FirebaseUser:
    """
    Mock Firebase token verification.
    In production, verify the Firebase token here.
    """
    # Mock implementation - replace with actual Firebase verification
    if not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Mock user data - replace with actual Firebase token verification
    return FirebaseUser(
        uid="mock-user-123",
        email="user@example.com",
        name="Mock User"
    )


