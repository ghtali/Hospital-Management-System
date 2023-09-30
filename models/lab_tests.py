"""
This file contains the LabTest model class.
"""

from .base import Base, db


class LabTest(Base):
    """
    The LabTest model class.
    """
    __tablename__ = 'lab_tests'

    # Fields
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the lab test object.
        """
        return f"<LabTest {self.id}>"
