from abc import ABC, abstractmethod
from typing import List, Optional

from db.models import Doctor


class IDoctorRepository(ABC):

    @abstractmethod
    def create(self, name: str, department: str) -> Doctor:
        pass

    @abstractmethod
    def get(self, doctor_id: int) -> Optional[Doctor]:
        pass

    @abstractmethod
    def get_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def update(self, doctor_id: int, name: str, department: str) -> Doctor:
        pass

    @abstractmethod
    def delete(self, doctor_id: int) -> None:
        pass
