from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255))

    filename: Mapped[str] = mapped_column(String(255))

    file_path: Mapped[str] = mapped_column(String(500))

    content_type: Mapped[str] = mapped_column(String(100))

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    owner = relationship("User")