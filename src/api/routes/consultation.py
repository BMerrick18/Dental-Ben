from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Literal

from src.services.consultation_services import (
    get_consultation, 
    add_message, 
    start_consultation,
    add_patient,
    end_consultation
)
from src.modules.patient.patient import Patient
from src.modules.consultation.consultation import Consultation, Conversation_message

router = APIRouter()

consultations = {}

class StartConsultation(BaseModel):
    nickname: str = Field(min_length=1)


# Ask the start_consultation service to start a new consultation and give it a unique ID when a nickname is provided
@router.post("/consultation", response_model=Consultation)
def start_consultation_route(request: StartConsultation):
    return start_consultation(consultations, request.nickname)

# Add a patient to the consultation
@router.post("/consultation/{consultation_id}/patient", response_model=Consultation)
def add_patient_route(consultation_id: str, patient: Patient):
    consultation = add_patient(consultations, consultation_id, patient)
    if consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultation

# Ask the add_message service to add a message to the conversation
@router.post("/consultation/{consultation_id}/message", response_model=Consultation)
def add_message_route(consultation_id: str, message: Conversation_message):
    consultation = add_message(consultations, consultation_id, message)
    if consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultation

# Ask the get_consultation service to get the consultation details using the consultation ID
@router.get("/consultation/{consultation_id}", response_model=Consultation)
def get_consultation_route(consultation_id: str):
    consultation = get_consultation(consultations, consultation_id)
    if consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultation

# End the consultation and delete it from the consultations dictionary
@router.delete("/consultation/{consultation_id}")
def end_consultation_route(consultation_id: str):
    ended = end_consultation(consultations, consultation_id)
    if not ended:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return {"status": "Consultation successfully ended and deleted"}

