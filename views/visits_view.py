from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtWidgets import QMessageBox
from models import VisitsModel
from dialogs import VisitDialog


class VisitsView(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.model = VisitsModel(db)
        self.init_ui()
        self.load_data()


    def init_ui(self):
        layout = QVBoxLayout(self)

        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Добавить посещение")
        self.refresh_btn = QPushButton("Обновить")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.add_btn.clicked.connect(self.on_add)
        self.refresh_btn.clicked.connect(self.load_data)


    def load_data(self):
        rows = self.model.get_all_with_names()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Пациент", "Врач", "Состояние", "Назначение", "Дата"])

        for i, row in enumerate(rows):
            healthy = "Здоров" if row[3] == 0 else "Есть жалобы"
            self.table.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(i, 1, QTableWidgetItem(row[1]))
            self.table.setItem(i, 2, QTableWidgetItem(row[2]))
            self.table.setItem(i, 3, QTableWidgetItem(healthy))
            self.table.setItem(i, 4, QTableWidgetItem(row[4] or ""))
            self.table.setItem(i, 5, QTableWidgetItem(str(row[5]) if row[5] else ""))


    def on_add(self):
        patients = self.model.get_patients_for_combo()
        doctors = self.model.get_doctors_for_combo()

        if not patients:
            QMessageBox.warning(self, "Ошибка", "Нет пациентов в базе данных")
            return
        if not doctors:
            QMessageBox.warning(self, "Ошибка", "Нет врачей в базе данных")
            return

        dialog = VisitDialog(self, patients, doctors)
        if dialog.exec_():
            data = dialog.get_data()
            self.model.insert(*data)
            self.load_data()