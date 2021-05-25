from src.models import Department, Employee
from . import ma


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True
