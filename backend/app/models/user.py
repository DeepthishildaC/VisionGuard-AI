from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Basic Information
    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    # Authentication
    hashed_password = Column(
        String(255),
        nullable=False,
    )

    # Account Status
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_locked = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    # User Profile
    profile_image = Column(
        String(255),
        nullable=True,
    )

    # Login Tracking
    last_login = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Foreign Key
    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False,
    )

    # Relationships
    role = relationship(
        "Role",
        back_populates="users",
    )

    chat_history = relationship(
        "ChatHistory",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    reports = relationship(
        "Report",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    login_history = relationship(
        "LoginHistory",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    incidents_resolved = relationship(
        "Incident",
        back_populates="resolved_by",
    )

    audit_logs = relationship(
        "AuditLog",
        back_populates="user",
    )

    settings = relationship(
        "Setting",
        back_populates="updated_by",
    )

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"