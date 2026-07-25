from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Camera(Base, TimestampMixin):
    __tablename__ = "cameras"

    # -----------------------------
    # Primary Key
    # -----------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # -----------------------------
    # Camera Information
    # -----------------------------
    camera_name = Column(
        String(100),
        nullable=False,
        index=True,
    )

    location = Column(
        String(255),
        nullable=False,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    # -----------------------------
    # Stream Information
    # -----------------------------
    stream_url = Column(
        String(255),
        nullable=False,
    )

    ip_address = Column(
        String(100),
        unique=True,
        nullable=True,
    )

    camera_type = Column(
        String(50),
        default="IP Camera",
        nullable=False,
    )

    # -----------------------------
    # Video Configuration
    # -----------------------------
    resolution = Column(
        String(50),
        default="1920x1080",
        nullable=False,
    )

    fps = Column(
        Integer,
        default=30,
        nullable=False,
    )

    # -----------------------------
    # Camera Status
    # -----------------------------
    status = Column(
        String(20),
        default="ONLINE",
        nullable=False,
    )

    ai_enabled = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_seen = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    # -----------------------------
    # Relationships
    # -----------------------------
    incidents = relationship(
        "Incident",
        back_populates="camera",
    )

    # -----------------------------
    # String Representation
    # -----------------------------
    def __repr__(self):
        return (
            f"<Camera("
            f"id={self.id}, "
            f"name='{self.camera_name}', "
            f"status='{self.status}')>"
        )