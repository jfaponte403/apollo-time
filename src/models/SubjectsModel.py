import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.Base import Base
from pydantic import BaseModel
from typing import Optional


class SubjectsModel(Base):
    __tablename__ = "subjects"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))


class SubjectSchema(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

