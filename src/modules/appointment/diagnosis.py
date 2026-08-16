# class Diagnosis:
#     def __init__(self, tooth, coronal_diagnosis, pulp_diagnosis, apical_diagnosis):
#         self.tooth = tooth
#         self.coronal_diagnosis = coronal_diagnosis
#         self.pulp_diagnosis = pulp_diagnosis
#         self.apical_diagnosis = apical_diagnosis

from pydantic import BaseModel, Field, ValidationError

class Diagnosis(BaseModel):
    tooth: str
    coronal_diagnosis: str
    pulp_diagnosis: str
    apical_diagnosis: str
