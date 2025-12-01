from sqlalchemy.orm import Session
from sqlalchemy import and_
import models, schemas

def create_metadata(db: Session, metadata: schemas.MetadataCreate):
    from main import MetadataModel
    db_metadata = MetadataModel(LID=metadata.LID, GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID, Cloud=metadata.Cloud)
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata

def create_metadata_cloud(db: Session, metadata: schemas.MetadataCreate):
    from main import MetadataModel
    db_metadata = MetadataModel(LID=metadata.LID, GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID, Cloud=metadata.Cloud)
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata

def create_syncrequest(db: Session, syncrequest: schemas.SyncRequestsCreate):
    from main import SyncRequestModel
    db_syncrequest = SyncRequestModel(DeviceID=syncrequest.DeviceID, Operation=syncrequest.Operation, GameID=syncrequest.GameID, Completed=syncrequest.Completed, TimeStamp=syncrequest.TimeStamp)
    db.add(db_syncrequest)
    db.commit()
    db.refresh(db_syncrequest)
    return db_syncrequest
