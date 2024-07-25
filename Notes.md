uvicorn --factory api.app:create_fastapi_app --reload --host 0.0.0.0 --port 8000

[//]: # (python3 -m grpc_tools.protoc -I. --python_out=./grpc_compiled --grpc_python_out=./grpc_compiled image_transform.proto)
[//]: # (python3 -m grpc_tools.protoc -I ./protos --python_out=./protos --grpc_python_out=./protos todo.proto)
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./proto/todo.proto

python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. protos/todo.proto


router gets clinet via DI, sends grpc req to running grpc service, its handled returned, in router 
converted to json