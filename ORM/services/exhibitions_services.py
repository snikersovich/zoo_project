from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ORM.models.exhibitions import Exhibitions
from ORM.services.database import SessionLocal


class ExhibitionsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_exhibitions(self, events_date: str, events_time: str, events_name: str) -> Exhibitions:
        """Создание новой выставки."""
        new_exposition = Exhibitions(
            events_date=events_date,
            events_time=events_time,
            events_name=events_name
        )
        self.db.add(new_exposition)
        self.db.commit()
        self.db.refresh(new_exposition)
        return new_exposition

    def get_exhibitions(self, events_id: int) -> Exhibitions:
        """Выборка выстовок по ID."""
        exhibitions = self.db.query(Exhibitions).filter(
            Exhibitions.events_id == events_id).first()
        if not exhibitions:
            raise NoResultFound(f"Выстовка с ID {events_id} не найдена.")
        return exhibitions

    def get_all_exhibitions(self) -> list[Exhibitions]:
        """Выборка всех выставок."""
        return self.db.query(Exhibitions).all()

    def update_exhibitions(self, events_id: int, events_date: str = None, events_time: str = None,
                          events_name: str = None) -> Exhibitions:
        """Обновление информации о выставке."""
        exhibitions = self.get_exhibitions(events_id)

        if events_date is not None:
            exhibitions.events_date = events_date
        if events_time is not None:
            exhibitions.events_time = events_time
        if events_name is not None:
            exhibitions.events_name = events_name

        self.db.commit()
        self.db.refresh(exhibitions)
        return exhibitions

    def delete_exhibitions(self, events_id: int) -> None:
        """Удаление выставки по ID."""
        exhibitions = self.get_exhibitions(events_id)
        self.db.delete(exhibitions)
        self.db.commit()