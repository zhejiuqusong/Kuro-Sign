import json
import os

from utils.common import BASE_PATH
from utils.update import CONFIG_TYPE, update_config

CONFIG_PATH = os.path.join(BASE_PATH, "config.json")


def read_config() -> CONFIG_TYPE:
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    raise FileNotFoundError("请将config.json.example重命名为config.json并填写信息")


def save_config(config: CONFIG_TYPE):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        return json.dump(config, f, indent=4)


class Config:
    def __init__(self):
        if os.environ.get("Kuro_Token"):
            self.config = None
        else:
            config = read_config()
            self.config = update_config(config)
            save_config(self.config)

    def get(self, key: str, default: None = None):
        if self.config is None:
            return os.environ.get("Kuro_" + key) or default
        return self.config.get(key, default)

    @property
    def token_list(self):
        """
        获取token列表
        """
        token = self.get("Token")
        return token.split("|")

    @property
    def sign_game(self):
        """
        获取签到游戏列表
        """
        game = self.get("SignGame")
        return game.split("|")
