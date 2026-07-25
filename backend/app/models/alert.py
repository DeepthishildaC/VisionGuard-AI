from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Alert(Base, TimestampMixin):
    __tablename__ = "alerts"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Alert Information
    # ---------------------------------
    title = Column(
        String(200),
        nullable=False,
    )

    message = Column(
        String(500),
        nullable=False,
    )

    severity = Column(
        String(50),
        default="MEDIUM",
        nullable=False,
    )

    status = Column(
        String(30),
        default="ACTIVE",
        nullable=False,
    )

    # ---------------------------------
    # Read Status
    # ---------------------------------
    is_read = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    # ---------------------------------
    # Foreign Key
    # ---------------------------------
    incident_id = Column(
        Integer,
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------------
    # Relationship
    # ---------------------------------
    incident = relationship(
        "Incident",
        back_populates="alerts",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<Alert("
            f"id={self.id}, "
            f"title='{self.title}', "
            f"severity='{self.severity}', "
            f"status='{self.status}', "
            f"is_read={self.is_read})>"
        )