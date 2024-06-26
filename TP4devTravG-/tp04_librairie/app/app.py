from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.books import router as task_router
from app.routes.users import router as user_router
from app.database import create_database

app = FastAPI(title="My library")
app.include_router(task_router)
app.include_router(user_router)
app.mount('/static', StaticFiles(directory='static'))

@app.on_event('startup')
def on_startup():
    print("Server started.")

@app.on_event("startup")
def on_application_started():
    create_database()


def on_shutdown():
    print("Bye bye!")
