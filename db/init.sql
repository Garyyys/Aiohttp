CREATE USER projector WITH PASSWORD '123';
CREATE DATABASE projector WITH ENCODING 'utf-8';
GRANT ALL PRIVILEGES ON DATABASE projector to projector;

\c projector

set role projector;

CREATE TABLE movies (
    movie_id serial PRIMARY KEY,
    name text NOT NULL,
    year int NOT NULL
);

CREATE TABLE  actors(
    actor_id serial PRIMARY KEY,
    name text NOT NULL,
    country text NOT NULL,
    age int NOT NULL
);

CREATE TABLE movie_actors(
    movie_id int REFERENCES movies (movie_id) ON UPDATE CASCADE ON DELETE CASCADE,
    actor_id int REFERENCES actors (actor_id) ON UPDATE CASCADE,
    CONSTRAINT movie_actors_pkey PRIMARY KEY (movie_id, actor_id)
);
