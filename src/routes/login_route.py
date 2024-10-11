import logging
from datetime import timedelta

from fastapi import APIRouter, HTTPException

from src.schemas.LoginSchema import LoginSchema
from src.repository.LoginRepository import LoginRepository
from src.repository.RoleRepository import RoleRepository
from src.utils.EnvironmentVariableResolver import EnvironmentVariableResolver
from src.utils.create_access_token import create_access_token

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

login = APIRouter()

@login.get("/")
def get_login():
    logger.info("GET / - Login route accessed")
    return "Login"

@login.post("/", status_code=200, response_model=dict)
def login_user(request: LoginSchema):
    logger.info("POST / - Login attempt for username: %s", request.username)

    try:
        login_entity = LoginRepository().find_by_request(request)

        if login_entity is None:
            logger.warning("Login failed: Invalid username or password for user: %s", request.username)
            raise HTTPException(status_code=401, detail="Invalid username or password")

        role = RoleRepository.find_role_by_user_id(login_entity.user_id)

        if role is None:
            logger.warning("Login failed: No role found for user ID: %s", login_entity.user_id)
            raise HTTPException(status_code=403, detail="User role not found")

        logger.info("User %s successfully authenticated with role: %s", login_entity.username, role.rol)

        access_token_expires = timedelta(minutes=EnvironmentVariableResolver().get_access_token_expire_minutes())
        access_token = create_access_token(
            data={
                "id": login_entity.user_id,
                "user": login_entity.username,
                "role": role.rol
            },
            expires_delta=access_token_expires
        )

        logger.info("Access token generated for user: %s", login_entity.username)

        return {"message": "Login successful", "token": access_token}

    except HTTPException as http_ex:
        logger.error("HTTP error during login for user: %s - %s", request.username, http_ex.detail)
        raise

    except Exception as e:
        logger.error("Unexpected error during login for user: %s - %s", request.username, str(e))
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

