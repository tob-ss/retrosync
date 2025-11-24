from sqlalchemy.orm import Session
import models, schemas
from models import create_dynamic_localmetadata

def create_localmetadata(db: Session, localmetadata: schemas.LocalMetadataCreate):
    db_localmetadata = create_dynamic_localmetadata(gameID=localmetadata.gameID, gameName=localmetadata.gameName, LastModified=localmetadata.LastModified, DeviceID=localmetadata.DeviceID)
    db.add(db_localmetadata)
    db.commit()
    db.refresh(db_localmetadata)
    return db_localmetadata