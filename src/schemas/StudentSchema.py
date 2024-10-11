import random
import string
from pydantic import BaseModel, EmailStr, Field, constr
from typing_extensions import Annotated
from typing import Optional


class StudentSchema(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=50)]
    email: EmailStr
    phone_number: Annotated[str, Field(min_length=1, max_length=12)]
    degree_id: constr(min_length=1)
    gpa: int

    role: str = "student"
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)

    @staticmethod
    def generate_password(length=10) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    @classmethod
    def set_username(cls, values):
        if 'username' not in values or values['username'] is None:
            name = values.get('name', '')
            email = values.get('email', '')
            base_username = name.split()[0].lower()
            domain_part = email.split('@')[0]
            values['username'] = f"{base_username}.{domain_part}"
        return values

    @classmethod
    def set_password(cls, values):
        if 'password' not in values or values['password'] is None:
            values['password'] = cls.generate_password()
        return values

    def __init__(self, **data):
        data = self.set_username(data)
        data = self.set_password(data)
        super().__init__(**data)