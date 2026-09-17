from uuid import uuid4

from src.modules.consultation.consultation import Consultation

# provide a nickname to start a new consultation and give it a unique ID
def start_consultation(consultations, nickname):
    consultation_id = str(uuid4())

    consultation = Consultation(
        consultation_id=consultation_id,
        nickname=nickname,
        status="active"
    )
    consultations[consultation_id] = consultation
    return consultation

#add a patient to the consultation
def add_patient(consultations, consultation_id, patient):
    consultation = get_consultation(consultations, consultation_id)
    if consultation is None:
        return None
    consultation.patient = patient
    return consultation

#add a message to the conversation
def add_message(consultations, consultation_id, message):
    consultation = get_consultation(consultations, consultation_id)
    if consultation is None:
        return None
    consultation.conversation.append(message)
    return consultation

#return the consultation details using the consultation ID
def get_consultation(consultations, consultation_id):
    return consultations.get(consultation_id)


#end the consultation and delete it
def end_consultation(consultations, consultation_id):
    if consultation_id not in consultations:
        return False
    del consultations[consultation_id]
    return True
