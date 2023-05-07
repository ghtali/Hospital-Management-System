from typing import List, Dict

from db.interfaces.lab_test_repository_interface import LabTestRepositoryInterface
from models.lab_tests import LabTest


class LabTestService:
    def __init__(self, lab_test_repo: LabTestRepositoryInterface):
        self.lab_test_repo = lab_test_repo

    def add_lab_test(self, lab_test_data: Dict) -> LabTest:
        lab_test = LabTest(**lab_test_data)
        return self.lab_test_repo.add_lab_test(lab_test)

    def get_all_lab_tests(self) -> List[LabTest]:
        return self.lab_test_repo.get_all_lab_tests()

    def get_lab_test_by_id(self, lab_test_id: int) -> LabTest:
        return self.lab_test_repo.get_lab_test_by_id(lab_test_id)

    def update_lab_test(self, lab_test_id: int, lab_test_data: Dict) -> LabTest:
        lab_test = self.lab_test_repo.get_lab_test_by_id(lab_test_id)
        for key, value in lab_test_data.items():
            setattr(lab_test, key, value)
        return self.lab_test_repo.update_lab_test(lab_test)

    def delete_lab_test(self, lab_test_id: int) -> bool:
        lab_test = self.lab_test_repo.get_lab_test_by_id(lab_test_id)
        return self.lab_test_repo.delete_lab_test(lab_test)
