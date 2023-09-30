from abc import ABC, abstractmethod
from typing import List

from models.appointments import Appointment


class AppointmentRepositoryInterface(ABC):
    @abstractmethod
    def get_all_appointments(self) -> List[Appointment]:
        pass

    @abstractmethod
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        pass

    @abstractmethod
    def create_appointment(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def update_appointment(self, appointment_id: int, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def delete_appointment(self, appointment_id: int) -> bool:
        pass
