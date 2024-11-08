from pydantic import BaseModel
from typing import Optional

class StudentModifySchema(BaseModel):
    user_id: Optional[str] = None
    degree_id: Optional[str] = None
    gpa: Optional[float] = None
    is_active: Optional[bool] = None
    user_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
