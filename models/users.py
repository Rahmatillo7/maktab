from sqlalchemy import Column,String,Integer
from db import Base

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(255),nullable=False)
    username = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    token = Column(String(255),nullable=True)
    address = Column(String(255),nullable=False)
    number = Column(Integer,nullable=False)
    email = Column(String(255),nullable=True)
    role = Column(String(255),nullable=False)