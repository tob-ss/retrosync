from sqlalchemy.orm import Session
from sqlalchemy import and_
import models, schemas


def create_metadata(db: Session, metadata: schemas.MetadataCreate, hash: int):
    from main import MetadataModel
    db_metadata = MetadataModel(Hash=hash, LID=metadata.LID, GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID, Cloud=metadata.Cloud)
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata

def create_metadata_cloud(db: Session, metadata: schemas.MetadataCreate, hash: int):
    from main import MetadataModel
    db_metadata = MetadataModel(Hash=hash,LID=metadata.LID, GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID, Cloud=metadata.Cloud)
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

def create_daemonstatus(db: Session, daemonstatus: schemas.DaemonStatusCreate):
    from main import DaemonStatusModel
    check_row = db.query(DaemonStatusModel).filter(DaemonStatusModel.DeviceID == daemonstatus.DeviceID).first()
    #print(check_row)
    if check_row:
        db.delete(check_row)
    db_daemonstatus = DaemonStatusModel(DeviceID=daemonstatus.DeviceID, LastOnline=daemonstatus.LastOnline)
    db.add(db_daemonstatus)
    db.commit()
    db.refresh(db_daemonstatus)
    return db_daemonstatus
