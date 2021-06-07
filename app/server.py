from aiohttp import web
from aiopg.sa import create_engine
from dotenv import dotenv_values

from views import routes

config = dotenv_values("example.env")


async def create_aiopg(app):
    """
    Creates database connection.
    """
    app['pg_engine'] = await create_engine(dsn=config['PG_DSN'])


async def dispose_aiopg(app):
    """
    Closes database connection.
    """
    app['pg_engine'].close()
    await app['pg_engine'].wait_closed()


if __name__ == '__main__':
    app = web.Application()

    app.on_startup.append(create_aiopg)
    app.on_cleanup.append(dispose_aiopg)

    app.add_routes(routes)

    web.run_app(app, port=80)
