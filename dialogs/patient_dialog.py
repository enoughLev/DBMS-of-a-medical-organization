from PyQt5.QtWidgets import (
    QDialog, QFormLayout, QLineEdit,
    QDateEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import QDate


class PatientDialog(QDialog):
    def __init__(self, parent=None, patient_data=None):
        super().__init__(parent)
        self.patient_data = patient_data
        self.is_edit = patient_data is not None

        self.setWindowTitle("Редактировать пациента" if self.is_edit else "Новый пациент")
        self.setModal(True)
        self.setMinimumWidth(350)

        self.fio_input = QLineEdit()
        self.birth_input = QDateEdit()
        self.birth_input.setCalendarPopup(True)
        self.birth_input.setDate(QDate.currentDate())
        self.address_input = QLineEdit()

        layout = QFormLayout(self)
        layout.addRow("ФИО:", self.fio_input)
        layout.addRow("Дата рождения:", self.birth_input)
        layout.addRow("Адрес:", self.address_input)

        if self.is_edit:
            self.fio_input.setText(patient_data[1])
            bdate = QDate.fromString(str(patient_data[2]), "yyyy-MM-dd")
            self.birth_input.setDate(bdate)
            self.address_input.setText(patient_data[3] or "")

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
            self.fio_input.text(),
            self.birth_input.date().toString("yyyy-MM-dd"),
            self.address_input.text()
        )