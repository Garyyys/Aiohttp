from os import environ
from aiohttp import web
from aiopg.sa import create_engine
from views import routes


async def create_aiopg(app):
    """
    Creates database connection.
    """
    dsn = environ.get('PG_DSN')

    if not dsn:
        raise Exception('PG_DSN environment variable is missing')

    app['pg_engine'] = await create_engine(dsn=dsn)


async def dispose_aiopg(app):
    """
    Closes database connection.
    """
    app['pg_engine'].close()
    await app['pg_engine'].wait_closed()

app_port=environ.get('APP_RUN_PORT')

if __name__ == '__main__':
    app = web.Application()

    app.on_startup.append(create_aiopg)
    app.on_cleanup.append(dispose_aiopg)

    app.add_routes(routes)

    web.run_app(app, port=app_port)
