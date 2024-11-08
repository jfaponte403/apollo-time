import logging
from fastapi import APIRouter, HTTPException, status

from src.models.DegreeModel import DegreeModel
from src.schemas.DegreeSchema import DegreeSchema
from src.repository.DegreeRepository import DegreeRepository

degree = APIRouter()
logger = logging.getLogger(__name__)

@degree.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_degree(request: DegreeSchema):
    try:
        logger.info("Received request to create a new degree: %s", request)
        degree_entity = DegreeModel.create_from_request(request)
        response = DegreeRepository().persist(degree_entity)

        if response:
            logger.info("Degree created successfully: %s", degree_entity)
            return {"message": "Degree created successfully."}

        logger.error("Database error: Unable to create the degree.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database error: Unable to create the degree."
        )

    except Exception as e:
        logger.error("An unexpected error occurred during degree creation: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )


@degree.get("/", response_model=dict)
def get_degrees():
    try:
        logger.info("Received request to retrieve all degrees.")
        degrees = DegreeRepository().find_all()

        if not degrees:
            logger.warning("No degrees found in the database.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No degrees found in the database."
            )

        logger.info("Degrees retrieved successfully. Count: %d", len(degrees))
        return {"message": "Degrees retrieved successfully.", "degrees": degrees}

    except Exception as e:
        logger.error("An unexpected error occurred while retrieving degrees: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )


@degree.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_degree(id: str):
    try:
        logger.info("Received request to delete degree with ID: %s", id)
        degree_entity = DegreeRepository().find_by_id(degree_id=id)

        if not degree_entity:
            logger.warning("Degree with ID %s does not exist.", id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Degree with the specified ID does not exist."
            )

        DegreeRepository().delete(degree_id=id)
        logger.info("Degree with ID %s deleted successfully.", id)
        return {"message": "Degree deleted successfully."}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error("An unexpected error occurred while deleting the degree: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )


@degree.put("/{id}", status_code=status.HTTP_200_OK, response_model=dict)
def modify_degree(id: str, request: DegreeSchema):
    try:
        logger.info("Received request to update degree with ID: %s", id)
        degree_entity = DegreeRepository().find_by_id(degree_id=str(id))

        if not degree_entity:
            logger.warning("Degree with ID %s not found.", id)
            raise HTTPException(status_code=404, detail="Degree not found")

        degree_entity.name = request.name

        response = DegreeRepository().update(degree_entity)

        if not response:
            logger.error("Failed to update degree with ID %s.", id)
            raise HTTPException(status_code=400, detail="Failed to update degree")

        logger.info("Degree with ID %s updated successfully.", id)
        return {"message": "Degree updated successfully."}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error("An unexpected error occurred while updating the degree: %s", e)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
