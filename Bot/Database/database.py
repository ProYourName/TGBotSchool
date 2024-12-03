import sqlite3

class Database:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    def get_newest(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE id = (SELECT MAX(id) FROM tickets)")
            return self.cursor.fetchall()
    def get_data_by_id(self,index):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE id IS ?",(index,))
            return self.cursor.fetchall()
    def get_data_by_tg_id(self,tg_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE tg_id IS ?",(tg_id,))
            return self.cursor.fetchall()
    def update_status(self,index, status):
        with self.connection:
            self.cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, index))
    def get_data_by_cluster(self,cluster_number, department):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE cluster_number IS ? AND department IS ?", (cluster_number, department))
            return self.cursor.fetchall()
    def add_data(self,data):
        with self.connection:
            self.cursor.execute("INSERT INTO tickets (platform_name, platform_address, user_message, class_number, tg_id, cluster_number, department, phone, FIO, status) VALUES (?,?,?,?,?,?,?,?,?,?)",(data["name"],data["address"],data["message"], data["class_number"], data["tg_id"], data["cluster"],data["department"], data["phone"], data["FIO"], "В процессе",))
            return None

