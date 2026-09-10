from pydantic import BaseModel
from src.modules.patient.patient import Patient

class Consultation(BaseModel):
    consultation_id: str
    nickname: str
    status: str
    patient: Patient | None = None