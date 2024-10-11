from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.repository.SubjectRepository import SubjectRepository
from src.database.DatabaseManager import get_db
from src.models.SubjectsModel import SubjectsModel
from src.schemas.SubjectSchema import SubjectSchema

subject = APIRouter()


@subject.get("/", response_model=List[SubjectSchema])
def get_all_subjects(db: Session = Depends(get_db)):
    subjects = SubjectRepository().get_all_subjects(db)
    return subjects

@subject.get("/{subject_id}", response_model=SubjectSchema)
def get_subject(subject_id: str, db: Session = Depends(get_db)):
    subject = SubjectRepository().get_subject_by_id(db, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@subject.post("/", response_model=SubjectSchema, status_code=status.HTTP_201_CREATED)
def create_subject(subject: SubjectSchema, db: Session = Depends(get_db)):
    new_subject = SubjectsModel(**subject.dict())  
    created_subject = SubjectRepository().create_subject(db, new_subject)
    return created_subject


@subject.put("/{subject_id}", response_model=SubjectSchema)
def update_subject(subject_id: str, updated_data: dict, db: Session = Depends(get_db)):
    updated_subject = SubjectRepository().update_subject(db, subject_id, updated_data)
    if not updated_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return updated_subject

@subject.delete("/{subject_id}", response_model=SubjectSchema)
def delete_subject(subject_id: str, db: Session = Depends(get_db)):
    deleted_subject = SubjectRepository().delete_subject(db, subject_id)
    if not deleted_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return deleted_subject
