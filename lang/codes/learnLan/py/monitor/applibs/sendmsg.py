# -*- coding: utf-8 -*-
"""
发送消息
"""
import json
import requests

from config import AppConfig


def send_msg(msg):
    smsg = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "isAtAll": True
        }
    }
    header = {
        "content-type": "application/json",
        "charset": "utf-8"
    }

    smsg = json.dumps(smsg)

    try:
        _ = requests.post(AppConfig.ding_url, data=smsg, headers=header)
    except requests.HTTPError as e:
        print(e)
