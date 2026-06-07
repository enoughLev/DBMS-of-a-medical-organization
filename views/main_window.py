from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QStatusBar
)

from views.patients_view import PatientsView
from views.doctors_view import DoctorsView
from views.visits_view import VisitsView
from views.audit_view import AuditView


class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db



        self.setWindowTitle("Медицинская информационная система")
        self.setGeometry(100, 100, 1200, 700)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.patients_view = PatientsView(self.db)
        self.doctors_view = DoctorsView(self.db)
        self.visits_view = VisitsView(self.db)
        self.audit_view = AuditView(self.db)

        self.tabs.addTab(self.patients_view, "Пациенты")
        self.tabs.addTab(self.doctors_view, "Врачи")
        self.tabs.addTab(self.visits_view, "Посещения")
        self.tabs.addTab(self.audit_view, "Журнал действий")

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Готов")


    def closeEvent(self, event):
        if self.db:
            self.db.disconnect()
        event.accept()