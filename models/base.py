"""
This file contains the base model and database configuration.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """
    The base model class that all other models inherit from.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        """
        Saves the model to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Deletes the model from the database.
        """
        db.session.delete(self)
        db.session.commit()
