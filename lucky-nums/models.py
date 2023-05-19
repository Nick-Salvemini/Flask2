from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class LuckyNumber(db.Model):
    '''Lucky Number Information'''
    
    __tablename__ = 'lucky_number'

    name =db.Column(
        db.Text,
        nullable=False
    )

    email = db.Column(
        db.Text,
        nullable=False
    )

    birth_year = db.Column(
        db.Integer,
        nullable=False
    )

    color = db.Column(
        db.Text
    )

    __table_args__ = (
        CheckConstraint(birth_year >= 1900, name = 'birth_year_min'),
        CheckConstraint(birth_year <= 2000, name = 'birth_year_max'),
        CheckConstraint(color.in_(['red', 'green', 'orange', 'blue']), name = 'color_list')
    )

    def serialize(self):
        """Returns a dict representation of todo which we can turn into JSON"""
        return {
            'name': self.name,
            'email': self.email,
            'birth_year': self.birth_year,
            'color': self.color,
        }