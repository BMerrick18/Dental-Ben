from src.services.input_service import InputService
from src.modules.appointment.radiographs import Radiographs

def add_radiographs():
    input_service = InputService()

    view = input_service.get_text("View: ")
    site = input_service.get_text("Site: ")
    justification = input_service.get_text("Justification: ")
    grade = input_service.get_text("Grade: ")
    report = input_service.get_text("Report: ")

    return Radiographs(
        view=view,
        site=site,
        justification=justification,
        grade=grade,
        report=report)

if __name__ == "__main__":
    test_radiographs = add_radiographs()
    print(test_radiographs.view, test_radiographs.site, test_radiographs.justification, test_radiographs.grade, test_radiographs.report)