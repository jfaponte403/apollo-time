from __future__ import annotations

import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey

from src.models.UserModel import UserModel

from src.database.Base import Base
from src.schemas.StudentSchema import StudentSchema
from src.schemas.TeacherSchema import TeacherSchema


class LoginModel(Base):
    __tablename__ = "login"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(100))

    @staticmethod
    def create_from_teacher_request(request: TeacherSchema, user_id: str) -> LoginModel:
        return LoginModel(
            user_id=str(user_id),
            username=request.username,
            password=request.password
        )

    @staticmethod
    def create_from_student_request(request: StudentSchema, user_id: str) -> LoginModel:
        return LoginModel(
            user_id=str(user_id),
            username=request.username,
            password=request.password
        )
