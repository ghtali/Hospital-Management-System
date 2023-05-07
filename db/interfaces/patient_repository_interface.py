from abc import ABC, abstractmethod
from typing import List, Optional

from db.models import Patient


class IPatientRepository(ABC):

    @abstractmethod
    def create(self, name: str, email: str, phone_number: str, address: str, birth_date: str) -> Patient:
        pass

    @abstractmethod
    def get(self, patient_id: int) -> Optional[Patient]:
        pass

    @abstractmethod
    def get_all(self) -> List[Patient]:
        pass

    @abstractmethod
    def update(self, patient_id: int, name: str, email: str, phone_number: str, address: str, birth_date: str) -> Patient:
        pass

    @abstractmethod
    def delete(self, patient_id: int) -> None:
        pass
