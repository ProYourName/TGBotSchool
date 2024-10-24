import sqlite3
import os

async def add_data_db(data):
    connection = sqlite3.connect(os.path.abspath("reports.db"))
    cursor = connection.cursor()
    cursor.execute("BEGIN")
    cursor.execute("INSERT INTO tickets (platform_name, platform_address, user_message) VALUES (?,?,?)",(data["name"],data["address"],data["message"]))
    cursor.execute("COMMIT")
    connection.close()

