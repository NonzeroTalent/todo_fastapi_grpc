from fastapi import FastAPI
from gateway.api.router import app_router

def create_fastapi_app():
    app = FastAPI(
        title="TODO Router",
        debug=True,
    )
    app.include_router(router=app_router)
    return app

