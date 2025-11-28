from sqlalchemy.orm import Session
import models, schemas

def create_metadata(db: Session, metadata: schemas.MetadataCreate):
    from main import MetadataModel
    check_row = db.query(MetadataModel).filter(MetadataModel.GameID == metadata.GameID).first()
    if check_row:
        db.delete(check_row)
    db_metadata = MetadataModel(GameID=metadata.GameID, GameName=metadata.GameName, LastModified=metadata.LastModified, DeviceID=metadata.DeviceID)
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata

def create_uploadrequest(db: Session, uploadrequest: schemas.UploadRequestCreate):
    from main import UploadRequestModel
    db_uploadrequest = UploadRequestModel(DeviceID=uploadrequest.DeviceID, Operation=uploadrequest.Operation, GameID=uploadrequest.GameID, Completed=uploadrequest.Completed, TimeStamp=uploadrequest.TimeStamp)
    db.add(db_uploadrequest)
    db.commit()
    db.refresh(db_uploadrequest)
    return db_uploadrequest

def create_downloadrequest(db: Session, downloadrequest: schemas.DownloadRequestCreate):
    from main import DownloadRequestModel
    db_downloadrequest = DownloadRequestModel(DeviceID=downloadrequest.DeviceID, Operation=downloadrequest.Operation, GameID=downloadrequest.GameID, Completed=downloadrequest.Completed, TimeStamp=downloadrequest.TimeStamp)
    db.add(db_downloadrequest)
    db.commit()
    db.refresh(db_downloadrequest)
    return db_downloadrequest