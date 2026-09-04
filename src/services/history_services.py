from src.services.input_service import InputService
from src.modules.appointment.emergency_history import Socrates_history

def add_socrates_history():
    input_service = InputService()

    presenting_complaint = input_service.get_text("Presenting complaint: ")
    site = input_service.get_text("Site: ")
    onset = input_service.get_text("Onset: ")
    character = input_service.get_text("Character: ")
    radiation = input_service.get_text("Radiation: ")
    associations = input_service.get_text("Associations: ")
    timing = input_service.get_text("Timing: ")
    alleviation = input_service.get_text("Alleviation: ")
    exacerbation = input_service.get_text("Exacerbation: ")
    sleep = input_service.get_text("Sleep: ")
    severity = input_service.get_float("Severity (0-10, blank to skip): ", min_value=0, max_value=10)

    return Socrates_history(
        presenting_complaint=presenting_complaint,
        site=site,
        onset=onset,
        character=character,
        radiation=radiation,
        associations=associations,
        timing=timing,
        alleviation=alleviation,
        exacerbation=exacerbation,
        sleep=sleep,
        severity=severity)

if __name__ == "__main__":
    test_socrates_history = add_socrates_history()
    print(test_socrates_history.presenting_complaint, test_socrates_history.site, test_socrates_history.onset, test_socrates_history.character, test_socrates_history.radiation, test_socrates_history.associations, test_socrates_history.timing, test_socrates_history.alleviation, test_socrates_history.exacerbation, test_socrates_history.sleep, test_socrates_history.severity)
