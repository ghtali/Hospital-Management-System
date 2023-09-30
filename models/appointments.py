"""
This file contains the Appointment model class.
"""

from .base import Base, db


class Appointment(Base):
    """
    The Appointment model class.
    """
    __tablename__ = 'appointments'

    # Fields
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey(
        'doctors.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.Text)

    # Relationships
    patient = db.relationship(
        'Patient', backref=db.backref('appointments', lazy=True))
    doctor = db.relationship(
        'Doctor', backref=db.backref('appointments', lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the appointment object.
        """
        return f"<Appointment {self.id}>"
