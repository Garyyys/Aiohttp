cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

build:
	docker network inspect $(NETWORK_NAME) || docker network create $(NETWORK_NAME)
	docker build -t $(DB_HOST) db/
	docker create $(DB_HOST) -net $(NETWORK_NAME) --name $(DB_HOST) $(DB_HOST)
	docker build -t $(APP_HOST) app/
	docker create $(APP_HOST) -net $(NETWORK_NAME) --name $(APP_HOST) $(APP_HOST)

run:
	docker start $(DB_HOST) || docker run -d --env-file=./config.env -p$(DB_PORT):5432 --name $(DB_HOST) --net $(NETWORK_NAME) $(DB_HOST)
	timeout 5
	docker start $(APP_HOST) || docker run -d --env-file=./config.env -p=$(APP_PORT):80 --name $(APP_HOST) --net $(NETWORK_NAME) $(APP_HOST)

stop:
	docker stop $(APP_HOST)
	docker stop $(DB_HOST)
