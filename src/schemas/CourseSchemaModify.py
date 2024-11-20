from pydantic import BaseModel, UUID4


class CourseSchemaModify(BaseModel):
    classroom_id: UUID4 | None = None
    subject_id: UUID4 | None = None
    degrees_id: UUID4 | None = None
    teacher_id: UUID4 | None = None
    name: str | None = None