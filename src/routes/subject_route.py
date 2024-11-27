from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.coercions import expect

from src.repository.SubjectRepository import SubjectRepository
from src.database.DatabaseManager import get_db
from src.models.SubjectsModel import SubjectsModel
from src.schemas.SubjectSchema import SubjectSchema

subject = APIRouter()


@subject.get("/")
def get_all_subjects(db: Session = Depends(get_db)):
    subjects_query = SubjectRepository().get_all_subjects(db)

    subjects_list = [subject_entity.to_dict() for subject_entity in subjects_query]

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"subjects": subjects_list}
    )


@subject.get("/{subject_id}", response_model=SubjectSchema)
def get_subject(subject_id: str, db: Session = Depends(get_db)):
    subject = SubjectRepository().get_subject_by_id(db, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject


@subject.post("/")
def create_subject(subject_request: SubjectSchema):
    try:

        subject_entity = SubjectsModel(
            name=subject_request.name
        )

        query = SubjectRepository().persist(subject_entity)

        if query is False:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": "error while creating subject"}
            )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Created subject"}
        )

    except Exception as e:
        raise e


@subject.put("/{subject_id}", response_model=SubjectSchema)
def update_subject(subject_id: str, updated_data: dict, db: Session = Depends(get_db)):
    updated_subject = SubjectRepository().update_subject(db, subject_id, updated_data)
    if not updated_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return updated_subject


@subject.delete("/{subject_id}", response_model=SubjectSchema)
def delete_subject(subject_id: str):
    try:
        deleted_subject = SubjectRepository().delete(subject_id)

        if deleted_subject is False:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Error while deleting subject"}
            )

        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"message": "deleted subject"}
        )


    except Exception as e:
        raise e
