import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    role_id: Mapped[str] = mapped_column(ForeignKey("roles.id"))
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(15))

    role: Mapped["Role"] = relationship("Role")
