import uuid

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey

from src.database.Base import Base
from src.models.UserModel import UserModel


class LoginModel(Base):
    __tablename__ = "login"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(100))

