from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Camera(Base, TimestampMixin):

    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)

    camera_name = Column(String(100), nullable=False)

    location = Column(String(200))

    ip_address = Column(String(100), unique=True)

    is_active = Column(Boolean, default=True)

    incidents = relationship(
        "Incident",
        back_populates="camera"
    )