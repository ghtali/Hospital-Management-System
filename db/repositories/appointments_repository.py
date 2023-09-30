from typing import List
from ..db.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from ..db.models import Appointment
from ..db.database import db_session


class AppointmentsRepository(AppointmentRepositoryInterface):
    def get_all(self) -> List[Appointment]:
        return db_session.query(Appointment).all()

    def get_by_id(self, appointment_id: int) -> Appointment:
        return db_session.query(Appointment).filter_by(id=appointment_id).first()

    def create(self, appointment: Appointment) -> Appointment:
        db_session.add(appointment)
        db_session.commit()
        return appointment

    def update(self, appointment_id: int, appointment: Appointment) -> Appointment:
        db_session.query(Appointment).filter_by(
            id=appointment_id).update(appointment.to_dict())
        db_session.commit()
        return appointment

    def delete(self, appointment_id: int) -> None:
        db_session.query(Appointment).filter_by(id=appointment_id).delete()
        db_session.commit()
