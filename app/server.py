# examples/server_simple.py
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from aiohttp import web
import asyncio
import asyncpg


async def handle(request):
    conn = await asyncpg.connect(user='projector', password='123',
                                 database='projector', host='172.17.0.2')
    values = await conn.fetch(
        'SELECT * FROM product'
    )
    await conn.close()

    list = []
    for row in values:
        list.append({
            'id': row['product_id'],
            'product': row['product'],
        })

    text = f' {list[0]}'

    return web.Response(text=text)


async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/echo', wshandle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, port=8080)
