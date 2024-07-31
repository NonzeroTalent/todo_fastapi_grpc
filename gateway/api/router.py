from fastapi import APIRouter
from gateway.api.routes.todo_router import todo_router


app_router = APIRouter()

app_router.include_router(todo_router, tags=["Todo list"], prefix="/todo")
