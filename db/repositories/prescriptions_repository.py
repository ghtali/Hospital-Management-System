from typing import List, Optional

from sqlalchemy.orm import Session

from db.interfaces.prescription_repository_interface import PrescriptionRepositoryInterface
from db.models import Prescription
from db.models import Patient, Doctor


class PrescriptionsRepository(PrescriptionRepositoryInterface):
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_all_prescriptions(self) -> List[Prescription]:
        return self.db_session.query(Prescription).all()

    def get_prescription_by_id(self, prescription_id: int) -> Optional[Prescription]:
        return self.db_session.query(Prescription).filter_by(id=prescription_id).first()

    def create_prescription(self, patient_id: int, doctor_id: int, description: str) -> Prescription:
        prescription = Prescription(
            patient_id=patient_id, doctor_id=doctor_id, description=description)
        self.db_session.add(prescription)
        self.db_session.commit()
        self.db_session.refresh(prescription)
        return prescription

    def update_prescription(self, prescription_id: int, description: str) -> Optional[Prescription]:
        prescription = self.get_prescription_by_id(prescription_id)
        if prescription is None:
            return None

        prescription.description = description
        self.db_session.commit()
        self.db_session.refresh(prescription)
        return prescription

    def delete_prescription(self, prescription_id: int) -> bool:
        num_deleted = self.db_session.query(
            Prescription).filter_by(id=prescription_id).delete()
        self.db_session.commit()
        return num_deleted > 0

    def get_patient(self, prescription: Prescription) -> Patient:
        return prescription.patient

    def get_doctor(self, prescription: Prescription) -> Doctor:
        return prescription.doctor
