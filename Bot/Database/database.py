import sqlite3
import os

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.abspath("reports.db"))
        self.cursor = self.connection.cursor()
    def add_data(self,data):
        with self.connection:
            self.cursor.execute("INSERT INTO tickets (platform_name, platform_address, user_message, class_number, tg_id, status) VALUES (?,?,?,?,?,?)",(data["name"],data["address"],data["message"], data["class_number"], data["tg_id"], "В процессе"))
    def get_newest(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE id = (SELECT MAX(id) FROM tickets)")
            return self.cursor.fetchall()
    def get_data_by_id(self,index):
        with self.connection:
            self.cursor.execute("SELECT * FROM tickets WHERE id IS ?",(index,))
            return self.cursor.fetchall()
    def update_status(self,index, status):
        with self.connection:
            self.cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, index))
database = Database()