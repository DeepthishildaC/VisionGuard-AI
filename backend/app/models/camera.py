from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Camera(Base, TimestampMixin):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)

    camera_name = Column(
        String(100),
        nullable=False,
        index=True
    )

    location = Column(
        String(255),
        nullable=False
    )

    stream_url = Column(
        String(255),
        nullable=False
    )

    ip_address = Column(
        String(100),
        unique=True,
        nullable=True
    )

    camera_type = Column(
        String(50),
        default="IP Camera"
    )

    resolution = Column(
        String(50),
        default="1920x1080"
    )

    fps = Column(
        Integer,
        default=30
    )

    status = Column(
        String(20),
        default="ONLINE"
    )

    ai_enabled = Column(
        Boolean,
        default=True
    )

    incidents = relationship(
        "Incident",
        back_populates="camera"
    )

    def __repr__(self):
        return f"<Camera(name='{self.camera_name}', status='{self.status}')>"