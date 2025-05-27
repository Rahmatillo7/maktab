from pydantic import BaseModel

class CreateNews(BaseModel):
    text : str

class UpdateNews(BaseModel):
    text : str