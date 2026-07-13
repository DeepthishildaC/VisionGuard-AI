from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Detection(Base, TimestampMixin):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)

    object_type = Column(
        String(100),
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    track_id = Column(
        Integer,
        nullable=True
    )

    bounding_box = Column(
        String(255),
        nullable=True
    )

    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        nullable=False
    )

    incident = relationship(
        "Incident",
        back_populates="detections"
    )