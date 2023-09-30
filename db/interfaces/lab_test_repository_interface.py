from abc import ABC, abstractmethod
from typing import List, Optional

from ..db.models import LabTest


class ILabTestRepository(ABC):

    @abstractmethod
    def create(self, name: str, description: str) -> LabTest:
        pass

    @abstractmethod
    def get(self, lab_test_id: int) -> Optional[LabTest]:
        pass

    @abstractmethod
    def get_all(self) -> List[LabTest]:
        pass

    @abstractmethod
    def update(self, lab_test_id: int, name: str, description: str) -> LabTest:
        pass

    @abstractmethod
    def delete(self, lab_test_id: int) -> None:
        pass
