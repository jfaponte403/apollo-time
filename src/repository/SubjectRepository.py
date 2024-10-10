from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.models.SubjectsModel import SubjectsModel

class SubjectRepository:
    def get_all_subjects(self, db: Session) -> list[SubjectsModel]:
        return db.query(SubjectsModel).all()

    def get_subject_by_id(self, db: Session, subject_id: str) -> SubjectsModel: 
        try:
            return db.query(SubjectsModel).filter(SubjectsModel.id == subject_id).one()
        except NoResultFound:
            return None  

    def create_subject(self, db: Session, subject: SubjectsModel) -> SubjectsModel:
        db.add(subject)
        db.commit()
        db.refresh(subject)
        return subject

    def update_subject(self, db: Session, subject_id: str, updated_data: dict) -> Optional[SubjectsModel]:
        subject = self.get_subject_by_id(db, subject_id)
        if subject is None:
            return None  

        for key, value in updated_data.items():
            setattr(subject, key, value)
        db.commit()
        db.refresh(subject)
        return subject

    def delete_subject(self, db: Session, subject_id: str) -> Optional[SubjectsModel]:
        subject = self.get_subject_by_id(db, subject_id)
        if subject:
            db.delete(subject)
            db.commit()
        return subject
