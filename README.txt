1. Билдим контейнеры: в директории db, app и прописываем "docker build .".
2. Поднимаем db : docker run -e POSTGRES_PASSWORD=123 -p 8081:5432 <cache, берем значение после билда>.
3. Узнать IP db, для этого выполняем команду: docker ps (узнаем ID или name)
   - далее прописываем docker inspect <name or ID cont> и оттуда берем значение IP.
   - Заходим в файл example.env, находим параметр 'host' и меняем значение на IP нашего db контейнера.
4. Поднимаем app: docker run -p 8080:80 <cache, берем значение после билда>
5. Создаем свою docker bridge network: docker network create <name>
    5.1 Узнать имена контейнеров или ID: docker ps
6. Подключаем контейнеры к docker bridge network: docker network connect <network name> <container name>
    6.1 Если нужно проверить, находятсья ли контейнеры внутри bridge network исполняем команду:
        docker inspect <network name>
7. В ./db/ находим schema.sql и создаем таблицы.
8. Заходим в браузер и прописываем localhost:8080.

Реализованный функционал:
    - отправка POST запроса для Movie (localhost:8080/add/)
    - отправка POST запроса для Actors (localhost:8080/actors/add/)

    - отправка GET запросов для таблицы Movie (localhost:8080/)
    - отправка GET запросов для таблицы Actors (localhost:8080/actors/)