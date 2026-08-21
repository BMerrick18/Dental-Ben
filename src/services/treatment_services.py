from src.services.input_service import InputService
from src.modules.appointment.treatment import Treatment

def add_treatment():
    input_service = InputService()

    options_discussed = input_service.comma_separated_to_list("Options discussed (comma-separated list): ")
    selected_option = input_service.get_text("Selected option: ")

    return Treatment(
        options_discussed=options_discussed,
        selected_option=selected_option)

if __name__ == "__main__":
    test_treatment = add_treatment()
    print(test_treatment.options_discussed, test_treatment.selected_option)

