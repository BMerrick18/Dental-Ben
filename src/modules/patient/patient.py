# class Patient:
#     def __init__(self, name, sex, dob, medical_conditions, medications, allergies):
#         self.name = name
#         self.sex = sex
#         self.dob = dob
#         self.medical_conditions = medical_conditions
#         self.medications = medications
#         self.allergies = allergies

from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Literal

from datetime import date 

class Patient(BaseModel):
    # first_name: str
    # last_name: str
    sex: Literal["male", "female", "unknown"]
    date_of_birth: date

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        if value < date(1900, 1, 1):
            raise ValueError("Date of birth cannot be before 1900")
        return value
    
    medical_conditions: list[str] = Field(default_factory=list)


    @field_validator("medical_conditions", mode="before")
    @classmethod
    def clean_medical_conditions(cls, value):
        if not value:
            return []
        return [item.strip() for item in value if item.strip()]

    medications: list[str] = Field(default_factory=list)
    allergies: list[str] = Field(default_factory=list)

    @field_validator("allergies", "medications", mode="before")
    @classmethod
    def clean_list_fields(cls, value):
        if not value:
            return []
        return [item.strip() for item in value if item.strip()]










# if __name__ == "__main__":
#     patient = Patient(
#         # first_name = "Ben",
#         # last_name = "Merrick",
#         sex = "male",
#         date_of_birth = date(2000, 2, 14),
#         medical_conditions = ["Asthma", "Diabetes"],
#         medications = ["Salbutamol", "Metformin"],
#         allergies = ["Peanuts", "Cats"]
#     )

#     print(patient.date_of_birth)
