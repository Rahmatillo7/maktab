from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Fanlar(Base):
    __tablename__ = 'fanlar'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nomi = Column(String(255), nullable=False)


    mavzular = relationship("Mavzular", back_populates="fan")
    about = relationship("About", back_populates="fan", uselist=False)

    def __str__(self):
        return self.nomi
