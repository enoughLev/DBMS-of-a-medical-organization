from PyQt5.QtWidgets import (
    QDialog, QFormLayout, QComboBox, QLineEdit,
    QDateEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import QDate


class VisitDialog(QDialog):
    def __init__(self, parent=None, patients=None, doctors=None):
        super().__init__(parent)
        self.setWindowTitle("Новое посещение")
        self.setModal(True)
        self.setMinimumWidth(400)

        self.patients = patients or []
        self.doctors = doctors or []

        self.patient_combo = QComboBox()
        self.doctor_combo = QComboBox()
        self.healthy_combo = QComboBox()
        self.healthy_combo.addItems(["Здоров", "Есть жалобы"])
        self.prescription_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        for p in self.patients:
            self.patient_combo.addItem(f"{p[0]} - {p[1]}", p[0])
        for d in self.doctors:
            self.doctor_combo.addItem(f"{d[0]} - {d[1]} ({d[2]})", d[0])

        layout = QFormLayout(self)
        layout.addRow("Пациент:", self.patient_combo)
        layout.addRow("Врач:", self.doctor_combo)
        layout.addRow("Состояние:", self.healthy_combo)
        layout.addRow("Назначение:", self.prescription_input)
        layout.addRow("Дата:", self.date_input)

        btns_layout = QHBoxLayout()
        self.ok_btn = QPushButton("Сохранить")
        self.cancel_btn = QPushButton("Отмена")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        btns_layout.addWidget(self.ok_btn)
        btns_layout.addWidget(self.cancel_btn)
        layout.addRow(btns_layout)


    def get_data(self):
        return (
            self.patient_combo.currentData(),
            self.doctor_combo.currentData(),
            0 if self.healthy_combo.currentText() == "Здоров" else 1,
            self.prescription_input.text() or None,
            self.date_input.date().toString("yyyy-MM-dd")
        )