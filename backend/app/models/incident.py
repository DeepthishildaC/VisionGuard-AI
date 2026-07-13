from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Incident(Base, TimestampMixin):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String(100), nullable=False)

    risk_level = Column(String(50))

    description = Column(String(500))

    camera_id = Column(
        Integer,
        ForeignKey("cameras.id")
    )

    camera = relationship(
        "Camera",
        back_populates="incidents"
    )