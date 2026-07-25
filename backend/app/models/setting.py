from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Setting(Base, TimestampMixin):
    __tablename__ = "settings"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Setting Information
    # ---------------------------------
    key = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    value = Column(
        Text,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    # ---------------------------------
    # Updated By
    # ---------------------------------
    updated_by_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    # ---------------------------------
    # Relationship
    # ---------------------------------
    updated_by = relationship(
        "User",
        back_populates="settings",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<Setting(key='{self.key}', value='{self.value}')>"
        )