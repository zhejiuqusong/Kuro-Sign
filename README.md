<!--
 * @Author: Night-stars-1 nujj1042633805@gmail.com
 * @Date: 2024-10-26 19:27:59
 * @LastEditors: Night-stars-1 nujj1042633805@gmail.com
 * @LastEditTime: 2024-10-27 17:29:34
-->
# Kuro-Sign
自动化完成库街区论坛与游戏签到任务

***你仅仅需要一个Token就可以完成所有内容，简单快捷***

## 使用说明

### 青龙面板
1. **创建订阅**：在青龙面板中创建新的订阅任务。
   - 名称：库街区签到
   - 类型：公开仓库
   - 链接：<https://github.com/Night-stars-1/Kuro-Sign.git>
   - 定时类型：crontab
   - 定时规则：0 0 * * *
   - 白名单：main.py
   - 依赖文件：utils|token.json.example
   - 文件后缀：py example
2. [设置配置文件或环境变量](#设置配置文件或环境变量)

### 源码运行
1. `pip install -r requirements`
2. [设置配置文件或环境变量](#设置配置文件或环境变量)
3. `python main.py`

## 设置配置文件或环境变量
> [!TIP]
> 配置文件和环境变量你只能选择一个
### 配置文件
- 将`config.json.example`重命名为`config.json`并填写里面的信息
### 环境变量
- 设置环境变量`Kuro_Token`的值为库街区的Token
- 其他环境变量为`Kuro_`+`config.json.example里面的键名`

## 配置注解
```json
{
    "Token": "键入token", // 登录Token
    "BbsSign": true, // 社区签到
    "LookPost": true, // 浏览帖子
    "LikePost": true, // 点赞帖子
    "SharePost": true, // 分享帖子
    "SignGame": "2|3", // 签到的游戏 战双->2 鸣潮->3
    "Source": "android" // Token的来源 app->android web->h5
}
```

## 关于Token
- 如果你不知道怎么抓包获取Token，可以使用[GetKjqToken](https://github.com/Night-stars-1/GetKjqToken)获取
