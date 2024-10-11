from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
import logging

from src.database.database import engine
from src.models.LoginModel import LoginModel
from src.models.StudentsModel import StudentsModel
from src.models.UserModel import UserModel
from src.repository.RoleRepository import RoleRepository
from src.schemas.StudentSchema import StudentSchema

logger = logging.getLogger(__name__)

student = APIRouter()

@student.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_student(request: StudentSchema):
    logger.info("Received request to create a new student.")
    try:
        role_id = RoleRepository.get_teacher_id()
        logger.info(f"Retrieved role ID for student: {role_id}")

        if role_id is None:
            logger.warning("Student role ID not found.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student role not found.")

        user = UserModel.create_from_student_request(request=request, role_id=str(role_id))
        logger.info(f"Created user model for {request.username}")

        with Session(engine) as session:
            session.add(user)
            session.flush()

            login = LoginModel.create_from_student_request(request=request, user_id=str(user.id))
            session.add(login)

            student_entity = StudentsModel.create_from_request(request=request, user_id=str(user.id))
            session.add(student_entity)

            session.commit()

        logger.info(f"Successfully created student: {request.username}")
        return {
            "message": "Student created successfully.",
            "username": request.username,
            "password": request.password
        }

    except Exception as e:
        logger.error(f"Error creating student: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred: {str(e)}")
