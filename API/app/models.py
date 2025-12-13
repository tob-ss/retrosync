from sqlalchemy import Column, String, create_engine, ARRAY, Numeric, Integer, Boolean, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
from database import Base

def create_dynamic_metadata(customer_prefix):
    class MetadataModel(Base):
        __tablename__ = f"{customer_prefix}_metadata"
        
        ID = Column(Integer, primary_key=True, index=True)
        Hash = Column(String(255), nullable=False)
        LID = Column(String(2), nullable=False)
        GameID = Column(String(50), nullable=False)
        GameName = Column(String(255), nullable=False)
        LastModified = Column(Numeric(20,6), nullable=False)
        DeviceID = Column(String(50), nullable=False)
        Cloud = Column(String(3), nullable=False)
    return MetadataModel

def create_dynamic_syncrequests(customer_prefix):
    class SyncRequestsModel(Base):
        __tablename__ = f"{customer_prefix}_syncrequests"
        RequestID = Column(Integer, primary_key=True, index=True)
        DeviceID = Column(String(255), nullable=False)
        Operation = Column(String(255), nullable=False)
        GameID = Column(String(255), nullable=False)
        Completed = Column(Boolean, nullable=False)
        TimeStamp = Column(Numeric(20,6), nullable=False)
    return SyncRequestsModel

def create_dynamic_daemonstatus(customer_prefix):
    class DaemonStatusModel(Base):
        __tablename__ = f"{customer_prefix}_daemonstatuses"
        DeviceID = Column(String(255), primary_key=True, nullable=False)
        LastOnline = Column(Numeric(20,6), nullable=False)
    return DaemonStatusModel