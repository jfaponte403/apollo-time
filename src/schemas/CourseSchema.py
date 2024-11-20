from pydantic import BaseModel


class CourseSchema(BaseModel):
    classroom_id: str
    subject_id: str
    degrees_id: str
    teacher_id: str
    name: str
