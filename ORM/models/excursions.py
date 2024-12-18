from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from ORM.services.database import Base


class Excursions(Base):
    __tablename__ = 'excursions'

    events_id = Column(Integer, primary_key=True, index=True)
    events_date = Column(String, nullable=False)
    events_time = Column(String, nullable=False)
    events_name = Column(String, nullable=False)
    tickets_number = Column(Integer, nullable=False)