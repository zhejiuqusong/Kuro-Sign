"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-10-27 15:38:10
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-10-27 17:37:53
"""
from datetime import datetime
import json
import os
import random
import string
from typing import TypedDict


class ResponseModel(TypedDict):
    code: int
    msg: str
    data: list

def random_string(length: int):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def current_month():
    now = datetime.now()
    return now.strftime("%m")

def read_config():
    if os.path.exists("config.json"):
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    raise FileNotFoundError("请将config.json.example重命名为config.json并填写信息")

if not (token := os.environ.get("Kuro_Token")):
    token = read_config()["token"]

headers = {
    "User-Agent": "okhttp/3.11.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "devCode": random_string(40),
    "source": "android",
    "version": "2.2.5",
    "versionCode": "2250",
    "token": token,
}
