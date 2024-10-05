from pydantic import BaseModel, constr

class PostLoginModel(BaseModel):
    username: constr(min_length=1)
    password: constr(min_length=1)
