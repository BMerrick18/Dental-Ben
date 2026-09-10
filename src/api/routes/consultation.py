from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from src.modules.patient.patient import Patient
from src.modules.consultation.consultation import Consultation

router = APIRouter()

consultations = {}

class StartConsultation(BaseModel):
    nickname: str

@router.post("/consultation", response_model=Consultation)
def start_consultation(consultation: StartConsultation):
    consultation_id = str(uuid4())
    consultations[consultation_id] = Consultation(
        consultation_id=consultation_id,
        nickname=consultation.nickname,
        status="active"
    )
    return consultations[consultation_id]

@router.post("/consultation/{consultation_id}/patient", response_model=Consultation)
def add_patient(consultation_id: str, patient: Patient):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    consultations[consultation_id].patient = patient
    return consultations[consultation_id]   

@router.get("/consultation/{consultation_id}", response_model=Consultation)
def get_consultation(consultation_id: str):
    if consultation_id not in consultations:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return consultations[consultation_id]

