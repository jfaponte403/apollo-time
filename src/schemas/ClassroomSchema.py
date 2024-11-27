from pydantic import BaseModel
from typing import Optional

class ClassroomSchema(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    capacity: Optional[int] = None
    is_active: Optional[bool] = True  

    class Config:
        orm_mode = True
