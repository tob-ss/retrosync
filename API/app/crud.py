from sqlalchemy.orm import Session
import models, schemas

def create_metadata(db: Session, metadata: schemas.MetadataCreate):
    from main import MetadataModel
    check_row = db.query(MetadataModel).filter(MetadataModel.LID == metadata.LID, MetadataModel.GameID == metadata.GameID).first()
    if check_row:
        db.delete(check_row)
    db_metadata = MetadataModel(LID=metadata.LID, GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID, Cloud=metadata.Cloud)
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata

def create_metadata_cloud(db: Session, metadata: schemas.MetadataCreate):
    from main import MetadataModel
    check_row = db.query(MetadataModel).filter(MetadataModel.LID == metadata.LID, MetadataModel.GameID == metadata.GameID, MetadataModel.LastModified == metadata.LastModified).first()
    print(check_row)
    if check_row:
        db.delete(check_row)
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
