from fastapi import FastAPI
from api.router import todo_router

def create_fastapi_app():
    app = FastAPI(
        title="TODO Router",
        debug=True,
    )
    app.include_router(router=todo_router)
    return app

