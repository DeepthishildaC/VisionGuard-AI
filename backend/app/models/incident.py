from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Incident(Base, TimestampMixin):
    __tablename__ = "incidents"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Incident Details
    # ---------------------------------
    event_type = Column(
        String(100),
        nullable=False,
        index=True,
    )

    risk_level = Column(
        String(50),
        default="LOW",
        nullable=False,
        index=True,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    # ---------------------------------
    # AI Detection Information
    # ---------------------------------
    confidence = Column(
        Float,
        nullable=True,
    )

    image_path = Column(
        String(255),
        nullable=True,
    )

    video_path = Column(
        String(255),
        nullable=True,
    )

    # ---------------------------------
    # Incident Status
    # ---------------------------------
    status = Column(
        String(30),
        default="OPEN",
        nullable=False,
        index=True,
    )

    is_resolved = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    # ---------------------------------
    # Foreign Keys
    # ---------------------------------
    camera_id = Column(
        Integer,
        ForeignKey("cameras.id"),
        nullable=False,
        index=True,
    )

    resolved_by_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    # ---------------------------------
    # Relationships
    # ---------------------------------
    camera = relationship(
        "Camera",
        back_populates="incidents",
    )

    resolved_by = relationship(
        "User",
        back_populates="incidents_resolved",
    )

    alerts = relationship(
        "Alert",
        back_populates="incident",
    )

    ai_summary = relationship(
        "AISummary",
        back_populates="incident",
        uselist=False,
    )

    detections = relationship(
        "Detection",
        back_populates="incident",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<Incident("
            f"id={self.id}, "
            f"event='{self.event_type}', "
            f"risk='{self.risk_level}', "
            f"status='{self.status}')>"
        )