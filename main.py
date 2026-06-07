import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from database import Database
from views import MainWindow


def main():
    app = QApplication(sys.argv)

    db = Database()
    if not db.connect():
        QMessageBox.critical(None, "Ошибка", "Не удалось подключиться к базе данных")
        sys.exit(1)

    window = MainWindow(db)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()