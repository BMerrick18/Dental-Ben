from src.services.input_service import InputService
from src.modules.appointment.attending import Attending

def people_present():
    input_service = InputService()

    clinician = input_service.get_name("Clinician: ")
    nurse = input_service.get_name("Nurse: ")
    companions = input_service.comma_separated_to_list("Companions (comma-separated list): ")

    return Attending(
        clinician=clinician,
        nurse=nurse,
        companions=companions,
    )


if __name__ == "__main__":
    test_attending_details = people_present()
    print(test_attending_details.nurse, test_attending_details.companions)