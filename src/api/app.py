from fastapi import FastAPI
from src.modules.patient.patient import Patient
from src.services.patient_details import save_patient_details
from src.database.database import retrieve_patient_by_id

app = FastAPI(title="Dental-Ben")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/patient")
def create_patient(patient: Patient):
    patient_id = save_patient_details(patient)
    return {"patient_id": patient_id}

@app.get("/patient/{patient_id}")
def get_patient_details(patient_id: int):
    patient = retrieve_patient_by_id(patient_id)
    return patient
