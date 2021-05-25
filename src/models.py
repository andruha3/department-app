from sqlalchemy.orm import relationship
from . import db
from datetime import datetime


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(80), nullable=False)
    employees = db.relationship(
        'Employee', backref='department', uselist=False)

    def __init__(self, department):
        self.department = department

    def __repr__(self):
        return f'Department - {self.department}'


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.String(80), db.ForeignKey(
        'department.id'), nullable=False)

    def __repr__(self):
        return f'Name - {self.name}, date of birth - {self.date_of_birth}, department - {self.department_id}, salary - {self.salary}'
