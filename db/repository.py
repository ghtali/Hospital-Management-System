from models.appointments import Appointment
from models.doctors import Doctor
from models.lab_tests import LabTest
from models.patients import Patient
from models.prescriptions import Prescription
from db import db


class AppointmentRepository:
    def get_all_appointments(self):
        return Appointment.query.all()

    def get_appointment_by_id(self, appointment_id):
        return Appointment.query.get(appointment_id)

    def create_appointment(self, patient_id, doctor_id, appointment_date_time, reason, status):
        appointment = Appointment(
            patient_id, doctor_id, appointment_date_time, reason, status)
        db.session.add(appointment)
        db.session.commit()
        return appointment

    def update_appointment(self, appointment, data):
        appointment.patient_id = data.get('patient_id', appointment.patient_id)
        appointment.doctor_id = data.get('doctor_id', appointment.doctor_id)
        appointment.appointment_date_time = data.get(
            'appointment_date_time', appointment.appointment_date_time)
        appointment.reason = data.get('reason', appointment.reason)
        appointment.status = data.get('status', appointment.status)
        db.session.commit()
        return appointment

    def delete_appointment(self, appointment):
        db.session.delete(appointment)
        db.session.commit()
        return appointment


class DoctorRepository:
    def get_all_doctors(self):
        return Doctor.query.all()

    def get_doctor_by_id(self, doctor_id):
        return Doctor.query.get(doctor_id)

    def create_doctor(self, first_name, last_name,
                      gender, date_of_birth, speciality, phone_number, email):
        doctor = Doctor(first_name=first_name, last_name=last_name, gender=gender,
                        date_of_birth=date_of_birth, speciality=speciality,
                        phone_number=phone_number, email=email)
        db.session.add(doctor)
        db.session.commit()
        return doctor

    def update_doctor(self, doctor, data):
        doctor.name = data.get('name', doctor.name)
        doctor.lastname = data.get('lastname', doctor.lastname)
        doctor.gender = data.get('gender', doctor.gender)
        doctor.date_of_birth = data.get('date_of_birth', doctor.date_of_birth)
        doctor.speciality = data.get('speciality', doctor.speciality)
        doctor.phone_number = data.get('phone_number', doctor.phone_number)
        doctor.email = data.get('email', doctor.email)
        db.session.commit()
        return doctor

    def delete_doctor(self, doctor):
        db.session.delete(doctor)
        db.session.commit()
        return doctor


class LabTestRepository:
    def get_all_lab_tests(self):
        return LabTest.query.all()

    def get_lab_test_by_id(self, lab_test_id):
        return LabTest.query.get(lab_test_id)

    def create_lab_test(self, test_name, date_created,
                        date_completed, result):
        lab_test = LabTest(test_name=test_name,
                           date_created=date_created, date_completed=date_completed,
                           result=result)
        db.session.add(lab_test)
        db.session.commit()
        return lab_test

    def update_lab_test(self, lab_test, data):
        lab_test.appointment_id = data.get(
            'appointment_id', lab_test.appointment_id)
        lab_test.test_name = data.get('test_name', lab_test.test_name)
        lab_test.date_created = data.get('date_created', lab_test.date_created)
        lab_test.date_completed = data.get(
            'date_completed', lab_test.date_completed)
        lab_test.result = data.get('result', lab_test.result)
        db.session.commit()
        return lab_test

    def delete_lab_test(self, lab_test):
        db.session.delete(lab_test)
        db.session.commit()
        return lab_test


class PatientRepository:
    def get_all_patients(self):
        return Patient.query.all()

    def get_patient_by_id(self, patient_id):
        return Patient.query.get(patient_id)

    def create_patient(self, first_name, last_name, date_of_birth, gender, address, phone_number, email):
        patient = Patient(first_name=first_name, last_name=last_name,
                          date_of_birth=date_of_birth, gender=gender, address=address,
                          phone_number=phone_number, email=email)
        db.session.add(patient)
        db.session.commit()
        return patient

    def update_patient(self, patient, data):
        patient.first_name = data.get('first_name', patient.first_name),
        patient.last_name = data.get('last_name', patient.last_name),
        patient.date_of_birth = data.get(
            'date_of_birth', patient.date_of_birth),
        patient.gender = data.get('gender', patient.gender),
        patient.address = data.get('address', patient.address),
        patient.phone_number = data.get('phone_number', patient.phone_number),
        patient.email = data.get('email', patient.email)
        db.session.commit()
        return patient

    def delete_patient(self, patient):
        db.session.delete(patient)
        db.session.commit()
        return patient


class PrescriptionRepository:
    def get_all_prescriptions(self):
        return Prescription.query.all()

    def get_prescription_by_id(self, prescription_id):
        return Prescription.query.get(prescription_id)

    def create_prescription(self, medicine_name, dosage, frequency, duration):
        prescription = Prescription(medicine_name=medicine_name,
                                    dosage=dosage, frequency=frequency, duration=duration)
        db.session.add(prescription)
        db.session.commit()
        return prescription

    def update_prescription(self, prescription, data):
        prescription.appointment_id = data.get(
            'appointment_id', prescription.appointment_id)
        prescription.medicine_name = data.get(
            'medicine_name', prescription.medicine_name)
        prescription.dosage = data.get('dosage', prescription.dosage)
        prescription.frequency = data.get('frequency', prescription.frequency)
        prescription.duration = data.get('duration', prescription.duration)
        db.session.commit()
        return prescription

    def delete_prescription(self, prescription):
        db.session.delete(prescription)
        db.session.commit()
        return prescription
