from fastapi import APIRouter, HTTPException, status
import logging

from src.models.CoursesModel import CoursesModel
from src.repository.CourseRepository import CourseRepository
from src.schemas.CourseSchema import CourseSchema

course = APIRouter()
logger = logging.getLogger(__name__)

@course.get("/", status_code=status.HTTP_200_OK)
def get_courses():
    logger.info("Received request to fetch all active courses.")
    try:
        courses = CourseRepository().find_all()

        if courses is None:
            logger.error("No active courses found or an error occurred.")
            raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching courses.")

        logger.info(f"Fetched {len(courses)} active courses successfully.")
        return courses

    except Exception as e:
        logger.error(f"Error fetching courses: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching courses.")

@course.post("/", status_code=status.HTTP_201_CREATED)
def post_course(request: CourseSchema):
    try:

        course_entity = CoursesModel.create_from_request(request)

        result = CourseRepository().persist(course_entity)

        if not result:
            return HTTPException(status_code=404, detail="Course could not be created.")

        return {
            "message": "course created"
        }

    except Exception as e:
        logger.error(f"Error fetching courses: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
