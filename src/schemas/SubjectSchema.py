import uuid
from typing import Optional

from pydantic import BaseModel


class SubjectSchema(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True