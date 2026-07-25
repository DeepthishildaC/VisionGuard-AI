from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.sql import func

from app.models.base import Base, TimestampMixin


class TokenBlacklist(Base, TimestampMixin):
    __tablename__ = "token_blacklist"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ---------------------------------
    # JWT Token
    # ---------------------------------
    token = Column(
        String(500),
        nullable=False,
        unique=True,
        index=True,
    )

    token_type = Column(
        String(20),
        nullable=False,
        default="ACCESS",
    )

    # ---------------------------------
    # Revocation Details
    # ---------------------------------
    revoked_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    expires_at = Column(
        DateTime(timezone=True),
        nullable=False,
    )

    # ---------------------------------
    # String Representation
    # ---------------------------------
    def __repr__(self):
        return (
            f"<TokenBlacklist("
            f"id={self.id}, "
            f"type='{self.token_type}')>"
        )