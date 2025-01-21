import logging
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.database.database import engine
from src.models.SubjectsModel import SubjectsModel


class SubjectRepository:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def persist(self, subject_entity: SubjectsModel) -> bool:
        try:
            self.logger.info("Persisting degree entity: %s", subject_entity.id)

            with Session(engine) as session:
                session.add(subject_entity)
                session.commit()

            return True

        except Exception as e:
            raise e

    def find_all(self) -> Optional[list[SubjectsModel]]:

        subjects = []

        with Session(engine) as session:
            result = session.query(SubjectsModel).all()

            for item in result:
                subjects.append(item.to_dict())

            return subjects


    def get_all_subjects(self, db: Session) -> list[SubjectsModel]:
        return db.query(SubjectsModel).all()

    def get_subject_by_id(self, db: Session, subject_id: str) -> SubjectsModel:
        try:
            return db.query(SubjectsModel).filter(SubjectsModel.id == subject_id).one()
        except NoResultFound:
            raise NoResultFound

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

    def delete(self, subject_id: str) -> bool:
        try:
            self.logger.info("Deleting subject: %s", subject_id)
            with Session(engine) as session:
                entity = session.get(SubjectsModel, subject_id)

                if not entity:
                    return False

                entity.is_active = False
                session.commit()

            return True

        except Exception as e:
            raise e
