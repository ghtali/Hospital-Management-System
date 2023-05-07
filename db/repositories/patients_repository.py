from typing import List, Optional

from sqlalchemy.orm import Session

from db.interfaces.patient_repository_interface import PatientRepositoryInterface
from db.models import Patient
from db.models import PatientSchema


class PatientsRepository(PatientRepositoryInterface):
    def __init__(self, session: Session):
        self._session = session

    def create(self, patient_data: PatientSchema) -> Patient:
        patient = Patient(**patient_data.dict())
        self._session.add(patient)
        self._session.commit()
        self._session.refresh(patient)
        return patient

    def get(self, patient_id: int) -> Optional[Patient]:
        return self._session.query(Patient).filter(Patient.id == patient_id).first()

    def update(self, patient_id: int, patient_data: PatientSchema) -> Optional[Patient]:
        patient = self.get(patient_id)
        if patient:
            patient_data_dict = patient_data.dict(exclude_unset=True)
            for key, value in patient_data_dict.items():
                setattr(patient, key, value)
            self._session.commit()
            self._session.refresh(patient)
        return patient

    def delete(self, patient_id: int) -> bool:
        rows_deleted = self._session.query(Patient).filter(
            Patient.id == patient_id).delete()
        self._session.commit()
        return bool(rows_deleted)

    def get_all(self) -> List[Patient]:
        return self._session.query(Patient).all()
