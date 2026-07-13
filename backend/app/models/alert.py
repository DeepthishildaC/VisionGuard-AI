from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Alert(Base, TimestampMixin):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(
        String(200),
        nullable=False
    )

    message = Column(
        String(500),
        nullable=False
    )

    severity = Column(
        String(50),
        default="Medium"
    )

    is_read = Column(
        Boolean,
        default=False
    )

    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        nullable=False
    )

    incident = relationship(
        "Incident",
        back_populates="alerts"
    )