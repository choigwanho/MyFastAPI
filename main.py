from fastapi import FastAPI
from api import api_get,api_post

def include_router(app):
    app.include_router(api_get.router, prefix='/main')
    app.include_router(api_post.router, prefix='/main')

def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()
