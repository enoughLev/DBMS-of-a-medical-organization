from PyQt5.QtWidgets import (
    QDialog, QFormLayout, QLineEdit,
    QPushButton, QHBoxLayout
)


class DoctorDialog(QDialog):
    def __init__(self, parent=None, doctor_data=None):
        super().__init__(parent)
        self.doctor_data = doctor_data
        self.is_edit = doctor_data is not None

        self.setWindowTitle("Редактировать врача" if self.is_edit else "Новый врач")
        self.setModal(True)
        self.setMinimumWidth(350)

        self.fio_input = QLineEdit()
        self.speciality_input = QLineEdit()
        self.exp_input = QLineEdit()
        self.degree_input = QLineEdit()
        self.title_input = QLineEdit()

        layout = QFormLayout(self)
        layout.addRow("ФИО:", self.fio_input)
        layout.addRow("Специальность:", self.speciality_input)
        layout.addRow("Стаж (лет):", self.exp_input)
        layout.addRow("Ученая степень:", self.degree_input)
        layout.addRow("Ученое звание:", self.title_input)

        if self.is_edit:
            self.fio_input.setText(doctor_data[1])
            self.speciality_input.setText(doctor_data[2])
            self.exp_input.setText(str(doctor_data[3]) if doctor_data[3] else "")
            self.degree_input.setText(doctor_data[4] or "")
            self.title_input.setText(doctor_data[5] or "")

        btns_layout = QHBoxLayout()
        self.ok_btn = QPushButton("Сохранить")
        self.cancel_btn = QPushButton("Отмена")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        btns_layout.addWidget(self.ok_btn)
        btns_layout.addWidget(self.cancel_btn)
        layout.addRow(btns_layout)


    def get_data(self):
        exp_text = self.exp_input.text()
        exp = int(exp_text) if exp_text.isdigit() else None
        return (
            self.fio_input.text(),
            self.speciality_input.text(),
            exp,
            self.degree_input.text() or None,
            self.title_input.text() or None
        )