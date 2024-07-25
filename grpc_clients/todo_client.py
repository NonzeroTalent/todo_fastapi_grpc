import grpc
from protos import todo_pb2_grpc
from fastapi import Request
from common import settings

async def get_gprc_todo_client():
    channel = grpc.aio.insecure_channel(settings.TODO_GRPC_SERVER_ADDRESS)
    return todo_pb2_grpc.TodoServiceStub(channel)