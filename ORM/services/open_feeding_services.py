from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ORM.models.open_feeding import Open_feeding
from ORM.services.database import SessionLocal


class OpenFeedingService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_open_feeding(self, events_date: str, events_time: str, events_name: str) -> Open_feeding:
        """Добавление нового открытого кормления."""
        new_feeding = Open_feeding(
            events_date=events_date,
            events_time=events_time,
            events_name=events_name
        )
        self.db.add(new_feeding)
        self.db.commit()
        self.db.refresh(new_feeding)
        return new_feeding

    def get_open_feeding(self, events_id: int) -> Open_feeding:
        """Выборка кормления из базы данных по ID."""
        feeding = self.db.query(Open_feeding).filter(Open_feeding.events_id == events_id).first()
        if not feeding:
            raise NoResultFound(f"Открытое кормление с ID {events_id} не найдено.")
        return feeding

    def get_all_open_feedings(self) -> list[Open_feeding]:
        """Выборка всех кормлений из базы данных."""
        return self.db.query(Open_feeding).all()

    def update_open_feeding(self, events_id: int, events_date: str, events_time: str, events_name: str) -> Open_feeding:
        """Обновление информации о кормлении."""
        feeding = self.get_open_feeding(events_id)
        feeding.events_date = events_date
        feeding.events_time = events_time
        feeding.events_name = events_name
        self.db.commit()
        return feeding

    def delete_open_feeding(self, events_id: int) -> None:
        """Удаление кормления из базы данных по ID."""
        feeding = self.get_open_feeding(events_id)
        self.db.delete(feeding)
        self.db.commit()