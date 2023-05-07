from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.models import Appointment
from db.repositories.appointments_repository import AppointmentsRepository
from services.appointments_service import AppointmentsService

router = APIRouter(prefix="/appointments", tags=["appointments"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: Appointment, db: Session = Depends(get_db)):
    appointment_service = AppointmentsService(AppointmentsRepository(db))
    created_appointment = appointment_service.create_appointment(appointment)

    return created_appointment


@router.get("/{appointment_id}", response_model=Appointment)
async def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentsService(AppointmentsRepository(db))
    appointment = appointment_service.get_appointment(appointment_id)

    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    return appointment


@router.put("/{appointment_id}", response_model=Appointment)
async def update_appointment(appointment_id: int, appointment: Appointment, db: Session = Depends(get_db)):
    appointment_service = AppointmentsService(AppointmentsRepository(db))
    updated_appointment = appointment_service.update_appointment(
        appointment_id, appointment)

    if not updated_appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    return updated_appointment


@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentsService(AppointmentsRepository(db))
    appointment_deleted = appointment_service.delete_appointment(
        appointment_id)

    if not appointment_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
