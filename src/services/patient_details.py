from modules.patient.patient import Patient
from services.input_service import InputService

def add_patient():
    input_service = InputService()

    first_name = input_service.get_name("First Name: ")
    second_name = input_service.get_name("Second Name: ")
    gender = input_service.get_text("Gender ")
    dob = input_service.get_text("Date of birth (YYYY-MM-DD): ")

    medical_conditions = input_service.comma_separated_to_list("Medical conditions (comma-separated list): ")
    medications = input_service.comma_separated_to_list("Medications (comma-separated list): ")
    allergies = input_service.comma_separated_to_list("Allergies (comma-separated list): ")

    return Patient(
        first_name=first_name,
        second_name=second_name,
        gender=gender,
        dob=dob,
        medical_conditions=medical_conditions,
        medications=medications,
        allergies=allergies,
    )

if __name__ == "__main__":
    test_patient = add_patient()
    print(test_patient.first_name, test_patient.medical_conditions, test_patient.dob)
