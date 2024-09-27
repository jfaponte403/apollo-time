import uuid

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base


class ClassroomsModel(Base):
    __tablename__ = "classrooms"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(50))
    capacity: Mapped[int] = mapped_column()
