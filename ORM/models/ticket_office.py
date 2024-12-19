from sqlalchemy import Column, Integer, String, BOOLEAN, Float
from ORM.services.database import Base


class Ticket_office(Base):
    __tablename__ = 'Ticket_office'

    ticket_prices = Column(Integer, nullable=False)

    excursion_tickets_sold = Column(Integer, nullable=False)
    exhibitions_tickets_sold = Column(Integer, nullable=False)
    open_feeding_tickets_sold = Column(Integer, nullable=False)

    excursion_tickets_quantity = Column(Integer, nullable=False)
    exhibitions_tickets_quantity = Column(Integer, nullable=False)
    open_feeding_tickets_quantity = Column(Integer, nullable=False)
