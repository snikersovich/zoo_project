from PyQt6.QtWidgets import QApplication
from Zoo.app.mainWin import MainWin
import sys
import traceback

from database import init_db, SessionLocal
from ORM.services.animals_services import AnimalService
from ORM.services.employees_services import EmployeeService


def main():
    init_db()
    db = SessionLocal()

    try:
        # animals_service = AnimalService(db)
        #
        # animals_service.add_animal("Лев", "Хищник", 1, 250, "Рыжий", False)
        # animals_service.add_animal("Зебра", "Травоядное", 2, 350, "Черно-белый", True)
        # animals_service.add_animal("Жираф", "Травоядное", 1, 1200, "Пятнистый", False)
        # animals_service.add_animal("Медведь", "Всеядное", 2, 500, "Коричневый", False)
        # animals_service.add_animal("Обезьяна", "Всеядное", 3, 70, "Серый", True)
        # animals_service.add_animal("Слон", "Травоядное", 1, 6000, "Серый", False)
        # animals_service.add_animal("Тигр", "Хищник", 1, 300, "Оранжевый с черными полосами", False)
        # animals_service.add_animal("Антилопа", "Травоядное", 4, 150, "Бежевый", True)
        # animals_service.add_animal("Попугай", "Всеядное", 2, 50, "Разноцветный", False)
        # animals_service.add_animal("Крокодил", "Хищник", 1, 1000, "Зеленый", False)
        #
        # employees_services = EmployeeService(db)
        #
        # employees_services.add_employee("Кассир", "Олег", "Жвакин", "Муж", 32, "Есть", 89145632987, 4, "110", "111"),
        # employees_services.add_employee("Уборщик", "Иван","Костров", "Муж", 48, "Нет", 89142321234, 1, "112", "113"),
        # employees_services.add_employee("Системный администратор", "Александр", "Макшнакнекс", "Муж", 23, "Есть", 89141234312, 2, "114", "115"),
        # employees_services.add_employee("Экскурсовод", "Жанна", "Кислая", "Жен", 28, "Есть", 89141284563, 5, "116", "117"),
        # employees_services.add_employee("Экскурсовод", "Алексей", "Морской", "Муж", 30, "Нет", 89149875632, 6, "118", "119"),
        # employees_services.add_employee("Ветеринар", "Мария", "Веселая", "Жен", 39, "Есть", 89145632133, 9, "120", "121"),
        # employees_services.add_employee("Рабочий кормлений животных", "Петр", "Парацетомол", "Муж", 18, "Нет", 89145621297, 0, "122", "123"),
        # employees_services.add_employee("Администратор", "Александра", "Гордеева", "Жен", 41, "Есть", 89145453721, 10, "124", "125"),
        # employees_services.add_employee("Охраник", "Евгений", "Барсов", "Муж", 52, "Есть", 89145424321, 8, "124", "125")

    finally:
        db.close()
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

