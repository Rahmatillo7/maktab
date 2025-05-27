from pydantic import BaseModel

class CreateAbout(BaseModel):
    text : str
    fan_id : int

class UpdateAbout(BaseModel):
    text : str
    fan_id : int