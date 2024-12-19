import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from ORM.services.database import SessionLocal
from ORM.services.excursions_services import ExcursionService
from ORM.services.exhibitions_services import ExhibitionsService


class TicketPurchaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Покупка билетов')
        self.setFixedSize(300, 250)
        self.setStyleSheet("background-color: #006633;")
        self.setWindowIcon(QIcon('resources/tickets'))

        self.ticket_price = 500  # цена взрослого билета
        self.ticket_label = QLabel("Билеты:")
        self.ticket_count = QSpinBox()
        self.ticket_count.setRange(0, 100)
        self.ticket_count.setStyleSheet("height: 30px; font-size: 16px;")

        self.ticket_slider = QSlider(Qt.Orientation.Horizontal)
        self.ticket_slider.setRange(0, 100)
        self.ticket_slider.valueChanged.connect(self.update_ticket_count)

        self.total_price_label = QLabel("Итого: 0 рублей")

        self.confirm_button = QPushButton("Подтвердить покупку")
        self.confirm_button.setStyleSheet("background-color: white; color: black;")
        self.confirm_button.clicked.connect(self.confirm_purchase)

        layout = QVBoxLayout()
        layout.addWidget(self.ticket_label)
        layout.addWidget(self.ticket_slider)
        layout.addWidget(self.ticket_count)
        layout.addWidget(self.total_price_label)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def update_ticket_count(self, value):
        self.ticket_count.setValue(value)
        self.update_total_price()

    def update_total_price(self):
        tickets = self.ticket_slider.value()
        total_price = (tickets * self.ticket_price)
        self.total_price_label.setText(f"Итого: {total_price} рублей")

    def confirm_purchase(self):
        tickets = self.ticket_slider.value()
        total_price = (tickets * self.ticket_price)
        QMessageBox.information(self, "Подтверждение покупки",
                                f"Вы купили {tickets} билетов. На сумму : {total_price}")


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Пользовательское окно')
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #006633;")

        layout = QVBoxLayout()

        self.ticket_button = QPushButton("Билеты")
        self.ticket_button.setStyleSheet("background-color: white; color: black;")
        self.ticket_button.clicked.connect(self.open_ticket_menu)
        layout.addWidget(self.ticket_button)

        self.excursions_button = QPushButton("Экскурсии")
        self.excursions_button.setStyleSheet("background-color: white; color: black;")
        self.excursions_button.clicked.connect(self.open_excursion_menu)
        layout.addWidget(self.excursions_button)

        self.exhibitions_button = QPushButton("Выставки")
        self.exhibitions_button.setStyleSheet("background-color: white; color: black;")
        self.exhibitions_button.clicked.connect(self.open_exhibitions_menu)
        layout.addWidget(self.exhibitions_button)

        layout = QVBoxLayout()
        layout.addWidget(self.ticket_button)
        layout.addWidget(self.excursions_button)
        layout.addWidget(self.exhibitions_button)

        self.setLayout(layout)

    def open_ticket_menu(self):
        self.ticket_window = TicketPurchaseWindow()
        self.ticket_window.show()

    def open_excursion_menu(self):
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

    def open_exhibitions_menu(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWin()
    user_window.show()
    sys.exit(app.exec())