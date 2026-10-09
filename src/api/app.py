from fastapi import FastAPI

from src.api.routes import consultation, health

app = FastAPI(title="Dental-Ben")

app.include_router(health.router)
app.include_router(consultation.router)