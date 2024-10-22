import json
from operator import index
from random import choice

from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
import os

class ChoiceCluster(CallbackData, prefix="my"):
    cluster_number:int
    cluster_name:str

class ChoiceStructure(CallbackData, prefix="my"):
    cluster_number:int
    Structure_number: str

with open(os.path.abspath("schoollist.json"), 'r') as js:
    json_data = json.load(js)



Clusters = [
    InlineKeyboardButton(text="Кластер 1", callback_data=ChoiceCluster(cluster_number=1,cluster_name="Cluster1").pack()),
    InlineKeyboardButton(text="Кластер 2", callback_data=ChoiceCluster(cluster_number=2,cluster_name="Cluster2").pack()),
    InlineKeyboardButton(text="Кластер 3", callback_data=ChoiceCluster(cluster_number=3,cluster_name="Cluster3").pack())
]

Keyboard_clusters = {
    "Cluster1":[
        InlineKeyboardButton(text=json_data["cluster1"][0]["name"], callback_data="cl1_pf_1"),
        InlineKeyboardButton(text=json_data["cluster1"][1]["name"], callback_data="cl1_pf_2"),
        InlineKeyboardButton(text=json_data["cluster1"][2]["name"], callback_data="cl1_pf_3")
    ],

    "Cluster2":[
        InlineKeyboardButton(text=json_data["cluster2"][0]["name"], callback_data="cl1_pf_1"),
        InlineKeyboardButton(text=json_data["cluster2"][1]["name"], callback_data="cl1_pf_2"),
        InlineKeyboardButton(text=json_data["cluster2"][2]["name"], callback_data="cl1_pf_3")
    ],

    "Cluster3":[
        InlineKeyboardButton(text=json_data["cluster3"][0]["name"], callback_data="cl1_pf_1"),
        InlineKeyboardButton(text=json_data["cluster3"][1]["name"], callback_data="cl1_pf_2"),
        InlineKeyboardButton(text=json_data["cluster3"][2]["name"], callback_data="cl1_pf_3")
    ]
}

