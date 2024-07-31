DC = docker compose --env-file docker-compose/docker-env.env

APP_FILE = docker-compose/app_router.yaml
TODO_GRPC_SERVER = docker-compose/todo_service.yaml

.PHONY: app
app:
	${DC} -p app_router -f ${APP_FILE} up -d

.PHONY: app-build
app-build:
	${DC} -p app_router -f ${APP_FILE} up --build -d

.PHONY: drop-app
drop-app:
	${DC} -p app_router -f ${APP_FILE} down -v --remove-orphans

.PHONY: rm-app
rm-app:
	${DC} -p app_router -f ${APP_FILE} down --rmi "all"

.PHONY: app-logs
app-logs:
	${DC} -p todo -f ${APP_FILE} logs


.PHONY: todo
todo:
	${DC} -p todo -f ${TODO_GRPC_SERVER} up -d

.PHONY: todo-build
todo-build:
	${DC} -p todo -f ${TODO_GRPC_SERVER} up --build -d

.PHONY: drop-todo
drop-todo:
	${DC} -p todo -f ${TODO_GRPC_SERVER} down -v --remove-orphans

.PHONY: todo-logs
todo-logs:
	${DC} -p todo -f ${TODO_GRPC_SERVER} logs

.PHONY: rm-todo
rm-todo:
	${DC} -p todo -f ${TODO_GRPC_SERVER} down --rmi "all"

####
.PHONY: all-app
all-app:
	#${DC} -p app_todo -f ${TODO_GRPC_SERVER} -f ${APP_FILE} up -d
	${DC} -p app_todo -f ${TODO_GRPC_SERVER} -f ${APP_FILE} up -d

.PHONY: all-app-build
all-app-build:
	${DC} -p app_todo -f ${TODO_GRPC_SERVER} -f ${APP_FILE}  up --build -d

.PHONY: drop-all-app
drop-all-app:
	${DC} -p app_todo -f ${APP_FILE} -f ${TODO_GRPC_SERVER} down -v --remove-orphans

.PHONY: rm-all-app
rm-all-app:
	${DC} -p app_todo -f ${APP_FILE} -f ${TODO_GRPC_SERVER} down -v --rmi "all"

.PHONY: all-app-logs
all-app-logs:
	${DC} -p app_todo -f ${APP_FILE} -f ${TODO_GRPC_SERVER} logs

.PHONY: all-app-exec
all-app-exec:
	${DC} -p app_todo -f ${APP_FILE} -f ${TODO_GRPC_SERVER} exec -T app bash

.PHONY: all-app-restart
all-app-restart:
	${DC} -p app_todo -f ${APP_FILE} -f ${TODO_GRPC_SERVER} restart
