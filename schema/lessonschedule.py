from datetime import date
from pydantic import BaseModel

class CreateLessonschedule(BaseModel):
    name: str
    room: str
    teacher: str
    time: date
    duration: int
    status: str
    start_time: date
    access_time: date
    notes: str

class UpdateLessonschedule(BaseModel):
    name : str
    room : str
    teacher : str
    time : date
    duration : int
    status : str
    start_time : date
    access_time : date
    notes : str