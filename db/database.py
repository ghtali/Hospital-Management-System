from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """
    The base model class.
    """
    __abstract__ = True

    # Fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return f"<{self.__class__.__name__} {self.id}>"

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Returns True if the two objects are equal.
        """
        return self.id == other.id
