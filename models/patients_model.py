from database import Database


class PatientsModel:
    def __init__(self, db: Database):
        self.db = db


    def get_all(self):
        sql = "SELECT id, full_name, birth_date, address FROM patients ORDER BY id"
        return self.db.fetch_all(sql)


    def get_by_id(self, patient_id):
        sql = "SELECT id, full_name, birth_date, address FROM patients WHERE id = :1"
        return self.db.fetch_one(sql, (patient_id,))


    def insert(self, full_name, birth_date, address):
        sql = """
            INSERT INTO patients (id, full_name, birth_date, address) 
            VALUES (seq_patients_id.NEXTVAL, :1, TO_DATE(:2, 'YYYY-MM-DD'), :3)
        """
        return self.db.execute(sql, (full_name, birth_date, address))


    def update(self, patient_id, full_name, birth_date, address):
        sql = """
            UPDATE patients 
            SET full_name = :1, birth_date = TO_DATE(:2, 'YYYY-MM-DD'), address = :3 
            WHERE id = :4
        """
        return self.db.execute(sql, (full_name, birth_date, address, patient_id))


    def delete(self, patient_id):
        sql = "DELETE FROM patients WHERE id = :1"
        return self.db.execute(sql, (patient_id,))


    def get_last_id(self):
        sql = "SELECT seq_patients_id.CURRVAL FROM dual"
        return self.db.fetch_one(sql)