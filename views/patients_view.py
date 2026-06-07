from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView
)
from models import PatientsModel
from dialogs import PatientDialog


class PatientsView(QWidget):
    def __init__(self, db):
        super().__init__()
        self.model = PatientsModel(db)
        self.init_ui()
        self.load_data()


    def init_ui(self):
        layout = QVBoxLayout(self)

        # Кнопки
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Добавить")
        self.edit_btn = QPushButton("Изменить")
        self.delete_btn = QPushButton("Удалить")
        self.refresh_btn = QPushButton("Обновить")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Таблица
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        # Сигналы
        self.add_btn.clicked.connect(self.on_add)
        self.edit_btn.clicked.connect(self.on_edit)
        self.delete_btn.clicked.connect(self.on_delete)
        self.refresh_btn.clicked.connect(self.load_data)


    def load_data(self):
        rows = self.model.get_all()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО", "Дата рождения", "Адрес"])

        for i, row in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(i, 1, QTableWidgetItem(row[1]))
            self.table.setItem(i, 2, QTableWidgetItem(str(row[2]) if row[2] else ""))
            self.table.setItem(i, 3, QTableWidgetItem(row[3] or ""))


    def on_add(self):
        dialog = PatientDialog(self)
        if dialog.exec_():
            data = dialog.get_data()
            self.model.insert(*data)
            self.load_data()


    def on_edit(self):
        current = self.table.currentRow()
        if current < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования")
            return

        pid = int(self.table.item(current, 0).text())
        row = self.model.get_by_id(pid)
        if row:
            dialog = PatientDialog(self, row)
            if dialog.exec_():
                data = dialog.get_data()
                self.model.update(pid, *data)
                self.load_data()


    def on_delete(self):
        current = self.table.currentRow()
        if current < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для удаления")
            return

        pid = int(self.table.item(current, 0).text())
        fio = self.table.item(current, 1).text()

        reply = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить пациента:\n{pid} - {fio}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.model.delete(pid)
            self.load_data()