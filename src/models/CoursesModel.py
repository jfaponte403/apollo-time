import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base


class CoursesModel(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    classroom_id: Mapped[str] = mapped_column(ForeignKey("classrooms.id"))
    subject_id: Mapped[str] = mapped_column(ForeignKey("subjects.id"))
    degrees_id: Mapped[str] = mapped_column(ForeignKey("degrees.id"))
    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.id"))

    classroom: Mapped["Classroom"] = relationship("Classroom")
    subject: Mapped["Subject"] = relationship("Subject")
    degree: Mapped["Degree"] = relationship("Degree")
    teacher: Mapped["Teacher"] = relationship("Teacher")
