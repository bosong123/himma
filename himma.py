import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import datetime
from time import sleep
# def on_message(ws, message):
#
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     print("### opened ###")
#     # {"channel": "kline", "params": "type=15min&symbol=btc_usdt&sinc=1"}
#     sendMsg="{\"channel\":\"kline\",\"params\":\"type=15min&symbol=btc_usdt&sinc=1\"}"
#     ws.send(sendMsg)
#     # sendMsg="{\"channel\":\"allprice\"}"
#     print(sendMsg)
#     def run(*args):
#         while(True) :
#             ws.send("{'event':'ping'}")
#             sleep(5)
#             ws.send(sendMsg)
#     thread.start_new_thread(run, ())

class ooobtc(websocket.WebSocketApp) :
    def __init__(self,url,header,cookie):
        self.ws = websocket.WebSocketApp(url=url,header=header,cookie=cookie,
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_open=self.on_open,
                                         on_open=self.on_open)

    def on_open(self):
        print("### opened ###")

    def on_message(self,message):
        print(message)

    def on_error(self):
        print("### error ###")

    def on_close(self):
        print("### error ###")


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://io.ooobtc.com/",
                              header=['Sec-WebSocket-Extensions: permessage-deflate',
                                      'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                                      'Connection: keep-alive, Upgrade',
                                      'Pragma: no-cache'],
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              cookie='cf_clearance=0222b5f8492b848375aad272e62d5ab92acc3ca2-1534554986-2592000-250; '
                                     '__cfduid=d223ee8f374252374a33bb1c73c7031ec1534554987; '
                                     '_ga=GA1.2.1537291927.1534554991;'
                                     ' _gid=GA1.2.1934247124.1534554991')
    ws.on_open = on_open
    ws.run_forever(http_proxy_host='127.0.0.1',http_proxy_port='8123')

