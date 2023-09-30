"""
This file contains the Doctor model class.
"""

from .base import Base, db


class Doctor(Base):
    """
    The Doctor model class.
    """
    __tablename__ = 'doctors'

    # Fields
    name = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the doctor object.
        """
        return f"<Doctor {self.id}>"
