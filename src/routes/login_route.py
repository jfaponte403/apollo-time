import logging
from fastapi import APIRouter, HTTPException

from src.models.PostLoginModel import PostLoginModel
from src.repository.LoginRepository import LoginRepository

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

        logger.info("Login successful for user: %s", login_entity.username)
        return {"message": "Login successful", "user": login_entity}

    except HTTPException as http_ex:
        logger.error("HTTP error during login for user: %s - %s", request.username, http_ex.detail)
        raise

    except Exception as e:
        logger.error("Unexpected error during login for user: %s - %s", request.username, str(e))
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
