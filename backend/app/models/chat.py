from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class ChatHistory(Base, TimestampMixin):
    __tablename__ = "chat_history"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # Chat Information
    # ---------------------------------
    question = Column(
        Text,
        nullable=False,
    )

    answer = Column(
        Text,
        nullable=False,
    )

    model_name = Column(
        String(100),
        default="Gemini",
        nullable=False,
    )

    response_time = Column(
        String(20),
        nullable=True,
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
        back_populates="chat_history",
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<ChatHistory("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"model='{self.model_name}')>"
        )