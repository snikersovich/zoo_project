from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from ORM.services.database import Base


class Employees(Base):
    __tablename__ = 'employees'

    employees_id = Column(Integer, primary_key=True, index=True)
    employees_position = Column(Integer, ForeignKey=True, index=True)
    employees_name = Column(String, nullable=False)
    employees_sex = Column(String, nullable=False)
    employees_bday = Column(Integer, nullable=False)
    employees_education = Column(String, nullable=False)
    employees_phone_number = Column(Integer, nullable=False)
    employees_experience = Column(Integer, nullable=False)
    employees_login = Column(String, nullable=False)
    employees_password = Column(Integer, nullable=False)
