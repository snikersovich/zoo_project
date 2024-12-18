from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ORM.models.excursions import Excursions
from ORM.services.database import SessionLocal


class ExcursionService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_excursion(self, events_date: str, events_time: str, events_name: str, tickets_number: int) -> Excursions:
        """Создание новой экскурсии."""
        new_excursions = Excursions(
            events_name=events_name,
            events_date=events_date,
            events_time=events_time,
            tickets_number=tickets_number
        )
        self.db.add(new_excursions)
        self.db.commit()
        self.db.refresh(new_excursions)
        return new_excursions

    def get_excursion(self, events_id: int) -> Excursions:
        """Выборка экскурсии по ID."""
        excursion = self.db.query(Excursions).filter(Excursions.events_id == events_id).first()
        if excursion is None:
            raise NoResultFound("Экскурсия не найдена.")
        return excursion

    def get_all_excursions(self) -> list[Excursions]:
        """Выборка всех экскурсий."""
        return self.db.query(Excursions).all()

    def update_excursion(self, events_id: int, events_date: str, events_time: str, events_name: str, tickets_number: int) -> Excursions:
        """Обновление информации о экскурсии."""
        excursion = self.get_excursion(events_id)
        excursion.events_date = events_date
        excursion.events_time = events_time
        excursion.events_name = events_name
        excursion.tickets_number = tickets_number

        self.db.commit()
        self.db.refresh(excursion)
        return excursion

    def delete_excursion(self, events_id: int) -> None:
        """Удаление экскурсии по ID."""
        excursion = self.get_excursion(events_id)
        self.db.delete(excursion)
        self.db.commit()