import grpc
from protos import todo_pb2
from typing import Any, List
from grpc.aio._call import AioRpcError
from fastapi.responses import JSONResponse
from google.protobuf.json_format import MessageToDict
from grpc_clients.todo_client import get_gprc_todo_client
from fastapi import APIRouter, Depends, status, HTTPException


todo_router = APIRouter()


@todo_router.get("/")
async def ping():
    return {"nigg": "er"}


@todo_router.post("/todo")
async def create_todo(
        name: str,
        completed: bool,
        day: int,
        client: Any = Depends(get_gprc_todo_client)
) -> JSONResponse:
    try:
        todo = await client.create_todo_item(
            todo_pb2.CreateTodoRequest(
                name=name,
                completed=completed,
                day=day
            ), timeout=5
        )
    except AioRpcError as err:
        raise HTTPException(status_code=404, detail=err.details())
    return JSONResponse(MessageToDict(todo))


@todo_router.get("/todos")
async def list_todos(client: Any = Depends(get_gprc_todo_client)):
    try:
        todos = await client.list_todo_items(todo_pb2.ListTodosRequest(), timeout=5)
    except AioRpcError as err:
        raise HTTPException(status_code=404, detail=err.details())
    return JSONResponse(MessageToDict(todos))

@todo_router.get("/todo")
async def get_todo(
        id: int,
        client: Any = Depends(get_gprc_todo_client)):
    try:
        todos = await client.get_todo_item(todo_pb2.GetTodoRequest(id=id), timeout=5)
    except AioRpcError as err:
        raise HTTPException(status_code=404, detail=err.details())
    return JSONResponse(MessageToDict(todos))

@todo_router.delete("/todo")
async def delete_todo(
        id: int,
        client: Any = Depends(get_gprc_todo_client)):
    try:
        todos = await client.delete_todo_item(todo_pb2.DeleteTodoRequest(id=id), timeout=5)
    except AioRpcError as err:
        raise HTTPException(status_code=404, detail=err.details())
    return JSONResponse(MessageToDict(todos))

@todo_router.put("/todo")
async def update_todo(
        id: int,
        name: str,
        completed: bool,
        day: int,
        client: Any = Depends(get_gprc_todo_client)):
    try:
        todos = await client.update_todo_item(todo_pb2.UpdateTodoRequest(id=id,
                                                                         name=name,
                                                                         completed=completed,
                                                                         day=day), timeout=5)
    except AioRpcError as err:
        print(f"ERR, {err}")
        raise HTTPException(status_code=404, detail=err.details())
    return JSONResponse(MessageToDict(todos))
