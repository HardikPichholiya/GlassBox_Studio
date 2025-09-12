"""Standardized response schemas for all API endpoints"""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class APIResponse(BaseModel, Generic[T]):
    """Standard API response format"""
    success: bool
    data: T
    message: str


class ErrorResponse(BaseModel):
    """Error response format"""
    success: bool = False
    data: None = None
    message: str


