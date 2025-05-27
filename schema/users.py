from pydantic import BaseModel, EmailStr


class CreateUsers(BaseModel):
    name : str
    username : str
    password : str
    address : str
    number : int
    email : EmailStr

class UpdateUsers(BaseModel):
    name : str
    username : str
    password : str
    address : str
    number : int
    email : EmailStr