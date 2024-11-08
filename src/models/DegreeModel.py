from __future__ import annotations
import uuid

from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.Base import Base
from src.schemas.DegreeSchema import DegreeSchema


class DegreeModel(Base):
    __tablename__ = "degrees"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    @staticmethod
    def create_from_request(request: DegreeSchema) -> DegreeModel:
        return DegreeModel(name=request.name)

    def to_http_response(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "create_at": self.created_at,
            "is_active": self.is_active
        }