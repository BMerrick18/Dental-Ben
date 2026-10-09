from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, field_validator
from sqlmodel import Field as SQLField
from sqlmodel import Relationship, SQLModel


#convert blank notes in the medical conditions, medications, and allergies to None
def blank_notes_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


class MedicalCondition(BaseModel):
    name: str
    notes: str | None = None

    @field_validator("notes", mode="before")
    @classmethod
    def empty_notes_are_null(cls, value):
        return blank_notes_to_none(value)


class Medication(BaseModel):
    name: str
    notes: str | None = None

    @field_validator("notes", mode="before")
    @classmethod
    def empty_notes_are_null(cls, value):
        return blank_notes_to_none(value)


class Allergy(BaseModel):
    name: str
    notes: str | None = None

    @field_validator("notes", mode="before")
    @classmethod
    def empty_notes_are_null(cls, value):
        return blank_notes_to_none(value)


class Patient(BaseModel):
    # first_name: str
    # last_name: str
    sex: Literal["male", "female", "unknown"]
    date_of_birth: date
    medical_conditions: list[MedicalCondition] = Field(default_factory=list)
    medications: list[Medication] = Field(default_factory=list)
    allergies: list[Allergy] = Field(default_factory=list)

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        if value < date(1900, 1, 1):
            raise ValueError("Date of birth cannot be before 1900")
        return value

    @field_validator("medical_conditions", "medications", "allergies", mode="before")
    @classmethod
    def clean_clinical_lists(cls, value):
        if not value:
            return []

        cleaned = []
        for item in value:
            if isinstance(item, str):
                name = item.strip()
                if name:
                    cleaned.append({"name": name})
            elif isinstance(item, dict):
                name = str(item.get("name", "")).strip()
                if name:
                    cleaned.append({**item, "name": name})
            else:
                cleaned.append(item)
        return cleaned


class PatientDB(SQLModel, table=True):
    patient_id: int | None = SQLField(default=None, primary_key=True)
    sex: str
    date_of_birth: date
    condition_links: list["MedicalConditionsLinkDB"] = Relationship(
        back_populates="patient"
    )
    medication_links: list["MedicationsLinkDB"] = Relationship(back_populates="patient")
    allergy_links: list["AllergiesLinkDB"] = Relationship(back_populates="patient")


class MedicalConditionsDB(SQLModel, table=True):
    medical_condition_id: int | None = SQLField(default=None, primary_key=True)
    name: str
    patient_links: list["MedicalConditionsLinkDB"] = Relationship(
        back_populates="condition"
    )


class MedicalConditionsLinkDB(SQLModel, table=True):
    patient_id: int = SQLField(foreign_key="patientdb.patient_id", primary_key=True)
    medical_condition_id: int = SQLField(
        foreign_key="medicalconditionsdb.medical_condition_id",
        primary_key=True,
    )
    notes: str | None = None
    patient: PatientDB = Relationship(back_populates="condition_links")
    condition: MedicalConditionsDB = Relationship(back_populates="patient_links")


class MedicationsDB(SQLModel, table=True):
    medication_id: int | None = SQLField(default=None, primary_key=True)
    name: str
    patient_links: list["MedicationsLinkDB"] = Relationship(back_populates="medication")


class MedicationsLinkDB(SQLModel, table=True):
    patient_id: int = SQLField(foreign_key="patientdb.patient_id", primary_key=True)
    medication_id: int = SQLField(
        foreign_key="medicationsdb.medication_id",
        primary_key=True,
    )
    notes: str | None = None
    patient: PatientDB = Relationship(back_populates="medication_links")
    medication: MedicationsDB = Relationship(back_populates="patient_links")


class AllergiesDB(SQLModel, table=True):
    allergy_id: int | None = SQLField(default=None, primary_key=True)
    name: str
    patient_links: list["AllergiesLinkDB"] = Relationship(back_populates="allergy")


class AllergiesLinkDB(SQLModel, table=True):
    patient_id: int = SQLField(foreign_key="patientdb.patient_id", primary_key=True)
    allergy_id: int = SQLField(foreign_key="allergiesdb.allergy_id", primary_key=True)
    notes: str | None = None
    patient: PatientDB = Relationship(back_populates="allergy_links")
    allergy: AllergiesDB = Relationship(back_populates="patient_links")
