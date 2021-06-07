from sqlalchemy import (
    orm,
    MetaData,
    Column,
    Integer,
    String,
    Table,
    ForeignKey)

Base = orm.declarative_base()

movie_actors = Table('movie_actors', Base.metadata,
                     Column('movie_id', Integer, ForeignKey('movies.movies.id')),
                     Column('actor_id', Integer, ForeignKey('actors.actors.id'))
                     )


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)

    actors = orm.relationship(
        'Actor',
        secondary=movie_actors,
        back_populates='movies')


class Actor(Base):
    __tablename__ = 'actors'

    actor_id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    age = Column(Integer)
