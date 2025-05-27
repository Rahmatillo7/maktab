from pydantic import BaseModel


class CreateFanlar(BaseModel):
    nomi : str


class UpdateFanlar(BaseModel):
    nomi : str
