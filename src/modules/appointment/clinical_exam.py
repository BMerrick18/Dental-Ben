from pydantic import BaseModel, Field, ValidationError

# class Extra_oral:
#     def __init__(self, lymph_nodes, salivary_glands, submandibular_zone, neck, tmj):
#         self.lymph_nodes: lymph_nodes
#         self.salivary_glands: salivary_glands
#         self.submandibular_zone: submandibular_zone
#         self.neck: neck
#         self.tmj: tmj

class Extra_oral(BaseModel):
    lymph_nodes: str | None = None
    salivary_glands: str | None = None
    submandibular_zone: str | None = None
    neck: str | None = None
    tmj: str | None = None
    
# class Intra_oral_st:
#     def __init__(self, palate, cheeks, lips, tongue, gingiva, floor_of_mouth):
#         self.palate: palate
#         self.cheeks: cheeks
#         self.lips: lips
#         self.tongue: tongue
#         self.gingiva: gingiva
#         self.floor_of_mouth: floor_of_mouth

class Intra_oral_st(BaseModel):
    palate: str | None = None
    cheeks: str | None = None
    lips: str | None = None
    tongue: str | None = None
    gingiva: str | None = None
    floor_of_mouth: str | None = None

# class Intra_oral_ht:
#     def __init__(self, caries, retained_roots, fractures, recurrent_caries):
#         self.caries: caries
#         self.retained_roots: retained_roots
#         self.fractures: fractures
#         self.recurrent_caries: recurrent_caries

class Intra_oral_ht(BaseModel):
    caries: list[str] = Field(default_factory=list)
    retained_roots: list[str] = Field(default_factory=list)
    fractures: list[str] = Field(default_factory=list)
    recurrent_caries: list[str] = Field(default_factory=list)

# class Special_tests:
#     def __init__(self, ttp, endofrost):
#         self.ttp: ttp
#         self.endofrost: endofrost

class Special_tests(BaseModel):
    ttp: list[str] = Field(default_factory=list)
    endofrost: list[str] = Field(default_factory=list)



