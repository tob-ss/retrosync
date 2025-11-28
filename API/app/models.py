from sqlalchemy import Column, String, create_engine, ARRAY, Numeric, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from database import Base

def create_dynamic_metadata(customer_prefix):
    class MetadataModel(Base):
        __tablename__ = f"{customer_prefix}_metadata"
        
        ID = Column(Integer, primary_key=True, index=True)
        LID = Column(String(2), nullable=False)
        GameID = Column(String(50), nullable=False)
        GameName = Column(String(255), nullable=False)
        LastModified = Column(Numeric(20,6), nullable=False)
        DeviceID = Column(String(50), nullable=False)
        Cloud = Column(String(3), nullable=False)
    return MetadataModel

def create_dynamic_uploadrequest(customer_prefix):
    class UploadRequestModel(Base):
        __tablename__ = f"{customer_prefix}_uploadrequests"
        RequestID = Column(Integer, primary_key=True, index=True)
        DeviceID = Column(String(255), nullable=False)
        Operation = Column(String(255), nullable=False)
        GameID = Column(String(255), nullable=False)
        Completed = Column(Boolean, nullable=False)
        TimeStamp = Column(Numeric(20,6), nullable=False)
    return UploadRequestModel

def create_dynamic_downloadrequest(customer_prefix):
    class DownloadRequestModel(Base):
        __tablename__ = f"{customer_prefix}_downloadrequests"
        RequestID = Column(Integer, primary_key=True, index=True)
        DeviceID = Column(String(255), nullable=False)
        Operation = Column(String(255), nullable=False)
        GameID = Column(String(255), nullable=False)
        Completed = Column(Boolean, nullable=False)
        TimeStamp = Column(Numeric(20,6), nullable=False)
    return DownloadRequestModel

def create_dynamic_daemonstatus(customer_prefix):
    class DaemonStatusModel(Base):
        __tablename__ = f"{customer_prefix}_daemonstatuses"
        RequestID = Column(Integer, primary_key=True, index=True)
        DeviceID = Column(String(255), nullable=False)
        Operation = Column(String(255), nullable=False)
        GameID = Column(String(255), nullable=False)
        Completed = Column(Boolean, nullable=False)
        TimeStamp = Column(Numeric(20,6), nullable=False)
    return DaemonStatusModel