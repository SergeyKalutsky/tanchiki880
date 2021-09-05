#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://206.81.21.227:8765"
    name = 'Sergey'
    while True:
        async with websockets.connect(uri) as websocket:
            await websocket.send(name)
            # print(f"> {name}")
            greeting = await websocket.recv()
            # print(f"< {greeting}")
            print(1)

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
loop.call_later(5, stop)
task = loop.create_task(hello())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass