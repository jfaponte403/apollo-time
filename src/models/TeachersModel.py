from __future__ import annotations
import uuid

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.database.Base import Base
from src.schemas.TeacherSchema import TeacherSchema


class TeacherModel(Base):
    __tablename__ = "teachers"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    salary: Mapped[float] = mapped_column(Float)
    specialization: Mapped[str] = mapped_column(String(100))

    @staticmethod
    def create_from_request(request: TeacherSchema, user_id: str) -> TeacherModel:
        return TeacherModel(
            user_id=str(user_id),
            salary=request.salary,
            specialization=request.specialization
        )