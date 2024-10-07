from pydantic import BaseModel, constr


class PostDegreeModel(BaseModel):
    name: constr(min_length=1)