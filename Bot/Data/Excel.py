import openpyxl
from Bot.Database.database import Database

database = Database("../reports.db")


def datashow(cluster_number, department):
    wb = openpyxl.load_workbook("../Data/temp.xlsx")
    wb.remove(wb['1'])
    wb.create_sheet('1')
    if department == 1:
        data = database.get_data_by_cluster(cluster_number,"Зав.хоз")
    elif department == 2:
        data = database.get_data_by_cluster(cluster_number, "Зав.хоз")

        print(data)


datashow(3,2)