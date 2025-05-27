from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class About(Base):
    __tablename__ = "about"
    id = Column(Integer,primary_key=True,autoincrement=True)
    text = Column(String(255),nullable=False)


    fan_id = Column(Integer, ForeignKey('fanlar.id'))

    fan = relationship("Fanlar", back_populates="about")
