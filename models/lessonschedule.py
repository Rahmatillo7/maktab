from sqlalchemy import Column, Integer, String
from db import Base

class Lessonschedule(Base):

    __tablename__ = "lessonschedule"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    room = Column(String(255), nullable=False)
    teacher = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    start_time = Column(String(20), nullable=False)
    day_name = Column(String(20), nullable=False)
    lesson_date = Column(String(30), nullable=False)