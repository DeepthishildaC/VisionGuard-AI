from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class AISummary(Base, TimestampMixin):
    __tablename__ = "ai_summaries"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    summary = Column(
        Text,
        nullable=False,
    )

    model_name = Column(
        String(100),
        nullable=False,
    )

    confidence = Column(
        String(20),
        nullable=True,
    )

    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        unique=True,
        nullable=False,
        index=True,
    )

    incident = relationship(
        "Incident",
        back_populates="ai_summary",
    )

    def __repr__(self):
        return (
            f"<AISummary(id={self.id}, incident_id={self.incident_id})>"
        )