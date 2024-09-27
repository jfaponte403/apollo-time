import uuid

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base


class TeacherModel(Base):
    __tablename__ = "teachers"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    salary: Mapped[float] = mapped_column(Float)
    specialization: Mapped[str] = mapped_column(String(100))

    user: Mapped["User"] = relationship("User")