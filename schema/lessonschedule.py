from pydantic import BaseModel

class CreateLessonschedule(BaseModel):
    name: str
    room: str
    teacher: str
    status: str
    day_name: str
    lesson_date: str
    start_time: str


class UpdateLessonschedule(BaseModel):
    name : str
    room : str
    teacher : str
    status : str
    day_name: str
    lesson_date: str
    start_time: str