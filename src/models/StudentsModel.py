import uuid

from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.Base import Base


class StudentsModel(Base):
    __tablename__ = "students"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    degree_id: Mapped[str] = mapped_column(ForeignKey("degrees.id"))
    gpa: Mapped[float] = mapped_column(Float)

    user: Mapped["User"] = relationship("User")
    degree: Mapped["Degree"] = relationship("Degree")