from sqlalchemy.orm import Session
import models, schemas
from models import create_dynamic_localmetadata

def create_localmetadata(db: Session, localmetadata: schemas.LocalMetadataCreate):
    from main import LocalMetadataModel
    check_row = db.query(LocalMetadataModel).filter(LocalMetadataModel.GameID == localmetadata.GameID).first()
    if check_row:
        db.delete(check_row)
    db_localmetadata = LocalMetadataModel(GameID=localmetadata.GameID, GameName=localmetadata.GameName, LastModified=localmetadata.LastModified, DeviceID=localmetadata.DeviceID)
    db.add(db_localmetadata)
    db.commit()
    db.refresh(db_localmetadata)
    return db_localmetadata

def create_uploadrequest(db: Session, uploadrequest: schemas.UploadRequestCreate):
    from main import UploadRequestModel
    db_uploadrequest = UploadRequestModel(DeviceID=uploadrequest.DeviceID, Operation=uploadrequest.Operation, GameID=uploadrequest.GameID, Completed=uploadrequest.Completed, TimeStamp=uploadrequest.TimeStamp)
    db.add(db_uploadrequest)
    db.commit()
    db.refresh(db_uploadrequest)
    return db_uploadrequest