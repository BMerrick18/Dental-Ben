from uuid import uuid4
from sqlmodel import select

from src.modules.consultation.consultation import(
    Consultation,
    ConsultationDB, 
    Conversation_message,
    Conversation_messageDB
)
from src.modules.patient.patient import Patient, PatientDB

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

#add a patient to the consultation
def add_patient(session, consultation_id, patient):
    #check if the consultation exists, if not return None
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None:
        return None

    db_patient = get_patient(session, consultation_id)
    if db_patient is None:
        #use the pydantic model to build the database model
        db_patient = PatientDB(
            consultation_id=consultation_id,
            sex=patient.sex,
            date_of_birth=patient.date_of_birth
        )
        session.add(db_patient)
    else:
        db_patient.sex = patient.sex
        db_patient.date_of_birth = patient.date_of_birth

    #commit the changes to the database
    session.commit()

    #return the consultation details
    return get_consultation(session, consultation_id)

#add a message to the conversation
def add_message(session, consultation_id, message):
    consultation = session.get(ConsultationDB, consultation_id)
    if consultation is None:
        return None
    
    db_message = Conversation_messageDB(
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
        Conversation_message(
            role=message.role,
            content=message.content
        )
        for message in messages_db
    ]

    patient = None
    if patient_db is not None:
        patient = Patient(
            sex=patient_db.sex,
            date_of_birth=patient_db.date_of_birth
        )

    return Consultation(
        consultation_id=consultation_db.consultation_id,
        nickname=consultation_db.nickname,
        status=consultation_db.status,
        patient=patient,
        conversation=conversation
    )

#return the messages of the conversation using the consultation ID
def get_messages(session, consultation_id):
    statement = select(Conversation_messageDB).where(Conversation_messageDB.consultation_id == consultation_id)
    return session.exec(statement).all()

#return the patient linked to the consultation ID
def get_patient(session, consultation_id):
    statement = select(PatientDB).where(PatientDB.consultation_id == consultation_id)
    return session.exec(statement).first()


#end the consultation and delete it
def end_consultation(consultations, consultation_id):
    if consultation_id not in consultations:
        return False
    del consultations[consultation_id]
    return True
