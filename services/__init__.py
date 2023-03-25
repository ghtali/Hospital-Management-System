from services.doctors_service import DoctorsService
from services.patients_service import PatientsService
from services.appointments_service import AppointmentsService
from services.lab_tests_service import LabTestsService
from services.prescriptions_service import PrescriptionsService


doctors_service = DoctorsService()
patients_service = PatientsService()
appointments_service = AppointmentsService()
lab_tests_service = LabTestsService()
prescriptions_service = PrescriptionsService()
