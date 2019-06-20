import json
from websocket import create_connection
from time import sleep

import requests

header_token = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cookie": "__cfduid=da2d78979170742a913d51a14a7fa1a0b1560947858",
    "dnt": "1",
    "referer": "https://exchange.xforce.ibmcloud.com/activity/map",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "x-ui": "XFE"
}
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Cookie": "__cfduid=da2d78979170742a913d51a14a7fa1a0b1560947858",
    "Host": "exchange.xforce.ibmcloud.com",
    "Origin": "https://exchange.xforce.ibmcloud.com",
    "Pragma": "no-cache",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    "Sec-WebSocket-Key": "IOvX7f0otQ5A2kKX9Pi5iA==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
url = "https://exchange.xforce.ibmcloud.com/api/auth/socketToken"
res = requests.get(url, headers=header_token)
print(res)
