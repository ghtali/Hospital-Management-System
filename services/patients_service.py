from typing import List

from ..db.interfaces import PatientRepositoryInterface
from models.patients import Patient


class PatientsService:
    def __init__(self, repo: PatientRepositoryInterface):
        self.repo = repo

    def get_all_patients(self) -> List[Patient]:
        return self.repo.get_all()

    def get_patient_by_id(self, patient_id: int) -> Patient:
        return self.repo.get_by_id(patient_id)

    def add_patient(self, patient: Patient) -> Patient:
        return self.repo.add(patient)

    def update_patient_by_id(self, patient_id: int, new_patient_data: Patient) -> Patient:
        patient = self.repo.get_by_id(patient_id)
        patient.name = new_patient_data.name
        patient.age = new_patient_data.age
        patient.gender = new_patient_data.gender
        patient.phone_number = new_patient_data.phone_number
        patient.address = new_patient_data.address
        return self.repo.update(patient_id, patient)

    def delete_patient(self, patient_id: int):
        return self.repo.delete(patient_id)
