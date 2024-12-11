from sqlalchemy import Column, Integer, String, BOOLEAN, Float
from ORM.services.database import Base


class Open_feeding(Base):
    __tablename__ = 'open_feeding'

    events_id = Column(Integer, primary_key=True, index=True)
    events_date = Column(String, nullable=False)
    events_time = Column(String, nullable=False)
    events_name = Column(String, nullable=False)