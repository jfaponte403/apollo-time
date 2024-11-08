from pydantic import BaseModel, UUID4


class CourseSchema(BaseModel):
    classroom_id: UUID4
    subject_id: UUID4
    degrees_id: UUID4
    teacher_id: UUID4
    name: str
