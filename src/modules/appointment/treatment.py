

# class Treatment:
#     def __init__(self):
#         self.options_discussed = []
#         self.selected_option = None

from pydantic import BaseModel, Field, ValidationError

class Treatment(BaseModel):
    options_discussed: list[str] = Field(default_factory=list)
    selected_option: str | None = None