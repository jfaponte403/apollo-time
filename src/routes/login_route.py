import logging
from datetime import timedelta

from fastapi import APIRouter, HTTPException

from src.models.PostLoginModel import PostLoginModel
from src.repository.LoginRepository import LoginRepository
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

@login.post("/")
def login_user(request: PostLoginModel):
    logger.info("POST / - Login attempt for username: %s", request.username)

    try:
        login_entity = LoginRepository.find_by_request(request)

        if login_entity is None:
            logger.warning("Login failed: Invalid username or password for user: %s", request.username)
            raise HTTPException(status_code=401, detail="Invalid username or password")

        access_token_expires = timedelta(minutes=EnvironmentVariableResolver().get_access_token_expire_minutes())
        access_token = create_access_token(data={"sub": login_entity.username}, expires_delta=access_token_expires)

        return {"message": "Login successful", "user": login_entity.username, "access_token": access_token}

    except HTTPException as http_ex:
        logger.error("HTTP error during login for user: %s - %s", request.username, http_ex.detail)
        raise

    except Exception as e:
        logger.error("Unexpected error during login for user: %s - %s", request.username, str(e))
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
