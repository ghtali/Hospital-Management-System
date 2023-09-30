from typing import List

from ..db.interfaces.prescription_repository_interface import PrescriptionRepositoryInterface
from models.prescriptions import Prescription


class PrescriptionService:
    def __init__(self, repository: PrescriptionRepositoryInterface):
        self.repository = repository

    def get_prescription(self, prescription_id: int) -> Prescription:
        return self.repository.get(prescription_id)

    def get_all_prescriptions(self) -> List[Prescription]:
        return self.repository.get_all()

    def create_prescription(self, prescription: Prescription) -> Prescription:
        return self.repository.create(prescription)

    def update_prescription(self, prescription_id: int, prescription: Prescription) -> Prescription:
        return self.repository.update(prescription_id, prescription)

    def delete_prescription(self, prescription_id: int):
        self.repository.delete(prescription_id)
