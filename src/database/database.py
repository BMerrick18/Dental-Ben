
from sqlalchemy import event
from sqlmodel import Session, SQLModel, create_engine

from src.modules.consultation.consultation import (
    ConsultationDB,
    ConversationMessageDB,
)
from src.modules.patient.patient import (
    AllergiesDB,
    AllergiesLinkDB,
    MedicalConditionsDB,
    MedicalConditionsLinkDB,
    MedicationsDB,
    MedicationsLinkDB,
    PatientDB,
)

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
    with Session(engine) as session:
        yield session
