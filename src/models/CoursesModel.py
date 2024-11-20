from __future__ import annotations

import uuid

from sqlalchemy import String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.database.Base import Base
from src.models.ClassroomsModel import ClassroomsModel
from src.models.DegreeModel import DegreeModel
from src.models.SubjectsModel import SubjectsModel
from src.models.TeachersModel import TeacherModel
from src.schemas.CourseSchema import CourseSchema


class CoursesModel(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    classroom_id: Mapped[str] = mapped_column(ForeignKey("classrooms.id", ondelete="CASCADE"))
    subject_id: Mapped[str] = mapped_column(ForeignKey("subjects.id", ondelete="CASCADE"))
    degrees_id: Mapped[str] = mapped_column(ForeignKey("degrees.id", ondelete="CASCADE"))
    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.id", ondelete="CASCADE"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    name: Mapped[str] = mapped_column(String, nullable=False)

    @staticmethod
    def create_from_request(request: CourseSchema) -> CoursesModel:
        return CoursesModel(
            classroom_id=str(request.classroom_id),
            subject_id=str(request.subject_id),
            degrees_id=str(request.degrees_id),
            teacher_id=str(request.teacher_id),
            name=str(request.name),
        )

    def to_http_response(self) -> dict:
        return {
            "id": self.id,
            "classroom_id": self.classroom_id,
            "subject_id": self.subject_id,
            "degrees_id": self.degrees_id,
            "teacher_id": self.teacher_id,
            "name": self.name,
            "is_active": self.is_active,
            "created_at": str(self.created_at),
        }
