import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base
from src.models.CoursesModel import CoursesModel

class SchedulesModel(Base):
    __tablename__ = "schedules"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))
    start_time: Mapped[str] = mapped_column(String(30))
    end_time: Mapped[str] = mapped_column(String(30))
    day_of_week: Mapped[str] = mapped_column(String(30))

