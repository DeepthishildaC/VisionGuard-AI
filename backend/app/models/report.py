from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Report(Base, TimestampMixin):
    __tablename__ = "reports"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Report Details
    # ---------------------------------
    report_name = Column(
        String(255),
        nullable=False,
        index=True,
    )

    report_type = Column(
        String(50),
        nullable=False,
        default="Daily",
    )

    description = Column(
        Text,
        nullable=True,
    )

    file_path = Column(
        String(255),
        nullable=False,
    )

    status = Column(
        String(20),
        default="GENERATED",
        nullable=False,
    )

    # ---------------------------------
    # Foreign Key
    # ---------------------------------
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------------
    # Relationships
    # ---------------------------------
    user = relationship(
        "User",
        back_populates="reports",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<Report("
            f"id={self.id}, "
            f"name='{self.report_name}', "
            f"type='{self.report_type}')>"
        )