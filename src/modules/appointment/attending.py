# class Attending:
#     def __init__(self, clinician, nurse=None, companions=None):
#         self.clinician = clinician
#         self.nurse = nurse
#         self.companions = companions

from pydantic import BaseModel, Field, ValidationError

class Attending(BaseModel):
    clinician: str
    nurse: str | None = None
    companions: list[str] = Field(default_factory=list)


if __name__ == "__main__":
    attending = Attending(
        clinician = "Ben",
        nurse = "Daisy",
        companions = ["Partner", "Daughter"]
    )

    print(attending.nurse, attending.companions)