# class Radiographs:
#     def __init__(self, view, site, justification, grade, report):
#         self.view = view
#         self.site = site
#         self.justification = justification
#         self.grade = grade
#         self.report = report

from pydantic import BaseModel, Field

class Radiographs(BaseModel):
    view: str | None = None
    site: str | None = None
    justification: str | None = None
    grade: str | None = None
    report: str | None = None