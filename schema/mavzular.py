from pydantic import BaseModel

class CreateMavzular(BaseModel):
    name : str
    fan_id : int
    text : str


class UpdateMavzular(BaseModel):
    name : str
    fan_id : int
    text : str