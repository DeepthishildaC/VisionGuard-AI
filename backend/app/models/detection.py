from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Detection(Base, TimestampMixin):
    __tablename__ = "detections"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Object Detection Details
    # ---------------------------------
    object_type = Column(
        String(100),
        nullable=False,
        index=True,
    )

    confidence = Column(
        Float,
        nullable=False,
    )

    # ByteTrack Object ID
    track_id = Column(
        Integer,
        nullable=True,
        index=True,
    )

    # Bounding Box
    # Format: x1,y1,x2,y2
    bounding_box = Column(
        String(255),
        nullable=True,
    )

    # ---------------------------------
    # Foreign Keys
    # ---------------------------------
    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------------
    # Relationships
    # ---------------------------------
    incident = relationship(
        "Incident",
        back_populates="detections",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<Detection("
            f"id={self.id}, "
            f"object='{self.object_type}', "
            f"confidence={self.confidence})>"
        )