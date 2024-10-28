from typing import Optional
from pydantic import BaseModel

class TeacherModifySchema(BaseModel):
    salary: Optional[float] = None
    specialization: Optional[str] = None
    name: Optional[str] = None  # Assuming you want to allow optional name updates
    email: Optional[str] = None  # Assuming you want to allow optional email updates
    phone_number: Optional[str] = None  # Assuming you want to allow optional phone updates
    username: Optional[str] = None  # Optional field for username update
    password: Optional[str] = None
