"""SQLAlchemy Project model (placeholder)"""

from sqlalchemy import Column, String

from .base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)


