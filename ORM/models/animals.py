from sqlalchemy import Column, Integer, String, BOOLEAN, Float
from ORM.services.database import Base


class Animals(Base):
    __tablename__ = 'animals'

    animals_id = Column(Integer, primary_key=True, index=True)
    animals_name = Column(String, nullable=False)
    animals_type = Column(String, nullable=False)
    animals_type_quantity = Column(Integer, nullable=False)
    animals_weight = Column(Float, nullable=False)
    animals_color = Column(String, nullable=False)
    animals_is_sick = Column(BOOLEAN, default=False)