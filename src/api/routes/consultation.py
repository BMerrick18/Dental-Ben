from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Literal

from src.modules.patient.patient import Patient
from src.modules.consultation.consultation import Consultation, Conversation_message

router = APIRouter()

consultations = {}

class StartConsultation(BaseModel):
    nickname: str = Field(min_length=1)


# Enter a nickname to start a new consultation and give it a unique ID
@router.post("/consultation", response_model=Consultation)
def start_consultation(consultation: StartConsultation):
    consultation_id = str(uuid4())
    consultations[consultation_id] = Consultation(
        consultation_id=consultation_id,
        nickname=consultation.nickname,
        status="active"
    )
    return consultations[consultation_id]

# Add a patient to the consultation
@router.post("/consultation/{consultation_id}/patient", response_model=Consultation)
def add_patient(consultation_id: str, patient: Patient):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    consultations[consultation_id].patient = patient
    return consultations[consultation_id]   

# Add a message to the conversation
@router.post("/consultation/{consultation_id}/message", response_model=Consultation)
def add_message(consultation_id: str, message: Conversation_message):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    consultations[consultation_id].conversation.append(message)
    return consultations[consultation_id]

# Get the consultation details using the consultation ID
@router.get("/consultation/{consultation_id}", response_model=Consultation)
def get_consultation(consultation_id: str):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultations[consultation_id]

# End the consultation and delete it from the consultations dictionary
@router.delete("/consultation/{consultation_id}")
def end_consultation(consultation_id: str):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    del consultations[consultation_id]
    return {"status": "Consultation ended successfully and deleted"}

