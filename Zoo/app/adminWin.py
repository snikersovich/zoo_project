import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

from ORM.services.database import init_db, SessionLocal
from ORM.services.animals_services import AnimalService
from ORM.services.employees_services import EmployeeService
from ORM.services.excursions_services import ExcursionService
from ORM.services.exhibitions_services import Exhibitions
from ORM.services.open_feeding_services import OpenFeedingService


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
        pass

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

        layout = QVBoxLayout()
        layout.addWidget(self.animals_table)
        self.animals_window.setLayout(layout)

        self.animals_window.show()

    def open_employees_menu(self):
        self.employees_window = QWidget()
        self.employees_window.setWindowTitle("Сотрудники")
        self.employees_window.resize(800, 600)

        self.employees_table = QTableWidget()
        self.employees_table.setColumnCount(4)
        self.employees_table.setHorizontalHeaderLabels(["Имя", "Должность", "Зарплата", "Дата найма"])

        db = SessionLocal()
        employee_service = EmployeeService(db)
        employees = employee_service.get_all_employees()
        db.close()

        self.employees_table.setRowCount(len(employees))
        for row, employee in enumerate(employees):
            self.employees_table.setItem(row, 0, QTableWidgetItem(employee.name))
            self.employees_table.setItem(row, 1, QTableWidgetItem(employee.position))
            self.employees_table.setItem(row, 2, QTableWidgetItem(str(employee.salary)))
            self.employees_table.setItem(row, 3, QTableWidgetItem(employee.hire_date.strftime("%d-%m-%Y")))

        layout = QVBoxLayout()
        layout.addWidget(self.employees_table)
        self.employees_window.setLayout(layout)

        self.employees_window.show()

    def open_ticket_office_menu(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWin()
    admin_win.show()
    sys.exit(app.exec())