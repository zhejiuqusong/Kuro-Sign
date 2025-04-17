from typing import Union


CONFIG_TYPE = dict[str, Union[str, bool]]


def update_config_v1(config: CONFIG_TYPE) -> CONFIG_TYPE:
    return {
        "version": 2,
        "Token": config.get("token", ""),
        "BbsSign": True,
        "LookPost": True,
        "LikePost": True,
        "SharePost": True,
        "SignGame": "2|3",
        "Source": "android",
    }


def update_config(config: CONFIG_TYPE):
    match config.get("version", 1):
        case 1:
            return update_config_v1(config)
        case _:
            return config
