# class Patient:
#     def __init__(self, name, gender, dob, medical_conditions, medications, allergies):
#         self.name = name
#         self.gender = gender
#         self.dob = dob
#         self.medical_conditions = medical_conditions
#         self.medications = medications
#         self.allergies = allergies

from pydantic import BaseModel, Field, ValidationError

from datetime import date 

class Patient(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    medical_conditions: list[str] = Field(default_factory=list)
    medications: list[str] = Field(default_factory=list)
    allergies: list[str] = Field(default_factory=list)

if __name__ == "__main__":
    patient = Patient(
        first_name = "Ben",
        last_name = "Merrick",
        gender = "male",
        date_of_birth = date(2000, 2, 14),
        medical_conditions = ["Asthma", "Diabetes"],
        medications = ["Salbutamol", "Metformin"],
        allergies = ["Peanuts", "Cats"]
    )

    print(patient.first_name, patient.date_of_birth)
