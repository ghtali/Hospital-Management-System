from typing import List
from datetime import datetime
from ..db.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from models.appointments import Appointment, AppointmentCreate, AppointmentUpdate


class AppointmentsService:
    def __init__(self, appointment_repository: AppointmentRepositoryInterface):
        self.appointment_repository = appointment_repository

    def create_appointment(self, appointment_create: AppointmentCreate) -> Appointment:
        appointment = self.appointment_repository.create_appointment(
            appointment_create)
        return appointment

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        appointment = self.appointment_repository.get_appointment_by_id(
            appointment_id)
        return appointment

    def get_all_appointments(self) -> List[Appointment]:
        appointments = self.appointment_repository.get_all_appointments()
        return appointments

    def update_appointment(self, appointment_id: int, appointment_update: AppointmentUpdate) -> Appointment:
        appointment = self.appointment_repository.update_appointment(
            appointment_id, appointment_update)
        return appointment

    def delete_appointment(self, appointment_id: int) -> None:
        self.appointment_repository.delete_appointment(appointment_id)

    def get_appointments_for_doctor(self, doctor_id: int) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_for_doctor(
            doctor_id)
        return appointments

    def get_appointments_for_patient(self, patient_id: int) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_for_patient(
            patient_id)
        return appointments

    def get_appointments_between_dates(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_between_dates(
            start_date, end_date)
        return appointments
