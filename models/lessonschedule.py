from sqlalchemy import Column, Integer, String, Date
from db import Base

class Lessonschedule(Base):

    __tablename__ = "lessonschedule"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    room = Column(String(255), nullable=False)
    teacher = Column(String(255), nullable=False)
    time = Column(Date, nullable=False)
    start_time = Column(Date, nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String(255), nullable=False)
    notes = Column(String(255), nullable=True)
    access_time = Column(Date, nullable=True)


