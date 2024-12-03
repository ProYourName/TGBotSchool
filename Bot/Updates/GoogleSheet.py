import gspread
import sqlite3
from oauth2client.service_account import ServiceAccountCredentials
from Bot.Database.database import Database

database = sqlite3.connect("../reports.db")
cursor = database.cursor()
cursor.execute("SELECT * FROM tickets")
data = cursor.fetchall()

# Привязка к таблице
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonkey.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open('ТГбот')
print(data)
# Получение данных
worksheet = spreadsheet.worksheet("Лист1")
