import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import datetime
import zlib
import numpy
import time

def stream_gzip_decompress(stream):
    zlib.r
    dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
    for chunk in stream:
        rv = dec.decompress(chunk)
        if rv:
            yield rv

def inflate(data):
    decompress = zlib.decompressobj(
            16 + zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def toString(data) :
    for d in data :
        r = chr(d)
        print(r)

def on_message(ws, message):
    dtime = datetime.datetime.now()
    un_time = time.mktime(dtime.timetuple())
    print(un_time)
    print("### message ###")
    print(message)

def on_data(ws,data) :
    print("### data ###")
    print(data)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### opened ###")
    # {"channel": "kline", "params": "type=15min&symbol=btc_usdt&sinc=1"}
    sendMsg = "{\"event\":\"addChannel\",\"channel\":\"ok_sub_spot_usd_btc_kline_15min\"}"
    #
    sendMsg = "{\"event\": \"addChannel'\",\"parameters\": {\"base\": \"btc\", \"binary\": \"1\", \"period\": \"15min\", \"product\": \"spot\", \"quote\": \"usd\", \"type\": \"kline\"}}"
    # sendMsg="{\"channel\":\"allprice\"}"
    print(sendMsg)
    def run(*args):
        ws.send(sendMsg)
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://real.okex.com:10441/websocket",
                              header=['Sec-WebSocket-Extensions: permessage-deflate',
                                      'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                                      'Connection: keep-alive, Upgrade',
                                      'Pragma: no-cache'],
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              on_data=on_data)
    ws.on_open = on_open
    ws.run_forever(http_proxy_host='127.0.0.1',http_proxy_port='8123')

