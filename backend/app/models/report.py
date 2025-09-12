"""SQLAlchemy Report model (placeholder)"""

from sqlalchemy import Column, String

from .base import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True)
    project_id = Column(String, nullable=False)
    summary = Column(String, nullable=False)


