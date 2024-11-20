from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.repository.UserRepository import UserRepository

user = APIRouter()

@user.get('/{id}')
def get_user(id: str):
    try:

        user_model = UserRepository().find_by_id(user_id=str(id))


        return JSONResponse(
            content={
                "name": user_model.name
            },
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        raise e