from pydantic import BaseModel, constr

class LoginSchema(BaseModel):
    username: constr(min_length=1)
    password: constr(min_length=1)
