import json
from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
import os

class ChoiceCluster(CallbackData, prefix="cluster"):
    cluster_number:int
    cluster_name:str

class BackButton(CallbackData, prefix="back"):
    stage: str

class ChoiceStructure(CallbackData, prefix="platform"):
    cluster_number:int
    structure_number: int
class ChoiceDep(CallbackData, prefix="platform"):
    department_choice:str

with open(os.path.abspath("schoollist.json"), 'r') as js:
    json_data = json.load(js)



Clusters = [
    InlineKeyboardButton(text="Варшавская", callback_data=ChoiceCluster(cluster_number=1,cluster_name="Cluster1").pack()),
    InlineKeyboardButton(text="Чертановский", callback_data=ChoiceCluster(cluster_number=2,cluster_name="Cluster2").pack()),
    InlineKeyboardButton(text="Аннино", callback_data=ChoiceCluster(cluster_number=3,cluster_name="Cluster3").pack()),
    InlineKeyboardButton(text="Назад", callback_data=BackButton(stage="1").pack())
]

department = [InlineKeyboardButton(text="Зав.хоз.", callback_data=ChoiceDep(department_choice="Зав.хоз").pack()),
              InlineKeyboardButton(text="ИТ-отдел", callback_data=ChoiceDep(department_choice="ИТ-отдел").pack())]

Keyboard_clusters = {
    "Cluster1":[
        InlineKeyboardButton(text=json_data["cluster1"][0]["name"], callback_data=ChoiceStructure(cluster_number=1,structure_number=0).pack()),
        InlineKeyboardButton(text=json_data["cluster1"][1]["name"], callback_data=ChoiceStructure(cluster_number=1,structure_number=1).pack()),
        InlineKeyboardButton(text=json_data["cluster1"][2]["name"], callback_data=ChoiceStructure(cluster_number=1,structure_number=2).pack()),
        InlineKeyboardButton(text="Назад", callback_data=BackButton(stage="2").pack())

    ],

    "Cluster2":[
        InlineKeyboardButton(text=json_data["cluster2"][0]["name"], callback_data=ChoiceStructure(cluster_number=2,structure_number=0).pack()),
        InlineKeyboardButton(text=json_data["cluster2"][1]["name"], callback_data=ChoiceStructure(cluster_number=2,structure_number=1).pack()),
        InlineKeyboardButton(text=json_data["cluster2"][2]["name"], callback_data=ChoiceStructure(cluster_number=2,structure_number=2).pack()),
        InlineKeyboardButton(text=json_data["cluster2"][3]["name"], callback_data=ChoiceStructure(cluster_number=2,structure_number=3).pack()),
        InlineKeyboardButton(text="Назад", callback_data=BackButton(stage="2").pack())
    ],

    "Cluster3":[
        InlineKeyboardButton(text=json_data["cluster3"][0]["name"], callback_data=ChoiceStructure(cluster_number=3,structure_number=0).pack()),
        InlineKeyboardButton(text=json_data["cluster3"][1]["name"], callback_data=ChoiceStructure(cluster_number=3,structure_number=1).pack()),
        InlineKeyboardButton(text=json_data["cluster3"][2]["name"], callback_data=ChoiceStructure(cluster_number=3,structure_number=2).pack()),
        InlineKeyboardButton(text=json_data["cluster3"][3]["name"], callback_data=ChoiceStructure(cluster_number=3,structure_number=3).pack()),
        InlineKeyboardButton(text="Назад", callback_data=BackButton(stage="2").pack())
    ]
}

