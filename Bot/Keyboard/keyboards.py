import json
from aiogram.types import InlineKeyboardButton
import os

with open(os.path.abspath("schoollist.json"), 'r') as js:
    json_data = json.load(js)

Clusters = [
    InlineKeyboardButton(text="Кластер 1", callback_data="cl1"),
    InlineKeyboardButton(text="Кластер 2", callback_data="cl2"),
    InlineKeyboardButton(text="Кластер 3", callback_data="cl3")
]

Keyboard_cluster1 = [
    InlineKeyboardButton(text=json_data["cluster1"][0]["name"], callback_data="cl1_pf_1"),
    InlineKeyboardButton(text=json_data["cluster1"][1]["name"], callback_data="cl1_pf_2"),
    InlineKeyboardButton(text=json_data["cluster1"][2]["name"], callback_data="cl1_pf_3")
]
