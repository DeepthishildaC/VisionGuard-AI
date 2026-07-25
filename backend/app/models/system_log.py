from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)

from app.models.base import Base, TimestampMixin


class SystemLog(Base, TimestampMixin):
    __tablename__ = "system_logs"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Log Details
    # ---------------------------------
    level = Column(
        String(20),
        nullable=False,
        default="INFO",
        index=True,
    )

    source = Column(
        String(100),
        nullable=False,
    )

    message = Column(
        Text,
        nullable=False,
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<SystemLog(level='{self.level}', source='{self.source}')>"
        )