from pydantic import BaseModel, constr


class DegreeSchema(BaseModel):
    name: constr(min_length=1)