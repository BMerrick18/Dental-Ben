from pydantic import BaseModel, Field
from typing import Literal
from sqlmodel import Field, SQLModel

from src.modules.patient.patient import Patient

class Conversation_message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class Consultation(BaseModel):
    consultation_id: str
    nickname: str
    status: str
    patient: Patient | None = None
    conversation: list[Conversation_message] = Field(default_factory=list)


class ConsultationDB(SQLModel, table=True):
    consultation_id: str = Field(primary_key=True)
    nickname: str
    status: str

class Conversation_messageDB(SQLModel, table=True):
    message_id: int | None = Field(default=None, primary_key=True)
    consultation_id: str
    role: str
    content: str