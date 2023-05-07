"""
This file contains the Prescription model class.
"""

from .base import Base, db


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
