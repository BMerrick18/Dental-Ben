# class :
#     presenting_complaint

#     def __init__(self, presenting_complaint, socrates):
#         self.presenting_complaint = presenting_complaint
#         self.socrates = {
#             "site": None,
#             "onset": None,
#             "character": None,
#             "radiation": None,
#             "associations": None,
#             "timing": None,
#             "alleviation": None,
#             "exacerbation": None,
#             "sleep": None,
#             "severity": None
#         }

from pydantic import BaseModel, Field, ValidationError

class Socrates_history(BaseModel):
    presenting_complaint: str | None = None
    site: str | None = None
    onset: str | None = None
    character: str | None = None
    radiation: str | None = None
    associations: str | None = None
    timing: str | None = None
    alleviation: str | None = None
    exacerbation: str | None = None
    sleep: str | None = None
    severity: float | None = Field(default=None, ge=0, le=10)