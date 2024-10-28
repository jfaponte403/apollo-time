from __future__ import annotations
import uuid

from sqlalchemy import ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.Base import Base
from src.schemas.StudentSchema import StudentSchema
from src.schemas.TeacherSchema import TeacherSchema
from sqlalchemy.sql import func

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    role_id: Mapped[str] = mapped_column(ForeignKey("roles.id"))
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(15))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    @staticmethod
    def create_from_teacher_request(request: TeacherSchema, role_id: str) -> UserModel:
        return UserModel(
            role_id=str(role_id),
            name=request.name,
            email=request.email,
            phone_number=request.phone_number
        )

    @staticmethod
    def create_from_student_request(request: StudentSchema, role_id: str) -> UserModel:
        return UserModel(
            role_id=str(role_id),
            name=request.name,
            email=request.email,
            phone_number=request.phone_number
        )