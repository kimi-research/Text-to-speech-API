from pydantic import BaseModel

# schema for REQUEST
class InputData(BaseModel):
    text: str  # Receives text as input

