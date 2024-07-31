uvicorn --factory api.app:create_fastapi_app --reload --host 0.0.0.0 --port 8000

[//]: # (python3 -m grpc_tools.protoc -I. --python_out=./grpc_compiled --grpc_python_out=./grpc_compiled image_transform.proto)
[//]: # (python3 -m grpc_tools.protoc -I ./protos --python_out=./protos --grpc_python_out=./protos todo.proto)
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./proto/todo.proto
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. protos/todo.proto


router gets clinet via DI, sends grpc req to running grpc service, its handled returned, in router 
converted to json

### Stage 2
* each mservice should compile the grpc files 
docker exec -it e319cdb071ef /bin/bash



#.PHONY: app
#app:
#	${DC} -f ${APP_FILE} -f ${TODO_GRPC_SERVER} up -d
#
#.PHONY: app-build
#app-build:
#	${DC} -f ${APP_FILE} -f ${TODO_GRPC_SERVER} up --build -d
#
#.PHONY: drop-app
#drop-app:
#	${DC} -f ${APP_FILE} -f ${TODO_GRPC_SERVER} down -v
#
#.PHONY: rm-app
#rm-app:
#	${DC} -f ${APP_FILE} -f ${TODO_GRPC_SERVER} down --rmi "all"
#.PHONY: all-logs
#all-logs:
#	${DC} -f ${APP_FILE} -f ${TODO_GRPC_SERVER} logs -f

#####

python -m grpc_tools.protoc -I ./protos --python_out=./protos --grpc_python_out=./protos todo.proto

python -m grpc_tools.protoc -I ./gateway/protos --python_out=./gateway/protos --grpc_python_out=./gateway/protos todo.proto
ORG semi org
&& python -m grpc_tools.protoc -I /gateway/protos --python_out=/gateway/protos --grpc_python_out=/gateway/protos todo.proto


python -m grpc_tools.protoc -I ../protos --python_out=../protos --grpc_python_out=../protos todo.proto