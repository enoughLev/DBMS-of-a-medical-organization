from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from models import AuditModel


class AuditView(QWidget):
    def __init__(self, db):
        super().__init__()
        self.model = AuditModel(db)
        self.init_ui()
        self.load_data()


    def init_ui(self):
        layout = QVBoxLayout(self)

        btn_layout = QHBoxLayout()
        self.refresh_btn = QPushButton("Обновить")
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        layout.addWidget(self.table)

        self.refresh_btn.clicked.connect(self.load_data)


    def load_data(self):
        rows = self.model.get_all()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID лога", "Сущность", "Операция",
            "Дата", "ID записи", "Пользователь",
            "Было", "Стало"
        ])

        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val) if val else ""))