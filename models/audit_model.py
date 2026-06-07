from database import Database


class AuditModel:
    def __init__(self, db: Database):
        self.db = db


    def get_all(self):
        sql = """
            SELECT log_id, entity_name, operation_type, operation_date, 
                   record_id, executed_by, 
                   old_data,
                   new_data
            FROM log_table
            ORDER BY log_id DESC
        """
        return self.db.fetch_all(sql)


    def get_by_date_range(self, start_date, end_date):
        sql = """
            SELECT log_id, entity_name, operation_type, operation_date, record_id, executed_by,
            old_data, new_data
            FROM log_table
            WHERE operation_date BETWEEN :1 AND :2
            ORDER BY log_id DESC
        """
        return self.db.fetch_all(sql, (start_date, end_date))


    def get_by_operation_type(self, op_type):
        sql = """
            SELECT log_id, entity_name, operation_type, operation_date, record_id, executed_by,
                   SUBSTR(old_data, 1, 100), SUBSTR(new_data, 1, 100)
            FROM log_table
            WHERE operation_type = :1
            ORDER BY log_id DESC
        """
        return self.db.fetch_all(sql, (op_type,))