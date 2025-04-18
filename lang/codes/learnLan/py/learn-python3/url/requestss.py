# -*- coding: utf-8 -*-

import json
import requests


url = "接口地址"
msg = "test"

def send_msg(url, msg):
    """
    requests使用示例.
    """
    sendMsg = {
        "msgtype": "text",
        "text": {
            "content": msg + "请及时处理",
        },
        "at": {
            "isAtAll": True
        }
    }

    
    headers = {"content-type": "application/json", "charset": "utf-8"}
    sendMsg = json.dumps(sendMsg)

    try:
        req = requests.post(url, data=sendMsg, headers=headers)
    except requests.HTTPError as e:
        print(e)
    
    return req.text

if __name__ == "__main__":
    res = send_msg(url, msg)
    print(res)