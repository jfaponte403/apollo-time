from fastapi import APIRouter, HTTPException, status

from src.models.DegreeModel import DegreeModel
from src.schemas.DegreeSchema import DegreeSchema
from src.repository.DegreeRepository import DegreeRepository

degree = APIRouter()

@degree.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_degree(request: DegreeSchema):
    try:
        degree_entity = DegreeModel.create_from_request(request)
        response = DegreeRepository().persist(degree_entity)

        if response:
            return {"message": "Degree created successfully."}

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database error: Unable to create the degree."
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )


@degree.get("/", response_model=dict)
def get_degrees():
    try:
        degrees = DegreeRepository().find_all()

        if not degrees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No degrees found in the database."
            )

        return {"message": "Degrees retrieved successfully.", "degrees": degrees}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )


@degree.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_degree(id: str):
    try:
        degree_entity = DegreeRepository().find_by_id(degree_id=id)

        if not degree_entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Degree with the specified ID does not exist."
            )

        DegreeRepository().delete(degree_id=id)
        return {"message": "Degree deleted successfully."}

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Please try again later."
        )