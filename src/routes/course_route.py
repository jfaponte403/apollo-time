import json

from fastapi import APIRouter, HTTPException, status
import logging
from fastapi.responses import JSONResponse

from src.models.CoursesModel import CoursesModel
from src.repository.CourseRepository import CourseRepository
from src.schemas.CourseSchema import CourseSchema
from src.schemas.CourseSchemaModify import CourseSchemaModify

course = APIRouter()
logger = logging.getLogger(__name__)


@course.get("/")
def get_courses():
    try:
        logger.info("Received request to fetch all active courses.")
        courses = CourseRepository().find_all()

        if not courses:
            return JSONResponse(
                content={"detail": "No courses found."},
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return JSONResponse(
            content={"courses": courses},
            status_code=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.error(f"Error fetching courses: {str(e)}", exc_info=True)
        raise e

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
        raise e

@course.delete("/{id}")
def delete_course(id: str):
    try:
        response = CourseRepository().delete(course_id=id)
        if not response:
            return JSONResponse(
                content={
                    "message": "course was not found"
                },
                status_code=status.HTTP_404_NOT_FOUND
            )

        return JSONResponse(
            content={
                "message": "course deleted successfully"
            },
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        raise e

@course.put("/{id}")
def put_course(id: str, request: CourseSchemaModify):
    try:
        course_entity = CourseRepository().find_by_id(course_id=id)

        if not course_entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )

        if request.degrees_id is not None and request.degrees_id != "":
            course_entity.degrees_id = request.degrees_id

        if request.classroom_id is not None and request.classroom_id != "":
            course_entity.classroom_id = request.classroom_id

        if request.subject_id is not None and request.subject_id != "":
            course_entity.subject_id = request.subject_id

        if request.teacher_id is not None and request.teacher_id != "":
            course_entity.teacher_id = request.teacher_id

        if request.name is not None and request.name != "":
            course_entity.name = request.name

        CourseRepository().update(course_entity)

        return JSONResponse(
            content={
                "message": "Course updated successfully"
            },
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
