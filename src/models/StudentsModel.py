from __future__ import annotations
import uuid

from sqlalchemy import String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base
from src.models.DegreeModel import DegreeModel
from src.models.UserModel import UserModel
from src.schemas.StudentSchema import StudentSchema
from sqlalchemy.sql import func

class StudentsModel(Base):
    __tablename__ = "students"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    degree_id: Mapped[str] = mapped_column(ForeignKey("degrees.id", ondelete="CASCADE"))
    gpa: Mapped[float] = mapped_column(Float)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    @staticmethod
    def create_from_request(request: StudentSchema, user_id: str) -> StudentsModel:
        return StudentsModel(
            user_id=str(user_id),
            degree_id=str(request.degree_id),
            gpa=request.gpa
        )