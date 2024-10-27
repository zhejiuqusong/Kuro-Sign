<!--
 * @Author: Night-stars-1 nujj1042633805@gmail.com
 * @Date: 2024-10-26 19:27:59
 * @LastEditors: Night-stars-1 nujj1042633805@gmail.com
 * @LastEditTime: 2024-10-27 17:25:53
-->
# Kuro-Sign
自动化完成库街区论坛与游戏签到任务

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
> 配置文件和环境变量你只需要选择一个
### 配置文件
- 将`token.json.example`重命名为`token.json`并填写里面的信息
### 环境变量
- 设置环境变量`Kuro-Token`的值为库街区的Token

## 关于Token
- 如果你不知道怎么抓包获取Token，可以使用[GetKjqToken](https://github.com/Night-stars-1/GetKjqToken)获取
