from sqlalchemy import Column, String, create_engine, ARRAY, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker
from database import Base

def create_dynamic_localmetadata(customer_prefix):
    class LocalMetadataModel(Base):
        __tablename__ = f"{customer_prefix}_localmetadata"
        GameID = Column(String(50), primary_key=True, nullable=False)
        GameName = Column(String(255), nullable=False)
        LastModified = Column(DECIMAL(11,10), nullable=False)
        DeviceID = Column(String(255), nullable=False)
    return LocalMetadataModel