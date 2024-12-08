import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


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

        if username == "admin" and password == "123":
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
        self.setStyleSheet("background-color: green;")

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
        pass

    def open_employees_menu(self):
        pass

    def open_ticket_office_menu(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWin()
    admin_win.show()
    sys.exit(app.exec())