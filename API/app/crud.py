from sqlalchemy.orm import Session
import models, schemas
from models import create_dynamic_localmetadata

def create_localmetadata(db: Session, localmetadata: schemas.LocalMetadataCreate):
    LocalMetadataModel = create_dynamic_localmetadata("test")
    db_localmetadata = LocalMetadataModel(GameID=localmetadata.GameID, GameName=localmetadata.GameName, LastModified=localmetadata.LastModified, DeviceID=localmetadata.DeviceID)
    db.add(db_localmetadata)
    db.commit()
    db.refresh(db_localmetadata)
    return db_localmetadata