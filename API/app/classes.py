from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_uploadrequest, create_dynamic_downloadrequest
import models, schemas, crud
from sqlalchemy.orm import Session

class LocalMetadataProcessor:
    def __init__(self, db: Session, localmetadata: schemas.MetadataCreate):
        self.localmetadata = localmetadata
        self.db = db

    def append_metadata(self):
        if self.localmetadata.LID == "CL":
            return crud.create_metadata_cloud(self.db, self.localmetadata)
        else:
            return crud.create_metadata(self.db, self.localmetadata)
            
class SyncRequestProcessor:
    def __init__(self, db: Session, syncrequest: schemas.SyncRequestsCreate):
        self.syncrequest = syncrequest
        self.db = db

    def append_syncrequest(self):
        return crud.create_syncrequest(self.db, self.syncrequest)