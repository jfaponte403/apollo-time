import uuid

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base
from src.models.DegreeModel import DegreeModel
from src.models.UserModel import UserModel

class StudentsModel(Base):
    __tablename__ = "students"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    degree_id: Mapped[str] = mapped_column(ForeignKey("degrees.id"))
    gpa: Mapped[float] = mapped_column(Float)
