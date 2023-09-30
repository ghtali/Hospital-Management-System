"""
This file contains the Patient model class.
"""

from .base import Base, db


class Patient(Base):
    """
    The Patient model class.
    """
    __tablename__ = 'patients'

    # Fields
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the patient object.
        """
        return f"<Patient {self.id}>"
