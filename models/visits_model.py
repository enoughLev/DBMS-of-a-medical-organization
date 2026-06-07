from database import Database


class VisitsModel:
    def __init__(self, db: Database):
        self.db = db


    def get_all_with_names(self):
        sql = """
            SELECT v.id, p.full_name as patient, d.full_name as doctor, 
                   v.pacient_healthy, v.doctors_prescription, v.visit_date
            FROM patient_visits v
            JOIN patients p ON v.patient_id = p.id
            JOIN doctors d ON v.doctor_id = d.id
            ORDER BY v.visit_date DESC
        """
        return self.db.fetch_all(sql)


    def insert(self, patient_id, doctor_id, pacient_healthy, doctors_prescription, visit_date):
        sql = """
            INSERT INTO patient_visits (id, patient_id, doctor_id, pacient_healthy, doctors_prescription, visit_date) 
            VALUES (seq_visits_id.NEXTVAL, :1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
        """
        return self.db.execute(sql, (patient_id, doctor_id, pacient_healthy, doctors_prescription, visit_date))


    def get_patients_for_combo(self):
        sql = "SELECT id, full_name FROM patients ORDER BY full_name"
        return self.db.fetch_all(sql)


    def get_doctors_for_combo(self):
        sql = "SELECT id, full_name, speciality FROM doctors ORDER BY full_name"
        return self.db.fetch_all(sql)