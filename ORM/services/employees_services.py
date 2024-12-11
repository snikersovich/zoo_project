from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ORM.models.employees import Employees
from ORM.services.database import SessionLocal


class EmployeeService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_employee(self, position: str, name: str, last_name: str, sex: str, age: int, education: str, phone_number: int,
                     experience: int, login: str, password: str) -> Employees:
        """Добавление нового сотрудника в базу данных."""
        new_employee = Employees(
            employees_position=position,
            employees_name=name,
            employees_last_name=last_name,
            employees_sex=sex,
            employees_age=age,
            employees_education=education,
            employees_phone_number=phone_number,
            employees_experience=experience,
            employees_login=login,
            employees_password=password
        )
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_employee(self, employee_id: int) -> Employees:
        """Выборка сотрудника из базы данных по ID."""
        employee = self.db.query(Employees).filter(Employees.employees_id == employee_id).first()
        if not employee:
            raise NoResultFound("Сотрудник не найден")
        return employee

    def update_employee(self, employee_id: int, **kwargs) -> Employees:
        """Обновление информации сотрудника."""
        employee = self.get_employee(employee_id)
        for key, value in kwargs.items():
            setattr(employee, key, value)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete_employee(self, employee_id: int) -> None:
        """Удаления сотрудника из базы данных по ID."""
        employee = self.get_employee(employee_id)
        self.db.delete(employee)
        self.db.commit()

    def get_all_employees(self):
        """Выборка всех сотрудников из базы данных."""
        return self.db.query(Employees).all()


