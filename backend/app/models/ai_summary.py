from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class AISummary(Base, TimestampMixin):
    __tablename__ = "ai_summaries"

    id = Column(Integer, primary_key=True, index=True)

    summary = Column(
        Text,
        nullable=False
    )

    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        nullable=False
    )

    incident = relationship(
        "Incident",
        back_populates="ai_summary"
    )