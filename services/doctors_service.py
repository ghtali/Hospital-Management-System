from typing import List

from db.interfaces.doctor_repository_interface import DoctorRepositoryInterface
from models.doctors import Doctor


class DoctorService:
    def __init__(self, repository: DoctorRepositoryInterface):
        self.repository = repository

    def create_doctor(self, doctor: Doctor) -> int:
        return self.repository.create_doctor(doctor)

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        return self.repository.get_doctor_by_id(doctor_id)

    def get_all_doctors(self) -> List[Doctor]:
        return self.repository.get_all_doctors()

    def update_doctor(self, doctor_id: int, doctor: Doctor) -> None:
        self.repository.update_doctor(doctor_id, doctor)

    def delete_doctor(self, doctor_id: int) -> None:
        self.repository.delete_doctor(doctor_id)
