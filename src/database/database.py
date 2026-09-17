
from sqlmodel import SQLModel, Session, create_engine

from src.modules.consultation.consultation import ConsultationDB

print("Database is running")

DATABASE_URL = "sqlite:///dental_ben.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
