from typing import Optional
from pydantic import BaseModel

class TeacherModifySchema(BaseModel):
    salary: Optional[float] = None
    specialization: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
