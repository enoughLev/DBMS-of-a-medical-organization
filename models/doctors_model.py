from database import Database


class DoctorsModel:
    def __init__(self, db: Database):
        self.db = db


    def get_all(self):
        sql = "SELECT id, full_name, speciality, experience_years, degree, title FROM doctors ORDER BY id"
        return self.db.fetch_all(sql)


    def get_by_id(self, doctor_id):
        sql = "SELECT id, full_name, speciality, experience_years, degree, title FROM doctors WHERE id = :1"
        return self.db.fetch_one(sql, (doctor_id,))


    def insert(self, full_name, speciality, experience_years, degree, title):
        sql = """
            INSERT INTO doctors (id, full_name, speciality, experience_years, degree, title) 
            VALUES (seq_doctors_id.NEXTVAL, :1, :2, :3, :4, :5)
        """
        return self.db.execute(sql, (full_name, speciality, experience_years, degree, title))


    def update(self, doctor_id, full_name, speciality, experience_years, degree, title):
        sql = """
            UPDATE doctors 
            SET full_name = :1, speciality = :2, experience_years = :3, degree = :4, title = :5 
            WHERE id = :6
        """
        return self.db.execute(sql, (full_name, speciality, experience_years, degree, title, doctor_id))


    def delete(self, doctor_id):
        sql = "DELETE FROM doctors WHERE id = :1"
        return self.db.execute(sql, (doctor_id,))