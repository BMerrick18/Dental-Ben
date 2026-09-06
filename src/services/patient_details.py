from datetime import datetime

from src.modules.patient.patient import Patient
from src.services.input_service import InputService
from src.database.database import save_patient, save_medical_condition, save_medication, save_allergy, link_patient_medical_condition, link_patient_medication, link_patient_allergy

input_service = InputService()

def get_first_name():
    return input_service.get_name("First Name: ")

def get_last_name():
    return input_service.get_name("Last Name: ")

def get_sex():
    return input_service.get_text("Sex at birth (M/F): ")

#validate the sex input and return the sex in lower case or None
def validate_sex(sex):
    if sex in ["m", "male"]:
        return "male"
    
    elif sex in ["f", "female"]:
        return "female"

    else:
        return None

#get the sex input and validate it, if invalid, ask again
def get_validated_sex():
    while True:
        sex = get_sex()
        validated_sex = validate_sex(sex)

        if validated_sex is not None:
            return validated_sex

        print("Invalid sex at birth. Please enter M or F.")

def get_date_of_birth():
    return input_service.get_text("Date of birth (YYYY-MM-DD): ")

#validate the date of birth input and return the date of birth or None
def validate_date_of_birth(date_of_birth):
    try:
        return datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        return None

#get the date of birth input and validate it, if invalid, ask again
def get_validated_date_of_birth():
    while True:
        date_of_birth = get_date_of_birth()
        validated_date_of_birth = validate_date_of_birth(date_of_birth)
   
        if validated_date_of_birth is not None:
            return validated_date_of_birth
        
        print("Invalid date. Please enter the date in the format YYYY-MM-DD.")

def get_medical_conditions():
    return input_service.comma_separated_to_list("Medical conditions (comma-separated list): ")

def get_medications():
    return input_service.comma_separated_to_list("Medications (comma-separated list): ")

def get_allergies():
    return input_service.comma_separated_to_list("Allergies (comma-separated list): ")

#get the patient details and return a Patient object
def add_patient():
    input_service = InputService()

    first_name = get_first_name()
    last_name = get_last_name()
    sex = get_validated_sex()
    date_of_birth = get_validated_date_of_birth()
    medical_conditions = get_medical_conditions()
    medications = get_medications()
    allergies = get_allergies()

    return Patient(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        date_of_birth=date_of_birth,
        medical_conditions=medical_conditions,
        medications=medications,
        allergies=allergies,
    )

#save the patient details to the database and return the patient id
def save_patient_details(patient):
    patient_id = save_patient(patient)

    for condition in patient.medical_conditions:
        condition_id = save_medical_condition(condition)
        link_patient_medical_condition(patient_id, condition_id)

    for medication in patient.medications:
        medication_id = save_medication(medication)
        link_patient_medication(patient_id, medication_id)

    for allergy in patient.allergies:
        allergy_id = save_allergy(allergy)
        link_patient_allergy(patient_id, allergy_id)

    return patient_id


if __name__ == "__main__":
    test_patient = add_patient()
    print(test_patient.first_name, test_patient.medical_conditions, test_patient.date_of_birth)
