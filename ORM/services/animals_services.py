from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ORM.models.animals import Animals


class AnimalService:
    def __init__(self, db: Session):
        self.db = db

    def add_animal(self, name: str, animal_type: str, quantity: int, weight: float, color: str, is_sick: bool = False) -> Animals:
        """Добавление нового животного в базу данных"""
        new_animal = Animals(
            animals_name=name,
            animals_type=animal_type,
            animals_type_quantity=quantity,
            animals_weight=weight,
            animals_color=color,
            animals_is_sick=is_sick
        )
        self.db.add(new_animal)
        self.db.commit()
        self.db.refresh(new_animal)
        return new_animal

    def get_animal(self, animal_id: int) -> Animals:
        """Выборка животного по ID"""
        animal = self.db.query(Animals).filter(Animals.animals_id == animal_id).first()
        if animal is None:
            raise NoResultFound(f"Животное с ID {animal_id} не найдено.")
        return animal

    def update_animal(self, animal_id: int, **kwargs) -> Animals:
        """Обновление информации животного."""
        animal = self.get_animal(animal_id)
        for key, value in kwargs.items():
            if hasattr(animal, key):
                setattr(animal, key, value)
        self.db.commit()
        self.db.refresh(animal)
        return animal

    def delete_animal(self, animal_id: int) -> bool:
        """Удаление животного из базы данных по ID."""
        animal = self.get_animal(animal_id)
        self.db.delete(animal)
        self.db.commit()
        return True

    def get_all_animals(self):
        """Выборка всех животных из базы данных."""
        return self.db.query(Animals).all()

    def get_animals_by_type(self, animal_type: str):
        """Выборка животных из базы данных по типу."""
        return self.db.query(Animals).filter(Animals.animals_type == animal_type).all()
