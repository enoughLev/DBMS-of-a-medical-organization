import cx_Oracle
from PyQt5.QtWidgets import QMessageBox
from config import DB_USER, DB_PASSWORD, DB_DSN


class Database:
    def __init__(self):
        self.connection = None


    def connect(self):
        try:
            self.connection = cx_Oracle.connect(
                DB_USER,
                DB_PASSWORD,
                DB_DSN
            )
            return True
        except Exception as e:
            QMessageBox.critical(None, "Ошибка БД", f"Не удалось подключиться:\n{e}")
            return False


    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None


    def execute(self, sql, params=None):
        if not self.connection:
            if not self.connect():
                return None
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params or {})
            self.connection.commit()
            return cursor
        except Exception as e:
            self.connection.rollback()
            QMessageBox.critical(None, "Ошибка SQL", f"{sql}\n\n{e}")
            return None


    def fetch_all(self, sql, params=None):
        cursor = self.execute(sql, params)
        if cursor:
            return cursor.fetchall()
        return []


    def fetch_one(self, sql, params=None):
        cursor = self.execute(sql, params)
        if cursor:
            return cursor.fetchone()
        return None