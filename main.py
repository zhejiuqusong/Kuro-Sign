"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-10-26 19:27:59
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-10-29 19:47:50
"""

"""
任务名称
name: 库街区签到任务
定时规则
cron: 1 9 * * *
"""
import random

from notify import send
from utils.bbs_sign import (
    bbs_sign,
    get_forum_detail,
    get_forum_list,
    get_task_list,
    like,
    share,
)
from utils.game_sign import get_role_list

GAME_LIST = [2, 3]
MESSAGE = []


def log(str):
    MESSAGE.append(str)
    print(str)


if __name__ == "__main__":
    for game_id in GAME_LIST:
        sign_list = get_role_list(game_id)
        if isinstance(sign_list, str):
            raise ValueError(sign_list)
        for sign_obj in sign_list:
            sign_status = sign_obj.sign()
            log(f"{sign_obj.game_name}签到：{sign_status}")
    task_list = get_task_list()
    forum_list = get_forum_list()
    for task in task_list:
        time = task["needActionTimes"] - task["completeTimes"]
        for i in range(time):
            if task["remark"] == "用户签到":
                sign_status = bbs_sign(random.choice(GAME_LIST))
                log(f"用户签到: {sign_status}")
            elif task["remark"] == "浏览3篇帖子":
                title = get_forum_detail(forum_list[i]["postId"])
                log(f"阅读帖子：{title}")
            elif task["remark"] == "点赞5次":
                like_status = like(forum_list[i]["postId"], forum_list[i]["userId"])
                log(f"点赞帖子：{forum_list[i]['postTitle']} - {like_status}")
            elif task["remark"] == "分享1次帖子":
                share_status = share()
                log(f"分享帖子: {share_status}")
        if time == 0:
            log(f"{task['remark']}: 已完成")
    send("库街区", "\n".join(MESSAGE))
