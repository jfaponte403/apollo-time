from pydantic import BaseModel


class ClassroomSchema(BaseModel):
    name: str
    type: str
    capacity: int
