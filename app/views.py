from aiohttp import web
from models import Movie, Actor

routes = web.RouteTableDef()


@routes.get('/')
async def movies(request):
    movies = []

    async with request.app['pg_engine'].acquire() as conn:
        async for row in conn.execute(Movie.__table__.select()):
            movies.append({
                'movie_id': row.movie_id,
                'name': row.name,
                'year': row.year
            })

    data = {
        'movies': movies
    }

    return web.json_response(data)


@routes.post('/add/')
async def add_movie(request):
    movies = []

    async with request.app['pg_engine'].acquire() as conn:
        data = await request.post()

        await conn.execute(Movie.__table__.insert().values(
            name=data['name'],
            year=data['year']
        ))

    return web.json_response({'status': 'ok'}, status=201)


@routes.get('/actors/')
async def actors(request):
    actors = []

    async with request.app['pg_engine'].acquire() as conn:
        async for row in conn.execute(Actor.__table__.select()):
            actors.append({
                'actor_id': row.actor_id,
                'name': row.name,
                'country': row.country,
                'age': row.age
            })

    data = {
        'actors': actors
    }

    return web.json_response(data)


@routes.post('/actors/add/')
async def add_actors(request):
    actors = []

    async with request.app['pg_engine'].acquire() as conn:
        data = await request.post()

        await conn.execute(Actor.__table__.insert().values(
            name=data['name'],
            country=data['country'],
            age=data['age'],
        ))

    return web.json_response({'status': 'ok'}, status=201)
