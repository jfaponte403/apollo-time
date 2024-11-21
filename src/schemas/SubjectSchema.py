import uuid
from typing import Optional

from pydantic import BaseModel


class SubjectSchema(BaseModel):
    name: str
    is_active: Optional[bool] = None
    class Config:
        orm_mode = True