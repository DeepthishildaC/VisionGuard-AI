from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Boolean
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Incident(Base, TimestampMixin):
    __tablename__ = "incidents"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Event Details
    event_type = Column(
        String(100),
        nullable=False,
        index=True
    )

    risk_level = Column(
        String(50),
        nullable=False,
        default="LOW"
    )

    description = Column(
        String(500),
        nullable=True
    )

    # AI Detection Confidence
    confidence = Column(
        Float,
        nullable=True
    )

    # Snapshot captured during incident
    image_path = Column(
        String(255),
        nullable=True
    )

    # Short video clip
    video_path = Column(
        String(255),
        nullable=True
    )

    # Status
    status = Column(
        String(30),
        default="OPEN"
    )

    # Whether security has resolved it
    is_resolved = Column(
        Boolean,
        default=False
    )

    # Camera
    camera_id = Column(
        Integer,
        ForeignKey("cameras.id"),
        nullable=False
    )

    camera = relationship(
        "Camera",
        back_populates="incidents"
    )

    def __repr__(self):
        return (
            f"<Incident(event='{self.event_type}', "
            f"risk='{self.risk_level}', "
            f"status='{self.status}')>"
        )