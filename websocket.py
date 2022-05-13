import matplotlib.pyplot as pit
import time

import matplotlib.pyplot as plt
import websockets
import asyncio
import json

xdate = []
ydate = []

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()


def update_graph():
    ax.plot(xdate, ydate)
    fig.canvas.draw()
    plt.pause(0.1)


async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            event_time = time.localtime(data['E'] // 1000)
            event_time_1 = f'{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}'
            print(event_time_1, '->', data['c'])
            xdate.append(event_time_1)
            ydate.append(int(float(data['c'])))
            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
