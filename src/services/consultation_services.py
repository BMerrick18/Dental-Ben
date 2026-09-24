from uuid import uuid4
from sqlmodel import select

from src.modules.consultation.consultation import (
    Consultation,
    ConsultationDB,
    ConversationMessage,
    ConversationMessageDB,
)
from src.modules.patient.patient import (
    Patient,
    PatientDB,
    MedicalCondition,
    Medication,
    Allergy,
    MedicalConditionsDB,
    MedicationsDB,
    AllergiesDB,
    MedicalConditionsLinkDB,
    MedicationsLinkDB,
    AllergiesLinkDB,
)

# provide a nickname to start a new consultation and give it a unique ID
def start_consultation(session, nickname):
    consultation_id = str(uuid4())

    consultation = ConsultationDB(
        consultation_id=consultation_id,
        nickname=nickname,
        status="active"
    )

    session.add(consultation)
    session.commit()

    return get_consultation(session, consultation_id)

#get a record from the database, or if it doesnt exist, create it, add it to the database, and return it
def get_or_create_by_name(session, model, name):
    row = session.exec(select(model).where(model.name == name)).first()
    if row is None:
        row = model(name=name)
        session.add(row)
        session.flush()
    return row

#find the medical conditions, medications, and allergies in the database or create them if they dont exist
#then link them to the patient in the relationship table along with the notes
def attach_clinical_records(session, patient_id, patient):
    seen_condition_ids = set()
    for condition in patient.medical_conditions:
        row = get_or_create_by_name(session, MedicalConditionsDB, condition.name)
        if row.medical_condition_id in seen_condition_ids:
            continue
        seen_condition_ids.add(row.medical_condition_id)
        session.add(MedicalConditionsLinkDB(
            patient_id=patient_id,
            medical_condition_id=row.medical_condition_id,
            notes=condition.notes,
        ))

    seen_medication_ids = set()
    for medication in patient.medications:
        row = get_or_create_by_name(session, MedicationsDB, medication.name)
        if row.medication_id in seen_medication_ids:
            continue
        seen_medication_ids.add(row.medication_id)
        session.add(MedicationsLinkDB(
            patient_id=patient_id,
            medication_id=row.medication_id,
            notes=medication.notes,
        ))

    seen_allergy_ids = set()
    for allergy in patient.allergies:
        row = get_or_create_by_name(session, AllergiesDB, allergy.name)
        if row.allergy_id in seen_allergy_ids:
            continue
        seen_allergy_ids.add(row.allergy_id)
        session.add(AllergiesLinkDB(
            patient_id=patient_id,
            allergy_id=row.allergy_id,
            notes=allergy.notes,
        ))

#convert the database patient to a pydantic patient
def patient_from_db(patient_db):
    return Patient(
        sex=patient_db.sex,
        date_of_birth=patient_db.date_of_birth,
        medical_conditions=[
            MedicalCondition(name=link.condition.name, notes=link.notes)
            for link in patient_db.condition_links
        ],
        medications=[
            Medication(name=link.medication.name, notes=link.notes)
            for link in patient_db.medication_links
        ],
        allergies=[
            Allergy(name=link.allergy.name, notes=link.notes)
            for link in patient_db.allergy_links
        ],
    )


#add a patient to the consultation
def add_patient(session, consultation_id, patient):
    #check if the consultation exists, if not return None
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None:
        return None

    db_patient = get_patient(session, consultation_id)
    if db_patient is not None:
        raise ValueError("Patient already exists on this consultation")

    db_patient = PatientDB(
        sex=patient.sex,
        date_of_birth=patient.date_of_birth
    )
    session.add(db_patient)
    session.flush()
    attach_clinical_records(session, db_patient.patient_id, patient)
    consultation.patient_id = db_patient.patient_id

    #commit the changes to the database
    session.commit()

    #return the consultation details
    return get_consultation(session, consultation_id)

#add a message to the conversation
def add_message(session, consultation_id, message):
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None:
        return None
    
    db_message = ConversationMessageDB(
        consultation_id=consultation_id,
        role=message.role,
        content=message.content
    )

    session.add(db_message)
    session.commit()

    return get_consultation(session, consultation_id)

#return the consultation details using the consultation ID
def get_consultation(session, consultation_id):
    consultation_db = session.get(ConsultationDB, consultation_id)

    if consultation_db is None:
        return None
    
    messages_db = get_messages(session, consultation_id)
    patient_db = get_patient(session, consultation_id)

    conversation = [
        ConversationMessage(
            role=message.role,
            content=message.content
        )
        for message in messages_db
    ]

    patient = None
    if patient_db is not None:
        patient = patient_from_db(patient_db)

    return Consultation(
        consultation_id=consultation_db.consultation_id,
        nickname=consultation_db.nickname,
        status=consultation_db.status,
        patient=patient,
        conversation=conversation
    )

#return the messages of the conversation using the consultation ID
def get_messages(session, consultation_id):
    statement = select(ConversationMessageDB).where(ConversationMessageDB.consultation_id == consultation_id)
    return session.exec(statement).all()

#return the patient linked to the consultation ID
def get_patient(session, consultation_id):
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None or consultation.patient_id is None:
        return None
    return session.get(PatientDB, consultation.patient_id)


#end the consultation and delete it, along with its messages
def end_consultation(session, consultation_id):
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None:
        return False

    messages = get_messages(session, consultation_id)
    for message in messages:
        session.delete(message)
    session.flush()

    session.delete(consultation)
    session.commit()
    return True
