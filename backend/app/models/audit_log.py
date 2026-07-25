from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Audit Information
    # ---------------------------------
    action = Column(
        String(100),
        nullable=False,
        index=True,
    )

    resource = Column(
        String(100),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    ip_address = Column(
        String(100),
        nullable=True,
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
        back_populates="audit_logs",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<AuditLog("
            f"id={self.id}, "
            f"action='{self.action}', "
            f"resource='{self.resource}')>"
        )