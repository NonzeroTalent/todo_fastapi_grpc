import os
import asyncio
from todo_service.services.todo import run_todo_service
# from common.settings import TODO_GRPC_SERVER_ADDRESS

# import sys
# sys.path.append("/app")



if __name__ == "__main__":
    asyncio.run(run_todo_service(os.getenv('TODO_GRPC_SERVER_ADDRESS')))
    # asyncio.run(run_todo_service("0.0.0.0:50050"))