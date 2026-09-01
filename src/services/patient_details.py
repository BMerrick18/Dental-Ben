from src.modules.patient.patient import Patient
from src.services.input_service import InputService
from src.database.database import save_patient, save_medical_condition, save_medication, save_allergy, link_patient_medical_condition, link_patient_medication, link_patient_allergy

def add_patient():
    input_service = InputService()

    first_name = input_service.get_name("First Name: ")
    last_name = input_service.get_name("Last Name: ")
    gender = input_service.get_text("Gender: ")
    date_of_birth = input_service.get_text("Date of birth (YYYY-MM-DD): ")

    medical_conditions = input_service.comma_separated_to_list("Medical conditions (comma-separated list): ")
    medications = input_service.comma_separated_to_list("Medications (comma-separated list): ")
    allergies = input_service.comma_separated_to_list("Allergies (comma-separated list): ")

    return Patient(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date_of_birth,
        medical_conditions=medical_conditions,
        medications=medications,
        allergies=allergies,
    )


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
