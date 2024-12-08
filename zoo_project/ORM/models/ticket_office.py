from sqlalchemy import Column, Integer, String, BOOLEAN, Float
from ORM.services.database import Base


class Ticket_office(Base):
    __tablename__ = 'Ticket_office'

    working_hours = Column(Float, nullable=False)
    ticket_prices = Column(Integer, nullable=False)
    tickets_sold = Column(Integer, nullable=False)
    tickets_quantity = Column(Integer, nullable=False)