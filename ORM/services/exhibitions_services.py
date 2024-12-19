from sqlalchemy.exc import NoResultFound
from ORM.models.exhibitions import Exhibitions
from ORM.services.database import SessionLocal


class ExhibitionsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_exhibition(self, events_date: str, events_time: str, events_name: str, tickets_number: int) -> Exhibitions:
        """Создание новой выставки."""
        new_exhibitions = Exhibitions(
            events_date=events_date,
            events_time=events_time,
            events_name=events_name,
            tickets_number=tickets_number
        )
        self.db.add(new_exhibitions)
        self.db.commit()
        self.db.refresh(new_exhibitions)
        return new_exhibitions

    def get_exhibition(self, events_id: int) -> Exhibitions:
        """Выборка выстовок по ID."""
        exhibitions = self.db.query(Exhibitions).filter(
            Exhibitions.events_id == events_id).first()
        if not exhibitions:
            raise NoResultFound(f"Выстовка с ID {events_id} не найдена.")
        return exhibitions

    def get_all_exhibitions(self) -> list[Exhibitions]:
        """Выборка всех выставок."""
        return self.db.query(Exhibitions).all()

    def update_exhibition(self, events_id: int, events_date: str, events_time: str, events_name: str, tickets_number: int) -> Exhibitions:
        """Обновление информации о выставке."""
        exhibitions = self.get_exhibition(events_id)
        exhibitions.events_date = events_date
        exhibitions.events_time = events_time
        exhibitions.events_name = events_name
        exhibitions.tickets_number = tickets_number

        self.db.commit()
        self.db.refresh(exhibitions)
        return exhibitions

    def delete_exhibitions(self, events_id: int) -> None:
        """Удаление выставки по ID."""
        exhibitions = self.get_exhibition(events_id)
        self.db.delete(exhibitions)
        self.db.commit()