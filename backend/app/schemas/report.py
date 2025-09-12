"""Pydantic schemas for Report resources (placeholder)"""

from pydantic import BaseModel


class Report(BaseModel):
  id: str
  project_id: str
  summary: str


