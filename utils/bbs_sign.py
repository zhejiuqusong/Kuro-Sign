"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-10-27 15:50:45
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-10-29 01:14:28
"""
from typing import List, TypedDict

import requests

from utils.common import ResponseModel, headers


class TaskItemModel(TypedDict):
    """完成次数"""

    completeTimes: int
    gainGold: int
    """目标次数"""
    needActionTimes: int
    process: float
    """任务名称"""
    remark: str
    skipType: int
    times: int

class ForumItemModel(TypedDict):
    """帖子Id"""
    postId: str
    """用户Id"""
    userId: str

def get_task_list() -> List[TaskItemModel]:
    url = "https://api.kurobbs.com/encourage/level/getTaskProcess"

    data = {"gameId": 0}
    response = requests.post(url, data=data, headers=headers)
    result: ResponseModel = response.json()
    return result["data"]["dailyTask"]

def bbs_sign(game_id):
    """
    论坛签到
    """
    url = "https://api.kurobbs.com/user/signIn"

    data = {"gameId": game_id}

    response = requests.post(url, data=data, headers=headers)
    result: ResponseModel = response.json()
    return result["msg"]

def get_forum_list() -> List[ForumItemModel]:
    """
    获取帖子列表
    """
    url = "https://api.kurobbs.com/forum/list"
    data = {
        "forumId": "9",
        "gameId": "3",
        "pageIndex": "1",
        "pageSize": "20",
        "searchType": "3",
        "timeType": "0"
    }
    response = requests.post(url, headers=headers, data=data)
    result: ResponseModel = response.json()
    return result["data"]["postList"]

def get_forum_detail(post_id):
    """
    获取帖子详情(用于完成阅读任务)

    :return: 帖子标题
    """
    url = "https://api.kurobbs.com/forum/getPostDetail"

    data = {
        "isOnlyPublisher": 0,
        "postId": post_id,
        "showOrderTyper": 2
    }
    response = requests.post(url, data=data, headers=headers)
    result: ResponseModel = response.json()
    title: str = result["data"]["postDetail"]["postTitle"]
    return title

def like(post_id, user_id):
    """
    点赞帖子
    """
    url = "https://api.kurobbs.com/forum/like"

    data = {
        "forumId": 11,
        "gameId": 3,
        "likeType": 1,
        "operateType": 1,
        "postCommentId": "",
        "postCommentReplyId": "",
        "postId": post_id,
        "postType": 1,
        "toUserId": user_id
    }

    response = requests.post(url, headers=headers, data=data)
    result: ResponseModel = response.json()
    if result["code"] == 200:
        return "点赞成功"
    else:
        return result["msg"]

def share():
    """
    分享贴子
    """

    url = "https://api.kurobbs.com/encourage/level/shareTask"

    data = {
        "gameId": 3,
    }

    response = requests.post(url, headers=headers, data=data)
    result: ResponseModel = response.json()
    if result["code"] == 200:
        return "分享成功"
    else:
        return result["msg"]
