import logging
from services.todo import run_todo_service
import asyncio
from common.settings import TODO_GRPC_SERVER_ADDRESS


if __name__ == "__main__":
    asyncio.run(run_todo_service(TODO_GRPC_SERVER_ADDRESS))