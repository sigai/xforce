import socketio

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
# standard Python
sio = socketio.Client()


@sio.event
def connect():
    print('connection established')

@sio.event
def message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('wss://exchange.xforce.ibmcloud.com/socket.io/?EIO=3&transport=websocket', headers=headers, namespaces=["/ticker_us-blue"])

print('my sid is', sio.sid)

sio.emit("my_message", "40/jobtracker,")
sio.wait()
