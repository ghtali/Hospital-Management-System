"""
This file contains the SQLAlchemy database models for the Hospital Management System.
"""

from .database import Base, db


class Doctor(Base):
    """
    The Doctor model class.
    """
    __tablename__ = 'doctors'

    # Fields
    name = db.Column(db.String(128), nullable=False)
    specialization = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the doctor object.
        """
        return f"<Doctor {self.id}>"


class Patient(Base):
    """
    The Patient model class.
    """
    __tablename__ = 'patients'

    # Fields
    name = db.Column(db.String(128), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the patient object.
        """
        return f"<Patient {self.id}>"


class Appointment(Base):
    """
    The Appointment model class.
    """
    __tablename__ = 'appointments'

    # Fields
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey(
        'doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patients.id'), nullable=False)

    # Relationships
    doctor = db.relationship(
        'Doctor', backref=db.backref('appointments', lazy=True))
    patient = db.relationship(
        'Patient', backref=db.backref('appointments', lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the appointment object.
        """
        return f"<Appointment {self.id}>"


class LabTest(Base):
    """
    The Lab Test model class.
    """
    __tablename__ = 'lab_tests'

    # Fields
    date = db.Column(db.Date, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey(
        'doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patients.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=False)

    # Relationships
    doctor = db.relationship(
        'Doctor', backref=db.backref('lab_tests', lazy=True))
    patient = db.relationship(
        'Patient', backref=db.backref('lab_tests', lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the lab test object.
        """
        return f"<LabTest {self.id}>"


class Prescription(Base):
    """
    The Prescription model class.
    """
    __tablename__ = 'prescriptions'

    # Fields
    date = db.Column(db.Date, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey(
        'doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patients.id'), nullable=False)
    medicine = db.Column(db.Text, nullable=False)

    # Relationships
    doctor = db.relationship(
        'Doctor', backref=db.backref('prescriptions', lazy=True))
    patient = db.relationship(
        'Patient', backref=db.backref('prescriptions', lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the prescription object.
        """
        return f"<Prescription {self.id}>"
