"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-10-27 15:38:10
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2025-02-04 23:57:28
"""

import os
import random
import string
from datetime import datetime
from typing import TypedDict

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

class ResponseModel(TypedDict):
    code: int
    msg: str
    data: list


def random_string(length: int):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def current_month():
    now = datetime.now()
    return now.strftime("%m")

def set_token(token: str, source: str):
    """
    设置headers 的 token 和 Token来源
    """
    headers["token"] = token
    if source in ["android", "h5"]:
        headers["source"] = source

headers = {
    "User-Agent": "okhttp/3.11.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "devCode": random_string(40),
    "source": "android",
    "version": "2.2.5",
    "versionCode": "2250",
}
