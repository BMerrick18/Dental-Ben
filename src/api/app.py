from fastapi import FastAPI
from src.api.routes import health, consultation
from src.database import database

app = FastAPI(title="Dental-Ben")

app.include_router(health.router)
app.include_router(consultation.router)