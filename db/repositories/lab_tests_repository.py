from typing import List
from db.interfaces.lab_test_repository_interface import LabTestRepositoryInterface
from db.models import LabTest
from db.database import db_session


class LabTestsRepository(LabTestRepositoryInterface):
    def get_lab_test_by_id(self, lab_test_id: int) -> LabTest:
        with db_session() as session:
            return session.query(LabTest).filter_by(id=lab_test_id).first()

    def get_all_lab_tests(self) -> List[LabTest]:
        with db_session() as session:
            return session.query(LabTest).all()

    def add_lab_test(self, lab_test: LabTest) -> LabTest:
        with db_session() as session:
            session.add(lab_test)
            session.commit()
            session.refresh(lab_test)
            return lab_test

    def update_lab_test(self, lab_test: LabTest) -> LabTest:
        with db_session() as session:
            session.merge(lab_test)
            session.commit()
            session.refresh(lab_test)
            return lab_test

    def delete_lab_test(self, lab_test_id: int) -> bool:
        with db_session() as session:
            lab_test = session.query(LabTest).filter_by(id=lab_test_id).first()
            if not lab_test:
                return False
            session.delete(lab_test)
            session.commit()
            return True
