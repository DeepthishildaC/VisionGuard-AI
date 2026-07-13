from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    role = relationship(
        "Role",
        back_populates="users"
    )