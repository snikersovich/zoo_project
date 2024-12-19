import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont

from ORM.services.database import init_db, SessionLocal
from ORM.services.animals_services import AnimalService
from ORM.services.employees_services import EmployeeService
from ORM.services.excursions_services import ExcursionService
from ORM.services.exhibitions_services import ExhibitionsService


class AdminWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вход администратора')
        self.setWindowIcon(QIcon('resources/zamok'))
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: #006633;")

        self.login_label = QLabel('Логин:')
        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("background-color: white; color: black;")

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("background-color: white; color: black;")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.submit_button = QPushButton('Войти')
        self.submit_button.setStyleSheet("background-color: white; color: black;")
        self.submit_button.clicked.connect(self.check_credentials)

        font = QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_input.setFont(font)
        self.password_label.setFont(font)
        self.password_input.setFont(font)
        self.submit_button.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.login_input.text()
        password = self.password_input.text()

        if username == "123" and password == "123":
            QMessageBox.information(self, 'Успех', 'Вход выполнен успешно!')
            self.open_admin_dashboard()
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')

    def open_admin_dashboard(self):
        self.dashboard = AdminDashboard()
        self.dashboard.show()


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Панель администратора')
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #006633;")

        layout = QVBoxLayout()

        self.animals_button = QPushButton('Животные')
        self.animals_button.setStyleSheet("background-color: white; color: black;")
        self.animals_button.clicked.connect(self.open_animals_menu)
        layout.addWidget(self.animals_button)


        self.employees_button = QPushButton('Сотрудники')
        self.employees_button.setStyleSheet("background-color: white; color: black;")
        self.employees_button.clicked.connect(self.open_employees_menu)
        layout.addWidget(self.employees_button)

        self.events_button = QPushButton('Мероприятия')
        self.events_button.setStyleSheet("background-color: white; color: black;")
        self.events_button.clicked.connect(self.open_events_menu)
        layout.addWidget(self.events_button)

        self.ticket_office_button = QPushButton('Касса')
        self.ticket_office_button.setStyleSheet("background-color: white; color: black;")
        self.ticket_office_button.clicked.connect(self.open_ticket_office_menu)
        layout.addWidget(self.ticket_office_button)

        font = QFont()
        font.setPointSize(12)
        self.animals_button.setFont(font)
        self.employees_button.setFont(font)
        self.events_button.setFont(font)
        self.ticket_office_button.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.animals_button)
        layout.addWidget(self.employees_button)
        layout.addWidget(self.events_button)
        layout.addWidget(self.ticket_office_button)

        self.setLayout(layout)

    def open_events_menu(self):
        self.events_window = QWidget()
        self.events_window.setWindowTitle("Мероприятия")
        self.events_window.resize(400, 300)
        self.events_window.setStyleSheet("background-color: #006633;")

        button_excursions = QPushButton("Экскурсии", self)
        button_excursions.clicked.connect(self.on_button_excursions_clicked)
        button_excursions.setStyleSheet("background-color: white; color: black;")

        button_exhibitions = QPushButton("Выставки", self)
        button_exhibitions.clicked.connect(self.on_button_exhibitions_clicked)
        button_exhibitions.setStyleSheet("background-color: white; color: black;")

        layout = QVBoxLayout()
        layout.addWidget(button_excursions)
        layout.addWidget(button_exhibitions)

        self.events_window.setLayout(layout)
        self.events_window.show()

    def on_button_excursions_clicked(self):
        self.excursions_window = QWidget()
        self.excursions_window.setWindowTitle("Экскурсии")
        self.excursions_window.resize(800, 600)

        excursions_table = QTableWidget()
        excursions_table.setColumnCount(4)
        excursions_table.setHorizontalHeaderLabels(
            ["Дата", "Время", "Название экскурсии", "Количесвто билетов"]
        )
        db = SessionLocal()
        excursions_services = ExcursionService(db)
        excursions = excursions_services.get_all_excursions()
        db.close()

        excursions_table.setRowCount(len(excursions))

        for row, excursion in enumerate(excursions):
            excursions_table.setItem(row, 0, QTableWidgetItem(str(excursion.events_date)))
            excursions_table.setItem(row, 1, QTableWidgetItem(str(excursion.events_time)))
            excursions_table.setItem(row, 2, QTableWidgetItem(str(excursion.events_name)))
            excursions_table.setItem(row, 3, QTableWidgetItem(int(excursion.tickets_number)))

        layout = QVBoxLayout()
        layout.addWidget(excursions_table)
        self.excursions_window.setLayout(layout)
        self.excursions_window.show()

    def on_button_exhibitions_clicked(self):
        self.exhibitions_window = QWidget()
        self.exhibitions_window.setWindowTitle("Выставки")
        self.exhibitions_window.resize(800, 600)

        exhibitions_table = QTableWidget()
        exhibitions_table.setColumnCount(4)
        exhibitions_table.setHorizontalHeaderLabels(
            ["Дата", "Время", "Название выставки", "Количество билетов"]
        )
        db = SessionLocal()
        exhibitions_services = ExhibitionsService(db)
        exhibitions = exhibitions_services.get_all_exhibitions()
        db.close()

        exhibitions_table.setRowCount(len(exhibitions))

        for row, exhibition in enumerate(exhibitions):
            exhibitions_table.setItem(row, 0, QTableWidgetItem(str(exhibition.events_date)))
            exhibitions_table.setItem(row, 1, QTableWidgetItem(str(exhibition.events_time)))
            exhibitions_table.setItem(row, 2, QTableWidgetItem(str(exhibition.events_name)))
            exhibitions_table.setItem(row, 3, QTableWidgetItem(int(exhibition.tickets_number)))

        layout = QVBoxLayout()
        layout.addWidget(exhibitions_table)
        self.exhibitions_window.setLayout(layout)
        self.exhibitions_window.show()

    def open_animals_menu(self):
        self.animals_window = QWidget()
        self.animals_window.setWindowTitle("Животные")
        self.animals_window.resize(800, 600)

        self.animals_table = QTableWidget()
        self.animals_table.setColumnCount(6)
        self.animals_table.setHorizontalHeaderLabels(["Имя", "Тип", "Количество", "Вес", "Цвет", "Заболевание"])

        db = SessionLocal()
        animals_services = AnimalService(db)
        animals = animals_services.get_all_animals()
        db.close()

        self.animals_table.setRowCount(len(animals))

        for row, animal in enumerate(animals):
            self.animals_table.setItem(row, 0, QTableWidgetItem(str(animal.animals_name)))
            self.animals_table.setItem(row, 1, QTableWidgetItem(str(animal.animals_type)))
            self.animals_table.setItem(row, 2,
                                       QTableWidgetItem(str(animal.animals_type_quantity)))
            self.animals_table.setItem(row, 3, QTableWidgetItem(str(animal.animals_weight)))
            self.animals_table.setItem(row, 4, QTableWidgetItem(str(animal.animals_color)))
            self.animals_table.setItem(row, 5, QTableWidgetItem("Да" if animal.animals_is_sick else "Нет"))

        layout = QVBoxLayout()
        layout.addWidget(self.animals_table)
        self.animals_window.setLayout(layout)

        self.animals_window.show()

    def open_employees_menu(self):
        self.employees_window = QWidget()
        self.employees_window.setWindowTitle("Сотрудники")
        self.employees_window.resize(800, 600)

        self.employees_table = QTableWidget()
        self.employees_table.setColumnCount(10)
        self.employees_table.setHorizontalHeaderLabels(["Должность", "Имя", "Фамилия", "Пол", "Возраст", "Образование",
                                                        "Номер телефона", "Опыт работы", "Логин", "Пароль"])

        db = SessionLocal()
        employee_service = EmployeeService(db)
        employees = employee_service.get_all_employees()
        db.close()

        self.employees_table.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            self.employees_table.setItem(row, 0, QTableWidgetItem(str(employee.employees_position)))
            self.employees_table.setItem(row, 1, QTableWidgetItem(str(employee.employees_name)))
            self.employees_table.setItem(row, 2, QTableWidgetItem(str(employee.employees_last_name)))
            self.employees_table.setItem(row, 3, QTableWidgetItem(str(employee.employees_sex)))
            self.employees_table.setItem(row, 4, QTableWidgetItem(int(employee.employees_age)))
            self.employees_table.setItem(row, 5, QTableWidgetItem(str(employee.employees_education)))
            self.employees_table.setItem(row, 6, QTableWidgetItem(int(employee.employees_phone_number)))
            self.employees_table.setItem(row, 7, QTableWidgetItem(int(employee.employees_experience)))
            self.employees_table.setItem(row, 8, QTableWidgetItem(int(employee.employees_login)))
            self.employees_table.setItem(row, 9, QTableWidgetItem(int(employee.employees_password)))

        layout = QVBoxLayout()
        layout.addWidget(self.employees_table)
        self.employees_window.setLayout(layout)

        self.employees_window.show()

    def open_ticket_office_menu(self):
        self.ticket_office_window = QWidget()
        self.ticket_office_window.setWindowTitle("Касса")
        self.ticket_office_window.resize(800, 600)

        # Логика кассы

        layout = QVBoxLayout()
        self.ticket_office_window.setLayout(layout)

        self.ticket_office_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWin()
    admin_win.show()
    sys.exit(app.exec())
