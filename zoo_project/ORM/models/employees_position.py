from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from ORM.services.database import Base


class Employees_position(Base):
    __tablename__ = 'employees_position'

    employees_position_id = Column(Integer, primary_key=True, index=True)
    employees_id = Column(Integer, ForeignKey=True, index=True)
    position_name = Column(String, nullable=False)