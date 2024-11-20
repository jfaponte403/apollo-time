from pydantic import BaseModel, UUID4


class CourseSchemaModify(BaseModel):
    classroom_id: UUID4 | str
    subject_id: UUID4 | str
    degrees_id: UUID4 | str
    teacher_id: UUID4 | str
    name: str | str