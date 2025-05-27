from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Mavzular(Base):
    __tablename__ = "mavzular"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    text = Column(Integer,nullable=False)


    fan_id = Column(Integer, ForeignKey("fanlar.id"), nullable=False)

    fan = relationship("Fanlar", back_populates="mavzular")
