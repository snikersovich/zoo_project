from PyQt6.QtWidgets import QApplication
from Zoo.app.mainWin import MainWin
import sys
import traceback

from database import init_db, SessionLocal
from ORM.services.animals_services import AnimalService


def main():
    init_db()
    db = SessionLocal()

    try:
        animals_service = AnimalService(db)

        animals_service.add_animal("Лев", "Хищник", 1, 250, "Рыжий", False)
        animals_service.add_animal("Зебра", "Травоядное", 2, 350, "Черно-белый", True)
        animals_service.add_animal("Жираф", "Травоядное", 1, 1200, "Пятнистый", False)
        animals_service.add_animal("Медведь", "Всеядное", 2, 500, "Коричневый", False)
        animals_service.add_animal("Обезьяна", "Всеядное", 3, 70, "Серый", True)
        animals_service.add_animal("Слон", "Травоядное", 1, 6000, "Серый", False)
        animals_service.add_animal("Тигр", "Хищник", 1, 300, "Оранжевый с черными полосами", False)
        animals_service.add_animal("Антилопа", "Травоядное", 4, 150, "Бежевый", True)
        animals_service.add_animal("Попугай", "Всеядное", 2, 50, "Разноцветный", False)
        animals_service.add_animal("Крокодил", "Хищник", 1, 1000, "Зеленый", False)

    finally:
        db.close()
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

