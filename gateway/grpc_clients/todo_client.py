import os
import sys
import grpc


# from gateway.protos import todo_pb2_grpc
# from gateway.common import settings

sys.path.append("/app/gateway")
from protos import todo_pb2_grpc



async def get_gprc_todo_client():
    channel = grpc.aio.insecure_channel(os.getenv('TODO_GRPC_SERVER_ADDRESS'))
    return todo_pb2_grpc.TodoServiceStub(channel)