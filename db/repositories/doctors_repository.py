from typing import List, Optional

from sqlalchemy.orm import Session

from db.models import Doctor
from db.interfaces.doctor_repository_interface import DoctorRepositoryInterface


class DoctorRepository(DoctorRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_doctors(self) -> List[Doctor]:
        return self.db.query(Doctor).all()

    def get_doctor_by_id(self, doctor_id: int) -> Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.id == doctor_id).first()

    def get_doctor_by_name(self, name: str) -> Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.name == name).first()

    def create_doctor(self, name: str, specialization: str, phone_number: str) -> Doctor:
        doctor = Doctor(name=name, specialization=specialization,
                        phone_number=phone_number)
        self.db.add(doctor)
        self.db.commit()
        self.db.refresh(doctor)
        return doctor

    def update_doctor(self, doctor_id: int, name: str, specialization: str, phone_number: str) -> Optional[Doctor]:
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            doctor.name = name
            doctor.specialization = specialization
            doctor.phone_number = phone_number
            self.db.commit()
            self.db.refresh(doctor)
            return doctor
        return None

    def delete_doctor(self, doctor_id: int) -> bool:
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.db.delete(doctor)
            self.db.commit()
            return True
        return False
