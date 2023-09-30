from abc import ABC, abstractmethod
from typing import List

from ..db.models import Prescription


class PrescriptionRepositoryInterface(ABC):
    @abstractmethod
    def get_prescriptions(self, patient_id: int) -> List[Prescription]:
        pass

    @abstractmethod
    def add_prescription(self, prescription: Prescription) -> Prescription:
        pass
