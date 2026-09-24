from fastapi import APIRouter, Depends,HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Literal
from sqlmodel import Session

from src.services.consultation_services import (
    get_consultation, 
    add_message, 
    start_consultation,
    add_patient,
    end_consultation
)
from src.modules.patient.patient import Patient
from src.modules.consultation.consultation import Consultation, Conversation_message, ConsultationDB
from src.database.database import get_session

router = APIRouter()

consultations = {}

class StartConsultation(BaseModel):
    nickname: str = Field(min_length=1)


# Ask the start_consultation service to start a new consultation and give it a unique ID when a nickname is provided
@router.post("/consultation", response_model=Consultation)
def start_consultation_route(
    request: StartConsultation,
    session: Session = Depends(get_session)
):
    return start_consultation(session, request.nickname)


# Add a patient to the consultation
@router.post("/consultation/{consultation_id}/patient", response_model=Consultation)
def add_patient_route(
    #provide the consultation ID of the consulation to add the patient to
    consultation_id: str,
    #provide the patient details using the patient model which is validated by the Pydantic model
    patient: Patient,
    #provide the session to the database
    session: Session = Depends(get_session)
):
    #ask the add_patient service to add the patient to the consultation
    consultation = add_patient(session, consultation_id, patient)
    #if the consultation is not found, raise an error
    if consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    #return the consultation details
    return consultation

# Ask the add_message service to add a message to the conversation
@router.post("/consultation/{consultation_id}/message", response_model=Consultation)
def add_message_route(
    consultation_id: str, 
    message: Conversation_message,
    session: Session = Depends(get_session)
):
    consultation = add_message(session, consultation_id, message)
    if consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultation

# Ask the get_consultation service to get the consultation details using the consultation ID
@router.get("/consultation/{consultation_id}", response_model=Consultation)
def get_consultation_route(
    consultation_id: str,
    session: Session = Depends(get_session)
):
    consultation = get_consultation(session, consultation_id)
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

