from typing import Literal

from pydantic import BaseModel
from pydantic import Field as PydanticField
from sqlmodel import Field, SQLModel

from src.modules.patient.patient import Patient


class ConversationMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class Consultation(BaseModel):
    consultation_id: str
    nickname: str
    status: str
    patient: Patient | None = None
    conversation: list[ConversationMessage] = PydanticField(default_factory=list)


class ConsultationDB(SQLModel, table=True):
    consultation_id: str = Field(primary_key=True)
    nickname: str
    status: str
    patient_id: int | None = Field(default=None, foreign_key="patientdb.patient_id")

class ConversationMessageDB(SQLModel, table=True):
    message_id: int | None = Field(default=None, primary_key=True)
    consultation_id: str = Field(foreign_key="consultationdb.consultation_id")
    role: str
    content: str