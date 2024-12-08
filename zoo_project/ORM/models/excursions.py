from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from ORM.services.database import Base


class Excursions(Base):
    __tablename__ = 'excursions'

    events_id = Column(Integer, primary_key=True, index=True)
    events_date = Column(Integer, nullable=False)
    events_time = Column(Integer, nullable=False)
    events_name = Column(String, nullable=False)