from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base, TimestampMixin


class LoginHistory(Base, TimestampMixin):
    __tablename__ = "login_history"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Login Details
    # ---------------------------------
    login_time = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    logout_time = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    ip_address = Column(
        String(100),
        nullable=True,
    )

    user_agent = Column(
        String(500),
        nullable=True,
    )

    status = Column(
        String(20),
        default="SUCCESS",
        nullable=False,
        index=True,
    )

    # ---------------------------------
    # Foreign Key
    # ---------------------------------
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------------
    # Relationship
    # ---------------------------------
    user = relationship(
        "User",
        back_populates="login_history",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<LoginHistory("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"status='{self.status}')>"
        )