from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.books import router as task_router
from app.routes.users import router as user_router

app = FastAPI(title="My library")
app.include_router(task_router)
app.include_router(user_router)
app.mount('/static', StaticFiles(directory='static'))

@app.on_event('startup')
def on_startup():
    print("Server started.")


def on_shutdown():
    print("Bye bye!")
