import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.Base import Base


class DegreesModel(Base):
    __tablename__ = "degrees"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
