from datetime import datetime
from flask.globals import request, session
from flask_restful import Resource
from src.schemas import DepartmentSchema, EmployeeSchema
from . import api, db
from .models import Department, Employee
from marshmallow import ValidationError


class DepartmentList(Resource):
    department_schema = DepartmentSchema()

    def get(self, id=None):
        if not id:
            departments = db.session.query(Department).all()
            return self.department_schema.dump(departments, many=True), 200
        department = db.session.query(Department).filter_by(id=id).first()
        if not department:
            return '', 404
        return self.department_schema.dump(department), 200

    def post(self):
        try:
            department = self.department_schema.load(
                request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(department)
        db.session.commit()
        return {'message': 'Created successfully'}, 201

    def put(self, id):
        department = db.session.query(Department).filter_by(id=id).first()
        if not department:
            return '', 404
        try:
            department = self.department_schema.load(
                request.json, instance=department, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        return {'message': 'Updated successfully'}, 200

    def delete(self, id):
        department = db.session.query(Department).filter_by(id=id).first()
        if not department:
            return '', 404
        db.session.delete(department)
        db.session.commit()
        return {'message': 'Deleted successfully'}, 204


class EmployeeList(Resource):
    employee_schema = EmployeeSchema()

    def get(self, id=None):
        if not id:
            employees = db.session.query(Employee).all()
            return self.employee_schema.dump(employees, many=True), 200
        employee = db.session.query(Employee).filter_by(id=id).first()
        if not employee:
            return '', 404
        return self.employee_schema.dump(employee), 200

    def post(self):
        try:
            employee = self.employee_schema.load(
                request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(employee)
        db.session.commit()
        return {'message': 'Created successfully'}, 201

    def put(self, id):
        employee = db.session.query(Employee).filter_by(id=id).first()
        if not employee:
            return '', 404
        try:
            employee = self.employee_schema.load(
                request.json, instance=employee, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, id):
        employee = db.session.query(Employee).filter_by(id=id).first()
        if not employee:
            return '', 404
        employee = self.employee_schema.load(
            request.json, instance=employee, session=db.session)
        name, date_of_birth, salary, department_id = employee

        if name:
            employee.name = name
        elif date_of_birth:
            employee.date_of_birth = date_of_birth
        elif salary:
            employee.salary = salary
        elif department_id:
            employee.department_id = department_id

        return {'message': 'Updated successfully'}, 200

    def delete(self, id):
        employee = db.session.query(Employee).filter_by(id=id).first()
        if not employee:
            return '', 404
        db.session.delete(employee)
        db.session.commit()
        return {'message': 'Deleted successfully'}, 204


api.add_resource(DepartmentList, '/departments',
                 '/departments/<id>', strict_slashes=False)
api.add_resource(EmployeeList, '/employees',
                 '/employees/<id>', strict_slashes=False)
