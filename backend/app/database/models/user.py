from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

documents = relationship(
    "Document",
    back_populates="owner",
    cascade="all, delete-orphan",
)
owner = relationship(
    "User",
    back_populates="documents",
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))