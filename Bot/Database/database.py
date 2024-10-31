import sqlite3
import os

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.abspath("reports.db"))
        self.cursor = self.connection.cursor()
    def add_data(self,data):
        with self.connection:
            self.cursor.execute("INSERT INTO tickets (platform_name, platform_address, user_message, class_number, tg_id) VALUES (?,?,?,?,?)",(data["name"],data["address"],data["message"], data["class_number"], data["tg_id"]))





