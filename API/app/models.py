from sqlalchemy import Column, Integer, String, create_engine, ARRAY, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from .database import Base

def create_dynamic_localmetadata(customer_prefix):
    class LocalMetadataModel(Base):
        __tablename__ = f"{customer_prefix}-localmetadata"
        gameID = Column(String(50), primary_key=True, nullable=False)
        gameName = Column(String(255), nullable=False)
        LastModified = Column(Float(10), nullable=False)
        DeviceID = Column(String(255), nullable=False)
    return LocalMetadataModel