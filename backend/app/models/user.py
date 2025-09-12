"""SQLAlchemy User model (placeholder)"""

from sqlalchemy import Column, String

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)


