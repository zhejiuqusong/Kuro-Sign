"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-10-27 15:20:58
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-10-27 17:30:35
"""
from typing import List, TypedDict

import requests

from utils.common import ResponseModel, current_month, headers

class RoleModel(TypedDict):
    serverId: str
    serverName: str
    roleId: str
    userId: int
    gameId: int


class BaseSign:
    def __init__(self, game_id: int, server_id: str, role_id: str, user_id: int, game_name: str = "未知"):
        self.game_id = game_id
        self.server_id = server_id
        self.role_id = role_id
        self.user_id = user_id
        self.game_name = game_name

    def get_sign_prize(self):
        """
        获取签到奖品
        """

        urlqueryRecord = "https://api.kurobbs.com/encourage/signIn/queryRecordV2"
        data = {
            "gameId": self.game_id,
            "serverId": self.server_id,
            "roleId": self.role_id,
            "userId": self.role_id,
        }
        response = requests.post(urlqueryRecord, headers=headers, data=data)

        result: ResponseModel = response.json()
        data = result["data"]
        code = result["code"]
        if code != 200:
            return f"请求失败，响应代码: {code}, 消息: {result['msg']}"
        if isinstance(data, list) and len(data) > 0:
            first_goods_name = data[0]["goodsName"]
            return first_goods_name

        return "数据格式不正确或数据为空"

    def sign(self):
        sign_url = "https://api.kurobbs.com/encourage/signIn/v2"

        datasign = {
            "gameId": self.game_id,
            "serverId": self.server_id,
            "roleId": self.role_id,
            "userId": self.role_id,
            "reqMonth": current_month(),
        }
        response = requests.post(sign_url, headers=headers, data=datasign)
        result: ResponseModel = response.json()
        code = result["code"]
        if code != 200:
            return f"签到失败，响应代码: {code}, 消息: {result.get('msg')}"
        try:
            goods_names = self.get_sign_prize()
            return goods_names
        except ValueError as e:
            print(f"获取奖品失败: {e}")
            return None

    def __str__(self):
        return f"Sign(game_id={self.game_id}, server_id={self.server_id}, role_id={self.role_id}, user_id={self.user_id})"

def get_role_list(game_id):
    """
    获取角色列表
    """
    url = "https://api.kurobbs.com/gamer/role/list"

    data = {"gameId": game_id}

    response = requests.post(url, data=data, headers=headers)
    result: ResponseModel = response.json()
    if result["code"] == 200:
        role_list: List[RoleModel] = result["data"]
        return [BaseSign(game_id=role["gameId"], server_id=role["serverId"], role_id=role["roleId"], user_id=role["userId"], game_name=role["serverName"]) for role in role_list]
    return result["msg"]

if __name__ == "__main__":
    sign_list = get_role_list()
    for sign_obj in sign_list:
        print(sign_obj)
