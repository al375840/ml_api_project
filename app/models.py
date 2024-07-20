from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SimpleModel(Base):
    __tablename__ = "simple_model"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Integer)