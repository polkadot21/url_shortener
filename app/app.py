from fastapi import FastAPI

from app.db.urls import init_db
from app.routers import shortener, health

app = FastAPI()

app.include_router(health.router)
app.include_router(shortener.router)


@app.on_event("startup")
def startup_event():
    init_db()
