
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import event

from src.modules.consultation.consultation import (
    ConsultationDB, 
    Conversation_messageDB
)

from src.modules.patient.patient import PatientDB

DATABASE_URL = "sqlite:///dental_ben.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
